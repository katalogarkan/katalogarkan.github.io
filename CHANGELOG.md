# CHANGELOG.md — katalogarkan

---

## Document Information

| Property | Value |
|----------|-------|
| Document Version | 1.2.0 |
| Project Version | 0.5.0 (Phase 5 Complete) |
| Last Updated | 2026-11-04 |
| Status | Active — Updated Per Change |
| Format | Keep a Changelog + Semantic Versioning |
| Location | Repository root (single source of truth) |

---

## Table of Contents

1. [Purpose](#1-purpose)
2. [Versioning Scheme](#2-versioning-scheme)
3. [Change Categories](#3-change-categories)
4. [Phase-to-Version Mapping](#4-phase-to-version-mapping)
5. [Release History](#5-release-history)
6. [Unreleased](#6-unreleased)
7. [How to Update This File](#7-how-to-update-this-file)
8. [Change Log](#8-change-log)

---

## 1. Purpose

### 1.1 What This Document Is

The chronological record of **every meaningful change** to the katalogarkan project — code, content, config, docs, and documentation revisions. This file lives at the repository root and is the **single source of truth** for project history.

### 1.2 Why It Exists

| Reason | Benefit |
|--------|---------|
| Track progress | Know what's done, what's next |
| Debug regressions | Find when a bug was introduced |
| Document decisions | Understand why changes were made |
| Release notes | Share updates with visitors |
| Portfolio evidence | Show project history to recruiters |
| Single audit trail | All changes recorded in one place |

### 1.3 Relationship to Other Docs

| Document | Relationship |
|----------|--------------|
| `docs/blueprint.md` | Defines what to build (forward-looking) |
| `docs/verification-checklist.md` | Tracks whether it's built (checkboxes) |
| **`CHANGELOG.md`** (this file) | Records **every change** (backward-looking, complete audit trail) |

**Rule:** Blueprint = plan. Checklist = progress. Changelog = **all changes, including documentation changes**.

**Important:** Every change to ANY document (blueprint, design-system, content-guide, cheatsheets, deployment-guide, verification-checklist, README, CONTRIBUTING, SECURITY, LICENSE, demo-video) must be recorded here. No change is too small.

---

## 2. Versioning Scheme

### 2.1 Semantic Versioning

Format: `MAJOR.MINOR.PATCH`

| Component | Increment When | Example |
|-----------|----------------|---------|
| MAJOR | Breaking change (redesign, URL change) | `0.x.x` → `1.0.0` |
| MINOR | New feature (new page, new section) | `0.1.0` → `0.2.0` |
| PATCH | Bug fix, content update, docs | `0.1.0` → `0.1.1` |

### 2.2 Pre-1.0 Convention

Before launch (Phase 1–6), versions are `0.x.y`:

| Phase | Version Range | Meaning |
|-------|---------------|---------|
| Planning | `0.0.x` | Docs only, no code |
| Phase 1 | `0.1.0` | Foundation |
| Phase 2 | `0.2.0` | Design & Home |
| Phase 3 | `0.3.0` | Static pages |
| Phase 4 | `0.4.0` | Katalog filter |
| Phase 5 | `0.5.0` | Blog + detail |
| Phase 6 | `0.6.0` | Polish |
| Launch | `1.0.0` | Production ready |

### 2.3 Post-1.0 Convention

| Change Type | Version Bump |
|-------------|--------------|
| New article | PATCH (`1.0.0` → `1.0.1`) |
| New project | PATCH (`1.0.1` → `1.0.2`) |
| New page | MINOR (`1.0.2` → `1.1.0`) |
| Redesign | MAJOR (`1.1.0` → `2.0.0`) |
| Bug fix | PATCH |
| Doc change | PATCH |

### 2.4 Documentation-Only Changes

Documentation changes (blueprint revisions, design system updates, etc.) are versioned separately from project code but still recorded here as PATCH entries under the current unreleased version.

---

## 3. Change Categories

Every entry uses one of these categories:

| Category | Usage |
|----------|-------|
| **Added** | New feature, page, component, content, document |
| **Changed** | Modification to existing feature, document, or config |
| **Deprecated** | Feature marked for removal |
| **Removed** | Feature removed |
| **Fixed** | Bug fix, inconsistency fix, conflict resolution |
| **Security** | Vulnerability fix |
| **Docs** | Documentation change (revision, correction, restructure) |
| **Content** | New/updated project or article |

---

## 4. Phase-to-Version Mapping

| Phase | Version | Name | Key Deliverable |
|-------|---------|------|-----------------|
| — | `0.0.1` | Planning | Initial docs (blueprint, design-system, content-guide, checklist, cheatsheets, deployment-guide) |
| — | `0.0.2` | Docs Audit | Documentation consistency audit and fixes |
| — | `0.0.3` | Docs Completion | CONTRIBUTING.md, SECURITY.md, LICENSE, screenshots |
| 1 | `0.1.0` | Fondasi Proyek | Astro runs locally + deploys to GitHub Pages |
| 2 | `0.2.0` | Desain & Home | Home page complete, responsive, dark mode |
| 3 | `0.3.0` | Halaman Statis | 6 static pages + 404 complete |
| 4 | `0.4.0` | Katalog + Filter | Katalog with filter/search/sort |
| 5 | `0.5.0` | Blog + Detail | Blog + dynamic detail pages |
| 6 | `0.6.0` | Polish & Deploy | SEO, performance, final deploy |
| Launch | `1.0.0` | Production | Website live, content added |

---

## 5. Release History

### [0.5.0] — 2026-11-04 — Phase 5 Complete

**Status:** Complete — Blog & Detail pages ready.

**Added:**

| File | Purpose |
|------|---------|
| `src/layouts/PostLayout.astro` | Article layout with prose + dark mode |
| `src/components/BlogCard.astro` | Article card component |
| `src/pages/blog.astro` | Blog list page with draft filtering |
| `src/pages/blog/[slug].astro` | Dynamic route for article rendering |
| `src/pages/katalog/[slug].astro` | Dynamic route for project detail rendering |
| `src/content/blog/first-post.md` | Sample article |

**Verification:**
- Phase 5: 18/18 auto-checks passed.
- Build: 12 pages built, 0 errors, 0 warnings.

**Next:** Phase 6 — Polish & Deploy.

---

### [0.4.0] — 2026-11-04 — Phase 4 Complete

**Status:** Complete — Katalog & React Filter ready.

**Added:**

| File | Purpose |
|------|---------|
| `src/components/ProjectCard.astro` | Project card with thumbnail, title, tech badges |
| `src/components/KatalogFilter.tsx` | React island for category filter, search, and sort |
| `src/pages/katalog.astro` | Katalog list page with client:load hydration |
| `src/content/katalog/portfolio-v2.md` | Sample project |

**Changed:**

| File | Change |
|------|--------|
| `src/content.config.ts` | Fixed Zod 4 deprecation: `z.string().url()` → `z.url()` |

**Verification:**
- Phase 4: 9/9 auto-checks passed.
- Build: 9 pages built, 0 errors, 0 warnings.

**Next:** Phase 5 — Blog + Detail.

---

### [0.3.0] — 2026-11-04 — Phase 3 Complete

**Status:** Complete — 7 static pages ready.

**Added:**

| File | Purpose |
|------|---------|
| `src/pages/about.astro` | Bio, journey timeline, values, info |
| `src/pages/skills.astro` | 4 categories with progress bars |
| `src/pages/services.astro` | 3 packages, 4-step process, FAQ |
| `src/pages/resources.astro` | Grid layout with empty state |
| `src/pages/testimonials.astro` | Grid layout with empty state |
| `src/pages/contact.astro` | Formspree integration + honeypot |
| `src/pages/404.astro` | Custom error page |

**Verification:**
- Phase 3: 18/18 auto-checks passed.
- Build: 9 pages built, 0 errors, 0 warnings.

**Next:** Phase 4 — Katalog + Filter.

---

### [0.2.0] — 2026-11-04 — Phase 2 Complete

**Status:** Complete — Home & Layout ready.

**Added:**

| File | Purpose |
|------|---------|
| `src/components/Header.astro` | 9 nav links, sticky, mobile hamburger |
| `src/components/Footer.astro` | 4 columns (name, links, socials, copyright) |
| `src/components/SkillBadge.astro` | Badge with optional level and icon |
| `src/pages/index.astro` | Hero, Featured Projects, Skills, Testimonials, CTA |

**Verification:**
- Phase 2: 30/30 auto-checks passed.
- Build: 0 errors, 0 warnings.

**Next:** Phase 3 — Halaman Statis.

---

### [0.1.0] — 2026-11-01 — Phase 1 Complete

**Status:** Complete — Phase 1 foundation ready.

**Overview:**

Astro 5 + Tailwind 4 project runs locally, deploys to GitHub Pages, and passes 57/57 Phase 1 checks.

**Added:**

| File | Purpose |
|------|---------|
| `package.json` | Astro 5, React 18, Tailwind 4, `@tailwindcss/vite`, `@astrojs/react`, `@astrojs/sitemap` |
| `package-lock.json` | Locked dependencies |
| `astro.config.mjs` | `site`, React + sitemap integrations, `@tailwindcss/vite` Vite plugin |
| `tsconfig.json` | TypeScript config |
| `.gitignore` | Ignores `node_modules/`, `dist/`, `.astro/` |
| `src/styles/global.css` | `@import "tailwindcss"`, `@plugin "@tailwindcss/typography"`, `@theme` tokens, dark mode CSS variables |
| `src/layouts/BaseLayout.astro` | HTML shell, `<html lang="en">`, viewport meta, `global.css` import |
| `src/components/Header.astro` | Placeholder header |
| `src/components/Footer.astro` | Placeholder footer |
| `src/pages/index.astro` | Temporary "Hello" page |
| `src/content.config.ts` | Zod schemas for `katalog` + `blog` (Astro 5 API) |
| `src/content/katalog/` | Empty folder |
| `src/content/blog/` | Empty folder |
| `.github/workflows/deploy.yml` | Explicit GitHub Pages deploy workflow (Node 22) |
| `LICENSE` | MIT license |
| `CHANGELOG.md` | This file (root, single source of truth) |

**Changed:**

| Change | Detail |
|--------|--------|
| Astro version | 5.x (current stable) |
| Tailwind version | 4.x with `@tailwindcss/vite` (no `tailwind.config.mjs`) |
| Node version | 22 (in CI workflow and local prerequisite) |
| Content config path | `src/content.config.ts` (not `src/content/config.ts`) |

**Fixed:**

| # | Issue | Resolution |
|---|-------|------------|
| 1 | Tailwind 3 → 4 migration | Removed `@astrojs/tailwind`, added `@tailwindcss/vite` |
| 2 | Config conflict | Removed `tailwind.config.mjs`, moved tokens to `@theme` |
| 3 | Content config path | Moved to `src/content.config.ts` |
| 4 | Node version mismatch | Pinned to 22 in CI |

**Verification:**

- 57/57 Phase 1 checks passed (see `docs/verification-checklist.md` §4)
- `npm run build` succeeds
- Live site accessible at https://katalogarkan.github.io

**Next:** Phase 2 — Desain & Home.

---

### [0.0.4] — 2026-11-04 — Documentation Sync After Phase 1

**Status:** Complete — Docs only, no code changes.

**Overview:**

Full documentation rewrite to align with actual Phase 1 stack (Astro 5, Tailwind 4, Node 22). Resolved 8 critical inconsistencies found in the docs audit.

**Changed (Docs):**

| File | Change |
|------|--------|
| `docs/blueprint.md` | v1.1.0 → v1.2.0: Astro 5 + Tailwind 4, no `tailwind.config.mjs`, `src/content.config.ts`, Node 22, single root `CHANGELOG.md`, decisions #31–37 added, Phase 1 marked complete |
| `docs/deployment-guide.md` | v1.1.0 → v1.2.0: Node 22, `@tailwindcss/vite` config, new §6.3 Tailwind 4 explanation, pre-deploy checklist updated |
| `docs/design-system.md` | v1.1.0 → v1.2.0: §18 rewritten as "Tailwind 4 Theme Reference", §19 full `global.css`, removed `darkMode: 'media'`, no `tailwind.config.mjs` |
| `docs/content-guide.md` | v1.0.0 → v1.1.0: `src/content.config.ts` path, image rules (all in `public/`), rename-slug workflow, diagnostic commands |
| `docs/cheatsheets.md` | v1.1.0 → v1.2.0: Astro 5 + Tailwind 4 patterns, no `tailwind.config.mjs`, React island example, mobile menu pattern |
| `docs/verification-checklist.md` | v1.2.0 → v1.3.0: Phase 1 = 57/57, Phase 2 expanded, regression checks R.01–R.10, total 236 checks |
| `docs/Demo-Video.md` | **New** v1.0.0: 90–120s demo video script, shot list, recording setup, editing guide, publishing |

**Removed:**

| File | Reason |
|------|--------|
| `docs/CHANGELOG.md` | Duplicate — root `CHANGELOG.md` is now single source of truth |

**Fixed (Cross-Document Conflicts):**

| # | Conflict | Resolution |
|---|----------|------------|
| 1 | Astro version (5 vs 7) | Astro 5.x is current stable — docs aligned to 5 |
| 2 | Tailwind integration (`@astrojs/tailwind` vs `@tailwindcss/vite`) | `@tailwindcss/vite` for Tailwind 4 |
| 3 | `tailwind.config.mjs` vs `@theme` | CSS-first `@theme` — no `tailwind.config.mjs` |
| 4 | Content config path (`src/content/config.ts` vs `src/content.config.ts`) | `src/content.config.ts` (Astro 5 API) |
| 5 | Node version (20 vs 22) | Node 22 |
| 6 | Changelog duplication (`docs/CHANGELOG.md` vs root `CHANGELOG.md`) | Root only |
| 7 | Phase 1 verification count (46 vs 57) | 57 checks (actual) |
| 8 | `blueprint.md` §5.9 hex vs `design-system.md` `var(--color-*)` | Both now use `@theme` CSS variables |

**Verification:**

- All 8 docs present in `docs/`
- All cross-references resolve
- No conflicting config between blueprint, design-system, deployment-guide
- Total checks: 236

**Next:** Phase 2 — Desain & Home.

---

### [0.0.3] — 2026-10-27 — Documentation Completion

**Status:** Complete — Docs only, no code.

**Overview:**

Added missing documentation files and rewrote two documents for conciseness.

**Added:**

| File | Purpose |
|------|---------|
| `LICENSE` | MIT license file |
| `CONTRIBUTING.md` | Contribution guidelines |
| `SECURITY.md` | Security policy |
| `screenshots/page-structure.png` | Architecture diagram (for README) |
| `screenshots/content-flow.png` | Content flow diagram (for README) |
| `screenshots/dark-mode-architecture.png` | Dark mode diagram (for README) |

**Changed:**

| File | Change |
|------|--------|
| `CONTRIBUTING.md` | Created v1.0.0 (long) then rewritten to v1.1.0 (concise) — 13 sections → 11 |
| `SECURITY.md` | Created v1.0.0 (long) then rewritten to v1.1.0 (concise) — 12 sections → 9 |
| `README.md` | Updated architecture section to reference image files in `screenshots/` |
| `docs/CHANGELOG.md` | This file — updated to record all changes (later moved to root) |

**Verification:**

- All docs present: `CONTRIBUTING.md`, `SECURITY.md`, `LICENSE`, `screenshots/*.png`
- `CONTRIBUTING.md` v1.1.0 — all essential rules retained
- `SECURITY.md` v1.1.0 — all essential rules retained
- `README.md` — 3 architecture images referenced with descriptions

**Next:** Phase 1 — Fondasi Proyek.

---

### [0.0.2] — 2026-10-26 — Docs Audit & Consistency Fix

**Status:** Complete — Documentation consistency fixes.

**Overview:**

Full audit of all 7 documents revealed 8 inconsistencies and missing references. All documents revised to align with a single source of truth. No code written.

**Changed (Blueprint):**

- Document Info split into `Document Version` and `Project Version`
- §5.9: Tailwind config references CSS variables
- §5.10: Global CSS reference with CSS variables
- §5.2: Dark mode strategy updated
- §18.2: Deploy workflow explicit
- §18.5: GitHub Pages settings section added
- §12.2: Dark mode implementation updated
- Phase 1 tasks: references updated
- §10: `docs/` folder and `LICENSE` added
- §23: Decisions #27–30 added
- §25: "CSS Variables" added to glossary

**Changed (Design System):**

- §9: Dark mode rewritten — CSS variables
- §9.2: "How Dark Mode Works" with examples
- §9.3: CSS variable column added
- §9.4: "Never use `dark:` prefix" rule
- §18: Tailwind config updated
- §19: Global CSS reference with light + dark
- §17.1: `prose dark:prose-invert` documented as only exception

**Added (Content Guide):**

- New document (previously referenced but missing)
- §1–§10: Purpose, collections, katalog content, blog content, writing guidelines, images, validation, workflow, troubleshooting, changelog

**Changed (Cheatsheets):**

- §7.1: Color classes table with light + dark resolution
- §7.2: Dark mode examples corrected
- §8.5: `client:only="react"` fixed
- §5.2: `content:` commit type added
- §3.1: `LICENSE` and `docs/README.md` added
- §13.1: `border-border` troubleshooting added
- §13.2: Dark mode troubleshooting references CSS variables

**Changed (Verification Checklist):**

- Removed "87 unique / 221 sub-checks" terminology — all counts are "checks"
- Phase 1 expanded from 40 to 46 checks
- Phase 2 expanded from 38 to 39 checks
- Phase 6 expanded from 40 to 41 checks
- §9: Total updated to 229 checks
- §10: CSS variable check and `dark:` variant check commands added

**Changed (Deployment Guide):**

- §5.4: Rewritten — `withastro/action@v3` alternative removed
- §5.2: Note "This must match `blueprint.md` §18.2 exactly"
- §3.3: `LICENSE` added to repository structure
- §7.1: `LICENSE` added to pre-deploy checklist
- §12.2: Dark mode CSS variable troubleshooting added

**Changed (README.md):**

- Removed broken references to `docs/screenshots/*.png`
- Removed duplicate `docs/README.md` reference
- Added `docs/content-guide.md` to docs table
- Updated verification count 221 → 229
- Added `LICENSE` badge + section

**Fixed (Cross-Document Conflicts):**

| # | Conflict | Resolution |
|---|----------|------------|
| 1 | `blueprint.md` §5.1 dark colors vs `design-system.md` §18 | Tailwind config uses CSS variables |
| 2 | `border: '#d0d7de'` made `border-border` invalid | Changed to `border: { DEFAULT: ... }` |
| 3 | `blueprint.md` §18.2 vs `deployment-guide.md` §5.2 | Explicit workflow chosen |
| 4 | `content-guide.md` referenced but missing | Document created |
| 5 | `README.md` references to missing screenshots | References removed |
| 6 | `README.md` references to missing `docs/README.md` | Created |
| 7 | "87 unique / 221 sub" terminology | Removed |
| 8 | Document Info "Version" ambiguous | Split into `Document Version` and `Project Version` |

**Verification:**

- All 8 docs present in `docs/`
- All cross-references resolve
- No broken links in README
- No conflicting config
- Total checks updated to 229

**Next:** Phase 1 — Fondasi Proyek.

---

### [0.0.1] — 2026-10-26 — Planning

**Status:** Complete — Documentation only, no code.

**Overview:**

Initial planning phase. All documentation created before any code is written. Foundation for Phases 1–6.

**Added:**

| Document | Path | Purpose |
|----------|------|---------|
| Blueprint | `docs/blueprint.md` | Architecture, tech stack, 6 phases, decisions log |
| Design System | `docs/design-system.md` | Colors, typography, spacing, components |
| Verification Checklist | `docs/verification-checklist.md` | Checks across 6 phases |
| Cheatsheets | `docs/cheatsheets.md` | Quick reference for daily development |
| Deployment Guide | `docs/deployment-guide.md` | GitHub Pages deploy step-by-step |
| Changelog | `docs/CHANGELOG.md` | This file (later moved to root) |

**Decisions Locked:**

| # | Decision | Value |
|---|----------|-------|
| 1 | Framework | Astro |
| 2 | Styling | Tailwind CSS |
| 3 | Content | Astro Content Collections |
| 4 | Interactivity | React island (katalog filter only) |
| 5 | Hosting | GitHub Pages |
| 6 | Primary color | `#0969da` |
| 7 | Font | Inter |
| 8 | Dark mode | OS preference (`prefers-color-scheme`) |
| 9 | Navbar pages | 9 |
| 10 | Katalog initial content | Empty |
| 11 | Blog initial content | Empty |
| 12 | Detail pages | Yes (both katalog & blog) |
| 13 | Contact form | Formspree |
| 14 | Domain | `katalogarkan.github.io` at launch |
| 15 | Git workflow | Commit to `main` |
| 16 | Commit convention | Conventional Commits |
| 17 | Empty state | Text message |
| 18 | 404 page | Custom |
| 19 | Sitemap | Auto-generate |
| 20 | OG image | Static 1 image |
| 21 | Performance target | Lighthouse ≥ 95 |
| 22 | CV | PDF in `public/` |
| 23 | Formspree | Sign up when Phase 3 starts |
| 24 | Content language | English |
| 25 | Avatar | Placeholder first |
| 26 | Custom domain | After Phase 6 |

**Total Files Created:** 6 docs

**Next:** Phase 1 — Fondasi Proyek.

---

## 6. Unreleased

### [0.6.0] — Phase 6 — Polish & Deploy

**Status:** Not started.

**Planned:**

| Category | Item |
|----------|------|
| Added | `public/robots.txt` |
| Added | `public/images/og-default.png` |
| Added | `public/favicon.svg` |
| Added | Per-page meta tags (title, description, OG) |
| Added | `README.md` |
| Added | `docs/README.md` (docs index) |
| Changed | Sitemap integration verified |
| Changed | Lighthouse audit ≥ 95 all |

**Acceptance:**

- Lighthouse ≥ 95 all 4 categories
- Sitemap + robots.txt accessible
- README complete
- Live site verified
- Verification: 41/41 checks passed

---

### [1.0.0] — Launch

**Status:** Not started.

**Planned:**

| Category | Item |
|----------|------|
| Content | First project added to katalog |
| Content | First article published |
| Changed | Version bumped to 1.0.0 |
| Changed | Demo video recorded (see `docs/demo-video.md`) |
| Changed | Custom domain connected (if purchased) |

**Acceptance:**

- Website live with real content
- All phases complete (236/236 checks)
- Ready to share on LinkedIn

---

## 7. How to Update This File

### 7.1 When to Update

| Trigger | Action |
|---------|--------|
| **Any file change** | Add entry to Unreleased |
| Phase complete | Move entry from Unreleased → Release History |
| Significant commit | Add entry to Unreleased |
| Bug fix | Add to Fixed |
| New content | Add to Content |
| Doc change | Add to Docs |
| Config change | Add to Changed |

**Rule:** If you changed a file, you update this changelog. No exceptions.

### 7.2 Update Workflow

| # | Step | Action |
|---|------|--------|
| 1 | Open `CHANGELOG.md` (root) | — |
| 2 | Find the current Unreleased section | — |
| 3 | Add entry under correct category | Added / Changed / Fixed / Docs / Content |
| 4 | Reference which file(s) changed | e.g., "`docs/blueprint.md` §5.9" |
| 5 | When phase complete, move to Release History | Change header to `[version] — date — name` |
| 6 | Commit | `docs: update changelog for [change]` |

### 7.3 Entry Format

```markdown
### [0.2.0] — 2026-11-XX — Phase 2 Complete

**Status:** Complete.

**Added:**

- `src/components/Header.astro`: 9 nav links + hamburger
- `src/pages/index.astro`: Hero section

**Changed:**

- `src/layouts/BaseLayout.astro`: Include Header & Footer

**Verification:** 39/39 checks passed
```

### 7.4 Rules

| Rule | Detail |
|------|--------|
| **Record every change** | No change is too small |
| **Reference the file** | Always mention which file changed |
| **Reference the section** | e.g., `§5.9` when possible |
| One entry per version | Don't split |
| Chronological order | Newest at top |
| Date in `YYYY-MM-DD` | — |
| Link to phase | Reference `docs/blueprint.md` §20 |
| Include verification count | From checklist when phase completes |
| No empty categories | Omit if no changes |
| Documentation changes count | Docs changes are recorded as PATCH entries |
| Single location | Only root `CHANGELOG.md` — no `docs/CHANGELOG.md` |

---

## 8. Change Log

| Version | Date | Changes |
|---------|------|---------|
| 1.2.0 | 2026-11-04 | Updated release history for Phase 2, 3, 4, and 5 completion. Project version bumped to 0.5.0. |
| 1.1.0 | 2026-11-04 | Synced with `blueprint.md` v1.2.0 after Phase 1: documented actual Phase 1 release (0.1.0) with Astro 5 + Tailwind 4 + Node 22; added [0.0.4] documentation sync release; consolidated changelog to root only (removed `docs/CHANGELOG.md`); updated Phase 2–6 acceptance counts (39/36/25/38/41 = 236); added `demo-video.md` reference; rules updated to enforce single location. |
| 1.0.0 | 2026-11-01 | Initial root changelog reflecting Phase 1 completion (v0.1.0). |

---

*End of document.*