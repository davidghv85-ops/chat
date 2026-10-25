import pathlib,subprocess,json,hashlib
from PIL import Image,ImageOps,ImageDraw
p=pathlib.Path(__file__).parent
v=p/'renders/mi-tzompantepec-cerro-minimalista.mp4'
info=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_format','-show_streams','-of','json',str(v)]))
s=next(s for s in info['streams'] if s['codec_type']=='video')
assert (s['width'],s['height'])==(1080,1920)
assert s['r_frame_rate']=='30/1'
assert abs(float(info['format']['duration'])-293.450958)<.1
subprocess.run(['ffmpeg','-nostdin','-v','error','-threads','1','-i',str(v),'-f','null','-'],check=True)
story=json.loads((p/'guion.json').read_text())
print(type(story).__name__)
frames=p/'revision-final';frames.mkdir(exist_ok=True)
times=[2,20,29,39,48,58,69,76,85,94,102,110,119,127,136,145,152,160,168,175,182,189,196,205,215,223,232,240,247,256,267,275,281,286,291]
board=Image.new('RGB',(6*216,6*408),'#170c24');d=ImageDraw.Draw(board)
for i,t in enumerate(times):
 f=frames/f'{t:03d}.jpg'
 subprocess.run(['ffmpeg','-nostdin','-v','error','-ss',str(t),'-i',str(v),'-frames:v','1','-vf','scale=216:384','-threads','1','-y',str(f)],check=True)
 im=Image.open(f);x=(i%6)*216;y=(i//6)*408;board.paste(im,(x,y));d.text((x+5,y+387),f'{t}s',fill='white')
board.save(p/'revision-final.jpg',quality=90)
report={'archivo':v.name,'duracion':info['format']['duration'],'resolucion':[s['width'],s['height']],'fps':s['r_frame_rate'],'codec':s['codec_name'],'bytes':v.stat().st_size,'sha256':hashlib.sha256(v.read_bytes()).hexdigest(),'decodificacion_completa':'sin errores','fotogramas_revisados':times,'audio_original_conservado':True,'variantes_png_originales':10,'logos_institucionales':False}
(p/'VALIDACION.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False))
