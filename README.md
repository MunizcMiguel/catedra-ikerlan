# Web Cátedra Ikerlan (versión estática, sin Wix)

Réplica rediseñada de https://www.catedraikerlan.com con todo el contenido, fotos y documentos descargados en local.
No necesita servidor: abre `index.html` con doble clic. Para publicarla basta con subir la carpeta a cualquier hosting estático (GitHub Pages, Netlify, servidor de la Universidad…).

## Estructura
- `index.html`, `equipo.html`, `convocatoria.html`, `estudiantes.html`, `tfg-tfm.html`, `practicas.html`, `investigacion.html`, `challenge-2023.html`, `noticias.html`, `contacto.html`
- `noticias/` – una página por noticia (10)
- `assets/img` – fotos optimizadas · `assets/docs` – PDFs · `assets/fonts` – Open Sans y Anton en local
- `assets/css/styles.css` – estilos (colores en `:root`) · `assets/js/main.js` – carrusel, pestañas, paginación, visor, vídeos, menú
- `_build/build.py` – generador: el texto de todas las páginas está aquí. Tras editarlo:

```
python _build/build.py
```

## Dependencias externas (opcionales)
- Vídeos de YouTube (se cargan solo al pulsar «play»), mapa de OpenStreetMap en Contacto y enlaces a funiovi.org / prensa.
- El formulario de contacto abre el programa de correo del usuario (mailto), ya que no hay backend.
- Tres presentaciones de la Jornada 2023 solo están en la web original (Wix no permite descargarlas directamente).
