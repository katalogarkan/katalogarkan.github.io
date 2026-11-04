# Project Blueprint

## Document Information

| Property | Value |
| :--- | :--- |
| Version | 1.0.0 |
| Last Updated | 2026-11-05 |
| Status | Approved — Source of Truth |
| Project | Personal Branding & Freelance Portfolio |
| Owner | Arkan Tsabit |
| Framework | Astro 5 |
| Styling | Tailwind CSS 4 |
| Hosting | GitHub Pages |

---

## 1. Project Overview

**katalogarkan** is a professional portfolio and freelance showcase for Arkan Tsabit. It serves two primary purposes:
1. **Showcase Expertise:** Displaying technical capabilities in both Full Stack Web Development and Cloud Data Engineering.
2. **Client Acquisition:** Providing a clear, professional catalog of freelance services, case studies (Katalog), and technical articles (Blog).

### Core Tech Stack
- **Framework:** Astro 5 (Static Site Generation for ultra-fast performance).
- **Styling:** Tailwind CSS 4 (CSS-first configuration via `@theme`).
- **Interactivity:** React 18 (Islands architecture used strictly for the Katalog filter).
- **Content:** Astro Content Collections (Markdown + Zod validation).
- **Backend:** Google Apps Script + Google Sheets (Serverless handling for Contact & Testimonials).

---

## 2. Architecture & Data Flow

Because the site is statically generated, there is no traditional server runtime. Data flows as follows:

1. **Content:** Markdown files (`.md`) are stored in `src/content/katalog/` and `src/content/blog/`.
2. **Build Process:** During `npm run build`, Astro reads the Markdown, validates frontmatter against `src/content.config.ts`, and generates static HTML.
3. **Interactivity:** The `/katalog` page loads a React island (`KatalogFilter.tsx`) which receives the static project data as props to enable client-side filtering.
4. **Forms:** The Contact and Testimonial forms send POST requests via `fetch` to a Google Apps Script Web App URL. The script appends the data to a Google Sheet.
5. **Deployment:** A push to the `main` branch triggers a GitHub Action that builds the site and deploys the `dist/` folder to GitHub Pages.

---

## 3. Directory Structure

```text
katalogarkan.github.io/
├── public/                 # Static assets (images, favicon, CV, robots.txt)
├── src/
│   ├── components/         # Astro & React components (Header, Footer, Cards, Filter)
│   ├── content/            # Markdown files (katalog/ and blog/)
│   ├── layouts/            # BaseLayout (SEO/HTML shell) and PostLayout (Prose)
│   ├── pages/              # All 12 route files
│   ├── styles/             # global.css (Tailwind @theme + Dark Mode)
│   └── content.config.ts   # Zod schemas for Content Collections
├── docs/                   # Project documentation (this folder)
├── astro.config.mjs        # Astro configuration
└── package.json            # Dependencies and scripts
```

---

## 4. Execution Phases (Summary)

The project was built systematically over 6 phases:

1. **Phase 1 (Foundation):** Repo setup, Astro + Tailwind installation, CI/CD deployment.
2. **Phase 2 (Design):** Layouts, Header/Footer, Home page, and Dark Mode via CSS variables.
3. **Phase 3 (Static Pages):** About, Skills, Services, Contact, Testimonials, 404.
4. **Phase 4 (Katalog):** Project cards, React filtering island, and dynamic routing.
5. **Phase 5 (Blog):** Markdown article rendering, PostLayout, and dynamic routing.
6. **Phase 6 (Polish):** SEO meta tags, Google Sheets integration, and final deployment.

---

## 5. Key Architectural Decisions

| Decision | Rationale |
| :--- | :--- |
| **Astro over Next.js** | The site is content-heavy but requires very little client-side state. Astro's zero-JS-by-default approach yields perfect Lighthouse scores. |
| **Tailwind CSS 4** | Used for rapid UI development. Tailwind 4 uses a CSS-first approach (`@theme`), eliminating the need for `tailwind.config.js`. |
| **Google Sheets for Backend** | Avoids the cost and complexity of a database (like Supabase or Firebase). Google Apps Script handles the logic for free. |
| **React for Katalog Filter** | While Astro handles static routing, filtering and sorting 5+ items based on user input requires client-side state. React provides this cleanly via an island. |

---
*End of document.*