from pathlib import Path
import wave,json,subprocess
import numpy as np
from scipy.signal import butter,sosfilt
P=Path(__file__).parent;SR=24000;D=293.450958;N=round(D*SR)
rng=np.random.default_rng(20261025);trans=np.zeros((N,2),np.float32);foley=np.zeros_like(trans);music=np.zeros_like(trans);events=[]
def add(dest,at,x,pan=0,label=''):
 k=round(at*SR);n=min(len(x),N-k)
 if k<0 or n<=0:return
 dest[k:k+n,0]+=x[:n]*np.sqrt((1-pan)/2);dest[k:k+n,1]+=x[:n]*np.sqrt((1+pan)/2)
 if label:events.append({'segundo':round(at,3),'efecto':label,'capa':'transiciones' if dest is trans else ('musica' if dest is music else 'actividad')})
def noise(d,lo=100,hi=7000):return sosfilt(butter(3,[lo,hi],btype='bandpass',fs=SR,output='sos'),rng.normal(size=round(d*SR)))
def sample(name):
 raw=subprocess.check_output(['ffmpeg','-v','error','-i',str(P/'assets/sonidos'/name),'-ar',str(SR),'-ac','1','-f','f32le','-'])
 x=np.frombuffer(raw,'<f4');return x/max(float(np.max(abs(x))),.05)
samples={n:sample(n) for n in ['espada-1.wav','espada-2.wav','madera-1.wav','madera-2.wav','pasos.ogg']}
def hit(at,name,amp=.25,pan=0,speed=1):
 x=samples[name];idx=np.arange(0,len(x)-1,speed);x=np.interp(idx,np.arange(len(x)),x)*amp
 add(foley,at,x,pan,name)
def air(at,pan):
 d=.42;t=np.arange(round(d*SR))/SR;x=noise(d,300,4300)*np.sin(np.pi*t/d)**2*.15
 add(trans,at,x,pan,'barrido suave');add(trans,at+.07,x*.2,-pan)
def ceramic(at,amp=.26,pan=.15):
 d=.58;t=np.arange(round(d*SR))/SR
 x=sum(w*np.sin(2*np.pi*f*t+rng.uniform(0,6.28))*np.exp(-t*k) for f,w,k in [(820,1,16),(1657,.55,12),(2765,.35,18),(4170,.19,22)])
 x+=noise(d,1200,6500)*np.exp(-t*90)*.6;x/=np.max(abs(x))+1e-7;add(foley,at,x*amp,pan,'contacto de vasijas y comales')
def wet_clay(a,b):
 d=b-a;t=np.arange(round(d*SR))/SR
 grain=noise(d,190,4200);grain*=np.maximum(0,np.sin(2*np.pi*1.65*t))**1.4
 low=np.sin(2*np.pi*(92*t+5*np.sin(t*5)))*np.maximum(0,np.sin(2*np.pi*.8*t))**6
 x=(grain*.11+low*.023)*np.minimum(1,t/.2)*np.minimum(1,(d-t)/.2)
 add(foley,a,x,-.2,'amasado y fricción del barro húmedo')
 for at in np.arange(a+.45,b-.3,1.1):ceramic(float(at),.22,(-1)**int(at)*.2)
shots=json.loads((P/'planos.json').read_text())
for i,s in enumerate(shots):
 a,b,asset=s['a'],s['b'],s['asset']
 if i:air(a-.025,(-1)**i*.45)
 if asset in [1,20]:wet_clay(a+.5,b-.08)
 if asset in [9,10]:
  for j,at in enumerate(np.arange(a+.6,b-.15,.73)):hit(float(at),'madera-1.wav' if j%2 else 'madera-2.wav',.20,(-1)**j*.25,.93+j*.04)
 if asset in [4,10,16]:
  for j,at in enumerate(np.arange(a+.55,b-.1,.51)):hit(float(at),'pasos.ogg',.11,(-1)**j*.3,.93)
 if asset in [12,18]:
  d=.48;t=np.arange(round(d*SR))/SR;add(foley,a+.9,noise(d,900,6500)*np.sin(np.pi*t/d)**2*.10,-.2,'paso de página')
# Clearly distinct combat layers: actual CC0 sword/wood/footstep samples, not transition sounds.
for a,b in [(98.35,113.75),(115.0,122.7),(155.9,164.0),(208.0,217.3)]:
 at=a+.25;j=0
 while at<b-1.0:
  hit(at,'espada-1.wav' if j%3==0 else 'espada-2.wav',.28 if j%3 else .23,(-1)**j*.45,.85+(j%4)*.07)
  hit(at+.31,'madera-1.wav',.19,(-1)**(j+1)*.3,.83)
  hit(at+.61,'pasos.ogg',.10,(-1)**j*.25,.9)
  at+=float(rng.uniform(.95,1.55));j+=1
