# katalogarkan — cheatsheets.md

---

## Document Information

| Property | Value |
|----------|-------|
| Document Version | 1.3.0 |
| Project Version | 0.5.0 (Phase 5 Complete) |
| Last Updated | 2026-11-04 |
| Status | Approved — Quick Reference |
| Project | Personal branding & katalog website |
| Owner | Arkan (Full Stack Web Developer) |
| Related | `blueprint.md`, `design-system.md`, `deployment-guide.md`, `content-guide.md` |
| Framework | Astro 5 + Tailwind CSS 4 |
| Node Version | 22 |

---

## Table of Contents

1. [Purpose](#1-purpose)
2. [Daily Commands](#2-daily-commands)
3. [File Paths](#3-file-paths)
4. [Astro Cheatsheet](#4-astro-cheatsheet)
5. [Tailwind 4 Cheatsheet](#5-tailwind-4-cheatsheet)
6. [Git & Deploy](#6-git--deploy)
7. [Design Tokens](#7-design-tokens)
8. [Component Patterns](#8-component-patterns)
9. [Content Cheatsheet](#9-content-cheatsheet)
10. [SEO & Meta](#10-seo--meta)
11. [Accessibility](#11-accessibility)
12. [Performance](#12-performance)
13. [Troubleshooting](#13-troubleshooting)
14. [Decision Quick Reference](#14-decision-quick-reference)
15. [Links](#15-links)
16. [Change Log](#16-change-log)

---

## 1. Purpose

### 1.1 What This Document Is

A one-stop quick reference for daily development on the katalogarkan project. Copy-paste commands, file paths, component patterns, and troubleshooting — no long explanations.

### 1.2 When to Use

| Situation | Section |
|-----------|---------|
| Starting dev server | §2 Daily Commands |
| Forgot where a file lives | §3 File Paths |
| Writing an Astro component | §4 Astro Cheatsheet |
| Writing Tailwind classes | §5 Tailwind 4 Cheatsheet |
| Committing / deploying | §6 Git & Deploy |
| Picking a color / spacing | §7 Design Tokens |
| Building a card / button | §8 Component Patterns |
| Adding a project / article | §9 Content Cheatsheet |
| Adding meta tags | §10 SEO & Meta |
| Checking accessibility | §11 Accessibility |
| Checking performance | §12 Performance |
| Something broken | §13 Troubleshooting |
| "Why did we choose X?" | §14 Decision Quick Reference |

### 1.3 Rule

If this document conflicts with `blueprint.md` or `design-system.md`, those documents win. This is a shortcut, not a source of truth.

---

## 2. Daily Commands

### 2.1 Development

```bash
# Install dependencies
npm install

# Start dev server (http://localhost:4321)
npm run dev

# Build for production (outputs to dist/)
npm run build

# Preview production build locally
npm run preview

# Type check (if configured)
npx astro check
```

### 2.2 Cleanup

```bash
# Remove node_modules + lockfile, reinstall
rm -rf node_modules package-lock.json && npm install

# Remove build output + Astro cache
rm -rf dist .astro
```

### 2.3 Windows Notes

```powershell
# PowerShell equivalent
Remove-Item -Recurse -Force node_modules, dist, .astro
```

---

## 3. File Paths

### 3.1 Key Files

| Purpose | Path |
|---------|------|
| Astro config | `astro.config.mjs` |
| Global CSS + Tailwind theme | `src/styles/global.css` |
| Content schema (Zod) | `src/content.config.ts` |
| Base layout | `src/layouts/BaseLayout.astro` |
| Post layout (blog/katalog detail) | `src/layouts/PostLayout.astro` |
| Header | `src/components/Header.astro` |
| Footer | `src/components/Footer.astro` |
| Project card | `src/components/ProjectCard.astro` |
| Blog card | `src/components/BlogCard.astro` |
| Skill badge | `src/components/SkillBadge.astro` |
| Katalog filter (React) | `src/components/KatalogFilter.tsx` |
| Home page | `src/pages/index.astro` |
| Katalog list | `src/pages/katalog.astro` |
| Katalog detail | `src/pages/katalog/[slug].astro` |
| Blog list | `src/pages/blog.astro` |
| Blog detail | `src/pages/blog/[slug].astro` |
| 404 page | `src/pages/404.astro` |
| Deploy workflow | `.github/workflows/deploy.yml` |
| Changelog | `CHANGELOG.md` |
| License | `LICENSE` |

### 3.2 Content Folders

| Content | Path | URL |
|---------|------|-----|
| Projects | `src/content/katalog/{slug}.md` | `/katalog/{slug}` |
| Articles | `src/content/blog/{slug}.md` | `/blog/{slug}` |

### 3.3 Asset Folders

| Asset | Path | Reference |
|-------|------|-----------|
| Project thumbnails | `public/images/projects/` | `/images/projects/{name}.png` |
| Blog covers | `public/images/blog/` | `/images/blog/{name}.png` |
| Avatar | `public/images/avatar.png` | `/images/avatar.png` |
| OG image | `public/images/og-default.png` | `/images/og-default.png` |
| CV | `public/cv.pdf` | `/cv.pdf` |
| Favicon | `public/favicon.svg` | `/favicon.svg` |
| Robots | `public/robots.txt` | `/robots.txt` |

### 3.4 Docs Folder

| Document | Path |
|----------|------|
| Docs index | `docs/README.md` |
| Blueprint | `docs/blueprint.md` |
| Design system | `docs/design-system.md` |
| Content guide | `docs/content-guide.md` |
| Verification checklist | `docs/verification-checklist.md` |
| Cheatsheets | `docs/cheatsheets.md` |
| Deployment guide | `docs/deployment-guide.md` |
| Demo video plan | `docs/demo-video.md` |

**Note:** Changelog lives at root (`CHANGELOG.md`), not in `docs/`.

---

## 4. Astro Cheatsheet

### 4.1 Component Structure

```astro
---
// Component script (runs at build time)
interface Props {
  title: string;
  description?: string;
}
const { title, description = "Default" } = Astro.props;
---

<!-- Template -->
<article>
  <h2>{title}</h2>
  {description && <p>{description}</p>}
</article>

<style>
  /* Scoped CSS */
</style>

<script>
  // Client-side JS (runs in browser)
</script>
```

### 4.2 Frontmatter

| Syntax | Purpose |
|--------|---------|
| `---` ... `---` | Component script block |
| `Astro.props` | Access props |
| `Astro.url` | Current URL |
| `Astro.params` | Dynamic route params |
| `Astro.request` | Request object |

### 4.3 Directives

| Directive | Purpose |
|-----------|---------|
| `client:load` | Hydrate immediately (React island) |
| `client:idle` | Hydrate when browser idle |
| `client:visible` | Hydrate when visible |
| `client:only="react"` | Skip SSR, client only |
| `is:global` | Global CSS (in `<style>`) |
| `set:html` | Render raw HTML |
| `class:list` | Conditional classes |

### 4.4 Content Collections

```js
// src/pages/katalog/[slug].astro
import { getCollection } from 'astro:content';

export async function getStaticPaths() {
  const projects = await getCollection('katalog');
  return projects.map(project => ({
    params: { slug: project.id },
    props: { project },
  }));
}

const { project } = Astro.props;
const { Content } = await project.render();
```

| Function | Purpose |
|----------|---------|
| `getCollection('katalog')` | All projects |
| `getCollection('blog', ({ data }) => !data.draft)` | Published articles only |
| `getEntry('katalog', 'slug')` | Single entry |
| `entry.render()` | Render Markdown body |
| `entry.id` | Slug (from filename) |
| `entry.data` | Validated frontmatter |

### 4.5 Layouts

```astro
---
// src/layouts/BaseLayout.astro
import Header from '../components/Header.astro';
import Footer from '../components/Footer.astro';
import '../styles/global.css';

interface Props {
  title: string;
  description?: string;
}
const { title, description = "Arkan — Full Stack Web Developer" } = Astro.props;
---

<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>{title}</title>
    <meta name="description" content={description} />
  </head>
  <body>
    <a href="#main" class="sr-only focus:not-sr-only ...">Skip to content</a>
    <Header />
    <main id="main">
      <slot />
    </main>
    <Footer />
  </body>
</html>
```

### 4.6 Gotchas

| Issue | Fix |
|-------|-----|
| `Astro.props` undefined | Destructure in frontmatter |
| `getCollection` not found | Import from `astro:content` |
| Content not rendering | Call `await entry.render()` |
| `content.config.ts` not found | Must be at `src/content.config.ts` (not `src/content/config.ts`) |
| Image 404 | Use `/images/...` (absolute), not `./images/...` |

---

## 5. Tailwind 4 Cheatsheet

### 5.1 Setup (Already Done)

```css
/* src/styles/global.css */
@import "tailwindcss";
@plugin "@tailwindcss/typography";

@theme {
  --color-primary: #0969da;
  /* ... */
}
```

```js
// astro.config.mjs
import tailwindcss from '@tailwindcss/vite';

export default defineConfig({
  vite: { plugins: [tailwindcss()] },
});
```

**No `tailwind.config.mjs`. No `@astrojs/tailwind`.**

### 5.2 Token Classes

| Class | Resolves To |
|-------|-------------|
| `bg-bg` | `var(--color-bg)` |
| `bg-bg-subtle` | `var(--color-bg-subtle)` |
| `text-text` | `var(--color-text)` |
| `text-text-muted` | `var(--color-text-muted)` |
| `text-primary` | `var(--color-primary)` |
| `bg-primary` | `var(--color-primary)` |
| `hover:bg-primary-hover` | `var(--color-primary-hover)` |
| `border-border` | `var(--color-border)` |
| `text-success` | `var(--color-success)` |
| `text-warning` | `var(--color-warning)` |
| `text-danger` | `var(--color-danger)` |

### 5.3 Dark Mode

| Rule | Example |
|------|---------|
| ✅ Correct — automatic | `class="bg-bg-subtle text-text"` |
| ❌ Wrong — hardcoded | `class="bg-white dark:bg-gray-900"` |
| ✅ Allowed exception | `class="prose dark:prose-invert"` |

**No `dark:` prefix.** CSS variables handle it.

### 5.4 Common Patterns

```html
<!-- Container -->
<div class="max-w-6xl mx-auto px-4 md:px-8">

<!-- Or the utility -->
<div class="container-page">

<!-- Grid: 1 col mobile, 2 tablet, 3 desktop -->
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">

<!-- Section -->
<section class="py-12 md:py-16">
  <div class="container-page">
    <h2 class="text-2xl font-bold mb-8">Title</h2>
  </div>
</section>

<!-- Card -->
<div class="bg-bg-subtle border border-border rounded-lg p-6 shadow-md hover:shadow-lg transition-shadow">

<!-- Button -->
<button class="bg-primary text-white font-medium px-4 py-2 rounded-md hover:bg-primary-hover focus-visible:ring-2 focus-visible:ring-primary focus-visible:ring-offset-2 transition-colors">

<!-- Text -->
<p class="text-text-muted text-sm">Secondary text</p>

<!-- Link -->
<a class="text-primary underline hover:text-primary-hover" href="/katalog">Katalog</a>

<!-- Badge -->
<span class="inline-flex items-center px-2 py-1 rounded-full text-xs font-medium bg-primary/10 text-primary">Astro</span>

<!-- Prose (Markdown body) -->
<article class="prose dark:prose-invert max-w-none">
```

### 5.5 Spacing Shortcuts

| Tailwind | Value |
|----------|-------|
| `p-1` `m-1` `gap-1` | 4px |
| `p-2` `m-2` `gap-2` | 8px |
| `p-4` `m-4` `gap-4` | 16px |
| `p-6` `m-6` `gap-6` | 24px |
| `p-8` `m-8` `gap-8` | 32px |
| `p-12` `m-12` `gap-12` | 48px |
| `p-16` `m-16` `gap-16` | 64px |

### 5.6 Gotchas

| Issue | Fix |
|-------|-----|
| Classes not applied | Check `@import "tailwindcss"` at top of `global.css` |
| `@theme` not working | Must be before `@layer base` |
| `border-border` not working | Ensure `--color-border` is in `@theme` |
| Dark mode not switching | Check `@media (prefers-color-scheme: dark)` block |
| `prose` not styled | Add `@plugin "@tailwindcss/typography"` |
| Arbitrary value fails | Use `bg-[var(--color-primary)]` or token class |

---

## 6. Git & Deploy

### 6.1 Commit Convention

| Type | Usage | Example |
|------|-------|---------|
| `feat:` | New feature | `feat: add katalog filter` |
| `fix:` | Bug fix | `fix: correct nav link` |
| `docs:` | Documentation | `docs: update blueprint` |
| `style:` | Formatting | `style: format header` |
| `refactor:` | Code restructure | `refactor: extract card` |
| `chore:` | Config, deps | `chore: bump astro` |
| `content:` | New/updated content | `content: add project X` |

### 6.2 Commit Flow

```bash
# Check status
git status

# Stage all
git add .

# Commit
git commit -m "feat: add katalog filter"

# Push (triggers deploy)
git push origin main
```

### 6.3 Deploy

| Step | Command |
|------|---------|
| Build locally | `npm run build` |
| Commit + push | `git add . && git commit -m "..." && git push origin main` |
| Watch Actions | https://github.com/katalogarkan/katalogarkan.github.io/actions |
| Verify live | https://katalogarkan.github.io |

### 6.4 Rollback

```bash
# Find commit
git log --oneline -10

# Revert (safe)
git revert <commit-hash>
git push origin main

# Reset (destructive)
git reset --hard <commit-hash>
git push --force origin main
```

### 6.5 Workflow File

Must match `blueprint.md` §18.2 / `deployment-guide.md` §5.2 exactly. Key points:

- Node 22
- `npm ci` (not `npm install`)
- Upload `./dist`
- Deploy via `actions/deploy-pages@v4`

---

## 7. Design Tokens

### 7.1 Colors

| Token | Light | Dark | Classes |
|-------|-------|------|---------|
| `primary` | `#0969da` | `#58a6ff` | `text-primary` `bg-primary` `border-primary` |
| `primary-hover` | `#0550ae` | `#79c0ff` | `hover:bg-primary-hover` `hover:text-primary-hover` |
| `bg` | `#ffffff` | `#0d1117` | `bg-bg` |
| `bg-subtle` | `#f6f8fa` | `#161b22` | `bg-bg-subtle` |
| `text` | `#1f2328` | `#e6edf3` | `text-text` |
| `text-muted` | `#656d76` | `#8b949e` | `text-text-muted` |
| `border` | `#d0d7de` | `#30363d` | `border-border` |
| `success` | `#1a7f37` | `#3fb950` | `text-success` |
| `warning` | `#9a6700` | `#d29922` | `text-warning` |
| `danger` | `#cf222e` | `#f85149` | `text-danger` |

All tokens are CSS variables in `@theme`. Dark mode overrides them automatically.

### 7.2 Typography

| Element | Size | Class |
|---------|------|-------|
| Hero | 60px | `text-6xl font-bold` |
| H1 | 36px | `text-4xl font-bold` |
| H2 | 24px | `text-2xl font-bold` |
| H3 | 20px | `text-xl font-bold` |
| H4 | 18px | `text-lg font-bold` |
| Body | 16px | `text-base` |
| Small | 14px | `text-sm` |
| Badge | 12px | `text-xs` |

### 7.3 Radius

| Class | Value | Usage |
|-------|-------|-------|
| `rounded-sm` | 4px | Badges |
| `rounded-md` | 8px | Buttons, inputs |
| `rounded-lg` | 12px | Cards |
| `rounded-full` | 9999px | Avatars, pills |

### 7.4 Shadow

| Class | Usage |
|-------|-------|
| `shadow-sm` | Header, button default |
| `shadow-md` | Card default |
| `shadow-lg` | Card hover, dropdown |

### 7.5 Breakpoints

| Prefix | Min width | Target |
|--------|-----------|--------|
| (none) | 0 | Mobile |
| `sm:` | 640px | Large phone |
| `md:` | 768px | Tablet |
| `lg:` | 1024px | Small laptop |
| `xl:` | 1280px | Desktop |
| `2xl:` | 1536px | Large desktop |

---

## 8. Component Patterns

### 8.1 Page Template

```astro
---
import BaseLayout from '../layouts/BaseLayout.astro';

const title = "Page Title";
const description = "Page description.";
---

<BaseLayout {title} {description}>
  <section class="py-12 md:py-16">
    <div class="container-page">
      <h1 class="text-4xl font-bold mb-4">{title}</h1>
      <p class="text-text-muted text-lg">{description}</p>
      <!-- content -->
    </div>
  </section>
</BaseLayout>
```

### 8.2 Card Grid Page

```astro
---
import BaseLayout from '../layouts/BaseLayout.astro';
import { getCollection } from 'astro:content';

const items = await getCollection('katalog');
---

<BaseLayout title="Katalog" description="Projects built by Arkan.">
  <section class="py-12 md:py-16">
    <div class="container-page">
      <h1 class="text-4xl font-bold mb-8">Katalog</h1>
      {items.length === 0 ? (
        <p class="text-text-muted">No projects yet — coming soon.</p>
      ) : (
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {items.map(item => <ProjectCard {...item.data} slug={item.id} />)}
        </div>
      )}
    </div>
  </section>
</BaseLayout>
```

### 8.3 Dynamic Detail Page

```astro
---
import BaseLayout from '../../layouts/BaseLayout.astro';
import { getCollection } from 'astro:content';

export async function getStaticPaths() {
  const items = await getCollection('katalog');
  return items.map(item => ({
    params: { slug: item.id },
    props: { item },
  }));
}

const { item } = Astro.props;
const { Content } = await item.render();
---

<BaseLayout title={item.data.title} description={item.data.description}>
  <article class="py-12 md:py-16">
    <div class="container-page max-w-prose">
      <h1 class="text-4xl font-bold mb-4">{item.data.title}</h1>
      <p class="text-text-muted mb-8">{item.data.description}</p>
      <div class="prose dark:prose-invert max-w-none">
        <Content />
      </div>
    </div>
  </article>
</BaseLayout>
```

### 8.4 React Island

```tsx
// src/components/KatalogFilter.tsx
import { useState } from 'react';

interface Project {
  title: string;
  category: string;
  techStack: string[];
  date: string;
}

export default function KatalogFilter({ projects }: { projects: Project[] }) {
  const [category, setCategory] = useState<string>('all');
  const [search, setSearch] = useState<string>('');
  const [sort, setSort] = useState<string>('newest');

  const filtered = projects
    .filter(p => category === 'all' || p.category === category)
    .filter(p => p.title.toLowerCase().includes(search.toLowerCase()))
    .sort((a, b) => sort === 'newest'
      ? new Date(b.date).getTime() - new Date(a.date).getTime()
      : new Date(a.date).getTime() - new Date(b.date).getTime()
    );

  return (
    <div>
      <input
        type="text"
        value={search}
        onChange={e => setSearch(e.target.value)}
        placeholder="Search..."
        className="w-full px-3 py-2 rounded-md border border-border bg-bg text-text"
      />
      {/* select category, select sort, grid of filtered */}
    </div>
  );
}
```

```astro
<!-- Usage in .astro -->
<KatalogFilter projects={projects} client:load />
```

### 8.5 Mobile Menu Toggle

```astro
<!-- Header.astro -->
<button
  id="menu-toggle"
  aria-label="Open menu"
  aria-expanded="false"
  aria-controls="mobile-menu"
  class="md:hidden"
>
  <svg class="w-6 h-6" aria-hidden="true">...</svg>
</button>

<nav id="mobile-menu" class="hidden md:hidden">
  <!-- links -->
</nav>

<script>
  const toggle = document.getElementById('menu-toggle');
  const menu = document.getElementById('mobile-menu');
  toggle?.addEventListener('click', () => {
    const expanded = toggle.getAttribute('aria-expanded') === 'true';
    toggle.setAttribute('aria-expanded', String(!expanded));
    menu?.classList.toggle('hidden');
  });
</script>
```

---

## 9. Content Cheatsheet

### 9.1 Katalog Frontmatter

```yaml
---
title: "Project Name"
description: "Short description (20–160 chars)."
techStack: ["Astro", "Tailwind CSS", "TypeScript"]
thumbnail: "/images/projects/project-name.png"
demoUrl: "https://example.com"
repoUrl: "https://github.com/katalogarkan/project-name"
category: "web-app"
featured: true
date: 2026-11-01
---
```

**Categories:** `web-app` | `landing-page` | `api` | `mobile`

### 9.2 Blog Frontmatter

```yaml
---
title: "Article Title"
date: 2026-11-04
description: "Short summary (20–160 chars)."
category: "tutorial"
tags: ["astro", "tailwind"]
draft: false
coverImage: "/images/blog/article-title.png"
---
```

**Categories:** `tutorial` | `tips` | `notes`

### 9.3 File Naming

| Rule | Example |
|------|---------|
| lowercase | `my-project.md` |
| hyphen-separated | `astro-tailwind-guide.md` |
| no spaces / underscores | ❌ `my project.md`, `my_project.md` |
| slug = filename | `my-project.md` → `/katalog/my-project` |

### 9.4 Add Content Checklist

| # | Step |
|---|------|
| 1 | Create `src/content/{collection}/{slug}.md` |
| 2 | Fill frontmatter (all required fields) |
| 3 | Write body (Markdown) |
| 4 | Add image to `public/images/{collection}/{slug}.png` |
| 5 | Run `npm run build` (validates schema) |
| 6 | Preview `npm run dev` |
| 7 | Commit + push |

### 9.5 Common Validation Errors

| Error | Fix |
|-------|-----|
| `title` required | Add `title:` |
| `Invalid enum value` | Use allowed category |
| `Expected array` | Use `[...]` for `techStack`/`tags` |
| `Invalid date` | Use `YYYY-MM-DD` |
| `Unknown key` | Check field name spelling |

---

## 10. SEO & Meta

### 10.1 Required Meta Tags

```astro
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{title} — Arkan</title>
  <meta name="description" content={description} />
  <link rel="canonical" href={`https://katalogarkan.github.io${Astro.url.pathname}`} />

  <!-- Open Graph -->
  <meta property="og:title" content={`${title} — Arkan`} />
  <meta property="og:description" content={description} />
  <meta property="og:image" content="https://katalogarkan.github.io/images/og-default.png" />
  <meta property="og:url" content={`https://katalogarkan.github.io${Astro.url.pathname}`} />
  <meta property="og:type" content="website" />

  <!-- Twitter -->
  <meta name="twitter:card" content="summary_large_image" />
</head>
```

### 10.2 Page Title Format

| Page | Title |
|------|-------|
| Home | `Arkan — Full Stack Web Developer` |
| Katalog | `Katalog — Arkan` |
| Blog | `Blog — Arkan` |
| Detail | `{entry.title} — Arkan` |

### 10.3 Sitemap & Robots

| File | Path | Content |
|------|------|---------|
| Sitemap | `/sitemap-index.xml` | Auto-generated by `@astrojs/sitemap` |
| Robots | `public/robots.txt` | `User-agent: *` / `Allow: /` / `Sitemap: https://katalogarkan.github.io/sitemap-index.xml` |

---

## 11. Accessibility

### 11.1 Checklist Per Component

| # | Check |
|---|-------|
| 1 | Semantic HTML (`<header>`, `<nav>`, `<main>`, `<article>`) |
| 2 | One `<h1>` per page |
| 3 | Heading levels not skipped |
| 4 | All images have `alt` |
| 5 | All inputs have `<label>` |
| 6 | Icon-only buttons have `aria-label` |
| 7 | Focus visible (`focus-visible:ring-2`) |
| 8 | Color contrast ≥ 4.5:1 |
| 9 | Keyboard navigable |
| 10 | Reduced motion respected |

### 11.2 Common Patterns

```html
<!-- Skip link -->
<a href="#main" class="sr-only focus:not-sr-only focus:absolute focus:top-4 focus:left-4 focus:bg-primary focus:text-white focus:px-4 focus:py-2 focus:rounded-md">
  Skip to content
</a>

<!-- Icon-only button -->
<button aria-label="Open menu">
  <svg class="w-6 h-6" aria-hidden="true">...</svg>
</button>

<!-- Decorative icon -->
<svg class="w-5 h-5" aria-hidden="true">...</svg>

<!-- Form label -->
<label for="email" class="block text-sm font-medium text-text mb-1">Email</label>
<input id="email" type="email" class="..." />
```

---

## 12. Performance

### 12.1 Targets

| Metric | Target |
|--------|--------|
| Lighthouse Performance | ≥ 95 |
| Lighthouse Accessibility | ≥ 95 |
| Lighthouse Best Practices | ≥ 95 |
| Lighthouse SEO | ≥ 95 |
| LCP | < 2.5s |
| CLS | < 0.1 |
| INP | < 200ms |

### 12.2 Budget

| Asset | Budget |
|-------|--------|
| JS (Katalog page) | < 50KB gzipped |
| JS (other pages) | < 10KB gzipped |
| CSS | < 20KB gzipped |
| Page weight | < 500KB |

### 12.3 Image Rules

| Rule | Detail |
|------|--------|
| Lazy load | `loading="lazy"` on below-fold |
| Hero image | No lazy, preload |
| Dimensions | Set width/height to avoid CLS |
| Format | `.webp` preferred, `.png` fallback |

---

## 13. Troubleshooting

### 13.1 Build Errors

| Symptom | Fix |
|---------|-----|
| `content.config.ts` not found | Must be `src/content.config.ts` (not `src/content/config.ts`) |
| `Invalid frontmatter` | Check `blueprint.md` §9 schema |
| `@tailwindcss/vite` not found | `npm install @tailwindcss/vite` |
| `@astrojs/tailwind` found | Remove it — not used in Tailwind 4 |

### 13.2 Styling Errors

| Symptom | Fix |
|---------|-----|
| Tailwind classes not applied | Check `@import "tailwindcss"` at top of `global.css` |
| `@theme` tokens not working | Ensure `@theme` is before `@layer base` |
| `border-border` not working | Check `--color-border` in `@theme` |
| Dark mode not switching | Check `@media (prefers-color-scheme: dark)` block |
| `prose` not styled | Add `@plugin "@tailwindcss/typography"` |

### 13.3 Deploy Errors

| Symptom | Fix |
|---------|-----|
| CI fails on `npm ci` | Commit `package-lock.json` |
| CI fails on build | Run `npm run build` locally first |
| 404 on live | Check Pages source = GitHub Actions |
| Assets 404 | Check `site` in `astro.config.mjs` |
| Old content | Hard refresh (Ctrl+Shift+R) |

### 13.4 Quick Diagnostic

```bash
# Full clean rebuild
rm -rf node_modules dist .astro package-lock.json && npm install && npm run build

# Check what Astro sees
npx astro check

# Find broken references
grep -r "old-slug" src/
```

---

## 14. Decision Quick Reference

| # | Decision | Value |
|---|----------|-------|
| 1 | Framework | Astro 5 |
| 2 | Styling | Tailwind CSS 4 (`@tailwindcss/vite`) |
| 3 | Tailwind config | CSS-first `@theme` (no `tailwind.config.mjs`) |
| 4 | Content | Astro Content Collections + Zod |
| 5 | Content config path | `src/content.config.ts` |
| 6 | Interactivity | React 18 island (katalog filter only) |
| 7 | Node version | 22 |
| 8 | Hosting | GitHub Pages |
| 9 | Deploy | GitHub Actions (explicit workflow) |
| 10 | Primary color | `#0969da` |
| 11 | Font | Inter |
| 12 | Dark mode | `prefers-color-scheme` + CSS variables |
| 13 | Contact form | Formspree |
| 14 | Changelog location | Root `CHANGELOG.md` |
| 15 | License | MIT |
| 16 | Content language | English |

Full list: `blueprint.md` §23.

---

## 15. Links

| Resource | URL |
|----------|-----|
| Live site | https://katalogarkan.github.io |
| Repository | https://github.com/katalogarkan/katalogarkan.github.io |
| Actions | https://github.com/katalogarkan/katalogarkan.github.io/actions |
| Astro Docs | https://docs.astro.build |
| Tailwind Docs | https://tailwindcss.com/docs |
| Tailwind Theme | https://tailwindcss.com/docs/theme |
| Content Collections | https://docs.astro.build/en/guides/content-collections/ |
| Formspree | https://formspree.io |
| Inter Font | https://fonts.google.com/specimen/Inter |

---

## 16. Change Log

| Version | Date | Changes |
|---------|------|---------|
| 1.3.0 | 2026-11-04 | Synced with `blueprint.md` v1.3.0 after Phase 5: `Project Version` bumped to 0.5.0; added `demo-video.md` to docs table; all content verified against current state (Astro 5, Tailwind 4, Node 22, `src/content.config.ts`, single root `CHANGELOG.md`); component list confirmed at 6 (+1 React island). |
| 1.2.0 | 2026-11-04 | Synced with `blueprint.md` v1.2.0 + `design-system.md` v1.2.0: Astro 5 + Tailwind 4; removed all `tailwind.config.mjs` references; `@theme` is the config; `src/content.config.ts` path; Node 22; `client:only="react"` fixed; dark mode via CSS variables (no `dark:` prefix); `prose dark:prose-invert` documented as only exception; `content:` commit type added; single root `CHANGELOG.md`; new §8.4 React island example; new §8.5 mobile menu pattern. |
| 1.1.0 | 2026-10-26 | Dark mode via CSS variables; deploy workflow references explicit version; `LICENSE` + `docs/README.md` added to file paths; added `border-border` troubleshooting. |
| 1.0.1 | 2026-10-26 | Document Info split into `Document Version` vs `Project Version`. |
| 1.0.0 | 2026-10-26 | Initial cheatsheets. |

---

*End of document.*