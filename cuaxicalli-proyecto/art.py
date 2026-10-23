import math

def flower_symbol():
 p=[]
 for j,(rad,rx,ry,col,n) in enumerate([(44,20,39,'#FF792E',18),(30,14,28,'#FFC52B',16),(17,11,19,'#FF792E',12)]):
  for i in range(n):p.append(f'<ellipse cx="0" cy="{-rad}" rx="{rx}" ry="{ry}" fill="{col}" stroke="#180B32" stroke-opacity=".14" stroke-width="1.5" transform="rotate({360*i/n+j*9})"/>')
 return '<symbol id="flower" viewBox="-90 -90 180 180">'+''.join(p)+'<circle r="17" fill="#FFC52B"/><circle r="8" fill="#FF792E"/>'+''.join(f'<circle cx="{11*math.cos(i):.1f}" cy="{11*math.sin(i):.1f}" r="2.3" fill="#180B32" opacity=".3"/>' for i in range(12))+'</symbol>'
def skull_symbol():
 return '''<symbol id="skull" viewBox="-110 -120 220 250"><path d="M-72 45 C-119 12 -110 -78 -64 -101 C-27 -123 30 -123 67 -100 C116 -73 118 10 77 46 L65 94 Q0 120 -65 94Z" fill="#FFF5DE" stroke="#180B32" stroke-width="7"/><path d="M-65 58 H65 V96 Q0 116 -65 96Z" fill="#FFC52B"/><path d="M-45 64 V99 M-22 66 V104 M0 67 V106 M22 66 V104 M45 64 V99 M-65 82 Q0 97 65 82" stroke="#180B32" stroke-width="5"/><circle cx="-44" cy="-22" r="35" fill="#7135D8"/><circle cx="44" cy="-22" r="35" fill="#7135D8"/><circle cx="-44" cy="-22" r="23" fill="#180B32"/><circle cx="44" cy="-22" r="23" fill="#180B32"/><path d="M0 3 L-14 31 Q0 23 14 31Z" fill="#180B32"/><path d="M0 -60 C-30 -76 -22 -96 0 -80 C22 -96 30 -76 0 -60" fill="#FF792E"/><path d="M-82 20 Q-55 10 -40 37 M82 20 Q55 10 40 37" stroke="#FF792E" stroke-width="7" stroke-linecap="round"/><path d="M-62 -69 Q-45 -83 -28 -69 M28 -69 Q45 -83 62 -69" stroke="#7135D8" stroke-width="7" stroke-linecap="round"/>'''+''.join(f'<circle cx="{cx+30*math.cos(i*math.pi/4):.1f}" cy="{-22+30*math.sin(i*math.pi/4):.1f}" r="4" fill="#FFC52B"/>' for cx in [-44,44] for i in range(8))+'''<circle cx="-79" cy="45" r="5" fill="#7135D8"/><circle cx="79" cy="45" r="5" fill="#7135D8"/></symbol>'''
def ghost_symbol():
 return '<symbol id="ghost" viewBox="-100 -130 200 270"><path d="M-75 90 V-35 C-75 -130 75 -130 75 -35 V90 Q50 55 25 90 Q0 55 -25 90 Q-50 55 -75 90Z" fill="#FFF5DE"/><ellipse cx="-28" cy="-35" rx="12" ry="20" fill="#180B32"/><ellipse cx="28" cy="-35" rx="12" ry="20" fill="#180B32"/><ellipse cy="14" rx="14" ry="20" fill="#7135D8"/><path d="M-48 30 Q-34 42 -25 32" stroke="#FF792E" stroke-width="5" stroke-linecap="round"/></symbol>'
DEFS='<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>'+flower_symbol()+skull_symbol()+ghost_symbol()+'''<linearGradient id="mist" x1="0" x2="1"><stop stop-color="#FFF5DE" stop-opacity="0"/><stop offset=".5" stop-color="#FFF5DE" stop-opacity=".13"/><stop offset="1" stop-color="#FFF5DE" stop-opacity="0"/></linearGradient></defs></svg>'''
def use(name,x,y,size,cls='',rotation=0):
 return f'<g class="{cls}" transform="translate({x} {y}) rotate({rotation})"><use href="#{name}" x="{-size/2}" y="{-size/2}" width="{size}" height="{size}"/></g>'
