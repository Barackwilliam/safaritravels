document.addEventListener('DOMContentLoaded', function () {
  var toggle = document.getElementById('nav-toggle');
  var navLinks = document.querySelectorAll('.site-nav a');
  navLinks.forEach(function (link) {
    link.addEventListener('click', function () {
      if (toggle) toggle.checked = false;
    });
  });

  /* ---------------------------------------------------------------
     Scroll-reveal: fades/lifts .reveal and .reveal-stagger elements
     into view the first time they enter the viewport.
  --------------------------------------------------------------- */
  var revealTargets = document.querySelectorAll('.reveal, .reveal-stagger');
  if ('IntersectionObserver' in window && revealTargets.length) {
    var revealObserver = new IntersectionObserver(function (entries, obs) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          obs.unobserve(entry.target);
        }
      });
    }, { threshold: 0.15, rootMargin: '0px 0px -60px 0px' });
    revealTargets.forEach(function (el) { revealObserver.observe(el); });
  } else {
    revealTargets.forEach(function (el) { el.classList.add('is-visible'); });
  }

  /* ---------------------------------------------------------------
     Animated counters: hero-stat-num counts up from 0 once visible.
     Reads the target from the element's own text (keeps "+", "%", etc).
  --------------------------------------------------------------- */
  var counters = document.querySelectorAll('.hero-stat-num');
  if ('IntersectionObserver' in window && counters.length) {
    var counterObserver = new IntersectionObserver(function (entries, obs) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        var el = entry.target;
        var raw = el.textContent.trim();
        var match = raw.match(/[\d.]+/);
        if (!match) { obs.unobserve(el); return; }
        var target = parseFloat(match[0]);
        var suffix = raw.replace(match[0], '');
        var duration = 1100;
        var start = null;
        function step(ts) {
          if (!start) start = ts;
          var progress = Math.min((ts - start) / duration, 1);
          var eased = 1 - Math.pow(1 - progress, 3);
          var current = Math.round(target * eased);
          el.textContent = current + suffix;
          if (progress < 1) {
            requestAnimationFrame(step);
          } else {
            el.textContent = raw;
          }
        }
        requestAnimationFrame(step);
        obs.unobserve(el);
      });
    }, { threshold: 0.4 });
    counters.forEach(function (el) { counterObserver.observe(el); });
  }
});
