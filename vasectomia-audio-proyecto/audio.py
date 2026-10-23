from pathlib import Path
import numpy as np,wave
sr=32000;D=76.450958;rng=np.random.default_rng(2310202663)
y=np.zeros((int(sr*D),2),np.float32)
def add(at,a,pan=0):
 k=int(at*sr);n=min(len(a),len(y)-k)
 if n>0:y[k:k+n,0]+=a[:n]*(.7-pan*.25);y[k:k+n,1]+=a[:n]*(.7+pan*.25)
def sweep(at):
 t=np.arange(int(.42*sr))/sr;n=rng.normal(0,1,len(t));a=np.convolve(n,np.ones(12)/12,'same')*np.sin(np.pi*t/.42)**2*.35;add(at,a,float(rng.uniform(-.8,.8)))
def tick(at,f=1000):
 t=np.arange(int(.18*sr))/sr;add(at,np.sin(2*np.pi*(f*t+400*t*t))*np.exp(-t*34)*.25)
for i,a in enumerate([0,3.68,10.5,14.58,19.1,31.7,44.2,52.14,56.64,62.58,65.7,73.12]):
 sweep(a+.02);tick(a+.54,760+i*43)
for a in [2.2,5.4,7.1,12.2,16.7,21.2,24.32,27.88,33.8,36.82,40.34,47.8,49.4,53.2,54.4,59,60.64,63,67,70.46,74.4]:tick(a,float(rng.uniform(850,1450)))
with wave.open(str(Path(__file__).parent/'assets/efectos.wav'),'wb') as f:
 f.setnchannels(2);f.setsampwidth(2);f.setframerate(sr);f.writeframes((np.clip(y,-.8,.8)*32767).astype('<i2').tobytes())
