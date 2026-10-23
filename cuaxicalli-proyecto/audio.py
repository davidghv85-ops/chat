from pathlib import Path
import numpy as np,wave
P=Path(__file__).parent;sr=32000;D=40.530958;n=int(sr*D);rng=np.random.default_rng(20261023028);t=np.arange(n)/sr
# Diseño sonoro original: aire de cripta, resonancias no melódicas y ecos; sin canción.
noise=rng.normal(0,1,n);f=np.fft.rfftfreq(n,1/sr);spec=np.fft.rfft(noise)
mask=np.exp(-((f-500)/700)**2)*(1-np.exp(-(f/90)**2));wind=np.fft.irfft(spec*mask,n=n);wind/=max(1,np.std(wind)*8)
base=wind*.14*(.6+.25*np.sin(2*np.pi*.13*t)+.15*np.sin(2*np.pi*.21*t))
base+=.022*np.sin(2*np.pi*(49*t+.1*np.sin(t*.4)))*(.6+.4*np.sin(t*.71)**2)
base+=.012*np.sin(2*np.pi*73.4*t+np.sin(t*.29))*np.sin(t*.43)**2
out=np.stack([base,np.roll(base,321)],axis=1)
def add(at,x,pan=0):
 k=int(at*sr);m=min(len(x),len(out)-k)
 if k>=0 and m>0:out[k:k+m,0]+=x[:m]*(.7-pan*.25);out[k:k+m,1]+=x[:m]*(.7+pan*.25)
def reverb(at,x,pan=0):
 for delay,g in [(0,1),(.18,.48),(.41,.33),(.79,.21),(1.27,.12),(1.79,.06)]:add(at+delay,x*g,pan*(-1 if delay>.4 else 1))
def impact(at):
 u=np.arange(int(.7*sr))/sr;a=np.sin(2*np.pi*(78*u-21*u*u))*np.exp(-u*8)*.2
 a+=rng.normal(0,1,len(u))*np.exp(-u*20)*.06;reverb(at,a)
def chain(at):
 u=np.arange(int(.28*sr))/sr
 a=sum(np.sin(2*np.pi*q*u) for q in [1107,1763,2641,3983])*np.exp(-u*24)*.028;reverb(at,a,float(rng.uniform(-1,1)))
def creak(at):
 u=np.arange(int(1.2*sr))/sr;phase=2*np.pi*(110*u+35*u*u+3*np.sin(u*13));a=(np.sin(phase)+.4*np.sin(phase*2.37))*np.sin(np.pi*u/1.2)**2*.065
 reverb(at,a,-.4)
def drop(at):
 u=np.arange(int(.2*sr))/sr;reverb(at,np.sin(2*np.pi*(1250*u-1200*u*u))*np.exp(-u*24)*.10,.6)
for a in [0,3.7,8.7,15.82,19.36,23.14,28.5,31.82,36.98]:impact(a+.03)
for a in [1.6,6.3,10.8,13.5,17.3,21,25.3,27.4,30.1,34.7,38.5]:chain(a)
for a in [2.2,22.9,32.3]:creak(a)
for a in [4.8,11.8,18.5,26.4,35.6]:drop(a)
# Ducking por energía de voz: los ecos retroceden mientras se habla.
with wave.open(str(P/'assets/audio-original.wav'),'rb') as w:
 a=np.frombuffer(w.readframes(w.getnframes()),'<i2').astype(np.float32)/32768;a=a.reshape(-1,w.getnchannels()).mean(1);fs=w.getframerate()
 step=int(fs*.04);r=np.array([np.sqrt(np.mean(a[i:i+step]**2)) for i in range(0,len(a),step)])
env=np.interp(t,np.arange(len(r))*.04,r);duck=np.clip(.8-env*2.0,.34,.8)
out*=duck[:,None]
fade=np.minimum(1,t/.4)*np.minimum(1,(D-t)/.5);out*=fade[:,None]
peak=np.max(np.abs(out));out*=min(1,.40/max(peak,1e-6))
with wave.open(str(P/'assets/catacumbas.wav'),'wb') as w:
 w.setnchannels(2);w.setsampwidth(2);w.setframerate(sr);w.writeframes((out*32767).astype('<i2').tobytes())
