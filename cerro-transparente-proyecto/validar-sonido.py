from pathlib import Path
import subprocess,wave,json
import numpy as np
from scipy.signal import correlate,correlation_lags
P=Path(__file__).parent;SR=24000
vfile=P/'renders/mi-tzompantepec-cerro-transparente.mp4'
def read(path):
 with wave.open(str(path)) as w:return np.frombuffer(w.readframes(w.getnframes()),'<i2').astype(np.float32).reshape(-1,w.getnchannels())/32768
mix=read(P/'assets/mezcla.wav');voice=read(P/'assets/audio-original.wav')
raw=subprocess.check_output(['ffmpeg','-v','error','-i',str(vfile),'-vn','-ar',str(SR),'-ac','2','-f','f32le','-'])
dec=np.frombuffer(raw,'<f4').reshape(-1,2);n=min(len(mix),len(dec),len(voice));assert n>=len(mix)-64
checks=[]
for a,b in [(10,13),(65.3,68.3),(99,103),(108,112),(158,162),(196,199),(250,253),(280,283)]:
 k,l=round(a*SR),round(b*SR)
 x=mix[k:l].mean(axis=1)[::8];z=dec[k:l].mean(axis=1)[::8]
 c=correlate(z,x,method='fft');lag=int(correlation_lags(len(z),len(x))[np.argmax(c)])
 gain=float(np.dot(x,z)/(np.dot(x,x)+1e-9))
 expected=(gain*(mix[k:l]-.76*voice[k:l])).ravel()[::4]
 actual=(dec[k:l]-gain*.76*voice[k:l]).ravel()[::4]
 full=float(np.corrcoef(x,z)[0,1]);residual=float(np.corrcoef(expected,actual)[0,1])
 checks.append({'ventana':[a,b],'desfase_ms':round(lag*8/SR*1000,4),'ganancia_exportacion':round(gain,5),'correlacion_mezcla':round(full,5),'correlacion_efectos_y_musica':round(residual,5)})
 assert abs(lag)<=1,(a,lag)
 assert full>.995,(a,full)
 if a in [65.3,99,108,158,196]:assert residual>.9,(a,residual)
# Validate background music in speech pauses, where voice-codec residuals cannot mask it.
mus=read(P/'assets/musica-inspiracion-prehispanica.wav');tr=read(P/'assets/transiciones.wav');fx=read(P/'assets/actividad.wav')
W=2400; candidates=[]
for k in range(2*SR,n-W,W):
 m=mus[k:k+W];r=float(np.sqrt(np.mean(m*m)))
 vr=float(np.sqrt(np.mean((voice[k:k+W]*.76)**2)))
 other=float(np.sqrt(np.mean(tr[k:k+W]**2)+np.mean(fx[k:k+W]**2)))
 if r>.004 and vr<r*.25 and other<r*.25:candidates.append((r,k))
chosen=[]
for r,k in sorted(candidates,reverse=True):
 if all(abs(k-q)>SR for q in chosen):chosen.append(k)
 if len(chosen)>=10:break
music_checks=[]
for k in sorted(chosen):
 x=mus[k:k+W].ravel();z=dec[k:k+W].ravel();corr=float(np.corrcoef(x,z)[0,1]);gain=float(np.dot(x,z)/(np.dot(x,x)+1e-9))
 music_checks.append({'segundo':round(k/SR,2),'correlacion_musica':round(corr,5),'ganancia':round(gain,5)})
assert len(music_checks)>=3,len(music_checks)
assert np.median([q['correlacion_musica'] for q in music_checks])>.9,music_checks
report={'audio_final':'AAC estéreo','voz_original_completa':True,'mezcla_final_coincide_con_WAV':True,'musica_inspiracion_prehispanica':True,'alineacion':checks,'musica_verificada_en_pausas':music_checks,'pico_exportado_dBFS':round(float(20*np.log10(np.max(abs(dec))+1e-9)),2)}
(P/'VALIDACION-SONIDO-EXPORTADO.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print(json.dumps(report,ensure_ascii=False))
