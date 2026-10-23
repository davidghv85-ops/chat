# Jornada de vasectomía sin bisturí · Tzompantepec

Video vertical 1080 × 1920 a 30 fps, sincronizado con el audio original de 76.450958 segundos. Doce escenas con paneles, ilustraciones hiperrealistas de campaña y sonidos nuevos discretos. No se añade música ni se reemplaza, acelera o corta la voz. Ganancia de reproducción del audio original: 0.9.

## Datos
- Gobierno con Sentido Humano de Tzompantepec, Coordinación de Salud, en conjunto con Jurisdicción Sanitaria N.º 2, Huamantla.
- Domingos 15 de noviembre y 6 de diciembre de 2026; desde las 08:00 AM.
- Hospital General de Huamantla.
- Cita previa: **247 106 1760** y **246 128 9905**, confirmados expresamente por el usuario en el chat. La confirmación corrige errores de reconocimiento automático; no se genera una voz sustituta.
- Los requisitos visibles proceden de la locución aportada: baño corporal normal, desayuno ligero, rasurado de zona anterior del escroto, acudir acompañado para traslado y llevar suspensorio. No se agregan promesas de eficacia, gratuidad ni instrucciones clínicas no proporcionadas.

## Banner original
Extraído de `uno.zip`, archivo `uno.png`, 2053 × 279 RGBA. Se conserva intacto en `assets/banner-original.png`, con SHA-256 documentado en BANNER-INTEGRIDAD.txt. Aparece centrado en la intro y baja entre 2.2 y 3.4 s; después queda fijo abajo. Ajuste proporcional a 1000 px de ancho, altura automática. Sin filtros, recortes, recoloración ni redibujo. Ningún panel ni transición se superpone al banner.

## Ilustraciones
Cuatro imágenes originales generadas para esta campaña: paciente adulto, agenda y objetos clínicos, higiene y desayuno, acompañamiento. Son ilustrativas; no representan un hospital ni funcionarios reales. Los logos institucionales no forman parte de esas imágenes generadas.

## Reproducir
Requiere Node ≥22, FFmpeg, Chromium y Python con NumPy. HyperFrames está fijado a 0.8.144.

```sh
python3 build.py
python3 audio.py
npm_config_cache=/tmp/npm-cache HYPERFRAMES_BROWSER_PATH=/usr/bin/chromium npm run check
npm_config_cache=/tmp/npm-cache HYPERFRAMES_BROWSER_PATH=/usr/bin/chromium npm run render -- --output renders/tzompantepec-vasectomia-con-audio.mp4 --quality high --fps 30 --workers 2
```

## Revisión
Se revisan escenas, fechas, teléfonos, cierre, sincronización con cambios de frase y presencia del banner. Los avisos de solapamiento durante transiciones de 0.42 s son intencionales; la ampliación de fotos se recorta dentro de sus paneles para crear parallax. Las imágenes reutilizadas en dos escenas se encuadran por separado; son nodos de composición independientes, no duplicaciones del banner. La transcripción automática se utiliza solo para tiempos y se corrigen en pantalla nombres propios y teléfonos confirmados.
