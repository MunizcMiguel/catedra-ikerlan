# -*- coding: utf-8 -*-
"""
Generador de la web estática de la Cátedra Ikerlan.

Todas las páginas comparten cabecera y pie; el contenido de cada página está
en este fichero. Para regenerar la web tras editar algo:

    python _build/build.py

Los .html resultantes se escriben en la carpeta raíz del proyecto y no
necesitan servidor (se pueden abrir con doble clic).
"""
import os
from datetime import date

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# ---------------------------------------------------------------- iconos
ICON = {
    'chev': '<svg class="chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M6 9l6 6 6-6"/></svg>',
    'menu': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg>',
    'arrow': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
    'left': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M15 18l-6-6 6-6"/></svg>',
    'right': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M9 18l6-6-6-6"/></svg>',
    'up': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M18 15l-6-6-6 6"/></svg>',
    'people': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="9" cy="8" r="3.2"/><path d="M3 20c0-3.3 2.7-6 6-6s6 2.7 6 6"/><circle cx="17" cy="9" r="2.4"/><path d="M16 14.2c2.8.3 5 2.6 5 5.8"/></svg>',
    'pencil': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16.5 3.5l4 4L8 20H4v-4z"/><path d="M14 6l4 4"/></svg>',
    'chess': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2v3M10.5 3.5h3"/><path d="M8.5 9.5C8.5 7 10 5.5 12 5.5s3.5 1.5 3.5 4c0 1.6-.8 2.6-1.5 3.5l1 4H9l1-4c-.7-.9-1.5-1.9-1.5-3.5z"/><path d="M6.5 21h11M7.5 17h9"/></svg>',
    'bulb': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 18h6M10 21h4"/><path d="M12 3a6 6 0 00-3.6 10.8c.7.5 1.1 1.3 1.1 2.2h5c0-.9.4-1.7 1.1-2.2A6 6 0 0012 3z"/></svg>',
    'chip': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="6" y="6" width="12" height="12" rx="2"/><path d="M9 2v4M15 2v4M9 18v4M15 18v4M2 9h4M2 15h4M18 9h4M18 15h4"/></svg>',
    'bolt': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M13 2L4 14h7l-1 8 9-12h-7z"/></svg>',
    'gear': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.7 1.7 0 00.3 1.8l.1.1a2 2 0 11-2.8 2.8l-.1-.1a1.7 1.7 0 00-1.8-.3 1.7 1.7 0 00-1 1.5V21a2 2 0 11-4 0v-.1a1.7 1.7 0 00-1.1-1.5 1.7 1.7 0 00-1.8.3l-.1.1a2 2 0 11-2.8-2.8l.1-.1a1.7 1.7 0 00.3-1.8 1.7 1.7 0 00-1.5-1H3a2 2 0 110-4h.1a1.7 1.7 0 001.5-1.1 1.7 1.7 0 00-.3-1.8l-.1-.1a2 2 0 112.8-2.8l.1.1a1.7 1.7 0 001.8.3H9a1.7 1.7 0 001-1.5V3a2 2 0 114 0v.1a1.7 1.7 0 001 1.5 1.7 1.7 0 001.8-.3l.1-.1a2 2 0 112.8 2.8l-.1.1a1.7 1.7 0 00-.3 1.8V9a1.7 1.7 0 001.5 1H21a2 2 0 110 4h-.1a1.7 1.7 0 00-1.5 1z"/></svg>',
    'euro': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 6.5A7 7 0 106.9 17.5 7 7 0 0018 17.5"/><path d="M4 10h9M4 14h9"/></svg>',
    'book': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 5.5C4.5 4 8 4 12 6c4-2 7.5-2 10-.5V19c-2.5-1.5-6-1.5-10 .5-4-2-7.5-2-10-.5z"/><path d="M12 6v13.5"/></svg>',
    'cal': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4M7.5 14h2M11 14h2M14.5 14h2M7.5 17.5h2M11 17.5h2"/></svg>',
    'mail': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/></svg>',
    'pin': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 21s-7-6.2-7-11.5a7 7 0 0114 0C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/></svg>',
    'user': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="4"/><path d="M4 21c0-4.4 3.6-8 8-8s8 3.6 8 8"/></svg>',
    'download': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3v12M7 10l5 5 5-5M4 20h16"/></svg>',
    'ext': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 4h6v6M20 4l-9 9M18 14v5a1 1 0 01-1 1H5a1 1 0 01-1-1V7a1 1 0 011-1h5"/></svg>',
    'team': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="7" r="3"/><circle cx="5" cy="10" r="2.2"/><circle cx="19" cy="10" r="2.2"/><path d="M7 20c0-2.8 2.2-5 5-5s5 2.2 5 5M1.5 19c0-2 1.5-3.6 3.5-3.6M22.5 19c0-2-1.5-3.6-3.5-3.6"/></svg>',
    'target': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1.2"/></svg>',
    'flag': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 21V4M5 4h11l-2 4 2 4H5"/></svg>',
    'trophy': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M8 4h8v5a4 4 0 01-8 0z"/><path d="M8 6H4v1a3 3 0 003 3M16 6h4v1a3 3 0 01-3 3M12 13v4M8 21h8M9 17h6"/></svg>',
}

AC = ' aria-current="page"'
HI = ' fetchpriority="high"'
LZ = ' loading="lazy"'


def big(name):
    return ICON[name].replace('<svg', '<svg style="width:30px;height:30px"')


