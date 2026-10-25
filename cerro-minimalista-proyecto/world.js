/* Deterministic, time-addressable camera gallery. No real-time clocks or random physics. */
window.createCerroWorld=(canvas,story)=>{
 const T=THREE,M=CerroModels,SP=23,ratio=1024/1864;
 const renderer=new T.WebGLRenderer({canvas,antialias:true,alpha:false,preserveDrawingBuffer:true,powerPreference:'high-performance'});
 renderer.setPixelRatio(1);renderer.setSize(640,1165,false);renderer.outputColorSpace=T.SRGBColorSpace;renderer.toneMapping=T.ACESFilmicToneMapping;renderer.toneMappingExposure=1.12;renderer.shadowMap.enabled=true;renderer.shadowMap.type=T.PCFSoftShadowMap;renderer.shadowMap.autoUpdate=false;
 const scene=new T.Scene();scene.background=new T.Color(0x2b163d);scene.fog=new T.Fog(0x2b163d,24,70);
 const H=8.9,camera=new T.OrthographicCamera(-H*ratio,H*ratio,H,-H,.1,110);
 const hemi=new T.HemisphereLight(0xfff7eb,0x352046,2.6);scene.add(hemi);
 const key=new T.DirectionalLight(0xffffff,3.4);key.castShadow=true;key.shadow.mapSize.set(1024,1024);key.shadow.camera.left=-9;key.shadow.camera.right=9;key.shadow.camera.top=10;key.shadow.camera.bottom=-10;key.shadow.camera.near=.5;key.shadow.camera.far=40;key.shadow.normalBias=.035;key.shadow.bias=-.00025;key.shadow.radius=4;scene.add(key);scene.add(key.target);
 const fill=new T.DirectionalLight(0xffc52b,.4);fill.position.set(6,6,-6);scene.add(fill);scene.add(fill.target);
 const ground=M.mesh(new T.PlaneGeometry(SP*story.length+100,130),new T.MeshStandardMaterial({color:0x2b153c,roughness:.94,dithering:true}),SP*(story.length-1)/2,-.015,-10);ground.rotation.x=-Math.PI/2;ground.castShadow=false;ground.receiveShadow=true;scene.add(ground);
 // A softly projected window pattern, drawn procedurally as lighting on the floor.
 const texCanvas=document.createElement('canvas');texCanvas.width=1024;texCanvas.height=1024;const ctx=texCanvas.getContext('2d');ctx.filter='blur(16px)';ctx.fillStyle='rgba(255,255,255,.8)';for(let y=0;y<3;y++)for(let x=0;x<2;x++)ctx.fillRect(70+x*470,45+y*320,405,265);
 const windowTex=new T.CanvasTexture(texCanvas);windowTex.colorSpace=T.SRGBColorSpace;
 const lightPatch=new T.Mesh(new T.PlaneGeometry(14,24),new T.MeshBasicMaterial({map:windowTex,transparent:true,opacity:.24,depthWrite:false,toneMapped:false}));lightPatch.rotation.set(-Math.PI/2,0,-.36);lightPatch.position.set(0,.015,-1);lightPatch.renderOrder=1;scene.add(lightPatch);
 const groups=[],occluders=[];
 story.forEach((s,i)=>{
  const g=new T.Group();g.position.x=i*SP;
  const model=M.make(s.kind);model.rotation.y=(i%3-1)*.14;g.add(model);g.userData.model=model;
  const road=[];for(let j=0;j<=14;j++){const f=j/14;road.push([-SP/2+SP*f,.048,3.8+.9*Math.sin(f*Math.PI*2)])}const c=new T.CatmullRomCurve3(road.map(p=>new T.Vector3(...p)));const pos=[],ix=[];
  for(let j=0;j<=100;j++){let u=j/100,p=c.getPoint(u),v=c.getTangent(u),n=new T.Vector3(-v.z,0,v.x).normalize().multiplyScalar(.36);pos.push(p.x+n.x,p.y,p.z+n.z,p.x-n.x,p.y,p.z-n.z);if(j<100){let k=j*2;ix.push(k,k+2,k+1,k+1,k+2,k+3)}}
  const geo=new T.BufferGeometry();geo.setAttribute('position',new T.Float32BufferAttribute(pos,3));geo.setIndex(ix);geo.computeVertexNormals();const ribbon=M.mesh(geo,'orange');ribbon.material=new T.MeshStandardMaterial({color:0xff792e,roughness:.9,side:T.DoubleSide,dithering:true});ribbon.castShadow=false;g.add(ribbon);scene.add(g);groups.push(g);
  if(i){const o=new T.Group();const tr=M.tree(0,0,2.5);o.add(tr);o.position.set((i-.5)*SP,0,2.3);scene.add(o);occluders.push(o)}
 });
 function smooth(v){v=Math.max(0,Math.min(1,v));return v*v*(3-2*v)}
 let lastTime=-100,lastShadowIndex=-1,lastTravel=true;
 function update(t){if(t===lastTime)return;lastTime=t;
  let i=0;for(let k=1;k<story.length;k++)if(t>=story[k].a)i=k;else break;
  const s=story[i],travel=i?smooth((t-s.a)/1.12):1;
  let x=(i-(1-travel))*SP;let local=Math.max(0,t-s.a);const hold=smooth((local-1.15)/Math.max(2,(s.b-s.a)-1.15));
  const yaw=.12*Math.sin(hold*Math.PI)*((i%2)*2-1);camera.position.set(x+6.5*Math.cos(yaw)+13.8*Math.sin(yaw),8.6,13.8*Math.cos(yaw)-6.5*Math.sin(yaw));camera.lookAt(x+.22*Math.sin(hold*Math.PI),1.7,0);
  camera.zoom=(s.kind==='hill'?1.015:1.04)+.075*Math.sin(hold*Math.PI);camera.updateProjectionMatrix();
  key.position.set(x-6.5,13,7);key.target.position.set(x,0,0);fill.position.set(x+6,6,-6);fill.target.position.set(x,0,0);lightPatch.position.x=x-1.5;
  for(let k=0;k<groups.length;k++)groups[k].visible=Math.abs(k-i)<=1;
  const traveling=i>0&&travel<1;renderer.shadowMap.needsUpdate=traveling||i!==lastShadowIndex||lastTravel;lastShadowIndex=i;lastTravel=traveling;
  for(let k=0;k<occluders.length;k++)occluders[k].visible=Math.abs((k+.5)-i)<1.5;
  canvas.style.filter=travel<1?'blur('+ (Math.sin(travel*Math.PI)*2.5).toFixed(2)+'px)':'none';
  renderer.render(scene,camera);
 }
 update(0);return {update,renderer,scene,camera};
};
