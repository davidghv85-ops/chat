from pathlib import Path
import numpy as np,wave
sr=32000;D=70.861021;rng=np.random.default_rng(22102026)
y=np.zeros((int(sr*D),2),np.float32)
def add(at,x,pan=0):
 k=int(at*sr);n=min(len(x),len(y)-k)
 if n>0:y[k:k+n,0]+=x[:n]*(.7-pan*.3);y[k:k+n,1]+=x[:n]*(.7+pan*.3)
def whoosh(at,pan=0):
 t=np.arange(int(sr*.38))/sr;n=rng.normal(0,1,len(t));n=np.convolve(n,np.ones(11)/11,'same')
 add(at,n*np.sin(np.pi*t/.38)**2*.35,pan)
def click(at,f=360):
 t=np.arange(int(sr*.14))/sr
 add(at,(np.sin(2*np.pi*(f*t-200*t*t))+.3*rng.normal(0,1,len(t)))*np.exp(-t*40)*.35)
def pop(at,f=950):
 t=np.arange(int(sr*.22))/sr;add(at,np.sin(2*np.pi*(f*t+120*t*t))*np.exp(-t*25)*.22)
starts=[0,4.7,9.5,17.36,22.74,28.56,35.02,42.14,50.16,54.74,62.72]
for i,a in enumerate(starts):
 whoosh(a+.04,(-1)**i*.7);click(a+.4,200+i*37);pop(a+.8,900+i*61)
for a in [2.3,6.5,8.2,12.2,14.9,19.6,20.8,25.6,27,30,32.5,37.5,39.8,44.6,46,47.3,48.5,51.2,53,56.1,59.3,64.1,66.5,68.6]:pop(a,float(rng.uniform(700,1200)))
with wave.open(str(Path(__file__).parent/'assets/efectos.wav'),'wb') as f:
 f.setnchannels(2);f.setsampwidth(2);f.setframerate(sr);f.writeframes((np.clip(y,-.8,.8)*32767).astype('<i2').tobytes())