# ---------------------------------------------------------------- noticias
NEWS = [
    dict(slug='inauguracion-sede-campus-gijon', date='2025-02-13',
         title='La Cátedra Ikerlan de Investigación y Desarrollo inaugura su sede en el Campus de Gijón de la Universidad de Oviedo',
         img='sede-inauguracion-2025', tag='Institucional',
         summary='En el acto se presentó la Convocatoria de Proyectos I+D+i 2025 financiados por la Cátedra Ikerlan, así como las posibilidades que ofrece Ikerlan a los estudiantes de la EPI de Gijón.',
         body='''
<p class="lead">En el acto, presentaron la Convocatoria de Proyectos I+D+i 2025 financiados por la Cátedra Ikerlan, así como las posibilidades que ofrece Ikerlan a los estudiantes de la EPI de Gijón para realizar sus trabajos de fin de estudios, tesis o prácticas.</p>
<figure><img src="../assets/img/sede-inauguracion-2025.jpg" alt="Asistentes a la inauguración de la sede de la Cátedra Ikerlan en la EPI de Gijón"></figure>
<p>Responsables del Centro Tecnológico Ikerlan del País Vasco visitaron el Campus de Gijón de la Universidad de Oviedo para inaugurar la sede de la Cátedra Ikerlan de Investigación y Desarrollo, situada en la primera planta del Edificio Departamental 7 de la EPI.</p>
<p>Durante la jornada, se desarrollaron varias reuniones con profesorado y estudiantado interesado en colaborar en las líneas de especialización de Ikerlan. Además, Marco González Hierro, responsable área IA y Datos de Ikerlan impartió una conferencia titulada <em>Impacto de la Inteligencia Artificial en Nuevos Desarrollos Tecnológicos Demandados por la Industria</em>. En esta conferencia se expusieron numerosos ejemplos industriales sobre el impacto de la Inteligencia Artificial en los nuevos desarrollos tecnológicos que actualmente las empresas demandan en ámbitos como: las tecnologías digitales, los sistemas electrónicos y la ciberseguridad y la energía y la mecatrónica.</p>
<figure><img src="../assets/img/sede-conferencia-2025.jpg" alt="Conferencia de Marco González en la EPI de Gijón"></figure>
<p>Una vez finalizada la conferencia, Unai Viscarret Álvarez, director de personas de Ikerlan; María Jesús Lamela Rey, directora de la Cátedra Ikerlan de la Universidad de Oviedo y Santiago Fernández López, director de la Fundación Universidad de Oviedo, presentaron la <a href="../convocatoria.html">Convocatoria de Proyectos I+D+i 2025</a> financiados por la Cátedra Ikerlan, así como las posibilidades que ofrece la compañía a los estudiantes de la EPI de Gijón para realizar sus trabajos de fin de estudios (grado y máster), doctorado o prácticas.</p>
<p>Para finalizar la jornada, tuvo lugar la inauguración de la sede de la Cátedra Ikerlan de Investigación y Desarrollo ubicada en el Departamento de Construcción e Ingeniería de Fabricación del Campus de Gijón, que contó con la presencia de la vicerrectora de Transferencia y Relaciones con la Empresa, Susana Luque Rodríguez, y de la directora de área de Cátedras de Empresa e Institucionales, Verónica Cañal Fernández.</p>
'''),
    dict(slug='jornada-catedra-ikerlan-2023', date='2023-09-25',
         title='Jornada Cátedra Ikerlan 2023', img='slide-08', tag='Jornada',
         summary='El pasado 20 de septiembre de 2023 compartimos con estudiantes y profesores la Jornada Cátedra Ikerlan 2023 en la EPI.',
         body='''
<p class="lead">El pasado 20 de septiembre de 2023 compartimos con estudiantes y profesores la Jornada Cátedra Ikerlan 2023 en la EPI.</p>
<p>Fue una excelente oportunidad para mostrar el trabajo que hacemos desde la Cátedra, las oportunidades de becas para el próximo año, las experiencias de egresados de la Cátedra… además de realizar entregas de premios y convocar la segunda edición del Concurso <a href="../challenge-2023.html">Challenge Ikerlan 2023</a>.</p>
<p>Os dejamos adjuntas a esta noticia las presentaciones que se utilizaron ese día, por si queréis revisarlas en el futuro.</p>
<div class="files">
  <a class="file" href="../assets/docs/challenge-2023-retos.pdf" target="_blank" rel="noopener"><span class="fi">PDF</span><span>ChallengeIkerlan2023.pdf<small>546 KB · descarga local</small></span></a>
  <a class="file" href="https://www.catedraikerlan.com/post/jornada-catedra-ikerlan-2023" target="_blank" rel="noopener"><span class="fi">PDF</span><span>1. IKERLAN_09_2023_UNIOVI.pdf<small>2,75 MB · disponible en la noticia original</small></span></a>
  <a class="file" href="https://www.catedraikerlan.com/post/jornada-catedra-ikerlan-2023" target="_blank" rel="noopener"><span class="fi">PDF</span><span>4. Especialidades y TFG_TFMs.pdf<small>2,41 MB · disponible en la noticia original</small></span></a>
  <a class="file" href="https://www.catedraikerlan.com/post/jornada-catedra-ikerlan-2023" target="_blank" rel="noopener"><span class="fi">PDF</span><span>5. Concurso de ideas – Cátedra Ikerlan Challenge 2023.pdf<small>2,64 MB · disponible en la noticia original</small></span></a>
</div>
<p>Para cualquier consulta, no dudes en contactar con nosotros: <a href="mailto:mjesuslr@uniovi.es">mjesuslr@uniovi.es</a> o <a href="mailto:munizcmiguel@uniovi.es">munizcmiguel@uniovi.es</a>.</p>
'''),
    dict(slug='premios-mario-martin-malena-potesta', date='2023-09-25',
         title='Mario Martín y Malena Potesta reciben los premios de la Cátedra Ikerlan',
         img='premios-2023-mario-malena', tag='Premios',
         summary='Premios a mejor expediente del máster en Ingeniería Mecatrónica y mejor TFG 2021/2022 en Desarrollo y Transferencia Tecnológica.',
         body='''
<p class="lead">Los alumnos Mario Martín y Malena Potesta recibieron los premios a mejor expediente del máster en Ingeniería Mecatrónica y mejor TFG 2021/2022 en Desarrollo y Transferencia Tecnológica.</p>
<div class="gallery gallery--wide" style="grid-template-columns:1fr 1fr">
  <button type="button" data-lightbox="p23"><img src="../assets/img/premios-2023-mario-malena.jpg" alt="Entrega de premios Cátedra Ikerlan 2023"></button>
  <button type="button" data-lightbox="p23"><img src="../assets/img/premios-2023-2.jpg" alt="Premiados y tutores en la entrega de premios 2023"></button>
</div>
<p>Enlace a la noticia completa: <a href="https://www.elcomercio.es/gijon/alumnos-epi-mario-martin-malena-potesta-reciben-20230921015013-nt.html" target="_blank" rel="noopener">El Comercio</a>.</p>
'''),
    dict(slug='renovamos-por-4-anos-la-catedra-ikerlan', date='2023-09-25',
         title='Renovamos por 4 años la Cátedra Ikerlan', img='jornada-2023-renovacion', tag='Institucional',
         summary='La Escuela Politécnica de Ingeniería acogió el 20 de septiembre la Jornada Ikerlan, en el contexto de la cátedra que acaba de ser renovada por cuatro años.',
         body='''
<p class="lead">La Escuela Politécnica de Ingeniería de la Universidad de Oviedo acogió el 20 de septiembre la Jornada Ikerlan, en el contexto de la cátedra que acaba de ser renovada por cuatro años.</p>
<figure><img src="../assets/img/jornada-2023-renovacion.jpg" alt="Acto inaugural de la Jornada Ikerlan 2023"></figure>
<p>En la imagen, de izquierda a derecha, Iker Urresti, Unai Viscarret, Inés Suárez, María Jesús Lamela, Marco González y Miguel Muñiz Calvente, durante el acto inaugural. La jornada contó con experiencias de egresados, presentación de oportunidades y convocatorias y entrega de premios.</p>
<p>Noticia original: <a href="https://www.lne.es/gijon/2023/09/21/politecnica-renueva-cuatro-anos-catedra-92361951.html" target="_blank" rel="noopener">La Nueva España</a>.</p>
'''),
    dict(slug='convocatoria-premios-catedra-ikerlan-2021-2022', date='2023-07-21',
         title='Convocatoria Premios Cátedra Ikerlan 2021-2022', img='convocatoria-premios-2021-2022', tag='Convocatoria',
         summary='Premio al mejor expediente en Ingeniería Mecatrónica y Premio TFG sobre innovación y transferencia tecnológica del curso 2021-2022.',
         body='''
<p class="lead">Convocatoria de un Premio al mejor expediente en Ingeniería Mecatrónica y un Premio TFG sobre innovación y transferencia tecnológica presentado durante el curso 2021-2022 en los Grados en Ingeniería Mecánica y en Ingeniería en Tecnologías Industriales de la EPI de Gijón de la Universidad de Oviedo.</p>
<figure><img src="../assets/img/convocatoria-premios-2021-2022.jpg" alt="Cartel de los Premios Cátedra Ikerlan-Universidad de Oviedo"></figure>
<p>El Premio al mejor expediente de Ingeniería Mecatrónica se resolverá directamente por la Dirección de la Cátedra y los Coordinadores del Máster y no es necesario que los estudiantes lo soliciten. El Premio TFG, financiado por la Cátedra IKERLAN, tendrá una dotación global bruta de mil euros (1.000 euros) y se entregará con un diploma acreditativo al estudiante premiado/a, así como con un diploma acreditativo al tutor/a del trabajo que resulte premiado. Este Premio es compatible con otros premios que haya podido recibir previamente el mismo TFG. Las candidaturas deberán ser remitidas por correo electrónico a la Fundación Universidad de Oviedo, según procedimiento establecido en las bases. El plazo de presentación de solicitudes finalizará el 31 de agosto de 2023.</p>
<p>Documentos relacionados en: <a href="https://www.funiovi.org/empresas/noticias/-/asset_publisher/wBPvnuGZI84p/content/catedra-ikerl-2" target="_blank" rel="noopener">Fundación Universidad de Oviedo – Cátedra IKERLAN – Noticias (funiovi.org)</a>.</p>
'''),
    dict(slug='i-concurso-ideas-catedra-ikerlan', date='2022-10-28',
         title='I Concurso Ideas Cátedra Ikerlan', img='concurso-ideas-2022-1', tag='Concurso',
         summary='En la visita a las instalaciones de Ikerlan, el 26 de octubre de 2022, se celebró la final del I Concurso Ideas Cátedra Ikerlan.',
         body='''
<p class="lead">En la visita a las instalaciones de Ikerlan, el 26 de octubre de 2022, se celebró la final del I Concurso Ideas Cátedra Ikerlan, en el que los premiados fueron:</p>
<ul class="winners">
  <li><span class="medal">1</span><span><strong>Primer premio</strong><br>David García Manzanares y Álvaro López Pascua</span></li>
  <li><span class="medal">2</span><span><strong>Segundo premio</strong><br>Gonzalo Rosales García, Jorge Carro Rodríguez y David Guijarro Villar</span></li>
  <li><span class="medal">3</span><span><strong>Tercer premio</strong><br>Jairo Codina Pérez</span></li>
</ul>
<p>¡Enhorabuena a los premiados y gracias a todos por participar!</p>
<div class="gallery gallery--wide" style="grid-template-columns:1fr 1fr">
  <button type="button" data-lightbox="ci22"><img src="../assets/img/concurso-ideas-2022-1.jpg" alt="Premiados del I Concurso de Ideas en Ikerlan"></button>
  <button type="button" data-lightbox="ci22"><img src="../assets/img/concurso-ideas-2022-2.jpg" alt="Participantes del I Concurso de Ideas"></button>
  <button type="button" data-lightbox="ci22"><img src="../assets/img/concurso-ideas-2022-3.jpg" alt="Equipo participante en el I Concurso de Ideas"></button>
  <button type="button" data-lightbox="ci22"><img src="../assets/img/concurso-ideas-2022-4.jpg" alt="Foto de grupo de la visita a Ikerlan"></button>
</div>
'''),
    dict(slug='premios-alejandro-fernandez-mario-martin', date='2022-05-09',
         title='Alejandro Fernández y Mario Martín premiados por la Cátedra Ikerlan',
         img='premios-2022-alejandro-mario', tag='Premios',
         summary='Premios al mejor TFG en Ingeniería Mecánica y Tecnologías Industriales y al mejor expediente de primer año del máster en Ingeniería Mecatrónica.',
         body='''
<figure><img src="../assets/img/premios-2022-alejandro-mario.jpg" alt="Alejandro Fernández y Mario Martín con sus diplomas"></figure>
<p class="lead">Alejandro Fernández y Mario Martín recibieron sendos premios de la Cátedra Ikerlan al mejor trabajo fin de grado en Ingeniería Mecánica y Tecnologías Industriales; y al mejor expediente de primer año en el máster de Ingeniería Mecatrónica.</p>
<p>Noticia en prensa: <a href="https://www.lne.es/gijon/2022/05/07/ikerlan-premia-excelencia-academica-65818389.amp.html" target="_blank" rel="noopener">La Nueva España</a>.</p>
'''),
    dict(slug='premios-2020-fruela-de-la-roza-pelayo-fernandez', date='2021-02-16',
         title='Fruela de la Roza y Pelayo Fernández ganadores de los Premios Cátedra Ikerlan 2020',
         img='premios-2020-fruela-pelayo', tag='Premios',
         summary='Premio al mejor TFG sobre innovación y transferencia tecnológica y al mejor expediente del primer año del máster en Ingeniería Mecatrónica.',
         body='''
<p class="lead">Fruela de la Roza ha recogido el premio al mejor trabajo fin de grado sobre innovación y transferencia tecnológica, en el que ha desarrollado una metodología para la utilización de componentes metálicos mediante la fabricación aditiva o impresión 3D.</p>
<p>Pelayo Fernández ha sido premiado por contar con el mejor expediente del primer año del máster universitario en Ingeniería Mecatrónica y del máster Erasmus Mundus.</p>
<figure><img src="../assets/img/premios-2020-fruela-pelayo.jpg" alt="Fruela de la Roza y Pelayo Fernández con sus premios"></figure>
<p>Noticia en prensa: <a href="https://www.elcomercio.es/asturias/universidad/ikerlan-premia-alumnos-universidad-oviedo-20201222145949-nt.html" target="_blank" rel="noopener">El Comercio</a>.</p>
'''),
    dict(slug='defensa-tesis-mikel-escalero', date='2020-12-10',
         title='22 de diciembre: defensa de tesis de Mikel Escalero Igartúa', img='tesis-mikel-escalero', tag='Tesis',
         summary='«Predicción de crecimiento de grietas en fatiga considerando fenómenos plásticos de punta de grieta: limitaciones de enfoques actuales y una metodología novedosa».',
         body='''
<p class="lead">El 22 de diciembre a las 12 horas se defenderá la tesis titulada <em>«Predicción de crecimiento de grietas en fatiga considerando fenómenos plásticos de punta de grieta: limitaciones de enfoques actuales y una metodología novedosa»</em> de Mikel Escalero Igartúa.</p>
<figure><img src="../assets/img/tesis-mikel-escalero.jpg" alt="Portada de la tesis de Mikel Escalero Igartúa"></figure>
<p>Algunos de los resultados de esta tesis pueden consultarse en la sección de <a href="../investigacion.html#crecimiento">Investigación</a>.</p>
'''),
    dict(slug='premios-catedra-ikerlan-2020', date='2020-12-10',
         title='El 22 de diciembre se fallarán los Premios de la Cátedra Ikerlan-Uniovi', img='premios-2020-cartel', tag='Premios',
         summary='El acto tendrá lugar en la Sala de Juntas del Aulario Sur del Campus de Gijón a las 10.50 horas.',
         body='''
<p class="lead">El acto tendrá lugar en la Sala de Juntas del Aulario Sur del Campus de Gijón a las 10.50 horas.</p>
<figure><img src="../assets/img/premios-2020-cartel.jpg" alt="Cartel del Premio al mejor Trabajo Fin de Grado sobre innovación y transferencia tecnológica"></figure>
<p>Consulta los <a href="premios-2020-fruela-de-la-roza-pelayo-fernandez.html">ganadores de los Premios Cátedra Ikerlan 2020</a>.</p>
'''),
]
MESES = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']


def fdate(s):
    y, m, d = map(int, s.split('-'))
    return f'{d} de {MESES[m-1]} de {y}'


# ---------------------------------------------------------------- plantilla
NAV = [
    ('index.html', 'Inicio'),
    ('convocatoria.html', 'Convocatoria proyectos'),
    ('equipo.html', 'Equipo'),
    ('estudiantes', 'Estudiantes', [
        ('estudiantes.html', 'Experiencias y formación'),
        ('tfg-tfm.html', 'TFG / TFM'),
        ('practicas.html', 'Prácticas y becas'),
        ('challenge-2023.html', 'Ikerlan Challenge 2023'),
    ]),
    ('investigacion.html', 'Investigación'),
]


