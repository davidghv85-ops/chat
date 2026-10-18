from pathlib import Path
import json,os,subprocess,concurrent.futures,threading
R=Path(__file__).resolve().parent;eps=json.loads((R/'catalogo.json').read_text());lock=threading.Lock();states={str(e['numero']):{'estado':'pendiente'} for e in eps};env=dict(os.environ,npm_config_cache='/tmp/npm-cache',HYPERFRAMES_BROWSER_PATH='/usr/bin/chromium')
def status(n,value,**kw):
 with lock:states[str(n)].update(estado=value,**kw);(R/'estado.json').write_text(json.dumps(states,ensure_ascii=False,indent=2));print(n,value,flush=True)
def run(e):
 n=e['numero'];p=R/e['ruta'];v=p/'renders'/f'mi-tzompantepec-{n:02}-90s.mp4';v.parent.mkdir(exist_ok=True)
 try:
  status(n,'validando')
  with (p/'check.log').open('w') as f:c=subprocess.run(['npm','run','check','--','--at','4,22,40,58,85','--snapshots'],cwd=p,env=env,stdout=f,stderr=subprocess.STDOUT)
  if c.returncode:status(n,'error de validación');return
  status(n,'renderizando')
  for attempt in range(2):
   with (p/'render.log').open('w') as f:c=subprocess.run(['npm','run','render','--','--output',str(v),'--quality','high','--fps','30','--workers','2'],cwd=p,env=env,stdout=f,stderr=subprocess.STDOUT)
   if not c.returncode:break
   if 'render_cancelled_parent_exited' not in (p/'render.log').read_text():break
   status(n,'reanudando exportación interrumpida')
  if c.returncode:status(n,'error de render');return
  status(n,'verificando')
  j=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration,size:stream=codec_name,width,height,r_frame_rate','-of','json',str(v)]));assert abs(float(j['format']['duration'])-90)<.01;assert any(x.get('width')==1080 and x.get('height')==1920 and x.get('r_frame_rate')=='30/1' for x in j['streams']);assert any(x.get('codec_name')=='aac' for x in j['streams'])
  with (p/'decode.log').open('w') as f:c=subprocess.run(['ffmpeg','-nostdin','-v','error','-threads','1','-i',str(v),'-f','null','-'],stdout=f,stderr=subprocess.STDOUT)
  assert c.returncode==0 and (p/'decode.log').stat().st_size==0
  subprocess.run(['ffmpeg','-nostdin','-v','error','-ss','4','-i',str(v),'-vf','fps=1/9,scale=216:384,tile=5x2','-frames:v','1','-y',str(p/'renders/verificacion.jpg')],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
  (p/'verificado.json').write_text(json.dumps(j,indent=2));status(n,'listo para revisión visual',archivo=str(v))
 except Exception as ex:status(n,'fallo',detalle=str(ex))
if __name__=='__main__':
 with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:list(ex.map(run,eps))
 print('LOTE TERMINADO',flush=True)
