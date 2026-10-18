from pathlib import Path
import numpy as np,wave,json,hashlib
R=Path(__file__).resolve().parent;sr=32000;hashes={}
for ep in json.loads((R/'catalogo.json').read_text()):
 n=ep['numero'];rng=np.random.default_rng(20261018+n*9821);out=np.zeros((sr*90,2),np.float32)
 def add(t,v,pan=0):
  st=int(t*sr);k=min(len(v),len(out)-st)
  out[st:st+k,0]+=v[:k]*np.sqrt((1-pan)/2);out[st:st+k,1]+=v[:k]*np.sqrt((1+pan)/2)
 def effect(t,kind,j):
  d=[.26,.16,.10,.34][kind];x=np.arange(int(sr*d))/sr
  if kind in [0,3]:
   v=rng.normal(0,.34,len(x));v=np.convolve(v,np.ones(5+n%9)/(5+n%9),'same');v*=np.sin(np.pi*x/d)**2
  elif kind==1:v=.3*np.sin(2*np.pi*((95+n*13)*x-60*x*x))*np.exp(-x*(20+n%8))
  else:v=(.18*np.sin(2*np.pi*(600+n*39+j*23)*x)+rng.normal(0,.05,len(x)))*np.exp(-x*(40+n%10))
  add(t,v,(-.5 if (j+n)%2 else .5))
 for i in range(10):
  for dt,k in [(.03,0),(.47,1),(.78,2),(1.05,2),(2.45,3),(2.85,2),(5.02,2)]:effect(i*9+dt,k,i)
 effect(88.7,3,20);effect(89.25,1,21)
 peak=np.max(abs(out));out*=.85/max(peak,.85)
 p=R/ep['ruta']/'assets/efectos.wav'
 with wave.open(str(p),'wb') as w:w.setnchannels(2);w.setsampwidth(2);w.setframerate(sr);w.writeframes((out*32767).astype('<i2').tobytes())
 hashes[str(n)]=hashlib.sha256(p.read_bytes()).hexdigest()
assert len(set(hashes.values()))==20
(R/'audio-sha256.json').write_text(json.dumps(hashes,indent=2));print('20 pistas originales de efectos, estéreo, 90 segundos; sin música ni voz')