def header(cur, r):
    items = []
    for entry in NAV:
        if len(entry) == 3:
            key, label, subs = entry
            active = any(cur == h for h, _ in subs)
            sub = ''.join(f'<li><a href="{r}{h}"{AC if cur == h else ""}>{t}</a></li>' for h, t in subs)
            items.append(f'<li class="has-sub{" active" if active else ""}"><button class="nav-btn" type="button" aria-expanded="false" aria-haspopup="true">{label} {ICON["chev"]}</button><ul class="submenu">{sub}</ul></li>')
        else:
            h, t = entry
            items.append(f'<li><a href="{r}{h}"{AC if cur == h else ""}>{t}</a></li>')
    pill = lambda h, t: f'<a class="pill" href="{r}{h}"{AC if cur == h else ""}>{t}</a>'
    return f'''<a class="skip" href="#main">Saltar al contenido</a>
<header class="site-header">
  <div class="container header-inner">
    <a class="brand" href="{r}index.html" aria-label="Cátedra Ikerlan – Inicio">
      <img class="logo-ikerlan" src="{r}assets/img/logo-ikerlan.png" alt="Ikerlan" width="76" height="34">
      <span class="divider" aria-hidden="true"></span>
      <img class="logo-uniovi" src="{r}assets/img/logo-uniovi.jpg" alt="Universidad de Oviedo" width="130" height="40">
      <span class="brand-title"><strong>Cátedra Ikerlan</strong><span>de Investigación y Desarrollo</span></span>
    </a>
    <button class="menu-toggle" type="button" aria-label="Abrir menú" aria-expanded="false" aria-controls="nav">{ICON["menu"]}</button>
    <nav class="nav" id="nav" aria-label="Principal">
      <ul>{''.join(items)}</ul>
      <div class="nav-cta">{pill("noticias.html", "Noticias")}{pill("contacto.html", "Contacto")}</div>
    </nav>
  </div>
</header>'''


def footer(r):
    return f'''<footer class="site-footer">
  <div class="container footer-grid">
    <div class="footer-brand">
      <strong>Cátedra Ikerlan</strong>
      <p>Cátedra Ikerlan-Uniovi de Investigación y Desarrollo: colaboración entre el Centro Tecnológico Ikerlan y la Universidad de Oviedo desde 2019.</p>
      <div class="footer-logos"><span><img src="{r}assets/img/logo-ikerlan.png" alt="Ikerlan" width="68" height="30"></span><span><img src="{r}assets/img/logo-uniovi.jpg" alt="Universidad de Oviedo" width="98" height="30"></span></div>
    </div>
    <div>
      <h3>La Cátedra</h3>
      <ul>
        <li><a href="{r}index.html">Inicio</a></li>
        <li><a href="{r}equipo.html">Equipo</a></li>
        <li><a href="{r}convocatoria.html">Convocatoria proyectos</a></li>
        <li><a href="{r}investigacion.html">Investigación</a></li>
        <li><a href="{r}noticias.html">Noticias</a></li>
      </ul>
    </div>
    <div>
      <h3>Estudiantes</h3>
      <ul>
        <li><a href="{r}estudiantes.html">Experiencias y formación</a></li>
        <li><a href="{r}tfg-tfm.html">TFG / TFM</a></li>
        <li><a href="{r}practicas.html">Prácticas y becas</a></li>
        <li><a href="{r}challenge-2023.html">Ikerlan Challenge 2023</a></li>
      </ul>
    </div>
    <div>
      <h3>Contacto</h3>
      <ul>
        <li>Escuela Politécnica de Ingeniería de Gijón<br>33204, Gijón</li>
        <li><a href="mailto:munizcmiguel@uniovi.es">munizcmiguel@uniovi.es</a></li>
        <li><a href="mailto:mjesuslr@uniovi.es">mjesuslr@uniovi.es</a></li>
        <li><a href="{r}contacto.html">Formulario de contacto</a></li>
      </ul>
    </div>
  </div>
  <div class="container footer-bottom">
    <span>© 2020–<span id="year">{date.today().year}</span> Cátedra Ikerlan-Uniovi</span>
    <span>Web original por Miguel Muñiz Calvente</span>
  </div>
</footer>
<button class="to-top" type="button" aria-label="Volver arriba">{ICON["up"]}</button>
<script src="{r}assets/js/main.js"></script>'''


def page(path, title, desc, body, cur=None):
    r = '../' * path.count('/')
    html = f'''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#19ff20">
<link rel="icon" href="{r}assets/img/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="{r}assets/css/styles.css">
</head>
<body>
{header(cur or path, r)}
<main id="main">
{body}
</main>
{footer(r)}
</body>
</html>
'''
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, 'w', encoding='utf-8', newline='\n') as f:
        f.write(html)
    print('  ', path)


def hero(title, text='', bg='slide-01', crumb=None, r=''):
    c = f'<div class="crumbs"><a href="{r}index.html">Inicio</a> / {crumb}</div>' if crumb else ''
    p = f'<p>{text}</p>' if text else ''
    return f'''<section class="page-hero">
  <div class="bg" style="background-image:url('{r}assets/img/{bg}.jpg')"></div>
  <div class="container">{c}<h1>{title}</h1>{p}</div>
  <div class="bar"></div>
</section>'''


def news_card(n, r='', featured=False):
    cls = 'card news-featured' if featured else 'card'
    return f'''<a class="{cls} reveal" href="{r}noticias/{n['slug']}.html" data-year="{n['date'][:4]}">
  <div class="card-media"><img src="{r}assets/img/{n['img']}.jpg" alt="" loading="lazy"></div>
  <div class="card-body">
    <span class="card-meta">{n['tag']} · {fdate(n['date'])}</span>
    <h3>{n['title']}</h3>
    <p>{n['summary']}</p>
    <span class="card-foot link-arrow">Leer noticia</span>
  </div>
</a>'''


def tabs(group, items, vertical=False, hash_=False):
    """items: list of (id, label_html, panel_html)"""
    btns, panels = [], []
    for k, (iid, label, panel) in enumerate(items):
        sel = 'true' if k == 0 else 'false'
        btns.append(f'<button role="tab" id="tab-{iid}" aria-controls="panel-{iid}" aria-selected="{sel}" tabindex="{0 if k == 0 else -1}">{label}</button>')
        panels.append(f'<div class="tabpanel" role="tabpanel" id="panel-{iid}" aria-labelledby="tab-{iid}"{"" if k == 0 else " hidden"}>{panel}</div>')
    cls = 'vtabs' if vertical else 'tabs'
    return f'''<div class="{cls}" data-tabs{" data-hash" if hash_ else ""}>
  <div class="tablist" role="tablist" aria-label="{group}">{''.join(btns)}</div>
  <div>{''.join(panels)}</div>
</div>'''


# ================================================================ páginas
def build_index():
    slides = [
        ('slide-01', 'Sede de Ikerlan'), ('slide-02', 'Edificio de Ikerlan'), ('slide-03', 'Entrada de Ikerlan'),
        ('slide-04', 'Vista aérea del Campus de Gijón'), ('slide-05', 'Edificio de Ikerlan'),
        ('slide-06', 'Instalaciones de Ikerlan'), ('slide-07', 'Campus de Gijón de la Universidad de Oviedo'),
        ('slide-08', 'Escuela Politécnica de Ingeniería de Gijón'),
    ]
    sl = ''.join(
        f'<div class="slide{" is-active" if k == 0 else ""}"><img src="assets/img/{s}.jpg" alt="{a}"{HI if k == 0 else LZ}></div>'
        for k, (s, a) in enumerate(slides))
    latest = ''.join(news_card(n) for n in NEWS[:3])
    body = f'''
<section class="hero" aria-roledescription="carrusel" aria-label="Imágenes de Ikerlan y la Universidad de Oviedo">
  <div class="slides">{sl}</div>
  <div class="container hero-content">
    <span class="eyebrow" style="color:var(--green)">Ikerlan · Universidad de Oviedo</span>
    <h1>Cátedra Ikerlan <span class="hl">de Investigación y Desarrollo</span></h1>
    <p>Desde 2019 reforzamos una colaboración de más de dos décadas entre el Centro Tecnológico Ikerlan y la Universidad de Oviedo.</p>
    <div class="hero-actions">
      <a class="btn btn--green" href="convocatoria.html">Convocatoria I+D+i 2025 {ICON["arrow"]}</a>
      <a class="btn btn--ghost" href="equipo.html">Conócenos</a>
    </div>
  </div>
  <div class="hero-controls">
    <button class="prev" type="button" aria-label="Imagen anterior">{ICON["left"]}</button>
    <span class="hero-counter" aria-live="polite">1 / 8</span>
    <button class="next" type="button" aria-label="Imagen siguiente">{ICON["right"]}</button>
  </div>
  <div class="container hero-dots" style="position:absolute;left:0;right:0;bottom:96px;z-index:3"><div class="dots"></div></div>
</section>

<div class="container quick">
  <nav class="quick-grid" aria-label="Accesos rápidos">
    <a href="equipo.html"><span class="ico">{ICON["people"]}</span><span>Quiénes somos<small>El equipo de la Cátedra</small></span></a>
    <a href="practicas.html"><span class="ico">{ICON["pencil"]}</span><span>Prácticas/becas<small>Becas de 600 €/mes</small></span></a>
    <a href="investigacion.html"><span class="ico">{ICON["chess"]}</span><span>Proyectos<small>Investigación conjunta</small></span></a>
    <a href="convocatoria.html"><span class="ico">{ICON["bulb"]}</span><span>Premios<small>Ayudas y convocatorias</small></span></a>
  </nav>
</div>

<section class="section">
  <div class="container split">
    <div class="reveal">
      <span class="eyebrow">Presentación</span>
      <h2>Conocimiento, talento joven y transferencia tecnológica</h2>
      <p class="lead">La Cátedra Ikerlan-Uniovi se firmó en octubre de 2019 con el objetivo de reforzar la colaboración, ya existente durante dos décadas, entre el Centro Tecnológico del País Vasco Ikerlan y la Universidad de Oviedo.</p>
      <p>Esta colaboración tiene como objeto la promoción del desarrollo del conocimiento, la formación de jóvenes investigadores y la transferencia de la tecnología a la sociedad. Los ámbitos de especialización se centran en tres grandes áreas:</p>
      <div class="areas">
        <div class="area">{ICON["chip"]}<h3>Tecnologías de Electrónica, Información y Comunicación</h3></div>
        <div class="area">{ICON["bolt"]}<h3>Energía y Electrónica de Potencia</h3></div>
        <div class="area">{ICON["gear"]}<h3>Fabricación Avanzada</h3></div>
      </div>
    </div>
    <div class="reveal">
      <div class="stats">
        <div class="stat"><b>+300</b><span>personas en la plantilla de Ikerlan</span></div>
        <div class="stat"><b>+1,5<em> M€</em></b><span>invertidos cada año en formación de estudiantes</span></div>
        <div class="stat"><b>6,25<em> %</em></b><span>de su facturación dedicado a formación</span></div>
        <div class="stat"><b>~100</b><span>estudiantes al año, de los que unos 40 son doctorandos</span></div>
      </div>
    </div>
  </div>
</section>

<section class="section section--soft">
  <div class="container split">
    <div class="reveal" style="order:2">
      <span class="eyebrow">Ikerlan</span>
      <h2>Un centro líder en transferencia tecnológica</h2>
      <p>Ikerlan, miembro del Basque Research and Technology Alliance (BRTA), es un centro líder en transferencia tecnológica y en la aportación de valor competitivo a la industria gracias, entre otros aspectos, a la especialización de sus investigadores.</p>
      <p>En 2018 IKERLAN logró la acreditación por parte de AENOR de su sistema de gestión integral (UNE-EN ISO 9001:2015 y UNE 166002:2014), lo que supone un reconocimiento de la excelencia del centro en el ámbito de la I+D+i. Actualmente cuenta con una plantilla de más de 300 trabajadores y anualmente invierte más de 1,5 M€ en la formación de estudiantes (6,25% de su facturación) con una media de 100 estudiantes por año, de los que aproximadamente 40 son doctorandos.</p>
      <div class="badge-row"><span class="badge badge--dark">BRTA</span><span class="badge">UNE-EN ISO 9001:2015</span><span class="badge">UNE 166002:2014</span><span class="badge">Acreditación AENOR</span></div>
    </div>
    <div class="reveal" style="order:1">
      <img src="assets/img/slide-02.jpg" alt="Sede de Ikerlan" loading="lazy" style="border-radius:var(--radius);box-shadow:var(--shadow-lg);width:100%">
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="feature reveal">
      <div class="feature-media"><img src="assets/img/concurso-ideas-portada.jpg" alt="Premiados del I Concurso de Ideas de la Cátedra Ikerlan" loading="lazy"></div>
      <div class="feature-body">
        <h2>Concurso ideas<small>Cátedra-Ikerlan</small></h2>
        <p>Durante la visita a Ikerlan el 26 de octubre de 2022 se celebró el I Concurso de Ideas de la Cátedra Ikerlan.</p>
        <p><strong>¡Enhorabuena a los premiados!</strong></p>
        <div class="hero-actions">
          <a class="btn btn--dark" href="noticias/i-concurso-ideas-catedra-ikerlan.html">Más {ICON["arrow"]}</a>
          <a class="btn btn--ghost" href="challenge-2023.html">Challenge 2023</a>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section section--soft">
  <div class="container">
    <div class="section-head"><div><span class="eyebrow">Actualidad</span><h2>Últimas noticias</h2></div><a class="link-arrow" href="noticias.html">Ver todas las noticias</a></div>
    <div class="grid grid-3">{latest}</div>
  </div>
</section>
'''
    page('index.html', 'Cátedra Ikerlan de Investigación y Desarrollo | Ikerlan · Universidad de Oviedo',
         'Cátedra Ikerlan-Uniovi: colaboración entre el Centro Tecnológico Ikerlan y la Universidad de Oviedo en formación, investigación y transferencia tecnológica.', body)


