from pathlib import Path
import json
P=Path(__file__).parent;D=135.450958
S=[
(0,3.8,'intro','TZOMPANTEPEC','Gobierno con sentido humano','',''),
(3.8,7.14,'statement','DIRECCIÓN DE','Seguridad Pública','Cerca de la ciudadanía','shield'),
(7.14,11.4,'cards','ACCIONES Y SERVICIOS','Seguridad que te acompaña','Atención · Prevención · Protección','shield'),
(11.4,15.3,'split','PROTEGEMOS','Tu familia','Salvaguardar su integridad','family'),
(15.3,19.8,'split','PROTEGEMOS','Tu patrimonio','En todo momento','lock'),
(19.8,24.3,'device','ATENCIÓN DIRECTA','¿Necesitas ayuda?','Canales para emergencias','phone'),
(24.3,28.16,'cards','COMUNICACIÓN','Canales oficiales','Emergencias · Denuncia · Atención local','phone'),
(28.16,31.94,'number','NÚMERO NACIONAL','Emergencias','911','phone'),
(31.94,36.24,'number','LÍNEA NACIONAL','Denuncia anónima','089','shield'),
(36.24,41.54,'device','RESPUESTA LOCAL','Estamos cerca de ti','Solicita apoyo de Seguridad Pública','phone'),
(41.54,48.58,'call','LLAMADAS DIRECTAS','Atención local','241 415 27 74','phone'),
(48.58,55.06,'wa','LÍNEA OFICIAL','WhatsApp','241 420 94 09','whatsapp'),
(55.06,60.5,'device','SOLICITA AUXILIO','Un contacto ágil y cercano','Llamadas y WhatsApp','phone'),
(60.5,64.35,'bank','PROGRAMA ACTIVO','Acompañamiento bancario','Prevención y apoyo','bank'),
(64.35,67.18,'statement','PROTECCIÓN','Al ciudadano','Tu tranquilidad es importante','shield'),
(67.18,70.4,'split','PREVENCIÓN','Áreas públicas','Cuidamos a las personas','family'),
(70.4,73.58,'bank','PREVENCIÓN','Zonas financieras','Seguridad cercana','bank'),
(73.58,77.3,'split','MÁS VIGILANCIA','Patrullajes incrementados','Prevención en cajeros y comercios','car'),
(77.3,80.32,'cards','SEGURIDAD','Cajeros y comercios','Mayor presencia preventiva','bank'),
(80.32,84,'bank','RESGUARDO PRESENCIAL','Cajeros automáticos','Atención en puntos clave','atm'),
(84,88.18,'panic','RESPUESTA','Botones de pánico','Integrados en puntos de alto flujo','alert'),
(88.18,91.7,'bank','ACOMPAÑAMIENTO INTEGRAL','Para tus retiros','Solicita apoyo','bank'),
(91.7,94.56,'bank','ACOMPAÑAMIENTO INTEGRAL','Y tus depósitos','Protección durante el traslado','bank'),
(94.56,97.96,'split','PRIVACIDAD','Total confidencialidad','Tu información se protege','lock'),
(97.96,103.1,'conditions','SIN MONTO MÍNIMO','Sin decir cuánto llevas','No necesitas especificar la cantidad','lock'),
(103.1,107.34,'number','DISPONIBLE','Días del año','365','calendar'),
(107.34,111.35,'statement','ANTE CUALQUIER EVENTUALIDAD','Solicita apoyo','Dirección de Seguridad Pública','shield'),
(111.35,115.2,'recap','CONTACTOS INSTITUCIONALES','Guarda estos números','Atención local y emergencias','phone'),
(115.2,120.92,'call','LLAMADAS DIRECTAS','Solicita apoyo','241 415 27 74','phone'),
(120.92,127.76,'wa','WHATSAPP OFICIAL','Estamos para ayudarte','241 420 94 09','whatsapp'),
(127.76,131.8,'split','NUESTRO COMPROMISO','Tu seguridad','Las y los ciudadanos son prioridad','family'),
(131.8,D,'recap','MÁXIMA PRIORIDAD','Tú y tu patrimonio','Seguridad Pública de Tzompantepec','shield')]
icons={
'shield':'<path d="M64 12l40 17v32c-3 28-40 49-40 49S27 89 24 61V29Z"/><path d="M44 61l14 14 28-31"/>',
'lock':'<rect x="29" y="53" width="70" height="57" rx="12"/><path d="M43 53V34a21 21 0 0 1 42 0v19M64 76v14"/>',
'family':'<circle cx="41" cy="36" r="16"/><circle cx="88" cy="37" r="16"/><circle cx="65" cy="75" r="13"/><path d="M12 99V79a29 29 0 0 1 39-26m27 1a29 29 0 0 1 38 25v20M43 115V99a22 22 0 0 1 44 0v16"/>',
'bank':'<path d="M13 42L64 13l51 29ZM18 108h92M26 47v52m25-52v52m26-52v52m25-52v52"/>',
'atm':'<rect x="27" y="12" width="74" height="104" rx="10"/><rect x="38" y="26" width="52" height="36" rx="3"/><path d="M39 76h50M48 76v25h32V76M44 49l12-12 10 9 15-15"/>',
'car':'<path d="M17 63l13-31h67l14 31M17 63h94v36H17ZM36 99v10m56-10v10M24 78h20m40 0h20M51 24h26M64 16v8"/>',
'alert':'<path d="M55 20a10 10 0 0 1 18 0l42 77a10 10 0 0 1-9 15H22a10 10 0 0 1-9-15ZM64 47v30M64 94h.1"/>',
'calendar':'<rect x="18" y="24" width="92" height="87" rx="12"/><path d="M18 48h92M42 14v20m44-20v20M42 72h12m20 0h12M42 91h12m20 0h12"/>'}
def icon(k):
 if k in ('phone','whatsapp'):return (P/'assets'/('telefono.svg' if k=='phone' else 'whatsapp.svg')).read_text()
 return '<svg viewBox="0 0 128 128" fill="none" stroke="currentColor" stroke-width="7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'+icons[k]+'</svg>'
