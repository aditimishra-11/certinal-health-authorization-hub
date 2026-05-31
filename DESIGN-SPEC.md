# Certinal Health Authorization Hub — Information Architecture & Design System

## 1. The Narrative Arc (why this order)
The story is a classic **wedge argument**: reframe the problem → prove a gap exists → name the insight → show the product → prove it works → show why it wins.

| Act | Sections | Job |
|-----|----------|-----|
| **I. Reframe** | 1–2 | Data flows everywhere; consent isn't the real problem |
| **II. Prove the gap** | 3–6 | Who owns what → the missing layer → a real broken workflow |
| **III. The insight** | 7–9 | Permission *execution*, why Certinal, the product reveal |
| **IV. The product** | 10–14 | Module explorer + 4 deep dives with UI mockups |
| **V. Proof** | 15–17 | 3 clickable prototype journeys |
| **VI. Strategy** | 18–20 | MVP vs future roadmap, competitive win, closing thesis |

## 2. Section map (20 scenes)
1. Hero — "India's Healthcare Data Problem Isn't Consent" (dark, animated data-flow) 
2. Healthcare ecosystem — same permission challenge across entities (dark)
3. Current landscape — layered ownership stack EMR/ABDM/Privacy/Certinal (darker, sticky build)
4. What each player solves — interactive comparison table (light)
5. The missing layer — reveal the Permission Gap (darker, spotlight)
6. Real example — research study breaks across PDF/Email/Excel (tint)
7. Core insight — huge typography moment (darker, full-bleed)
8. Why Certinal — strengths mapped to the problem (dark)
9. Product vision — Health Authorization Hub + architecture diagram (dark, hero-2)
10. Product overview — interactive module explorer (surface)
11. Module 1 — Consent Lifecycle + mobile mockup (light)
12. Module 2 — Authorization Workflow engine builder (dark)
13. Module 3 — Withdrawal Management lifecycle (tint)
14. Module 4 — Audit Evidence Vault timeline (darker)
15. Prototype 1 — Patient registration (clickable, light)
16. Prototype 2 — Research participation (clickable, dark)
17. Prototype 3 — Compliance audit (clickable, tint)
18. MVP vs Future — interactive roadmap toggle (dark)
19. Why this wins — positioning quadrant + comparison (surface)
20. Conclusion — "From Consent Capture to Permission Execution" (darker, hero close)

Rhythm of backgrounds alternates dark↔light so the eye never fatigues; the three biggest emotional beats (1, 7, 20) are dark full-bleed.

## 3. Visual design system
- **Type:** Space Grotesk (display) + Inter (body) + JetBrains Mono (labels/code). Tight negative tracking on headlines.
- **Palette:** ink navy `#0A0F1E` base; indigo `#5B7CFA` + healthcare teal `#19C6B0` brand gradient; cyan/violet accents; amber `#F4A93B` = manual/paper pain, rose `#FB6F84` = broken, green `#2FD79B` = resolved.
- **Surfaces:** layered navy cards on dark, white cards on light; glassmorphism for floating UI.
- **Motion:** IntersectionObserver reveal (up/scale/fade), staggered children, sticky-scroll builds, SVG path-draw, marquee data-dots. Respects `prefers-reduced-motion`.
- **Components:** cards, pills/chips (signal-colored), diagram nodes + flow arrows, device & browser mockup frames, timeline, comparison table, stat blocks, progress bar + dot-nav.

## 4. Build contract for section authors
- Each section = one `<section class="scene scene--X" id="sN" data-scene>` with a `.container`.
- Use shared utilities/components from `styles.css`. Any custom CSS/JS is **prefixed `sN-`** and scoped to the section to prevent collisions.
- Animations: add `data-reveal="up|scale|fade"` and `.stagger` — global JS wires them.
- Self-contained: section-specific JS wrapped in an IIFE scoped to `#sN`.