def build_equipo():
    def person(img, name, role):
        return f'<article class="person reveal"><img src="assets/img/{img}.jpg" alt="{name}" loading="lazy"><h3>{name}</h3><p>{role}</p></article>'
    body = f'''
{hero('Equipo', 'Profesores e investigadores de ambos centros que mantienen una estrecha relación de cooperación en formación e investigación.', 'slide-03', 'Equipo')}
<section class="section">
  <div class="container">
    <div class="split" style="align-items:start;margin-bottom:48px">
      <div>
        <span class="eyebrow">Quiénes somos</span>
        <h2>Lo más importante es el factor humano</h2>
      </div>
      <div>
        <p>La Cátedra de Ikerlan-Uniovi está formada por profesores e investigadores de ambos centros, los cuales han mantenido una estrecha relación de cooperación en tareas de formación de estudiantes (prácticas externas, TFGs, TFMs…) e investigación. Fruto de la excelente colaboración entre ambos centros se ha consolidado esta Cátedra.</p>
        <p>Si bien los resultados en investigación y formación han sido satisfactorios durante los últimos años, lo más importante para ambas instituciones es el factor humano. A continuación se presentan las personas involucradas en la Cátedra Ikerlan-Uniovi.</p>
      </div>
    </div>
    <div class="grid" style="grid-template-columns:2fr 3fr;gap:40px" id="equipos">
      <div>
        <div class="team-label"><h2>Equipo Uniovi</h2></div>
        <div class="people" style="grid-template-columns:repeat(auto-fill,minmax(200px,1fr))">
          {person('maria-jesus-lamela', 'María Jesús Lamela', 'Directora de la Cátedra Ikerlan')}
          {person('miguel-muniz', 'Miguel Muñiz Calvente', 'Profesor e Investigador DCIF')}
        </div>
      </div>
      <div>
        <div class="team-label"><h2>Equipo Ikerlan</h2></div>
        <div class="people" style="grid-template-columns:repeat(auto-fill,minmax(200px,1fr))">
          {person('unai-viscarret', 'Unai Viscarret', 'Director de Personas y Comunicación en IKERLAN')}
          {person('iker-urresti', 'Iker Urresti', 'Responsable de área Tecnologías Mecatrónicas')}
          {person('marco-gonzalez', 'Marco González', 'Responsable de Equipo AI &amp; Data')}
        </div>
      </div>
    </div>
  </div>
</section>
<section class="section--tight"><div class="container" style="padding-bottom:64px">
  <div class="cta"><div><h2>¿Quieres colaborar con la Cátedra?</h2><p>Escríbenos y te informaremos de prácticas, TFG/TFM y proyectos.</p></div><a class="btn btn--green" href="contacto.html">Contacta con nosotros {ICON["arrow"]}</a></div>
</div></section>
'''
    page('equipo.html', 'Equipo | Cátedra Ikerlan', 'Personas que forman la Cátedra Ikerlan-Uniovi: equipo de la Universidad de Oviedo y de Ikerlan.', body)


def build_convocatoria():
    BASES = 'https://www.funiovi.org/documents/223560/5879801/Bases+Convocatoria+ayudas+investigaci%C3%B3n/21fda878-6380-4b48-b244-28ecf2e094a7'
    ANEXO = 'https://www.funiovi.org/documents/223560/5879801/Anexo+III+-+Modelo+de+solicitud+IKERLAN/27272ae0-710e-4fe2-8781-98e363ca1da7'
    MAS = 'https://www.funiovi.org/-/catedra-ikerl-5'
    t = tabs('Detalles de la convocatoria', [
        ('objeto', 'Objeto', '<h3>Objeto de la convocatoria</h3><p>El objeto de esta convocatoria es promover la realización de proyectos de I+D+i que refuercen la colaboración entre el Centro Tecnológico Ikerlan y la Universidad de Oviedo y que fomenten la iniciación de estudiantes de Ingeniería en tareas de investigación y transferencia tecnológica.</p>'),
        ('ip', 'Investigador/a principal', '<h3>¿Quién puede solicitarla?</h3><p>El/la Investigador/a Principal que opte a esta convocatoria deberá ser profesor/a o investigador/a de la Universidad de Oviedo con contrato vigente, al menos, durante el periodo de desarrollo del proyecto presentado.</p>'),
        ('financiacion', 'Financiación', '<h3>Financiación</h3><p>La financiación permitirá formalizar periodos de prácticas extracurriculares a estudiantes de la Universidad de Oviedo, que estén cursando estudios oficiales de Grado y Máster, para facilitar su participación en actividades de I+D+i, como un primer paso a la realización de una Tesis Doctoral y su futura orientación profesional y/o investigadora.</p><p>La presente convocatoria financiará un total máximo de <strong>4 proyectos</strong> con una aportación bruta total de <strong>2.500 euros por proyecto</strong>. Los proyectos presentados deberán enmarcarse en una de las líneas de especialización definidas por Ikerlan, en las bases de la convocatoria. La no pertenencia a alguna de estas líneas implicará la no financiación del proyecto.</p>'),
        ('plazo', 'Plazo y solicitudes', f'<h3>Plazo y solicitudes</h3><p>El plazo de presentación comenzará el día siguiente al de publicación de esta convocatoria y finalizará 15 días naturales después, el <strong>26 de febrero de 2025</strong>, incluido.</p><p>Las solicitudes serán dirigidas a la Fundación Universidad de Oviedo antes del 26 de febrero de 2025, incluido.</p><p><a class="btn btn--dark btn--sm" href="{ANEXO}" target="_blank" rel="noopener">Modelo de solicitud (Anexo) {ICON["download"]}</a></p>'),
    ])
    premios = [n for n in NEWS if n['tag'] in ('Premios', 'Convocatoria', 'Concurso')][:4]
    body = f'''
{hero('Ayudas a la investigación <span class="hl">en proyectos I+D+i 2025</span>', 'En el marco de la Cátedra Ikerlan de Investigación y Desarrollo de la Universidad de Oviedo.', 'convocatoria-fondo-2', 'Convocatoria proyectos')}
<section class="section">
  <div class="container">
    <div class="facts">
      <div class="fact reveal">{ICON["euro"]}<b>2.500 €</b><span>por proyecto (máx. 4 proyectos)</span></div>
      <a class="fact reveal" href="{BASES}" target="_blank" rel="noopener">{ICON["book"]}<b>Bases</b><span>Consulta las bases de la convocatoria ↗</span></a>
      <div class="fact reveal">{ICON["cal"]}<b>26 feb 2025</b><span>Fin del plazo de solicitudes</span></div>
      <a class="fact reveal" href="{ANEXO}" target="_blank" rel="noopener">{ICON["pencil"]}<b>Anexo 1</b><span>Modelo de solicitud ↗</span></a>
    </div>
  </div>
</section>
<section class="section section--soft">
  <div class="container split" style="align-items:start">
    <div>{t}</div>
    <aside class="reveal">
      <div class="card card--line"><div class="card-body">
        <span class="card-meta">Fundación Universidad de Oviedo</span>
        <h3>Más información</h3>
        <p>Toda la documentación oficial de la convocatoria está publicada por la Fundación Universidad de Oviedo.</p>
        <div class="card-foot" style="display:flex;gap:10px;flex-wrap:wrap">
          <a class="btn btn--green btn--sm" href="{MAS}" target="_blank" rel="noopener">funiovi.org {ICON["ext"]}</a>
          <a class="btn btn--ghost btn--sm" href="{BASES}" target="_blank" rel="noopener">Bases {ICON["download"]}</a>
        </div>
      </div></div>
    </aside>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="section-head"><div><span class="eyebrow">Premios Cátedra Ikerlan</span><h2>Premios y convocatorias anteriores</h2></div><a class="link-arrow" href="noticias.html">Todas las noticias</a></div>
    <div class="grid grid-4">{''.join(news_card(n) for n in premios)}</div>
  </div>
</section>
'''
    page('convocatoria.html', 'Convocatoria proyectos I+D+i 2025 | Cátedra Ikerlan',
         'Ayudas a la investigación en proyectos I+D+i 2025 de la Cátedra Ikerlan de la Universidad de Oviedo: 2.500 € por proyecto.', body)


def build_estudiantes():
    vids = [('BSxfhJ1263w', 'Experiencia Oscar Seijo', 'video-oscar-seijo'),
            ('4KvMcKTQ0cw', 'Experiencia Mario Cabello', 'video-mario-cabello'),
            ('BPdkhxVXu8I', 'Experiencia Fernando González', 'video-fernando-gonzalez')]
    vl = ''.join(f'<button type="button" data-id="{i}" data-title="{t}" data-thumb="assets/img/{img}.jpg" aria-pressed="false"><img src="assets/img/{img}.jpg" alt="" loading="lazy"><span><b>{t}</b><small>Vídeo · YouTube</small></span></button>' for i, t, img in vids)
    body = f'''
{hero('Estudiantes', 'Prácticas, TFG/TFM, becas y formación: vive experiencias reales con las tecnologías y laboratorios más punteros.', 'slide-05', 'Estudiantes')}
<section class="section">
  <div class="container">
    <div class="section-head"><div><span class="eyebrow">Testimonios</span><h2>Algunas experiencias</h2></div><p class="muted" style="margin:0;max-width:420px">Egresados que han pasado por Ikerlan nos cuentan su experiencia.</p></div>
    <div class="video-stage" data-videos>
      <div class="video-main"></div>
      <div class="video-list">{vl}</div>
    </div>
  </div>
</section>
<section class="section section--soft">
  <div class="container">
    <div class="section-head"><div><span class="eyebrow">Oportunidades</span><h2>Prácticas y proyectos para estudiantes</h2></div></div>
    <div class="grid grid-3">
      <article class="card reveal">
        <div class="card-media"><img src="assets/img/cursos-formacion.jpg" alt="Espacio de formación" loading="lazy"></div>
        <div class="card-body"><span class="card-meta">Formación</span><h3>Cursos y formación</h3>
          <p>Desde la Cátedra Ikerlan-Uniovi se impulsa la realización de cursos de formación para estudiantes y personal investigador de ambas instituciones.</p>
          <p>En esta página web podrá encontrar enlaces a los diferentes cursos ofertados.</p></div>
      </article>
      <a class="card reveal" href="practicas.html">
        <div class="card-media"><img src="assets/img/slide-01.jpg" alt="Sede de Ikerlan" loading="lazy"></div>
        <div class="card-body"><span class="card-meta">Prácticas</span><h3>Prácticas en Ikerlan</h3>
          <p>En Ikerlan es posible realizar prácticas remuneradas durante el curso o en verano.</p>
          <span class="card-foot link-arrow">Ver prácticas y becas</span></div>
      </a>
      <a class="card reveal" href="tfg-tfm.html">
        <div class="card-media"><img src="assets/img/tfg-tfm.jpg" alt="TFG y TFM con Ikerlan" loading="lazy"></div>
        <div class="card-body"><span class="card-meta">TFG / TFM</span><h3>TFGs y TFMs en Ikerlan o en Uniovi</h3>
          <p>Tanto en Ikerlan como en Uniovi te ofrecemos la posibilidad de realizar trabajos fin de grado y fin de máster en un entorno tecnológico.</p>
          <span class="card-foot link-arrow">Ver propuestas</span></div>
      </a>
    </div>
  </div>
</section>
<section class="section"><div class="container">
  <div class="cta"><div><h2>Ikerlan Challenge 2023</h2><p>Concurso de ideas para estudiantes de Grado y Máster con premios de hasta 600 €.</p></div><a class="btn btn--green" href="challenge-2023.html">Ver el concurso {ICON["arrow"]}</a></div>
</div></section>
'''
    page('estudiantes.html', 'Estudiantes | Cátedra Ikerlan', 'Experiencias, cursos, prácticas y TFG/TFM para estudiantes en Ikerlan y la Universidad de Oviedo.', body)


