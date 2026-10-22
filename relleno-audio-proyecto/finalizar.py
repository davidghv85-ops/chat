"""Compositar el banner institucional original completo, sin editar su archivo."""
from pathlib import Path
import subprocess,hashlib,sys,shutil,json
P=Path(__file__).parent
if len(sys.argv)!=2:
 raise SystemExit('Uso: python3 finalizar.py /ruta/al/banner-original.png')
src=Path(sys.argv[1]).resolve()
if not src.is_file():raise SystemExit('Falta el archivo original del banner.')
probe=json.loads(subprocess.check_output(['ffprobe','-v','error','-select_streams','v:0','-show_entries','stream=width,height','-of','json',str(src)]))['streams'][0]
w,h=probe['width'],probe['height']
if not (6<w/h<9):raise SystemExit('La proporción del archivo no coincide con el banner horizontal. Revisar sin recortar ni deformar.')
base=P/'renders/BORRADOR-SIN-BANNER-relleno.mp4'
if not base.is_file():raise SystemExit('Primero renderiza la base con el audio original.')
dest=P/'assets'/('banner-original'+src.suffix.lower())
if src!=dest.resolve():shutil.copyfile(src,dest)
hash_before=hashlib.sha256(src.read_bytes()).hexdigest()
output=P/'renders/tzompantepec-separacion-residuos-con-audio.mp4'
# La única adaptación en la composición del video es el tamaño proporcional para que quepa completo.
subprocess.run(['ffmpeg','-nostdin','-v','error','-i',str(base),'-loop','1','-i',str(dest),'-filter_complex','[1:v]scale=1000:-2:flags=lanczos[b];[0:v][b]overlay=x=40:y=H-h-26:format=auto[v]','-map','[v]','-map','0:a','-c:v','libx264','-preset','medium','-crf','16','-threads','4','-pix_fmt','yuv420p','-c:a','copy','-t','70.861021','-movflags','+faststart','-y',str(output)],check=True)
assert hashlib.sha256(dest.read_bytes()).hexdigest()==hash_before
(P/'BANNER-INTEGRIDAD.txt').write_text(f'Banner original: {src.name}\nDimensiones: {w} × {h}\nSHA-256 original y copia: {hash_before}\nArchivo intacto. Video: ajuste proporcional, sin recorte, filtro, coloración, redibujo ni animación. Visible desde el primer hasta el último fotograma.\n')
print(output)
