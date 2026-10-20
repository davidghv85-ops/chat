# Tzompantepec · Cuidado del agua
Video vertical 1080 × 1920, 60 segundos, 30 fps. Ocho escenas con ilustraciones SVG originales, paneles animados y efectos sonoros sintetizados para esta pieza. Sin música y sin voz. Texto de corrido y descripción incluidos por separado.

## Reproducir la edición
Requiere Node ≥22, Python 3 con NumPy, FFmpeg y Chromium. CLI fijada en package.json a HyperFrames 0.8.144.

```sh
python3 build.py
python3 audio.py
npm_config_cache=/tmp/npm-cache HYPERFRAMES_BROWSER_PATH=/usr/bin/chromium npm run check
npm_config_cache=/tmp/npm-cache HYPERFRAMES_BROWSER_PATH=/usr/bin/chromium npm run render -- --output renders/tzompantepec-cuidado-del-agua-60s.mp4 --quality high --fps 30 --workers 2
```

La fuente HTML y los diagramas no requieren imágenes externas ni servicios de audio. audio.py crea assets/efectos.wav de manera determinista. La fuente usa la grafía Tzompantepec confirmada por el usuario en la conversación. No incluye logotipos institucionales inventados.

## Revisión
Los avisos de solapamiento entre escenas durante las transiciones de 0.46 s corresponden al deslizamiento intencional del nuevo panel sobre el anterior. La revisión de texto y contraste se hace también en los momentos de lectura de cada escena. El guion continuo es un acompañamiento escrito; el MP4 contiene solo efectos.