def build_tfg():
    becados = ['Desarrollo de una APP para la asistencia en el cálculo de vida a fatiga y el análisis modal operacional',
               'Desarrollo de un programa para la interpretación de resultados en tiempo real en ensayos de crecimiento de grieta por fatiga',
               'ProFatigue 2.0: Mejora y actualización de software para el ajuste del campo S-N',
               'Estudio de metodologías para el cálculo de vida a fatiga en el dominio de la frecuencia',
               'Estudio de técnicas de optimización aplicadas al diseño de elementos estructurales o mecánicos mediante simulación numérica',
               'Metodología para la readaptación de modelos numéricos mediante técnicas de optimización',
               'Estudio numérico-experimental de la influencia de sobrecargas en el crecimiento de grietas por fatiga',
               'Estimación de tensiones en estructuras sometidas a cargas dinámicas',
               'Cálculo numérico de una pasarela peatonal',
               'Fabricación, validación y puesta en servicio de un sistema para la asistencia en la calibración de equipos de correlación digital de imágenes',
               'Influencia de la frecuencia de ensayo en la caracterización de vida a fatiga',
               'Influencia de la tensión media en la caracterización de la vida a fatiga del acero estructural S275 y en la acumulación de daño a fatiga',
               'Estudio del impacto de las condiciones de mecanizado en la caracterización de vida a fatiga',
               'Estudio experimental del crecimiento de grieta por fatiga del acero S275']
    otros = ['Integridad estructural en componentes de fabricación aditiva', 'Banco de ensayos de fatiga para el sector eólico',
             'Diseño mecatrónico para la instalación de equipos de grandes dimensiones',
             'Estimación de desgaste en juntas por efecto de fricción y holguras mediante simulación dinámica de sistemas multicuerpo',
             'Monitorización de la condición de instalaciones de ascensor', 'Monitorización de rodamientos pitch de un aerogenerador',
             'Structural Health Monitoring: stress estimation and monitoring', 'Diseño de un driver inteligente para semiconductores MOSFET de SiC',
             'Sistemas de comunicación Ethernet para aplicaciones industriales de control con requisitos real-time',
             'Extensión inalámbrica para soluciones de control industrial con requisitos tiempo real',
             'Extensión inalámbrica tiempo real para control con requisitos de bajo consumo',
             'Estudio de plataformas SDR para aplicaciones C-V2X basadas en LTE',
             'Emulador de canal inalámbrico RF sobre plataformas de alto rendimiento MPSoC de Xilinx',
             'Integración de modem WiFi tiempo real sobre plataformas System-on-Chip basadas en Linux']
    gal = [('inv-crecimiento-grietas', 'Ensayo de crecimiento de grieta'), ('tesis-mikel-portada', 'Simulación numérica de grieta'),
           ('ikerlan-sede-2', 'Sede de Ikerlan'), ('premios-2020-fruela-pelayo', 'Premios Cátedra Ikerlan 2020'),
           ('inv-corrosion', 'Defecto por corrosión'), ('inv-multiaxial', 'Daño por fatiga multiaxial'),
           ('slide-07', 'Campus de Gijón'), ('slide-04', 'Vista aérea del campus'), ('slide-01', 'Sede de Ikerlan'),
           ('inv-basquin', 'Modelo de Basquin')]
    ul = lambda xs: '<ul class="list-check">' + ''.join(f'<li>{x}</li>' for x in xs) + '</ul>'
    g = '<div class="gallery">' + ''.join(f'<button type="button" data-lightbox="tfg"><img src="assets/img/{i}.jpg" alt="{a}" loading="lazy"></button>' for i, a in gal) + '</div>'
    t = tabs('Trabajos TFG/TFM', [
        ('becados', 'Propuestas con beca 400 €/mes', '<p class="muted">Ejemplos de propuestas de TFG/TFM en cursos anteriores con beca de 400 €/mes.</p>' + ul(becados)),
        ('otros', 'Otros TFG/TFM realizados en Ikerlan', ul(otros)),
        ('galeria', 'Galería', g),
    ])
    body = f'''
{hero('TFG / TFM', 'Ejemplos de TFM y TFG desarrollados en colaboración con IKERLAN.', 'tfg-tfm', 'Estudiantes / TFG/TFM')}
<section class="section">
  <div class="container split">
    <div class="reveal">
      <span class="eyebrow">Trabajos fin de estudios</span>
      <h2>Haz tu TFG o TFM en un entorno tecnológico</h2>
      <p>Tanto en Ikerlan como en Uniovi te ofrecemos la posibilidad de realizar trabajos fin de grado y fin de máster en un entorno tecnológico. En el caso de que escojas hacer tu TFG/TFM en Ikerlan, ambas opciones están remuneradas.</p>
      <p>En el caso de que escojas realizarlo en Uniovi, ponte en contacto con los profesores encargados de la Cátedra Ikerlan para que te informen de los proyectos que serán becados. Nuestra intención es que los mejores estudiantes de cada promoción obtengan una beca y puedan disfrutar de la experiencia de ir más allá en su aprendizaje y quieran vivir experiencias reales con las tecnologías y laboratorios más punteros.</p>
      <div class="note">Si estás interesado en realizar el TFG/TFM en colaboración con IKERLAN (ya sea desplazándote a sus instalaciones en Mondragón/Arrasate o incorporándote a un Grupo de Investigación en la EPI-Gijón) ponte en <a href="contacto.html">contacto con nosotros</a> (<a href="mailto:munizcmiguel@uniovi.es">munizcmiguel@uniovi.es</a>).</div>
    </div>
    <div class="reveal"><img src="assets/img/tfg-tfm.jpg" alt="TFM y TFG con Ikerlan" style="border-radius:var(--radius);box-shadow:var(--shadow-lg);width:100%"></div>
  </div>
</section>
<section class="section section--soft"><div class="container">{t}</div></section>
'''
    page('tfg-tfm.html', 'TFG / TFM | Cátedra Ikerlan', 'Propuestas y ejemplos de TFG y TFM realizados en colaboración con Ikerlan.', body)


def build_practicas():
    becas = [
        ('Desarrollo modelo 3D para simular cierre de grieta en fatiga', 'Febrero-Junio 2021', 'Desarrollo de modelos de elementos finitos avanzados en Abaqus para la simulación del crecimiento de grieta por fatiga considerando la influencia de la plasticidad y la forma del frente de grieta.', 'Mario Martín Blanco'),
        ('Estudio efecto de escala en fallo de rodamientos de grandes dimensiones', 'Febrero-Abril 2021', 'Aplicación del GLM a la predicción de vida a fatiga de rodamientos de diferentes dimensiones.', 'Antonio Llera Iglesias'),
        ('Desarrollo de modelos biomecánicos de la articulación temporomandibular', '15/12/2020 – 15/03/2021', 'Desarrollo de modelos biomecánicos de elementos finitos en Abaqus.', 'Natalia García'),
        ('Asistencia en el desarrollo de Abaqus2MatLab', '01/11/2020 – 28/02/2021', 'Desarrollo de modelos de elementos finitos avanzados en Abaqus y generación de código en MatLab para la interacción con los mismos.', 'Fruela de la Roza Palicio'),
        ('Implementación de métodos experimentales y numéricos alternativos para la caracterización del crecimiento de grietas a fatiga', '03/02/2020 – 30/04/2020 y 05/10/2020 – 05/11/2020', 'Ejecución de una campaña experimental en probetas de diferentes espesores y análisis de resultados. Desarrollo de un modelo de elementos finitos (Abaqus) para predecir la propagación de grietas a fatiga.', 'Mario López'),
        ('Cálculos avanzados de fiabilidad estructural (fatiga, optimización, cálculo no lineal, etc.)', '01/11/2019 – 31/01/2020', 'Uso de software para realizar simulaciones por elementos finitos (Ansys, Abaqus o RFEM). Desarrollo de manuales, vídeos y ejercicios prácticos del software utilizado. Estudio de funcionalidades sobre fiabilidad estructural integradas en software comercial de cálculo numérico.', 'Daniel Álvarez González'),
        ('Estudio del comportamiento estático y dinámico de elementos estructurales de vidrio monolítico y laminado', None, 'Uso de programas de cálculo numérico, incluyendo consideraciones de viscoelasticidad y fatiga. Implementación en Matlab de un software de cálculo de elementos estructurales de vidrio.', 'Alberto Justo Lobato'),
        ('Simulación numérica de ensayos de fractura y fatiga de polímeros con probetas lisas y entalladas', '01/10/2019 – 31/01/2020', 'Cálculos numéricos y aplicación de modelos probabilísticos a la caracterización de la fractura y fatiga de polímeros.', 'Lucas Venta Viñuela'),
        ('Fiabilidad estructural y caracterización de materiales', '17/12/2018 – 31/12/2019', 'Programas experimentales y cálculos mediante elementos finitos en el campo de la fiabilidad estructural y caracterización de materiales.', 'Marta Casasola'),
        ('Análisis a fatiga de materiales poliméricos', 'Junio 2018', 'Realización de ensayos de caracterización a fatiga de materiales poliméricos.', 'Adrián Álvarez Vázquez'),
    ]
    ini = lambda n: ''.join(w[0] for w in n.split()[:2])
    cards = ''.join(f'''<article class="beca" data-item>
  <h3>{t}</h3>
  <dl>{f"<div><dt>Duración de la beca</dt><dd>{d}</dd></div>" if d else ""}<div><dt>Actividades de investigación</dt><dd>{a}</dd></div></dl>
  <div class="who"><span class="avatar">{ini(p)}</span><span><small class="muted" style="display:block;font-weight:400;font-size:.75rem">Persona asignada</small>{p}</span></div>
</article>''' for t, d, a, p in becas)
    temas = ['Fiabilidad estructural', 'Materiales', 'Fabricación', 'Electrónica', 'Energía', 'Ciberseguridad', 'Telecomunicaciones', 'Análisis de Datos', 'IA']
    body = f'''
{hero('Prácticas y becas', 'Realiza tus prácticas sin moverte de la EPI-Gijón gracias a la «Sala Cátedra-Ikerlan».', 'slide-06', 'Estudiantes / Prácticas')}
<section class="section">
  <div class="container split" style="align-items:start">
    <div class="reveal">
      <span class="eyebrow">Próximas becas y contratos</span>
      <h2>Prácticas sin moverte de la EPI-Gijón</h2>
      <p>En el marco de la Cátedra Ikerlan de Investigación y Desarrollo es posible realizar las prácticas sin moverte de la EPI-Gijón, gracias a nuestra «Sala Cátedra-Ikerlan» disponible en el Edificio Departamental Oeste de UNIOVI.</p>
      <p>Siempre estamos buscando gente implicada y proactiva en cualquiera de las temáticas en las que investiga y desarrolla producto Ikerlan:</p>
      <div class="badge-row" style="margin-bottom:20px">{''.join(f'<span class="badge">{x}</span>' for x in temas)}</div>
      <p>Si quieres más información, puedes enviarnos un correo y/o tu CV a los <a href="equipo.html">profesores vinculados a la Cátedra Ikerlan</a> (<a href="mailto:munizcmiguel@uniovi.es">munizcmiguel@uniovi.es</a>).</p>
      <div class="hero-actions"><a class="btn btn--green" href="mailto:munizcmiguel@uniovi.es?subject=Becas%20C%C3%A1tedra%20Ikerlan">Envía tu CV {ICON["mail"]}</a><a class="btn btn--ghost" href="contacto.html">Contacta con nosotros</a></div>
    </div>
    <div class="stats reveal">
      <div class="stat"><b>≥ 4</b><span>becarios previstos cada año</span></div>
      <div class="stat"><b>600<em> €</em></b><span>al mes de beca</span></div>
      <div class="stat"><b>3–4</b><span>meses de duración</span></div>
      <div class="stat"><b>EPI</b><span>Sala Cátedra-Ikerlan en Gijón</span></div>
    </div>
  </div>
</section>
<section class="section section--soft">
  <div class="container" data-pager="6">
    <div class="section-head"><div><span class="eyebrow">Histórico</span><h2>Algunos ejemplos de becas y contratos anteriores</h2></div></div>
    <div class="pager-grid">{cards}</div>
    <div class="pager" aria-label="Paginación"></div>
  </div>
</section>
'''
    page('practicas.html', 'Prácticas y becas | Cátedra Ikerlan', 'Becas y contratos de la Cátedra Ikerlan: prácticas remuneradas de 600 €/mes en la EPI de Gijón.', body)


