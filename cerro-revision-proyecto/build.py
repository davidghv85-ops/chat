from pathlib import Path
import json,math,html
from story import S,D
P=Path(__file__).parent
# Each group follows the audio anchors; its interior shots show wide/action/detail.
G=[
([2,19],['Mi Tzompantepec','La tierra guarda su historia']),
([19,2,18],['Memoria de generaciones','El paisaje conserva el pasado','Una historia que sigue viva']),
([2,2,19],['Cerro del Chichimecateútli','Tzompantepec, Tlaxcala','Identidad y herencia histórica']),
([17,7,17],['Señor chichimeca','Raíces en la lengua náhuatl','Autoridad y liderazgo']),
([18,3],['Antes de la llegada española','Una historia muy antigua']),
([0,0,3],['1700–1200','Primeras comunidades agrícolas','Habitar y cultivar']),
([18,3,0],['Fase Tzompantepec','Un periodo temprano','Desarrollo cultural']),
([0,1,3],['Agricultura','Cerámica','Vida en comunidad']),
([3,4],['Un territorio decisivo','La historia cambió de rumbo']),
([4,4],['1519','El encuentro de distintos pueblos']),
([4,4],['Rumbo a Tenochtitlan','Soldados y aliados indígenas']),
([5,7],['Tlaxcala y su autonomía','Frente al poder mexica']),
([5,6,5],['Primero, resistencia','Los primeros enfrentamientos','La defensa del territorio']),
([6,5,6],['Septiembre de 1519','En territorio tlaxcalteca','Jornadas de enfrentamientos']),
([2,6,2],['La memoria del cerro','El recuerdo de aquellos combates','Historia y tradición']),
([7,17,7],['Un protagonista indígena','Una figura de gran importancia','Más allá de Tlaxcala']),
([7,5,7],['Chichimecateútli','Liderazgo militar','Al frente de sus guerreros']),
([16,16],['≈10 000','Un contingente aproximado']),
([12,13],['Tradición regional','Memoria de los enfrentamientos']),
([13,13,6],['El relato de Pedro Morón','Una tradición regional','Las jornadas de guerra']),
([12,18,12],['Memoria e investigación','Los detalles siguen en estudio','Conocer y contrastar']),
([7,8],['La historia continuó','Más allá de aquellos combates']),
([8,8,7],['Negociaciones','Alianzas','Decisiones entre pueblos']),
([7,8],['Capitán de la coalición','Chichimecateútli']),
([9,10,9],['Los bergantines','Traslado de materiales','Organización y construcción']),
([10,9],['Trabajo colectivo','Trabajadores y guerreros tlaxcaltecas']),
([11,11,10],['1521','México-Tenochtitlan','Un desenlace histórico']),
([5,8,11],['Una época compleja','Resistencia y decisiones','Alianzas y consecuencias']),
([14,14,15],['Siglos de transformación','Nuevas formas de vida','Tradiciones que continúan']),
([19,1],['Raíces que permanecen','La memoria indígena']),
([2,19],['Mucho más que un cerro','Un símbolo de identidad']),
([3,16,15,19],['Generaciones conectadas','Guerreros y comunidades','Memoria compartida','Una herencia que permanece']),
([12,15,18],['Conocer para valorar','Reconocer nuestra historia','Transmitirla a quienes vienen']),
([2,19],['Testigo del tiempo','El cerro permanece']),
([2,15],['Más que un lugar en el mapa','Tzompantepec']),
([19,2,15],['Mi Tzompantepec','Una historia para transmitir','¿Qué historia del cerro conoces?'])]
assets=[('origenes',i) for i in range(4)]+[('guerreros',i) for i in range(4)]+[('alianzas',i) for i in range(4)]+[('legado',i) for i in range(4)]+[('memoria',i) for i in range(4)]
shots=[]
for g,(s,(ids,titles)) in enumerate(zip(S,G)):
 a,b,kind,oldtitle,body,p1,p2=s;n=len(ids)
 for j,(asset,title) in enumerate(zip(ids,titles)):
  x=a+(b-a)*j/n;end=a+(b-a)*(j+1)/n
  if g==5:sub='a. n. e. · Primeras comunidades agrícolas' if j==0 else 'Cultivo y asentamientos tempranos'
  elif g==17:sub='Combatientes · Cifra aproximada'
  elif g==19:sub='Relato de tradición regional'
  elif g==20:sub='Los detalles del episodio siguen en investigación'
  elif g==35:sub='Comparte tu respuesta en los comentarios' if j==2 else 'La memoria de nuestra tierra'
  else:sub=body if j==0 else ''
  shots.append(dict(a=round(x,5),b=round(end,5),asset=asset,title=title,sub=sub,group=g,pose=[p1,p2,p1,p2][j],detail=(j%2==1 and asset not in [16]),side=('right' if (g+j)%2 else 'left'),accent=asset in [4,5,6,7,13,16],num=title in ['1700–1200','1519','1521','≈10 000']))
