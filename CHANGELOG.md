# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-11-05

### Added
- **Official Launch:** Successfully deployed v1.0.0 to GitHub Pages.
- **Master Documentation:** Updated `README.md`, `SECURITY.md`, and `CONTRIBUTING.md` for public release.
- **Full Rebranding:** Finalized the transition to a "Full Stack Developer & Cloud Data Engineer" portfolio.

---

## [0.6.0] - 2026-11-05 (Phase 6: Polish & Deploy)

### Description
The final polish phase to ensure the website is SEO-friendly, accessible, and ready for production deployment.

### Added
- `public/robots.txt` and `public/favicon.svg` for search engine crawling and branding.
- Open Graph (OG) and Twitter Card meta tags in `src/layouts/BaseLayout.astro` for social media sharing.
- Placeholder assets: `avatar.png`, `cv.pdf`, and `og-default.png` in the `public/` directory.

### Fixed
- Resolved Astro compiler errors caused by HTML comments (`<!-- -->`) inside template expressions `{}`.
- Fixed a React hydration type mismatch in `katalog.astro` by converting `Date` to `string`.
- Removed a duplicate `favicon.svg` in `public/images/` to prevent asset conflicts.
- Fixed anchor scrolling UX from Home to specific Services sections (`/services#cloud-devops`).

### Changed
- Updated `astro.config.mjs` to include the `site` URL for sitemap generation.
- Cleaned up `.gitignore` to exclude local testing scripts (`*.py`, `structure.py`).

---

## [0.5.0] - 2026-11-04 (Phase 5: Blog & Detail Pages)

### Description
Implemented the blogging system and dynamic routing for article and project details.

### Added
- `src/layouts/PostLayout.astro` for readable, prose-styled articles with Dark Mode support.
- `src/components/BlogCard.astro` to display article previews.
- `src/pages/blog.astro` to list all published articles.
- Dynamic routes `src/pages/blog/[slug].astro` and `src/pages/katalog/[slug].astro` to render Markdown content.

### Fixed
- Fixed an Astro 5 API migration error (`project.render()` to `render(project)`).
- Moved `[slug].astro` from root `pages/` to `pages/blog/` to fix layout import paths.
- Cleared the `.astro` cache to resolve 404 errors on dynamic routes.

---

## [0.4.0] - 2026-11-04 (Phase 4: Katalog & React Filter)

### Description
Built the project portfolio page with a fast, client-side filtering system using React Islands.

### Added
- `src/components/KatalogFilter.tsx` (React) with category filter, search by tech, and sort by date.
- `src/components/ProjectCard.astro` to display project thumbnails and tech stacks.
- `src/pages/katalog.astro` to hydrate the React island (`client:load`).

### Fixed
- Fixed a Zod 4 deprecation warning by changing `z.string().url()` to `z.url()`.

---

## [0.3.0] - 2026-11-04 (Phase 3: Static Pages)

### Description
Created the 7 essential static pages to complete the website's navigation.

### Added
- `src/pages/about.astro` with Bio, Technical Journey timeline, and Achievements.
- `src/pages/skills.astro` with categorized skills and 10+ verified certification links.
- `src/pages/services.astro` with 14 detailed freelance offerings and pricing.
- `src/pages/contact.astro` with form integration.
- `src/pages/resources.astro`, `src/pages/testimonials.astro`, and `src/pages/404.astro`.

---

## [0.2.0] - 2026-11-04 (Phase 2: Design & Home)

### Description
Established the core design system, layout, and the Home page structure.

### Added
- `src/components/Header.astro` with 8 navigation links and a mobile hamburger menu.
- `src/components/Footer.astro` with a 4-column layout and dynamic copyright year.
- `src/pages/index.astro` (Home) featuring Hero, Stats, Services Summary, and Featured Projects.
- `src/components/SkillBadge.astro` for displaying the tech stack.

---

## [0.1.0] - 2026-11-01 (Phase 1: Project Foundation)

### Description
Initialized the repository, configured the tech stack, and set up the deployment pipeline.

### Added
- Astro 5 + React 18 + Tailwind CSS 4 configuration (`package.json`, `astro.config.mjs`).
- `src/styles/global.css` using Tailwind 4 `@theme` for CSS variables and Dark Mode.
- `src/content.config.ts` with Zod schemas for the Blog and Katalog collections.
- GitHub Actions workflow (`.github/workflows/deploy.yml`) for auto-deployment to GitHub Pages.