def pub(title, authors, journal, url=None):
    t = f'<a href="{url}" target="_blank" rel="noopener">{title}</a>' if url else title
    return f'<li><strong>{t}</strong><span>{authors}</span><em>{journal}</em></li>'


def build_investigacion():
    lines = [
        ('crecimiento', 'inv-crecimiento-grietas', 'Desarrollo de modelos de predicción de crecimiento de grietas por fatiga',
         '<p>En los últimos años, se han llevado a cabo diferentes trabajos encaminados a mejorar las técnicas y metodologías actuales para la predicción del crecimiento de grietas por fatiga, permitiendo tomar mejores decisiones RUN/REPAIR/REPLACE.</p><p>Algunos ejemplos de los resultados obtenidos pueden verse en los siguientes artículos científicos:</p>',
         [pub('Distribution of the effective stress intensity factor range through thickness: influence on fatigue crack growth rate curves', 'G. Calvín, M. Escalero, H. Zabala, M. Muñiz-Calvente', 'Theoretical and Applied Fracture Mechanics (under review), 2021'),
          pub('Fatigue Assessment of Selective Laser Melted Ti-6Al-4V: Influence of Speed Manufacturing and Porosity', 'U. Segurajauregi, A. Álvarez-Vázquez, M. Muñiz-Calvente, Í. Urresti', 'Metals 11 (7), 1022, 2021'),
          pub('Suitability of constraint and closure models for predicting crack growth in generic configurations', 'Escalero, M., Muniz-Calvente, M., Zabala, H., Urresti, I.', 'Engineering Fracture Mechanics, 2020, 225, 106808'),
          pub('A methodology for simulating plasticity induced crack closure and crack shape evolution based on elastic–plastic fracture parameters', 'Escalero, M., Muniz-Calvente, M., Zabala, H., … Branco, R., Antunes, F.V.', 'Engineering Fracture Mechanics, 2020, 107412'),
          pub('Study of alternatives and experimental validation for predictions of hole-edge fatigue crack growth in 42CrMo4 steel', 'Escalero, M., Blasón, S., Zabala, H., … Muniz-Calvente, M., Fernández-Canteli, A.', 'Engineering Structures, 2018, 176, pp. 621–631')],
         'Muchas de estas investigaciones han sido desarrolladas en el marco de las tesis doctorales desarrolladas por investigadores de Ikerlan y dirigidas por profesores de UNIOVI.'),
        ('basquin', 'inv-basquin', 'Mejorando los modelos de fatiga lineal y bi-lineal de Basquin mediante la inclusión de aspectos probabilísticos y el efecto de escala',
         '<p>En un trabajo de colaboración entre Ikerlan y Uniovi se ha desarrollado una metodología probabilística que permite abandonar el enfoque determinista de los comúnmente utilizados «ajustes lineales del campo S-N», basados en la ley de Basquin.</p><p>El resultado de la investigación ha sido publicado en Engineering Failure Analysis, revista JCR (Q1).</p>',
         [pub('Improving with probabilistic and scale features the Basquin linear and bi-linear fatigue models', 'Usabiaga, H., Muniz-Calvente, M., Ramalle, M., Urresti, I., Fernández Canteli, A.', 'Engineering Failure Analysis, 2020, 116, 104728', 'https://www.sciencedirect.com/science/article/pii/S1350630720306981')],
         None),
        ('corrosion', 'inv-corrosion', 'Estudio de la influencia de los defectos generados por corrosión en la vida a fatiga de componentes y estructuras',
         '<p>En esta línea de investigación conjunta se ha estudiado la forma de generar corrosiones aceleradas sobre materiales metálicos con el objetivo de obtener defectos superficiales similares a los obtenidos en componentes sumergidos en agua marina.</p><p>Posteriormente, estos componentes han sido ensayados bajo cargas cíclicas para obtener su vida a fatiga y determinar la reducción de vida asociada al proceso de corrosión, la cual puede ser estimada mediante mecánica de la fractura si se conocen la geometría de los defectos superficiales inducidos.</p>',
         [pub('Fatigue life estimation of pre-corroded 42CrMo4 subjected to accelerated pitting corrosion method', 'M. Álvarez, M. Muñiz-Calvente, I. Urresti, M. Escalero, J. Gracia', 'International Journal of Fracture, 2021')],
         None),
        ('multiaxial', 'inv-multiaxial', 'Desarrollo de metodología para evaluar el daño por fatiga bajo cargas aleatorias multiaxiales',
         '<p>Gracias a la colaboración Ikerlan-Uniovi, se han realizado importantes avances en las metodologías para la predicción de la vida a fatiga de componentes sometidos a cargas aleatorias multiaxiales.</p><p>Algunos ejemplos de los resultados obtenidos pueden verse en los siguientes artículos científicos:</p>',
         [pub('Pitch bearing lifetime prediction considering the effect of pitch control strategy', 'Lopez, A., Zurutuza, A., Olave, M., … Muniz-Calvente, M., Fernandez-Canteli, A.', 'Journal of Physics: Conference Series, 2019, 1222(1), 012017'),
          pub('A comparative analysis of multiaxial fatigue models under random loading', 'Portugal, I., Olave, M., Urresti, I., … Muñiz-Calvente, M., Fernández-Canteli, A.', 'Engineering Structures, 2019, 182, pp. 112–122'),
          pub('Methodology to evaluate fatigue damage under multiaxial random loading', 'Portugal, I., Olave, M., Zurutuza, A., … Muñiz-Calvente, M., Fernández-Canteli, A.', 'Engineering Fracture Mechanics, 2017, 185, pp. 114–123')],
         'Estas investigaciones han sido desarrolladas en el marco de la tesis doctoral de Ibai Portugal, quien fue al mismo tiempo investigador en Ikerlan y estudiante de doctorado en UNIOVI.'),
    ]
    short = {'crecimiento': 'Crecimiento de grietas por fatiga', 'basquin': 'Modelos probabilísticos de Basquin',
             'corrosion': 'Corrosión y vida a fatiga', 'multiaxial': 'Fatiga bajo cargas multiaxiales'}
    items = []
    for iid, img, title, text, pubs, note in lines:
        n = f'<p class="note">{note}</p>' if note else ''
        panel = f'''<div class="research-panel">
  <div><span class="eyebrow">Línea de investigación</span><h2 style="font-size:1.5rem">{title}</h2>{text}<ul class="pubs">{''.join(pubs)}</ul>{n}</div>
  <figure><button type="button" data-lightbox="inv" style="padding:0;border:0;background:none;cursor:zoom-in;width:100%"><img src="assets/img/{img}.jpg" alt="{short[iid]}" loading="lazy"></button></figure>
</div>'''
        items.append((iid, f'<img src="assets/img/{img}.jpg" alt="" loading="lazy"><span>{short[iid]}</span>', panel))
    body = f'''
{hero('Investigación', 'Proyectos de investigación y publicaciones conjuntas entre Ikerlan y la Universidad de Oviedo.', 'inv-crecimiento-grietas', 'Investigación')}
<section class="section"><div class="container">{tabs('Líneas de investigación', items, vertical=True, hash_=True)}</div></section>
'''
    page('investigacion.html', 'Investigación | Cátedra Ikerlan', 'Proyectos de investigación y publicaciones conjuntas Ikerlan-Uniovi: fatiga, crecimiento de grietas, corrosión y cargas multiaxiales.', body)


