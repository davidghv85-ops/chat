# Mercadito Económico · materiales 3D
Video vertical 1080×1920, 30fps, 44.810958s de audio original completo. Intro con banner institucional original de uno.zip; después queda al pie, sin filtros, recortes, redibujo o recoloración.

Paleta: morado oscuro, amarillo huevo y naranja. Paneles de geometría 3D real con grosor y biseles (Three.js), materiales físicos con clearcoat, entorno de estudio, reflejos y luces; anillos metálicos y base cerámica con movimiento de cámara determinista. Combinados con ilustraciones CGI de productos en PNG transparente animadas por capas: las bolsas y la caja no son modelos 3D navegables. Los títulos, fechas y teléfonos son texto superpuesto para mantener su nitidez.

Información del audio: domingo 8 de noviembre de 2026, de 2:30 a 4:30 de la tarde, Auditorio Municipal; ahorros del 30% al 70%. Teléfonos confirmados por el usuario: 241 115 7000 y 241 240 4290. No se anuncia atención por WhatsApp. Voz original conservada, efectos originales suaves de transición y confirmación, sin música.

Fuentes DejaVu, Three.js y GSAP locales. Licencias adjuntas o en encabezados originales.

Recrear: python3 build.py; python3 audio.py; npm run check; npm run render -- --output renders/mercadito-economico-3d.mp4 --quality high --fps 30 --workers 4.

En este entorno, usar `PRODUCER_BROWSER_GPU_MODE=hardware HYPERFRAMES_BROWSER_PATH=/usr/bin/chromium npm run render ...` para seleccionar la ruta Mesa natural de Chromium. El equipo no tiene GPU dedicada: el render sigue usando llvmpipe por CPU. Esta selección evita el arranque muy lento de SwiftShader con materiales físicos. El archivo check-mesa.log corresponde a la comprobación válida y completada; los intentos de comprobación de SwiftShader se descartaron antes de exportar.

El analizador marca dos advertencias de imágenes compartidas entre escenas. Son reutilizaciones intencionales de los dos recursos CGI, sin duplicación de pistas de video o audio. Revisión: cero errores de ejecución, distribución y animación; 18/18 verificaciones de contraste aprobadas.
