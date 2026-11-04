# katalogarkan

## Personal Branding Website & Project Katalog with Astro, Tailwind CSS, and React

[![Status](https://img.shields.io/badge/status-phase%205%20complete-blue)](https://github.com/katalogarkan/katalogarkan.github.io)
[![Astro](https://img.shields.io/badge/Astro-5.x-BC52EE)](https://astro.build/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind-4.x-06B6D4)](https://tailwindcss.com/)
[![React](https://img.shields.io/badge/React-18.x-61DAFB)](https://react.dev/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.x-3178C6)](https://www.typescriptlang.org/)
[![Node](https://img.shields.io/badge/Node-22.x-339933)](https://nodejs.org/)
[![GitHub Pages](https://img.shields.io/badge/Deploy-GitHub%20Pages-222222)](https://katalogarkan.github.io)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Live Site](https://img.shields.io/badge/Live%20Site-katalogarkan.github.io-0969da)](https://katalogarkan.github.io)
[![Verification](https://img.shields.io/badge/Verification-132%2F173%20passed-yellow)](docs/verification-checklist.md)

---

## Project Overview

katalogarkan is a personal branding website and project katalog for Arkan, a Full Stack Web Developer. The website introduces who Arkan is and showcases projects he has built in a filterable, searchable katalog. Built with Astro for static generation, Tailwind CSS for styling, and React for the katalog filter island. Content is written in Markdown files stored in the repository — no database, no CMS, no server.

### Key Highlights

- **12 Routes** — 9 static pages + 2 dynamic detail routes + 1 custom 404
- **Filterable Katalog** — category filter, search, sort (React island)
- **Blog** — Markdown-based articles with prose styling
- **Dark Mode** — follows OS preference via CSS variables (no toggle, no JS)
- **Responsive** — 320px to 2560px, mobile-first
- **SEO-Ready** — sitemap, robots.txt, Open Graph, canonical URLs (Phase 6)
- **Lighthouse target** — ≥ 95 in all 4 categories (measured in Phase 6)
- **Zero Hosting Cost** — GitHub Pages free tier

### Quick Stats

| Metric | Value |
|--------|-------|
| Static Pages | 9 |
| Dynamic Routes | 2 |
| Error Pages | 1 |
| Components | 6 (+ 2 layouts) |
| Verification Checks | 132 / 173 (Phase 1–5 complete) |
| Lighthouse Score | Target ≥ 95 (not yet measured — Phase 6) |
| Hosting Cost | $0 |

> **Status:** Phase 5 complete (2026-11-04). Phase 6 (SEO, Lighthouse, final deploy) pending. 12 pages built, 0 errors, 0 warnings.

---

## Live Site

### [katalogarkan.github.io](https://katalogarkan.github.io)

Every push to `main` triggers automatic deploy via GitHub Actions.

| Page | URL |
|------|-----|
| Home | https://katalogarkan.github.io |
| About | https://katalogarkan.github.io/about |
| Skills | https://katalogarkan.github.io/skills |
| Katalog | https://katalogarkan.github.io/katalog |
| Katalog Detail | https://katalogarkan.github.io/katalog/{slug} |
| Services | https://katalogarkan.github.io/services |
| Blog | https://katalogarkan.github.io/blog |
| Blog Detail | https://katalogarkan.github.io/blog/{slug} |
| Resources | https://katalogarkan.github.io/resources |
| Testimonials | https://katalogarkan.github.io/testimonials |
| Contact | https://katalogarkan.github.io/contact |
| 404 | https://katalogarkan.github.io/404 |

---

## Technology Stack

| Layer | Technology | Version |
|-------|------------|---------|
| Framework | Astro | 5.x |
| Styling | Tailwind CSS | 4.x |
| Tailwind integration | `@tailwindcss/vite` | 4.x |
| Content | Astro Content Collections | built-in |
| Interactivity | React (island) | 18.x |
| Language | TypeScript | 5.x |
| Typography | `@tailwindcss/typography` | latest |
| Hosting | GitHub Pages | — |
| CI/CD | GitHub Actions | — |
| Node | Node.js | 22+ |

**Note:** Tailwind 4 uses CSS-first config via `@theme` in `src/styles/global.css`. There is **no `tailwind.config.mjs`** and **no `@astrojs/tailwind`** integration.

---

## System Architecture

### Page Structure

![Page Structure](screenshots/page-structure.png)

**Description:** This diagram shows the high-level page layout used across the entire website. Every page shares a common shell: a sticky header at the top containing the site logo ("Arkan") and 9 navigation links (Home, About, Skills, Katalog, Services, Blog, Resources, Testimonials, Contact). Below the header is the page content area, which varies per route. At the bottom is a 4-column footer containing the name and tagline, quick links, social links, and copyright. On mobile viewports (< 768px), the navigation collapses into a hamburger menu that expands vertically when tapped. This consistent shell ensures visual stability and fast navigation across all 12 routes.

### Content Flow

![Content Flow Diagram](screenshots/content-flow.png)

**Description:** This diagram illustrates how content travels from the author's local environment to the visitor's browser. The flow has five stages: (1) The writer (Arkan) authors Markdown files in `src/content/katalog/` or `src/content/blog/`, with YAML frontmatter validated by Zod schemas in `src/content.config.ts` (Astro 5 API). (2) When the code is pushed to GitHub, a GitHub Actions workflow triggers an Astro build. (3) Astro reads every Markdown file, validates frontmatter against the Zod schema, and generates a static HTML page per entry using `getStaticPaths`. (4) The build output is packaged into `dist/` and uploaded as a GitHub Pages artifact. (5) The artifact is deployed to the GitHub Pages CDN, where visitors access it at `katalogarkan.github.io`. No server runtime is involved — every page is pre-rendered at build time.

### Dark Mode Architecture

![Dark Mode Architecture](screenshots/dark-mode-architecture.png)

**Description:** This diagram explains how dark mode is implemented without JavaScript or a manual toggle. The architecture relies entirely on CSS custom properties (variables). At the top level, `src/styles/global.css` defines all color tokens as CSS variables inside the `@theme` block (e.g., `--color-bg: #ffffff`, `--color-text: #1f2328`). A media query `@media (prefers-color-scheme: dark)` overrides these same variables with dark values (e.g., `--color-bg: #0d1117`, `--color-text: #e6edf3`). Tailwind 4 auto-generates utility classes like `bg-bg`, `text-text`, and `border-border` from these `@theme` declarations, and those classes resolve to `var(--color-*)` references. When the OS switches between light and dark mode, the CSS variables update automatically, and every component that uses token classes reflects the change instantly. There are zero `dark:` variant classes in the codebase (except `prose-invert` for typography), which keeps components clean and consistent.

---

## Quick Start

```bash
# Clone repository
git clone https://github.com/katalogarkan/katalogarkan.github.io.git
cd katalogarkan.github.io

# Install dependencies
npm install

# Start dev server
npm run dev
# → http://localhost:4321

# Build for production
npm run build

# Preview production build
npm run preview
```

**Prerequisites:** Node.js 22+, npm 10+, Git 2.40+.

---

## Deployment

```bash
# 1. Verify local build
npm run build

# 2. Commit changes
git add .
git commit -m "feat: add new content"

# 3. Push to main (triggers auto-deploy)
git push origin main

# 4. Wait 1–2 minutes

# 5. Verify live
# https://katalogarkan.github.io

# 6. Check deploy status
# https://github.com/katalogarkan/katalogarkan.github.io/actions
```

---

## Site Features

### Pages

| Page | Features |
|------|----------|
| **Home** | Hero, featured projects, skills summary, testimonials, CTA |
| **About** | Bio, timeline, values, CV download, info |
| **Skills** | 4 categories (Frontend, Backend, Database, DevOps), skill bars |
| **Katalog** | Filter, search, sort (React island), grid layout |
| **Katalog Detail** | Title, date, category, tech badges, Markdown body, demo/repo links |
| **Services** | 3 packages, 4-step process, FAQ |
| **Blog** | Article list, category badges, tags |
| **Blog Detail** | Title, date, category, tags, Markdown prose body |
| **Resources** | Template/snippet/tool grid (empty state at launch) |
| **Testimonials** | Client quote grid (empty state at launch) |
| **Contact** | Formspree form + social links |
| **404** | Custom error page with back link |

### Katalog Filter

| Feature | Detail |
|---------|--------|
| Category filter | `web-app` / `landing-page` / `api` / `mobile` |
| Search | By title and tech stack |
| Sort | By date (newest / oldest) |
| Hydration | React island (`client:load`) |
| JS budget | < 50KB gzipped ✅ |

### Dark Mode

| Property | Value |
|----------|-------|
| Strategy | `prefers-color-scheme` (OS preference) |
| Implementation | CSS variables in `global.css` (`@theme` + media query) |
| Toggle | None |
| JavaScript | None required |
| Components | Zero `dark:` variants (except `prose-invert`) |

### Contact Form

| Property | Value |
|----------|-------|
| Backend | Formspree |
| Fields | Name, Email, Subject, Message |
| Spam protection | Honeypot field + Formspree filter |
| Fallback | `mailto:` link |

---

## Content Management

Content is written in Markdown — no CMS, no database.

### Add New Project

```bash
# 1. Create file
touch src/content/katalog/my-project.md

# 2. Add frontmatter + body (see docs/content-guide.md §3)

# 3. Add thumbnail
# Place at public/images/projects/my-project.png

# 4. Preview
npm run dev
# Open http://localhost:4321/katalog

# 5. Validate
npm run build

# 6. Commit + push
git add . && git commit -m "content: add my-project" && git push
```

### Add New Article

```bash
# 1. Create file
touch src/content/blog/my-article.md

# 2. Add frontmatter with draft: true

# 3. Write body

# 4. Preview
npm run dev
# Open http://localhost:4321/blog

# 5. When ready, set draft: false

# 6. Validate + deploy
npm run build
git add . && git commit -m "content: add my-article" && git push
```

---

## Verification

### Phase 1–5 Complete — Phase 6 Pending

| Phase | Name | Auto Checks | Status | Date |
|-------|------|:---:|:---:|------|
| 1 | Project Foundation | 57/57 | ✅ Complete | 2026-11-01 |
| 2 | Design & Home | 30/30 | ✅ Complete | 2026-11-04 |
| 3 | Static Pages | 18/18 | ✅ Complete | 2026-11-04 |
| 4 | Katalog + Filter | 9/9 | ✅ Complete | 2026-11-04 |
| 5 | Blog + Detail | 18/18 | ✅ Complete | 2026-11-04 |
| 6 | Polish & Deploy | 0/41 | ⏳ Not started | — |
| **TOTAL** | **All Phases** | **132/173** | **76% complete** | — |

> **Note:** 236 total verification points are documented in `docs/verification-checklist.md`. Phase completion is recorded using automated check counts (`CHANGELOG.md`). Both figures are correct for their contexts — see `verification-checklist.md` §10.1.

---

## Performance

### Lighthouse Results

| Category | Target | Status |
|----------|:---:|:---:|
| Performance | ≥ 95 | ⏳ Not yet measured (Phase 6) |
| Accessibility | ≥ 95 | ⏳ Not yet measured (Phase 6) |
| Best Practices | ≥ 95 | ⏳ Not yet measured (Phase 6) |
| SEO | ≥ 95 | ⏳ Not yet measured (Phase 6) |

### Core Web Vitals

| Metric | Target | Status |
|--------|--------|:---:|
| LCP | < 2.5s | ⏳ Pending measurement |
| CLS | < 0.1 | ⏳ Pending measurement |
| INP | < 200ms | ⏳ Pending measurement |

---

## Quick Commands

```bash
# START DEV SERVER
npm run dev

# BUILD FOR PRODUCTION
npm run build

# PREVIEW PRODUCTION BUILD
npm run preview

# COUNT PROJECTS
ls src/content/katalog/ | wc -l

# COUNT ARTICLES
ls src/content/blog/ | wc -l

# FIND DRAFT ARTICLES
grep -l "draft: true" src/content/blog/*.md

# DEPLOY (auto via push)
git add . && git commit -m "feat: update" && git push

# TRIGGER DEPLOY (empty commit)
git commit --allow-empty -m "chore: trigger deploy" && git push
```

---

## Documentation

| File | Purpose |
|------|---------|
| [docs/README.md](docs/README.md) | Documentation index |
| [docs/blueprint.md](docs/blueprint.md) | Architecture, tech stack, 6 phases, decisions log |
| [docs/design-system.md](docs/design-system.md) | Colors, typography, spacing, components, dark mode |
| [docs/content-guide.md](docs/content-guide.md) | How to write katalog & blog content |
| [docs/verification-checklist.md](docs/verification-checklist.md) | 236 checks across 6 phases |
| [docs/cheatsheets.md](docs/cheatsheets.md) | Quick reference for daily development |
| [docs/deployment-guide.md](docs/deployment-guide.md) | GitHub Pages deploy step-by-step |
| [docs/demo-video.md](docs/demo-video.md) | Demo video script and production plan |
| [CHANGELOG.md](CHANGELOG.md) | Version history — every change recorded (root, single source of truth) |

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| `npm run dev` fails | Check Node 22+, run `npm install` |
| Build fails on CI | Check `deploy.yml` uses Node 22 |
| GitHub Pages 404 | Enable Pages in Settings → Pages → Source: GitHub Actions |
| Assets 404 | Check `site` in `astro.config.mjs` |
| Tailwind classes not applied | Check `@import "tailwindcss"` at top of `src/styles/global.css` |
| `@theme` tokens not working | Ensure `@theme` is before `@layer base` in `global.css` |
| `border-border` not working | Check `--color-border` in `@theme` |
| Dark mode not working | Check `@media (prefers-color-scheme: dark)` block in `global.css` |
| React island not hydrating | Check `client:load` directive on `<KatalogFilter />` |
| Content collection error | Check frontmatter against `src/content.config.ts` schema |
| Font not loading | Check Google Fonts link in `BaseLayout.astro` |

---

## Security

### Third-Party Services

| Service | Purpose | Data Shared |
|---------|---------|-------------|
| GitHub Pages | Hosting | None (static) |
| Formspree | Contact form | Name, email, message |
| Google Fonts | Inter font | IP address (standard) |

### Best Practices

1. No secrets in repository
2. `npm audit` before each phase
3. External links use `rel="noopener noreferrer"`
4. Formspree honeypot field for spam
5. HTTPS enforced by GitHub Pages

---

## Project Structure

```
katalogarkan.github.io/
│
├── public/                          # Static assets
│   ├── favicon.svg
│   ├── robots.txt
│   ├── cv.pdf
│   └── images/
│       ├── projects/
│       ├── blog/
│       ├── avatar.png
│       └── og-default.png
│
├── src/
│   ├── components/                  # 6 components + 1 React island
│   │   ├── Header.astro
│   │   ├── Footer.astro
│   │   ├── ProjectCard.astro
│   │   ├── BlogCard.astro
│   │   ├── SkillBadge.astro
│   │   └── KatalogFilter.tsx
│   ├── content/                     # Content Collections
│   │   ├── katalog/
│   │   └── blog/
│   ├── content.config.ts            # Zod schemas (Astro 5 API)
│   ├── layouts/                     # 2 layouts
│   │   ├── BaseLayout.astro
│   │   └── PostLayout.astro
│   ├── pages/                       # 12 routes
│   └── styles/
│       └── global.css               # @import + @theme + dark mode
│
├── docs/                            # 8 documentation files
│
├── screenshots/                     # Architecture diagrams
│   ├── page-structure.png
│   ├── content-flow.png
│   └── dark-mode-architecture.png
│
├── astro.config.mjs
├── package.json
├── package-lock.json
├── tsconfig.json
├── CHANGELOG.md                     # Single source of truth
├── LICENSE
├── .gitignore
└── .github/workflows/deploy.yml
```

**Notes:**
- No `tailwind.config.mjs` — Tailwind 4 config lives in `src/styles/global.css` via `@theme`.
- Content config at `src/content.config.ts` (Astro 5 API).
- Single `CHANGELOG.md` at root.

---

## Quick Links

| Resource | URL |
|----------|-----|
| **Live Site** | https://katalogarkan.github.io |
| **Repository** | https://github.com/katalogarkan/katalogarkan.github.io |
| **Actions** | https://github.com/katalogarkan/katalogarkan.github.io/actions |
| **Pages Settings** | https://github.com/katalogarkan/katalogarkan.github.io/settings/pages |
| **Sitemap** | https://katalogarkan.github.io/sitemap-index.xml (Phase 6) |
| **Robots** | https://katalogarkan.github.io/robots.txt (Phase 6) |
| **Local Dev** | http://localhost:4321 |
| **Astro Docs** | https://docs.astro.build |
| **Tailwind Docs** | https://tailwindcss.com/docs |
| **Tailwind Theme** | https://tailwindcss.com/docs/theme |

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact

- **Project Maintainer**: Arkan
- **GitHub**: https://github.com/katalogarkan
- **Website**: https://katalogarkan.github.io
- **LinkedIn**: (add when ready)
- **Email**: (add when ready)

---

Built by Arkan | Full Stack Web Developer