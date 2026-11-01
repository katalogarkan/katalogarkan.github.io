# katalogarkan — deployment-guide.md

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
| Related | `blueprint.md` §18 (Deployment), `cheatsheets.md` §6 |
| Repository | `katalogarkan/katalogarkan.github.io` |
| Hosting | GitHub Pages |
| CI/CD | GitHub Actions |
| Node Version | 20 |
| Build Output | `dist/` |

---

## Table of Contents

1. [Purpose](#1-purpose)
2. [Deployment Architecture](#2-deployment-architecture)
3. [Prerequisites](#3-prerequisites)
4. [GitHub Pages Setup](#4-github-pages-setup)
5. [GitHub Actions Workflow](#5-github-actions-workflow)
6. [Astro Configuration](#6-astro-configuration)
7. [First Deploy](#7-first-deploy)
8. [Subsequent Deploys](#8-subsequent-deploys)
9. [Verification](#9-verification)
10. [Rollback](#10-rollback)
11. [Custom Domain](#11-custom-domain)
12. [Troubleshooting](#12-troubleshooting)
13. [Security](#13-security)
14. [Performance](#14-performance)
15. [Change Log](#15-change-log)

---

## 1. Purpose

### 1.1 What This Document Is

The step-by-step guide to deploying the katalogarkan website to GitHub Pages. Covers initial setup, ongoing deploys, rollback, custom domain, and troubleshooting.

### 1.2 Who Uses This

| Role | Usage |
|------|-------|
| Owner (Arkan) | Deploy the website, fix deploy issues |
| Future contributor | Understand deployment process |
| AI assistant | Diagnose deploy problems |

### 1.3 Relationship to Blueprint

| Blueprint §18 | This Document |
|---------------|---------------|
| Deployment summary (tables) | Step-by-step instructions |
| Config examples | Full setup + verification |
| Acceptance criteria | Troubleshooting + rollback |

**Rule:** The workflow in §5.2 of this document must match `blueprint.md` §18.2 exactly.

---

## 2. Deployment Architecture

### 2.1 Flow Diagram

```
┌──────────────────────────────────────────────────────┐
│  LOCAL MACHINE                                       │
│                                                      │
│  1. Arkan edits files                                │
│  2. git commit                                       │
│  3. git push origin main                             │
│                                                      │
└──────────────────────┬───────────────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────────────┐
│  GITHUB REPOSITORY                                   │
│                                                      │
│  4. Push triggers .github/workflows/deploy.yml       │
│                                                      │
└──────────────────────┬───────────────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────────────┐
│  GITHUB ACTIONS                                      │
│                                                      │
│  5. Checkout repo                                    │
│  6. Setup Node 20                                    │
│  7. npm ci                                           │
│  8. npm run build                                    │
│  9. Upload dist/ as artifact                         │
│  10. Deploy artifact to GitHub Pages                 │
│                                                      │
└──────────────────────┬───────────────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────────────┐
│  GITHUB PAGES CDN                                    │
│                                                      │
│  11. Serve static files                              │
│  12. https://katalogarkan.github.io                  │
│                                                      │
└──────────────────────────────────────────────────────┘
```

### 2.2 Key Properties

| Property | Value |
|----------|-------|
| Repository | `katalogarkan/katalogarkan.github.io` |
| Branch | `main` |
| Build output | `dist/` |
| Node version | 20 |
| Workflow | Explicit (see §5.2) |
| Deploy time | ~1–2 minutes |
| HTTPS | Auto-enabled |
| Cost | Free |

### 2.3 Why `katalogarkan.github.io` as Repo Name

GitHub Pages has two URL formats:

| Format | Repo Name | URL |
|--------|-----------|-----|
| User site | `{username}.github.io` | `https://{username}.github.io` |
| Project site | Any other name | `https://{username}.github.io/{repo}` |

By naming the repo `katalogarkan.github.io`, the site lives at the root URL `https://katalogarkan.github.io` — no `base` path needed in `astro.config.mjs`.

---

## 3. Prerequisites

### 3.1 Local Machine

| Requirement | Version | Check |
|-------------|---------|-------|
| Node.js | 20+ | `node --version` |
| npm | 10+ | `npm --version` |
| Git | 2.40+ | `git --version` |

### 3.2 GitHub Account

| Requirement | Status |
|-------------|--------|
| Account `katalogarkan` exists | ✅ |
| Repository `katalogarkan.github.io` exists | ✅ |
| Repo is Public | ✅ (required for free GitHub Pages) |
| GitHub Pages enabled | ⚠️ Must be enabled in Settings |

### 3.3 Repository Structure

Before first deploy, the repo must contain:

| File | Purpose |
|------|---------|
| `package.json` | Dependencies |
| `astro.config.mjs` | Astro config with `site` |
| `.github/workflows/deploy.yml` | Deploy workflow |
| `src/pages/index.astro` | At least one page |
| `LICENSE` | MIT license |

---

## 4. GitHub Pages Setup

### 4.1 Enable GitHub Pages

| # | Step | Action |
|---|------|--------|
| 1 | Open repository | `https://github.com/katalogarkan/katalogarkan.github.io` |
| 2 | Click **Settings** | Top navigation |
| 3 | Click **Pages** | Left sidebar |
| 4 | Under **Build and deployment** → **Source** | Select **GitHub Actions** |
| 5 | Save | (Auto-saves) |

**Important:** Do NOT select "Deploy from a branch". Select **GitHub Actions** — the workflow handles the build.

### 4.2 Verify Pages Settings

| Setting | Expected Value |
|---------|----------------|
| Source | GitHub Actions |
| Custom domain | (empty at launch) |
| Enforce HTTPS | ✅ (default) |

### 4.3 Check Workflow Permissions

| # | Step | Action |
|---|------|--------|
| 1 | Settings → **Actions** → **General** | — |
| 2 | Under **Workflow permissions** | Select **Read and write permissions** |
| 3 | Save | — |

**Why:** The deploy workflow needs `pages: write` and `id-token: write` permissions. These are declared in `deploy.yml`, but the repo-level setting must allow them.

---

## 5. GitHub Actions Workflow

### 5.1 File Location

```
.github/workflows/deploy.yml
```

### 5.2 Complete Workflow (Explicit — Single Source of Truth)

This must match `blueprint.md` §18.2 exactly.

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
          node-version: 20
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

### 5.3 Workflow Breakdown

| Step | Purpose |
|------|---------|
| `on.push.branches: [main]` | Trigger on push to main |
| `on.workflow_dispatch` | Allow manual trigger |
| `permissions` | Read repo, write Pages, OIDC token |
| `concurrency` | One deploy at a time |
| `checkout` | Clone repo |
| `setup-node` | Install Node 20 + cache npm |
| `npm ci` | Install exact deps from `package-lock.json` |
| `npm run build` | Build Astro → `dist/` |
| `upload-pages-artifact` | Package `dist/` for Pages |
| `deploy-pages` | Deploy artifact to Pages CDN |

### 5.4 Why Not `withastro/action@v3`

The official Astro action is simpler but hides the build steps. The explicit workflow above is preferred because:

| Reason | Detail |
|--------|--------|
| Transparency | Every step is visible in the log |
| Debuggability | If a step fails, you see exactly which one |
| Control | Easy to add caching, env vars, or extra build steps |
| Learning | Understand what Astro's action does under the hood |

**No alternative workflow is provided in this document.** The explicit workflow in §5.2 is the single source of truth.

---

## 6. Astro Configuration

### 6.1 Required Config

```js
// astro.config.mjs
import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';
import react from '@astrojs/react';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://katalogarkan.github.io',
  integrations: [tailwind(), react(), sitemap()],
});
```

### 6.2 Why `site` Is Required

| Feature | Without `site` | With `site` |
|---------|----------------|-------------|
| Sitemap | Fails | Works |
| Canonical URLs | Missing | Correct |
| OG image URLs | Broken | Correct |
| RSS feed (future) | Fails | Works |

**Rule:** `site` must match the live URL exactly, no trailing slash.

### 6.3 No `base` Needed

Because the repo is named `katalogarkan.github.io`, the site is served at the root (`/`). No `base` config needed.

**If repo name were different** (e.g., `my-website`), you would need:

```js
export default defineConfig({
  site: 'https://katalogarkan.github.io',
  base: '/my-website',
  // ...
});
```

**Not applicable here.**

---

## 7. First Deploy

### 7.1 Pre-Deploy Checklist

| # | Check | Done |
|---|-------|:---:|
| 1 | `npm run build` succeeds locally | ☐ |
| 2 | `dist/` folder created | ☐ |
| 3 | `astro.config.mjs` has `site` | ☐ |
| 4 | `.github/workflows/deploy.yml` exists and matches §5.2 | ☐ |
| 5 | GitHub Pages source = GitHub Actions | ☐ |
| 6 | Workflow permissions = Read and write | ☐ |
| 7 | Repo is Public | ☐ |
| 8 | `LICENSE` file exists | ☐ |

### 7.2 Deploy Steps

| # | Step | Command |
|---|------|---------|
| 1 | Stage all files | `git add .` |
| 2 | Commit | `git commit -m "chore: initial deploy"` |
| 3 | Push | `git push origin main` |
| 4 | Open Actions tab | `https://github.com/katalogarkan/katalogarkan.github.io/actions` |
| 5 | Wait for workflow | ~1–2 minutes |
| 6 | Check green check | ✅ |
| 7 | Open live URL | `https://katalogarkan.github.io` |

### 7.3 What to Expect

| Time | What Happens |
|------|--------------|
| 0s | Push received, workflow queued |
| ~10s | Workflow starts (`build` job) |
| ~30s | Checkout + Node setup + npm ci |
| ~60s | Astro build completes |
| ~70s | Artifact uploaded |
| ~80s | `deploy` job starts |
| ~90s | Deploy completes |
| ~120s | Live URL serves new content |

**First deploy may take longer** (2–3 min) due to cache warming.

---

## 8. Subsequent Deploys

### 8.1 Normal Workflow

```bash
# 1. Make changes
# 2. Test locally
npm run dev

# 3. Build to verify
npm run build

# 4. Commit + push
git add .
git commit -m "feat: add new project"
git push origin main

# 5. Wait 1–2 min
# 6. Verify live
```

### 8.2 What Triggers a Deploy

| Trigger | Deploys? |
|---------|:---:|
| Push to `main` | ✅ |
| Push to other branch | ❌ |
| Pull request | ❌ |
| Manual `workflow_dispatch` | ✅ |
| Empty commit to `main` | ✅ |

### 8.3 Deploy Frequency

| Content Type | Frequency |
|--------------|-----------|
| New project | When added |
| New article | When published |
| Code change | When committed |
| Config change | When committed |

**No limit** on deploys — GitHub Actions free tier allows unlimited minutes for public repos.

---

## 9. Verification

### 9.1 After Deploy

| # | Check | Method |
|---|-------|--------|
| 1 | Action completed with green check | Actions tab |
| 2 | Live URL loads | Open in browser |
| 3 | Home page shows latest content | Visual |
| 4 | No console errors | DevTools Console |
| 5 | All assets load (no 404) | DevTools Network |
| 6 | Dark mode works | Change OS theme |
| 7 | Mobile responsive | DevTools device mode |

### 9.2 Verify Specific Content

| Content | URL |
|---------|-----|
| New project | `https://katalogarkan.github.io/katalog/{slug}` |
| New article | `https://katalogarkan.github.io/blog/{slug}` |
| Sitemap | `https://katalogarkan.github.io/sitemap-index.xml` |
| Robots | `https://katalogarkan.github.io/robots.txt` |

### 9.3 Check Deploy Logs

| # | Step | Action |
|---|------|--------|
| 1 | Open Actions tab | Click workflow run |
| 2 | Click `build` job | View build logs |
| 3 | Click `deploy` job | View deploy logs |
| 4 | Check for errors | Red text = error |

---

## 10. Rollback

### 10.1 Rollback via Git Revert (Recommended)

```bash
# 1. Find the commit to revert
git log --oneline -10

# 2. Revert the bad commit
git revert <commit-hash>

# 3. Push (triggers deploy of reverted state)
git push origin main
```

**Why revert, not reset:** Revert creates a new commit that undoes the change. History is preserved. Safe for production.

### 10.2 Rollback via Reset (Destructive)

```bash
# 1. Reset to previous commit
git reset --hard <commit-hash>

# 2. Force push
git push --force origin main
```

**Warning:** This rewrites history. Only use if no one else has pulled the branch.

### 10.3 Rollback via GitHub UI

| # | Step | Action |
|---|------|--------|
| 1 | Open commit history | Repo → Commits |
| 2 | Find the bad commit | — |
| 3 | Click **Revert** | Creates revert PR |
| 4 | Merge PR | Triggers deploy of reverted state |

### 10.4 Emergency: Disable Pages

If the live site is broken and needs to be taken down immediately:

| # | Step | Action |
|---|------|--------|
| 1 | Settings → Pages | — |
| 2 | Source → **None** | Save |
| 3 | Site returns 404 | — |
| 4 | Fix the issue locally | — |
| 5 | Re-enable Pages → GitHub Actions | — |

---

## 11. Custom Domain

### 11.1 When to Add

| Condition | Status |
|-----------|--------|
| Phase 6 complete | Required before custom domain |
| Domain purchased | Required |
| DNS access | Required |

### 11.2 Domain Options

| Domain | Est. Cost/Year | Registrar |
|--------|----------------|-----------|
| `katalogarkan.com` | ~$10–15 | Namecheap, Cloudflare |
| `katalogarkan.dev` | ~$12–15 | Namecheap, Cloudflare |
| `katalogarkan.id` | ~Rp 200K–300K | Local registrar |

### 11.3 Setup Steps

| # | Step | Action |
|---|------|--------|
| 1 | Buy domain | Namecheap / Cloudflare / local |
| 2 | Open DNS settings | Registrar dashboard |
| 3 | Add CNAME record | `www` → `katalogarkan.github.io` |
| 4 | Add A records (apex) | `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153` |
| 5 | GitHub → Settings → Pages | Custom domain: `katalogarkan.com` |
| 6 | Save | — |
| 7 | Wait for DNS check | ~24 hours |
| 8 | Enable **Enforce HTTPS** | After DNS verified |
| 9 | Update `astro.config.mjs` | `site: 'https://katalogarkan.com'` |
| 10 | Push + deploy | — |

### 11.4 DNS Records

| Type | Name | Value |
|------|------|-------|
| A | `@` | `185.199.108.153` |
| A | `@` | `185.199.109.153` |
| A | `@` | `185.199.110.153` |
| A | `@` | `185.199.111.153` |
| CNAME | `www` | `katalogarkan.github.io` |

### 11.5 After Custom Domain

| # | Check | Done |
|---|-------|:---:|
| 1 | `https://katalogarkan.com` loads | ☐ |
| 2 | `https://www.katalogarkan.com` loads | ☐ |
| 3 | HTTPS works (green lock) | ☐ |
| 4 | Old `github.io` URL redirects | ☐ |
| 5 | Sitemap uses new domain | ☐ |
| 6 | OG image URLs use new domain | ☐ |

---

## 12. Troubleshooting

### 12.1 Deploy Fails

| Symptom | Cause | Fix |
|---------|-------|-----|
| Action red X | Build error | Check `build` job logs |
| `npm ci` fails | `package-lock.json` out of sync | Run `npm install` locally, commit lockfile |
| `npm run build` fails | Code error | Run `npm run build` locally, fix errors |
| `Node version` error | Wrong Node in workflow | Check `node-version: 20` in `deploy.yml` |
| `Permission denied` | Workflow permissions | Settings → Actions → Read and write |

### 12.2 Deploy Succeeds but Site Broken

| Symptom | Cause | Fix |
|---------|-------|-----|
| 404 on all pages | Pages source not set | Settings → Pages → Source: GitHub Actions |
| Assets 404 | `site` missing or wrong | Check `astro.config.mjs` `site` |
| CSS not loading | Build output incomplete | Check `dist/` has CSS files |
| Images 404 | Wrong path | Check `/images/...` not `./images/...` |
| Dark mode not working | CSS variables missing | Check `global.css` has `prefers-color-scheme` block |
| Old content | CDN cache | Wait 5 min, hard refresh (Ctrl+Shift+R) |

### 12.3 Custom Domain Issues

| Symptom | Cause | Fix |
|---------|-------|-----|
| DNS not verified | Records not propagated | Wait 24h, check with `dig` |
| HTTPS fails | DNS not verified yet | Wait, then enable Enforce HTTPS |
| `github.io` still works | Custom domain not saved | Save in Settings → Pages |
| `www` not working | Missing CNAME | Add CNAME `www` → `katalogarkan.github.io` |

### 12.4 Workflow Not Triggering

| Symptom | Cause | Fix |
|---------|-------|-----|
| Push doesn't trigger | Wrong branch | Check `on.push.branches: [main]` |
| Workflow disabled | Manually disabled | Actions tab → Enable workflow |
| No Actions tab | Actions disabled | Settings → Actions → Allow all actions |

### 12.5 Diagnostic Commands

```bash
# Check local build
npm run build

# Check local preview
npm run preview

# Check git status
git status

# Check remote
git remote -v

# Check branch
git branch

# Check last commit
git log --oneline -5

# Check DNS (custom domain)
dig katalogarkan.com
nslookup katalogarkan.com
```

---

## 13. Security

### 13.1 Deploy Security

| # | Concern | Mitigation |
|---|---------|------------|
| 1 | Secrets in repo | No secrets — Formspree ID is public |
| 2 | Malicious dependencies | `npm audit` before each phase |
| 3 | Workflow permissions | Minimal: `contents: read`, `pages: write`, `id-token: write` |
| 4 | Branch protection | Enable after launch (see §13.2) |
| 5 | Force push | Avoid on `main` |

### 13.2 Branch Protection (Recommended After Launch)

| # | Setting | Value |
|---|---------|-------|
| 1 | Settings → Branches → Add rule | `main` |
| 2 | Require pull request | ✅ (optional for solo) |
| 3 | Require status checks | ✅ (deploy) |
| 4 | Restrict force push | ✅ |

**For solo project:** Branch protection is optional. Enable if you want to prevent accidental force pushes.

### 13.3 HTTPS

| Property | Value |
|----------|-------|
| Enforced by | GitHub Pages |
| Certificate | Auto-provisioned (Let's Encrypt) |
| Renewal | Auto |
| HSTS | Not configured (default) |

---

## 14. Performance

### 14.1 Deploy Performance

| Metric | Target | Actual |
|--------|--------|--------|
| Build time | < 2 min | ~60s |
| Deploy time | < 1 min | ~30s |
| Total time | < 3 min | ~90s |
| CDN propagation | < 5 min | ~2 min |

### 14.2 Site Performance (Post-Deploy)

| Metric | Target |
|--------|--------|
| Lighthouse Performance | ≥ 95 |
| Lighthouse Accessibility | ≥ 95 |
| Lighthouse Best Practices | ≥ 95 |
| Lighthouse SEO | ≥ 95 |
| LCP | < 2.5s |
| CLS | < 0.1 |

### 14.3 CDN

| Property | Value |
|----------|-------|
| CDN | GitHub Pages (Fastly) |
| Global | Yes |
| Cache | Static assets cached |
| Invalidation | Automatic on deploy |
---

*End of document.*