def card(label,txt,k,cl=''):
 return f'<div class="mini enter {cl}"><span class="mini-icon">{icon(k)}</span><div><small>{label}</small><strong>{txt}</strong></div></div>'
def device(wa=False):
 return '<div class="device-wrap enter"><div class="phone-frame"><div class="speaker"></div><div class="screen-head">'+icon('whatsapp' if wa else 'phone')+'<span>Seguridad Pública</span></div><div class="screen-content"><div class="bubble b1 enter">Necesito apoyo.</div><div class="bubble b2 enter">Estamos para ayudarte.</div><div class="screen-shield enter">'+icon('shield')+'</div><div class="screen-label enter">ATENCIÓN CIUDADANA</div></div><div class="screen-bottom"></div></div><div class="device-shadow"></div></div>'
parts=[]
for i,(a,b,k,label,title,body,obj) in enumerate(S):
 text=f'<div class="copy"><div class="label enter">{label}</div><h1 class="enter">{title}</h1>'
 mid='';extra=''; light=i in (4,8,14,18,22,24,30)
 if k=='intro':
  text='<div class="intro-copy enter">TZOMPANTEPEC</div>';mid='<div class="intro-ring" data-layout-ignore></div>'
 elif k in ('call','wa'):
  text+=f'<div class="contact-panel enter {k}"><span class="contact-icon">{icon(obj)}</span><strong>{body}</strong></div><div class="sub enter">'+('Llama para solicitar apoyo' if k=='call' else 'Escríbenos para solicitar apoyo')+'</div>'
  mid=device(k=='wa')
  if i==29:extra='<div class="emergency-note enter" data-at="126.25">Emergencias <b>911</b></div>'
 elif k=='number':
  text+=f'<div class="big-number enter">{body}</div>';mid=f'<div class="monument enter">{icon(obj)}</div>'
 elif k=='recap':
  text+=f'<p class="sub enter">{body}</p>';mid='<div class="recap-grid">'+card('LLAMADAS','241 415 27 74','phone')+card('WHATSAPP','241 420 94 09','whatsapp','green')+card('EMERGENCIAS','911','phone')+card('DENUNCIA ANÓNIMA','089','shield')+'</div>'
 elif k=='cards':
  text+=f'<p class="sub enter">{body}</p>'
  vals=[('ATENCIÓN','Respuesta cercana','phone'),('PREVENCIÓN','Protección ciudadana','shield'),('APOYO','Tu patrimonio','lock')]
  if i==6:vals=[('EMERGENCIAS','911','phone'),('DENUNCIA ANÓNIMA','089','shield'),('ATENCIÓN LOCAL','Llamadas y WhatsApp','whatsapp')]
  if i==18:vals=[('PATRULLAJES','Cajeros','car'),('PRESENCIA','Comercios','bank'),('PREVENCIÓN','Protección','shield')]
  mid='<div class="cards-row">'+''.join(card(*v) for v in vals)+'</div>'
 elif k=='device':
  text+=f'<p class="sub enter">{body}</p>';mid=device()
 elif k=='conditions':
  text+=f'<p class="sub enter">{body}</p>';mid='<div class="condition-stack">'+card('ACOMPAÑAMIENTO','Sin monto mínimo','shield')+card('CONFIDENCIAL','Sin especificar la cantidad','lock')+'</div>'
 elif k=='bank':
  text+=f'<p class="sub enter">{body}</p>'
  mid=f'<div class="bank-object enter"><div class="bank-roof"></div><div class="bank-label">{icon(obj)}</div><div class="columns"><i></i><i></i><i></i><i></i></div><div class="bank-base"></div><div class="security-badge enter">{icon("shield")}</div></div>'
 elif k=='panic':
  text+=f'<p class="sub enter">{body}</p>';mid='<div class="panic-object enter"><div class="panic-ring"></div><div class="panic-button">'+icon('alert')+'</div></div>'
 else:
  text+=f'<p class="sub enter">{body}</p>';mid=f'<div class="monument enter">{icon(obj)}</div>'
 text+='</div>' if k!='intro' else ''
 parts.append(f'<section id="s{i}" class="scene {k} {"light" if light else ""}" style="opacity:{1 if i==0 else 0};z-index:{i}"><div class="scene-glow" data-layout-ignore></div><div class="beam" data-layout-ignore></div><div class="scene-content" data-layout-allow-overflow data-layout-allow-overlap>{text}{mid}{extra}</div></section>')
