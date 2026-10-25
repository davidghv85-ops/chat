from pathlib import Path
import ast,json,hashlib
from PIL import Image
P=Path(__file__).parent
A=next(ast.literal_eval(n.value) for n in ast.parse((P/'build.py').read_text()).body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='assets' for t in n.targets))
report=[];missing=[]
for key,name in A.items():
 f=P/'assets/ilustraciones'/f'{name}.png'
 if not f.exists():missing.append(name);continue
 im=Image.open(f);assert im.mode=='RGBA',(name,im.mode)
 h=im.getchannel('A').histogram();assert h[0]>im.width*im.height*.04,name
 report.append({'id':key,'archivo':f.name,'dimensiones':im.size,'modo':im.mode,'fraccion_transparente':round(h[0]/(im.width*im.height),3),'bbox_contenido':im.getchannel('A').getbbox(),'sha256':hashlib.sha256(f.read_bytes()).hexdigest()})
print(len(report),'de',len(A),'PNG individuales listos. Faltan:',missing)
if not missing:(P/'TRANSPARENCIA.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
assert 'background-position' not in (P/'index.html').read_text()
assert 'foreground-object' not in (P/'index.html').read_text()
assert 'Chichimecateútli' not in (P/'index.html').read_text()