def build_challenge():
    def sr(tag, title, html):
        return f'<details><summary><span class="tag">{tag}</span>{title}</summary><div class="acc-body">{html}</div></details>'
    r1 = [
        sr('SR1', 'Sistemas de clasificación de e-waste basándose en visión artificial', '<p>Este subreto tratará de desarrollar sistemas de identificación y clasificación de residuos electrónicos basándose en visión artificial. Dichos desarrollos deberían ir orientados a dotar a la planta de reciclaje de la capacidad de discretizar los residuos en el mayor número de grupos posibles en función de diferentes características del material electrónico, facilitando así la customización de su manipulación a posteriori. Los sistemas desarrollados podrán orientarse a la clasificación por tipología de e-waste (partir de un contenedor de múltiples tipos de e-waste mezclados con objetivo de separarlos), a la separación de sus componentes triturados u otras tareas que se identifiquen como necesarias en una planta de e-waste.</p>'),
        sr('SR2', 'Desarrollo de máquinas o robots de clasificación o separación', '<p>Este subreto consistirá en el desarrollo mecatrónico de máquinas, mecanismos o robots innovadores para los sistemas de manipulación o clasificación de los residuos. Dichos desarrollos deberían ir orientados a maximizar la capacidad de procesado de las líneas de reciclaje, mejorando el porcentaje de residuos reciclados. Los sistemas desarrollados podrán orientarse a la clasificación de tipología de e-waste (partir de un contenedor de múltiples tipos de e-waste mezclados con objetivo de separarlos), a la separación de sus componentes triturados u otras tareas que se identifiquen como necesarias en una planta de e-waste. Deberán ser sistemas de alta velocidad y dinámica, con capacidad de adaptación a diferentes tipos de residuos. Se deberán considerar los sistemas de actuación, estructuras y componentes mecánicos, sistemas de agarre/manipulación, así como la electrónica (PLC o similar) y el control de los diferentes ejes/actuadores.</p>'),
        sr('SR3', 'Dispositivo Edge (HW/FW/Comunicaciones 5G/Seguridad)', '<p>Desarrollo de un sistema de monitorización con conectividad 5G que permita realizar la identificación y clasificación automática de los diferentes tipos de residuos electrónicos. El dispositivo debe tener capacidad de integrar diferentes sensores y cámaras que permitan realizar esta identificación y clasificación de forma autónoma, realizando una ejecución en tiempo real de los algoritmos que permitan controlar otros dispositivos, robots o actuadores dentro de la línea de reciclaje.</p><p>Se debe tener en cuenta la selección del hardware con la capacidad necesaria de conectividad y procesamiento, la arquitectura software, visualización de datos local y comunicaciones con la nube. El dispositivo debe disponer de los mecanismos de seguridad hardware y software necesarios para proteger el acceso no autorizado al sistema, la protección de datos almacenados y la transmisión de las comunicaciones. Se debe maximizar la disponibilidad de planta, garantizar la operación óptima y generar información de interés para implantar políticas de mantenimiento predictivo.</p>'),
        sr('SR4', 'Plataforma Cloud cibersegura con capacidades de IA', '<p>Desarrollo de una plataforma Cloud cibersegura con capacidad de entrenar modelos de Inteligencia Artificial. La plataforma debe ser capaz de recibir y almacenar datos e imágenes de dispositivos situados en diferentes líneas de reciclaje situadas por todo el mundo. Utilizando estos datos, la plataforma debe entrenar modelos de Inteligencia Artificial a partir de imágenes que puedan detectar y clasificar diferentes tipos de e-waste. La plataforma debe ser capaz de descargar estos modelos en los dispositivos Edge para que estos realicen una identificación local. La plataforma debe contemplar las políticas de seguridad necesarias para proteger el acceso malicioso, el cifrado de los datos, la comunicación segura con los dispositivos remotos y los interfaces de comunicación con usuario. La plataforma debe ofrecer al usuario una interfaz web donde pueda visualizar las diferentes plantas de e-waste, los dispositivos conectados, su telemetría y datos, así como el resultado de la inferencia de los modelos entrenados. La plataforma puede estar basada en cloud público (AWS, Azure, etc.) o en cloud privado.</p>'),
    ]
    r2 = [
        sr('SR1', 'Desarrollo mecatrónico del robot o drone (semi)autónomo', '<p>Este subreto consiste en idear y desarrollar un robot o drone (semi) autónomo innovador, orientado a cumplir las especificaciones del enlace proporcionado. Será de relevancia considerar la navegabilidad por la estructura, la precisión de posicionamiento, la capacidad de amarre a la estructura (en caso de reapriete puede haber un momento de reacción del orden de 500 N·m), sus sistemas mecánicos, actuadores y electrónica básica de control.</p>'),
        sr('SR2', 'Integridad estructural del sistema de apriete del robot', '<p>En este reto se analizará la integridad estructural y fiabilidad mecánica del sistema de apriete del robot para su correcto dimensionamiento. El análisis deberá ir orientado a garantizar las especificaciones del enlace proporcionado en cuanto a par de apriete y ambiente hostil, a su vez buscando que el sistema sea lo más ligero posible, lo que permitiría una integración óptima en el robot.</p>'),
        sr('SR3', 'Robot inteligente (HW/FW/Comunicaciones/Seguridad)', '<p>Desarrollo de un sistema Edge con conectividad que permita realizar el funcionamiento autónomo del robot. El dispositivo debe tener capacidad de integrar diferentes sensores y cámaras que permitan realizar una inspección y sustitución autónoma de los tornillos, realizando una ejecución en tiempo real de los algoritmos que permitan al robot desplazarse, localizar los tornillos en base a visión artificial, identificar el estado y salud estructural de los tornillos e interactuar con ellos para su sustitución.</p><p>Es clave que este tipo de soluciones consideren la necesidad de llevar a cabo el procesamiento in situ, sin necesidad de optar por sistemas de procesamiento remoto. Será crucial buscar un equilibrio entre precisión y agilidad de procesamiento con el fin de que esta labor se lleve a cabo en un tiempo asumible. También será de interés el desarrollo de un sistema de toma de decisión para la sustitución de tornillos. Para ello será crucial tener en cuenta el histórico de las inspecciones llevadas a cabo, con el fin de conocer evoluciones de degradación y determinar la acción de mantenimiento a realizar, buscando una minimización del riesgo y de las intervenciones necesarias.</p><p>Se debe tener en cuenta la selección del hardware con la capacidad necesaria de procesamiento, la arquitectura software y comunicaciones con la nube y con otros robots. El dispositivo debe disponer de los mecanismos de ciberseguridad y seguridad funcional que eviten que el robot pueda ser hackeado o que durante su operación pueda interferir con operarios humanos. Los robots deben ser capaces de funcionar, comunicarse, sincronizarse y operar de forma colaborativa cuando sea necesario, repartiéndose las tareas para aumentar la eficiencia del sistema. Se debe proponer un sistema de comunicaciones que permita la comunicación P2P entre robots, así como la comunicación con una nube, teniendo en cuenta que las plataformas eólicas offshore pueden estar en zonas con cobertura celular baja.</p>'),
        sr('SR4', 'Plataforma Cloud cibersegura con capacidades de IA', '<p>Desarrollo de una plataforma Cloud cibersegura con capacidad de entrenar modelos de Inteligencia Artificial. La plataforma debe ser capaz de recibir y almacenar datos e imágenes de robots situados en diferentes plataformas offshore situadas por todo el mundo. Utilizando estos datos, la plataforma debe entrenar modelos de Inteligencia Artificial a partir de imágenes que puedan detectar los tornillos, determinar su estado, establecer rutas de navegación, etc. La plataforma debe ser capaz de descargar estos modelos en los dispositivos Edge para que estos realicen una identificación local offline. La plataforma debe contemplar las políticas de seguridad necesarias para proteger el acceso malicioso, el cifrado de los datos, la comunicación segura con los dispositivos remotos y los interfaces de comunicación con usuario. La plataforma debe ofrecer al usuario una interfaz web donde pueda visualizar los diferentes robots conectados, su telemetría y datos, así como el resultado de la inferencia de los modelos entrenados. La plataforma puede estar basada en cloud público (AWS, Azure, etc.) o en cloud privado.</p>'),
    ]
    def reto(img, alt, title, desc, srs):
        return f'''<div class="split" style="align-items:start;gap:32px">
  <div><h3 style="font-size:1.35rem">{title}</h3>{desc}</div>
  <figure style="margin:0"><button type="button" data-lightbox="retos" style="padding:0;border:0;background:none;cursor:zoom-in;width:100%"><img src="assets/img/{img}.jpg" alt="{alt}" loading="lazy" style="border-radius:var(--radius);box-shadow:var(--shadow);width:100%"></button></figure>
</div>
<h4 style="margin:28px 0 12px">Subretos (elige 1 ó 2)</h4>
<div class="accordion">{''.join(srs)}</div>'''
    t = tabs('Retos del concurso', [
        ('reto1', 'Reto 1 · Reciclaje de residuos electrónicos', reto('reto-1-ewaste', 'Residuos electrónicos', 'Desarrollo de un sistema de reciclaje automatizado para residuos electrónicos',
            '<p>Los residuos electrónicos, también conocidos como e-waste, son una creciente preocupación a nivel mundial debido a su impacto ambiental y a la necesidad de recuperar materiales valiosos. Este reto implica el diseño y desarrollo de un sistema automatizado para la clasificación, desmontaje y reciclaje de residuos electrónicos. La planta deberá considerar aspectos como la identificación de diferentes tipos de residuos electrónicos, la extracción segura de componentes y materiales valiosos, y la minimización de los residuos finales.</p>', r1)),
        ('reto2', 'Reto 2 · Robot para turbinas eólicas offshore', reto('reto-2-eolica', 'Generador de turbina eólica offshore', 'Desarrollo de un sistema robótico para la inspección y el apriete autónomo de tornillos en turbinas eólicas offshore',
            '<p>Las turbinas eólicas offshore, como la serie GE Haliade-X, Vestas V236 o Siemens-Gamesa SG14, son esenciales para la generación de energía renovable. Sin embargo, el mantenimiento de estas turbinas, especialmente la inspección y el reemplazo de tornillos de los generadores de accionamiento directo (Direct Drive), es un proceso laborioso y potencialmente peligroso que actualmente se realiza mediante acceso por cuerda. La automatización de este proceso puede mejorar la eficiencia, reducir costos y mejorar la seguridad.</p><p>El objetivo de este reto es desarrollar un sistema robótico que pueda navegar de forma autónoma o semi-autónoma por la superficie exterior del generador de una turbina eólica offshore, identificar tornillos que requieran inspección, apriete o reemplazo, y realizar las tareas necesarias. Este reto está inspirado en el <a href="https://iuk.ktn-uk.org/opportunities/ktn-ix-challenge-robotics-platform-generator-bolt-inspection-and-tightening/" target="_blank" rel="noopener">KTN-iX Challenge</a>.</p>', r2)),
    ])
    body = f'''
{hero('Ikerlan <span class="hl">Challenge 2023</span>', 'Concurso de ideas de la Cátedra Ikerlan para estudiantes de Grado y Máster.', 'concurso-ideas-2022-4', 'Estudiantes / Challenge 2023')}
<section class="section">
  <div class="container split" style="align-items:start">
    <div class="reveal">
      <span class="eyebrow">Objetivo</span>
      <h2>Innovación, talento y nuevas ideas con impacto</h2>
      <p>El objetivo del IKERLAN CHALLENGE 2023 es promover y fomentar la innovación, el talento y el desarrollo de nuevas ideas que aporten valor a la sociedad, con especial énfasis en la búsqueda de soluciones que puedan impactar en la sociedad, en la creación de puestos de trabajo, en la reducción del coste de la energía o en la mejora de procesos industriales.</p>
      <p>Durante el desarrollo del concurso se pretende crear un ecosistema de creatividad e inspiración entre estudiantes, profesores y personas trabajadoras de Ikerlan S.Coop., donde compartir conocimientos y experiencias.</p>
      <div class="hero-actions">
        <a class="btn btn--green" href="assets/docs/challenge-2023-bases.pdf" target="_blank">Bases del concurso {ICON["download"]}</a>
        <a class="btn btn--ghost" href="assets/docs/challenge-2023-retos.pdf" target="_blank">Descripción completa de los retos {ICON["download"]}</a>
      </div>
    </div>
    <div class="prizes reveal">
      <div class="prize"><h3>Alumnos de Máster</h3><ol><li>1.<sup>er</sup> premio <b>600 €</b></li><li>2.º premio <b>300 €</b></li><li>3.<sup>er</sup> premio <b>150 €</b></li></ol></div>
      <div class="prize"><h3>Alumnos de Grado</h3><ol><li>1.<sup>er</sup> premio <b>600 €</b></li><li>2.º premio <b>300 €</b></li><li>3.<sup>er</sup> premio <b>150 €</b></li></ol></div>
      <p class="muted" style="grid-column:1/-1;margin:0;font-size:.9rem">Se establecen 2 categorías con 3 premios en cada categoría.</p>
    </div>
  </div>
</section>
<section class="section section--soft">
  <div class="container">
    <div class="section-head"><div><span class="eyebrow">¿Cómo participar?</span><h2>Individualmente o en equipos de hasta 3 personas</h2></div></div>
    <div class="steps">
      <div class="step reveal">{big("team")}<div class="k">Equipo</div><span class="d">1 – 3 personas</span><p>Participa de forma individual o en equipos de hasta 3 personas.</p></div>
      <div class="step reveal">{big("target")}<div class="k">Reto</div><span class="d">1 ó 2 subretos</span><p>Escoge un reto y desarrolla un proyecto para dar solución a 1 ó 2 de los subretos planteados.</p></div>
      <div class="step reveal">{big("flag")}<div class="k">Fase 1</div><span class="d">Hasta el 15 oct 2023</span><p>Prepara una presentación del proyecto (PDF con páginas horizontales) y envíala al concurso.</p></div>
      <div class="step reveal">{big("trophy")}<div class="k">Final</div><span class="d">19 oct 2023</span><p>3 equipos finalistas de cada categoría (Grado y Máster) presentarán sus proyectos en Ikerlan (Mondragón). La Cátedra corre con los gastos del viaje.</p></div>
    </div>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="section-head"><div><span class="eyebrow">Retos</span><h2>Retos del concurso</h2></div><a class="link-arrow" href="assets/docs/challenge-2023-retos.pdf" target="_blank">Descripción completa (PDF)</a></div>
    {t}
  </div>
</section>
'''
    page('challenge-2023.html', 'Ikerlan Challenge 2023 | Cátedra Ikerlan', 'Concurso de ideas Ikerlan Challenge 2023: retos, fases, premios y bases.', body)