# Distant hoof-like clops stay specific to the horse passages.
for s in shots:
 if s['asset']==13:
  for at in np.arange(s['a']+.6,s['b']-.4,.65):
   hit(float(at),'madera-2.wav',.13,-.15,.68);hit(float(at)+.17,'madera-1.wav',.09,.25,.75)
# Original low-level pentatonic breath-flute / skin-and-wood percussion / seed-rattle cue.
# It is contemporary inspired scoring, not a claim of reconstructed Mexica music.
B=60/72
notes=[293.665,349.228,391.995,440,523.251,587.330]
patterns=[[0,2,3,2,1,0],[2,3,4,3,2,0],[0,1,2,4,3,2],[3,2,1,0,2,0]]
def flute(at,f,d=1.6):
 t=np.arange(round(d*SR))/SR;env=np.minimum(1,t/.19)*np.minimum(1,(d-t)/.36)
 phase=2*np.pi*f*(t+.00035*np.sin(2*np.pi*4.7*t))
 x=(np.sin(phase)+.19*np.sin(2*phase)+.06*np.sin(3*phase))*.043
 x+=noise(d,1300,5500)*.011
 add(music,at,x*env,.13,'flauta de inspiración prehispánica')
for phrase in range(int(D/(16*B))+1):
 base=phrase*16*B
 for j,n in enumerate(patterns[phrase%4]):
  at=base+np.array([1,3,6,9,11,13])[j]*B
  if at<D-2:flute(float(at),notes[n],float([1.45,1.8,1.2][j%3]))
for beat in range(int(D/B)):
 at=beat*B
 if beat%4 in [0,2]:
  d=.45;t=np.arange(round(d*SR))/SR;f=102 if beat%4==0 else 173
  x=(np.sin(2*np.pi*(f*t+11*t*np.exp(-t*14)))+.24*np.sin(2*np.pi*f*1.59*t))*np.exp(-t*12)*.044
  x+=noise(d,300,1800)*np.exp(-t*55)*.018;add(music,at,x,-.15,'percusión de piel y madera')
 if beat%2==1:
  d=.19;t=np.arange(round(d*SR))/SR;add(music,at,noise(d,2200,8500)*np.exp(-t*24)*.023,.25,'sonaja')
fade=np.minimum(1,np.arange(N)/SR/2)*np.minimum(1,(D-np.arange(N)/SR)/3);music*=fade[:,None]
# Normalize music by its own RMS, so louder effects never reduce battle/pottery audibility.
music*=.0112/max(float(np.sqrt(np.mean(music*music))),1e-6)
for dest in [foley,trans]:
 for delay,g in [(.051,.09),(.099,.04)]:
  k=round(delay*SR);dest[k:]+=dest[:-k,::-1]*g
foley*=1.85
for name,x in [('transiciones.wav',trans),('actividad.wav',foley),('musica-inspiracion-prehispanica.wav',music)]:
 with wave.open(str(P/'assets'/name),'wb') as w:w.setnchannels(2);w.setsampwidth(2);w.setframerate(SR);w.writeframes((np.clip(x,-.95,.95)*32767).astype('<i2').tobytes())
(P/'sonido-eventos.json').write_text(json.dumps(events,ensure_ascii=False,indent=2))
subprocess.run(['ffmpeg','-nostdin','-v','error','-y','-i',str(P/'assets/audio-original.wav'),'-i',str(P/'assets/transiciones.wav'),'-i',str(P/'assets/actividad.wav'),'-i',str(P/'assets/musica-inspiracion-prehispanica.wav'),'-filter_complex','[0:a]volume=0.76,pan=stereo|c0=c0|c1=c0[v];[v][1:a][2:a][3:a]amix=inputs=4:duration=first:normalize=0,alimiter=limit=0.89:level=0:latency=1[a]','-map','[a]','-ar',str(SR),'-c:a','pcm_s16le',str(P/'assets/mezcla.wav')],check=True)
report={}
for name,x in [('transiciones',trans),('actividad',foley),('musica',music)]:
 report[name]={'RMS_dBFS':round(float(20*np.log10(np.sqrt(np.mean(x*x))+1e-9)),2),'pico_dBFS':round(float(20*np.log10(np.max(abs(x))+1e-9)),2)}
 for a,b in [(65.2,68.44),(98.35,113.75)]:
  q=x[round(a*SR):round(b*SR)];report[name][f'RMS_{a}_{b}']=round(float(20*np.log10(np.sqrt(np.mean(q*q))+1e-9)),2)
(P/'NIVELES-SONIDO.json').write_text(json.dumps(report,ensure_ascii=False,indent=2));print(json.dumps(report,ensure_ascii=False));print(len(events),'eventos')
