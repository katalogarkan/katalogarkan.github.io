# katalogarkan — cheatsheets.md

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
| Related | `blueprint.md`, `design-system.md`, `content-guide.md`, `verification-checklist.md` |
| Purpose | Quick reference for daily development |
| Framework | Astro + Tailwind CSS |
| Hosting | GitHub Pages |

---

## Table of Contents

1. [Quick Start](#1-quick-start)
2. [Project Commands](#2-project-commands)
3. [File Paths](#3-file-paths)
4. [Content Commands](#4-content-commands)
5. [Git Commands](#5-git-commands)
6. [Deploy Commands](#6-deploy-commands)
7. [Tailwind Quick Reference](#7-tailwind-quick-reference)
8. [Astro Quick Reference](#8-astro-quick-reference)
9. [Content Schema Quick Reference](#9-content-schema-quick-reference)
10. [Common Patterns](#10-common-patterns)
11. [Environment](#11-environment)
12. [URLs](#12-urls)
13. [Troubleshooting](#13-troubleshooting)
14. [One-Liners](#14-one-liners)
15. [Documentation Links](#15-documentation-links)
16. [Change Log](#16-change-log)

---

## 1. Quick Start

### 1.1 First Time Setup

```bash
# 1. Clone repo
git clone https://github.com/katalogarkan/katalogarkan.github.io.git
cd katalogarkan.github.io

# 2. Install dependencies
npm install

# 3. Start dev server
npm run dev

# 4. Open browser
# http://localhost:4321
```

### 1.2 Daily Workflow

```bash
# 1. Pull latest
git pull origin main

# 2. Start dev server
npm run dev

# 3. Edit files (Astro auto-reloads)

# 4. Test at http://localhost:4321

# 5. Build to verify
npm run build

# 6. Commit + push
git add .
git commit -m "feat: add new project"
git push origin main

# 7. Wait 1–2 min for GitHub Actions
# 8. Verify at https://katalogarkan.github.io
```

---

## 2. Project Commands

### 2.1 NPM Scripts

| Command | Purpose |
|---------|---------|
| `npm install` | Install dependencies |
| `npm run dev` | Start dev server (localhost:4321) |
| `npm run build` | Build for production (outputs to `dist/`) |
| `npm run preview` | Preview production build locally |
| `npm run astro` | Run Astro CLI commands |

### 2.2 Astro CLI

| Command | Purpose |
|---------|---------|
| `npx astro add react` | Add React integration |
| `npx astro add tailwind` | Add Tailwind integration |
| `npx astro add sitemap` | Add sitemap integration |
| `npx astro check` | Type-check project |
| `npx astro --help` | Show all commands |

### 2.3 Dependency Management

```bash
# Install a new package
npm install package-name

# Install as dev dependency
npm install -D package-name

# Update all packages
npm update

# Check outdated packages
npm outdated

# Audit for vulnerabilities
npm audit

# Fix vulnerabilities
npm audit fix
```

---

## 3. File Paths

### 3.1 Key Files

| File | Path |
|------|------|
| Home page | `src/pages/index.astro` |
| About page | `src/pages/about.astro` |
| Skills page | `src/pages/skills.astro` |
| Katalog page | `src/pages/katalog.astro` |
| Katalog detail | `src/pages/katalog/[slug].astro` |
| Services page | `src/pages/services.astro` |
| Blog page | `src/pages/blog.astro` |
| Blog detail | `src/pages/blog/[slug].astro` |
| Resources page | `src/pages/resources.astro` |
| Testimonials page | `src/pages/testimonials.astro` |
| Contact page | `src/pages/contact.astro` |
| 404 page | `src/pages/404.astro` |
| Base layout | `src/layouts/BaseLayout.astro` |
| Post layout | `src/layouts/PostLayout.astro` |
| Header | `src/components/Header.astro` |
| Footer | `src/components/Footer.astro` |
| Project card | `src/components/ProjectCard.astro` |
| Blog card | `src/components/BlogCard.astro` |
| Skill badge | `src/components/SkillBadge.astro` |
| Katalog filter | `src/components/KatalogFilter.tsx` |
| Content schema | `src/content/config.ts` |
| Global CSS | `src/styles/global.css` |
| Astro config | `astro.config.mjs` |
| Tailwind config | `tailwind.config.mjs` |
| TypeScript config | `tsconfig.json` |
| Package manifest | `package.json` |
| Deploy workflow | `.github/workflows/deploy.yml` |
| License | `LICENSE` |

### 3.2 Content Folders

| Folder | Purpose |
|--------|---------|
| `src/content/katalog/` | Project Markdown files |
| `src/content/blog/` | Article Markdown files |
| `public/images/projects/` | Project thumbnails |
| `public/images/blog/` | Blog cover images |
| `public/images/` | Avatar, OG image |
| `public/` | Favicon, robots.txt, cv.pdf |

### 3.3 Docs

| File | Path |
|------|------|
| Docs index | `docs/README.md` |
| Blueprint | `docs/blueprint.md` |
| Design system | `docs/design-system.md` |
| Content guide | `docs/content-guide.md` |
| Verification checklist | `docs/verification-checklist.md` |
| Cheatsheets | `docs/cheatsheets.md` |
| Deployment guide | `docs/deployment-guide.md` |
| Changelog | `docs/CHANGELOG.md` |

---

## 4. Content Commands

### 4.1 Add New Project

```bash
# 1. Create file
touch src/content/katalog/my-project.md

# 2. Edit frontmatter (see content-guide.md §3.2)

# 3. Add thumbnail
# Place at public/images/projects/my-project.png

# 4. Preview
npm run dev
# Open http://localhost:4321/katalog

# 5. Build to validate
npm run build

# 6. Commit + push
git add .
git commit -m "feat: add my-project"
git push
```

### 4.2 Add New Article

```bash
# 1. Create file
touch src/content/blog/my-article.md

# 2. Edit frontmatter (see content-guide.md §4.2)
# Start with draft: true

# 3. Add cover image (optional)
# Place at public/images/blog/my-article.png

# 4. Preview
npm run dev
# Open http://localhost:4321/blog

# 5. When ready, set draft: false

# 6. Build to validate
npm run build

# 7. Commit + push
git add .
git commit -m "content: add my-article"
git push
```

### 4.3 Validate All Content

```bash
# Build validates all frontmatter against Zod schema
npm run build

# If errors, check terminal output
# Fix frontmatter and rebuild
```

### 4.4 List All Content

```bash
# List projects
ls src/content/katalog/

# List articles
ls src/content/blog/

# Count projects
ls src/content/katalog/ | wc -l

# Count articles
ls src/content/blog/ | wc -l
```

---

## 5. Git Commands

### 5.1 Daily Commands

```bash
# Check status
git status

# Stage all changes
git add .

# Stage specific file
git add src/pages/index.astro

# Commit
git commit -m "feat: add hero section"

# Push
git push origin main

# Pull latest
git pull origin main
```

### 5.2 Commit Convention

| Type | Usage | Example |
|------|-------|---------|
| `feat:` | New feature | `feat: add katalog filter` |
| `fix:` | Bug fix | `fix: correct dark mode colors` |
| `docs:` | Documentation | `docs: update content guide` |
| `style:` | Formatting | `style: format header component` |
| `refactor:` | Restructure | `refactor: extract card component` |
| `chore:` | Config, deps | `chore: update tailwind config` |
| `content:` | New/updated content | `content: add portfolio-v2 project` |

### 5.3 Branch Commands (Optional)

```bash
# Create feature branch
git checkout -b feat/katalog-filter

# Switch back to main
git checkout main

# Merge feature branch
git merge feat/katalog-filter

# Delete feature branch
git branch -d feat/katalog-filter
```

### 5.4 Undo Commands

```bash
# Undo unstaged changes to a file
git checkout -- src/pages/index.astro

# Undo staged changes
git reset HEAD src/pages/index.astro

# Undo last commit (keep changes)
git reset --soft HEAD~1

# Undo last commit (discard changes)
git reset --hard HEAD~1

# View commit history
git log --oneline -10
```

---

## 6. Deploy Commands

### 6.1 Deploy to GitHub Pages

```bash
# 1. Commit changes
git add .
git commit -m "feat: add new content"

# 2. Push to main
git push origin main

# 3. GitHub Actions auto-deploys
# Wait 1–2 minutes

# 4. Verify
# Open https://katalogarkan.github.io
```

### 6.2 Check Deploy Status

```bash
# Open GitHub Actions
# https://github.com/katalogarkan/katalogarkan.github.io/actions

# Or via CLI (if gh installed)
gh run list
gh run view
```

### 6.3 Manual Deploy (Force)

```bash
# If Actions fails, trigger manually
git commit --allow-empty -m "chore: trigger deploy"
git push origin main
```

### 6.4 Rollback

```bash
# Revert to previous commit
git revert HEAD
git push origin main

# Or reset to specific commit (destructive)
git reset --hard <commit-hash>
git push --force origin main
```

---

## 7. Tailwind Quick Reference

### 7.1 Color Classes

| Class | Resolves To (Light) | Resolves To (Dark) |
|-------|---------------------|---------------------|
| `text-primary` | `#0969da` | `#58a6ff` |
| `bg-primary` | `#0969da` | `#58a6ff` |
| `bg-bg` | `#ffffff` | `#0d1117` |
| `bg-bg-subtle` | `#f6f8fa` | `#161b22` |
| `text-text` | `#1f2328` | `#e6edf3` |
| `text-text-muted` | `#656d76` | `#8b949e` |
| `border-border` | `#d0d7de` | `#30363d` |

**Note:** These classes use CSS variables (`var(--color-*)`) from `global.css`. Dark mode is automatic — no `dark:` prefix needed. See `design-system.md` §9 and §19.

### 7.2 Dark Mode

```html
<!-- Correct: token classes, dark mode automatic -->
<div class="bg-bg-subtle border border-border">
<p class="text-text">
<p class="text-text-muted">

<!-- Wrong: hardcoded dark variant -->
<div class="bg-white dark:bg-gray-900">
```

**Exception:** `prose dark:prose-invert` for Markdown content (typography plugin does not read CSS variables).

### 7.3 Spacing

| Class | Value |
|-------|-------|
| `p-1` / `m-1` / `gap-1` | 4px |
| `p-2` / `m-2` / `gap-2` | 8px |
| `p-4` / `m-4` / `gap-4` | 16px |
| `p-6` / `m-6` / `gap-6` | 24px |
| `p-8` / `m-8` / `gap-8` | 32px |
| `p-12` / `m-12` / `gap-12` | 48px |
| `p-16` / `m-16` / `gap-16` | 64px |

### 7.4 Responsive

```html
<!-- Mobile first -->
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3">
<nav class="hidden md:flex">
<button class="md:hidden">
```

### 7.5 Common Patterns

```html
<!-- Container -->
<div class="max-w-6xl mx-auto px-4 md:px-8">

<!-- Card -->
<div class="bg-bg-subtle border border-border rounded-lg p-6 shadow-md hover:shadow-lg transition-shadow">

<!-- Button primary -->
<button class="bg-primary text-white font-medium px-4 py-2 rounded-md hover:bg-primary-hover focus-visible:ring-2 focus-visible:ring-primary focus-visible:ring-offset-2 transition-colors">

<!-- Badge -->
<span class="inline-flex items-center px-2 py-1 rounded-full text-xs font-medium bg-primary/10 text-primary">

<!-- Section -->
<section class="py-12 md:py-16">
  <div class="max-w-6xl mx-auto px-4 md:px-8">
    <h2 class="text-2xl font-bold mb-8">Title</h2>
  </div>
</section>
```

---

## 8. Astro Quick Reference

### 8.1 Page Template

```astro
---
import BaseLayout from '../layouts/BaseLayout.astro';

const title = 'Page Title';
const description = 'Page description.';
---

<BaseLayout title={title} description={description}>
  <h1>{title}</h1>
  <p>{description}</p>
</BaseLayout>
```

### 8.2 Content Collection Query

```astro
---
import { getCollection } from 'astro:content';

// Get all projects
const projects = await getCollection('katalog');

// Get featured only
const featured = await getCollection('katalog', ({ data }) => data.featured === true);

// Get published blog (not draft)
const posts = await getCollection('blog', ({ data }) => data.draft !== true);

// Sort by date
const sorted = projects.sort((a, b) => b.data.date.valueOf() - a.data.date.valueOf());
---
```

### 8.3 Dynamic Route

```astro
---
import { getCollection } from 'astro:content';

export async function getStaticPaths() {
  const projects = await getCollection('katalog');
  return projects.map(project => ({
    params: { slug: project.slug },
    props: { project },
  }));
}

const { project } = Astro.props;
const { Content } = await project.render();
---

<h1>{project.data.title}</h1>
<Content />
```

### 8.4 React Island

```astro
---
import KatalogFilter from '../components/KatalogFilter.tsx';
import { getCollection } from 'astro:content';

const projects = await getCollection('katalog');
---

<KatalogFilter projects={projects} client:load />
```

### 8.5 Hydration Directives

| Directive | When to Use |
|-----------|-------------|
| `client:load` | Immediately (filter) |
| `client:idle` | After page load |
| `client:visible` | When scrolled into view |
| `client:only="react"` | Skip SSR (React-only) — requires framework name |

---

## 9. Content Schema Quick Reference

### 9.1 Katalog Frontmatter

```yaml
---
title: "Project Name"
description: "Short description (≤160 chars)."
techStack: ["Astro", "Tailwind"]
thumbnail: "/images/projects/project.png"
demoUrl: "https://example.com"
repoUrl: "https://github.com/katalogarkan/project"
category: "web-app"
featured: true
date: 2026-10-01
---
```

**Required:** `title`, `description`, `techStack`, `thumbnail`, `category`, `date`
**Optional:** `demoUrl`, `repoUrl`, `featured`
**Category values:** `web-app` / `landing-page` / `api` / `mobile`

### 9.2 Blog Frontmatter

```yaml
---
title: "Article Title"
date: 2026-10-01
description: "Short summary (≤160 chars)."
category: "tutorial"
tags: ["astro", "tailwind"]
draft: false
coverImage: "/images/blog/article.png"
---
```

**Required:** `title`, `date`, `description`, `category`
**Optional:** `tags`, `draft`, `coverImage`
**Category values:** `tutorial` / `tips` / `notes`

### 9.3 Date Format

Always `YYYY-MM-DD`:
- ✅ `2026-10-01`
- ❌ `10/01/2026`
- ❌ `October 1, 2026`

---

## 10. Common Patterns

### 10.1 New Page

```bash
# 1. Create file
touch src/pages/my-page.astro

# 2. Add content
# See §8.1

# 3. Add to nav (if needed)
# Edit src/components/Header.astro

# 4. Test
npm run dev
```

### 10.2 New Component

```bash
# 1. Create file
touch src/components/MyComponent.astro

# 2. Add content
# Use props, no React

# 3. Import in page
# import MyComponent from '../components/MyComponent.astro';
```

### 10.3 New React Island

```bash
# 1. Create file
touch src/components/MyIsland.tsx

# 2. Add React component
# Use useState, useEffect, etc.

# 3. Import with client directive
# <MyIsland client:load />
```

### 10.4 Add Image

```bash
# 1. Place in public/images/
cp ~/Downloads/my-image.png public/images/projects/my-image.png

# 2. Reference in frontmatter
# thumbnail: "/images/projects/my-image.png"

# 3. Or in Markdown
# ![Alt text](/images/projects/my-image.png)
```

---

## 11. Environment

### 11.1 Versions

| Tool | Version |
|------|---------|
| Node.js | 20+ |
| npm | 10+ |
| Astro | latest |
| Tailwind | latest |

### 11.2 Check Versions

```bash
node --version
npm --version
npx astro --version
```

### 11.3 Environment Variables

**None required at launch.** Formspree endpoint is hardcoded in `contact.astro` (public, safe).

If needed in future:

```bash
# .env (gitignored)
PUBLIC_FORMSPREE_ID=your-id
```

```astro
---
const formspreeId = import.meta.env.PUBLIC_FORMSPREE_ID;
---
```

---

## 12. URLs

### 12.1 Local

| Service | URL |
|---------|-----|
| Dev server | http://localhost:4321 |
| Home | http://localhost:4321/ |
| Katalog | http://localhost:4321/katalog |
| Blog | http://localhost:4321/blog |

### 12.2 Live

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
| Sitemap | https://katalogarkan.github.io/sitemap-index.xml |
| Robots | https://katalogarkan.github.io/robots.txt |

### 12.3 Repository

| Resource | URL |
|----------|-----|
| Repo | https://github.com/katalogarkan/katalogarkan.github.io |
| Actions | https://github.com/katalogarkan/katalogarkan.github.io/actions |
| Settings | https://github.com/katalogarkan/katalogarkan.github.io/settings |
| Pages settings | https://github.com/katalogarkan/katalogarkan.github.io/settings/pages |

---

## 13. Troubleshooting

### 13.1 Build Errors

| Error | Fix |
|-------|-----|
| `Cannot find module 'astro'` | `npm install` |
| `Node version too old` | Install Node 20+ |
| `Frontmatter validation failed` | Check `content-guide.md` §7.2 |
| `Cannot find package '@astrojs/react'` | `npm install @astrojs/react react react-dom` |
| `Tailwind classes not applied` | Check `content` paths in `tailwind.config.mjs` |
| `border-border` class not working | Check `border: { DEFAULT: ... }` in Tailwind config |

### 13.2 Runtime Errors

| Error | Fix |
|-------|-----|
| React island not hydrating | Check `client:load` directive |
| Dark mode not working | Check `darkMode: 'media'` + CSS variables in `global.css` |
| Images 404 | Check path starts with `/` and file exists in `public/` |
| Font not loading | Check Google Fonts link in `BaseLayout.astro` |
| Nav links 404 | Check route exists in `src/pages/` |
| Content not showing | Check `draft: true` (for blog) or build not run |

### 13.3 Deploy Errors

| Error | Fix |
|-------|-----|
| GitHub Pages 404 | Enable Pages in Settings → Pages → Source: GitHub Actions |
| Action fails on build | Check Node version in `deploy.yml` is 20 |
| Assets 404 on live | Check `site` in `astro.config.mjs` matches repo URL |
| Deploy stuck | Check Actions tab for error; re-run failed job |

### 13.4 Git Errors

| Error | Fix |
|-------|-----|
| `Permission denied` | Check SSH key or use HTTPS |
| `Merge conflict` | `git pull`, resolve, commit |
| `Detached HEAD` | `git checkout main` |
| `Rejected push` | `git pull --rebase`, then push |

---

## 14. One-Liners

### 14.1 Setup

```bash
# Clone + install + dev
git clone https://github.com/katalogarkan/katalogarkan.github.io.git && cd katalogarkan.github.io && npm install && npm run dev

# Update + install + dev
git pull && npm install && npm run dev

# Clean rebuild
rm -rf node_modules dist .astro && npm install && npm run build
```

### 14.2 Content

```bash
# Count projects
ls src/content/katalog/ | wc -l

# Count articles
ls src/content/blog/ | wc -l

# Find draft articles
grep -l "draft: true" src/content/blog/*.md

# List all project titles
grep "^title:" src/content/katalog/*.md
```

### 14.3 Git

```bash
# Quick commit + push
git add . && git commit -m "feat: update" && git push

# Undo last commit (keep changes)
git reset --soft HEAD~1

# View last 5 commits
git log --oneline -5
```

### 14.4 Deploy

```bash
# Trigger deploy (empty commit)
git commit --allow-empty -m "chore: trigger deploy" && git push
```

---

## 15. Documentation Links

| Resource | URL |
|----------|-----|
| Astro Docs | https://docs.astro.build |
| Tailwind Docs | https://tailwindcss.com/docs |
| Astro Content Collections | https://docs.astro.build/en/guides/content-collections/ |
| Astro GitHub Pages | https://docs.astro.build/en/guides/deploy/github/ |
| Astro React Integration | https://docs.astro.build/en/guides/integrations-guide/react/ |
| Formspree | https://formspree.io |
| Inter Font | https://fonts.google.com/specimen/Inter |
| GitHub Pages | https://pages.github.com |
| Conventional Commits | https://www.conventionalcommits.org |
| Zod | https://zod.dev |
---

*End of document.*