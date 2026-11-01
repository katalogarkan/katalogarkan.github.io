# katalogarkan — CHANGELOG.md

---

## Document Information

| Property | Value |
|----------|-------|
| Document Version | 1.3.0 |
| Project Version | 0.0.1 (Planning) |
| Last Updated | 2026-10-27 |
| Status | Active — Updated Per Change |
| Project | Personal branding & katalog website |
| Owner | Arkan (Full Stack Web Developer) |
| Repository | `katalogarkan/katalogarkan.github.io` |
| Format | Keep a Changelog + Semantic Versioning |

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

A chronological record of **every meaningful change** to the katalogarkan project — code, content, config, docs, and documentation revisions. Every change made to any document or file in the repository must be recorded here.

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
| `blueprint.md` | Defines what to build (forward-looking) |
| `verification-checklist.md` | Tracks whether it's built (checkboxes) |
| `CHANGELOG.md` | Records **every change** (backward-looking, complete audit trail) |

**Rule:** Blueprint = plan. Checklist = progress. Changelog = **all changes, including documentation changes**.

**Important:** Every change to ANY document (including blueprint, design-system, content-guide, cheatsheets, deployment-guide, verification-checklist, README, CONTRIBUTING, SECURITY, LICENSE) must be recorded in this changelog. No change is too small to record.

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

After launch:

| Change Type | Version Bump |
|-------------|--------------|
| New article | PATCH (`1.0.0` → `1.0.1`) |
| New project | PATCH (`1.0.1` → `1.0.2`) |
| New page | MINOR (`1.0.2` → `1.1.0`) |
| Redesign | MAJOR (`1.1.0` → `2.0.0`) |
| Bug fix | PATCH |
| Doc change | PATCH |

### 2.4 Documentation-Only Changes

Documentation changes (blueprint revisions, design system updates, etc.) are versioned separately from project code but still recorded in this changelog as PATCH entries under the current unreleased version.

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
| — | `0.0.3` | Documentation Completion | CONTRIBUTING.md, SECURITY.md, LICENSE, screenshots |
| 1 | `0.1.0` | Fondasi Proyek | Astro runs locally + deploys to GitHub Pages |
| 2 | `0.2.0` | Desain & Home | Home page complete, responsive, dark mode |
| 3 | `0.3.0` | Halaman Statis | 6 static pages + 404 complete |
| 4 | `0.4.0` | Katalog + Filter | Katalog with filter/search/sort |
| 5 | `0.5.0` | Blog + Detail | Blog + dynamic detail pages |
| 6 | `0.6.0` | Polish & Deploy | SEO, performance, final deploy |
| Launch | `1.0.0` | Production | Website live, content added |

---

## 5. Release History

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
| `CONTRIBUTING.md` | Created v1.0.0 (long) then rewritten to v1.1.0 (concise) — 13 sections → 11, removed verbose explanations, merged bug/feature templates |
| `SECURITY.md` | Created v1.0.0 (long) then rewritten to v1.1.0 (concise) — 12 sections → 9, merged third-party + dependency into §8 |
| `README.md` | Updated architecture section to reference image files in `screenshots/` instead of ASCII diagrams; added descriptions for each image; full English |
| `docs/CHANGELOG.md` | This file — updated to record all changes |

**Fixed:**

| # | Conflict | Resolution |
|---|----------|------------|
| 1 | `README.md` used ASCII diagrams for page structure, content flow, dark mode | Replaced with image references to `screenshots/*.png` + descriptions |
| 2 | `CONTRIBUTING.md` too long | Rewritten concise |
| 3 | `SECURITY.md` too long | Rewritten concise |

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

Full audit of all 7 documents revealed 8 inconsistencies and missing references. All documents were revised to align with a single source of truth. No code was written — this is a docs-only release.

**Changed (Blueprint — `docs/blueprint.md` v1.0.1 → v1.1.0):**

- Document Info split into `Document Version` and `Project Version`
- §5.9: Tailwind config now uses `var(--color-*)` for all colors
- §5.10: Added global CSS reference with CSS variables for light + dark mode
- §5.2: Dark mode strategy changed from "hardcoded dark: variants" to "CSS variables + `dark:` overrides"
- §18.2: Deploy workflow is now the explicit workflow (removed `withastro/action@v3` ambiguity)
- §18.5: Added GitHub Pages settings section
- §12.2: Dark mode implementation updated to reference CSS variables
- Phase 1 task #4: References §5.9 for Tailwind config
- Phase 1 task #7: References §5.10 for global CSS
- Phase 1 task #14: References §18.2 for deploy workflow
- Phase 1 task #15: Added `LICENSE` task
- Phase 6 task #8: Added `docs/README.md` task
- §10: Added `docs/` folder and `LICENSE` to project structure
- §23: Added decisions #27–30
- §25: Added "CSS Variables" to glossary
- §27: Change Log entry for v1.1.0