def candle(x,y,s=1):
 return f'<g class="candle" transform="translate({x} {y}) scale({s})"><ellipse cy="12" rx="32" ry="9" fill="#180B32" opacity=".3"/><rect x="-19" y="-100" width="38" height="112" rx="7" fill="#FFF5DE"/><path d="M-17 -92 Q-5 -65 0 -88 T17 -92" stroke="#FFC52B" stroke-width="7"/><g class="flame"><ellipse cy="-123" rx="35" ry="45" fill="#FFC52B" opacity=".12"/><path d="M0 -160 C-40 -117 -12 -89 0 -98 C25 -110 21 -132 0 -160Z" fill="#FF792E"/><path d="M0 -141 C-19 -119 -8 -103 0 -106 C15 -110 10 -125 0 -141Z" fill="#FFC52B"/></g></g>'
def flowers_line(x1,x2,y,count=12,size=90):
 return ''.join(use('flower',x1+(x2-x1)*i/(count-1),y+7*math.sin(i*1.8),size,'bloom',i*23) for i in range(count))
def altar():
 s='<path d="M160 560 V330 Q160 40 450 40 Q740 40 740 330 V560" fill="#321955" stroke="#7135D8" stroke-width="18"/>'
 for i in range(17):
  a=math.pi+i*math.pi/16;s+=use('flower',450+290*math.cos(a),350+290*math.sin(a),96,'bloom',i*27)
 s+='<rect x="275" y="220" width="350" height="210" rx="25" fill="#FFC52B"/><rect x="292" y="237" width="316" height="176" rx="15" fill="#180B32"/>'+use('flower',450,320,150,'bloom')
 s+='<path d="M95 520 H805 V620 H95Z" fill="#FF792E"/><path d="M190 430 H710 V525 H190Z" fill="#7135D8"/><path d="M310 365 H590 V435 H310Z" fill="#FF792E"/><path d="M95 520 H805 M190 430 H710 M310 365 H590" stroke="#FFC52B" stroke-width="14"/>'
 s+=candle(230,430,.72)+candle(670,430,.72)+candle(140,520,.9)+candle(760,520,.9)
 s+=use('skull',340,466,115,'skull-move',-5)+use('skull',560,466,115,'skull-move',5)
 s+='<g class="bread"><ellipse cx="450" cy="508" rx="66" ry="35" fill="#FFC52B"/><path d="M410 489 l80 35 M490 489 l-80 35" stroke="#FFF5DE" stroke-width="14" stroke-linecap="round"/><circle cx="450" cy="485" r="15" fill="#FF792E"/></g>'
 s+=flowers_line(105,795,600,12,90)
 return s

