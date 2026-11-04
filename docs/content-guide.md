# katalogarkan — content-guide.md

---

## Document Information

| Property | Value |
|----------|-------|
| Document Version | 1.2.0 |
| Project Version | 0.5.0 (Phase 5 Complete) |
| Last Updated | 2026-11-04 |
| Status | Approved — Source of Truth |
| Project | Personal branding & katalog website |
| Owner | Arkan (Full Stack Web Developer) |
| Related | `blueprint.md` §9 (Content Schema), §10 (Project Structure) |
| Content Root | `src/content/katalog/`, `src/content/blog/` |
| Schema File | `src/content.config.ts` |
| Validation | Zod (via Astro Content Collections) |

---

## Table of Contents

1. [Purpose](#1-purpose)
2. [Content Collections Overview](#2-content-collections-overview)
3. [Katalog Content](#3-katalog-content)
4. [Blog Content](#4-blog-content)
5. [Writing Guidelines](#5-writing-guidelines)
6. [Images & Assets](#6-images--assets)
7. [Validation & Build](#7-validation--build)
8. [Workflow](#8-workflow)
9. [Troubleshooting](#9-troubleshooting)
10. [Change Log](#10-change-log)

---

## 1. Purpose

### 1.1 What This Document Is

The complete guide for writing, validating, and publishing content on the katalogarkan website. Covers both content collections (`katalog` for projects, `blog` for articles), frontmatter requirements, body structure, image handling, and the publish workflow.

### 1.2 Who Uses This

| Role | Usage |
|------|-------|
| Owner (Arkan) | Write new projects and articles |
| Future contributor | Understand content rules |
| AI assistant | Generate valid content files |

### 1.3 Relationship to Blueprint

| Blueprint Section | This Document |
|-------------------|---------------|
| §9 Content Schema | Full frontmatter fields + field rules + examples |
| §10 Project Structure | Image paths, file naming, folder layout |
| §11.3 Dynamic Routes | How `[slug]` is derived from filename |
| §16 Error Handling | Empty states (already handled in pages) |

**Rule:** If a field is defined in `blueprint.md` §9, this document explains how to fill it correctly. If there is a conflict, `blueprint.md` wins for schema; this document wins for writing guidance.

---

## 2. Content Collections Overview

### 2.1 Two Collections

| Collection | Directory | Purpose | Route |
|------------|-----------|---------|-------|
| `katalog` | `src/content/katalog/` | Project case studies | `/katalog/[slug]` |
| `blog` | `src/content/blog/` | Articles | `/blog/[slug]` |

### 2.2 Schema File

Single schema file for both collections:

```
src/content.config.ts
```

**Note:** Astro 5+ uses `src/content.config.ts` (not `src/content/config.ts`). The file sits at `src/` root, not inside `src/content/`.

### 2.3 File Naming & Slug Rules

| Rule | Detail |
|------|--------|
| File extension | `.md` (Markdown only — no `.mdx` at launch) |
| Filename | lowercase, hyphen-separated |
| Slug derivation | Filename without `.md` (e.g., `my-project.md` → `/katalog/my-project`) |
| One file per project/article | No nesting inside collection folders |
| No spaces or uppercase | Use `-` not `_`, lowercase only |

**Examples:**

| File | URL |
|------|-----|
| `src/content/katalog/portfolio-v2.md` | `/katalog/portfolio-v2` |
| `src/content/blog/first-post.md` | `/blog/first-post` |

### 2.4 Folder Structure

```
src/content/
├── katalog/
│   ├── portfolio-v2.md
│   ├── project-two.md
│   └── project-three.md
└── blog/
    ├── first-post.md
    └── second-article.md
```

---

## 3. Katalog Content

### 3.1 Frontmatter Fields

| Field | Type | Required | Default | Rules |
|-------|------|:---:|---------|-------|
| `title` | string | Yes | — | 3–80 chars, title case |
| `description` | string | Yes | — | 20–160 chars, one or two sentences |
| `techStack` | string[] | Yes | — | 1–10 items, official technology names |
| `thumbnail` | string | Yes | — | Path starting with `/images/projects/`, `.png` or `.webp` |
| `demoUrl` | string | No | — | Full URL, must start with `https://` |
| `repoUrl` | string | No | — | Full URL, must start with `https://` |
| `category` | enum | Yes | — | One of: `web-app`, `landing-page`, `api`, `mobile` |
| `featured` | boolean | No | `false` | `true` shows on Home (max 3 recommended) |
| `date` | date | Yes | — | `YYYY-MM-DD` format |

### 3.2 Category Values

| Value | Meaning |
|-------|---------|
| `web-app` | Full web application with interactivity |
| `landing-page` | Single-page marketing/portfolio site |
| `api` | Backend API or service |
| `mobile` | Mobile-first or PWA project |

**Rule:** Category values are case-sensitive and must match exactly. No custom categories at launch.

### 3.3 Body Structure

Recommended body sections (Markdown `##` headings):

```markdown
## Overview
What the project is, who it's for, why it exists.

## Problem
The problem this project solves.

## Solution
How the project solves it — features, approach.

## Tech Stack
Detailed breakdown of technologies used and why.

## Challenges
What was hard, what was learned.

## Links
- Demo: https://...
- Repo: https://...
```

**Rule:** Body is optional in structure but recommended for detail pages. Minimum: an `## Overview` section with 2+ paragraphs.

### 3.4 Complete Example

```markdown
---
title: "Portfolio v2"
description: "A rebuilt personal portfolio with Astro and Tailwind, featuring a filterable project katalog and dark mode."
techStack: ["Astro", "Tailwind CSS", "TypeScript", "React"]
thumbnail: "/images/projects/portfolio-v2.png"
demoUrl: "https://katalogarkan.github.io"
repoUrl: "https://github.com/katalogarkan/katalogarkan.github.io"
category: "web-app"
featured: true
date: 2026-11-01
---

## Overview

Portfolio v2 is a complete rebuild of my personal website. It serves two purposes: introduce me as a Full Stack Web Developer, and showcase projects in a filterable katalog.

## Problem

My previous portfolio was built with a heavy framework and had no way to filter or search projects. Recruiters had to scroll through a long list.

## Solution

Built with Astro for static output, Tailwind for styling, and a single React island for the katalog filter. Content is managed via Markdown files in the repo — no CMS, no database.

## Tech Stack

- **Astro 5** — static site generation
- **Tailwind CSS 4** — styling via `@theme`
- **React 18** — katalog filter island
- **TypeScript** — type safety

## Challenges

Migrating from Tailwind 3 to Tailwind 4 required moving all config from `tailwind.config.mjs` to `@theme` in `global.css`. The CSS-first approach is cleaner but less documented.

## Links

- Demo: https://katalogarkan.github.io
- Repo: https://github.com/katalogarkan/katalogarkan.github.io
```

---

## 4. Blog Content

### 4.1 Frontmatter Fields

| Field | Type | Required | Default | Rules |
|-------|------|:---:|---------|-------|
| `title` | string | Yes | — | 3–100 chars, title case |
| `date` | date | Yes | — | `YYYY-MM-DD` format |
| `description` | string | Yes | — | 20–160 chars, meta description |
| `category` | enum | Yes | — | One of: `tutorial`, `tips`, `notes` |
| `tags` | string[] | No | `[]` | 0–10 items, lowercase, hyphen-separated |
| `draft` | boolean | No | `false` | `true` hides from `/blog` and build |
| `coverImage` | string | No | — | Path starting with `/images/blog/` |

### 4.2 Category Values

| Value | Meaning |
|-------|---------|
| `tutorial` | Step-by-step guide |
| `tips` | Short advice, listicle, opinion |
| `notes` | Personal notes, learnings, TIL |

**Rule:** Category values are case-sensitive and must match exactly.

### 4.3 Body Structure

Recommended body structure:

```markdown
Opening paragraph — hook, what the article covers.

## Section 1
Content...

## Section 2
Content...

## Conclusion
Summary, takeaway, or call to action.
```

**Rules:**
- One `#` H1 is auto-generated from `title` — do NOT add `#` in the body.
- Use `##` for sections, `###` for sub-sections.
- Code blocks: use triple backticks with language (```` ```js ````, ```` ```bash ````).
- Inline code: single backticks.
- Links: `[text](url)` — prefer descriptive text over "click here".

### 4.4 Draft Workflow

| Stage | `draft` value | Visible on `/blog`? | Built? |
|-------|:---:|:---:|:---:|
| Writing | `true` | ❌ | ❌ |
| Ready to publish | `false` | ✅ | ✅ |

**Rule:** Set `draft: false` only when the article is complete and proofread. Drafts are excluded from the build, so they won't appear on the live site.

### 4.5 Complete Example

```markdown
---
title: "Migrating to Tailwind CSS 4 in Astro"
date: 2026-11-04
description: "A practical guide to moving from Tailwind 3 to Tailwind 4 in an Astro project, including the @theme directive and @tailwindcss/vite."
category: "tutorial"
tags: ["astro", "tailwind", "migration"]
draft: false
coverImage: "/images/blog/tailwind-4-migration.png"
---

Tailwind 4 moves configuration from JavaScript to CSS. If you're using Astro with Tailwind 3, here's how to migrate.

## 1. Remove `@astrojs/tailwind`

Uninstall the old integration:

```bash
npm uninstall @astrojs/tailwind
```

## 2. Install `@tailwindcss/vite`

```bash
npm install tailwindcss @tailwindcss/vite
```

## 3. Update `astro.config.mjs`

```js
import tailwindcss from '@tailwindcss/vite';

export default defineConfig({
  vite: {
    plugins: [tailwindcss()],
  },
});
```

## 4. Replace `@tailwind` directives

In `global.css`, replace:

```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

With:

```css
@import "tailwindcss";
```

## 5. Move config to `@theme`

Delete `tailwind.config.mjs`. Move colors and fonts to `@theme` in `global.css`.

## Conclusion

Tailwind 4 is CSS-first and faster to configure once you get used to `@theme`. The migration is mostly mechanical.
```

---

## 5. Writing Guidelines

### 5.1 Voice & Tone

| Rule | Detail |
|------|--------|
| Voice | First person ("I built", "I learned") |
| Tone | Professional, direct, no fluff |
| Tense | Past for completed work, present for facts |
| Person | "I" for owner, "you" for reader |

### 5.2 Formatting

| Element | Rule |
|---------|------|
| Headings | Sentence case (`## Overview`, not `## OVERVIEW`) |
| Paragraphs | 2–5 sentences max |
| Lists | Use when listing 3+ items |
| Bold | Sparingly, for key terms |
| Italic | For emphasis or titles |
| Code | Always in backticks with language tag |
| Emojis | ❌ Do not use (professional tone) |

### 5.3 SEO

| Rule | Detail |
|------|--------|
| `title` | Include primary keyword, ≤ 60 chars for search |
| `description` | Include primary keyword, 120–160 chars |
| First paragraph | Mention primary keyword naturally |
| Headings | Use `##` with relevant keywords |
| Links | Descriptive anchor text, not "click here" |

### 5.4 Language

| Rule | Detail |
|------|--------|
| Language | English only (per `blueprint.md` §3.2) |
| Spelling | American English (`color`, not `colour`) |
| Contractions | Allowed (`don't`, `it's`) |
| Numbers | Spell out 1–9, numerals for 10+ |

### 5.5 Length

| Content Type | Recommended Length |
|--------------|-------------------|
| Katalog body | 200–600 words |
| Blog article | 500–1500 words |
| Blog tips/notes | 300–800 words |

**Rule:** Long enough to be useful, short enough to be read. No filler.

---

## 6. Images & Assets

### 6.1 Locations

| Asset | Directory | Referenced as |
|-------|-----------|---------------|
| Project thumbnails | `public/images/projects/` | `/images/projects/{name}.png` |
| Blog cover images | `public/images/blog/` | `/images/blog/{name}.png` |
| Profile photo | `public/images/avatar.png` | `/images/avatar.png` |
| OG image | `public/images/og-default.png` | `/images/og-default.png` |
| CV PDF | `public/cv.pdf` | `/cv.pdf` |

**Rule:** All images live in `public/`. Reference them with a leading `/` (absolute path from site root). Never use `./` or `../`.

### 6.2 Naming Rules

| Rule | Detail |
|------|--------|
| Format | lowercase, hyphen-separated |
| Extension | `.png` (thumbnails), `.webp` (optimized photos) |
| Match slug | Image name should match the content file slug |
| No spaces | Use `-` not `_` or space |

**Example:**

| Content file | Thumbnail |
|--------------|-----------|
| `portfolio-v2.md` | `portfolio-v2.png` |
| `first-post.md` | `first-post.png` |

### 6.3 Dimensions

| Asset | Recommended Size | Max Size |
|-------|------------------|----------|
| Project thumbnail | 1200×675 (16:9) | 200KB |
| Blog cover | 1200×630 (1.91:1) | 200KB |
| Profile photo | 400×400 (1:1) | 100KB |
| OG image | 1200×630 | 200KB |

### 6.4 Alt Text

| Rule | Detail |
|------|--------|
| Always provided | Required for accessibility |
| Describe content | What the image shows, not "image of" |
| Max length | 125 chars |
| Decorative images | `alt=""` (empty) — but avoid decorative images |

**Note:** `alt` text is **not** part of frontmatter. It is written in the Markdown body when images are embedded:

```markdown
![Screenshot of the katalog filter in action](/images/projects/portfolio-v2.png)
```

The thumbnail (from frontmatter) is used in `ProjectCard` — the `alt` there is auto-generated from `title`. If you need custom alt text for the thumbnail, it is not supported at launch (see `blueprint.md` §24 Open Questions).

### 6.5 Adding Images

| # | Step | Action |
|---|------|--------|
| 1 | Prepare image | Resize to recommended dimensions, optimize (< 200KB) |
| 2 | Name it | Match the content file slug (e.g., `portfolio-v2.png`) |
| 3 | Place in folder | `public/images/projects/` or `public/images/blog/` |
| 4 | Reference in frontmatter | `thumbnail: "/images/projects/portfolio-v2.png"` |
| 5 | Commit + push | Image is served statically |

**Rule:** Do NOT put content images in `src/assets/`. This project uses `public/` only (no Astro `<Image>` optimization at launch).

---

## 7. Validation & Build

### 7.1 How Validation Works

```
1. Astro build starts
   │
   ▼
2. Astro reads all files in src/content/katalog/ and src/content/blog/
   │
   ▼
3. Each file's frontmatter is validated against the Zod schema in src/content.config.ts
   │
   ▼
4. If validation passes → page is generated
   If validation fails → build fails with error pointing to the file
```

### 7.2 Common Validation Errors

| Error | Cause | Fix |
|-------|-------|-----|
| `title` is required | Missing `title` in frontmatter | Add `title: "..."` |
| `category` must be one of ... | Invalid category value | Use one of the allowed enum values |
| `date` is not a valid date | Wrong date format | Use `YYYY-MM-DD` (no quotes needed, but allowed) |
| `techStack` must be an array | Used string instead of array | Use `techStack: ["Astro", "React"]` |
| `thumbnail` is required | Missing thumbnail | Add `thumbnail: "/images/projects/..."` |
| `description` too short | Less than 20 chars | Write a fuller description |
| `featured` must be boolean | Used string `"true"` | Use `true` (no quotes) |
| Unknown key | Typo in field name | Check schema in `content.config.ts` |

### 7.3 Pre-Commit Validation

| # | Step | Command |
|---|------|---------|
| 1 | Run build locally | `npm run build` |
| 2 | Check for errors | Look for red text in terminal |
| 3 | If errors, fix and re-run | — |
| 4 | If clean, commit | `git add . && git commit -m "content: add new project"` |

**Rule:** Never push content that fails `npm run build`. The CI will fail and the site won't deploy.

### 7.4 Schema Reference

The Zod schema lives in `src/content.config.ts`. It must match `blueprint.md` §9. If you need to add a field:

| # | Step | Action |
|---|------|--------|
| 1 | Update `src/content.config.ts` | Add field with Zod type |
| 2 | Update `blueprint.md` §9 | Document the field |
| 3 | Update this document §3 or §4 | Add field rules |
| 4 | Update existing content files | Add field or rely on default |
| 5 | Run `npm run build` | Verify all content passes |

---

## 8. Workflow

### 8.1 Add a New Project

| # | Step | Action |
|---|------|--------|
| 1 | Create file | `src/content/katalog/{slug}.md` |
| 2 | Add frontmatter | Copy from §3.4 example, fill all required fields |
| 3 | Write body | Follow §3.3 structure |
| 4 | Add thumbnail | `public/images/projects/{slug}.png` |
| 5 | Validate | `npm run build` |
| 6 | Preview | `npm run dev` → open `/katalog/{slug}` |
| 7 | Commit | `git add . && git commit -m "content: add {project name}"` |
| 8 | Push | `git push origin main` |
| 9 | Verify live | Wait 1–2 min, open `/katalog/{slug}` |

### 8.2 Add a New Article

| # | Step | Action |
|---|------|--------|
| 1 | Create file | `src/content/blog/{slug}.md` |
| 2 | Add frontmatter | Copy from §4.5 example, set `draft: true` while writing |
| 3 | Write body | Follow §4.3 structure |
| 4 | Add cover image (optional) | `public/images/blog/{slug}.png` |
| 5 | Set `draft: false` | When complete |
| 6 | Validate | `npm run build` |
| 7 | Preview | `npm run dev` → open `/blog/{slug}` |
| 8 | Commit | `git add . && git commit -m "content: publish {article title}"` |
| 9 | Push | `git push origin main` |
| 10 | Verify live | Wait 1–2 min, open `/blog/{slug}` |

### 8.3 Edit Existing Content

| # | Step | Action |
|---|------|--------|
| 1 | Open file | `src/content/{collection}/{slug}.md` |
| 2 | Edit frontmatter or body | — |
| 3 | Validate | `npm run build` |
| 4 | Preview | `npm run dev` |
| 5 | Commit | `git commit -m "content: update {slug}"` |
| 6 | Push | `git push origin main` |

### 8.4 Delete Content

| # | Step | Action |
|---|------|--------|
| 1 | Delete file | `src/content/{collection}/{slug}.md` |
| 2 | Delete image (optional) | `public/images/{collection}/{slug}.png` |
| 3 | Check for broken links | Search repo for `/katalog/{slug}` or `/blog/{slug}` |
| 4 | Validate | `npm run build` |
| 5 | Commit | `git commit -m "content: remove {slug}"` |
| 6 | Push | `git push origin main` |

**Note:** Deleting a content file removes its page. If another page links to it, that link will 404. Search for references before deleting.

### 8.5 Rename a Slug

Renaming a file changes its URL. This breaks existing links.

| # | Step | Action |
|---|------|--------|
| 1 | Rename file | `git mv src/content/{collection}/old.md src/content/{collection}/new.md` |
| 2 | Update internal links | Search for `/katalog/old` or `/blog/old` and replace |
| 3 | Rename image (optional) | `git mv public/images/.../old.png public/images/.../new.png` |
| 4 | Update frontmatter `thumbnail`/`coverImage` | If image renamed |
| 5 | Validate | `npm run build` |
| 6 | Commit | `git commit -m "content: rename {old} to {new}"` |
| 7 | Push | `git push origin main` |

**No redirects at launch** — old URL will 404. If the URL was shared publicly, consider keeping a stub file at the old slug or add a redirect later (see `blueprint.md` §24).

---

## 9. Troubleshooting

### 9.1 Build Errors

| Symptom | Cause | Fix |
|---------|-------|-----|
| Build fails on `content.config.ts` | Zod schema syntax error | Check schema syntax |
| Build fails on a specific file | Frontmatter doesn't match schema | Read error message, fix field |
| `Unknown key` error | Typo in field name | Check allowed fields in §3.1 / §4.1 |
| `Expected array, received string` | Used string for `techStack`/`tags` | Use `[...]` array syntax |
| `Invalid enum value` | Wrong category | Use exact value from §3.2 / §4.2 |
| `Invalid date` | Wrong format | Use `YYYY-MM-DD` |

### 9.2 Content Not Appearing

| Symptom | Cause | Fix |
|---------|-------|-----|
| Article not on `/blog` | `draft: true` | Set `draft: false` |
| Project not on Home | `featured: false` | Set `featured: true` |
| Page 404 after deploy | File not committed | `git status`, commit, push |
| Page 404 locally | Dev server cache | Restart `npm run dev` |
| Image not showing | Wrong path | Check `/images/...` not `./images/...` |
| Image not showing | Wrong folder | Check `public/images/projects/` vs `public/images/blog/` |

### 9.3 Slug Issues

| Symptom | Cause | Fix |
|---------|-------|-----|
| URL has uppercase | Filename has uppercase | Rename file lowercase |
| URL has spaces | Filename has spaces | Rename with hyphens |
| URL has `_` | Filename has underscore | Rename with hyphens |
| `[slug]` page not generated | `getStaticPaths` didn't pick up file | Check file is `.md` in correct collection |

### 9.4 Diagnostic Commands

```bash
# Check build (validates all content)
npm run build

# Check dev server (preview content)
npm run dev

# List content files
ls src/content/katalog/
ls src/content/blog/

# Check git status (uncommitted content)
git status

# Find references to a slug
grep -r "old-slug" src/
```

---

## 10. Change Log

| Version | Date | Changes |
|---------|------|---------|
| 1.2.0 | 2026-11-04 | Synced with `blueprint.md` v1.3.0 after Phase 5: `Project Version` bumped to 0.5.0; examples updated to match actual Phase 5 content (`portfolio-v2.md`, `first-post.md`); file naming examples corrected; image naming examples aligned with real slugs; no structural changes to schema or writing rules. |
| 1.1.0 | 2026-11-04 | Synced with `blueprint.md` v1.2.0: schema path updated to `src/content.config.ts` (Astro 5 API); examples updated to Astro 5 + Tailwind 4; image rules clarified (all images in `public/`, no `src/assets/`); added rename-slug workflow; added diagnostic commands. |
| 1.0.0 | 2026-10-26 | Initial content guide. |

---

*End of document.*