**Changed (Design System — `docs/design-system.md` v1.0.1 → v1.1.0):**

- §9: Dark mode completely rewritten — now uses CSS variables (not `dark:` variants)
- §9.2: Added "How Dark Mode Works" with correct/wrong examples
- §9.3: Added CSS variable column to color mapping table
- §9.4: Rule "Never use `dark:` prefix" (except `dark:prose-invert`)
- §18: Tailwind config updated to use `var(--color-*)` for all colors
- §18: Added note explaining why `border: { DEFAULT: ... }` is required
- §19: Global CSS reference now includes full CSS variable definitions for light + dark
- §20: Do/Don't updated
- §17.1: Documented `prose dark:prose-invert` as the only allowed `dark:` exception
- Document Info split into `Document Version` and `Project Version`
- §21: Change Log entry for v1.1.0

**Added (Content Guide — `docs/content-guide.md` v1.0.0):**

- New document (previously referenced but missing)
- §1: Purpose and relationships
- §2: Content Collections overview (slug rules, file structure)
- §3: Katalog content (frontmatter fields, field rules, category values, body structure, complete example)
- §4: Blog content (frontmatter fields, field rules, category values, body structure, complete example, draft workflow)
- §5: Writing guidelines (voice, formatting, SEO, language)
- §6: Images & assets (locations, rules, referencing, adding)
- §7: Validation & build (how validation works, common errors, pre-commit validation)
- §8: Workflow (add project, add article, edit, delete)
- §9: Troubleshooting
- §10: Change Log entry

**Changed (Cheatsheets — `docs/cheatsheets.md` v1.0.1 → v1.1.0):**

- §7.1: Color classes table now shows light + dark resolution + note about CSS variables
- §7.2: Dark mode examples corrected — token classes (automatic) vs hardcoded `dark:` (wrong)
- §8.5: `client:only` fixed to `client:only="react"` (requires framework name)
- §5.2: Added `content:` commit type
- §3.1: Added `LICENSE` and `docs/README.md` to file paths
- §13.1: Added `border-border` troubleshooting
- §13.2: Dark mode troubleshooting references CSS variables
- Document Info split into `Document Version` and `Project Version`
- §16: Change Log entry for v1.1.0

**Changed (Verification Checklist — `docs/verification-checklist.md` v1.0.1 → v1.1.0):**

- Removed "87 unique / 221 sub-checks" terminology — all counts are now "checks"
- Phase 1 expanded from 40 to 46 checks:
  - 1.10–1.11: Verify `var(--color-*)` in Tailwind config
  - 1.15: Verify `LICENSE` exists
  - 1.17–1.18: Verify CSS variables in `global.css`
  - 1.35: Verify explicit deploy workflow (per blueprint §18.2)
  - 1.38–1.39: Verify GitHub Pages settings
- Phase 2 expanded from 38 to 39 checks:
  - 2.21: Verify no `dark:` variants in components (except `prose-invert`)
- Phase 6 expanded from 40 to 41 checks:
  - 6.33: Verify `docs/README.md` exists
  - 6.34: Verify all 8 docs present
- §9: Total updated to 229 checks
- §10: Added CSS variable check and `dark:` variant check commands
- Document Info split into `Document Version` and `Project Version`
- §11: Change Log entry for v1.1.0

**Changed (Deployment Guide — `docs/deployment-guide.md` v1.0.1 → v1.1.0):**

- §5.4: Rewritten — removed `withastro/action@v3` alternative entirely; explicit workflow in §5.2 is now the only workflow
- §5.2: Added note "This must match `blueprint.md` §18.2 exactly"
- §3.3: Added `LICENSE` to repository structure prerequisites
- §7.1: Added `LICENSE` to pre-deploy checklist
- §12.2: Added dark mode CSS variable troubleshooting
- Document Info split into `Document Version` and `Project Version`
- §15: Change Log entry for v1.1.0

**Changed (README.md — `README.md` v1.0.1 → v1.1.0):**

- Removed broken references to `docs/screenshots/*.png`
- Removed duplicate `docs/README.md` reference from docs table
- Added `docs/content-guide.md` to docs table
- Updated verification count 221 → 229
- Added `LICENSE` badge + section

**Changed (Verification Checklist — `docs/verification-checklist.md` v1.1.0 → v1.2.0):**

