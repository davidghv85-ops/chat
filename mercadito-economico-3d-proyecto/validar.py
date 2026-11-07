from pathlib import Path
import json,subprocess,hashlib
import numpy as np
from PIL import Image
P=Path(__file__).parent;mp=P/'renders/mercadito-economico-3d.mp4'
info=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_format','-show_streams','-of','json',str(mp)]));v=next(s for s in info['streams'] if s['codec_type']=='video');assert (v['width'],v['height'])==(1080,1920);assert abs(float(info['format']['duration'])-44.810958)<.08

def read(path):return np.frombuffer(subprocess.check_output(['ffmpeg','-v','error','-i',str(path),'-ar','24000','-ac','1','-f','f32le','-']),dtype=np.float32)
y=read(mp);voice=read(P/'assets/audio-original.wav');fx=read(P/'assets/efectos.wav');n=min(len(y),len(voice),len(fx));expected=voice[:n]*.72+fx[:n]*.27;corr=float(np.corrcoef(y[:n],expected)[0,1]);gain=float(np.dot(y[:n],expected)/np.dot(expected,expected));peak=float(20*np.log10(np.max(abs(y))));assert corr>.99
S=json.loads((P/'guion.json').read_text());out=P/'final-frames';out.mkdir(exist_ok=True);frames=[round((s[0]+(s[1]-s[0])*.65)*30) for s in S];select='+'.join(f'eq(n,{n})' for n in frames)
subprocess.run(['ffmpeg','-v','error','-y','-i',str(mp),'-vf',f'select={select.replace(",",chr(92)+",")},scale=540:960','-fps_mode','vfr',str(out/'%02d.jpg')],check=True)
imgs=sorted(out.glob('*.jpg'));assert len(imgs)==13
c=Image.new('RGB',(1350,3*480),'#777');vars=[]
for i,img in enumerate(imgs):
 im=Image.open(img);a=np.array(im);vars.append(float(a[:360].std()));assert vars[-1]>15;im.thumbnail((270,480));c.paste(im,((i%5)*270,(i//5)*480))
c.save(P/'FINAL-REVISION.jpg')
material_checks=[]
for idx in [3,5,8,10,11,12]:
 a=np.array(Image.open(imgs[idx]).convert('RGB')); roi=a[330:690,70:470]; mean=float(roi.mean());assert mean>110,(idx,mean);material_checks.append({'escena':idx,'luminancia_panel':mean})
produce_checks=[]
for idx in [1,2,4,6,7,9]:
 a=np.array(Image.open(imgs[idx]).convert('RGB')).astype(float);roi=a[250:800,30:510];green=((roi[:,:,1]>roi[:,:,0]*1.08)&(roi[:,:,1]>roi[:,:,2]*1.08)&(roi[:,:,1]>55));assert int(green.sum())>1000,(idx,int(green.sum()));produce_checks.append({'escena':idx,'pixeles_verdes_producto':int(green.sum())})

logo=hashlib.sha256((P/'assets/banner-original.png').read_bytes()).hexdigest();assert logo=='80cc19bec02e7b45b3b4c82f5bce37c71ded8b411b7378f9951ea3940be88629'
r={'video':{'width':v['width'],'height':v['height'],'duration':info['format']['duration'],'fps':v['r_frame_rate']},'audio':{'correlacion_mezcla':corr,'ganancia_exportada':gain,'pico_dbfs':peak},'logo_original_sha256':logo,'escenas_verificadas':len(imgs),'fotogramas_sin_pantallas_negras':min(vars)>15,'paneles_3d_verificados':material_checks,'productos_verificados':produce_checks,'contactos':json.loads((P/'CONTACTOS-CONFIRMADOS.json').read_text())};(P/'VALIDACION.json').write_text(json.dumps(r,ensure_ascii=False,indent=2));print(json.dumps(r,ensure_ascii=False,indent=2))
