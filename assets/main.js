/* UMCO v2 — shared behaviour */
(function () {
  'use strict';

  // Nav scroll state
  var nav = document.querySelector('.nav');
  if (nav) {
    var onScroll = function () { nav.classList.toggle('scrolled', window.scrollY > 12); };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  // Mobile menu
  var burger = document.querySelector('.nav-burger');
  var mobileMenu = document.querySelector('.mobile-menu');
  if (burger && mobileMenu) {
    burger.addEventListener('click', function () {
      var open = mobileMenu.classList.toggle('open');
      burger.classList.toggle('open', open);
      burger.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    mobileMenu.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () {
        mobileMenu.classList.remove('open');
        burger.classList.remove('open');
      });
    });
  }

  // Scroll reveal
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
    });
  }, { threshold: 0.12, rootMargin: '0px 0px -4% 0px' });
  document.querySelectorAll('.reveal, .reveal-stagger').forEach(function (el) { io.observe(el); });

  // Animated counters — reads target from data-count ("500+", "98%", "15")
  function countUp(el) {
    var raw = el.getAttribute('data-count');
    var num = parseInt(raw, 10);
    var suffix = raw.replace(/[0-9]/g, '');
    var dur = 1700, start = null;
    function tick(ts) {
      if (!start) start = ts;
      var p = Math.min((ts - start) / dur, 1);
      var ease = 1 - Math.pow(1 - p, 3);
      el.textContent = Math.round(num * ease) + suffix;
      if (p < 1) requestAnimationFrame(tick);
      else el.textContent = raw;
    }
    requestAnimationFrame(tick);
  }
  var counterIO = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (e.isIntersecting) {
        e.target.querySelectorAll('[data-count]').forEach(countUp);
        counterIO.unobserve(e.target);
      }
    });
  }, { threshold: 0.4 });
  document.querySelectorAll('.count-group').forEach(function (g) { counterIO.observe(g); });

  // Consultation form
  window.umcoSubmit = function (ev) {
    ev.preventDefault();
    var btn = ev.target.querySelector('.form-submit');
    if (!btn) return;
    btn.disabled = true;
    btn.textContent = 'Request received — we’ll respond within one business day.';
  };

  // Smooth anchors with nav offset
  document.querySelectorAll('a[href^="#"]').forEach(function (a) {
    a.addEventListener('click', function (ev) {
      var id = a.getAttribute('href');
      if (id.length < 2) return;
      var target = document.querySelector(id);
      if (target) {
        ev.preventDefault();
        window.scrollTo({ top: target.getBoundingClientRect().top + window.scrollY - 86, behavior: 'smooth' });
      }
    });
  });
})();

/* ── v2.1: hero slider, carousels, parallax ── */
(function () {
  'use strict';
  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // Hero slider
  var hs = document.querySelector('.hs');
  if (hs) {
    var slides = hs.querySelectorAll('.hs-slide');
    var dots = hs.querySelectorAll('.hs-dot');
    var DUR = 7000, cur = 0, timer = null;
    hs.style.setProperty('--hs-dur', DUR + 'ms');

    function show(i) {
      cur = (i + slides.length) % slides.length;
      slides.forEach(function (s, k) { s.classList.toggle('active', k === cur); });
      dots.forEach(function (d, k) {
        d.classList.remove('active');
        if (k === cur) { void d.offsetWidth; d.classList.add('active'); }
      });
    }
    function play() { stop(); if (!reduced) timer = setInterval(function () { show(cur + 1); }, DUR); }
    function stop() { if (timer) clearInterval(timer); timer = null; }

    dots.forEach(function (d, k) { d.addEventListener('click', function () { show(k); play(); }); });
    hs.querySelectorAll('[data-hs]').forEach(function (btn) {
      btn.addEventListener('click', function () { show(cur + parseInt(btn.dataset.hs, 10)); play(); });
    });
    hs.addEventListener('mouseenter', stop);
    hs.addEventListener('mouseleave', play);

    // touch swipe
    var sx = 0;
    hs.addEventListener('touchstart', function (e) { sx = e.touches[0].clientX; }, { passive: true });
    hs.addEventListener('touchend', function (e) {
      var dx = sx - e.changedTouches[0].clientX;
      if (Math.abs(dx) > 48) { show(cur + (dx > 0 ? 1 : -1)); play(); }
    }, { passive: true });

    // mouse parallax on active background
    if (!reduced && window.matchMedia('(pointer:fine)').matches) {
      hs.addEventListener('mousemove', function (e) {
        var r = hs.getBoundingClientRect();
        var x = (e.clientX - r.left) / r.width - 0.5;
        var y = (e.clientY - r.top) / r.height - 0.5;
        var bg = slides[cur].querySelector('.hs-bg');
        if (bg) bg.style.translate = (x * -16) + 'px ' + (y * -10) + 'px';
      });
    }
    play();
  }

  // Generic snap carousels
  document.querySelectorAll('[data-carousel]').forEach(function (car) {
    var track = car.querySelector('.car-track');
    var bar = car.querySelector('.car-progress i');
    var card = track.firstElementChild;
    var step = card ? card.offsetWidth + 20 : 320;

    car.querySelectorAll('.car-arrow').forEach(function (btn) {
      btn.addEventListener('click', function () {
        track.scrollBy({ left: step * parseInt(btn.dataset.dir, 10), behavior: 'smooth' });
      });
    });
    function progress() {
      var max = track.scrollWidth - track.clientWidth;
      if (bar) bar.style.width = (max > 0 ? (track.scrollLeft / max) * 100 : 100) + '%';
    }
    track.addEventListener('scroll', progress, { passive: true });
    window.addEventListener('resize', progress);
    progress();
  });

  // Subtle scroll parallax on page-hero glow
  var ph = document.querySelector('.page-hero');
  if (ph && !reduced) {
    window.addEventListener('scroll', function () {
      var y = Math.min(window.scrollY, 600);
      ph.style.backgroundPosition = '0 ' + y * 0.18 + 'px';
    }, { passive: true });
  }
})();

/* ── Calendly popup on Book Consultation buttons ── */
(function () {
  'use strict';
  var URL = 'https://calendly.com/umco-consult/30min';
  document.querySelectorAll('[data-calendly]').forEach(function (el) {
    el.addEventListener('click', function (ev) {
      if (window.Calendly && typeof Calendly.initPopupWidget === 'function') {
        ev.preventDefault();
        Calendly.initPopupWidget({ url: URL + '?hide_gdpr_banner=1&primary_color=c6a35d' });
      }
      // else: fall through to the href (contact.html) as a no-JS fallback
    });
  });
})();