def build_noticias():
    years = sorted({n['date'][:4] for n in NEWS}, reverse=True)
    f = '<button type="button" data-year="all" aria-pressed="true">Todas</button>' + ''.join(f'<button type="button" data-year="{y}" aria-pressed="false">{y}</button>' for y in years)
    cards = news_card(NEWS[0], featured=True) + ''.join(news_card(n) for n in NEWS[1:])
    body = f'''
{hero('Noticias', 'Actualidad de la Cátedra Ikerlan: premios, jornadas, convocatorias y defensas de tesis.', 'sede-inauguracion-2025', 'Noticias')}
<section class="section" data-filter>
  <div class="container">
    <div class="filters" role="group" aria-label="Filtrar por año">{f}</div>
    <div class="news-grid">{cards}</div>
  </div>
</section>
'''
    page('noticias.html', 'Noticias | Cátedra Ikerlan', 'Noticias de la Cátedra Ikerlan-Uniovi.', body)

    for k, n in enumerate(NEWS):
        others = [x for x in NEWS if x is not n][:4]
        rel = ''.join(f'<li><a href="{x["slug"]}.html"><img src="../assets/img/{x["img"]}.jpg" alt="" loading="lazy"><span>{x["title"]}<small>{fdate(x["date"])}</small></span></a></li>' for x in others)
        prev_ = NEWS[k + 1] if k + 1 < len(NEWS) else None
        next_ = NEWS[k - 1] if k > 0 else None
        nav = '<div style="display:flex;justify-content:space-between;gap:12px;flex-wrap:wrap;margin-top:32px;padding-top:24px;border-top:1px solid var(--line)">'
        nav += f'<a class="btn btn--ghost btn--sm" href="{prev_["slug"]}.html">← Anterior</a>' if prev_ else '<span></span>'
        nav += f'<a class="btn btn--ghost btn--sm" href="{next_["slug"]}.html">Siguiente →</a>' if next_ else '<span></span>'
        nav += '</div>'
        body = f'''
{hero(n['title'], '', n['img'], f'<a href="../noticias.html">Noticias</a>', r='../').replace('<h1>', '<h1 style="font-size:clamp(1.7rem,3.4vw,2.6rem);max-width:900px">')}
<section class="section">
  <div class="container article">
    <article class="article-body">
      <div class="article-meta"><span class="badge badge--dark">{n['tag']}</span><time datetime="{n['date']}">{fdate(n['date'])}</time></div>
      {n['body']}
      {nav}
    </article>
    <aside class="article-aside">
      <div class="aside-box"><h3>Otras noticias</h3><ul>{rel}</ul></div>
      <a class="btn btn--dark" href="../noticias.html">Todas las noticias {ICON["arrow"]}</a>
    </aside>
  </div>
</section>
'''
        desc = n['summary'].replace('"', '&quot;').replace('«', '').replace('»', '')
        page(f'noticias/{n["slug"]}.html', f'{n["title"]} | Cátedra Ikerlan', desc, body, cur='noticias.html')


def build_contacto():
    body = f'''
{hero('Contacto', 'Contacta con la Cátedra Ikerlan-Uniovi.', 'slide-07', 'Contacto')}
<section class="section">
  <div class="container contact-grid">
    <div>
      <div class="contact-card">
        <h2>Cátedra Ikerlan-Uniovi</h2>
        <div class="contact-item">{ICON["pin"]}<div><small>Sede</small>Edificio Departamental 7, primera planta<br>Escuela Politécnica de Ingeniería de Gijón<br>Campus de Gijón · 33204, Gijón</div></div>
        <div class="contact-item">{ICON["user"]}<div><small>Directora de la Cátedra</small>María Jesús Lamela<br><a href="mailto:mjesuslr@uniovi.es">mjesuslr@uniovi.es</a></div></div>
        <div class="contact-item">{ICON["mail"]}<div><small>Prácticas, becas y TFG/TFM</small>Miguel Muñiz Calvente<br><a href="mailto:munizcmiguel@uniovi.es">munizcmiguel@uniovi.es</a></div></div>
      </div>
      <div class="map"><iframe title="Mapa: Escuela Politécnica de Ingeniería de Gijón" loading="lazy" src="https://www.openstreetmap.org/export/embed.html?bbox=-5.6330%2C43.5195%2C-5.6150%2C43.5275&amp;layer=mapnik&amp;marker=43.5236%2C-5.6244"></iframe></div>
    </div>
    <form class="form" id="contact-form" novalidate>
      <div class="full"><h2 style="margin:0">Escríbenos</h2><p class="muted" style="margin:.3em 0 0">Al enviar se abrirá tu programa de correo con el mensaje ya preparado.</p></div>
      <label>Nombre<input name="nombre" required autocomplete="given-name"></label>
      <label>Apellido<input name="apellido" autocomplete="family-name"></label>
      <label>Email<input type="email" name="email" required autocomplete="email"></label>
      <label>Teléfono<input type="tel" name="telefono" autocomplete="tel"></label>
      <label class="full">Dirección<input name="direccion" autocomplete="street-address"></label>
      <label>Asunto<select name="asunto"><option>Consulta general</option><option>Prácticas y becas</option><option>TFG / TFM</option><option>Convocatoria de proyectos</option><option>Otro</option></select></label>
      <label>Destinatario<select name="destino"><option value="munizcmiguel@uniovi.es">Miguel Muñiz Calvente</option><option value="mjesuslr@uniovi.es">María Jesús Lamela</option></select></label>
      <label class="full">Mensaje<textarea name="mensaje" required placeholder="Escribe tu mensaje aquí…"></textarea></label>
      <div class="full"><button class="btn btn--green" type="submit">Enviar {ICON["arrow"]}</button></div>
      <p class="form-msg" role="status">¡Gracias por tu mensaje! Si no se ha abierto tu programa de correo, escríbenos directamente a <a href="mailto:munizcmiguel@uniovi.es">munizcmiguel@uniovi.es</a>.</p>
    </form>
  </div>
</section>
'''
    page('contacto.html', 'Contacto | Cátedra Ikerlan', 'Contacta con la Cátedra Ikerlan-Uniovi en la Escuela Politécnica de Ingeniería de Gijón.', body)


# URLs de la antigua web de Wix -> páginas nuevas (para no romper enlaces ni Google)
OLD_URLS = {
    'blog': 'noticias.html',
    'equipo-1': 'equipo.html',
    'copia-de-prácticas': 'tfg-tfm.html',
    'challenge2023': 'challenge-2023.html',
    'prácticas': 'practicas.html',
    'proyectos': 'investigacion.html',
    'experiencias': 'estudiantes.html',
    'premios': 'convocatoria.html',
    'post/escribe-en-tu-blog-desde-tu-sitio-web-o-móvil': 'noticias.html',
    'post/convocatoria-premios-cátedra-ikerlan-2021-2022': 'noticias/convocatoria-premios-catedra-ikerlan-2021-2022.html',
    'post/renovamos-por-4-años-la-cátedra-ikerlan': 'noticias/renovamos-por-4-anos-la-catedra-ikerlan.html',
    'post/jornada-catedra-ikerlan-2023': 'noticias/jornada-catedra-ikerlan-2023.html',
    'post/22-diciembre-defensa-de-tesis': 'noticias/defensa-tesis-mikel-escalero.html',
    'post/alejandro-fernández-y-mario-martín-premiados-por-la-cátedra-ikerlan': 'noticias/premios-alejandro-fernandez-mario-martin.html',
    'post/fruela-de-la-roza-y-pelayo-fernández-ganadores-de-los-premios-cátedra-ikerlan-2020': 'noticias/premios-2020-fruela-de-la-roza-pelayo-fernandez.html',
    'post/mario-martín-y-malena-potesta-reciben-los-premios-de-la-cátedra-ikerlan': 'noticias/premios-mario-martin-malena-potesta.html',
    'post/la-cátedra-ikerlan-de-investigación-y-desarrollo-inaugura-su-sede-en-el-campus-de-gijón-de-la-univer': 'noticias/inauguracion-sede-campus-gijon.html',
    'post/i-concurso-ideas-cátedra-ikerlan': 'noticias/i-concurso-ideas-catedra-ikerlan.html',
}


def build_redirects():
    for old, new in OLD_URLS.items():
        target = '../' * (old.count('/') + 1) + new
        html = f'''<!doctype html>
<html lang="es"><head><meta charset="utf-8">
<title>Cátedra Ikerlan</title>
<meta name="robots" content="noindex">
<meta http-equiv="refresh" content="0; url={target}">
<link rel="canonical" href="{target}">
</head><body><p>Esta página se ha movido: <a href="{target}">continuar</a>.</p></body></html>
'''
        full = os.path.join(ROOT, old, 'index.html')
        os.makedirs(os.path.dirname(full), exist_ok=True)
        with open(full, 'w', encoding='utf-8', newline='\n') as f:
            f.write(html)
    print('   %d redirecciones de URLs antiguas' % len(OLD_URLS))


def build_404():
    body = f'''{hero('Página no encontrada', 'La página que buscas no existe o ha cambiado de dirección.', crumb='404')}
<section class="section"><div class="container">
  <p><a class="btn btn--green" href="index.html">Volver al inicio {ICON["arrow"]}</a> <a class="btn" href="noticias.html">Ver noticias</a></p>
</div></section>
'''
    page('404.html', 'Página no encontrada | Cátedra Ikerlan', 'Página no encontrada.', body)
    # GitHub Pages sirve 404.html en cualquier ruta: fija la base para que funcionen los enlaces relativos
    full = os.path.join(ROOT, '404.html')
    with open(full, encoding='utf-8') as f:
        html = f.read()
    base = "<script>document.write('<base href=\"'+(location.pathname.indexOf('/catedra-ikerlan/')===0?'/catedra-ikerlan/':'/')+'\">')</script>"
    html = html.replace('<meta charset="utf-8">', '<meta charset="utf-8">\n' + base, 1)
    with open(full, 'w', encoding='utf-8', newline='\n') as f:
        f.write(html)


def favicon():
    svg = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="#161616"/><rect x="14" y="12" width="9" height="9" rx="2" fill="#19ff20"/><rect x="14" y="26" width="9" height="26" rx="2" fill="#fff"/><path d="M30 12h9v22l11-12h11L48 36l13 16H50l-11-14v14h-9z" fill="#fff"/></svg>'
    with open(os.path.join(ROOT, 'assets/img/favicon.svg'), 'w', encoding='utf-8') as f:
        f.write(svg)


if __name__ == '__main__':
    print('Generando páginas en', ROOT)
    favicon()
    build_index(); build_equipo(); build_convocatoria(); build_estudiantes(); build_tfg()
    build_practicas(); build_investigacion(); build_challenge(); build_noticias(); build_contacto()
    build_404(); build_redirects()
    print('Listo.')
