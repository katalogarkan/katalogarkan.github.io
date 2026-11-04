---
title: "Portfolio v2"
description: "A rebuilt personal portfolio with Astro and Tailwind, featuring a filterable project katalog and dark mode."
techStack: ["Astro", "Tailwind CSS", "TypeScript", "React"]
thumbnail: "/images/projects/portfolio-v2.png"
demoUrl: "https://katalogarkan.github.io"
repoUrl: "https://github.com/katalogarkan/katalogarkan.github.io"
category: "web-app"
featured: true
date: 2026-11-01
---

## Overview

Portfolio v2 is a complete rebuild of my personal website. It serves two purposes: to introduce me as a Full Stack Web Developer, and to showcase my projects in a filterable and searchable katalog.

## Problem

My previous portfolio was built with a heavy JavaScript framework. It loaded slowly on mobile devices, had no way to filter or search projects, and was difficult to update with new content. Recruiters and clients had to scroll through a long list to find what they were looking for.

## Solution

I rebuilt the site using Astro for static site generation and Tailwind CSS for styling. The entire site is now static HTML with zero JavaScript by default, making it incredibly fast. For the katalog filter, I used a single React island that only hydrates when the user visits the katalog page.

Content is managed via Markdown files in the repository. Adding a new project is as simple as creating a new `.md` file — no database, no CMS, no admin panel needed.

## Tech Stack

- **Astro 5** — Static site generation and content collections
- **Tailwind CSS 4** — Utility-first styling with CSS-first `@theme` configuration
- **React 18** — Used only for the katalog filter island
- **TypeScript** — Type safety across the entire project
- **GitHub Pages** — Free static hosting with automatic deploys via GitHub Actions

## Challenges

Migrating from Tailwind CSS 3 to Tailwind CSS 4 was the biggest challenge. The new version uses a CSS-first configuration approach via the `@theme` directive, which is completely different from the old `tailwind.config.mjs` file. The documentation was still evolving at the time, so I had to rely on the source code to understand how things worked.

Another challenge was implementing dark mode without using JavaScript. Instead of a manual toggle, the site follows the user's operating system preference using the `prefers-color-scheme` media query. All colors are defined as CSS variables, so switching between light and dark mode is instant and requires no JavaScript.

## Lessons Learned

- Static site generators like Astro are perfect for content-heavy websites like portfolios and blogs.
- React islands are a great way to add interactivity without sacrificing performance.
- CSS variables are a powerful tool for theming and dark mode.
- Writing content in Markdown is much faster than using a CMS.

## Links

- [Live Demo](https://katalogarkan.github.io)
- [Repository](https://github.com/katalogarkan/katalogarkan.github.io)