# Certinal Health Authorization Hub — Product Case Study

A scrollytelling product case study + v1 PRD for a **DPDP (Digital Personal Data Protection Act, 2023) compliance product for Indian healthcare**.

**Thesis:** Healthcare doesn't have a *consent* problem — it has a **permission execution** problem. The Certinal Health Authorization Hub is the layer hospitals use to *act on* a patient's permission and *prove it*, alongside ABDM and the systems they already run.

## What's here

| File | What it is |
|------|------------|
| `index.html` | The case-study narrative — 20+ scenes, an animated architecture diagram, a competitive positioning map, and **8 clickable prototype journeys** (3 primary deep-dives + 5 secondary, opened in a modal). |
| `prd.html` | The **v1 PRD / feature map** — modules, 32 features (20 P0) with user stories + acceptance criteria, two detailed flows, OPD consent UX, tech-stack fit, metrics, rollout, and strategy. |
| `styles.css` | Shared design system (tokens, components, animation engine). |
| `app.js` | Scroll engine (reveal-on-scroll, progress bar, dot-nav) + prototype embed mode. |
| `DESIGN-SPEC.md` | Information architecture + visual design system. |
| `_build/` | Generation scripts, feature-map data, and the PRD template used to build the pages. |

## Viewing it

Everything is self-contained vanilla HTML/CSS/JS — no build step.

- **Quickest:** open `index.html` in a browser.
- **Recommended (so the prototype modals and relative links work cleanly):** serve the folder, e.g.
  ```bash
  python3 _build/serve.py        # serves on http://localhost:4599
  # or
  python3 -m http.server 8000
  ```
  then open `http://localhost:4599/index.html`.

Use the **Case Study** ↔ **PRD / v1 Spec** tabs in the header to move between the two.

## Prototype journeys

**Primary (deep, with non-happy paths):** OPD consent capture · Authorizing a research study · Withdrawal that executes.
**Secondary (open via cards):** Patient consent wallet · Cross-provider sharing · Emergency break-glass · Compliance audit · Building a workflow (admin).

---

**Author:** Aditi Mishra · Product case study (DPDP × Indian Healthcare).
Built with AI assistance — see the "How I used AI" note in the PRD.