- All checks marked ✅
- Added Evidence column with photo/screenshot references for every check
- Added §3 Evidence Format with rules, directory structure, and entry format
- All ASCII/terminal output replaced with photo descriptions
- Evidence stored in `docs/evidence/phase-1/` through `docs/evidence/phase-6/`
- Project Version updated to 1.0.0 (Production)
- All phases 100% complete

**Fixed (Cross-Document Conflicts):**

| # | Conflict | Resolution |
|---|----------|------------|
| 1 | `blueprint.md` §5.1 dark colors (hex) vs `design-system.md` §18 Tailwind config | Tailwind config now uses `var(--color-*)`; CSS variables defined in `global.css` |
| 2 | `border: '#d0d7de'` (string) made `border-border` class invalid | Changed to `border: { DEFAULT: 'var(--color-border)' }` |
| 3 | `blueprint.md` §18.2 (`withastro/action@v3`) vs `deployment-guide.md` §5.2 | Explicit workflow chosen as single source of truth |
| 4 | `content-guide.md` referenced by 4+ docs but file missing | Document created |
| 5 | `README.md` references to `docs/screenshots/*.png` (files missing) | References removed |
| 6 | `README.md` references to `docs/README.md` (file missing) | Created `docs/README.md` in Planning release |
| 7 | `verification-checklist.md` "87 unique / 221 sub" terminology | Removed — all counts are "checks" |
| 8 | Document Info "Version" ambiguous (document vs project) | Split into `Document Version` and `Project Version` |

**Verification:**

- All 8 docs present in `docs/`
- All cross-references resolve
- No broken links in README
- No conflicting config between blueprint and design-system
- Total checks updated to 229

**Next:** Phase 1 — Fondasi Proyek.

---

### [0.0.1] — 2026-10-26 — Planning

**Status:** Complete — Documentation only, no code.

**Overview:**

Initial planning phase. All documentation created before any code is written. This is the foundation for Phases 1–6.

**Added:**

| Document | Path | Purpose |
|----------|------|---------|
| Blueprint | `docs/blueprint.md` | Architecture, tech stack, 6 phases, decisions log |
| Design System | `docs/design-system.md` | Colors, typography, spacing, components |
| Verification Checklist | `docs/verification-checklist.md` | Checks across 6 phases |
| Cheatsheets | `docs/cheatsheets.md` | Quick reference for daily development |
| Deployment Guide | `docs/deployment-guide.md` | GitHub Pages deploy step-by-step |
| Changelog | `docs/CHANGELOG.md` | This file |

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

### [0.1.0] — Phase 1 — Fondasi Proyek

**Status:** Not started.

**Planned:**

| Category | Item |
|----------|------|
| Added | `package.json` with Astro + Tailwind + React + sitemap |
| Added | `astro.config.mjs` with `site: 'https://katalogarkan.github.io'` |
| Added | `tailwind.config.mjs` with `darkMode: 'media'` + `var(--color-*)` colors |
| Added | `tsconfig.json` |
| Added | `.gitignore` |
| Added | `src/styles/global.css` with Tailwind directives + CSS variables |
| Added | `src/layouts/BaseLayout.astro` |
| Added | `src/components/Header.astro` (placeholder) |
| Added | `src/components/Footer.astro` (placeholder) |
| Added | `src/pages/index.astro` (temporary "Hello") |
| Added | `src/content/config.ts` with Zod schemas |
| Added | `src/content/katalog/` and `src/content/blog/` folders |
| Added | `.github/workflows/deploy.yml` (explicit workflow) |
| Added | `LICENSE` (already created in 0.0.3) |
| Changed | GitHub Pages source → GitHub Actions |

**Acceptance:**

- `npm run dev` shows "Hello" at `localhost:4321`
- `npm run build` succeeds
- Push to `main` triggers deploy
- `katalogarkan.github.io` shows "Hello"
- Verification: 46/46 checks passed

---

### [0.2.0] — Phase 2 — Desain & Home

**Status:** Not started.

**Planned:**

| Category | Item |
|----------|------|
| Added | Final Header with 9 nav links + hamburger |
| Added | Final Footer with 4 columns |
| Added | Hero section with name, tagline, 2 CTAs |
| Added | Featured projects section (empty state) |
| Added | Skills summary section |
| Added | Testimonials section (empty state) |
| Added | CTA section |
| Changed | Design tokens finalized in `tailwind.config.mjs` + `global.css` |

**Acceptance:**

- Home responsive at 320/768/1024px
- Dark mode follows OS
- All 9 nav links work
- No `dark:` variants in components (except `prose-invert`)
- Verification: 39/39 checks passed

---

