from pathlib import Path
import numpy as np,wave
from story import S,D
P=Path(__file__).parent;sr=32000;y=np.zeros((int(D*sr),2),np.float32);rng=np.random.default_rng(2026102536)
def add(at,x,pan=0):
 k=int(at*sr);n=min(len(x),len(y)-k)
 if n>0:y[k:k+n,0]+=x[:n]*(.7-pan*.2);y[k:k+n,1]+=x[:n]*(.7+pan*.2)
def camera_air(at):
 t=np.arange(int(.9*sr))/sr;n=rng.normal(0,1,len(t));n=np.convolve(n,np.ones(19)/19,'same');add(at,n*np.sin(np.pi*t/.9)**2*.19,.45)
def paper(at):
 t=np.arange(int(.22*sr))/sr;n=rng.normal(0,1,len(t));a=np.convolve(n,np.ones(4)/4,'same')*np.exp(-t*25)*np.sin(np.pi*t/.22)**2*.08;add(at,a,-.4)
def wood(at,f):
 t=np.arange(int(.20*sr))/sr;a=(np.sin(2*np.pi*f*t)+.22*np.sin(2*np.pi*f*2.73*t))*np.exp(-t*35)*.10;add(at,a)
for i,(a,b,k,_,_,_,_) in enumerate(S):
 if i:camera_air(a+.04)
 wood(a+1.13,190+(i%7)*31)
 if k in ['book','research','pots']:paper(a+max(2,(b-a)*.5))
peak=np.max(np.abs(y));y*=min(1,.28/max(peak,1e-8))
with wave.open(str(P/'assets/efectos.wav'),'wb') as w:
 w.setnchannels(2);w.setsampwidth(2);w.setframerate(sr);w.writeframes((y*32767).astype('<i2').tobytes())
