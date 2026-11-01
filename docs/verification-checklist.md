# katalogarkan — verification-checklist.md

---

## Document Information

| Property | Value |
|----------|-------|
| Document Version | 1.1.0 |
| Project Version | 0.0.1 (Planning) |
| Last Updated | 2026-10-26 |
| Status | Approved — Source of Truth |
| Project | Personal branding & katalog website |
| Owner | Arkan (Full Stack Web Developer) |
| Related | `blueprint.md` §20 (Execution Phases), §21 (Acceptance Criteria) |
| Total Checks | 221 |
| Total Phases | 6 |
| Legend | ☐ = pending · ✅ = passed · ❌ = failed |

---

## Table of Contents

1. [Purpose](#1-purpose)
2. [How to Use](#2-how-to-use)
3. [Phase 1 — Fondasi Proyek](#3-phase-1--fondasi-proyek)
4. [Phase 2 — Desain & Home](#4-phase-2--desain--home)
5. [Phase 3 — Halaman Statis](#5-phase-3--halaman-statis)
6. [Phase 4 — Katalog + Filter](#6-phase-4--katalog--filter)
7. [Phase 5 — Blog + Detail](#7-phase-5--blog--detail)
8. [Phase 6 — Polish & Deploy](#8-phase-6--polish--deploy)
9. [Overall Summary](#9-overall-summary)
10. [Quick Verification Commands](#10-quick-verification-commands)
11. [Change Log](#11-change-log)

---

## 1. Purpose

### 1.1 What This Document Is

A phase-by-phase checklist to verify each step of the katalogarkan project is complete and working. Every item is binary: done or not done. Total: 221 checks across 6 phases.

### 1.2 How It Differs from Blueprint

| Blueprint §21 | This Document |
|---------------|---------------|
| High-level acceptance criteria | Granular, per-task checks |
| 18 criteria | 221 checks |
| Summary | Step-by-step verification |

**Rule:** Blueprint defines what "done" means. This document tracks whether each item is done.

---

## 2. How to Use

### 2.1 Workflow

```
1. Start a phase
   │
   ▼
2. Work through tasks (blueprint §20)
   │
   ▼
3. After each task, open this file
   │
   ▼
4. Check the box (☐ → ✅)
   │
   ▼
5. If a check fails, fix and re-verify
   │
   ▼
6. Phase complete when all boxes ✅
   │
   ▼
7. Move to next phase
```

### 2.2 Status Symbols

| Symbol | Meaning |
|--------|---------|
| ☐ | Pending — not yet verified |
| ✅ | Passed — verified working |
| ❌ | Failed — needs fix |

### 2.3 Verification Methods

| Method | When to Use |
|--------|-------------|
| **Visual** | Open page in browser, check appearance |
| **Command** | Run terminal command, check output |
| **DevTools** | Inspect element, check network/console |
| **Lighthouse** | Run audit in Chrome DevTools |
| **Manual** | Click, type, interact |

---

## 3. Phase 1 — Fondasi Proyek

**Goal:** Astro project runs locally and deploys to GitHub Pages.

**Prerequisites:** Node.js 20+, Git, GitHub account, repository exists.

### 3.1 Project Setup

| # | Check | Method | Status |
|---|-------|--------|:---:|
| 1.1 | Project folder created via `npm create astro@latest` | Command | ☐ |
| 1.2 | `npm install` completes without errors | Command | ☐ |
| 1.3 | `node_modules/` folder exists | Visual | ☐ |
| 1.4 | `package.json` has `astro` dependency | Visual | ☐ |

### 3.2 Configuration Files

| # | Check | Method | Status |
|---|-------|--------|:---:|
| 1.5 | `astro.config.mjs` exists with `site: 'https://katalogarkan.github.io'` | Visual | ☐ |
| 1.6 | `astro.config.mjs` has `tailwind()` integration | Visual | ☐ |
| 1.7 | `astro.config.mjs` has `react()` integration | Visual | ☐ |
| 1.8 | `astro.config.mjs` has `sitemap()` integration | Visual | ☐ |
| 1.9 | `tailwind.config.mjs` exists with `darkMode: 'media'` | Visual | ☐ |
| 1.10 | `tailwind.config.mjs` uses `var(--color-*)` for colors (per design-system §18) | Visual | ☐ |
| 1.11 | `tailwind.config.mjs` has `border: { DEFAULT: 'var(--color-border)' }` | Visual | ☐ |
| 1.12 | `tailwind.config.mjs` has `fontFamily.sans` with Inter | Visual | ☐ |
| 1.13 | `tsconfig.json` exists | Visual | ☐ |
| 1.14 | `.gitignore` ignores `node_modules/`, `dist/`, `.astro/` | Visual | ☐ |
| 1.15 | `LICENSE` file exists (MIT) | Visual | ☐ |

### 3.3 Base Files

| # | Check | Method | Status |
|---|-------|--------|:---:|
| 1.16 | `src/styles/global.css` exists with Tailwind directives | Visual | ☐ |
| 1.17 | `global.css` defines CSS variables in `:root` (per design-system §19) | Visual | ☐ |
| 1.18 | `global.css` overrides CSS variables in `@media (prefers-color-scheme: dark)` | Visual | ☐ |
| 1.19 | `src/layouts/BaseLayout.astro` exists | Visual | ☐ |
| 1.20 | `BaseLayout.astro` has `<html lang="en">` | Visual | ☐ |
| 1.21 | `BaseLayout.astro` imports `global.css` | Visual | ☐ |
| 1.22 | `BaseLayout.astro` loads Inter font from Google Fonts | Visual | ☐ |
| 1.23 | `src/components/Header.astro` exists (placeholder) | Visual | ☐ |
| 1.24 | `src/components/Footer.astro` exists (placeholder) | Visual | ☐ |
| 1.25 | `src/pages/index.astro` exists | Visual | ☐ |
| 1.26 | `index.astro` uses `BaseLayout` | Visual | ☐ |

### 3.4 Content Schema

| # | Check | Method | Status |
|---|-------|--------|:---:|
| 1.27 | `src/content/config.ts` exists | Visual | ☐ |
| 1.28 | `config.ts` defines `katalog` collection | Visual | ☐ |
| 1.29 | `config.ts` defines `blog` collection | Visual | ☐ |
| 1.30 | `katalog` schema has `title`, `description`, `techStack`, `thumbnail`, `category`, `date` | Visual | ☐ |
| 1.31 | `blog` schema has `title`, `date`, `description`, `category` | Visual | ☐ |
| 1.32 | `src/content/katalog/` folder exists | Visual | ☐ |
| 1.33 | `src/content/blog/` folder exists | Visual | ☐ |

### 3.5 Deploy Pipeline

| # | Check | Method | Status |
|---|-------|--------|:---:|
| 1.34 | `.github/workflows/deploy.yml` exists | Visual | ☐ |
| 1.35 | `deploy.yml` uses explicit workflow (checkout + setup-node + npm ci + build + upload-pages-artifact + deploy-pages) per blueprint §18.2 | Visual | ☐ |
| 1.36 | `deploy.yml` triggers on push to `main` | Visual | ☐ |
| 1.37 | `deploy.yml` uses Node 20 | Visual | ☐ |
| 1.38 | GitHub Pages source set to "GitHub Actions" | Settings → Pages | ☐ |
| 1.39 | Workflow permissions set to "Read and write" | Settings → Actions | ☐ |

### 3.6 Local Verification

| # | Check | Method | Status |
|---|-------|--------|:---:|
| 1.40 | `npm run dev` starts without errors | Command | ☐ |
| 1.41 | `localhost:4321` shows "Hello" page | Visual | ☐ |
| 1.42 | `npm run build` succeeds with no errors | Command | ☐ |
| 1.43 | `dist/` folder created after build | Visual | ☐ |

### 3.7 Remote Verification

| # | Check | Method | Status |
|---|-------|--------|:---:|
| 1.44 | Push to `main` triggers GitHub Action | Visual (Actions tab) | ☐ |
| 1.45 | GitHub Action completes with green check | Visual | ☐ |
| 1.46 | `katalogarkan.github.io` shows "Hello" page | Visual | ☐ |

**Phase 1 Summary:** ☐ / 46 checks

---

## 4. Phase 2 — Desain & Home

**Goal:** Home page looks professional, responsive, dark mode works.

**Prerequisites:** Phase 1 complete (all checks ✅).

### 4.1 Header Finalization

| # | Check | Method | Status |
|---|-------|--------|:---:|
| 2.1 | Header has logo/name "Arkan" | Visual | ☐ |
| 2.2 | Header has 9 nav links | Visual | ☐ |
| 2.3 | Nav links: Home, About, Skills, Katalog, Services, Blog, Resources, Testimonials, Contact | Visual | ☐ |
| 2.4 | Header is sticky at top | Visual (scroll) | ☐ |
| 2.5 | Hamburger visible on mobile (< 768px) | DevTools | ☐ |
| 2.6 | Hamburger toggles menu on click | Manual | ☐ |
| 2.7 | Desktop nav hidden on mobile | DevTools | ☐ |
| 2.8 | Hamburger has `aria-label` | Visual (code) | ☐ |
| 2.9 | Hamburger has `aria-expanded` | Visual (code) | ☐ |

### 4.2 Footer Finalization

| # | Check | Method | Status |
|---|-------|--------|:---:|
| 2.10 | Footer has 4 columns | Visual | ☐ |
| 2.11 | Column 1: Name + tagline | Visual | ☐ |
| 2.12 | Column 2: Quick links (Home, About, Katalog, Contact) | Visual | ☐ |
| 2.13 | Column 3: Social links (GitHub, LinkedIn, Email) | Visual | ☐ |
| 2.14 | Column 4: Copyright + version | Visual | ☐ |
| 2.15 | Footer responsive (stack on mobile) | DevTools | ☐ |

### 4.3 Design Tokens

| # | Check | Method | Status |
|---|-------|--------|:---:|
| 2.16 | Primary color applied to links (light mode: `#0969da`) | Visual | ☐ |
| 2.17 | Inter font loaded and applied | DevTools | ☐ |
| 2.18 | Dark mode auto-follows OS preference | Manual (change OS theme) | ☐ |
| 2.19 | Light mode background is white | Visual | ☐ |
| 2.20 | Dark mode background is `#0d1117` | Visual | ☐ |
| 2.21 | No `dark:` variants used in components (except `prose-invert`) | Visual (code grep) | ☐ |

### 4.4 Home Page Sections

| # | Check | Method | Status |
|---|-------|--------|:---:|
| 2.22 | Hero section has name | Visual | ☐ |
| 2.23 | Hero section has tagline | Visual | ☐ |
| 2.24 | Hero has "View Katalog" button | Visual | ☐ |
| 2.25 | Hero has "Contact Me" button | Visual | ☐ |
| 2.26 | Featured projects section exists | Visual | ☐ |
| 2.27 | Featured section hides if no projects (empty state) | Visual | ☐ |
| 2.28 | Skills summary section exists | Visual | ☐ |
| 2.29 | Testimonials section exists | Visual | ☐ |
| 2.30 | Testimonials section hides if empty | Visual | ☐ |
| 2.31 | CTA section exists | Visual | ☐ |

### 4.5 Responsive Check

| # | Check | Method | Status |
|---|-------|--------|:---:|
| 2.32 | Home renders at 320px width | DevTools | ☐ |
| 2.33 | Home renders at 768px width | DevTools | ☐ |
| 2.34 | Home renders at 1024px width | DevTools | ☐ |
| 2.35 | No horizontal scroll at any breakpoint | DevTools | ☐ |
| 2.36 | Text readable at 320px | Visual | ☐ |

### 4.6 Navigation Check

| # | Check | Method | Status |
|---|-------|--------|:---:|
| 2.37 | All 9 nav links navigate correctly | Manual | ☐ |
| 2.38 | Active link highlighted (if implemented) | Manual | ☐ |
| 2.39 | Logo click returns to Home | Manual | ☐ |

**Phase 2 Summary:** ☐ / 39 checks

---

## 5. Phase 3 — Halaman Statis

**Goal:** 6 static pages + 404 complete.

**Prerequisites:** Phase 2 complete (all checks ✅).

### 5.1 About Page

| # | Check | Method | Status |
|---|-------|--------|:---:|
| 3.1 | `/about` page renders | Visual | ☐ |
| 3.2 | Bio section with photo | Visual | ☐ |
| 3.3 | Timeline section | Visual | ☐ |
| 3.4 | Values section (3 cards) | Visual | ☐ |
| 3.5 | CV download link (if available) | Visual | ☐ |
| 3.6 | Info section (location, languages) | Visual | ☐ |

### 5.2 Skills Page

| # | Check | Method | Status |
|---|-------|--------|:---:|
| 3.7 | `/skills` page renders | Visual | ☐ |
| 3.8 | 4 categories: Frontend, Backend, Database, DevOps | Visual | ☐ |
| 3.9 | Skill bars with level (%) | Visual | ☐ |
| 3.10 | `SkillBadge` component renders | Visual | ☐ |

### 5.3 Services Page

| # | Check | Method | Status |
|---|-------|--------|:---:|
| 3.11 | `/services` page renders | Visual | ☐ |
| 3.12 | 3 package cards | Visual | ☐ |
| 3.13 | Process section (4 steps) | Visual | ☐ |
| 3.14 | FAQ section (3–4 questions) | Visual | ☐ |

### 5.4 Resources Page

| # | Check | Method | Status |
|---|-------|--------|:---:|
| 3.15 | `/resources` page renders | Visual | ☐ |
| 3.16 | Empty state shows "No resources yet" | Visual | ☐ |
| 3.17 | Grid layout responsive | DevTools | ☐ |

### 5.5 Testimonials Page

| # | Check | Method | Status |
|---|-------|--------|:---:|
| 3.18 | `/testimonials` page renders | Visual | ☐ |
| 3.19 | Empty state shows "No testimonials yet" | Visual | ☐ |
| 3.20 | Grid layout responsive | DevTools | ☐ |

### 5.6 Contact Page

| # | Check | Method | Status |
|---|-------|--------|:---:|
| 3.21 | `/contact` page renders | Visual | ☐ |
| 3.22 | Form has Name, Email, Subject, Message fields | Visual | ☐ |
| 3.23 | Form has submit button | Visual | ☐ |
| 3.24 | Every field has `<label>` | Visual (code) | ☐ |
| 3.25 | Form submits to Formspree | Manual (test submit) | ☐ |
| 3.26 | Success message shows after submit | Manual | ☐ |
| 3.27 | Social links (GitHub, LinkedIn, Email) | Visual | ☐ |
| 3.28 | Honeypot field exists (spam protection) | Visual (code) | ☐ |

### 5.7 404 Page

| # | Check | Method | Status |
|---|-------|--------|:---:|
| 3.29 | `/404` page renders | Visual | ☐ |
| 3.30 | Shows "404 — Page not found" | Visual | ☐ |
| 3.31 | "Back to Home" button works | Manual | ☐ |

### 5.8 Responsive & Dark Mode

| # | Check | Method | Status |
|---|-------|--------|:---:|
| 3.32 | All 6 pages render at 320px | DevTools | ☐ |
| 3.33 | All 6 pages render at 768px | DevTools | ☐ |
| 3.34 | All 6 pages render at 1024px | DevTools | ☐ |
| 3.35 | All 6 pages work in dark mode | Manual | ☐ |

**Phase 3 Summary:** ☐ / 35 checks

---

## 6. Phase 4 — Katalog + Filter

**Goal:** Katalog page with filter/search/sort works.

**Prerequisites:** Phase 3 complete (all checks ✅).

### 6.1 ProjectCard Component

| # | Check | Method | Status |
|---|-------|--------|:---:|
| 4.1 | `ProjectCard.astro` exists | Visual | ☐ |
| 4.2 | Renders thumbnail | Visual | ☐ |
| 4.3 | Renders title | Visual | ☐ |
| 4.4 | Renders description | Visual | ☐ |
| 4.5 | Renders tech badges | Visual | ☐ |
| 4.6 | Renders demo link (if `demoUrl`) | Visual | ☐ |
| 4.7 | Renders repo link (if `repoUrl`) | Visual | ☐ |
| 4.8 | Whole card links to `/katalog/[slug]` | Manual | ☐ |
| 4.9 | Hover effect (shadow lift) | Manual | ☐ |

### 6.2 Katalog Page

| # | Check | Method | Status |
|---|-------|--------|:---:|
| 4.10 | `/katalog` page renders | Visual | ☐ |
| 4.11 | Empty state shows "No projects yet" | Visual | ☐ |
| 4.12 | Grid layout (1/2/3 columns) | DevTools | ☐ |

### 6.3 KatalogFilter (React Island)

| # | Check | Method | Status |
|---|-------|--------|:---:|
| 4.13 | `KatalogFilter.tsx` exists | Visual | ☐ |
| 4.14 | Hydrates with `client:load` | Visual (code) | ☐ |
| 4.15 | Category filter dropdown works | Manual (with temp data) | ☐ |
| 4.16 | Search input filters by title | Manual | ☐ |
| 4.17 | Search input filters by techStack | Manual | ☐ |
| 4.18 | Sort by date (newest) works | Manual | ☐ |
| 4.19 | Sort by date (oldest) works | Manual | ☐ |
| 4.20 | Combined filter + search works | Manual | ☐ |

### 6.4 Performance

| # | Check | Method | Status |
|---|-------|--------|:---:|
| 4.21 | JS bundle for `/katalog` < 50KB gzipped | DevTools (Network) | ☐ |
| 4.22 | React island hydrates without errors | DevTools (Console) | ☐ |
| 4.23 | No console errors on `/katalog` | DevTools (Console) | ☐ |

### 6.5 Test with Temp Data

| # | Check | Method | Status |
|---|-------|--------|:---:|
| 4.24 | Add 1 temp project to `src/content/katalog/` | Manual | ☐ |
| 4.25 | Temp project renders in grid | Visual | ☐ |
| 4.26 | Filter by category works with temp data | Manual | ☐ |
| 4.27 | Search works with temp data | Manual | ☐ |
| 4.28 | Sort works with temp data | Manual | ☐ |
| 4.29 | Delete temp project after testing | Manual | ☐ |

**Phase 4 Summary:** ☐ / 29 checks

---

## 7. Phase 5 — Blog + Detail

**Goal:** Blog list + dynamic detail pages work.

**Prerequisites:** Phase 4 complete (all checks ✅).

### 7.1 BlogCard Component

| # | Check | Method | Status |
|---|-------|--------|:---:|
| 5.1 | `BlogCard.astro` exists | Visual | ☐ |
| 5.2 | Renders title | Visual | ☐ |
| 5.3 | Renders date | Visual | ☐ |
| 5.4 | Renders description | Visual | ☐ |
| 5.5 | Renders category badge | Visual | ☐ |
| 5.6 | Renders tags | Visual | ☐ |
| 5.7 | Whole card links to `/blog/[slug]` | Manual | ☐ |

### 7.2 Blog Page

| # | Check | Method | Status |
|---|-------|--------|:---:|
| 5.8 | `/blog` page renders | Visual | ☐ |
| 5.9 | Empty state shows "No articles yet" | Visual | ☐ |
| 5.10 | Draft articles hidden (`draft: true`) | Manual (add draft) | ☐ |

### 7.3 PostLayout

| # | Check | Method | Status |
|---|-------|--------|:---:|
| 5.11 | `PostLayout.astro` exists | Visual | ☐ |
| 5.12 | Renders article title | Visual | ☐ |
| 5.13 | Renders date | Visual | ☐ |
| 5.14 | Renders category | Visual | ☐ |
| 5.15 | Renders tags | Visual | ☐ |
| 5.16 | Renders prose body | Visual | ☐ |
| 5.17 | Renders back link to `/blog` | Visual | ☐ |

### 7.4 Dynamic Routes

| # | Check | Method | Status |
|---|-------|--------|:---:|
| 5.18 | `blog/[slug].astro` exists | Visual | ☐ |
| 5.19 | `getStaticPaths` implemented | Visual (code) | ☐ |
| 5.20 | `katalog/[slug].astro` exists | Visual | ☐ |
| 5.21 | `getStaticPaths` implemented | Visual (code) | ☐ |

### 7.5 Markdown Rendering

| # | Check | Method | Status |
|---|-------|--------|:---:|
| 5.22 | H2 renders correctly | Visual | ☐ |
| 5.23 | H3 renders correctly | Visual | ☐ |
| 5.24 | Bold renders correctly | Visual | ☐ |
| 5.25 | Italic renders correctly | Visual | ☐ |
| 5.26 | Links render correctly | Visual | ☐ |
| 5.27 | Lists render correctly | Visual | ☐ |
| 5.28 | Code blocks render with syntax highlighting | Visual | ☐ |
| 5.29 | Tables render correctly | Visual | ☐ |
| 5.30 | Blockquotes render correctly | Visual | ☐ |
| 5.31 | Images render correctly | Visual | ☐ |

### 7.6 Test with Temp Content

| # | Check | Method | Status |
|---|-------|--------|:---:|
| 5.32 | Add 1 temp article to `src/content/blog/` | Manual | ☐ |
| 5.33 | Temp article renders in blog list | Visual | ☐ |
| 5.34 | `/blog/[slug]` renders detail page | Visual | ☐ |
| 5.35 | Add 1 temp project to `src/content/katalog/` | Manual | ☐ |
| 5.36 | `/katalog/[slug]` renders detail page | Visual | ☐ |
| 5.37 | Delete temp content after testing | Manual | ☐ |

### 7.7 Empty States

| # | Check | Method | Status |
|---|-------|--------|:---:|
| 5.38 | Blog empty state shows correctly | Visual | ☐ |
| 5.39 | Katalog empty state shows correctly | Visual | ☐ |

**Phase 5 Summary:** ☐ / 39 checks

---

## 8. Phase 6 — Polish & Deploy

**Goal:** SEO, performance, final deploy.

**Prerequisites:** Phase 5 complete (all checks ✅).

### 8.1 SEO

| # | Check | Method | Status |
|---|-------|--------|:---:|
| 6.1 | `/sitemap-index.xml` accessible | Visual | ☐ |
| 6.2 | `/robots.txt` accessible | Visual | ☐ |
| 6.3 | `robots.txt` references sitemap | Visual | ☐ |
| 6.4 | Every page has unique `<title>` | DevTools | ☐ |
| 6.5 | Every page has `<meta name="description">` | DevTools | ☐ |
| 6.6 | Every page has `<link rel="canonical">` | DevTools | ☐ |
| 6.7 | Every page has OG tags (`og:title`, `og:description`, `og:image`) | DevTools | ☐ |
| 6.8 | OG image is 1200×630 | Visual | ☐ |

### 8.2 Assets

| # | Check | Method | Status |
|---|-------|--------|:---:|
| 6.9 | `/favicon.svg` exists and shows in tab | Visual | ☐ |
| 6.10 | All project thumbnails load | Visual | ☐ |
| 6.11 | All blog cover images load | Visual | ☐ |
| 6.12 | Avatar loads | Visual | ☐ |

### 8.3 Performance

| # | Check | Method | Status |
|---|-------|--------|:---:|
| 6.13 | Lighthouse Performance ≥ 95 (Home) | Lighthouse | ☐ |
| 6.14 | Lighthouse Performance ≥ 95 (Katalog) | Lighthouse | ☐ |
| 6.15 | Lighthouse Accessibility ≥ 95 (Home) | Lighthouse | ☐ |
| 6.16 | Lighthouse Best Practices ≥ 95 (Home) | Lighthouse | ☐ |
| 6.17 | Lighthouse SEO ≥ 95 (Home) | Lighthouse | ☐ |
| 6.18 | LCP < 2.5s (Home) | Lighthouse | ☐ |
| 6.19 | CLS < 0.1 (Home) | Lighthouse | ☐ |
| 6.20 | Total page weight < 500KB (Home) | DevTools (Network) | ☐ |

### 8.4 Accessibility

| # | Check | Method | Status |
|---|-------|--------|:---:|
| 6.21 | Skip link works (Tab on load) | Manual | ☐ |
| 6.22 | All interactive elements reachable via Tab | Manual | ☐ |
| 6.23 | Focus ring visible on all interactive elements | Manual | ☐ |
| 6.24 | All images have `alt` | Visual (code) | ☐ |
| 6.25 | All form inputs have `<label>` | Visual (code) | ☐ |
| 6.26 | Color contrast ≥ 4.5:1 (body text) | Lighthouse | ☐ |
| 6.27 | `prefers-reduced-motion` respected | Manual (OS setting) | ☐ |

### 8.5 Documentation

| # | Check | Method | Status |
|---|-------|--------|:---:|
| 6.28 | `README.md` exists | Visual | ☐ |
| 6.29 | `README.md` has project description | Visual | ☐ |
| 6.30 | `README.md` has setup instructions | Visual | ☐ |
| 6.31 | `README.md` has live URL | Visual | ☐ |
| 6.32 | `README.md` links to `docs/` | Visual | ☐ |
| 6.33 | `docs/README.md` exists (docs index) | Visual | ☐ |
| 6.34 | All 8 docs in `docs/` present | Visual | ☐ |

### 8.6 Final Deploy

| # | Check | Method | Status |
|---|-------|--------|:---:|
| 6.35 | Push to `main` triggers Action | Visual | ☐ |
| 6.36 | Action completes with green check | Visual | ☐ |
| 6.37 | Live site shows Home page | Visual | ☐ |
| 6.38 | All 9 pages accessible on live site | Manual | ☐ |
| 6.39 | 404 page works on live site | Manual | ☐ |
| 6.40 | Dark mode works on live site | Manual | ☐ |
| 6.41 | Mobile responsive on live site | Manual | ☐ |

**Phase 6 Summary:** ☐ / 41 checks

---

## 9. Overall Summary

| Phase | Name | Total Checks | Passed | Failed | Status |
|-------|------|:---:|:---:|:---:|:---:|
| 1 | Fondasi Proyek | 46 | ☐ | ☐ | ☐ |
| 2 | Desain & Home | 39 | ☐ | ☐ | ☐ |
| 3 | Halaman Statis | 35 | ☐ | ☐ | ☐ |
| 4 | Katalog + Filter | 29 | ☐ | ☐ | ☐ |
| 5 | Blog + Detail | 39 | ☐ | ☐ | ☐ |
| 6 | Polish & Deploy | 41 | ☐ | ☐ | ☐ |
| **TOTAL** | | **229** | ☐ | ☐ | ☐ |

---

## 10. Quick Verification Commands

```bash
# Phase 1 — Local dev
npm run dev
# Open http://localhost:4321

# Phase 1 — Build
npm run build
# Check dist/ folder exists

# Phase 1 — Check deploy
git push
# Open GitHub Actions tab

# Phase 1 — Check dark mode CSS variables
grep -n "prefers-color-scheme" src/styles/global.css

# Phase 1 — Check no manual dark: variants (except prose-invert)
grep -rn "dark:" src/components/ src/pages/ src/layouts/ | grep -v "prose-invert"

# Phase 2–5 — Test responsive
# Open DevTools → Toggle device toolbar → test 320/768/1024px

# Phase 2–5 — Test dark mode
# Change OS theme to dark, refresh page

# Phase 4 — Test filter (with temp data)
# Add temp project, run npm run dev, test filter manually

# Phase 5 — Test dynamic routes (with temp content)
# Add temp article/project, visit /blog/[slug] or /katalog/[slug]

# Phase 6 — Lighthouse
# Open DevTools → Lighthouse → Analyze page load

# Phase 6 — Check sitemap
# Visit /sitemap-index.xml

# Phase 6 — Check robots
# Visit /robots.txt

# Phase 6 — Check all routes
# Visit each: /, /about, /skills, /katalog, /services, /blog, /resources, /testimonials, /contact, /404
```
---

*End of document.*