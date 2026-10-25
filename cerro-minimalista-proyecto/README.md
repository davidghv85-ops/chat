# Mi Tzompantepec · Cerro del Chichimecateútli

Motion minimalista vertical de 1080×1920, 30 fps, con el audio completo del usuario: 293.450958 segundos, aproximadamente 4:53. Morado oscuro dominante, naranja, amarillo huevo y blanco. **Sin logotipos institucionales ni banner.**

## Dirección visual
La referencia minimalista del usuario guía el diseño: escenario mate, luz de ventana, sombras de contacto, pocos protagonistas y un camino naranja que conecta las maquetas. El fondo y la cámara continúan entre las 36 estaciones narrativas. Se usan geometrías 3D reales con Three.js 0.160.1, no fotografías de objetos 3D ni iconos planos simulando volumen. El render de la maqueta se compone sobre una tarjeta vertical redondeada; la tipografía editorial y los PNG del personaje se mantienen nítidos en la composición Full HD.

Las maquetas son interpretativas y simbólicas. No son un levantamiento del cerro ni reconstrucciones arqueológicas o retratos históricos documentales. Se ilustran el relieve, agricultura, cerámica, libros, paso del tiempo, resistencia, trabajo colectivo, alianzas, un caballo sin violencia gráfica y bergantines. La información visible sigue la narración aportada; el episodio de Pedro Morón se presenta como tradición regional con detalles aún en investigación. La cifra de combatientes se muestra como aproximada.

## Personaje
Se utilizan las variantes PNG originales del ZIP nuevo `Imagen de ChatGPT 13 oct 2026, 08_56_41 a.m-5-Photoroom.zip`, sin redibujar ni recolorear el personaje. El manifiesto vincula cada archivo con su nombre original. Las poses participan como guía en primer plano, con cambios de postura y movimientos suaves de conjunto. Se conserva su identidad visual; no se afirma que exista una animación facial o un rig esquelético nuevo.

## Audio
El archivo original se conserva completo, sin acelerarlo, cortarlo ni reemplazar la voz. Se añaden efectos originales muy discretos de desplazamiento de cámara, papel y madera. Sin música nueva ni ambiente de miedo. La mezcla deja margen para que la narración sea inteligible.

## Reproducir
Requiere Node ≥22, FFmpeg, Chromium con WebGL/SwiftShader o llvmpipe, Python 3 y NumPy. HyperFrames está fijado a 0.8.144. El escenario 3D se dibuja a resolución interna de 640×1165 y se integra con texto y personajes a 1080×1920. Esto equilibra el render por software de casi cinco minutos con la claridad editorial.

```sh
python3 build.py
python3 audio.py
npm_config_cache=/tmp/npm-cache HYPERFRAMES_BROWSER_PATH=/usr/bin/chromium npm run check
npm_config_cache=/tmp/npm-cache HYPERFRAMES_BROWSER_PATH=/usr/bin/chromium npm run render -- --output renders/mi-tzompantepec-cerro-minimalista.mp4 --quality high --fps 30 --workers 4
```

`models.js` contiene todas las maquetas originales. `world.js` construye el mundo, la iluminación, las sombras, la cinta naranja y la cámara determinista. `story.py` conserva los tiempos del guion. La biblioteca Three.js se conserva junto con su licencia MIT. Puede reconstruirse desde three@0.160.1/build/three.module.js usando esbuild@0.25.9 en formato IIFE con global-name=THREE.

## Revisión
Comprobar maquetas, personajes, legibilidad, cambios de tema, años y cierre. Las variantes repetidas son imágenes intencionales en composiciones independientes. Los mensajes del driver «GPU stall due to ReadPixels» describen la captura de WebGL por software, no un error de guion o de imagen; se revisa el MP4 renderizado. Los datos del audio no se presentan como una investigación nueva independiente. La distinción entre tradición e investigación se conserva en las escenas correspondientes.
