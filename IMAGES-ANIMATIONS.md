# UMCO v2.1 — Interactive Layer: Assets, Animation & Implementation Spec

Companion to `DESIGN.md`. Everything below is **already implemented** in the static site
(`assets/main.css` v2.1 block + `assets/main.js` v2.1 IIFE), except where marked *(Next.js)*.

---

## 1. Image Asset Plan (all royalty-free, Unsplash)

### Hero slider (1920w, q80)
| Slide | Source URL | Alt text | Placement |
|---|---|---|---|
| 1 Business Growth | unsplash.com/photos/photo-1449824913935-59a10b8d2000 | City business district skyline at dusk | `.hs-slide:1 .hs-bg` |
| 2 Digital Transformation | unsplash.com/photos/photo-1551288049-bebda4e38f71 | Analytics dashboard with performance charts | `.hs-slide:2 .hs-bg` |
| 3 Audit & Compliance | unsplash.com/photos/photo-1454165804606-c3d57bc86b40 | Executive reviewing financial reports and charts | `.hs-slide:3 .hs-bg` |
| 4 Risk & Advisory | unsplash.com/photos/photo-1558494949-ef010cbdcc31 | Data centre infrastructure, network operations | `.hs-slide:4 .hs-bg` |

### Service carousel (700w, q78, `loading="lazy"` — all people-free by policy)
audit `photo-1434626881859-194d67b2b86f` (charts/graph paper) · tax `photo-1554224154-26032ffc0d07` (calculator on tax forms) · risk `photo-1563986768609-322da13575f3` · financial `photo-1460925895917-afdab827c52f` (laptop dashboard) · digital `photo-1518770660439-4636190af475` (circuit board) · BPO `photo-1497366216548-37526070297c` (office interior) · corporate `photo-1486406146926-c627a92ad1ab` (corporate towers) · management `photo-1497366811353-6870744d04b2` (office interior)

### Industry slider (600w, q78, lazy — all people-free by policy)
Manufacturing `photo-1565043666747-69f6646db940` · Technology `photo-1531297484001-80022131f5a1` (laptop, dark desk) · Healthcare `photo-1538108149393-fbbd81895907` (hospital ward) · Retail `photo-1441986300917-64674bd600d8` (store racks) · Education `photo-1481627834876-b7833e8f5570` (library) · Financial Services `photo-1611974789855-9c2a0a7236a3` (candlestick chart) · Real Estate `photo-1486325212027-8081e485255e` (city towers) · International `photo-1526304640581-d334cdbbf45e` (currency)

### Insights featured
`photo-1611974789855-9c2a0a7236a3` (1200w) — market chart on screen.

**Image policy: no photographs of people anywhere on the site** — objects, environments, architecture, and data visuals only.

