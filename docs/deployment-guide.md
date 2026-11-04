# Deployment Guide

## Document Information

| Property | Value |
| :--- | :--- |
| Version | 1.0.0 |
| Last Updated | 2026-11-05 |
| Status | Approved — Source of Truth |
| Hosting | GitHub Pages |
| CI/CD | GitHub Actions |
| Build Output | `dist/` |

---

## 1. How Deployment Works

This website uses **GitHub Pages** for free hosting and **GitHub Actions** for the automated build process.

The flow is simple:
1. You run `git push` to the `main` branch.
2. GitHub Actions detects the push.
3. Actions runs `npm install` and `npm run build`.
4. The build output (the `dist/` folder) is uploaded to GitHub Pages.
5. The website goes live within 1–2 minutes.

---

## 2. Initial Setup (One-Time Only)

If you are setting up this repository for the first time, make sure the following settings are correct in GitHub:

1. Go to **Settings** → **Pages**.
2. Under **Build and deployment** → **Source**, select **GitHub Actions** (do NOT select *Deploy from a branch*).
3. Go to **Settings** → **Actions** → **General**.
4. Under **Workflow permissions**, select **Read and write permissions**.
5. Save.

---

## 3. The Workflow File

The configuration file is located at `.github/workflows/deploy.yml`. This file tells GitHub what to do.

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

---

## 4. Routine Deployment

Every time you finish editing code or adding an article, follow these steps:

```bash
# 1. Check the local build (make sure there are no errors)
npm run build

# 2. Commit your changes
git add .
git commit -m "content: add new article"

# 3. Push to GitHub
git push origin main

# 4. Wait 1-2 minutes, then check the "Actions" tab on GitHub.
# 5. Open https://katalogarkan.github.io to see the result.
```

---

## 5. Troubleshooting (If the Deploy Fails)

If you see a red cross (❌) in the **Actions** tab, these are the most common causes:

| Issue | Solution |
| :--- | :--- |
| **Build failed (Zod Error)** | There is a typo in the Markdown frontmatter. Check the error log and make sure `category`, `date`, and `title` are correct. |
| **Asset 404 (broken image)** | Make sure the image filename in the Markdown exactly matches the one in `public/images/`. Remember, letter case matters! |
| **Node version mismatch** | Make sure `node-version` in `deploy.yml` is set to `22`. |
| **Permission denied** | Go to Settings → Actions → General and make sure it is set to "Read and write". |
| **Tailwind classes not appearing** | Make sure `@import "tailwindcss";` is at the very top of `global.css`. |

### How to Read the Error Log:
1. Open the repository on GitHub.
2. Click the **Actions** tab.
3. Click the failed workflow (red cross).
4. Click the **build** or **deploy** job.
5. Read the red text to find out what went wrong.

---

## 6. Rollback (Restore a Previous Version)

If you push and break the website, you can restore it using Git Revert.

```bash
# 1. View the commit history
git log --oneline -5

# 2. Revert to a safe commit (replace <commit-id> with the correct ID)
git revert <commit-id>

# 3. Push
git push origin main
```

GitHub Actions will automatically re-deploy the previous version.

---
*End of document.*