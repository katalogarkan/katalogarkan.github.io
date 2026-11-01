# CHANGELOG.md — katalogarkan

## Document Information

| Property | Value |
|----------|-------|
| Document Version | 1.0.0 |
| Project Version | 0.1.0 (Phase 1 Complete) |
| Last Updated | 2026-11-01 |
| Status | Active — Updated Per Change |
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

Chronological record of every meaningful change to the katalogarkan project.

---

## 2. Versioning Scheme

Format: `MAJOR.MINOR.PATCH`

### 2.1 Pre-1.0 Convention

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

### 2.2 Post-1.0 Convention

| Change Type | Version Bump |
|-------------|--------------|
| New article | PATCH |
| New project | PATCH |
| New page | MINOR |
| Redesign | MAJOR |
| Bug fix | PATCH |
| Doc change | PATCH |

---

## 3. Change Categories

| Category | Usage |
|----------|-------|
| **Added** | New feature, page, component, content, document |
| **Changed** | Modification to existing feature, document, or config |
| **Deprecated** | Feature marked for removal |
| **Removed** | Feature removed |
| **Fixed** | Bug fix, inconsistency fix, conflict resolution |
| **Security** | Vulnerability fix |
| **Docs** | Documentation change |
| **Content** | New/updated project or article |

---

## 4. Phase-to-Version Mapping

| Phase | Version | Name | Key Deliverable |
|-------|---------|------|-----------------|
| — | `0.0.1` | Planning | Initial docs |
| — | `0.0.2` | Docs Audit | Documentation consistency audit and fixes |
| — | `0.0.3` | Docs Completion | CONTRIBUTING, SECURITY, LICENSE |
| 1 | `0.1.0` | Fondasi Proyek | Astro runs locally + deploys to GitHub Pages |
| 2 | `0.2.0` | Desain & Home | Home page complete, responsive, dark mode |
| 3 | `0.3.0` | Halaman Statis | 6 static pages + 404 complete |
| 4 | `0.4.0` | Katalog + Filter | Katalog with filter/search/sort |
| 5 | `0.5.0` | Blog + Detail | Blog + dynamic detail pages |
| 6 | `0.6.0` | Polish & Deploy | SEO, performance, final deploy |
| Launch | `1.0.0` | Production | Website live, content added |

---

## 5. Release History

### [0.1.0] — 2026-11-01 — Phase 1 Complete

**Status:** Complete — Phase 1 foundation ready.

**Added:**
- `package.json` with Astro 7.4.4, React 7.1.2, Tailwind 4
- `astro.config.mjs` using `@tailwindcss/vite`
- `src/content.config.ts` for Zod validation (Astro 7 API)
- `src/styles/global.css` with `@theme` and CSS variables for dark mode
- `src/components/Header.astro` and `Footer.astro` placeholders
- `verify-phase-1.py` for automated verification
- `.github/workflows/deploy.yml` (Node 22)

**Changed:**
- Upgraded from Astro 5 to Astro 7 (fixed 8 vulnerabilities, 1 critical)
- Migrated from `@astrojs/tailwind` to `@tailwindcss/vite` (removed `tailwind.config.mjs`)

**Fixed:**
- `[WinError 2]` bug in Python verification script on Windows

**Verification:**
- 57/57 checks passed
- `npm run build` succeeds
- Live site accessible at https://katalogarkan.github.io

---

## 6. Unreleased

### Planned for Phase 2

| Category | Item |
|----------|------|
| Feature | Final Header with 9 nav links & hamburger menu |
| Feature | Final Footer with 4 columns |
| Feature | Professional Home page (Hero, CTA, featured projects) |

---

## 7. How to Update This File

### 7.1 When to Update

| Trigger | Action |
|---------|--------|
| Any file change | Add entry to Unreleased |
| Phase complete | Move entry from Unreleased → Release History |
| Bug fix | Add to Fixed |
| New content | Add to Content |
| Doc change | Add to Docs |
| Config change | Add to Changed |

### 7.2 Update Workflow

| # | Step | Action |
|---|------|--------|
| 1 | Open `CHANGELOG.md` | — |
| 2 | Find the Unreleased section | — |
| 3 | Add entry under correct category | Added / Changed / Fixed / Docs / Content |
| 4 | Reference which file(s) changed | e.g., "`blueprint.md` §5.9" |
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
| Record every change | No change is too small |
| Reference the file | Always mention which file changed |
| Reference the section | e.g., `§5.9` when possible |
| One entry per version | Don't split |
| Chronological order | Newest at top |
| Date in `YYYY-MM-DD` | — |
| Include verification count | From checklist when phase completes |
| No empty categories | Omit if no changes |

---

## 8. Change Log

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-11-01 | Initial changelog reflecting actual Phase 1 completion (v0.1.0). |