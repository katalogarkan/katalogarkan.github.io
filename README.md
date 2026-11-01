# katalogarkan

## Personal Branding Website & Project Katalog with Astro, Tailwind CSS, and React

[![Status](https://img.shields.io/badge/status-production-brightgreen)](https://github.com/katalogarkan/katalogarkan.github.io)
[![Astro](https://img.shields.io/badge/Astro-5.x-BC52EE)](https://astro.build/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind-4.x-06B6D4)](https://tailwindcss.com/)
[![React](https://img.shields.io/badge/React-19.x-61DAFB)](https://react.dev/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.x-3178C6)](https://www.typescriptlang.org/)
[![GitHub Pages](https://img.shields.io/badge/Deploy-GitHub%20Pages-222222)](https://katalogarkan.github.io)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Live Site](https://img.shields.io/badge/Live%20Site-katalogarkan.github.io-0969da)](https://katalogarkan.github.io)
[![Verification](https://img.shields.io/badge/Verification-229%2F229%20passed-brightgreen)](docs/verification-checklist.md)

---

## Project Overview

katalogarkan is a personal branding website and project katalog for Arkan, a Full Stack Web Developer. The website introduces who Arkan is and showcases projects he has built in a filterable, searchable katalog. Built with Astro for static generation, Tailwind CSS for styling, and React for the katalog filter island. Content is written in Markdown files stored in the repository — no database, no CMS, no server.

### Key Highlights

- **12 Routes** — 9 static pages + 2 dynamic detail routes + 1 custom 404
- **Filterable Katalog** — category filter, search, sort (React island)
- **Blog** — Markdown-based articles with prose styling
- **Dark Mode** — follows OS preference via CSS variables (no toggle, no JS)
- **Responsive** — 320px to 2560px, mobile-first
- **SEO-Ready** — sitemap, robots.txt, Open Graph, canonical URLs
- **Lighthouse 100/100** in all 4 categories
- **Zero Hosting Cost** — GitHub Pages free tier

### Quick Stats

| Metric | Value |
|--------|-------|
| Static Pages | 9 |
| Dynamic Routes | 2 |
| Error Pages | 1 |
| Components | 8 |
| Verification Checks | 229 / 229 ✅ |
| Lighthouse Score | 100 / 100 / 100 / 100 |
| Hosting Cost | $0 |

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
| Services | https://katalogarkan.github.io/services |
| Blog | https://katalogarkan.github.io/blog |
| Resources | https://katalogarkan.github.io/resources |
| Testimonials | https://katalogarkan.github.io/testimonials |
| Contact | https://katalogarkan.github.io/contact |

---

## Technology Stack

| Layer | Technology | Version |
|-------|------------|---------|
| Framework | Astro | 5.x |
| Styling | Tailwind CSS | 4.x |
| Content | Astro Content Collections | built-in |
| Interactivity | React (island) | 19.x |
| Language | TypeScript | 5.x |
| Typography | `@tailwindcss/typography` | latest |
| Hosting | GitHub Pages | — |
| CI/CD | GitHub Actions | — |
| Node | Node.js | 20+ |

---

## System Architecture

### Page Structure

![Page Structure](screenshots/page-structure.png)

**Description:** This diagram shows the high-level page layout used across the entire website. Every page shares a common shell: a sticky header at the top containing the site logo ("Arkan") and 9 navigation links (Home, About, Skills, Katalog, Services, Blog, Resources, Testimonials, Contact). Below the header is the page content area, which varies per route (see §7 Site Features). At the bottom is a 4-column footer containing the name and tagline, quick links, social links, and copyright. On mobile viewports (< 768px), the navigation collapses into a hamburger menu that expands vertically when tapped. This consistent shell ensures visual stability and fast navigation across all 12 routes.

### Content Flow

![Content Flow Diagram](screenshots/content-flow.png)

**Description:** This diagram illustrates how content travels from the author's local environment to the visitor's browser. The flow has five stages: (1) The writer (Arkan) authors Markdown files in `src/content/katalog/` or `src/content/blog/`, with YAML frontmatter validated by Zod schemas in `src/content/config.ts`. (2) When the code is pushed to GitHub, a GitHub Actions workflow triggers an Astro build. (3) Astro reads every Markdown file, validates frontmatter against the Zod schema, and generates a static HTML page per entry using `getStaticPaths`. (4) The build output is packaged into `dist/` and uploaded as a GitHub Pages artifact. (5) The artifact is deployed to the GitHub Pages CDN, where visitors access it at `katalogarkan.github.io`. No server runtime is involved — every page is pre-rendered at build time.

### Dark Mode Architecture

![Dark Mode Architecture](screenshots/dark-mode-architecture.png)

**Description:** This diagram explains how dark mode is implemented without JavaScript or a manual toggle. The architecture relies entirely on CSS custom properties (variables). At the top level, `src/styles/global.css` defines all color tokens as CSS variables inside `:root` (e.g., `--color-bg: #ffffff`, `--color-text: #1f2328`). A media query `@media (prefers-color-scheme: dark)` overrides these same variables with dark values (e.g., `--color-bg: #0d1117`, `--color-text: #e6edf3`). The Tailwind config (`tailwind.config.mjs`) maps semantic utility classes like `bg-bg`, `text-text`, and `border-border` to `var(--color-*)` references. When the OS switches between light and dark mode, the CSS variables update automatically, and every component that uses token classes reflects the change instantly. There are zero `dark:` variant classes in the codebase (except `prose-invert` for typography), which keeps components clean and consistent.

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
| **Resources** | Template/snippet/tool grid |
| **Testimonials** | Client quote grid |
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
| Implementation | CSS variables in `global.css` |
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

# 2. Add frontmatter + body

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

### All 6 Phases Complete — 229/229 Checks Passed

| Phase | Name | Checks | Status |
|-------|------|--------|:---:|
| 1 | Project Foundation | 46 | ✅ |
| 2 | Design & Home | 39 | ✅ |
| 3 | Static Pages | 35 | ✅ |
| 4 | Katalog + Filter | 29 | ✅ |
| 5 | Blog + Detail | 39 | ✅ |
| 6 | Polish & Deploy | 41 | ✅ |
| **TOTAL** | **All Phases** | **229** | **✅** |

---

## Performance

### Lighthouse Results

| Category | Score |
|----------|:---:|
| Performance | 100 |
| Accessibility | 100 |
| Best Practices | 100 |
| SEO | 100 |

### Core Web Vitals

| Metric | Target | Actual | Status |
|--------|--------|--------|:---:|
| LCP | < 2.5s | ~1.2s | ✅ |
| CLS | < 0.1 | ~0.01 | ✅ |
| INP | < 200ms | ~50ms | ✅ |

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
| [docs/verification-checklist.md](docs/verification-checklist.md) | 229 checks across 6 phases |
| [docs/cheatsheets.md](docs/cheatsheets.md) | Quick reference for daily development |
| [docs/deployment-guide.md](docs/deployment-guide.md) | GitHub Pages deploy step-by-step |
| [docs/CHANGELOG.md](docs/CHANGELOG.md) | Version history — every change recorded |

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| `npm run dev` fails | Check Node 20+, run `npm install` |
| Build fails on CI | Check `deploy.yml` uses Node 20 |
| GitHub Pages 404 | Enable Pages in Settings → Pages → Source: GitHub Actions |
| Assets 404 | Check `site` in `astro.config.mjs` |
| Tailwind classes not applied | Check `content` paths in `tailwind.config.mjs` |
| `border-border` not working | Check `border: { DEFAULT: 'var(--color-border)' }` |
| Dark mode not working | Check CSS variables in `global.css` + `prefers-color-scheme` block |
| React island not hydrating | Check `client:load` directive |
| Content collection error | Check frontmatter against `config.ts` schema |
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
│   ├── components/                  # 8 components
│   ├── content/                     # Content Collections
│   ├── layouts/                     # Page layouts
│   ├── pages/                       # 12 routes
│   └── styles/
│
├── docs/                            # 8 documentation files
│
├── screenshots/                     # Architecture diagrams
│   ├── page-structure.png
│   ├── content-flow.png
│   └── dark-mode-architecture.png
│
├── astro.config.mjs
├── tailwind.config.mjs
├── package.json
├── tsconfig.json
├── LICENSE
├── .gitignore
└── .github/workflows/deploy.yml
```

---

## Quick Links

| Resource | URL |
|----------|-----|
| **Live Site** | https://katalogarkan.github.io |
| **Repository** | https://github.com/katalogarkan/katalogarkan.github.io |
| **Actions** | https://github.com/katalogarkan/katalogarkan.github.io/actions |
| **Pages Settings** | https://github.com/katalogarkan/katalogarkan.github.io/settings/pages |
| **Sitemap** | https://katalogarkan.github.io/sitemap-index.xml |
| **Robots** | https://katalogarkan.github.io/robots.txt |
| **Local Dev** | http://localhost:4321 |
| **Astro Docs** | https://docs.astro.build |
| **Tailwind Docs** | https://tailwindcss.com/docs |

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