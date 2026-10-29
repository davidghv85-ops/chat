import numpy as np
from scipy.io import wavfile
from pathlib import Path
P=Path(__file__).parent; sr=24000;dur=33.850958
x=np.zeros((round(dur*sr),2));rng=np.random.default_rng(291030)
def add(at,y):
 i=round(at*sr);n=min(len(y),len(x)-i)
 x[i:i+n,0]+=y[:n];x[i:i+n,1]+=y[:n]*.94
for a in [0.2,3.15,5.65,9.8,16.12,18.8,23.2,27.08,29.8]:
 t=np.arange(int(.42*sr))/sr;env=np.sin(np.pi*t/.42)**2
 noise=rng.normal(0,1,len(t));noise=np.convolve(noise,np.ones(9)/9,'same')
 add(a,.14*noise*env+.07*np.sin(2*np.pi*(170*t-110*t*t))*np.exp(-18*t))
for j,a in enumerate([11.6,12.62,13.62,14.5,15.58,20.52,24.26,27.86]):
 t=np.arange(int(.22*sr))/sr;f=580+j*55
 add(a,.12*(np.sin(2*np.pi*f*t)+.3*np.sin(2*np.pi*f*1.5*t))*np.exp(-24*t)*np.minimum(1,t*400))
wavfile.write(P/'assets/efectos.wav',sr,(np.clip(x,-1,1)*32767).astype('int16'))
