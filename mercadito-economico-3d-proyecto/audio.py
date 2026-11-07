from pathlib import Path
import json
import numpy as np
from scipy.io import wavfile
P=Path(__file__).parent;sr=24000;D=44.810958
x=np.zeros((round(D*sr),2));rng=np.random.default_rng(811026)
def add(at,y,pan=0):
 i=round(at*sr);n=min(len(y),len(x)-i)
 x[i:i+n,0]+=y[:n]*(1-pan*.35);x[i:i+n,1]+=y[:n]*(1+pan*.35)
S=json.loads((P/'guion.json').read_text())
for j,s in enumerate(S):
 a=s[0]+.04;t=np.arange(int(.34*sr))/sr;env=np.sin(np.pi*t/.34)**2
 noise=rng.normal(0,1,len(t));noise=np.convolve(noise,np.ones(13)/13,'same');phase=2*np.pi*(270*t-180*t*t)
 add(a,.14*noise*env+.08*np.sin(phase)*np.exp(-20*t),(-1)**j*.6)
 # soft panel-lock click, a timbre unique to this campaign
 t=np.arange(int(.16*sr))/sr
 add(a+.28,.055*np.sin(2*np.pi*1100*t)*np.exp(-60*t)+.025*rng.normal(0,1,len(t))*np.exp(-90*t))
for at in [6.8,11,16.5,25.5,28,35,38.5,42.2]:
 t=np.arange(int(.30*sr))/sr
 y=.09*np.sin(2*np.pi*640*t)*np.exp(-18*t)+.055*np.sin(2*np.pi*960*t)*np.exp(-22*t)
 y*=np.minimum(1,t*350);add(at,y)
wavfile.write(P/'assets/efectos.wav',sr,(x.clip(-1,1)*32767).astype(np.int16))
