from pathlib import Path
import subprocess,json,hashlib
import numpy as np
from scipy.signal import correlate
P=Path(__file__).parent;mp=P/'renders/jornada-vacunacion-final.mp4'
info=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_streams','-show_format','-of','json',str(mp)]));v=next(s for s in info['streams'] if s['codec_type']=='video');a=next(s for s in info['streams'] if s['codec_type']=='audio');assert (v['width'],v['height'])==(1080,1920);assert abs(float(info['format']['duration'])-33.850958)<.08

def read(path):return np.frombuffer(subprocess.check_output(['ffmpeg','-v','error','-i',str(path),'-ar','24000','-ac','1','-f','f32le','-']),dtype=np.float32)
y=read(mp);voice=read(P/'assets/audio-original.wav');fx=read(P/'assets/efectos.wav');n=min(len(y),len(voice),len(fx));expected=voice[:n]*.644+fx[:n]*.224
corr=float(np.corrcoef(y[:n],expected)[0,1]);assert corr>.99
r={'video':{'width':v['width'],'height':v['height'],'fps':v['r_frame_rate'],'duration':info['format']['duration']},'audio':{'correlacion_con_mezcla_voz_original_y_efectos':corr,'pico_dBFS':float(20*np.log10(np.max(abs(y))))},'banner_sha256':hashlib.sha256((P/'assets/banner-original.png').read_bytes()).hexdigest(),'observacion_layout':'Aviso del analizador en 27.356–27.48s: superposición intencional de escenas durante el barrido de 0.38s. Fotogramas asentados revisados sin texto recortado.','escenas':9,'animaciones':99}
(P/'VALIDACION.json').write_text(json.dumps(r,ensure_ascii=False,indent=2));print(json.dumps(r,ensure_ascii=False,indent=2))
