/* ============================================================
   Global scrollytelling engine — reveals, progress, nav, sticky
   Section-specific interactivity lives in each section's own IIFE.
   ============================================================ */
(function () {
  "use strict";

  /* ---- Embed mode: ?only=<sectionId> shows just that one prototype (used by the PRD "See it" modal) ---- */
  var ONLY = new URLSearchParams(window.location.search).get("only");
  if (ONLY) {
    var keep = document.getElementById(ONLY);
    if (keep) {
      document.body.classList.add("is-embed");
      Array.prototype.forEach.call(document.querySelectorAll("main > *"), function (el) {
        if (el !== keep) el.style.display = "none";
      });
      ["topnav", "dotnav", "progress"].forEach(function (id) {
        var e = document.getElementById(id);
        if (e) e.style.display = "none";
      });
      var ft = document.querySelector(".site-footer");
      if (ft) ft.style.display = "none";
      keep.querySelectorAll("[data-reveal]").forEach(function (e) { e.classList.add("is-visible"); });
      keep.querySelectorAll(".stagger").forEach(function (e) { e.classList.add("is-visible"); });
    }
  }

  /* ---- Reveal on scroll (IntersectionObserver) ---- */
  const revealEls = document.querySelectorAll("[data-reveal], .stagger");
  const io = new IntersectionObserver(
    (entries) => {
      entries.forEach((e) => {
        if (e.isIntersecting) {
          const el = e.target;
          const delay = el.getAttribute("data-delay");
          if (delay) el.style.transitionDelay = delay + "ms";
          el.classList.add("is-visible");
          io.unobserve(el);
        }
      });
    },
    { threshold: 0.16, rootMargin: "0px 0px -8% 0px" }
  );
  revealEls.forEach((el) => io.observe(el));

  /* ---- Scroll progress bar ---- */
  const bar = document.getElementById("progress");
  const onScroll = () => {
    const se = document.scrollingElement || document.documentElement;
    const top = se.scrollTop || window.pageYOffset || 0;
    const max = se.scrollHeight - se.clientHeight;
    const scrolled = max > 0 ? top / max : 0;
    if (bar) bar.style.width = (scrolled * 100).toFixed(2) + "%";

    const nav = document.getElementById("topnav");
    if (nav) nav.classList.toggle("is-stuck", top > 40);
  };
  document.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  /* ---- Dot navigation ---- */
  const scenes = Array.from(document.querySelectorAll("[data-scene]"));
  const dotnav = document.getElementById("dotnav");
  if (dotnav && scenes.length) {
    scenes.forEach((sc, i) => {
      const b = document.createElement("button");
      b.title = sc.getAttribute("data-title") || "Section " + (i + 1);
      b.addEventListener("click", () =>
        sc.scrollIntoView({ behavior: "smooth" })
      );
      dotnav.appendChild(b);
    });
    const dots = Array.from(dotnav.children);
    const dotIo = new IntersectionObserver(
      (entries) => {
        entries.forEach((e) => {
          if (e.isIntersecting) {
            const i = scenes.indexOf(e.target);
            dots.forEach((d, di) => d.classList.toggle("is-active", di === i));
          }
        });
      },
      { threshold: 0.5 }
    );
    scenes.forEach((sc) => dotIo.observe(sc));
  }

  /* ---- Counter animation for [data-count] ---- */
  const countIo = new IntersectionObserver(
    (entries) => {
      entries.forEach((e) => {
        if (!e.isIntersecting) return;
        const el = e.target;
        const target = parseFloat(el.getAttribute("data-count"));
        const suffix = el.getAttribute("data-suffix") || "";
        const dur = 1400;
        let start = null;
        const step = (ts) => {
          if (!start) start = ts;
          const p = Math.min((ts - start) / dur, 1);
          const eased = 1 - Math.pow(1 - p, 3);
          const val = target * eased;
          el.textContent =
            (target % 1 === 0 ? Math.round(val) : val.toFixed(1)) + suffix;
          if (p < 1) requestAnimationFrame(step);
        };
        requestAnimationFrame(step);
        countIo.unobserve(el);
      });
    },
    { threshold: 0.6 }
  );
  document.querySelectorAll("[data-count]").forEach((el) => countIo.observe(el));

  /* ---- SVG path-draw on view ---- */
  const drawIo = new IntersectionObserver(
    (entries) => {
      entries.forEach((e) => {
        if (e.isIntersecting) {
          e.target.classList.add("is-drawn");
          drawIo.unobserve(e.target);
        }
      });
    },
    { threshold: 0.3 }
  );
  document.querySelectorAll("[data-draw]").forEach((el) => drawIo.observe(el));
})();
