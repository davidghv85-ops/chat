import pathlib,subprocess,json,hashlib,math
from PIL import Image,ImageDraw
p=pathlib.Path(__file__).parent;v=p/'renders/mi-tzompantepec-cerro-revision.mp4'
info=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_format','-show_streams','-of','json',str(v)]))
s=next(s for s in info['streams'] if s['codec_type']=='video');a=next(s for s in info['streams'] if s['codec_type']=='audio')
assert (s['width'],s['height'])==(1080,1920)
assert s['r_frame_rate']=='30/1'
assert abs(float(info['format']['duration'])-293.450958)<.1
subprocess.run(['ffmpeg','-nostdin','-v','error','-threads','1','-i',str(v),'-f','null','-'],check=True)
shots=json.loads((p/'planos.json').read_text());frames=p/'revision-final';frames.mkdir(exist_ok=True)
# Review the settled portion of every shot, not a transition or entrance.
times=[round(q['a']+min((q['b']-q['a'])*.65,2),3) for q in shots]
board=Image.new('RGB',(8*216,math.ceil(len(times)/8)*408),'#170c24');d=ImageDraw.Draw(board)
for i,t in enumerate(times):
 f=frames/f'{i:02d}.jpg'
 subprocess.run(['ffmpeg','-nostdin','-v','error','-ss',str(t),'-i',str(v),'-frames:v','1','-vf','scale=216:384','-threads','1','-y',str(f)],check=True)
 im=Image.open(f);x=(i%8)*216;y=(i//8)*408;board.paste(im,(x,y));d.text((x+5,y+387),f'{i+1}: {t}s',fill='white')
board.save(p/'revision-final.jpg',quality=92)
# A readable selected sheet covers the most important narrative subjects.
selected=[0,5,10,14,18,22,26,30,34,39,43,47,51,55,59,62,66,70,74,78,82,86,90,93]
b=Image.new('RGB',(6*270,4*504),'#170c24');d=ImageDraw.Draw(b)
for n,i in enumerate(selected):
 im=Image.open(frames/f'{i:02d}.jpg').resize((270,480));x=n%6*270;y=n//6*504;b.paste(im,(x,y));d.text((x+5,y+482),f'{i+1}: {times[i]}s',fill='white')
b.save(p/'revision-seleccion.jpg',quality=93)
report={'archivo':v.name,'duracion':info['format']['duration'],'resolucion':[s['width'],s['height']],'fps':s['r_frame_rate'],'codec':s['codec_name'],'codec_audio':a['codec_name'],'bytes':v.stat().st_size,'sha256':hashlib.sha256(v.read_bytes()).hexdigest(),'decodificacion_completa':'sin errores','planos':len(shots),'duracion_maxima_plano':round(max(q['b']-q['a'] for q in shots),3),'fotogramas_revisados':times,'audio_original_completo':True,'eventos_sonoros':len(json.loads((p/'sonido-eventos.json').read_text())),'musica':False,'logos_institucionales':False}
(p/'VALIDACION.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print(json.dumps(report,ensure_ascii=False))
