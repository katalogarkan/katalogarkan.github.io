# katalogarkan — content-guide.md

---

## Document Information

| Property | Value |
|----------|-------|
| Document Version | 1.0.0 |
| Project Version | 0.0.1 (Planning) |
| Last Updated | 2026-10-26 |
| Status | Approved — Source of Truth |
| Project | Personal branding & katalog website |
| Owner | Arkan (Full Stack Web Developer) |
| Related | `blueprint.md` §9 (Content Schema), `cheatsheets.md` §9 |
| Collections | `katalog`, `blog` |
| Content Format | Markdown + YAML frontmatter |
| Content Language | English |

---

## Table of Contents

1. [Purpose](#1-purpose)
2. [Content Philosophy](#2-content-philosophy)
3. [Collection Overview](#3-collection-overview)
4. [Katalog Content Guide](#4-katalog-content-guide)
5. [Blog Content Guide](#5-blog-content-guide)
6. [Markdown Writing Rules](#6-markdown-writing-rules)
7. [Image Guidelines](#7-image-guidelines)
8. [Writing Style](#8-writing-style)
9. [Validation & Troubleshooting](#9-validation--troubleshooting)
10. [Content Workflow](#10-content-workflow)
11. [Change Log](#11-change-log)

---

## 1. Purpose

### 1.1 What This Document Is

The complete guide for writing and publishing content on the katalogarkan website. Covers frontmatter requirements, Markdown syntax, image handling, writing style, and the publish workflow for both the `katalog` and `blog` collections.

### 1.2 Who Uses This

| Role | Usage |
|------|-------|
| Owner (Arkan) | Reference when writing projects and articles |
| Future contributor | Onboarding — understand content rules |
| AI assistant | Generate valid content that passes Zod validation |

### 1.3 Relationship to Other Docs

| Document | Relationship |
|----------|--------------|
| `blueprint.md` §9 | Defines the Zod schema (source of truth for fields) |
| `cheatsheets.md` §9 | Quick-reference frontmatter summary |
| `design-system.md` §17 | Prose styling for rendered Markdown |
| This document | Full writing guide, examples, and workflow |

**Rule:** If a field is not in `blueprint.md` §9, it does not exist. Do not invent fields.

---

## 2. Content Philosophy

| # | Principle | Application |
|---|-----------|-------------|
| 1 | **Honest** | No fake projects, no placeholder testimonials. Empty state is better than fake content. |
| 2 | **Concise** | Descriptions ≤ 160 characters (SEO-friendly). |
| 3 | **Useful** | Every article teaches something specific. |
| 4 | **Accurate** | Tech stack lists real technologies used. |
| 5 | **Maintainable** | Markdown in repo, no CMS, no database. |
| 6 | **English** | All content in English at launch. |

---

## 3. Collection Overview

### 3.1 Two Collections

| Collection | Directory | Purpose | Route |
|------------|-----------|---------|-------|
| `katalog` | `src/content/katalog/` | Project showcase | `/katalog`, `/katalog/[slug]` |
| `blog` | `src/content/blog/` | Articles | `/blog`, `/blog/[slug]` |

### 3.2 File Naming

| Rule | Detail |
|------|--------|
| Format | `kebab-case.md` |
| Example (katalog) | `personal-portfolio-v2.md` |
| Example (blog) | `astro-content-collections-guide.md` |
| Slug source | Filename (without `.md`) becomes the URL slug |
| Rule | Lowercase, hyphens only, no spaces, no uppercase |

**Slug rules:**

| Valid | Invalid |
|-------|---------|
| `my-project.md` | `My Project.md` |
| `astro-tips-2026.md` | `Astro_Tips_2026.md` |
| `api-v2.md` | `api v2.md` |

---

## 4. Katalog Content Guide

### 4.1 Frontmatter Fields

Source of truth: `blueprint.md` §9.1.

| Field | Type | Required | Default | Rules |
|-------|------|:---:|---------|-------|
| `title` | string | Yes | — | Project name, 3–60 chars |
| `description` | string | Yes | — | 1–2 lines, ≤ 160 chars |
| `techStack` | string[] | Yes | — | 1–8 technologies, exact names |
| `thumbnail` | string | Yes | — | Path starting with `/images/projects/` |
| `demoUrl` | string | No | — | Must start with `https://` |
| `repoUrl` | string | No | — | Must start with `https://` |
| `category` | enum | Yes | — | `web-app` / `landing-page` / `api` / `mobile` |
| `featured` | boolean | No | `false` | `true` shows on Home |
| `date` | date | Yes | — | Format `YYYY-MM-DD` |

### 4.2 Category Values

| Value | Meaning | Example |
|-------|---------|---------|
| `web-app` | Full application with multiple features | Dashboard, SaaS, admin panel |
| `landing-page` | Single-page marketing site | Product launch page |
| `api` | Backend API or service | REST API, GraphQL server |
| `mobile` | Mobile application | React Native app |

**Rule:** Pick exactly one. Do not invent new categories.

### 4.3 Complete Example

```markdown
---
title: "Personal Portfolio v2"
description: "A fast, accessible portfolio built with Astro and Tailwind CSS."
techStack: ["Astro", "Tailwind CSS", "TypeScript"]
thumbnail: "/images/projects/portfolio-v2.png"
demoUrl: "https://portfolio.example.com"
repoUrl: "https://github.com/katalogarkan/portfolio-v2"
category: "web-app"
featured: true
date: 2026-10-01
---

## Overview

A personal portfolio rebuilt from scratch with Astro. The goal was to replace
a heavy React SPA with a static site that loads in under 1 second.

## Problem

The old portfolio used Create React App and shipped 400KB of JavaScript.
Lighthouse performance score was 62.

## Solution

Rebuilt with Astro + Tailwind CSS. Only one React island (contact form).
All other pages are static HTML.

## Tech Decisions

- **Astro** for static generation and content collections
- **Tailwind CSS** for utility-first styling
- **TypeScript** for type safety

## Results

- Lighthouse Performance: 99
- Total JS: 12KB gzipped
- Build time: 8 seconds

## Links

- [Live Demo](https://portfolio.example.com)
- [Source Code](https://github.com/katalogarkan/portfolio-v2)
```

### 4.4 Body Structure (Recommended)

| Section | Content |
|---------|---------|
| Overview | What the project is, in 1 paragraph |
| Problem | What problem it solves |
| Solution | How it solves it |
| Tech Decisions | Why each technology was chosen |
| Results | Metrics, outcomes (if available) |
| Links | Demo + repo (if not in frontmatter) |

**Rule:** Sections are recommended, not required. A short project can have only Overview + Links.

### 4.5 Tech Stack Naming

Use exact, conventional names:

| Correct | Incorrect |
|---------|-----------|
| `"Astro"` | `"astro"`, `"Astro.js"` |
| `"Tailwind CSS"` | `"tailwind"`, `"TailwindCSS"` |
| `"TypeScript"` | `"ts"`, `"typescript"` |
| `"React"` | `"react.js"` |
| `"Node.js"` | `"node"`, `"NodeJS"` |
| `"PostgreSQL"` | `"postgres"`, `"Postgres"` |

---

## 5. Blog Content Guide

### 5.1 Frontmatter Fields

Source of truth: `blueprint.md` §9.2.

| Field | Type | Required | Default | Rules |
|-------|------|:---:|---------|-------|
| `title` | string | Yes | — | Article title, 10–80 chars |
| `date` | date | Yes | — | Format `YYYY-MM-DD` |
| `description` | string | Yes | — | Summary, ≤ 160 chars |
| `category` | enum | Yes | — | `tutorial` / `tips` / `notes` |
| `tags` | string[] | No | `[]` | 0–5 free-form tags |
| `draft` | boolean | No | `false` | `true` hides from `/blog` |
| `coverImage` | string | No | — | Path starting with `/images/blog/` |

### 5.2 Category Values

| Value | Meaning | Example |
|-------|---------|---------|
| `tutorial` | Step-by-step guide | "How to set up Astro Content Collections" |
| `tips` | Short advice, listicle | "5 Tailwind tricks I use daily" |
| `notes` | Personal notes, learnings | "What I learned rebuilding my portfolio" |

**Rule:** Pick exactly one. Do not invent new categories.

### 5.3 Complete Example

```markdown
---
title: "How to Set Up Astro Content Collections"
date: 2026-10-15
description: "A step-by-step guide to typed Markdown content in Astro."
category: "tutorial"
tags: ["astro", "typescript", "markdown"]
draft: false
coverImage: "/images/blog/astro-content-collections.png"
---

## What You'll Build

A typed content collection for blog articles, validated with Zod.

## Prerequisites

- Node.js 20+
- Astro project initialized
- Basic TypeScript knowledge

## Step 1: Create the Collection

Create `src/content/blog/` and add your first Markdown file.

```markdown
---
title: "My First Article"
date: 2026-10-01
description: "A short summary."
category: "tutorial"
---

Hello, world.
```

## Step 2: Define the Schema

Edit `src/content/config.ts`:

```ts
import { defineCollection, z } from 'astro:content';

const blog = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    date: z.date(),
    description: z.string(),
    category: z.enum(['tutorial', 'tips', 'notes']),
    tags: z.array(z.string()).default([]),
    draft: z.boolean().default(false),
    coverImage: z.string().optional(),
  }),
});

export const collections = { blog };
```

## Step 3: Query the Collection

```astro
---
import { getCollection } from 'astro:content';
const posts = await getCollection('blog', ({ data }) => !data.draft);
---
```

## Common Mistakes

- Forgetting `type: 'content'` in the collection definition
- Using `string` for `date` instead of `z.date()`
- Not filtering out drafts

## Conclusion

Content Collections give you typed Markdown with zero runtime cost.
```

### 5.4 Body Structure (Recommended)

| Section | Content |
|---------|---------|
| Intro | What the article covers, in 1–2 sentences |
| Prerequisites | What reader needs (if tutorial) |
| Main content | Steps, sections, examples |
| Conclusion | Summary, next steps |

**Rule:** Tutorials should have numbered steps. Tips should have a list. Notes can be free-form.

### 5.5 Tags

| Rule | Detail |
|------|--------|
| Format | Lowercase, hyphenated |
| Count | 0–5 tags |
| Examples | `"astro"`, `"tailwind"`, `"content-collections"` |
| Reuse | Reuse existing tags when possible |
| No synonyms | Use `"javascript"` not `"js"` |

---

## 6. Markdown Writing Rules

### 6.1 Supported Syntax

| Feature | Syntax | Example |
|---------|--------|---------|
| Heading | `## Heading` | H2 (H1 is page title, do not use in body) |
| Bold | `**bold**` | **bold** |
| Italic | `*italic*` | *italic* |
| Link | `[text](url)` | [Astro](https://astro.build) |
| Inline code | `` `code` `` | `npm run dev` |
| Code block | ` ```lang ` | See §6.2 |
| List (unordered) | `- item` | — |
| List (ordered) | `1. item` | — |
| Blockquote | `> quote` | — |
| Table | `\| a \| b \|` | See §6.3 |
| Image | `![alt](path)` | See §7 |

### 6.2 Code Blocks

Always specify the language:

````markdown
```js
const x = 1;
```
````

| Language | Tag |
|----------|-----|
| JavaScript | `js` |
| TypeScript | `ts` |
| Astro | `astro` |
| HTML | `html` |
| CSS | `css` |
| Bash | `bash` |
| JSON | `json` |
| YAML | `yaml` |
| Markdown | `markdown` |

**Rule:** Never use bare ` ``` ` without a language tag.

### 6.3 Tables

```markdown
| Column A | Column B |
|----------|----------|
| Value 1  | Value 2  |
| Value 3  | Value 4  |
```

**Rule:** Every table must have a header row.

### 6.4 Heading Rules

| Rule | Detail |
|------|--------|
| No H1 in body | Page title comes from frontmatter `title` |
| Start with H2 | First heading in body is `##` |
| No skipped levels | H2 → H3 → H4, never H2 → H4 |
| One topic per section | Do not mix unrelated content |

### 6.5 Links

| Rule | Detail |
|------|--------|
| Internal links | Use relative paths: `/katalog`, `/blog/some-article` |
| External links | Full URL: `https://example.com` |
| Link text | Descriptive, not "click here" |
| Open in new tab | Not in Markdown (handled by Astro for external links) |

### 6.6 Inline Code

Use inline code for:
- File names: `config.ts`
- Commands: `npm install`
- Package names: `astro`
- Variable names: `techStack`

Do not use inline code for:
- Emphasis (use bold or italic)
- Product names in prose (use plain text)

---

## 7. Image Guidelines

### 7.1 Directory Structure

| Image Type | Directory | Example |
|------------|-----------|---------|
| Project thumbnail | `public/images/projects/` | `portfolio-v2.png` |
| Blog cover | `public/images/blog/` | `astro-content-collections.png` |
| Inline (body) image | `public/images/projects/` or `public/images/blog/` | `screenshot-1.png` |
| Avatar | `public/images/` | `avatar.png` |
| OG image | `public/images/` | `og-default.png` |

### 7.2 File Naming

| Rule | Detail |
|------|--------|
| Format | `kebab-case.png` or `kebab-case.jpg` |
| Example | `portfolio-v2.png` |
| No spaces | `my image.png` ❌ |
| No uppercase | `MyImage.png` ❌ |

### 7.3 Dimensions

| Image Type | Recommended Size | Max File Size |
|------------|------------------|---------------|
| Project thumbnail | 1200×675 (16:9) | 200KB |
| Blog cover | 1200×630 | 200KB |
| Inline image | 1200px wide max | 200KB |
| Avatar | 400×400 (square) | 100KB |
| OG image | 1200×630 | 300KB |

### 7.4 Alt Text

| Rule | Detail |
|------|--------|
| Required | Every image must have alt text |
| Descriptive | Describe what the image shows |
| No "image of" | Write the content, not "image of X" |
| Empty for decorative | `alt=""` for purely decorative images |

**Examples:**

| Good | Bad |
|------|-----|
| `alt="Portfolio homepage screenshot"` | `alt="image"` |
| `alt="Lighthouse score showing 99 performance"` | `alt="screenshot"` |
| `alt=""` (decorative divider) | `alt="divider image"` |

### 7.5 Referencing in Frontmatter

```yaml
thumbnail: "/images/projects/portfolio-v2.png"
coverImage: "/images/blog/astro-content-collections.png"
```

**Rule:** Path starts with `/` (not `./` or `../`). Path is relative to `public/`.

### 7.6 Referencing in Body

```markdown
![Portfolio homepage screenshot](/images/projects/portfolio-v2.png)
```

---

## 8. Writing Style

### 8.1 Voice

| Rule | Detail |
|------|--------|
| Person | First person for blog (`I built`, `I learned`) |
| Person | Third person for katalog (`Arkan built`, or passive `Built with`) |
| Tone | Direct, technical, no fluff |
| Tense | Past tense for completed projects, present tense for tutorials |

### 8.2 Sentence Rules

| Rule | Detail |
|------|--------|
| Length | ≤ 25 words per sentence |
| Paragraphs | ≤ 4 sentences per paragraph |
| Active voice | Prefer over passive |
| No filler | Remove "very", "really", "just", "basically" |

### 8.3 Formatting Rules

| Rule | Detail |
|------|--------|
| Lists over paragraphs | For 3+ items, use a list |
| Code over description | Show code, not just describe it |
| Tables over prose | For comparisons, use a table |
| Headings every 2–4 paragraphs | Keep sections scannable |

### 8.4 What to Avoid

| Avoid | Why |
|-------|-----|
| Marketing language | "Revolutionary", "game-changing" |
| Unverified claims | "Fastest", "best" without data |
| Placeholder content | "Lorem ipsum", "TODO" |
| Fake projects | Do not invent projects for katalog |
| Fake testimonials | Empty state is honest |

---

## 9. Validation & Troubleshooting

### 9.1 How Validation Works

Astro validates every Markdown file against the Zod schema in `src/content/config.ts` at build time. If a file fails validation, the build fails with an error message.

### 9.2 Validate All Content

```bash
npm run build
```

If validation fails, the terminal shows the file and field that failed.

### 9.3 Common Errors

| Error | Cause | Fix |
|-------|-------|-----|
| `title: Required` | Missing `title` | Add `title` to frontmatter |
| `date: Expected date, received string` | Date not in `YYYY-MM-DD` | Fix date format |
| `category: Invalid enum value` | Wrong category | Use one of the allowed values |
| `techStack: Expected array` | Not an array | Wrap in `["...", "..."]` |
| `thumbnail: Required` | Missing `thumbnail` | Add `thumbnail` path |
| `description: Required` | Missing `description` | Add `description` |
| `demoUrl: Invalid url` | Not a valid URL | Use full `https://` URL |
| `Cannot find module` | Wrong import path | Check `src/content/config.ts` |

### 9.4 Check Specific Content

```bash
# Check a single file's frontmatter
head -20 src/content/katalog/my-project.md

# List all drafts
grep -l "draft: true" src/content/blog/*.md

# List all project titles
grep "^title:" src/content/katalog/*.md

# Count projects
ls src/content/katalog/ | wc -l

# Count articles
ls src/content/blog/ | wc -l
```

### 9.5 Test Locally Before Push

```bash
# 1. Add content
# 2. Start dev server
npm run dev

# 3. Check page renders
# http://localhost:4321/katalog
# http://localhost:4321/blog

# 4. Build to validate
npm run build

# 5. If build passes, commit + push
```

---

## 10. Content Workflow

### 10.1 Add a New Project

| # | Step | Command / Action |
|---|------|------------------|
| 1 | Create file | `touch src/content/katalog/my-project.md` |
| 2 | Add frontmatter | See §4.3 |
| 3 | Add thumbnail | Place at `public/images/projects/my-project.png` |
| 4 | Write body | See §4.4 |
| 5 | Preview | `npm run dev` → `/katalog` |
| 6 | Validate | `npm run build` |
| 7 | Commit | `git add . && git commit -m "feat: add my-project"` |
| 8 | Push | `git push origin main` |
| 9 | Verify live | Wait 1–2 min, open `/katalog/my-project` |

### 10.2 Add a New Article

| # | Step | Command / Action |
|---|------|------------------|
| 1 | Create file | `touch src/content/blog/my-article.md` |
| 2 | Add frontmatter | See §5.3 |
| 3 | Add cover image (optional) | Place at `public/images/blog/my-article.png` |
| 4 | Write body | See §5.4 |
| 5 | Preview | `npm run dev` → `/blog` |
| 6 | Validate | `npm run build` |
| 7 | Commit | `git add . && git commit -m "feat: add my-article"` |
| 8 | Push | `git push origin main` |
| 9 | Verify live | Wait 1–2 min, open `/blog/my-article` |

### 10.3 Edit Existing Content

| # | Step | Action |
|---|------|--------|
| 1 | Open file | `src/content/katalog/` or `src/content/blog/` |
| 2 | Edit frontmatter or body | — |
| 3 | Preview | `npm run dev` |
| 4 | Validate | `npm run build` |
| 5 | Commit | `git add . && git commit -m "content: update my-project"` |
| 6 | Push | `git push origin main` |

### 10.4 Delete Content

| # | Step | Action |
|---|------|--------|
| 1 | Delete file | `rm src/content/katalog/my-project.md` |
| 2 | Delete thumbnail (optional) | `rm public/images/projects/my-project.png` |
| 3 | Validate | `npm run build` |
| 4 | Commit | `git add . && git commit -m "content: remove my-project"` |
| 5 | Push | `git push origin main` |

### 10.5 Unpublish an Article (Keep Draft)

| # | Step | Action |
|---|------|--------|
| 1 | Edit frontmatter | Set `draft: true` |
| 2 | Validate | `npm run build` |
| 3 | Commit | `git add . && git commit -m "content: unpublish my-article"` |
| 4 | Push | `git push origin main` |

The article disappears from `/blog` and its detail page returns 404.

### 10.6 Content Cadence

| Content Type | Suggested Frequency |
|--------------|---------------------|
| New project | When completed |
| New article | 1–2 per month |
| Update old article | When outdated |

**Rule:** Do not add placeholder content. Empty state is better than fake content.

---

## 11. Change Log

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-10-26 | Initial content guide. Covers collection overview, katalog frontmatter + example, blog frontmatter + example, Markdown rules, image guidelines, writing style, validation, troubleshooting, content workflow. |

---

*End of document.*