def art(kind):
 s='<svg viewBox="0 0 900 680" xmlns="http://www.w3.org/2000/svg" fill="none" overflow="visible">'
 s+='<ellipse cx="450" cy="625" rx="375" ry="42" fill="#0B0518" opacity=".45"/>'
 if kind in ['altar','intro','final']:s+=altar()
 elif kind=='skulls':
  s+='<ellipse cx="450" cy="330" rx="320" ry="250" stroke="#7135D8" stroke-width="8" stroke-dasharray="22 20"/>'
  s+=use('skull',450,325,400,'skull-move')+use('skull',165,460,165,'skull-move',-17)+use('skull',735,460,165,'skull-move',17)
  s+=flowers_line(150,750,590,10,110)
  s+=use('ghost',160,170,150,'ghost',-10)+use('ghost',760,150,170,'ghost',12)
 elif kind=='contest':
  s+=use('skull',260,300,325,'skull-move',-8)+use('ghost',650,320,330,'ghost',8)
  s+='<path d="M450 110 v390" stroke="#7135D8" stroke-width="8" stroke-dasharray="12 20"/>'
  s+=candle(110,570)+candle(790,570)+flowers_line(200,700,590,8,105)
 elif kind=='prize':
  s+='<path d="M185 450 H715 V590 H185Z" fill="#7135D8"/><path d="M185 450 L265 390 H785 L715 450Z" fill="#FFC52B"/><path d="M715 450 L785 390 V540 L715 590Z" fill="#321955"/>'
  for i,(x,y,r) in enumerate([(300,300,-15),(450,200,0),(610,310,17)]):
   s+=f'<g class="coin" transform="translate({x} {y}) rotate({r})"><ellipse rx="91" ry="113" fill="#FF792E"/><ellipse cx="-10" rx="82" ry="106" fill="#FFC52B" stroke="#FFF5DE" stroke-width="5"/><path d="M10 -60 V60 M39 -40 Q-50 -75 -45 -10 Q-38 10 15 16 Q70 26 35 55 Q0 75 -40 45" stroke="#180B32" stroke-width="12" stroke-linecap="round"/></g>'
  s+=use('skull',110,410,145,'skull-move',-15)+use('skull',790,400,145,'skull-move',15)+flowers_line(180,720,590,8,100)
 elif kind=='theatre':
  s+='<path d="M80 595 V170 Q450 -100 820 170 V595" fill="#0B0518" stroke="#7135D8" stroke-width="22"/><path class="curtain" d="M90 150 Q230 25 430 95 Q320 300 175 580 H90Z" fill="#7135D8"/><path class="curtain" d="M810 150 Q670 25 470 95 Q580 300 725 580 H810Z" fill="#7135D8"/>'
  for i,(x,y,r) in enumerate([(250,250,-15),(650,250,15),(290,470,-8),(610,470,8)]):s+=use('skull' if i%2==0 else 'ghost',x,y,200,'mask skull-move',r)
  s+=flowers_line(120,780,610,10,86)+candle(85,590,.6)+candle(815,590,.6)
 elif kind=='family':
  s+=use('ghost',450,270,360,'ghost')+use('ghost',180,380,240,'ghost',-12)+use('ghost',720,380,240,'ghost',12)
  s+=use('skull',320,540,150,'skull-move',-10)+use('skull',580,540,150,'skull-move',10)+flowers_line(160,740,625,10,95)
 elif kind=='date':
  s+='<path d="M100 600 V260 Q100 35 300 35 Q500 35 500 260 V600" fill="#321955" stroke="#7135D8" stroke-width="18"/>'
  s+=use('skull',300,330,290,'skull-move')+use('ghost',700,270,250,'ghost',10)
  s+=candle(600,580)+candle(800,580)+flowers_line(100,800,625,12,100)
 s+=use('ghost',70,160,145,'ghost',-12)+use('ghost',830,130,150,'ghost',12)+candle(65,620,.5)+candle(835,620,.5)
 s+='<g class="smoke"><path d="M30 600 Q300 450 460 570 T870 520" stroke="url(#mist)" stroke-width="80" stroke-linecap="round"/><path d="M0 560 Q200 400 400 530 T920 440" stroke="url(#mist)" stroke-width="35" stroke-linecap="round"/></g></svg>'
 return s

def borders():
 s='<svg class="border-art" viewBox="0 0 1080 1730" xmlns="http://www.w3.org/2000/svg" fill="none" data-layout-ignore>'
 for i in range(7):
  y=100+i*230
  s+=use('flower',14,y,102,'edge-bloom',i*25)+use('flower',1066,y+65,102,'edge-bloom',i*33)
 for i in range(5):s+=use('skull',30 if i%2 else 1050,270+i*310,85,'edge-skull',-15 if i%2 else 15)
 for i in range(26):
  x=30+(i*173)%1020;y=40+(i*317)%1600
  # Most petals stay in edge zones so text remains unobscured.
  if 100<x<980:x=55 if i%2 else 1025
  s+=f'<ellipse class="petal" cx="{x}" cy="{y}" rx="7" ry="20" fill="'+('#FF792E' if i%2 else '#FFC52B')+f'" transform="rotate({i*27} {x} {y})"/>'
 s+='<path d="M0 30 Q540 140 1080 30" stroke="#FFC52B" stroke-width="4"/>'
 for i in range(7):
  x=20+i*155;col=['#7135D8','#FF792E','#FFC52B'][i%3]
  s+=f'<g class="paper" transform="translate({x} 45)"><path d="M0 0 H130 V75 L110 95 L90 75 L65 95 L40 75 L20 95 L0 75Z" fill="{col}" opacity=".8"/><path d="M22 16 H110 M22 52 H110" stroke="#180B32" stroke-width="6" stroke-dasharray="8 10"/><circle cx="65" cy="37" r="12" fill="#180B32"/></g>'
 return s+'</svg>'