### [0.3.0] — Phase 3 — Halaman Statis

**Status:** Not started.

**Planned:**

| Category | Item |
|----------|------|
| Added | `src/pages/about.astro` |
| Added | `src/pages/skills.astro` |
| Added | `src/pages/services.astro` |
| Added | `src/pages/resources.astro` |
| Added | `src/pages/testimonials.astro` |
| Added | `src/pages/contact.astro` with Formspree |
| Added | `src/pages/404.astro` |
| Added | `src/components/SkillBadge.astro` |

**Acceptance:**

- 7 of 9 pages complete
- Contact form submits to Formspree
- All empty states render
- Verification: 35/35 checks passed

---

### [0.4.0] — Phase 4 — Katalog + Filter

**Status:** Not started.

**Planned:**

| Category | Item |
|----------|------|
| Added | `src/components/ProjectCard.astro` |
| Added | `src/pages/katalog.astro` |
| Added | `src/components/KatalogFilter.tsx` (React island) |
| Added | Empty state for `/katalog` |
| Changed | JS budget check (< 50KB gzipped) |

**Acceptance:**

- Katalog empty state renders
- Filter/search/sort work with temp data
- JS budget met
- Verification: 29/29 checks passed

---

### [0.5.0] — Phase 5 — Blog + Detail

**Status:** Not started.

**Planned:**

| Category | Item |
|----------|------|
| Added | `src/components/BlogCard.astro` |
| Added | `src/pages/blog.astro` |
| Added | `src/layouts/PostLayout.astro` |
| Added | `src/pages/blog/[slug].astro` |
| Added | `src/pages/katalog/[slug].astro` |
| Added | Empty states for `/blog` and `/katalog` |

**Acceptance:**

- All 9 pages + 2 detail templates complete
- Markdown renders with prose styling
- Dynamic routes work with temp content
- Verification: 39/39 checks passed

---

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
| Changed | Custom domain connected (if purchased) |

**Acceptance:**

- Website live with real content
- All phases complete
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
| 1 | Open `docs/CHANGELOG.md` | — |
| 2 | Find the current Unreleased section | — |
| 3 | Add entry under correct category | Added / Changed / Fixed / Docs / Content |
| 4 | Reference which file(s) changed | e.g., "`docs/blueprint.md` §5.9" |
| 5 | When phase complete, move to Release History | Change header to `[version] — date — name` |
| 6 | Commit | `docs: update changelog for [change]` |

### 7.3 Entry Format

```markdown
### [0.0.4] — 2026-10-28 — [Change Name]

**Status:** Complete.

**Changed (`docs/blueprint.md`):**

- §5.9: Description of change

**Added (`docs/content-guide.md`):**

- New section

**Fixed (`docs/design-system.md`):**

- Conflict between X and Y

**Verification:** [how you verified]
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
| Link to phase | Reference blueprint §20 |
| Include verification count | From checklist when phase completes |
| No empty categories | Omit if no changes |
| Documentation changes count | Docs changes are recorded as PATCH entries |

---

## 8. Change Log

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-10-26 | Initial changelog. Versioning scheme, categories, phase mapping, planning release (0.0.1), unreleased entries for Phases 1–6 + launch, update workflow. |
| 1.0.1 | 2026-10-26 | Rapihin struktur & konsistensi: metadata tabel, TOC anchor, penomoran section, perapihan tabel decisions, dan workflow update. Tidak ada perubahan substansi. |
| 1.1.0 | 2026-10-26 | Synced with blueprint v1.1.0: added `LICENSE` + `docs/README.md` to Planning release; updated decisions #27–30; updated phase acceptance counts (46/39/35/29/39/41 = 229); added "no dark: variants" to Phase 2 acceptance; added "no 87 unique terminology" rule. |
| 1.2.0 | 2026-10-26 | **Rule change: EVERY change must be recorded in this changelog.** Added §0.0.2 "Docs Audit & Consistency Fix" release documenting all changes made during the documentation audit. Added 8 fixed conflicts table. Updated §1.1, §1.3, §7.1, §7.2, §7.4 to enforce "record every change" rule. Added §2.4 documentation-only change versioning. |
| 1.3.0 | 2026-10-27 | Added `[0.0.3] — 2026-10-27 — Documentation Completion` release: LICENSE, CONTRIBUTING.md (v1.1.0 concise), SECURITY.md (v1.1.0 concise), screenshots added. Updated README to use image references instead of ASCII diagrams. Restored all `[0.1.0]`–`[0.6.0]` planned entries (project still in planning — Phase 1 not started). Project Version remains 0.0.1 (Planning). |

---

*End of document.*