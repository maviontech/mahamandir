/* Swarved Mahamandir Dham — main.js
 * Serene entry veil, scroll reveals, nav, lightbox, to-top.
 */

(function () {
  'use strict';

  // ------------------------------------------------------------
  // Entry veil — show only on the very first page load of a session.
  // sessionStorage key persists across page navigations within a tab
  // but clears when the tab/browser is closed, so the veil greets the
  // user once per visit, not on every click.
  // ------------------------------------------------------------
  const veil = document.getElementById('entryVeil');
  if (veil) {
    const SEEN_KEY = 'smm_veil_seen';
    let alreadySeen = false;
    try { alreadySeen = sessionStorage.getItem(SEEN_KEY) === '1'; } catch (_) {}

    if (alreadySeen) {
      // Subsequent page — hide immediately, no animation, no delay
      veil.style.transition = 'none';
      veil.classList.add('is-hidden');
    } else {
      // First visit — play the contemplative entry and mark as seen
      try { sessionStorage.setItem(SEEN_KEY, '1'); } catch (_) {}
      window.addEventListener('load', () => {
        setTimeout(() => veil.classList.add('is-hidden'), 2200);
      });
      // Allow click / Esc to dismiss instantly
      const dismiss = () => veil.classList.add('is-hidden');
      veil.addEventListener('click', dismiss);
      document.addEventListener('keydown', (e) => { if (e.key === 'Escape') dismiss(); });
    }
  }

  // ------------------------------------------------------------
  // Header scroll state
  // ------------------------------------------------------------
  const header = document.getElementById('siteHeader');
  if (header) {
    const onScroll = () => {
      if (window.scrollY > 8) header.classList.add('is-scrolled');
      else header.classList.remove('is-scrolled');
    };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  // ------------------------------------------------------------
  // Mobile nav toggle
  // ------------------------------------------------------------
  const navToggle = document.getElementById('navToggle');
  const navList = document.getElementById('navList');
  if (navToggle && navList) {
    navToggle.addEventListener('click', () => {
      const open = navList.classList.toggle('is-open');
      navToggle.setAttribute('aria-expanded', open);
      document.body.classList.toggle('no-scroll', open);
    });
    navList.querySelectorAll('a').forEach((a) => {
      a.addEventListener('click', () => {
        navList.classList.remove('is-open');
        navToggle.setAttribute('aria-expanded', 'false');
        document.body.classList.remove('no-scroll');
      });
    });
  }

  // ------------------------------------------------------------
  // Scroll reveal
  // ------------------------------------------------------------
  const reveals = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    const obs = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          obs.unobserve(entry.target);
        }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
    reveals.forEach((el) => obs.observe(el));
  } else {
    reveals.forEach((el) => el.classList.add('is-visible'));
  }

  // ------------------------------------------------------------
  // Back to top
  // ------------------------------------------------------------
  const toTop = document.getElementById('toTop');
  if (toTop) {
    const onScroll2 = () => {
      if (window.scrollY > 600) toTop.classList.add('is-visible');
      else toTop.classList.remove('is-visible');
    };
    window.addEventListener('scroll', onScroll2, { passive: true });
    toTop.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));
  }

  // ------------------------------------------------------------
  // Lightbox
  // ------------------------------------------------------------
  const lightbox = document.getElementById('lightbox');
  if (lightbox) {
    const imgEl = document.getElementById('lightboxImg');
    const capEl = document.getElementById('lightboxCaption');
    const closeEl = document.getElementById('lightboxClose');
    const prevEl = document.getElementById('lightboxPrev');
    const nextEl = document.getElementById('lightboxNext');

    const triggers = Array.from(document.querySelectorAll('[data-lightbox]'));
    let current = 0;

    const open = (idx) => {
      if (idx < 0 || idx >= triggers.length) return;
      current = idx;
      const t = triggers[idx];
      const src = t.getAttribute('href') || t.querySelector('img')?.src;
      const cap = t.getAttribute('data-caption') || '';
      if (imgEl) { imgEl.src = src; imgEl.alt = cap; }
      if (capEl) capEl.textContent = cap;
      lightbox.classList.add('is-open');
      lightbox.setAttribute('aria-hidden', 'false');
      document.body.classList.add('no-scroll');
    };
    const close = () => {
      lightbox.classList.remove('is-open');
      lightbox.setAttribute('aria-hidden', 'true');
      document.body.classList.remove('no-scroll');
    };
    const step = (dir) => {
      let idx = current + dir;
      if (idx < 0) idx = triggers.length - 1;
      if (idx >= triggers.length) idx = 0;
      open(idx);
    };

    triggers.forEach((t, i) => {
      t.addEventListener('click', (e) => { e.preventDefault(); open(i); });
    });
    if (closeEl) closeEl.addEventListener('click', close);
    if (prevEl) prevEl.addEventListener('click', () => step(-1));
    if (nextEl) nextEl.addEventListener('click', () => step(1));
    lightbox.addEventListener('click', (e) => { if (e.target === lightbox) close(); });
    document.addEventListener('keydown', (e) => {
      if (!lightbox.classList.contains('is-open')) return;
      if (e.key === 'Escape') close();
      if (e.key === 'ArrowLeft') step(-1);
      if (e.key === 'ArrowRight') step(1);
    });
  }

  // ------------------------------------------------------------
  // Shared: reduced-motion preference
  // ------------------------------------------------------------
  const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // ------------------------------------------------------------
  // Hero carousel — prev/next arrows, dot indicators,
  // keyboard arrows, touch swipe, auto-advance with pause on hover.
  // ------------------------------------------------------------
  const heroCarousel = document.querySelector('.hero--carousel');
  if (heroCarousel) {
    const slides = Array.from(heroCarousel.querySelectorAll('.hero__slide'));
    const dots   = Array.from(heroCarousel.querySelectorAll('.hero-dot'));
    const prev   = heroCarousel.querySelector('#heroPrev');
    const next   = heroCarousel.querySelector('#heroNext');
    let idx = 0;
    let timer = null;
    const AUTOPLAY_MS = 7000;

    const show = (n) => {
      const len = slides.length;
      const target = ((n % len) + len) % len;
      slides.forEach((s, i) => s.classList.toggle('is-active', i === target));
      dots.forEach((d, i) => {
        d.classList.toggle('is-active', i === target);
        d.setAttribute('aria-selected', i === target);
      });
      idx = target;
    };

    const goNext = () => show(idx + 1);
    const goPrev = () => show(idx - 1);

    if (next) next.addEventListener('click', () => { goNext(); restart(); });
    if (prev) prev.addEventListener('click', () => { goPrev(); restart(); });
    dots.forEach((d) => d.addEventListener('click', () => {
      show(Number(d.dataset.goto));
      restart();
    }));

    // Keyboard — only when hero is in viewport
    document.addEventListener('keydown', (e) => {
      const rect = heroCarousel.getBoundingClientRect();
      const inView = rect.bottom > 100 && rect.top < window.innerHeight - 100;
      if (!inView) return;
      if (e.key === 'ArrowLeft')  { goPrev(); restart(); }
      if (e.key === 'ArrowRight') { goNext(); restart(); }
    });

    // Touch swipe
    let touchX = null;
    heroCarousel.addEventListener('touchstart', (e) => {
      touchX = e.changedTouches[0].clientX;
    }, { passive: true });
    heroCarousel.addEventListener('touchend', (e) => {
      if (touchX == null) return;
      const dx = e.changedTouches[0].clientX - touchX;
      if (Math.abs(dx) > 50) { dx < 0 ? goNext() : goPrev(); restart(); }
      touchX = null;
    }, { passive: true });

    // Autoplay
    const start = () => { timer = setInterval(goNext, AUTOPLAY_MS); };
    const stop  = () => { if (timer) { clearInterval(timer); timer = null; } };
    const restart = () => { stop(); start(); };
    if (!prefersReduced) start();

    // Pause on hover / focus
    heroCarousel.addEventListener('mouseenter', stop);
    heroCarousel.addEventListener('mouseleave', start);
    heroCarousel.addEventListener('focusin',    stop);
    heroCarousel.addEventListener('focusout',   start);

    // Pause when tab hidden
    document.addEventListener('visibilitychange', () => {
      document.hidden ? stop() : start();
    });
  }

  // ------------------------------------------------------------
  // Subtle parallax on hero (only desktop, reduced-motion respects)
  // ------------------------------------------------------------
  const hero = document.getElementById('hero');
  // Parallax only applies to legacy single-image hero (not carousel)
  if (hero && !hero.classList.contains('hero--carousel') && !prefersReduced && window.matchMedia('(min-width: 900px)').matches) {
    window.addEventListener('scroll', () => {
      const y = window.scrollY;
      if (y < window.innerHeight) {
        hero.style.backgroundPosition = `center ${50 + y * 0.05}%`;
      }
    }, { passive: true });
  }
})();
