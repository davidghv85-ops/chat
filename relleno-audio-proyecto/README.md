# Separación de residuos · Audio original del usuario

Motion vertical 1080 × 1920, 30 fps, duración basada en el audio: 70.861021 segundos. Once escenas con paneles en perspectiva, contenedores de orgánicos e inorgánicos, rutas, camión, ciudad y barrera del relleno sanitario. Sonidos nuevos discretos bajo el audio original, sin música añadida. El audio se conserva completo y sin acelerar ni cortar; la ganancia de reproducción es 0.9 para dejar margen a los efectos.

## Estado
Finalizado con el banner original recibido en uno.zip (uno.png, 2053 × 279), fijo abajo durante todo el video. El archivo se conserva intacto; su SHA-256 se documenta en BANNER-INTEGRIDAD.txt. La base sin banner queda como borrador histórico.

## Reproducir
Requiere Node ≥22, FFmpeg, Chromium y Python con NumPy. Dependencias del CLI fijadas en package.json.

```sh
python3 build.py
python3 audio.py
npm_config_cache=/tmp/npm-cache HYPERFRAMES_BROWSER_PATH=/usr/bin/chromium npm run check
npm_config_cache=/tmp/npm-cache HYPERFRAMES_BROWSER_PATH=/usr/bin/chromium npm run render -- --output renders/tzompantepec-separacion-residuos-con-audio.mp4 --quality high --fps 30 --workers 2
```

Para la base ya renderizada antes de recibir el banner, `finalizar.py` conserva una copia binaria intacta del banner y documenta su SHA-256; en el video solo lo ajusta de forma proporcional a 1000 px de ancho, completo, fijo y sin filtros. El banner se coloca sobre la franja inferior durante toda la duración. El audio codificado de la base se copia sin recodificar en esa operación.

## Sincronización y revisión
Los tiempos de escenas se basan en la transcripción automática local y los cambios de frase: voz a 9.5 s; invitación a 17.36 s; separación a 22.74 s; cierre del relleno a 28.56 s; municipio limpio a 35.02 s; acción inmediata a 42.14 s; compromiso a 50.16 s; gestión a 54.74 s; cierre participativo a 62.72 s. Los nombres y conceptos en pantalla usan Tzompantepec, Coordinación de Ecología, relleno sanitario, orgánicos e inorgánicos.

Los avisos de solapamiento del verificador entre escenas corresponden a las transiciones de 0.4 s: el panel entrante cubre al anterior. Se inspeccionan además los momentos de lectura de cada escena. El banner no participa en ninguna transición.
