from pathlib import Path
import wave
import numpy as np
sr=32000
rng=np.random.default_rng(1510202687)
out=np.zeros((60*sr,2),np.float32)
def add(at,a,pan=0):
 n=min(len(a),len(out)-int(at*sr));idx=int(at*sr)
 if n>0:out[idx:idx+n,0]+=a[:n]*(.7-pan*.25);out[idx:idx+n,1]+=a[:n]*(.7+pan*.25)
def plink(at,f=1100,pan=0):
 t=np.arange(int(sr*.36))/sr
 a=(np.sin(2*np.pi*(f*t+260*t*t))+.3*np.sin(2*np.pi*f*2.7*t))*np.exp(-t*19)*.23
 add(at,a,pan)
def swipe(at,direction=1):
 t=np.arange(int(sr*.48))/sr;n=rng.normal(0,1,len(t));sm=np.convolve(n,np.ones(7)/7,'same')
 a=sm*np.sin(np.pi*t/.48)**2*.35
 add(at,a,direction)
 t=np.arange(int(sr*.22))/sr
 add(at+.28,np.sin(2*np.pi*(110*t-140*t*t))*np.exp(-t*25)*.35)
for i,s in enumerate([0,8,16,23,32,39,46,52]):
 swipe(s+.06,1 if i%2 else -1)
 plink(s+.65,920+i*71,-.5)
 plink(s+1.05,1340+i*43,.5)
for t in [2.2,3.6,6.2,10.4,12.6,15,18.4,20.8,25.4,27.8,30.2,34.2,36.4,41,43.5,47.8,49.8,53.8,56.2,58.1]:
 plink(t,float(rng.uniform(900,1900)),float(rng.uniform(-1,1)))
peak=np.max(np.abs(out));out*=.84/max(.84,peak)
with wave.open(str(Path(__file__).parent/'assets/efectos.wav'),'wb') as f:
 f.setnchannels(2);f.setsampwidth(2);f.setframerate(sr);f.writeframes((out*32767).astype('<i2').tobytes())