css='''@font-face{font-family:Civic;src:url(assets/display.ttf);font-weight:900}@font-face{font-family:Civic;src:url(assets/body.ttf);font-weight:400}*{box-sizing:border-box}body{margin:0;background:#200B36;color:#FFF9F4;font-family:Civic}#root{position:relative;width:1920px;height:1080px;overflow:hidden}#stage{position:relative;width:1920px;height:1080px;perspective:1800px;overflow:hidden}.scene{position:absolute;inset:0;background:#200B36;overflow:hidden}.scene-content{position:relative;display:flex;flex-direction:row;align-items:center;gap:80px;width:100%;height:100%;padding:92px 105px 175px;perspective:1800px}.copy{position:relative;width:980px;flex-shrink:0;z-index:2}.label{font-size:30px;font-weight:900;letter-spacing:.065em;color:#FFD342;margin-bottom:28px}h1{font-size:106px;line-height:1.04;letter-spacing:-.04em;margin:0;font-weight:900;max-width:1050px}.sub{font-size:39px;line-height:1.35;margin:35px 0 0;max-width:950px}.scene-glow{position:absolute;width:1700px;height:1300px;right:-300px;top:-130px;background:#6324AC22;border-radius:50%}.beam{position:absolute;width:190px;height:1800px;right:-20px;top:-700px;background:#6324AC;transform:rotate(-32deg);border-left:3px solid #C9A7F4}.light{background:#FFF9F4;color:#200B36}.light .label{color:#6324AC}.light .scene-glow{background:#DCC8F055}.light .beam{background:#EADCF7;border-color:#C9A7F4}.monument{position:relative;flex-shrink:0;width:530px;height:530px;border-radius:110px;background:#6324AC;box-shadow:26px 34px 0 #11051F44,0 0 0 2px #9A6ACE inset;display:flex;align-items:center;justify-content:center;color:#FFF9F4;transform:rotate(-6deg);z-index:1}.monument svg,.monument img{width:350px;height:350px}.monument img{filter:brightness(0) invert(1)}.light .monument{box-shadow:26px 34px 0 #D8C1ED}.statement .copy{width:1040px}.statement h1{font-size:120px}.statement .monument{width:460px;height:460px}.intro .scene-content{justify-content:center;align-items:flex-start;padding-top:190px}.intro-copy{font-size:47px;font-weight:900;letter-spacing:.14em;color:#C9A7F4}.intro-ring{position:absolute;left:560px;top:95px;width:800px;height:800px;border:3px solid #6324AC;border-radius:50%;box-shadow:0 0 0 70px #6324AC22,0 0 0 140px #6324AC11}.device-wrap{position:relative;width:500px;height:730px;flex-shrink:0;transform:rotate(5deg);z-index:1}.phone-frame{position:relative;width:430px;height:710px;background:#F7F2FE;border:13px solid #170620;border-radius:62px;box-shadow:14px 18px 0 #A886CD,28px 35px 42px #0005;overflow:hidden;padding:65px 17px 30px;color:#200B36}.speaker{position:absolute;top:16px;left:125px;width:150px;height:23px;background:#170620;border-radius:20px}.screen-head{display:flex;gap:13px;align-items:center;background:#6324AC;color:white;padding:20px 13px;margin:0 -17px;font-size:22px;font-weight:900}.screen-head svg,.screen-head img{width:34px;height:34px;filter:brightness(0) invert(1)}.screen-content{padding-top:26px}.bubble{font-size:26px;line-height:1.3;border-radius:17px;padding:20px;margin-bottom:20px;background:#E5D5F3;max-width:315px;box-shadow:0 5px 0 #0000000D}.b2{margin-left:35px;background:#D4EDDD}.screen-shield{width:155px;height:155px;color:#6324AC;margin:25px auto 12px}.screen-shield svg{width:100%;height:100%}.screen-label{text-align:center;font-size:16px;font-weight:900;color:#6324AC}.screen-bottom{position:absolute;width:120px;height:7px;background:#200B36;bottom:12px;left:142px;border-radius:20px}.contact-panel{display:flex;align-items:center;gap:25px;padding:32px 30px;margin-top:34px;background:#FFF9F4;color:#200B36;border-radius:27px;border:2px solid #D6BFF2;box-shadow:0 18px 0 #6324AC;white-space:nowrap}.contact-panel strong{font-size:86px;letter-spacing:-.025em;font-weight:900;font-variant-numeric:tabular-nums}.contact-icon{width:89px;height:89px;flex-shrink:0;display:flex;align-items:center;justify-content:center;background:#6324AC;border-radius:23px;color:#FFF9F4}.contact-icon svg,.contact-icon img{width:56px;height:56px;filter:brightness(0) invert(1)}.wa .contact-icon{background:#168447}.call .copy,.wa .copy{width:1110px}.call h1,.wa h1{font-size:105px}.call .device-wrap,.wa .device-wrap{transform:scale(.88) rotate(7deg);transform-origin:center}.big-number{font-size:325px;font-weight:900;line-height:1.06;letter-spacing:-.07em;color:#FFD342;margin-top:12px;font-variant-numeric:tabular-nums}.light .big-number{color:#6324AC}.number h1{font-size:83px}.number .monument{width:485px;height:485px}.cards .scene-content{flex-direction:column;align-items:flex-start;justify-content:center;gap:45px}.cards .copy{width:1600px}.cards h1{font-size:103px}.cards .sub{margin-top:18px}.cards-row{display:flex;gap:24px;width:100%}.mini{display:flex;gap:25px;align-items:center;position:relative;background:#FFF9F4;color:#200B36;border-radius:25px;padding:30px;box-shadow:0 15px 0 #6324AC;min-height:155px;flex:1}.mini-icon{display:flex;align-items:center;justify-content:center;width:88px;height:88px;background:#6324AC;color:white;border-radius:22px;flex-shrink:0}.mini-icon svg,.mini-icon img{width:57px;height:57px}.mini-icon img{filter:brightness(0) invert(1)}.mini small{display:block;font-size:20px;font-weight:900;letter-spacing:.04em;color:#6324AC;margin-bottom:12px}.mini strong{display:block;font-size:38px;line-height:1.15;letter-spacing:-.02em}.cards-row .mini{align-items:flex-start;flex-direction:column;padding:30px;min-height:265px}.green .mini-icon{background:#168447}.light .mini{background:#200B36;color:#FFF9F4;box-shadow:0 15px 0 #D4BAEC}.light .mini small{color:#C9A7F4}.recap .scene-content{gap:65px}.recap .copy{width:700px}.recap h1{font-size:92px}.recap-grid{width:940px;display:grid;grid-template-columns:1fr 1fr;gap:25px;z-index:2}.recap-grid .mini{flex-direction:column;align-items:flex-start;gap:20px;padding:26px;min-height:245px}.recap-grid .mini strong{font-size:39px;white-space:nowrap}.recap-grid .mini small{font-size:20px}.bank-object{position:relative;width:570px;height:500px;flex-shrink:0;transform:rotate(-4deg);filter:drop-shadow(15px 25px 15px #0003);margin-top:50px}.bank-roof{position:absolute;top:0;width:100%;height:170px;background:#C9A7F4;clip-path:polygon(50% 0,100% 65%,100% 100%,0 100%,0 65%)}.bank-label{position:absolute;left:225px;top:37px;color:#200B36;width:120px;height:120px}.bank-label svg{width:100%;height:100%}.columns{position:absolute;top:170px;left:35px;right:35px;height:260px;display:flex;justify-content:space-between}.columns i{display:block;width:77px;background:linear-gradient(90deg,#FFF9F4,#C9A7F4);border-radius:5px}.bank-base{position:absolute;top:430px;width:100%;height:65px;border-radius:12px;background:#C9A7F4;border-bottom:18px solid #6324AC}.security-badge{position:absolute;width:190px;height:190px;bottom:-5px;right:-45px;background:#FFD342;color:#200B36;border-radius:50%;padding:30px;box-shadow:0 12px 0 #A8790F}.security-badge svg{width:100%;height:100%}.condition-stack{display:flex;flex-direction:column;gap:30px;width:620px}.conditions .copy{width:900px}.conditions h1{font-size:99px}.condition-stack .mini strong{font-size:40px}.panic-object{width:530px;height:530px;position:relative;flex-shrink:0;display:flex;align-items:center;justify-content:center}.panic-ring{position:absolute;inset:0;border:4px solid #C9A7F4;border-radius:50%;box-shadow:0 0 0 35px #6324AC55}.panic-button{width:350px;height:350px;background:#FFD342;border-radius:50%;color:#200B36;padding:70px;box-shadow:0 28px 0 #A8790F,0 40px 30px #0005;position:relative}.panic-button svg{width:100%;height:100%}.emergency-note{position:absolute;right:135px;bottom:190px;padding:12px 26px;background:#FFD342;color:#200B36;border-radius:18px;font-size:28px;font-weight:900;z-index:4}.emergency-note b{font-size:45px;margin-left:15px}.signature{position:absolute;width:620px;height:auto;right:65px;bottom:25px;z-index:300}'''
js='''const tl=gsap.timeline({paused:true});window.__timelines={main:tl};const scenes=DATA;
tl.from('#banner',{x:-585,y:-455,scale:2.5,duration:.95,ease:'power3.inOut'},2.75);tl.from('#banner',{opacity:0,duration:.4,ease:'power2.out'},.15);
scenes.forEach((s,i)=>{const[a,b,k]=s,q='#s'+i;
if(i){tl.set(q,{opacity:1},a);if(i%4===0){tl.from(q,{y:1080,duration:.36,ease:'expo.inOut'},a)}else{tl.from(q,{x:1920,duration:.38,ease:'expo.inOut'},a)}tl.set('#s'+(i-1),{opacity:0},a+.4)}
const entries=[{y:50,opacity:0,ease:'power3.out'},{x:-80,opacity:0,ease:'expo.out'},{scale:.84,rotation:-2,opacity:0,ease:'back.out(1.1)'}];
document.querySelectorAll(q+' .enter').forEach((e,j)=>{const at=e.dataset.at?+e.dataset.at:a+.14+j*.075;tl.from(e,{...entries[j%3],duration:.48},at)});
tl.from(q+' .beam',{x:190,rotation:-8,duration:.75,ease:'expo.out'},a+.1);
tl.to(q+' .scene-glow',{x:-80,y:30,duration:b-a,ease:'sine.inOut'},a);
// Camera drift remains separate from object motion and never touches logo.
if(k!=='intro'){tl.to(q+' .copy',{x:9,scale:1.025,duration:Math.max(.3,b-a-1),ease:'sine.inOut'},a+.9)}
if(document.querySelector(q+' .monument')){tl.to(q+' .monument',{rotation:1.5,y:-18,duration:Math.max(.3,b-a-1),ease:'sine.inOut'},a+.9)}
if(document.querySelector(q+' .device-wrap')){tl.to(q+' .device-wrap',{rotation:-2,y:-15,duration:Math.max(.3,b-a-1.4),ease:'sine.inOut'},a+1.2);tl.from(q+' .phone-frame',{rotationY:-17,duration:.8,ease:'power3.out'},a+.25)}
if(document.querySelector(q+' .bank-object')){tl.to(q+' .bank-object',{rotation:2,y:-18,duration:Math.max(.3,b-a-1),ease:'sine.inOut'},a+.9);tl.from(q+' .columns i',{scaleY:0,transformOrigin:'bottom',stagger:.08,duration:.45,ease:'back.out(1.1)'},a+.4)}
if(k==='panic'){tl.to(q+' .panic-ring',{scale:1.12,duration:.8,repeat:2,yoyo:true,ease:'sine.inOut'},a+.65);tl.from(q+' .panic-button',{scale:.7,duration:.5,ease:'back.out(1.5)'},a+.4)}
if(k==='intro')tl.to(q+' .intro-ring',{scale:1.2,rotation:30,duration:3,ease:'sine.inOut'},.2);
if(k==='cards')tl.from(q+' .mini-icon',{rotation:12,scale:.75,stagger:.12,duration:.6,ease:'back.out(1.4)'},a+.55);
});'''.replace('DATA',json.dumps(S,ensure_ascii=False))
html='<!doctype html><html lang="es"><head><meta charset="utf-8"><style>'+css+'</style></head><body><div id="root" data-composition-id="main" data-width="1920" data-height="1080" data-start="0" data-duration="'+str(D)+'"><div id="stage">'+''.join(parts)+'</div><img id="banner" class="signature" src="assets/banner-original.png" alt="Logotipos institucionales originales"><audio id="voice" data-start="0" data-duration="'+str(D)+'" data-track-index="2" data-volume="0.72" src="assets/audio-original.wav"></audio><audio id="fx" data-start="0" data-duration="'+str(D)+'" data-track-index="3" data-volume="0.3" src="assets/efectos.wav"></audio></div><script src="assets/gsap.min.js"></script><script>'+js+'</script></body></html>'
(P/'index.html').write_text(html);(P/'guion.json').write_text(json.dumps(S,ensure_ascii=False,indent=2))