parts=[]
for i,s in enumerate(shots):
 sheet,tile=assets[s['asset']];xp=(tile%2)*100;yp=(tile//2)*100;bgsize='200% 200%'
 single={1:'alfareros',2:'cerro',4:'espanoles',5:'guerreros-detalle',7:'comandante',9:'bergantines'}
 if s['asset'] in single and (s['detail'] or i%3!=0 or s['asset']==1):sheet=single[s['asset']];xp=yp=0;bgsize='100% 100%'
 mode='numbers' if s['num'] else '';detail='detail' if s['detail'] else '';side=s['side']; fg=3 if s['accent'] else (2 if s['asset'] in [1,12,18] else (i%2))
 # The generated contact sheets remain byte-for-byte intact; CSS selects quadrants.
 parts.append(f'''<section id="s{i}" class="shot {mode} {detail} {side}" style="opacity:{1 if i==0 else 0};z-index:{i+1}" data-layout-allow-overflow>
 <div class="window-light" data-layout-ignore></div><svg class="ribbon" viewBox="0 0 1080 1920" data-layout-ignore><path d="M-100 1580 C180 1420 1040 1410 900 1030 S250 750 610 330 S1050 100 1200 -130"/></svg>
 <div class="scene-content"><div class="copy"><h1>{html.escape(s['title'])}</h1>{'<p>'+html.escape(s['sub'])+'</p>' if s['sub'] else ''}</div><div class="hero-space"></div><div class="lower-space"></div></div>
 <div class="visual" data-layout-ignore><div class="art-camera"><div class="art" style="background-image:url(assets/ilustraciones/{sheet}.png);background-position:{xp}% {yp}%;background-size:{bgsize}"></div></div></div>
 <div class="foreground-object fg{fg}" data-layout-ignore><div style="background-position:{fg%2*100}% {fg//2*100}%"></div></div>
 <figure class="mascot" data-layout-ignore><div class="shadow"></div><img src="assets/personaje/variante-{s['pose']:02d}.png" alt="Personaje original del usuario"></figure>
 <div class="accent-dot" data-layout-ignore></div></section>''')
css='''@font-face{font-family:Manrope;src:url(assets/titulos.woff2);font-weight:600}@font-face{font-family:Manrope;src:url(assets/lectura.woff2);font-weight:400}@font-face{font-family:Dates;src:url(assets/editorial.ttf)}*{box-sizing:border-box}body{margin:0;background:#281337;color:#FFF9EF;font-family:Manrope}#root{position:relative;width:1080px;height:1920px;overflow:hidden;background:#281337}.shot{position:absolute;inset:0;overflow:hidden;background:#281337;isolation:isolate}.scene-content{width:100%;height:100%;padding:104px 74px 50px;display:flex;flex-direction:column;gap:20px;position:relative;z-index:5;pointer-events:none}.copy{flex:none;max-width:930px}.copy h1{font-size:88px;line-height:1.10;letter-spacing:-.042em;font-weight:600;margin:0;max-width:930px;text-wrap:balance;text-shadow:0 4px 25px #28133788}.copy p{font-weight:400;font-size:43px;line-height:1.3;max-width:870px;margin:26px 0 0;color:#FFF9EF}.copy p:before{content:'';display:block;width:66px;height:6px;border-radius:5px;background:#FFC52B;margin-bottom:23px}.hero-space{flex:1}.lower-space{height:420px;flex:none}.visual{position:absolute;left:0;top:430px;width:1080px;height:1080px;z-index:3;mask-image:linear-gradient(to bottom,rgba(0,0,0,0),#000 3%,#000 96%,rgba(0,0,0,0));-webkit-mask-image:linear-gradient(to bottom,rgba(0,0,0,0),#000 3%,#000 96%,rgba(0,0,0,0))}.art-camera{width:100%;height:100%;perspective:1500px}.art{width:100%;height:100%;background-size:200% 200%;background-repeat:no-repeat;transform-origin:50% 20%;will-change:transform}.detail .visual{top:440px}.mascot{position:absolute;z-index:6;bottom:36px;left:30px;width:460px;height:620px;margin:0;transform-origin:50% 90%}.mascot img{width:100%;height:100%;object-fit:contain;object-position:bottom;filter:drop-shadow(10px 15px 13px #12091f55)}.right .mascot{left:auto;right:35px}.shadow{position:absolute;left:95px;bottom:0;width:240px;height:25px;background:#10081c55;border-radius:100%;filter:blur(12px)}.window-light{position:absolute;inset:-200px;background:repeating-linear-gradient(100deg,rgba(255,216,173,0) 0 170px,rgba(255,216,173,.07) 180px 350px,rgba(255,216,173,0) 365px 550px);transform:rotate(-24deg) translate(130px,200px);filter:blur(25px);opacity:.65;z-index:0}.ribbon{position:absolute;inset:0;width:100%;height:100%;z-index:1;opacity:.65}.ribbon path{fill:none;stroke:#FF8A32;stroke-width:130;stroke-linecap:round}.numbers h1{font-family:Dates;font-size:156px;font-weight:400;color:#FFC52B;letter-spacing:-.07em}.numbers .copy{max-width:950px}.foreground-object{position:absolute;z-index:7;bottom:125px;right:-180px;width:490px;height:490px;filter:blur(1px);opacity:.9;pointer-events:none}.foreground-object>div{width:100%;height:100%;background-image:url(assets/ilustraciones/primer-plano.png);background-size:200% 200%;background-repeat:no-repeat}.right .foreground-object{right:auto;left:-180px}.fg1,.fg3{width:370px;height:370px;bottom:260px;opacity:.75}.accent-dot{position:absolute;z-index:2;left:860px;top:430px;width:18px;height:18px;border-radius:100%;background:#FFC52B;box-shadow:0 0 40px #FFC52B44}.detail .copy h1{font-size:84px}.numbers.detail .copy h1{font-size:150px}#s0 h1{font-size:103px}'''
js='''const SHOTS=DATA;const tl=gsap.timeline({paused:true});window.__timelines={main:tl};
SHOTS.forEach((s,i)=>{const q='#s'+i,d=s.b-s.a,dir=i%2?1:-1;
if(i){tl.set(q,{opacity:1},s.a);const prev='#s'+(i-1);const tr=.44;
// A coordinated push is the transition itself: outgoing remains composed until handoff.
if(i%4===0){tl.from(q,{yPercent:100,duration:tr,ease:'power3.inOut'},s.a);tl.to(prev,{yPercent:-100,duration:tr,ease:'power3.inOut'},s.a)}
else{tl.from(q,{xPercent:dir*100,duration:tr,ease:'power3.inOut'},s.a);tl.to(prev,{xPercent:-dir*100,duration:tr,ease:'power3.inOut'},s.a)}
tl.set(prev,{opacity:0},s.a+tr+.02);}
const settle=s.a+(i?.20:.12);
tl.from(q+' h1',{y:48,opacity:0,duration:.48,ease:'expo.out'},settle);
tl.from(q+' p',{x:-35,opacity:0,duration:.45,ease:'sine.out'},settle+.13);
tl.from(q+' .visual',{y:90,opacity:0,scale:.94,duration:.62,ease:'power3.out'},settle+.05);
const sc=s.detail?1.10:.94;tl.fromTo(q+' .art',{scale:sc,x:s.detail?-25:dir*-15,y:s.detail?65:10,rotation:dir*-.7},{scale:sc+.08,x:s.detail?30:dir*22,y:s.detail?35:0,rotation:dir*.7,duration:Math.max(.5,d-.42),ease:'sine.inOut',immediateRender:false},s.a+.40);
tl.from(q+' .mascot',{x:s.side==='right'?120:-120,y:35,opacity:0,scale:.94,duration:.57,ease:'back.out(1.12)'},settle+.16);
tl.to(q+' .mascot',{y:-13,rotation:dir*1,duration:Math.max(.5,d-.95),ease:'sine.inOut'},s.a+.88);
tl.from(q+' .foreground-object',{x:s.side==='right'?-210:210,scale:1.2,opacity:0,duration:.6,ease:'power2.out'},s.a+.22);
tl.to(q+' .foreground-object',{y:-28,x:s.side==='right'?40:-40,rotation:dir*-4,duration:Math.max(.5,d-.9),ease:'sine.inOut'},s.a+.85);
tl.from(q+' .accent-dot',{scale:0,duration:.35,ease:'back.out(1.6)'},s.a+.65);
tl.to(q+' .ribbon',{x:dir*25,y:-40,duration:d,ease:'sine.inOut'},s.a);
});'''.replace('DATA',json.dumps(shots,ensure_ascii=False))
(P/'index.html').write_text('<!doctype html><html lang="es"><head><meta charset="UTF-8"><style>'+css+'</style></head><body><div id="root" data-composition-id="main" data-start="0" data-duration="'+str(D)+'" data-width="1080" data-height="1920">'+''.join(parts)+'<audio id="mezcla" src="assets/mezcla.wav" data-start="0" data-duration="'+str(D)+'" data-track-index="2" data-volume="1"></audio></div><script src="assets/gsap.min.js"></script><script>'+js+'</script></body></html>')
(P/'planos.json').write_text(json.dumps(shots,ensure_ascii=False,indent=2))
print(len(shots),'planos; máximo',max(s['b']-s['a'] for s in shots))
