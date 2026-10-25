# Cerro del Chichimecateútli · revisión de gráficas y sonido

Vertical 1080×1920, 30 fps, 293.450958 segundos de narración original completa. Sin logos institucionales ni música añadida.

## Qué cambia
Se reemplaza íntegramente la galería de primitivas geométricas por **20 escenas CGI detalladas y seis ilustraciones individuales adicionales**, compuestas en **94 planos de entre 1.95 y 3.87 segundos**. Las acciones visibles corresponden a la explicación: campesinos, alfareros modelando barro, comunidades, guerreros tlaxcaltecas, soldados españoles, liderazgo indígena, negociaciones, transporte de madera y construcción de bergantines. Se añaden cuatro objetos independientes de primer plano para oclusiones y profundidad. Se mantiene la paleta morado oscuro, naranja, amarillo huevo y blanco.

Las láminas generadas se conservan completas; CSS selecciona cada cuadrante. El movimiento final es una composición **2.5D**: seguimiento de cámara, acercamientos y planos de detalle, parallax, oclusiones, transiciones espaciales y tipografía sincronizada. No se presenta como animación esquelética ni como modelos navegables en 3D. El personaje utiliza las imágenes originales del ZIP del usuario, con cambio de postura y movimiento del conjunto.

## Contexto histórico
Las ilustraciones son interpretativas; vestuario, rostros, poblados y relieve son recursos visuales de época, no fotografías ni reconstrucciones arqueológicas acreditadas de sitios concretos. Los títulos y tiempos siguen la narración aportada. Se preservan los calificadores: contingente **aproximado** de 10,000 combatientes y episodio de Pedro Morón como **tradición regional**, cuyos detalles continúan en investigación. No se agrega una afirmación de verificación histórica independiente.

## Sonido
La voz original está completa y no se acelera ni recorta. `audio.py` crea 377 eventos sonoros deterministas y una mezcla estéreo: aire de transiciones, cerámica, papel, madera, pasos, cascos y choques de escudos. Los ambientes de batalla son tenues y aparecen únicamente en las ventanas narrativas correspondientes. No se incluyen disparos, explosiones ni música. Mezcla con limitador y margen de pico. Los efectos son diseño sonoro sintético de esta pieza, no grabaciones documentales.

## Reproducir
Node ≥22, Chromium, FFmpeg, Python, NumPy y SciPy.

```
python3 build.py
python3 audio.py
HYPERFRAMES_BROWSER_PATH=/usr/bin/chromium npm run check
HYPERFRAMES_BROWSER_PATH=/usr/bin/chromium npm run render -- --output renders/mi-tzompantepec-cerro-revision.mp4 --quality high --fps 30 --workers 4
```

La mezcla se regenera desde el audio original y el código. Las imágenes originales de la mascota no se modifican. `planos.json` incluye los tiempos, temas y recursos; `sonido-eventos.json`, las entradas de efectos. Tipografía Manrope 5.3.0 bajo OFL y DejaVu Serif con licencia incluida. HyperFrames fijado a 0.8.144.
