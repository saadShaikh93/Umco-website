# UMCO Website v2 — Design & Implementation Specification

Enterprise-grade redesign for Umair Manzoor & Co Chartered Accountants.
Benchmark set: Deloitte, PwC, KPMG (authority) × Stripe, Mercury, Ramp (craft).

---

## 1. Information Architecture

```
/
├── index.html                  Homepage
├── services.html               Services overview (8 practices)
│   └── services/
│       ├── audit-assurance.html
│       ├── tax-advisory.html
│       ├── financial-advisory.html
│       ├── management-consulting.html
│       ├── business-process-outsourcing.html
│       ├── digital-transformation.html
│       ├── risk-advisory.html
│       └── corporate-advisory.html
├── industries.html             8 sectors + international-investor section
├── about.html                  Story, values, standards
├── team.html                   Leadership
├── case-studies.html           6 anonymised engagements (Challenge/Solution/Outcome)
├── insights.html               Article grid (6 briefings)
├── careers.html                Culture + open roles
└── contact.html                Consultation booking form + direct channels
```

Primary nav: Services · Industries · About · Case Studies · Insights · Contact + **Book Consultation** CTA.
Careers lives in footer + mobile menu (low-frequency audience, kept out of primary nav to protect conversion focus).

## 2. Color Palette

| Token | Hex | Use |
|---|---|---|
| `--navy-950` | `#050B16` | Footer |
| `--navy-900` | `#0A1628` | Hero, dark bands, primary buttons |
| `--navy-800` | `#102341` | Hover states, links |
| `--gold` | `#C6A35D` | Accent: underlines, metrics, serif accents |
| `--gold-deep` | `#A8853F` | Gold on light backgrounds (AA contrast) |
| `--paper` | `#F7F8FA` | Alternate section background |
| `--ink` | `#16202F` | Body headings/text |
| `--ink-muted` | `#5B6678` | Secondary text |
| `--line` | `#E5E8EE` | Borders, hairline grids |

Rule: gold is **never** used as a fill for large areas — only lines, numerals, icons, and one CTA per viewport. That restraint is what reads "premium" instead of "golden WordPress theme."

## 3. Typography System

- **Inter** (400–700) — UI and body. Tight tracking (−0.02em) on headings.
- **Instrument Serif** italic — editorial accent on the final phrase of key headlines (`.serif-accent`), rendered gold on dark. This is the signature device of the identity.
- Scale: `clamp()`-based fluid type. H1 38–68px, H2 30–46px, body 16px/1.6, captions 11–13px with letter-spaced uppercase kickers.

## 4. Component Library (all in `assets/main.css`)

| Component | Class | Notes |
|---|---|---|
| Navigation | `.nav`, `.nav-menu`, `.mobile-menu` | Blur backdrop, gold underline hover, staggered entrance, burger drawer |
| Buttons | `.btn-gold / -navy / -ghost-light / -ghost-dark` | 4 variants cover every surface |
| Hero | `.hero`, `.hero-metrics` | Grid-line texture, radial gold glow, animated counters |
| Trust strip | `.trust-strip` | Credentials bar under hero |
| Service card | `.svc-card` in `.svc-grid` | Hairline grid, gold bottom-border reveal |
| Industry tile | `.ind-tile` | Dark band tiles |
| Case card | `.case-card` | Challenge/Solution/Outcome rows |
| Team card | `.team-card` | Avatar, credentials chips |
| Insight card | `.insight-card` | Category + date meta |
| Process | `.process-grid` | 4-step cells |
| Figure panel | `.figure-panel` | Dark stat panel with gold numerals |
| Form | `.form-shell`, `.field` | Bottom-border inputs, animated gold underline on focus |
| CTA band | `.cta-band` | Dark conversion band, used on every page |
| Page hero | `.page-hero` | Interior pages: breadcrumb + headline + lede |

Motion: single easing curve `cubic-bezier(0.32,0.72,0,1)` everywhere; `IntersectionObserver` reveals (`.reveal`, `.reveal-stagger`); `prefers-reduced-motion` fully respected.

## 5. Content Principles (conversion-focused)

- Every page ends in the same CTA band → one conversion path: **contact.html**.
- Case studies are anonymised but specific ("refund cycle under 90 days") — credible without fabricating testimonials.
- Leadership page names only the real founder; practice areas are presented honestly as teams, not invented people.
- Copy speaks to the buyer's fear (audit adjustments, blocked refunds, partner disappearing after signing), not the firm's vanity.

## 6. SEO

Implemented: unique `<title>`/`meta description`/OG tags per page, semantic landmarks (`header/nav/section/footer`), single H1 per page, descriptive alt text, breadcrumbs on interior pages.
Recommended next: `sitemap.xml` + `robots.txt` on deploy, `Organization` + `ProfessionalService` JSON-LD, canonical URLs once the domain is wired, self-hosted fonts for LCP.

## 7. React / Next.js Migration Plan

When ready to move to Next.js (App Router):

1. **Scaffold** — `create-next-app` (TypeScript, Tailwind optional; the token system maps 1:1 to a Tailwind theme or CSS modules).
2. **Layout shell** — `app/layout.tsx` holds Nav + Footer (port `navbar()`/`footer()` from `_build.py`); fonts via `next/font` (Inter + Instrument Serif) — eliminates the Google Fonts render-block.
3. **Data layer** — the Python dicts in `_build.py` (SERVICES, INDUSTRIES, CASES, INSIGHTS) become typed objects in `lib/content.ts`; service pages become one dynamic route `app/services/[slug]/page.tsx` with `generateStaticParams`.
4. **Components** — each item in the table above becomes a React component; reveal animations port to `framer-motion` (`whileInView` + `staggerChildren`) for spring physics.
5. **Insights → MDX** — `app/insights/[slug]` with contentlayer or MDX for a real publishing workflow.
6. **Forms** — contact form posts to a route handler → email (Resend) or CRM; add spam honeypot.
7. **Deploy** — Vercel; `next/image` for any photography; target Lighthouse ≥ 95 across the board.

---

*Rebuild the static site anytime with `python3 _build.py`. Previous site preserved in `_v1-backup/`.*