**Optimization recommendations**
- Production: download → serve as AVIF/WebP with JPEG fallback; `srcset` at 480/768/1280/1920.
- Hero slide 1 image: `fetchpriority="high"`, no lazy (it's the LCP); all others lazy.
- Every Unsplash URL already carries `w=` and `q=` params to cap transfer size.
- All images sit under a navy gradient veil → low-quality compression is invisible; q78 is enough.

## 2. Slider Content (implemented)

**Hero (4 slides, 7s auto-advance, pause on hover, swipe on touch):**
1. *Business Growth* — "Helping businesses scale with confidence."
2. *Digital Transformation* — "Transforming finance through technology."
3. *Audit & Compliance* — "Strengthening trust through assurance."
4. *Risk & Advisory* — "Managing risk in a rapidly changing world."
Each: gold-pulse tag → headline (serif-gold accent) → subline → Book Consultation + Explore Services. Progress dots animate fill across the 7s interval.

**Carousels:** Services (8 cards, hover-expand bullet reveal), Industries (8 image tiles, hover zoom + description reveal), Case Studies (6 cards with metric chips). All use native scroll-snap with arrow buttons + gold progress bar — buttery on mobile, zero library weight.

## 3. Animation Specifications

| Element | Effect | Duration / Easing |
|---|---|---|
| Hero slide change | crossfade + Ken Burns zoom (1 → 1.07) | 1100ms fade, 9s zoom |
| Slide copy | staggered rise (tag→h1→p→CTAs) | 700–760ms, delays 250/400/550/690ms |
| Hero bg | mouse parallax ±16px / ±10px | direct, pointer:fine only |
| Particles | 14 gold/white dots drifting upward | 14–22s loops, GPU transform only |
| Counters | cubic ease-out count-up on intersection | 1700ms |
| Service card hover | lift −7px, image scale 1.07, icon tilt, bullets max-height reveal | 420–700ms `cubic-bezier(0.32,0.72,0,1)` |
| Industry tile hover | image scale 1.08, body slides up, description fades in | 480–800ms |
| Feature cards | stagger entrance 90ms/card; hover: gold top-bar scaleX, icon morph (scale 1.08, −5°, navy/gold invert) | 420ms |
| Scroll reveals | translateY(26px)→0 + fade | 650–700ms |
| Map | grayscale(0.55) → color on hover | 420ms |

All within the 300–800ms interaction window (long durations are ambient, not blocking). `prefers-reduced-motion` disables every animation and the autoplay timer.

## 4. Framer Motion Examples *(Next.js)*

```tsx
// Hero slide copy
const rise = {
  hidden: { opacity: 0, y: 30 },
  show: (i: number) => ({ opacity: 1, y: 0,
    transition: { delay: 0.25 + i * 0.15, duration: 0.7, ease: [0.32, 0.72, 0, 1] } }),
};
<AnimatePresence mode="wait">
  <motion.div key={slide.id} initial="hidden" animate="show" exit={{ opacity: 0 }}>
    {[Tag, H1, Sub, CTAs].map((El, i) => <motion.div key={i} custom={i} variants={rise}><El/></motion.div>)}
  </motion.div>
</AnimatePresence>

// Section reveal (replaces IntersectionObserver)
<motion.section initial={{ opacity: 0, y: 26 }} whileInView={{ opacity: 1, y: 0 }}
  viewport={{ once: true, margin: "-4%" }} transition={{ duration: 0.65 }} />

// Stagger grid
<motion.div variants={{ show: { transition: { staggerChildren: 0.09 } } }} />
```

## 5. GSAP Recommendations *(Next.js or CDN)*

- `ScrollTrigger` for the hero metrics pin + parallax depth on `.hs-bg` (`yPercent: -8, scrub: 0.6`).
- `gsap.utils.toArray('.feat-card')` + batch for grid staggers.
- Counter: `gsap.to(obj, { val: target, snap: { val: 1 }, scrollTrigger: {...} })`.
- Skip GSAP for the carousels — native scroll-snap outperforms transform-based carousels on mobile.

## 6–8. Responsive, Mobile, Accessibility

- Breakpoints 1020/760/480px; carousels collapse to swipe-first (arrows remain), hero metrics 2×2, feature grid 1-col.
- Touch: hero swipe gesture implemented; snap carousels are native momentum scroll; tap targets ≥42px.
- A11y: `aria-roledescription="carousel"`, per-slide `aria-label="Slide n of 4"`, labelled arrow/dot buttons, `tabindex="0"` on flip cards so hover reveals work by keyboard focus, reduced-motion kills autoplay + animation, decorative layers `aria-hidden`.

## 9. SEO Image Optimization

Descriptive alt text on every content image (pattern: "{subject} — UMCO"); decorative backgrounds via CSS so they don't pollute the accessibility tree; lazy + dimensions to protect CLS; on deploy add `og:image` (1200×630 navy/gold brand card) per page.

## 10. Production Checklist

1. `python3 _build.py` regenerates all 17 pages.
2. Self-host the four hero images (AVIF) before launch; keep Unsplash for long-tail cards if desired.
3. Add `sitemap.xml`, `robots.txt`, JSON-LD (`ProfessionalService`).
4. Wire the contact form to email/CRM (currently client-side confirm).
5. Lighthouse target: ≥90 mobile / ≥95 desktop — the JS is ~6KB unminified with zero dependencies, so the only LCP lever is hero image delivery.
