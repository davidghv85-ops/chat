from pathlib import Path
import json,wave,subprocess
import numpy as np
from scipy.signal import butter,sosfilt
P=Path(__file__).parent;SR=24000;D=293.450958
rng=np.random.default_rng(220261025);y=np.zeros((round(D*SR),2),np.float32);events=[]
def add(at,x,pan=0,label=''):
 k=int(at*SR);n=min(len(x),len(y)-k)
 if k<0 or n<=0:return
 y[k:k+n,0]+=x[:n]*np.sqrt((1-pan)/2);y[k:k+n,1]+=x[:n]*np.sqrt((1+pan)/2)
 if label:events.append({'segundo':round(at,3),'efecto':label})
def noise(d,lo=120,hi=7000):
 n=rng.normal(size=round(d*SR));return sosfilt(butter(3,[lo,hi],btype='bandpass',fs=SR,output='sos'),n)
def whoosh(at,typ=0):
 d=.52;t=np.arange(round(d*SR))/SR
 w=noise(d,220+typ*70,4200)*np.sin(np.pi*t/d)**2*.31
 add(at,w,-.5+typ*.25,'transición de aire estéreo')
 add(at+.13,w*.32,.6)
 # Dry, restrained landing, not a melodic note.
 impact(at+.30,'wood',.10)
def impact(at,kind='metal',amp=.15,pan=0):
 d=.8 if kind=='metal' else .28;t=np.arange(round(d*SR))/SR
 if kind=='metal':
  freqs=[790,1213,1741,2429,3183,4259];x=sum(np.sin(2*np.pi*f*t+rng.uniform(0,6.28))*np.exp(-t*(6+i*2))/(1+i*.6) for i,f in enumerate(freqs));x+=noise(d,1300,8000)*np.exp(-t*55)*.7
 elif kind=='clay':
  x=(np.sin(2*np.pi*233*t)+.43*np.sin(2*np.pi*641*t))*np.exp(-t*24)+noise(d,200,2300)*np.exp(-t*60)*.5
 elif kind=='hoof':
  x=(np.sin(2*np.pi*160*t)+.55*np.sin(2*np.pi*440*t))*np.exp(-t*45)+noise(d,220,3500)*np.exp(-t*65)*.7
 else:x=noise(d,100,2900)*np.exp(-t*40)+np.sin(2*np.pi*125*t)*np.exp(-t*28)*.6
 x=x/(np.max(np.abs(x))+1e-6)*amp
 add(at,x,pan,{'metal':'choque tenue de escudos','clay':'toque de cerámica','hoof':'cascos sobre tierra','wood':'golpe de madera'}[kind])
def step(at,amp=.09,pan=0):
 d=.18;t=np.arange(round(d*SR))/SR;x=noise(d,90,3600)*np.exp(-t*25)*(.5+.5*np.sin(np.pi*t/d));add(at,x*amp,pan,'pasos y tierra')
def rustle(at,d=.6,amp=.08,label='roce de papel y tela'):
 t=np.arange(round(d*SR))/SR;x=noise(d,600,6500)*np.sin(np.pi*t/d)**2*amp;add(at,x,-.25,label)
def environment(a,b,kind):
 n=round((b-a)*SR);t=np.arange(n)/SR
 env=np.minimum(1,t/.8)*np.minimum(1,(b-a-t)/.8)
 if kind=='water':x=noise(b-a,160,5000)*(.7+.2*np.sin(2*np.pi*.6*t))*.028
 else:x=noise(b-a,90,1300)*(.7+.15*np.sin(2*np.pi*.31*t))*.024
 add(a,x*env,0,'agua y trabajo naval' if kind=='water' else 'aire del paisaje')
shots=json.loads((P/'planos.json').read_text())
for i,s in enumerate(shots):
 if i:whoosh(max(0,s['a']-.05),i%4)
 asset=s['asset'];a=s['a']
 if asset==1:
  impact(a+1.0,'clay',.17,-.2);rustle(a+1.7,.6,.10,'manos trabajando barro')
 if asset in [12,18]:rustle(a+.85,.45,.15)
 if asset in [9,10]:
  impact(a+1.0,'wood',.12,-.2);impact(a+1.7,'wood',.10,.25)
 if asset in [4,10]:
  for j in range(4):step(a+.65+j*.5,.09,(-1)**j*.35)
 if asset==13:
  for j in range(4):
   impact(a+.7+j*.62,'hoof',.12,-.3);impact(a+.87+j*.62,'hoof',.09,.25)
# Distinct battle beds only under the voiced conflict passages. No guns/explosions.
for a,b in [(98.4,122.7),(141.8,148.6),(155.9,164),(208.4,216.9)]:
 environment(a,b,'wind')
 at=a+.4
 while at<b-.8:
  impact(at,'metal',rng.uniform(.065,.105),rng.uniform(-.6,.6))
  step(at+.25,.065,rng.uniform(-.6,.6));at+=rng.uniform(1.1,2.2)
 for at in np.arange(a+.8,b-1,1.9):
  impact(float(at),'hoof',.07,-.35);impact(float(at)+.15,'hoof',.06,.35)
environment(0,25.8,'wind');environment(42.3,71.5,'wind');environment(192.7,217.4,'water');environment(271.1,D,'wind')
peak=float(np.max(np.abs(y)));y*=min(1,.48/max(peak,1e-8))
# Tiny room reflections help the effects feel spatial without washing out speech.
for delay,g in [(.047,.14),(.091,.075)]:
 k=round(delay*SR);y[k:]+=y[:-k,::-1]*g
with wave.open(str(P/'assets/efectos.wav'),'wb') as w:
 w.setnchannels(2);w.setsampwidth(2);w.setframerate(SR);w.writeframes((np.clip(y,-.95,.95)*32767).astype('<i2').tobytes())
(P/'sonido-eventos.json').write_text(json.dumps(events,ensure_ascii=False,indent=2))
subprocess.run(['ffmpeg','-nostdin','-v','error','-y','-i',str(P/'assets/audio-original.wav'),'-i',str(P/'assets/efectos.wav'),'-filter_complex','[0:a]volume=0.76,pan=stereo|c0=c0|c1=c0[v];[1:a]volume=1.15[f];[v][f]amix=inputs=2:duration=first:normalize=0,alimiter=limit=0.89:level=0:latency=1[a]','-map','[a]','-ar',str(SR),'-c:a','pcm_s16le',str(P/'assets/mezcla.wav')],check=True)
print(len(events),'eventos sonoros, mezcla estéreo terminada')
