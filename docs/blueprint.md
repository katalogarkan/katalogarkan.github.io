# katalogarkan — blueprint.md

---

## Document Information

| Property | Value |
|----------|-------|
| Document Version | 1.3.0 |
| Project Version | 0.5.0 (Phase 5 Complete) |
| Last Updated | 2026-11-04 |
| Status | Approved — Source of Truth |
| Project | Personal branding & katalog website |
| Owner | Arkan (Full Stack Web Developer) |
| Repository | `katalogarkan/katalogarkan.github.io` |
| Live URL | https://katalogarkan.github.io |
| Framework | Astro 5 |
| Styling | Tailwind CSS 4 |
| Hosting | GitHub Pages |
| Total Static Pages | 9 |
| Total Dynamic Routes | 2 |
| Total Error Pages | 1 |
| Total Components | 6 |
| Total Layouts | 2 |
| Total Phases | 6 |
| UI Language | English |
| Content Language | English |

---

## Table of Contents

1. [Project Overview](#1-project-overview)
2. [Goals & Non-Goals](#2-goals--non-goals)
3. [Assumptions & Constraints](#3-assumptions--constraints)
4. [Tech Stack](#4-tech-stack)
5. [Design Tokens](#5-design-tokens)
6. [Site Map & Pages](#6-site-map--pages)
7. [Page Content Spec](#7-page-content-spec)
8. [Component Specs](#8-component-specs)
9. [Content Schema](#9-content-schema)
10. [Project Structure](#10-project-structure)
11. [Routing & Rendering](#11-routing--rendering)
12. [Interactivity](#12-interactivity)
13. [SEO & Metadata](#13-seo--metadata)
14. [Accessibility](#14-accessibility)
15. [Performance](#15-performance)
16. [Error Handling](#16-error-handling)
17. [Git Workflow](#17-git-workflow)
18. [Deployment](#18-deployment)
19. [Security](#19-security)
20. [Execution Phases](#20-execution-phases)
21. [Acceptance Criteria](#21-acceptance-criteria)
22. [Troubleshooting](#22-troubleshooting)
23. [Decisions Log](#23-decisions-log)
24. [Open Questions](#24-open-questions)
25. [Glossary](#25-glossary)
26. [References](#26-references)
27. [Change Log](#27-change-log)

---

## 1. Project Overview

### 1.1 What This Project Is

A personal branding website for Arkan, a Full Stack Web Developer. The website serves two purposes:

1. **Personal branding** — introduces who Arkan is, what he does, and why someone should work with him.
2. **Project katalog** — showcases projects he has built, filterable and searchable.

The website is built with Astro (static site generator), styled with Tailwind CSS, and hosted for free on GitHub Pages. Content (projects and blog articles) is written in Markdown files stored in the repository — no database, no CMS, no server.

### 1.2 Why This Project Exists

| Problem | Solution |
|---------|----------|
| No central place to showcase work | 9-page website with katalog |
| Recruiters/clients can't find projects | Filterable katalog with detail pages |
| No long-term content platform | Blog with Markdown-based articles |
| Free hosting required | GitHub Pages (zero cost) |
| Must last 1+ year without redesign | Astro + Content Collections (maintainable) |

### 1.3 What the Website Looks Like (High Level)

```
┌─────────────────────────────────────────────────────┐
│  HEADER: Arkan · Home About Skills Katalog ...      │
├─────────────────────────────────────────────────────┤
│                                                     │
│  PAGE CONTENT                                       │
│  (varies per page — see §7)                         │
│                                                     │
├─────────────────────────────────────────────────────┤
│  FOOTER: Name · Links · Social · Copyright          │
└─────────────────────────────────────────────────────┘
```

### 1.4 What the Website Does NOT Do

- No login or user accounts
- No payment or e-commerce
- No real-time features
- No database
- No admin dashboard
- No mobile app
- No multi-language at launch
- No CMS at launch

### 1.5 How Content Works

```
Writer (Arkan)
    │
    ▼
Markdown file in src/content/katalog/ or src/content/blog/
    │
    ▼
Astro reads file, validates against schema (content.config.ts)
    │
    ▼
Astro generates static HTML page at build time
    │
    ▼
GitHub Actions deploys to GitHub Pages
    │
    ▼
Visitor sees page at katalogarkan.github.io
```

Adding a new project = create one `.md` file, commit, push. GitHub Actions rebuilds and deploys automatically.

---

## 2. Goals & Non-Goals

### 2.1 Goals

| # | Goal | How We Measure |
|---|------|----------------|
| 1 | Personal branding for full stack web developer | Home + About + Skills pages live and complete |
| 2 | Showcase projects in a filterable katalog | Katalog page with filter, search, sort working |
| 3 | Publish articles via Markdown | Blog page with at least 1 article rendering |
| 4 | Maintainable for 1+ year without redesign | Content Collections + reusable components |
| 5 | Fast, SEO-friendly, responsive, accessible | Lighthouse ≥ 95 in all 4 categories |
| 6 | Zero hosting cost | GitHub Pages free tier only |

### 2.2 Non-Goals

| # | Non-Goal | Why Not |
|---|----------|---------|
| 1 | E-commerce or payment | Not a store |
| 2 | User accounts or login | Static site, no server |
| 3 | Real-time features | Static site |
| 4 | Mobile app | Web only |
| 5 | Multi-language (i18n) at launch | Adds complexity; can add later |
| 6 | CMS at launch | Markdown in repo is sufficient |
| 7 | Admin dashboard | No server, no auth |
| 8 | Analytics | Privacy — skipped at launch |

---

## 3. Assumptions & Constraints

### 3.1 Assumptions

| # | Assumption |
|---|-----------|
| 1 | Owner has Node.js 22+ installed locally |
| 2 | Owner has Git installed and configured |
| 3 | Owner has GitHub account `katalogarkan` |
| 4 | Owner writes content in Markdown |
| 5 | Owner has basic Astro knowledge (or willing to learn) |
| 6 | Repository `katalogarkan.github.io` exists (already created) |
| 7 | GitHub Pages enabled for the repository |
| 8 | Owner works on Windows, macOS, or Linux |

### 3.2 Constraints

| # | Constraint | Impact |
|---|-----------|--------|
| 1 | Static hosting only — no server runtime | No API routes, no SSR, no database |
| 2 | No database | Content stored as Markdown files |
| 3 | No authentication | No private pages |
| 4 | Content via files in repository | Adding content = commit + push |
| 5 | Build output must be `dist/` | Astro default |
| 6 | Node version pinned to 22 in CI | GitHub Actions workflow |
| 7 | Repository name fixed: `katalogarkan.github.io` | Cannot rename without breaking URL |
| 8 | All content in English | No i18n at launch |

---

## 4. Tech Stack

### 4.1 Core Stack

| Layer | Technology | Version | Why |
|-------|-----------|---------|-----|
| Framework | Astro | 5.x | Content-driven, minimal JS, built for static sites |
| Styling | Tailwind CSS | 4.x | Utility-first, CSS-first config via `@theme` |
| Tailwind integration | `@tailwindcss/vite` | 4.x | Native Vite plugin (no `tailwind.config.mjs`) |
| Content | Astro Content Collections | built-in | Typed Markdown with Zod validation |
| Interactivity | React (island) | 18.x | Katalog filter needs client state |
| Language | TypeScript | 5.x | Type safety |
| Typography | `@tailwindcss/typography` | latest | Prose styling for Markdown |
| Hosting | GitHub Pages | — | Free, repo already exists |
| CI/CD | GitHub Actions | — | Auto-deploy on push |

### 4.2 Dependencies

| Package | Purpose |
|---------|---------|
| `astro` | Framework |
| `@tailwindcss/vite` | Tailwind 4 Vite plugin |
| `@astrojs/react` | React island integration |
| `@astrojs/sitemap` | Auto-generate sitemap |
| `react` | React runtime |
| `react-dom` | React DOM |
| `tailwindcss` | Utility CSS |
| `@tailwindcss/typography` | Markdown prose styling |

### 4.3 Not Used (and Why)

| Technology | Why Not |
|-----------|---------|
| Next.js | Overkill for content site; heavier JS |
| Vue / Svelte | React chosen for filter island |
| CMS (Sanity, Contentful) | Content via Markdown in repo is simpler |
| Database | Static site — no server |
| Server runtime | GitHub Pages limitation |
| Analytics | Privacy — skipped at launch |
| CSS-in-JS | Tailwind is simpler for this scale |
| `@astrojs/tailwind` | Superseded by `@tailwindcss/vite` for Tailwind 4 |
| `tailwind.config.mjs` | Tailwind 4 uses CSS-first `@theme` config |

---

## 5. Design Tokens

### 5.1 Color Palette

| Token | Light Mode | Dark Mode | CSS Variable | Usage |
|-------|-----------|-----------|--------------|-------|
| `primary` | `#0969da` | `#58a6ff` | `--color-primary` | Links, buttons, accents |
| `primary-hover` | `#0550ae` | `#79c0ff` | `--color-primary-hover` | Hover states |
| `bg` | `#ffffff` | `#0d1117` | `--color-bg` | Page background |
| `bg-subtle` | `#f6f8fa` | `#161b22` | `--color-bg-subtle` | Card background |
| `text` | `#1f2328` | `#e6edf3` | `--color-text` | Body text |
| `text-muted` | `#656d76` | `#8b949e` | `--color-text-muted` | Secondary text |
| `border` | `#d0d7de` | `#30363d` | `--color-border` | Borders |
| `success` | `#1a7f37` | `#3fb950` | `--color-success` | Success states |
| `warning` | `#9a6700` | `#d29922` | `--color-warning` | Warning states |
| `danger` | `#cf222e` | `#f85149` | `--color-danger` | Error states |

### 5.2 Typography

| Token | Value |
|-------|-------|
| Font family | Inter |
| Font source | Google Fonts |
| Base size | 16px |
| Line height (body) | 1.6 |
| Line height (heading) | 1.2 |
| Heading weight | 700 |
| Body weight | 400 |
| Code font | `ui-monospace, SFMono-Regular, Menlo, monospace` |

### 5.3 Type Scale

| Token | Size | Usage |
|-------|------|-------|
| `text-xs` | 12px | Badges, labels |
| `text-sm` | 14px | Secondary text |
| `text-base` | 16px | Body |
| `text-lg` | 18px | Lead paragraph |
| `text-xl` | 20px | H3 |
| `text-2xl` | 24px | H2 |
| `text-4xl` | 36px | H1 |
| `text-6xl` | 60px | Hero |

### 5.4 Spacing

| Token | Value |
|-------|-------|
| `space-xs` | 4px |
| `space-sm` | 8px |
| `space-md` | 16px |
| `space-lg` | 24px |
| `space-xl` | 32px |
| `space-2xl` | 48px |
| `space-3xl` | 64px |

### 5.5 Border Radius

| Token | Value |
|-------|-------|
| `radius-sm` | 4px |
| `radius-md` | 8px |
| `radius-lg` | 12px |
| `radius-full` | 9999px |

### 5.6 Shadow

| Token | Value |
|-------|-------|
| `shadow-sm` | `0 1px 2px rgba(0,0,0,0.05)` |
| `shadow-md` | `0 4px 6px rgba(0,0,0,0.1)` |
| `shadow-lg` | `0 10px 15px rgba(0,0,0,0.1)` |

### 5.7 Breakpoints

| Token | Value | Target |
|-------|-------|--------|
| `sm` | 640px | Large phone |
| `md` | 768px | Tablet |
| `lg` | 1024px | Small laptop |
| `xl` | 1280px | Desktop |
| `2xl` | 1536px | Large desktop |

### 5.8 Dark Mode

| Property | Value |
|----------|-------|
| Strategy | `prefers-color-scheme` (OS preference) |
| Manual toggle | No |
| Persistence | N/A |
| Implementation | CSS variables overridden in `@media (prefers-color-scheme: dark)` in `global.css` |
| Default | Light (if OS has no preference) |

### 5.9 Tailwind Config (Single Source of Truth — Tailwind 4)

Tailwind 4 uses **CSS-first configuration** via the `@theme` directive. There is **no `tailwind.config.mjs`**.

```css
/* src/styles/global.css */
@import "tailwindcss";
@plugin "@tailwindcss/typography";

@theme {
  --color-primary: #0969da;
  --color-primary-hover: #0550ae;
  --color-bg: #ffffff;
  --color-bg-subtle: #f6f8fa;
  --color-text: #1f2328;
  --color-text-muted: #656d76;
  --color-border: #d0d7de;
  --color-success: #1a7f37;
  --color-warning: #9a6700;
  --color-danger: #cf222e;

  --font-sans: "Inter", system-ui, -apple-system, sans-serif;
  --font-mono: ui-monospace, SFMono-Regular, Menlo, monospace;

  --container-prose: 65ch;
}
```

**Rule:** All color tokens are declared in `@theme`. Tailwind 4 auto-generates utility classes (`bg-primary`, `text-text-muted`, `border-border`, etc.) from these variables.

### 5.10 Dark Mode Overrides (Global CSS)

```css
/* src/styles/global.css — continued after @theme block */
@layer base {
  :root {
    color-scheme: light dark;
  }

  @media (prefers-color-scheme: dark) {
    :root {
      --color-primary: #58a6ff;
      --color-primary-hover: #79c0ff;
      --color-bg: #0d1117;
      --color-bg-subtle: #161b22;
      --color-text: #e6edf3;
      --color-text-muted: #8b949e;
      --color-border: #30363d;
      --color-success: #3fb950;
      --color-warning: #d29922;
      --color-danger: #f85149;
    }
  }

  html {
    scroll-behavior: smooth;
  }

  body {
    background-color: var(--color-bg);
    color: var(--color-text);
    font-family: var(--font-sans);
    -webkit-font-smoothing: antialiased;
  }

  @media (prefers-reduced-motion: reduce) {
    * {
      animation-duration: 0.01ms !important;
      transition-duration: 0.01ms !important;
    }
  }
}

@layer components {
  .container-page {
    max-width: 72rem;
    margin-inline: auto;
    padding-inline: 1rem;
  }
  @media (min-width: 768px) {
    .container-page {
      padding-inline: 2rem;
    }
  }
}
```

**Rule:** Light mode uses `@theme` values in `global.css`. Dark mode overrides the same CSS variables in `@media (prefers-color-scheme: dark)`. Single source of truth: `src/styles/global.css`.

---

## 6. Site Map & Pages

### 6.1 Complete Page List

| # | Route | File | Type | Purpose |
|---|-------|------|------|---------|
| 1 | `/` | `src/pages/index.astro` | Static | Home — hero, highlights, CTA |
| 2 | `/about` | `src/pages/about.astro` | Static | Bio, timeline, CV |
| 3 | `/skills` | `src/pages/skills.astro` | Static | Skill categories with levels |
| 4 | `/katalog` | `src/pages/katalog.astro` | Static + React island | Project grid with filter |
| 5 | `/katalog/[slug]` | `src/pages/katalog/[slug].astro` | Dynamic (SSG) | Project detail |
| 6 | `/services` | `src/pages/services.astro` | Static | Service packages |
| 7 | `/blog` | `src/pages/blog.astro` | Static | Article list |
| 8 | `/blog/[slug]` | `src/pages/blog/[slug].astro` | Dynamic (SSG) | Article detail |
| 9 | `/resources` | `src/pages/resources.astro` | Static | Templates, snippets, tools |
| 10 | `/testimonials` | `src/pages/testimonials.astro` | Static | Client testimonials |
| 11 | `/contact` | `src/pages/contact.astro` | Static | Contact form + social links |
| 12 | `/404` | `src/pages/404.astro` | Static | Custom 404 page |

**Total: 12 routes** (9 static + 2 dynamic + 1 error)

### 6.2 Navigation Structure

**Desktop navbar (left to right):**

```
Arkan | Home · About · Skills · Katalog · Services · Blog · Resources · Testimonials · Contact
```

**Mobile navbar:**

```
Arkan | ☰ (hamburger)
```

Hamburger opens a vertical menu with the same 9 links.

### 6.3 Footer Structure

| Column | Content |
|--------|---------|
| 1 | Name + tagline |
| 2 | Quick links: Home, About, Katalog, Contact |
| 3 | Social: GitHub, LinkedIn, Email |
| 4 | Copyright + version |

---

## 7. Page Content Spec

### 7.1 Home (`/`)

**Purpose:** First impression — who Arkan is, what he does, why work with him.

| Section | Content | Component | Empty State |
|---------|---------|-----------|-------------|
| Hero | Name, tagline, 2 CTA buttons (`View Katalog`, `Contact Me`) | Inline | — |
| Featured projects | 3 project cards where `featured: true` | `ProjectCard` | Hide section if none |
| Skills summary | Tech badges (top 8 skills) | `SkillBadge` | Hide if none |
| Testimonials | 2–3 quotes | Inline | Hide if none |
| CTA | "Interested in working together? Contact me" + button | Inline | — |

### 7.2 About (`/about`)

**Purpose:** Build trust — who is Arkan, background, values.

| Section | Content |
|---------|---------|
| Bio | Photo + 2–3 paragraphs |
| Timeline | Vertical list (year → event) |
| Values | 3 cards: Clean code, Clear communication, On time |
| CV download | PDF link (if available) |
| Info | Location, languages, availability |

### 7.3 Skills (`/skills`)

**Purpose:** Show technical depth visually.

| Section | Content |
|---------|---------|
| Categories | Frontend, Backend, Database, DevOps & Tools |
| Skill bars | Per skill: name + level (%) |
| Certifications | Optional list |

**Skill categories (planned):**

| Category | Skills |
|----------|--------|
| Frontend | HTML, CSS, JavaScript, React, Tailwind, Astro |
| Backend | Node.js, PHP, Laravel, Express |
| Database | MySQL, PostgreSQL, MongoDB |
| DevOps & Tools | Git, GitHub, Docker, Linux |

### 7.4 Katalog (`/katalog`)

**Purpose:** Showcase projects — the main attraction.

| Section | Content | Component |
|---------|---------|-----------|
| Header | Title + description | Inline |
| Filter bar | Category filter, search, sort | `KatalogFilter` (React) |
| Grid | Project cards | `ProjectCard` |

**Empty state:** "No projects yet — coming soon."

### 7.5 Katalog Detail (`/katalog/[slug]`)

**Purpose:** Full project case study.

| Section | Content |
|---------|---------|
| Header | Title, date, category, tech badges |
| Thumbnail | Full-width image |
| Body | Markdown content |
| Links | Demo + repo buttons |
| Back | Link to `/katalog` |

### 7.6 Services (`/services`)

**Purpose:** Offer services (if Arkan accepts clients).

| Section | Content |
|---------|---------|
| Packages | 3 cards: Landing Page, Web App, Custom |
| Process | 4 steps: Discuss → Design → Develop → Launch |
| FAQ | 3–4 questions |

### 7.7 Blog (`/blog`)

**Purpose:** SEO & thought leadership — proof of expertise.

| Section | Content | Component |
|---------|---------|-----------|
| Header | Title + description | Inline |
| List | Article cards | `BlogCard` |

**Empty state:** "No articles yet — coming soon."

### 7.8 Blog Detail (`/blog/[slug]`)

**Purpose:** Full article.

| Section | Content | Component |
|---------|---------|-----------|
| Header | Title, date, category, tags | `PostLayout` |
| Body | Markdown content (prose) | `PostLayout` |
| Back | Link to `/blog` | `PostLayout` |

### 7.9 Resources (`/resources`)

**Purpose:** Lead magnet — attract visitors with free assets.

| Section | Content |
|---------|---------|
| Grid | Resource cards: template, snippet, tool |
| Each card | Title, description, download/link button |

**Empty state:** "No resources yet — coming soon."

### 7.10 Testimonials (`/testimonials`)

**Purpose:** Social proof.

| Section | Content |
|---------|---------|
| Grid | Testimonial cards: quote, name, role, company |

**Empty state:** "No testimonials yet — coming soon."

### 7.11 Contact (`/contact`)

**Purpose:** Conversion — make it easy to reach Arkan.

| Section | Content |
|---------|---------|
| Form | Name, Email, Subject, Message + submit |
| Info | Email, GitHub, LinkedIn, WhatsApp |
| Response time | "Usually within 1×24 hours" |

### 7.12 404 (`/404`)

**Purpose:** Friendly error page.

| Section | Content |
|---------|---------|
| Heading | "404 — Page not found" |
| Message | "The page you're looking for doesn't exist." |
| CTA | "Back to Home" button |

---

## 8. Component Specs

### 8.1 Header

| Property | Value |
|----------|-------|
| File | `src/components/Header.astro` |
| Props | None |
| Content | Logo (name), nav links (9), hamburger (mobile) |
| Behavior | Sticky top, hamburger toggle on mobile |
| Script | Vanilla JS toggle (`<script>` in Astro) |
| Accessibility | `aria-label` on hamburger, `aria-expanded` state |

### 8.2 Footer

| Property | Value |
|----------|-------|
| File | `src/components/Footer.astro` |
| Props | None |
| Content | 4 columns (see §6.3) |

### 8.3 ProjectCard

| Property | Value |
|----------|-------|
| File | `src/components/ProjectCard.astro` |
| Props | `title`, `description`, `techStack`, `thumbnail`, `demoUrl`, `repoUrl`, `category`, `date`, `slug` |
| Content | Thumbnail, title, description, tech badges, demo/repo links |
| Link | Whole card → `/katalog/[slug]` |
| Hover | Slight lift (`shadow-md` → `shadow-lg`) |

### 8.4 BlogCard

| Property | Value |
|----------|-------|
| File | `src/components/BlogCard.astro` |
| Props | `title`, `date`, `description`, `category`, `tags`, `slug` |
| Content | Title, date, description, category badge, tags |
| Link | Whole card → `/blog/[slug]` |

### 8.5 SkillBadge

| Property | Value |
|----------|-------|
| File | `src/components/SkillBadge.astro` |
| Props | `name`, `level` (optional), `icon` (optional) |
| Content | Badge with name + optional level bar |

### 8.6 KatalogFilter (React Island)

| Property | Value |
|----------|-------|
| File | `src/components/KatalogFilter.tsx` |
| Props | `projects` (array) |
| Hydration | `client:load` |
| State | `category`, `search`, `sort` |
| Behavior | Filter by category, search by title/tech, sort by date |
| Output | Renders `<ProjectCard>` grid (client-side) |

### 8.7 BaseLayout

| Property | Value |
|----------|-------|
| File | `src/layouts/BaseLayout.astro` |
| Props | `title`, `description`, `ogImage` (optional) |
| Content | `<html>`, `<head>`, Header, `<slot />`, Footer |
| Includes | `global.css`, Inter font, meta tags |

### 8.8 PostLayout

| Property | Value |
|----------|-------|
| File | `src/layouts/PostLayout.astro` |
| Props | `frontmatter` (title, date, category, tags), `content` |
| Content | Article header, prose body, back link |
| Includes | `BaseLayout` + prose styles |

---

## 9. Content Schema

### 9.1 Collection: `katalog`

**Directory:** `src/content/katalog/`

| Field | Type | Required | Default | Description |
|-------|------|:---:|---------|-------------|
| `title` | string | Yes | — | Project title |
| `description` | string | Yes | — | Short description (1–2 lines) |
| `techStack` | string[] | Yes | — | Technologies used |
| `thumbnail` | string | Yes | — | Image path |
| `demoUrl` | string | No | — | Live demo URL |
| `repoUrl` | string | No | — | Repository URL |
| `category` | enum | Yes | — | `web-app` / `landing-page` / `api` / `mobile` |
| `featured` | boolean | No | `false` | Show on Home |
| `date` | date | Yes | — | Completion date |

### 9.2 Collection: `blog`

**Directory:** `src/content/blog/`

| Field | Type | Required | Default | Description |
|-------|------|:---:|---------|-------------|
| `title` | string | Yes | — | Article title |
| `date` | date | Yes | — | Publish date |
| `description` | string | Yes | — | Summary |
| `category` | enum | Yes | — | `tutorial` / `tips` / `notes` |
| `tags` | string[] | No | `[]` | Free-form tags |
| `draft` | boolean | No | `false` | Hide if true |
| `coverImage` | string | No | — | Cover image path |

### 9.3 Example Frontmatter — Katalog

```yaml
---
title: "Project Name"
description: "Short description of the project."
techStack: ["Astro", "Tailwind", "TypeScript"]
thumbnail: "/images/projects/project-name.png"
demoUrl: "https://example.com"
repoUrl: "https://github.com/katalogarkan/project-name"
category: "web-app"
featured: true
date: 2026-10-01
---
```

### 9.4 Example Frontmatter — Blog

```yaml
---
title: "Article Title"
date: 2026-10-01
description: "Short summary of the article."
category: "tutorial"
tags: ["astro", "tailwind"]
draft: false
coverImage: "/images/blog/article-title.png"
---
```

---

## 10. Project Structure

```
katalogarkan.github.io/
│
├── public/                          # Static assets (not processed)
│   ├── favicon.svg
│   ├── robots.txt
│   ├── cv.pdf                       # CV download (placeholder until ready)
│   └── images/
│       ├── projects/                # Project thumbnails
│       ├── blog/                    # Article cover images
│       ├── avatar.png               # Profile photo (placeholder)
│       └── og-default.png           # Open Graph image (1200×630)
│
├── src/
│   ├── components/                  # Reusable components
│   │   ├── Header.astro
│   │   ├── Footer.astro
│   │   ├── ProjectCard.astro
│   │   ├── BlogCard.astro
│   │   ├── SkillBadge.astro
│   │   └── KatalogFilter.tsx        # React island
│   │
│   ├── content/                     # Content Collections
│   │   ├── katalog/                 # Project Markdown files
│   │   └── blog/                    # Article Markdown files
│   │
│   ├── content.config.ts            # Zod schemas (Astro 5 API)
│   │
│   ├── layouts/                     # Page layouts
│   │   ├── BaseLayout.astro
│   │   └── PostLayout.astro
│   │
│   ├── pages/                       # Routes (auto-routing)
│   │   ├── index.astro              # /
│   │   ├── about.astro              # /about
│   │   ├── skills.astro             # /skills
│   │   ├── katalog.astro            # /katalog
│   │   ├── katalog/
│   │   │   └── [slug].astro         # /katalog/[slug]
│   │   ├── services.astro           # /services
│   │   ├── blog.astro               # /blog
│   │   ├── blog/
│   │   │   └── [slug].astro         # /blog/[slug]
│   │   ├── resources.astro          # /resources
│   │   ├── testimonials.astro       # /testimonials
│   │   ├── contact.astro            # /contact
│   │   └── 404.astro                # /404
│   │
│   └── styles/
│       └── global.css               # Tailwind 4 @import + @theme + dark mode
│
├── docs/                            # Documentation
│   ├── README.md                    # Docs index
│   ├── blueprint.md                 # This file
│   ├── design-system.md
│   ├── content-guide.md
│   ├── verification-checklist.md
│   ├── cheatsheets.md
│   ├── deployment-guide.md
│   └── demo-video.md
│
├── screenshots/                     # Architecture diagrams for README
│   ├── page-structure.png
│   ├── content-flow.png
│   └── dark-mode-architecture.png
│
├── astro.config.mjs                 # Astro config (integrations, site)
├── package.json                     # Dependencies + scripts
├── package-lock.json                # Locked dependencies
├── tsconfig.json                    # TypeScript config
├── CHANGELOG.md                     # Single source of truth for changes
├── LICENSE                          # MIT
├── .gitignore                       # Ignore node_modules, dist, .astro
└── .github/
    └── workflows/
        └── deploy.yml               # GitHub Pages deploy
```

**Notes:**
- No `tailwind.config.mjs` — Tailwind 4 config lives in `src/styles/global.css` via `@theme`.
- Content config lives at `src/content.config.ts` (Astro 5+ API), not `src/content/config.ts`.
- Single `CHANGELOG.md` at repository root (see §27).
- `docs/` contains planning & reference docs only.

---

## 11. Routing & Rendering

### 11.1 Route Table

| Route | Source | Rendering | Data Source |
|-------|--------|-----------|-------------|
| `/` | `index.astro` | Static | `katalog` (featured) |
| `/about` | `about.astro` | Static | None |
| `/skills` | `skills.astro` | Static | None |
| `/katalog` | `katalog.astro` + `KatalogFilter.tsx` | Static + React island | `katalog` (all) |
| `/katalog/[slug]` | `getStaticPaths` from `katalog` | Static (SSG) | `katalog` (one) |
| `/services` | `services.astro` | Static | None |
| `/blog` | `blog.astro` | Static | `blog` (all, not draft) |
| `/blog/[slug]` | `getStaticPaths` from `blog` | Static (SSG) | `blog` (one) |
| `/resources` | `resources.astro` | Static | None |
| `/testimonials` | `testimonials.astro` | Static | None |
| `/contact` | `contact.astro` | Static | None |
| `/404` | `404.astro` | Static | None |

### 11.2 Build Process

```
1. npm run build
   │
   ▼
2. Astro reads all pages + content collections
   │
   ▼
3. Validates frontmatter against content.config.ts (Zod)
   │
   ▼
4. Generates static HTML for each route
   │
   ▼
5. Bundles CSS (Tailwind 4 via @tailwindcss/vite) + minimal JS (React island)
   │
   ▼
6. Outputs to dist/
   │
   ▼
7. GitHub Actions uploads dist/ to GitHub Pages
```

### 11.3 Dynamic Route Generation

For `/katalog/[slug]`:

```js
export async function getStaticPaths() {
  const projects = await getCollection('katalog');
  return projects.map(project => ({
    params: { slug: project.id },
    props: { project },
  }));
}
```

Same pattern for `/blog/[slug]`.

---

## 12. Interactivity

### 12.1 Katalog Filter (React Island)

| Feature | Detail |
|---------|--------|
| Component | `KatalogFilter.tsx` |
| Hydration | `client:load` |
| Filter | By `category` (dropdown) |
| Search | By `title` and `techStack` (text input) |
| Sort | By `date` (newest / oldest) |
| State | Local (React `useState`) |
| Data source | Props from `katalog.astro` |
| Output | Renders `<ProjectCard>` grid client-side |

**Why React here?** Filter + search + sort requires client-side state. Astro alone can't do this without a full page reload.

**Why not React everywhere?** Only the filter needs interactivity. Everything else is static HTML — faster, simpler.

### 12.2 Dark Mode

| Feature | Detail |
|---------|--------|
| Strategy | CSS `prefers-color-scheme` |
| Toggle | None |
| JavaScript | None required |
| Implementation | CSS variables in `global.css` (see §5.10) |
| Default | Light (if OS has no preference) |

### 12.3 Mobile Menu

| Feature | Detail |
|---------|--------|
| Component | `Header.astro` |
| Behavior | Hamburger toggle |
| Implementation | Vanilla JS (`<script>` in Astro) |
| Accessibility | `aria-expanded`, `aria-controls` |

### 12.4 Contact Form

| Feature | Detail |
|---------|--------|
| Fields | Name, Email, Subject, Message |
| Validation | HTML5 + custom |
| Backend | Formspree |
| Fallback | `mailto:` link |
| Spam protection | Honeypot field |

---

## 13. SEO & Metadata

### 13.1 Per-Page Meta Tags

| Tag | Source | Example |
|-----|--------|---------|
| `<title>` | `{page title} — Arkan` | `Katalog — Arkan` |
| `<meta name="description">` | Page-specific | `Projects built by Arkan, full stack web developer.` |
| `<meta name="viewport">` | Fixed | `width=device-width, initial-scale=1` |
| `<link rel="canonical">` | `https://katalogarkan.github.io{path}` | `https://katalogarkan.github.io/katalog` |
| `<meta property="og:title">` | Page title | `Katalog — Arkan` |
| `<meta property="og:description">` | Page description | `Projects built by Arkan...` |
| `<meta property="og:image">` | `/images/og-default.png` | Full URL |
| `<meta property="og:url">` | Canonical URL | Full URL |
| `<meta property="og:type">` | `website` or `article` | `website` |
| `<meta name="twitter:card">` | `summary_large_image` | — |

### 13.2 Sitemap

| Property | Value |
|----------|-------|
| Generator | `@astrojs/sitemap` |
| Output | `/sitemap-index.xml` |
| Auto-included | All static + dynamic pages |

### 13.3 Robots

| Property | Value |
|----------|-------|
| File | `public/robots.txt` |
| Content | `User-agent: *` + `Allow: /` + `Sitemap: https://katalogarkan.github.io/sitemap-index.xml` |

### 13.4 OG Image

| Property | Value |
|----------|-------|
| File | `public/images/og-default.png` |
| Size | 1200×630 |
| Content | Name + tagline + primary color background |
| Per-page | Static (same image for all pages at launch) |

---

## 14. Accessibility

| # | Requirement | Implementation |
|---|-------------|----------------|
| 1 | Color contrast ≥ 4.5:1 | Verified via Tailwind palette |
| 2 | Focus visible | `focus-visible:ring-2` on all interactive |
| 3 | Semantic HTML | `<header>`, `<nav>`, `<main>`, `<footer>`, `<article>` |
| 4 | Alt text | All images have `alt` |
| 5 | Keyboard navigation | All interactive reachable via Tab |
| 6 | Skip link | "Skip to content" at top of `<body>` |
| 7 | ARIA labels | On icon-only buttons (hamburger) |
| 8 | Reduced motion | Respect `prefers-reduced-motion` |
| 9 | Form labels | Every input has `<label>` |
| 10 | Language | `<html lang="en">` |

---

## 15. Performance

### 15.1 Targets

| Metric | Target |
|--------|--------|
| Lighthouse Performance | ≥ 95 |
| Lighthouse Accessibility | ≥ 95 |
| Lighthouse Best Practices | ≥ 95 |
| Lighthouse SEO | ≥ 95 |
| LCP | < 2.5s |
| CLS | < 0.1 |
| INP | < 200ms |

### 15.2 Budget

| Asset | Budget |
|-------|--------|
| Total JS (Katalog page) | < 50KB gzipped |
| Total JS (other pages) | < 10KB gzipped |
| Total CSS | < 20KB gzipped |
| Total page weight | < 500KB |
| Font files | ≤ 2 (Inter regular + bold) |

### 15.3 Strategies

| Strategy | Detail |
|----------|--------|
| Static output | Astro default |
| JS minimal | Only `KatalogFilter` + mobile menu |
| Image optimization | Astro `<Image>` component |
| Font loading | `font-display: swap` |
| Preload | Hero image only |

---

## 16. Error Handling

### 16.1 Empty States

| Page | Message |
|------|---------|
| Katalog | "No projects yet — coming soon." |
| Blog | "No articles yet — coming soon." |
| Resources | "No resources yet — coming soon." |
| Testimonials | "No testimonials yet — coming soon." |

### 16.2 404 Page

| Element | Content |
|---------|---------|
| Heading | "404 — Page not found" |
| Message | "The page you're looking for doesn't exist." |
| CTA | "Back to Home" button |

### 16.3 Form Errors

| Error | Message |
|-------|---------|
| Empty field | "This field is required." |
| Invalid email | "Please enter a valid email." |
| Submit fail | "Something went wrong. Try email instead." |

---

## 17. Git Workflow

### 17.1 Branch Strategy

| Branch | Purpose |
|--------|---------|
| `main` | Production (auto-deploy) |
| `dev` | Integration (optional) |
| `feat/*` | Feature branches (optional) |

**Default:** commit directly to `main` (solo project).

### 17.2 Commit Convention

Conventional Commits:

| Type | Usage |
|------|-------|
| `feat:` | New feature |
| `fix:` | Bug fix |
| `docs:` | Documentation |
| `style:` | Formatting |
| `refactor:` | Code restructure |
| `chore:` | Config, deps |
| `content:` | New/updated project or article |

Example: `feat: add katalog filter component`

### 17.3 Commit Cadence

| Phase | Commits |
|-------|---------|
| Phase 1 | 1 commit per file group (config, layout, content schema, deploy) |
| Phase 2–5 | 1 commit per section |
| Phase 6 | 1 commit per fix |

---

## 18. Deployment

### 18.1 GitHub Pages

| Property | Value |
|----------|-------|
| Repository | `katalogarkan/katalogarkan.github.io` |
| Branch | `main` |
| Build output | `dist/` |
| URL | https://katalogarkan.github.io |

### 18.2 GitHub Actions Workflow (Explicit — Single Source of Truth)

File: `.github/workflows/deploy.yml`

```yaml
name: Deploy to GitHub Pages

on:
  push:
    branches: [main]
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: "pages"
  cancel-in-progress: false

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Setup Node
        uses: actions/setup-node@v4
        with:
          node-version: 22
          cache: 'npm'

      - name: Install dependencies
        run: npm ci

      - name: Build with Astro
        run: npm run build

      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: ./dist

  deploy:
    needs: build
    runs-on: ubuntu-latest
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    steps:
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
```

### 18.3 Astro Config

```js
// astro.config.mjs
import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';
import react from '@astrojs/react';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://katalogarkan.github.io',
  integrations: [react(), sitemap()],
  vite: {
    plugins: [tailwindcss()],
  },
});
```

### 18.4 Deployment Flow

```
1. Arkan commits + pushes to main
   │
   ▼
2. GitHub Actions triggers (deploy.yml)
   │
   ▼
3. Actions: checkout → setup Node 22 → npm ci → npm run build
   │
   ▼
4. Actions: upload dist/ as artifact
   │
   ▼
5. Actions: deploy artifact to GitHub Pages
   │
   ▼
6. Site live at katalogarkan.github.io
```

### 18.5 GitHub Pages Settings

| Setting | Value |
|---------|-------|
| Source | GitHub Actions (NOT "Deploy from a branch") |
| Custom domain | (empty at launch) |
| Enforce HTTPS | ✅ (default) |
| Workflow permissions | Read and write |

### 18.6 Custom Domain (Future)

| Property | Value |
|----------|-------|
| Domain | TBD (`katalogarkan.com` or `katalogarkan.dev`) |
| DNS | CNAME to `katalogarkan.github.io` |
| HTTPS | Auto via GitHub |

---

## 19. Security

| # | Concern | Mitigation |
|---|---------|------------|
| 1 | Formspree spam | Honeypot field + Formspree spam filter |
| 2 | Exposed secrets | No secrets in repo; `.gitignore` covers `.env` |
| 3 | Third-party JS | None (only React island, bundled) |
| 4 | External links | `rel="noopener noreferrer"` on `target="_blank"` |
| 5 | Dependency vulnerabilities | `npm audit` before each phase |
| 6 | CSP | Not configured at launch (Astro static) |
| 7 | HTTPS | Enforced by GitHub Pages |
| 8 | Content injection | Markdown files are trusted (owner-authored) |

---

## 20. Execution Phases

### Phase 1 — Fondasi Proyek ✅ Complete (2026-11-01)

**Goal:** Astro project runs locally and deploys to GitHub Pages.

**Prerequisites:** Node.js 22+, Git, GitHub account, repository exists.

| # | Task | File | Status |
|---|------|------|:---:|
| 1 | Init project | `package.json` | ✅ |
| 2 | Install deps (Astro 5, React 18, Tailwind 4) | `package.json` | ✅ |
| 3 | Astro config | `astro.config.mjs` | ✅ |
| 4 | Tailwind config via `@theme` (see §5.9) | `src/styles/global.css` | ✅ |
| 5 | TypeScript config | `tsconfig.json` | ✅ |
| 6 | Gitignore | `.gitignore` | ✅ |
| 7 | Global CSS + dark mode variables (see §5.10) | `src/styles/global.css` | ✅ |
| 8 | Base layout | `src/layouts/BaseLayout.astro` | ✅ |
| 9 | Header placeholder | `src/components/Header.astro` | ✅ |
| 10 | Footer placeholder | `src/components/Footer.astro` | ✅ |
| 11 | Temporary Home | `src/pages/index.astro` | ✅ |
| 12 | Content schema | `src/content.config.ts` | ✅ |
| 13 | Content folders | `src/content/katalog/`, `src/content/blog/` | ✅ |
| 14 | Deploy workflow (see §18.2) | `.github/workflows/deploy.yml` | ✅ |
| 15 | LICENSE | `LICENSE` | ✅ |
| 16 | Verify build + deploy | — | ✅ |

**Phase 1 done when:**
- `npm run dev` shows "Hello" at `localhost:4321`
- `npm run build` succeeds (no errors)
- Push to `main` triggers GitHub Action
- `katalogarkan.github.io` shows "Hello"

**Verification:** 57/57 checks passed.

---

### Phase 2 — Desain & Home ✅ Complete (2026-11-04)

**Goal:** Home page looks professional, responsive, dark mode works.

**Prerequisites:** Phase 1 complete.

| # | Task | File | Verify | Status |
|---|------|------|--------|:---:|
| 1 | Finalize Header (9 nav, hamburger) | `Header.astro` | All 9 links work, hamburger on mobile | ✅ |
| 2 | Finalize Footer (4 columns) | `Footer.astro` | All 4 columns render | ✅ |
| 3 | Verify design tokens | `global.css` | Colors match §5.1 + §5.10 | ✅ |
| 4 | Hero section | `index.astro` | Name, tagline, 2 CTAs | ✅ |
| 5 | Featured projects | `index.astro` | Empty state hides section | ✅ |
| 6 | Skills summary | `index.astro` | Tech badges render | ✅ |
| 7 | Testimonials section | `index.astro` | Empty state hides section | ✅ |
| 8 | CTA section | `index.astro` | Contact link works | ✅ |
| 9 | Mobile responsive check | — | 3 breakpoints (640/768/1024) | ✅ |
| 10 | Dark mode check | — | Change OS theme, verify | ✅ |

**Phase 2 done when:**
- Home matches design spec
- Responsive on mobile, tablet, desktop
- Dark mode follows OS preference
- All 9 nav links navigate correctly
- No `dark:` variants in components (except `prose-invert`)

**Verification:** 30/30 checks passed. Build: 0 errors, 0 warnings.

---

### Phase 3 — Halaman Statis ✅ Complete (2026-11-04)

**Goal:** 6 static pages + 404 complete.

**Prerequisites:** Phase 2 complete.

| # | Task | File | Verify | Status |
|---|------|------|--------|:---:|
| 1 | About page | `about.astro` | Bio, timeline, CV link | ✅ |
| 2 | Skills page | `skills.astro` | Categories, skill bars | ✅ |
| 3 | Services page | `services.astro` | 3 packages, process, FAQ | ✅ |
| 4 | Resources page | `resources.astro` | Grid with empty state | ✅ |
| 5 | Testimonials page | `testimonials.astro` | Grid with empty state | ✅ |
| 6 | Contact page + form | `contact.astro` | Form submits to Formspree | ✅ |
| 7 | 404 page | `404.astro` | Custom 404 renders | ✅ |
| 8 | SkillBadge component | `SkillBadge.astro` | Renders with/without level | ✅ |

**Phase 3 done when:**
- 7 of 9 pages complete (Home + 6 static + 404)
- Contact form submits successfully
- All empty states render correctly

**Verification:** 18/18 checks passed. Build: 9 pages built, 0 errors, 0 warnings.

---

### Phase 4 — Katalog + Filter ✅ Complete (2026-11-04)

**Goal:** Katalog page with filter/search/sort works.

**Prerequisites:** Phase 3 complete.

| # | Task | File | Verify | Status |
|---|------|------|--------|:---:|
| 1 | ProjectCard component | `ProjectCard.astro` | Renders all props | ✅ |
| 2 | Katalog list page | `katalog.astro` | Empty state shows | ✅ |
| 3 | KatalogFilter (React) | `KatalogFilter.tsx` | Filter/search/sort work | ✅ |
| 4 | Empty state | `katalog.astro` | "No projects yet" | ✅ |
| 5 | Hydration check | — | React island hydrates (`client:load`) | ✅ |
| 6 | Build size check | — | JS < 50KB gzipped | ✅ |

**Phase 4 done when:**
- Katalog renders empty state
- Filter works when temp project added
- JS budget met

**Verification:** 9/9 checks passed. Build: 9 pages built, 0 errors, 0 warnings.

**Fixed:** Zod 4 deprecation `z.string().url()` → `z.url()` in `src/content.config.ts`.

---

### Phase 5 — Blog + Detail ✅ Complete (2026-11-04)

**Goal:** Blog list + dynamic detail pages work.

**Prerequisites:** Phase 4 complete.

| # | Task | File | Verify | Status |
|---|------|------|--------|:---:|
| 1 | BlogCard component | `BlogCard.astro` | Renders all props | ✅ |
| 2 | Blog list page | `blog.astro` | Empty state shows | ✅ |
| 3 | PostLayout | `PostLayout.astro` | Article header + prose | ✅ |
| 4 | Blog detail route | `blog/[slug].astro` | Dynamic route works | ✅ |
| 5 | Katalog detail route | `katalog/[slug].astro` | Dynamic route works | ✅ |
| 6 | Empty states | both | "No articles yet" / "No projects yet" | ✅ |
| 7 | Markdown rendering | — | Prose styled via typography plugin | ✅ |

**Phase 5 done when:**
- All 9 pages + 2 detail templates complete
- Markdown renders with prose styling
- Dynamic routes work with temp content

**Verification:** 18/18 checks passed. Build: 12 pages built, 0 errors, 0 warnings.

---

### Phase 6 — Polish & Deploy ⏳ Not Started

**Goal:** SEO, performance, final deploy.

**Prerequisites:** Phase 5 complete.

| # | Task | File | Verify | Status |
|---|------|------|--------|:---:|
| 1 | Sitemap integration | `astro.config.mjs` | `/sitemap-index.xml` accessible | ☐ |
| 2 | robots.txt | `public/robots.txt` | Accessible at `/robots.txt` | ☐ |
| 3 | OG image | `public/images/og-default.png` | 1200×630, renders in social preview | ☐ |
| 4 | Per-page meta tags | all `.astro` | Title, description, OG per page | ☐ |
| 5 | Favicon | `public/favicon.svg` | Shows in browser tab | ☐ |
| 6 | Lighthouse audit | — | ≥ 95 all 4 categories | ☐ |
| 7 | README.md | `README.md` | Complete with setup instructions | ☐ |
| 8 | Docs index | `docs/README.md` | Links to all docs | ☐ |
| 9 | Final deploy + verify | — | Live site verified | ☐ |

**Phase 6 done when:**
- Lighthouse ≥ 95 (Performance, Accessibility, Best Practices, SEO)
- Sitemap and robots.txt accessible
- README complete
- Live site verified end-to-end

**Acceptance:** 41/41 checks passed.

---

## 21. Acceptance Criteria

| Phase | Criteria | How to Verify | Status |
|-------|----------|---------------|:---:|
| 1 | `npm run dev` works | Run locally, open `localhost:4321` | ✅ |
| 1 | `npm run build` succeeds | Run locally, no errors | ✅ |
| 1 | GitHub Action deploys | Check Actions tab, green check | ✅ |
| 1 | Live URL shows "Hello" | Open `katalogarkan.github.io` | ✅ |
| 2 | Home responsive on 3 sizes | DevTools responsive mode | ✅ |
| 2 | Dark mode auto | Change OS theme, verify colors | ✅ |
| 2 | Navbar 9 links work | Click each link | ✅ |
| 3 | 6 static pages complete | Visit each route | ✅ |
| 3 | Contact form submits | Test submission, check Formspree | ✅ |
| 4 | Katalog empty state shows | Visit `/katalog` | ✅ |
| 4 | Filter works with test data | Add temp project, test filter | ✅ |
| 5 | Blog empty state shows | Visit `/blog` | ✅ |
| 5 | Detail routes render | Add temp article, visit `/blog/test` | ✅ |
| 5 | Markdown prose styled | Visual check | ✅ |
| 6 | Lighthouse ≥ 95 all | Run Lighthouse audit | ⏳ |
| 6 | Sitemap accessible | Visit `/sitemap-index.xml` | ⏳ |
| 6 | robots.txt accessible | Visit `/robots.txt` | ⏳ |
| 6 | README complete | Read file | ⏳ |

---

## 22. Troubleshooting

| Issue | Cause | Solution |
|-------|-------|----------|
| `npm run dev` fails | Node version or missing deps | Check Node 22+, run `npm install` |
| Build fails on CI | Node version mismatch | Check `deploy.yml` uses Node 22 |
| GitHub Pages 404 | Repo name wrong or Pages not enabled | Check repo name `katalogarkan.github.io`, enable Pages in Settings |
| Assets 404 on Pages | `site` missing in `astro.config.mjs` | Set `site: 'https://katalogarkan.github.io'` |
| Tailwind classes not applied | `@import "tailwindcss"` missing | Check `global.css` starts with `@import "tailwindcss"` |
| Tailwind 4 plugin error | Missing `@tailwindcss/vite` in Vite plugins | Check `astro.config.mjs` `vite.plugins` |
| Dark mode not working | CSS variables not overridden | Check `@media (prefers-color-scheme: dark)` block in `global.css` |
| React island not hydrating | Missing directive | Check `client:load` on component |
| Content collection error | Frontmatter doesn't match schema | Check `content.config.ts` Zod schema |
| Formspree not submitting | Endpoint wrong or spam filter | Check endpoint URL, check spam |
| Font not loading | Missing Google Fonts link | Check `BaseLayout.astro` head |

---

## 23. Decisions Log

| # | Decision | Value | Rationale |
|---|----------|-------|-----------|
| 1 | Framework | Astro | Content-driven, minimal JS, long-term maintainable |
| 2 | Styling | Tailwind CSS | Utility-first, consistent, fast |
| 3 | Content | Astro Content Collections | Built-in, Zod validation, Markdown-based |
| 4 | Interactivity | React island | Filter needs client state |
| 5 | Hosting | GitHub Pages | Free, repo already exists |
| 6 | Primary color | `#0969da` | Professional, GitHub-like |
| 7 | Font | Inter | Modern, readable |
| 8 | Dark mode | OS preference + CSS variables | Simple, no toggle; single source of truth in §5.9 + §5.10 |
| 9 | Navbar pages | 9 | Full version |
| 10 | Katalog initial content | Empty | No placeholder projects |
| 11 | Blog initial content | Empty | No placeholder articles |
| 12 | Detail pages | Yes (both) | Dynamic routes for katalog & blog |
| 13 | Contact form | Formspree | No server needed |
| 14 | Domain | `katalogarkan.github.io` at launch | Custom domain later |
| 15 | Git workflow | Commit to `main` | Solo project |
| 16 | Commit convention | Conventional Commits | Standard, readable |
| 17 | Empty state | Text message | Simple, honest |
| 18 | 404 page | Custom | Better UX |
| 19 | Sitemap | Auto-generate | SEO |
| 20 | OG image | Static 1 image | Simple at launch |
| 21 | Performance target | Lighthouse ≥ 95 | High bar, achievable |
| 22 | CV | PDF in `public/` | Static download |
| 23 | Formspree | Sign up when Phase 3 starts | Not needed earlier |
| 24 | Content language | English | International audience |
| 25 | Avatar | Placeholder first | Replace when ready |
| 26 | Custom domain | After Phase 6 | Focus on build first |
| 27 | Deploy workflow | Explicit workflow (not `withastro/action@v3`) | Transparent, easier to debug; single source in §18.2 |
| 28 | Tailwind dark mode | CSS variables in `global.css` (§5.10) | Avoids hardcoded `dark:` variants everywhere; single source of truth |
| 29 | License | MIT | Permissive, portfolio-friendly |
| 30 | Docs location | `docs/` with `README.md` index | Centralized, navigable |
| 31 | Astro version | Astro 5.x | Current stable; Content Layer API |
| 32 | Tailwind integration | `@tailwindcss/vite` (not `@astrojs/tailwind`) | Tailwind 4 requires Vite plugin; `@astrojs/tailwind` deprecated |
| 33 | Tailwind config | CSS-first `@theme` (no `tailwind.config.mjs`) | Tailwind 4 native approach |
| 34 | Node version | Node 22 in CI | Current LTS; matches local dev |
| 35 | Content config path | `src/content.config.ts` | Astro 5+ API (moved from `src/content/config.ts`) |
| 36 | Changelog location | Root `CHANGELOG.md` | Keep a Changelog convention; single source of truth |
| 37 | Screenshots folder | `screenshots/` at repo root | Used by README architecture diagrams |

---

## 24. Open Questions

| # | Question | Impact | Target Phase | Status |
|---|----------|--------|--------------|--------|
| 1 | Custom domain (`katalogarkan.com` / `.dev`)? | Deployment | Phase 6+ | ⏳ Open |
| 2 | Formspree account created? | Contact form | Phase 3 | ✅ Resolved |
| 3 | CV PDF ready for `/about`? | About page | Phase 3 | ⏳ Open |
| 4 | Avatar/photo ready? | Home, About | Phase 2 | ⏳ Open |
| 5 | First 3 projects to feature? | Home | Phase 2 | ⏳ Open |
| 6 | Blog: write first article before launch? | Blog launch | Phase 5 | ✅ Sample article added |
| 7 | Testimonials: real quotes available? | Testimonials | Phase 3 | ⏳ Open |
| 8 | Resources: any templates/snippets ready? | Resources | Phase 3 | ⏳ Open |

---

## 25. Glossary

| Term | Definition |
|------|------------|
| Astro | Static site framework with islands architecture |
| Content Collections | Astro feature for typed Markdown content |
| Island | Interactive component hydrated on client |
| SSG | Static Site Generation |
| Zod | TypeScript schema validation library |
| OG | Open Graph (social media meta tags) |
| LCP | Largest Contentful Paint |
| CLS | Cumulative Layout Shift |
| INP | Interaction to Next Paint |
| CTA | Call to Action |
| MDX | Markdown + JSX (not used at launch) |
| Hydration | Process of attaching JS to static HTML |
| CSS Variables | Custom properties (`--color-*`) used for dark mode overrides |
| `@theme` | Tailwind 4 CSS directive for defining design tokens |
| `@tailwindcss/vite` | Vite plugin that compiles Tailwind 4 |

---

## 26. References

| Resource | URL |
|----------|-----|
| Astro Docs | https://docs.astro.build |
| Tailwind Docs | https://tailwindcss.com/docs |
| Tailwind 4 Theme | https://tailwindcss.com/docs/theme |
| Astro Content Collections | https://docs.astro.build/en/guides/content-collections/ |
| Astro GitHub Pages | https://docs.astro.build/en/guides/deploy/github/ |
| Astro React Integration | https://docs.astro.build/en/guides/integrations-guide/react/ |
| Formspree | https://formspree.io |
| Inter Font | https://fonts.google.com/specimen/Inter |
| GitHub Pages | https://pages.github.com |
| Conventional Commits | https://www.conventionalcommits.org |

---

## 27. Change Log

| Version | Date | Changes |
|---------|------|---------|
| 1.3.0 | 2026-11-04 | Synced with `CHANGELOG.md` v1.2.0 after Phase 5: `Project Version` bumped to 0.5.0; Phase 2, 3, 4, 5 marked ✅ Complete with verification counts (30/30, 18/18, 9/9, 18/18); Phase 6 marked ⏳ Not Started with 41 planned checks; §21 Acceptance Criteria updated with status column; §24 Open Questions updated with status (Formspree ✅, sample article ✅); component count corrected to 6 (+1 React island); `demo-video.md` added to project structure. |
| 1.2.0 | 2026-11-04 | Rewrite for consistency after Phase 1: Astro 5 + Tailwind 4 (`@tailwindcss/vite`, `@theme`), Node 22, `src/content.config.ts`, no `tailwind.config.mjs`, single root `CHANGELOG.md`, decisions #31–37 added, Phase 1 marked complete. |
| 1.1.0 | 2026-10-26 | Dark mode via CSS variables; explicit deploy workflow; added GitHub Pages settings, LICENSE, `docs/README.md`; decisions #27–30. |
| 1.0.1 | 2026-10-26 | Initial planning split into Document Version vs Project Version. |
| 1.0.0 | 2026-10-26 | Initial blueprint. |

---

*End of document.*