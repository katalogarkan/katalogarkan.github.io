# docs/README.md — katalogarkan

---

## Document Information

| Property | Value |
|----------|-------|
| Document Version | 1.1.0 |
| Project Version | 0.1.0 (Phase 1 Complete) |
| Last Updated | 2026-11-04 |
| Status | Active — Documentation Index |
| Project | Personal branding & katalog website |
| Owner | Arkan (Full Stack Web Developer) |
| Purpose | Navigate all documentation in `docs/` |

---

## Table of Contents

1. [What This Is](#1-what-this-is)
2. [Start Here](#2-start-here)
3. [Document Index](#3-document-index)
4. [Read by Role](#4-read-by-role)
5. [Read by Task](#5-read-by-task)
6. [Source of Truth](#6-source-of-truth)
7. [Document Conventions](#7-document-conventions)
8. [Document Map](#8-document-map)
9. [Relationship to Root README](#9-relationship-to-root-readme)
10. [Change Log](#10-change-log)

---

## 1. What This Is

This folder contains **planning and reference documentation** for the katalogarkan project. It is **not** the project source code — that lives in `src/`.

Every architectural decision, design token, content rule, verification check, deploy step, and demo video plan is written down here so that:

- The owner (Arkan) has a single reference for every decision.
- Future contributors can onboard without guessing.
- AI assistants can generate consistent code.
- Every change is traceable via the root `CHANGELOG.md`.

**This file (`docs/README.md`) is the index.** The project overview, setup instructions, and quick commands live in the **root** [`README.md`](../README.md) — not here.

---

## 2. Start Here

### 2.1 If You Are New

| Step | Read | Why |
|:---:|------|-----|
| 1 | [`../README.md`](../README.md) | Project overview, stack, setup |
| 2 | [`blueprint.md`](blueprint.md) §1–§4 | Context, goals, tech stack |
| 3 | [`design-system.md`](design-system.md) §2 | Design principles |
| 4 | [`cheatsheets.md`](cheatsheets.md) §2–§3 | Daily commands, file paths |

### 2.2 If You Are Ready to Build

| Step | Read | Why |
|:---:|------|-----|
| 1 | [`blueprint.md`](blueprint.md) §20 | Current phase and tasks |
| 2 | [`verification-checklist.md`](verification-checklist.md) | Definition of done for this phase |
| 3 | [`design-system.md`](design-system.md) §11 | Component patterns |
| 4 | [`cheatsheets.md`](cheatsheets.md) §8 | Copy-paste patterns |

### 2.3 If You Are Writing Content

| Step | Read | Why |
|:---:|------|-----|
| 1 | [`content-guide.md`](content-guide.md) §3–§4 | Frontmatter rules |
| 2 | [`content-guide.md`](content-guide.md) §5 | Writing guidelines |
| 3 | [`content-guide.md`](content-guide.md) §8 | Workflow |

### 2.4 If You Are Deploying

| Step | Read | Why |
|:---:|------|-----|
| 1 | [`deployment-guide.md`](deployment-guide.md) §5 | Workflow file |
| 2 | [`deployment-guide.md`](deployment-guide.md) §7 | First deploy |
| 3 | [`deployment-guide.md`](deployment-guide.md) §12 | Troubleshooting |

---

## 3. Document Index

### 3.1 Documents in `docs/`

| # | Document | Version | Purpose | Status |
|:-:|----------|:---:|---------|--------|
| 1 | [`blueprint.md`](blueprint.md) | 1.2.0 | Architecture, tech stack, 6 phases, decisions log | Approved — Source of Truth |
| 2 | [`design-system.md`](design-system.md) | 1.2.0 | Colors, typography, spacing, components, dark mode | Approved — Source of Truth |
| 3 | [`content-guide.md`](content-guide.md) | 1.1.0 | How to write katalog & blog content | Approved — Source of Truth |
| 4 | [`deployment-guide.md`](deployment-guide.md) | 1.2.0 | GitHub Pages deploy step-by-step | Approved — Source of Truth |
| 5 | [`verification-checklist.md`](verification-checklist.md) | 1.3.0 | 236 checks across 6 phases | Active — Updated Per Phase |
| 6 | [`cheatsheets.md`](cheatsheets.md) | 1.2.0 | Quick reference for daily development | Approved — Quick Reference |
| 7 | [`demo-video.md`](demo-video.md) | 1.0.0 | Demo video script and production plan | Draft — Planning |
| 8 | `README.md` | 1.1.0 | This file — docs index | Active — Documentation Index |

### 3.2 Documents at Root (not in `docs/`)

| Document | Purpose |
|----------|---------|
| [`../README.md`](../README.md) | Project overview, setup, quick commands, features |
| [`../CHANGELOG.md`](../CHANGELOG.md) | **Single source of truth** for all project changes |
| [`../LICENSE`](../LICENSE) | MIT license |
| [`../CONTRIBUTING.md`](../CONTRIBUTING.md) | Contribution guidelines |
| [`../SECURITY.md`](../SECURITY.md) | Security policy |

### 3.3 Assets

| Folder | Purpose |
|--------|---------|
| [`../screenshots/`](../screenshots/) | Architecture diagrams referenced by root README |

---

## 4. Read by Role

### 4.1 Owner (Arkan)

| Order | Document | When |
|:---:|----------|------|
| 1 | [`blueprint.md`](blueprint.md) | Planning, architecture decisions |
| 2 | [`verification-checklist.md`](verification-checklist.md) | Before marking a phase complete |
| 3 | [`cheatsheets.md`](cheatsheets.md) | Daily development |
| 4 | [`content-guide.md`](content-guide.md) | Writing projects/articles |
| 5 | [`design-system.md`](design-system.md) | Styling components |
| 6 | [`deployment-guide.md`](deployment-guide.md) | Deploying, fixing deploy errors |
| 7 | [`demo-video.md`](demo-video.md) | Recording demo video |

### 4.2 Future Contributor

| Order | Document | Why |
|:---:|----------|-----|
| 1 | [`../README.md`](../README.md) | Project overview |
| 2 | [`blueprint.md`](blueprint.md) §1–§4 | Context and stack |
| 3 | [`design-system.md`](design-system.md) | Visual language |
| 4 | [`content-guide.md`](content-guide.md) | Content rules |
| 5 | [`cheatsheets.md`](cheatsheets.md) | Commands |
| 6 | [`../CONTRIBUTING.md`](../CONTRIBUTING.md) | How to contribute |

### 4.3 AI Assistant

| Order | Document | Why |
|:---:|----------|-----|
| 1 | [`blueprint.md`](blueprint.md) | Full architecture |
| 2 | [`design-system.md`](design-system.md) | Exact tokens and patterns |
| 3 | [`content-guide.md`](content-guide.md) | Content rules |
| 4 | [`cheatsheets.md`](cheatsheets.md) | Common patterns |
| 5 | [`../CHANGELOG.md`](../CHANGELOG.md) | Current state |

---

## 5. Read by Task

| Task | Primary Doc | Secondary Doc |
|------|-------------|---------------|
| Set up local dev | [`../README.md`](../README.md) §Quick Start | [`cheatsheets.md`](cheatsheets.md) §2 |
| Build a page | [`blueprint.md`](blueprint.md) §7 | [`design-system.md`](design-system.md) §11 |
| Style a component | [`design-system.md`](design-system.md) §11 | [`cheatsheets.md`](cheatsheets.md) §5 |
| Add a color/token | [`design-system.md`](design-system.md) §3 | [`blueprint.md`](blueprint.md) §5 |
| Add a project | [`content-guide.md`](content-guide.md) §3 | [`blueprint.md`](blueprint.md) §9.1 |
| Add an article | [`content-guide.md`](content-guide.md) §4 | [`blueprint.md`](blueprint.md) §9.2 |
| Add an image | [`content-guide.md`](content-guide.md) §6 | — |
| Deploy | [`deployment-guide.md`](deployment-guide.md) | [`blueprint.md`](blueprint.md) §18 |
| Fix a deploy error | [`deployment-guide.md`](deployment-guide.md) §12 | [`cheatsheets.md`](cheatsheets.md) §13 |
| Verify a phase | [`verification-checklist.md`](verification-checklist.md) | [`blueprint.md`](blueprint.md) §21 |
| Record demo video | [`demo-video.md`](demo-video.md) | — |
| Understand a decision | [`blueprint.md`](blueprint.md) §23 | [`../CHANGELOG.md`](../CHANGELOG.md) |
| Find a command | [`cheatsheets.md`](cheatsheets.md) §2 | — |
| Fix a build error | [`cheatsheets.md`](cheatsheets.md) §13 | [`content-guide.md`](content-guide.md) §7 |

---

## 6. Source of Truth

When documents disagree, this is the priority order:

| Priority | Document | Wins For |
|:---:|----------|----------|
| 1 | [`blueprint.md`](blueprint.md) | Architecture, tech stack, decisions |
| 2 | [`design-system.md`](design-system.md) | Visual tokens, component styles |
| 3 | [`content-guide.md`](content-guide.md) | Content rules, frontmatter |
| 4 | [`deployment-guide.md`](deployment-guide.md) | Deploy process |
| 5 | [`verification-checklist.md`](verification-checklist.md) | Definition of done |
| 6 | [`cheatsheets.md`](cheatsheets.md) | Quick reference (not authoritative) |
| 7 | [`demo-video.md`](demo-video.md) | Demo video only |

### 6.1 Special Mirror Rules

These pairs **must match exactly**:

| Pair | Rule |
|------|------|
| [`blueprint.md`](blueprint.md) §18.2 ↔ [`deployment-guide.md`](deployment-guide.md) §5.2 | Deploy workflow |
| [`blueprint.md`](blueprint.md) §5.9 ↔ [`design-system.md`](design-system.md) §18 | Tailwind `@theme` |
| [`blueprint.md`](blueprint.md) §5.10 ↔ [`design-system.md`](design-system.md) §19 | Global CSS |
| [`blueprint.md`](blueprint.md) §9 ↔ [`content-guide.md`](content-guide.md) §3–§4 | Content schema |
| [`blueprint.md`](blueprint.md) §20 ↔ [`verification-checklist.md`](verification-checklist.md) §4–§9 | Phase checks |

### 6.2 Changelog

[`../CHANGELOG.md`](../CHANGELOG.md) is the **only** changelog. There is no `docs/CHANGELOG.md`. Every change to any document must be recorded there.

---

## 7. Document Conventions

### 7.1 Two Version Fields

Every document has:

| Field | Meaning |
|-------|---------|
| `Document Version` | The document's own version (bumped on edit) |
| `Project Version` | The project version at time of last edit |

### 7.2 Section Numbering

- Sections: `§1`, `§2`, …
- Subsections: `§5.9`, `§18.2`
- Cross-references use `§N` or `filename.md §N.M`

### 7.3 Status Values

| Status | Meaning |
|--------|---------|
| Approved — Source of Truth | Authoritative; do not edit without changelog entry |
| Active — Updated Per Phase | Updated as phases complete |
| Active — Updated Per Change | Updated on every change |
| Approved — Quick Reference | Convenience only, not authoritative |
| Draft — Planning | Not yet final |

### 7.4 Change Logs

Each document has a **Change Log** section at the end for document-specific revisions. Project-wide changes go in [`../CHANGELOG.md`](../CHANGELOG.md).

**Rule:** If you edit a document, update its Change Log **and** the root `CHANGELOG.md`.

### 7.5 Cross-Reference Format

| Type | Format | Example |
|------|--------|---------|
| Same doc | `§N.M` | `§5.9` |
| Other doc in `docs/` | `filename.md §N.M` | `blueprint.md` §18.2 |
| Link in `docs/` | `[text](file.md)` | [`blueprint.md`](blueprint.md) |
| Root file | `../filename` | [`../CHANGELOG.md`](../CHANGELOG.md) |
| Root README | `../README.md` | [`../README.md`](../README.md) |

---

## 8. Document Map

```
docs/
│
├── README.md ......................... This file (index)
│
├── blueprint.md ...................... What to build
│   ├── §1–§3   Project overview, goals, constraints
│   ├── §4      Tech stack
│   ├── §5      Design tokens
│   ├── §6–§8   Pages, content spec, components
│   ├── §9      Content schema
│   ├── §10     Project structure
│   ├── §11     Routing & rendering
│   ├── §12     Interactivity
│   ├── §13–§16 SEO, a11y, performance, errors
│   ├── §17–§19 Git, deploy, security
│   ├── §20     Execution phases
│   ├── §21     Acceptance criteria
│   ├── §22     Troubleshooting
│   └── §23–§27 Decisions, questions, glossary, refs, changelog
│
├── design-system.md .................. How it looks
│   ├── §1–§2   Purpose, principles
│   ├── §3–§8   Colors, typography, spacing, radius, shadow, breakpoints
│   ├── §9      Dark mode
│   ├── §10–§17 Layouts, components, icons, motion, focus, forms, images, prose
│   ├── §18     Tailwind 4 @theme reference
│   ├── §19     Global CSS reference
│   └── §20     Do & Don't
│
├── content-guide.md .................. How to write content
│   ├── §1–§2   Purpose, collections overview
│   ├── §3      Katalog content
│   ├── §4      Blog content
│   ├── §5      Writing guidelines
│   ├── §6      Images & assets
│   ├── §7      Validation & build
│   ├── §8      Workflow
│   └── §9      Troubleshooting
│
├── deployment-guide.md ............... How to deploy
│   ├── §1–§2   Purpose, architecture
│   ├── §3–§4   Prerequisites, Pages setup
│   ├── §5      GitHub Actions workflow
│   ├── §6      Astro config
│   ├── §7–§8   First deploy, subsequent deploys
│   ├── §9–§10  Verification, rollback
│   ├── §11     Custom domain
│   ├── §12     Troubleshooting
│   └── §13–§14 Security, performance
│
├── verification-checklist.md ......... How to know it's done
│   ├── §1–§3   Purpose, how to use, format
│   ├── §4      Phase 1 — Fondasi Proyek
│   ├── §5      Phase 2 — Desain & Home
│   ├── §6      Phase 3 — Halaman Statis
│   ├── §7      Phase 4 — Katalog + Filter
│   ├── §8      Phase 5 — Blog + Detail
│   ├── §9      Phase 6 — Polish & Deploy
│   └── §10     Summary + regression checks
│
├── cheatsheets.md .................... Quick reference
│   ├── §2      Daily commands
│   ├── §3      File paths
│   ├── §4–§5   Astro, Tailwind 4
│   ├── §6      Git & deploy
│   ├── §7      Design tokens
│   ├── §8      Component patterns
│   ├── §9      Content
│   ├── §10–§12 SEO, a11y, performance
│   ├── §13     Troubleshooting
│   └── §14     Decision quick reference
│
└── demo-video.md ..................... Demo video plan
    ├── §1–§4   Purpose, goals, audience, distribution
    ├── §5      Video structure
    ├── §6      Full script
    ├── §7      Shot list
    ├── §8–§10  Setup, checklist, editing
    ├── §11     Accessibility
    └── §12     Publishing
```

---

## 9. Relationship to Root README

| Root [`README.md`](../README.md) | This file (`docs/README.md`) |
|----------------------------------|------------------------------|
| Project overview | Documentation index |
| Tech stack summary | Document index |
| Quick Start | Start Here by role/task |
| Quick Commands | (links to cheatsheets) |
| Site Features | (links to blueprint) |
| Verification summary | (links to checklist) |
| Performance summary | (links to blueprint §15) |
| Documentation links | Full document map |
| License | (links to root LICENSE) |
| Contact | — |

**Rule:** Root README = project-facing (for visitors, recruiters, contributors). `docs/README.md` = documentation-facing (for navigating the docs). Do not duplicate content — link instead.

### 9.1 Root README Changes Needed

The current root `README.md` (`katalogarkan.txt`) has several inconsistencies with the current docs. These should be fixed to match:

| # | Issue | Fix |
|:-:|-------|-----|
| 1 | React badge says `19.x` | Change to `18.x` (matches blueprint §4.1) |
| 2 | Node prerequisite says `20+` | Change to `22+` (matches blueprint §3.1, deploy.yml) |
| 3 | Verification badge says `229/229` | Change to `57/236` (Phase 1 only complete) |
| 4 | Verification table says all 6 phases ✅ | Change to Phase 1 ✅, Phases 2–6 ⏳ |
| 5 | Lighthouse says `100/100/100/100` | Change to "Target: ≥ 95 (not yet measured)" — Lighthouse not run until Phase 6 |
| 6 | Troubleshooting says `Node 20` | Change to `Node 22` |
| 7 | Troubleshooting says `tailwind.config.mjs` | Change to `global.css` `@theme` (Tailwind 4) |
| 8 | Troubleshooting says `config.ts` schema | Change to `content.config.ts` |
| 9 | Architecture says `tailwind.config.mjs` maps tokens | Change to `@theme` in `global.css` |
| 10 | Architecture says `src/content/config.ts` | Change to `src/content.config.ts` |
| 11 | Project structure says `tailwind.config.mjs` | Remove — no such file in Tailwind 4 |
| 12 | Docs table lists `docs/CHANGELOG.md` | Change to root `CHANGELOG.md` |
| 13 | Quick Commands says `ls src/content/katalog/ \| wc -l` | Keep (valid) |
| 14 | Status badge says `production` | Change to `phase 1 complete` or `in development` |
| 15 | "12 Routes" says 9 static + 2 dynamic + 1 error | Correct (matches blueprint §6.1) |

**Rule:** Root README must match the current state of the project, not the target state. Update it when a phase completes.

---

## 10. Change Log

| Version | Date | Changes |
|---------|------|---------|
| 1.1.0 | 2026-11-04 | Synced with `blueprint.md` v1.2.0 after Phase 1: updated document versions; added `demo-video.md`; documented single root `CHANGELOG.md`; added document map, source of truth priority, conventions; added §9 relationship to root README + list of root README fixes needed. |
| 1.0.0 | 2026-10-26 | Initial docs index. |

---

*End of document.*