/* Cátedra Ikerlan — interacciones (sin dependencias) */
(function () {
  'use strict';
  const $ = (s, c = document) => c.querySelector(s);
  const $$ = (s, c = document) => Array.from(c.querySelectorAll(s));
  const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* Menú móvil y submenús */
  const toggle = $('.menu-toggle');
  const nav = $('.nav');
  if (toggle && nav) {
    toggle.addEventListener('click', () => {
      const open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open);
      document.body.classList.toggle('nav-open', open);
    });
  }
  $$('.has-sub > .nav-btn').forEach(btn => {
    btn.addEventListener('click', e => {
      e.preventDefault();
      const li = btn.parentElement;
      const open = li.classList.toggle('open');
      btn.setAttribute('aria-expanded', open);
    });
  });
  document.addEventListener('click', e => {
    $$('.has-sub.open').forEach(li => { if (!li.contains(e.target)) { li.classList.remove('open'); $('.nav-btn', li).setAttribute('aria-expanded', 'false'); } });
  });
  document.addEventListener('keydown', e => {
    if (e.key === 'Escape') $$('.has-sub.open').forEach(li => li.classList.remove('open'));
  });

  /* Carrusel de portada */
  const hero = $('.hero');
  if (hero) {
    const slides = $$('.slide', hero);
    const dots = $('.dots', hero);
    const counter = $('.hero-counter', hero);
    let i = 0, timer;
    slides.forEach((_, k) => {
      const b = document.createElement('button');
      b.type = 'button';
      b.setAttribute('aria-label', 'Imagen ' + (k + 1));
      b.addEventListener('click', () => { go(k); restart(); });
      dots.appendChild(b);
    });
    const go = n => {
      i = (n + slides.length) % slides.length;
      slides.forEach((s, k) => s.classList.toggle('is-active', k === i));
      $$('button', dots).forEach((d, k) => d.classList.toggle('is-active', k === i));
      counter.textContent = (i + 1) + ' / ' + slides.length;
      // precarga la siguiente
      const nx = slides[(i + 1) % slides.length].querySelector('img');
      if (nx && nx.loading === 'lazy') nx.loading = 'eager';
    };
    const restart = () => { clearInterval(timer); if (!reduced) timer = setInterval(() => go(i + 1), 5500); };
    $('.prev', hero).addEventListener('click', () => { go(i - 1); restart(); });
    $('.next', hero).addEventListener('click', () => { go(i + 1); restart(); });
    hero.addEventListener('mouseenter', () => clearInterval(timer));
    hero.addEventListener('mouseleave', restart);
    go(0); restart();
  }

  /* Pestañas (horizontales y verticales) */
  $$('[data-tabs]').forEach(root => {
    const tabs = $$(':scope > .tablist [role="tab"], :scope > .tablist-wrap > .tablist [role="tab"]', root);
    const select = t => {
      tabs.forEach(x => {
        const on = x === t;
        x.setAttribute('aria-selected', on);
        x.tabIndex = on ? 0 : -1;
        document.getElementById(x.getAttribute('aria-controls')).hidden = !on;
      });
    };
    tabs.forEach((t, k) => {
      t.addEventListener('click', () => {
        select(t);
        if (root.hasAttribute('data-hash')) history.replaceState(null, '', '#' + t.id.replace(/^tab-/, ''));
        if (window.innerWidth < 960 && root.classList.contains('vtabs')) {
          document.getElementById(t.getAttribute('aria-controls')).scrollIntoView({ behavior: reduced ? 'auto' : 'smooth', block: 'start' });
        }
      });
      t.addEventListener('keydown', e => {
        const dir = { ArrowRight: 1, ArrowDown: 1, ArrowLeft: -1, ArrowUp: -1 }[e.key];
        if (!dir) return;
        e.preventDefault();
        const n = tabs[(k + dir + tabs.length) % tabs.length];
        n.focus(); select(n);
      });
    });
    const fromHash = location.hash && tabs.find(t => t.id === 'tab-' + location.hash.slice(1));
    select(fromHash || tabs.find(t => t.getAttribute('aria-selected') === 'true') || tabs[0]);
  });

  /* Paginación de tarjetas (evita listas interminables) */
  $$('[data-pager]').forEach(root => {
    const per = parseInt(root.dataset.pager, 10) || 6;
    const items = $$('[data-item]', root);
    const grid = $('.pager-grid', root);
    const bar = $('.pager', root);
    const pages = Math.ceil(items.length / per);
    let cur = 0;
    const show = p => {
      cur = p;
      items.forEach((it, k) => { it.hidden = Math.floor(k / per) !== p; });
      $$('button', bar).forEach(b => {
        if (b.dataset.p !== undefined) b.setAttribute('aria-current', +b.dataset.p === p);
      });
      bar.querySelector('.pg-prev').disabled = p === 0;
      bar.querySelector('.pg-next').disabled = p === pages - 1;
    };
    if (pages <= 1) { bar.remove(); return; }
    const mk = (txt, cls, fn, label) => {
      const b = document.createElement('button');
      b.type = 'button'; b.innerHTML = txt; if (cls) b.className = cls;
      if (label) b.setAttribute('aria-label', label);
      b.addEventListener('click', () => { fn(); grid.scrollIntoView({ behavior: reduced ? 'auto' : 'smooth', block: 'nearest' }); });
      bar.appendChild(b); return b;
    };
    mk('&larr;', 'pg-prev', () => show(Math.max(0, cur - 1)), 'Página anterior');
    for (let p = 0; p < pages; p++) { const b = mk(String(p + 1), '', () => show(p), 'Página ' + (p + 1)); b.dataset.p = p; }
    mk('&rarr;', 'pg-next', () => show(Math.min(pages - 1, cur + 1)), 'Página siguiente');
    show(0);
  });

  /* Filtro de noticias por año */
  $$('[data-filter]').forEach(root => {
    const btns = $$('.filters button', root);
    const cards = $$('[data-year]', root);
    btns.forEach(b => b.addEventListener('click', () => {
      btns.forEach(x => x.setAttribute('aria-pressed', x === b));
      const y = b.dataset.year;
      cards.forEach(c => { c.hidden = y !== 'all' && c.dataset.year !== y; });
    }));
  });

  /* Visor de imágenes */
  const lb = document.createElement('div');
  lb.className = 'lightbox';
  lb.setAttribute('role', 'dialog');
  lb.setAttribute('aria-modal', 'true');
  lb.setAttribute('aria-label', 'Visor de imágenes');
  lb.innerHTML = '<button class="lb-close" aria-label="Cerrar">&times;</button><button class="lb-prev" aria-label="Anterior">&#8249;</button><img alt=""><button class="lb-next" aria-label="Siguiente">&#8250;</button><div class="lb-count"></div>';
  document.body.appendChild(lb);
  let group = [], gi = 0, lastFocus = null;
  const lbImg = $('img', lb);
  const lbShow = n => {
    gi = (n + group.length) % group.length;
    const b = group[gi];
    lbImg.src = b.dataset.full || $('img', b).src;
    lbImg.alt = $('img', b).alt;
    $('.lb-count', lb).textContent = (gi + 1) + ' / ' + group.length;
    $('.lb-prev', lb).style.display = $('.lb-next', lb).style.display = group.length > 1 ? '' : 'none';
  };
  const lbClose = () => { lb.classList.remove('open'); document.body.style.overflow = ''; if (lastFocus) lastFocus.focus(); };
  $$('[data-lightbox]').forEach(b => b.addEventListener('click', () => {
    group = $$('[data-lightbox="' + b.dataset.lightbox + '"]');
    lastFocus = b;
    lbShow(group.indexOf(b));
    lb.classList.add('open');
    document.body.style.overflow = 'hidden';
    $('.lb-close', lb).focus();
  }));
  $('.lb-close', lb).addEventListener('click', lbClose);
  $('.lb-prev', lb).addEventListener('click', () => lbShow(gi - 1));
  $('.lb-next', lb).addEventListener('click', () => lbShow(gi + 1));
  lb.addEventListener('click', e => { if (e.target === lb) lbClose(); });
  document.addEventListener('keydown', e => {
    if (!lb.classList.contains('open')) return;
    if (e.key === 'Escape') lbClose();
    if (e.key === 'ArrowLeft') lbShow(gi - 1);
    if (e.key === 'ArrowRight') lbShow(gi + 1);
  });

  /* Vídeos de YouTube: se cargan sólo al pulsar */
  $$('[data-videos]').forEach(root => {
    const main = $('.video-main', root);
    const items = $$('.video-list button', root);
    const setVideo = (b, play) => {
      items.forEach(x => x.setAttribute('aria-pressed', x === b));
      const id = b.dataset.id, title = b.dataset.title;
      if (play) {
        main.innerHTML = '<iframe src="https://www.youtube-nocookie.com/embed/' + id + '?autoplay=1&rel=0" title="' + title + '" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>';
      } else {
        main.innerHTML = '<img src="' + b.dataset.thumb + '" alt=""><button class="play" type="button" aria-label="Reproducir: ' + title + '"><span><svg viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg></span></button><div class="caption">' + title + '</div>';
        $('.play', main).addEventListener('click', () => setVideo(b, true));
      }
    };
    items.forEach(b => b.addEventListener('click', () => setVideo(b, false)));
    setVideo(items[0], false);
  });

  /* Formulario de contacto: abre el cliente de correo con el mensaje */
  const form = $('#contact-form');
  if (form) {
    form.addEventListener('submit', e => {
      e.preventDefault();
      if (!form.reportValidity()) return;
      const d = new FormData(form);
      const to = d.get('destino');
      const subject = '[Web Cátedra Ikerlan] ' + (d.get('asunto') || 'Consulta');
      const body = [
        'Nombre: ' + d.get('nombre') + ' ' + d.get('apellido'),
        'Email: ' + d.get('email'),
        d.get('telefono') ? 'Teléfono: ' + d.get('telefono') : '',
        d.get('direccion') ? 'Dirección: ' + d.get('direccion') : '',
        '',
        d.get('mensaje')
      ].filter((l, k) => l !== '' || k === 4).join('\n');
      window.location.href = 'mailto:' + to + '?subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(body);
      $('.form-msg', form).classList.add('show');
    });
  }

  /* Botón volver arriba */
  const top = $('.to-top');
  if (top) {
    const onScroll = () => top.classList.toggle('show', window.scrollY > 600);
    window.addEventListener('scroll', onScroll, { passive: true });
    top.addEventListener('click', () => window.scrollTo({ top: 0, behavior: reduced ? 'auto' : 'smooth' }));
    onScroll();
  }

  /* Aparición suave */
  if ('IntersectionObserver' in window && !reduced) {
    const io = new IntersectionObserver(es => es.forEach(en => { if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); } }), { rootMargin: '0px 0px -40px 0px' });
    $$('.reveal').forEach(el => io.observe(el));
  } else {
    $$('.reveal').forEach(el => el.classList.add('in'));
  }

  const y = $('#year');
  if (y) y.textContent = new Date().getFullYear();
})();
