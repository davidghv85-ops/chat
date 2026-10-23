# Gran Festival CUAXICALLI · Tzompantepec
Video vertical 1080 × 1920, 30 fps. Duración de la voz original: 40.530958 s. Nueve escenas de motion vectorial originales: calaveritas ornamentadas, cempasúchil de múltiples pétalos, papel picado, fantasmas flotantes, veladoras, humo, ofrendas, proscenio de teatro y premios. Sin imágenes fotorrealistas ni material de campañas anteriores.

## Datos del anuncio
- Gobierno con Sentido Humano de Tzompantepec, a través de la Dirección de Educación, Cultura, Turismo y Juventud.
- Nombre **CUAXICALLI**, confirmado expresamente por el usuario.
- Concursos de ofrendas y disfraces; premios en dinero en efectivo, sin inventar cantidades.
- Obra de teatro: **Las cuatro caras del miedo**.
- Para todas las edades. **28 de octubre, Presidencia Municipal**. No se añade un horario que la voz no menciona.

## Identidad institucional
El banner es el PNG original recibido en `uno.zip`: 2053 × 279 RGBA, sin modificar. Se muestra al centro en la intro y baja entre 1.9 y 3.1 s; después permanece fijo abajo. Solo presentación proporcional a 1000 px de ancho, sin recorte, recoloración, filtro, distorsión ni redibujo. Integridad documentada en BANNER-INTEGRIDAD.txt.

## Sonido
La locución original permanece completa, sin acelerar, cortar ni sustituir. Se reproduce con ganancia 0.85 para dejar margen a la mezcla. audio.py crea un paisaje sonoro nuevo de viento de cripta, resonancias graves no melódicas, cadenas, puertas y gotas con ecos. El ambiente se atenúa por la energía de la voz. Sin canción añadida ni samples externos. El paisaje sonoro es determinista y exclusivo de esta pieza.

## Reproducir
Requiere Node ≥22, FFmpeg, Chromium y Python con NumPy. CLI fijado en package.json a HyperFrames 0.8.144.

```sh
python3 build.py
python3 audio.py
npm_config_cache=/tmp/npm-cache HYPERFRAMES_BROWSER_PATH=/usr/bin/chromium npm run check
npm_config_cache=/tmp/npm-cache HYPERFRAMES_BROWSER_PATH=/usr/bin/chromium npm run render -- --output renders/tzompantepec-festival-cuaxicalli-28-octubre.mp4 --quality high --fps 30 --workers 2
```

art.py contiene todas las ilustraciones SVG originales. build.py compone la tipografía, paneles y animaciones GSAP, sin recursos web. El halo y las formas que sobrepasan deliberadamente el marco de ilustración son decoraciones; nunca recortan el texto ni cubren el logo. Los avisos de solapamiento entre escenas durante los 0.4 s de transición son intencionales. Los textos se revisan también en sus momentos de lectura.
