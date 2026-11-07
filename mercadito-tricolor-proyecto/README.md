# Mercadito Económico · morado, naranja y amarillo huevo
Versión con composición propia, basada en el acabado refinado de los paneles de referencia: bordes finos, sombras suaves y profundidad por capas. El naranja y el amarillo huevo ocupan superficies principales del calendario, horario, productos, ahorros y contactos, junto al morado oscuro.

Intro institucional dedicada 0–3.05 segundos: logo original centrado y franjas de color animadas detrás; después el mismo PNG se desplaza al pie. Sin títulos del evento durante la intro. No se modifica el archivo, el color, la proporción o el contenido de los logos.

13 escenas: invitación, pase del mercado, calendario seccionado, lugar, horario apilado, bento de alimentos, ahorro del 30% al 70%, apoyo al hogar y contactos. Audio original completo, sin acelerar ni cortar: 44.810958s. Exportación vertical 1080×1920, 30fps. Efectos suaves originales de la pieza revisada, sin música.

Datos: domingo 8 de noviembre de 2026, Auditorio Municipal, de 2:30 a 4:30 p. m. Teléfonos confirmados por el usuario: 241 115 7000 y 241 240 4290.

Recrear: python3 build.py; npm run check; npm run render -- --output renders/mercadito-morado-naranja-amarillo.mp4 --quality high --fps 30 --workers 4.

Comprobación: 26/26 controles de contraste aprobados; sin errores de ejecución o animación. Los avisos de superposición corresponden a escenas durante sus transiciones de 0.4s y no a los cuadros de lectura asentados, revisados individualmente. Fuentes DejaVu con licencia y GSAP con encabezado original.
