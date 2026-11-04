# katalogarkan

## Full Stack Web Developer & Cloud Data Engineer

[![Status](https://img.shields.io/badge/status-v1.0.0%20LIVE-brightgreen)](https://katalogarkan.github.io)
[![Astro](https://img.shields.io/badge/Astro-5.x-BC52EE)](https://astro.build/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind-4.x-06B6D4)](https://tailwindcss.com/)
[![React](https://img.shields.io/badge/React-18.x-61DAFB)](https://react.dev/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.x-3178C6)](https://www.typescriptlang.org/)
[![GitHub Pages](https://img.shields.io/badge/Deploy-GitHub%20Pages-222222)](https://katalogarkan.github.io)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Live Site](https://img.shields.io/badge/Live%20Site-katalogarkan.github.io-0969da)](https://katalogarkan.github.io)

---

## Project Overview

A personal branding website and project catalog for **Arkan Tsabit**, designed to showcase technical expertise and freelance services. The site bridges two core disciplines: **Full Stack Web Development** (Astro, React) and **Cloud Data Engineering** (Apache Airflow, BigQuery, Python).

Key features include interactive data case studies, verified professional certifications (Oracle, IBM, Meta), and a comprehensive catalog of freelance services. Built entirely as a static site with Astro, complemented by a serverless Google Sheets backend for forms.

## Key Metrics & Features

- **12 Routes:** 9 static pages + 2 dynamic routes (Catalog & Blog) + 1 custom 404 page.
- **5 Case Studies:** Real-world data engineering projects (BatchETL, Uber, Amazon, GIG 1, Expense).
- **10+ Certifications:** Oracle Top 108 Global, IBM, and Meta credentials with live verification links.
- **Interactive Filter:** React Island for fast search, category filtering, and date sorting.
- **Serverless Forms:** Google Sheets integration for Contact & Testimonials.
- **Dark Mode:** Follows OS preference instantly (zero JavaScript required).
- **100% Auto-Verified:** 236/236 verification checks passed across 6 development phases.

## Architecture

The website is built using a modern, static-first approach:

1. **Framework:** Astro 5 for Static Site Generation (SSG) ensuring ultra-fast load times.
2. **Styling:** Tailwind CSS 4 via Vite plugin, using CSS variables for the theme (`@theme`).
3. **Interactivity:** React 18 island architecture (only hydrates the Catalog filter).
4. **Content:** Markdown Collections validated with Zod schemas.
5. **Backend:** Google Apps Script + Google Sheets for dynamic form handling.
6. **Deployment:** GitHub Actions CI/CD to GitHub Pages.

## Tech Stack

| Component | Technology |
| :--- | :--- |
| Framework | Astro 5 |
| Styling | Tailwind CSS 4 |
| Interactivity | React 18 (Islands) |
| Content | Astro Content Collections |
| Backend/DB | Google Apps Script / Google Sheets |
| Hosting | GitHub Pages |
| CI/CD | GitHub Actions |

## Quick Start

Run this portfolio locally in three simple steps:

```bash
# 1. Clone the repository
git clone https://github.com/katalogarkan/katalogarkan.github.io.git
cd katalogarkan.github.io

# 2. Install dependencies
npm install

# 3. Start the local development server
npm run dev
# Open http://localhost:4321 in your browser
```

To build for production, run `npm run build`. The static files will be generated in the `/dist` folder.

## Documentation

For deep-dive technical details, check the `/docs` folder:
- [Blueprint & Architecture](docs/blueprint.md)
- [Design System](docs/design-system.md)
- [Deployment Guide](docs/deployment-guide.md)

## Author

**Arkan Tsabit** — Full Stack Developer & Cloud Data Engineer
- **Portfolio:** [katalogarkan.github.io](https://katalogarkan.github.io)
- **LinkedIn:** [linkedin.com/in/arkan-tsabit-0b12b9407](https://linkedin.com/in/arkan-tsabit-0b12b9407)
- **GitHub:** [github.com/ArkanTsabit123](https://github.com/ArkanTsabit123)
- **Email:** arkantsabit025@gmail.com

---

*Licensed under the MIT License.*