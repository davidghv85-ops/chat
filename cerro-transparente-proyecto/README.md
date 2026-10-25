# Cerro del Chichimecateutli · ilustraciones completas y transparentes

Motion vertical 1080×1920, 30 fps, narración original completa 293.450958 segundos. Morado oscuro, naranja, amarillo huevo y blanco; sin logos institucionales.

## Cambios solicitados
- Se eliminaron por completo las ilustraciones decorativas pequeñas de las esquinas: árbol, agave, olla y escudo.
- Cada escena utiliza un PNG individual con transparencia real y la miniatura completa. No se muestran cuadrantes de láminas compartidas, recuadros opacos ni máscaras degradadas para ocultar fondos.
- Se conserva el repertorio temático y se añaden cuatro escenas: comales/barro, enfrentamiento, diálogo y herencia del oficio. 24 ilustraciones grandes, 94 planos, de 1.95 a 3.87 segundos.
- Se corrige la grafía a **Cerro del Chichimecateutli** en pantalla y textos. La grabación de voz se conserva íntegra.
- El movimiento mantiene las ilustraciones dentro del lienzo: desplazamientos, pequeñas escalas, cambios espaciales y poses del personaje. Composición 2.5D; no se afirma animación esquelética de figuras.

## Sonido
Se separan voz, transiciones, actividad y música. Los barridos bajan de nivel. Las escenas de combate incorporan muestras de espada, madera y pasos; las de alfarería llevan fricción/amasado húmedo y contactos resonantes de vasijas y comales. Se incluyen otros golpes de trabajo naval y páginas. Las fuentes CC0 y sus licencias están en `assets/sonidos`.

Música original muy tenue de inspiración prehispánica: flauta/ocarina modelada, percusión de piel/madera y sonajas; no es una reconstrucción de música mexica documentada. Voz al frente y limitador de seguridad. `NIVELES-SONIDO.json` registra niveles separados y ventanas de alfarería/combate. El diseño de sonidos no se presenta como grabación documental de acontecimientos históricos.

## Contenido histórico
Miniaturas interpretativas, no fotografías ni reconstrucciones acreditadas de lugares, rostros o vestuario. El contenido sigue el audio aportado. La cifra de combatientes es aproximada; el relato de Pedro Morón se mantiene como tradición regional cuyos detalles continúan en investigación.

## Reproducir
Requiere Node ≥22, Chromium, FFmpeg, Python 3, NumPy y SciPy. HyperFrames 0.8.144.

```
python3 build.py
python3 audio.py
HYPERFRAMES_BROWSER_PATH=/usr/bin/chromium npm run check
HYPERFRAMES_BROWSER_PATH=/usr/bin/chromium npm run render -- --output renders/mi-tzompantepec-cerro-transparente.mp4 --quality high --fps 30 --workers 4
```

Los stems y la mezcla WAV se regeneran con `audio.py`. El personaje mantiene las imágenes originales del ZIP del usuario. Manrope y DejaVu conservan sus licencias. `planos.json` contiene tiempos y temas; `TRANSPARENCIA.json`, los datos del canal alfa; los PNG definitivos no se agrupan en sprites. Un filtro de composición subpíxel limpia el borde alfa y no modifica los archivos originales.
