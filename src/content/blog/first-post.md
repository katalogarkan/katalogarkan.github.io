---
title: "How to add dark mode to Astro with CSS variables"
date: 2026-10-20
description: "A practical guide to implementing dark mode in Astro using CSS variables and prefers-color-scheme."
category: "tutorial"
tags: ["astro", "css", "dark-mode"]
draft: false
---

In this tutorial, we'll look at how to add dark mode to an Astro website using pure CSS variables.

## Why CSS Variables?

CSS variables are perfect for dark mode because they allow you to define a color once and reuse it everywhere. When the user switches their operating system theme, the browser automatically updates all variables.

## Implementation

First, define your light mode colors in `:root`.

```css
:root {
  --color-bg: #ffffff;
  --color-text: #1f2328;
}