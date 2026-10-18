# MI TZOMPANTEPEC — Proyecto editable

Los index.html son las fuentes finales. Incluyen los paneles, la narración escrita completa, las animaciones y las preguntas. Los PNG originales del personaje están en assets/character. Las ilustraciones SVG son conceptuales.

Requisitos: Node 22 o superior, Python con NumPy, FFmpeg, Chromium y Git LFS. HyperFrames está fijado en 0.8.144. Los efectos WAV se regeneran con semilla fija y no se guardan en Git. No ejecutar un generador de guiones anterior: editar estos HTML y sus guion.json/textos correspondientes.

Desde este directorio:

```sh
python -m venv --system-site-packages .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python audio.py
.venv/bin/python batch.py
```

El lote valida cada composición, exporta 1080×1920 a 30 fps, comprueba 90 segundos y audio AAC, decodifica el MP4 completo y crea una hoja de revisión. Usa dos exportaciones simultáneas, cada una con dos trabajadores. Para un episodio, entrar a su carpeta y usar npm_config_cache=/tmp/npm-cache HYPERFRAMES_BROWSER_PATH=/usr/bin/chromium npm run check, o el mismo prefijo con npm run render. El navegador se configura con HYPERFRAMES_BROWSER_PATH=/usr/bin/chromium. No se necesita un servidor persistente para exportar.

Las carpetas de la serie de entregables contienen los MP4, los textos y las descripciones. Las limitaciones y correcciones de fuentes están documentadas en FUENTES-Y-ALCANCE.md.
