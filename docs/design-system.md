# Design System

## Document Information

| Property | Value |
| :--- | :--- |
| Version | 1.0.0 |
| Last Updated | 2026-11-05 |
| Status | Approved — Source of Truth |
| Framework | Astro 5 + Tailwind CSS 4 |
| Theme | CSS-first via `@theme` |
| Dark Mode | OS Preference (`prefers-color-scheme`) |

---

## 1. Design Principles

1. **Content First:** No excessive decoration that distracts from the portfolio and text.
2. **Consistent:** Every page uses the same components and spacing.
3. **Accessible:** Color contrast meets WCAG AA standards, with keyboard navigation support.
4. **Fast:** Uses CSS variables (not JavaScript) for Dark Mode to enable instant rendering.
5. **Responsive:** Mobile-first, tested from 320px up to 2560px.

---

## 2. Color System (Tailwind 4 `@theme`)

All colors are defined as CSS Variables in `src/styles/global.css` through the `@theme` directive.

| Token | Light Mode | Dark Mode | Tailwind Class | Usage |
| :--- | :--- | :--- | :--- | :--- |
| `primary` | `#0969da` | `#58a6ff` | `bg-primary`, `text-primary` | Buttons, Links, Accents |
| `bg` | `#ffffff` | `#0d1117` | `bg-bg` | Page background |
| `bg-subtle` | `#f6f8fa` | `#161b22` | `bg-bg-subtle` | Card/Box background |
| `text` | `#1f2328` | `#e6edf3` | `text-text` | Main text (Headings, Body) |
| `text-muted` | `#656d76` | `#8b949e` | `text-text-muted` | Secondary text, descriptions |
| `border` | `#d0d7de` | `#30363d` | `border-border` | Borders (Cards, Header) |

### 2.1 Dark Mode Implementation
Dark Mode runs automatically based on the visitor's operating system preference. We use `@media (prefers-color-scheme: dark)` in `global.css` to override the color variable values.
**Important:** Never use the `dark:` class manually (e.g., `dark:bg-black`) inside components. Use the color tokens above so they change automatically.

---

## 3. Typography

- **Font Family:** `Inter` (loaded from Google Fonts).
- **Fallback:** `system-ui, -apple-system, sans-serif`.

| Element | Tailwind Class | Size |
| :--- | :--- | :--- |
| **Hero Title** | `text-4xl md:text-6xl font-bold` | 36px – 60px |
| **H1 / Page Title** | `text-4xl font-bold` | 36px |
| **H2 / Section Title** | `text-2xl font-bold` | 24px |
| **H3 / Card Title** | `text-xl font-bold` | 20px |
| **Body Text** | `text-base` | 16px |
| **Small Text** | `text-sm` | 14px |
| **Badge / Tags** | `text-xs font-medium` | 12px |

---

## 4. Layout & Spacing

- **Container:** Use the `.container-page` class (max-width 72rem / 1152px) already defined in `global.css`.
- **Section Padding:** `py-12 md:py-16` or `py-16 md:py-24` for Hero sections.
- **Gap (spacing between Cards):** `gap-6` (24px).
- **Card Padding:** `p-6` (24px).

---

## 5. Component Patterns

Below are the Tailwind class patterns for the main components. Do not change these arbitrarily so the UI stays consistent.

### 5.1 Primary Button
Used for primary actions such as "Hire Me" or "Send Message".
```html
<a href="..." class="inline-flex items-center justify-center px-6 py-3 rounded-md bg-primary text-white font-medium hover:bg-primary-hover transition-colors">
  Button Text
</a>
```

### 5.2 Secondary (Outline) Button
Used for alternative actions such as "View Projects".
```html
<a href="..." class="inline-flex items-center justify-center px-6 py-3 rounded-md bg-transparent text-primary font-medium border border-primary hover:bg-primary hover:text-white transition-colors">
  Button Text
</a>
```

### 5.3 Card
Used for Project Cards, Blog Cards, or Services boxes.
```html
<div class="bg-bg-subtle border border-border rounded-lg p-6 hover:shadow-md transition-shadow">
  <!-- Content -->
</div>
```

### 5.4 Badge / Tag (Tech Stack)
Used to display technologies (Python, Astro, etc.).
```html
<span class="inline-flex items-center px-2 py-1 rounded-md text-xs font-medium bg-primary/10 text-primary">
  Python
</span>
```

### 5.5 Form Inputs
Every form input must have a `<label>` for accessibility.
```html
<label for="name" class="block text-sm font-medium text-text mb-1">Name</label>
<input type="text" id="name" class="w-full px-4 py-2 rounded-md border border-border bg-bg text-text focus:ring-2 focus:ring-primary focus:border-primary" />
```

---

## 6. Prose (Markdown Styling)

For the Blog Detail and Katalog Detail pages, we use the `@tailwindcss/typography` plugin.
Wrap the Markdown content with this class so the text is automatically formatted neatly (headings, bullets, code blocks):

```html
<article class="prose dark:prose-invert max-w-none text-text">
  <!-- Markdown Content -->
</article>
```
*(Note: `dark:prose-invert` is the ONLY `dark:` class allowed in this project, because the typography plugin requires it to change text colors).*

---
*End of document.*