# katalogarkan — design-system.md

---

## Document Information

| Property | Value |
|----------|-------|
| Document Version | 1.3.0 |
| Project Version | 0.5.0 (Phase 5 Complete) |
| Last Updated | 2026-11-04 |
| Status | Approved — Source of Truth |
| Project | Personal branding & katalog website |
| Owner | Arkan (Full Stack Web Developer) |
| Related | `blueprint.md` §5 (Design Tokens) |
| Framework | Astro 5 + Tailwind CSS 4 |
| Tailwind Config | CSS-first via `@theme` (no `tailwind.config.mjs`) |
| Dark Mode | `prefers-color-scheme` + CSS variables |
| Font | Inter (Google Fonts) |
| Primary Color | `#0969da` |

---

## Table of Contents

1. [Purpose](#1-purpose)
2. [Design Principles](#2-design-principles)
3. [Color System](#3-color-system)
4. [Typography System](#4-typography-system)
5. [Spacing System](#5-spacing-system)
6. [Border Radius](#6-border-radius)
7. [Shadow System](#7-shadow-system)
8. [Breakpoints](#8-breakpoints)
9. [Dark Mode](#9-dark-mode)
10. [Layout Patterns](#10-layout-patterns)
11. [Component Styles](#11-component-styles)
12. [Iconography](#12-iconography)
13. [Motion & Animation](#13-motion--animation)
14. [Focus & Interaction States](#14-focus--interaction-states)
15. [Form Elements](#15-form-elements)
16. [Image Treatment](#16-image-treatment)
17. [Code & Prose](#17-code--prose)
18. [Tailwind 4 Theme Reference](#18-tailwind-4-theme-reference)
19. [Global CSS Reference](#19-global-css-reference)
20. [Do & Don't](#20-do--dont)
21. [Change Log](#21-change-log)

---

## 1. Purpose

### 1.1 What This Document Is

The single source of truth for all visual decisions in the katalogarkan website. Every color, font size, spacing value, shadow, and component style is defined here.

### 1.2 Who Uses This

| Role | Usage |
|------|-------|
| Owner (Arkan) | Reference when building components |
| Future contributor | Onboarding — understand visual language |
| AI assistant | Generate consistent code |

### 1.3 Relationship to Blueprint

| Blueprint §5 | This Document |
|--------------|---------------|
| Token names and values (summary) | Full implementation details |
| Color palette table | Usage rules, contrast, examples |
| Typography table | Full type scale, weights, line heights |
| Spacing table | Layout patterns, component spacing |
| §5.9 Tailwind config (`@theme`) | §18 mirrors it exactly |
| §5.10 Global CSS | §19 mirrors it exactly |

**Rule:** If a value exists in both documents, this document wins for implementation details. Blueprint wins for architectural decisions. §18 and §19 here must match `blueprint.md` §5.9 and §5.10 exactly.

---

## 2. Design Principles

| # | Principle | Application |
|---|-----------|-------------|
| 1 | **Content first** | No decoration that distracts from text |
| 2 | **Consistent** | Same spacing, same colors, same patterns everywhere |
| 3 | **Accessible** | Contrast ≥ 4.5:1, focus visible, keyboard navigable |
| 4 | **Fast** | Minimal CSS, no heavy animations, system fonts fallback |
| 5 | **Responsive** | Mobile-first, works from 320px to 2560px |
| 6 | **Dark mode native** | Every color has a dark counterpart via CSS variables |
| 7 | **Developer-friendly** | Token names map directly to Tailwind classes |

---

## 3. Color System

### 3.1 Semantic Color Tokens

| Token | Light | Dark | CSS Variable | Tailwind Class | Usage |
|-------|-------|------|--------------|----------------|-------|
| `primary` | `#0969da` | `#58a6ff` | `--color-primary` | `text-primary` `bg-primary` | Links, buttons, accents |
| `primary-hover` | `#0550ae` | `#79c0ff` | `--color-primary-hover` | `hover:bg-primary-hover` | Hover states |
| `bg` | `#ffffff` | `#0d1117` | `--color-bg` | `bg-bg` | Page background |
| `bg-subtle` | `#f6f8fa` | `#161b22` | `--color-bg-subtle` | `bg-bg-subtle` | Card background |
| `text` | `#1f2328` | `#e6edf3` | `--color-text` | `text-text` | Body text |
| `text-muted` | `#656d76` | `#8b949e` | `--color-text-muted` | `text-text-muted` | Secondary text |
| `border` | `#d0d7de` | `#30363d` | `--color-border` | `border-border` | Borders |
| `success` | `#1a7f37` | `#3fb950` | `--color-success` | `text-success` | Success states |
| `warning` | `#9a6700` | `#d29922` | `--color-warning` | `text-warning` | Warning states |
| `danger` | `#cf222e` | `#f85149` | `--color-danger` | `text-danger` | Error states |

### 3.2 Contrast Ratios

| Pair | Light | Dark | WCAG |
|------|-------|------|------|
| `text` on `bg` | 16.1:1 | 14.3:1 | AAA |
| `text-muted` on `bg` | 5.9:1 | 6.1:1 | AA |
| `primary` on `bg` | 4.8:1 | 6.4:1 | AA |
| `text` on `bg-subtle` | 15.8:1 | 13.2:1 | AAA |
| `border` on `bg` | 1.4:1 | 1.6:1 | Decorative only |

### 3.3 Color Usage Rules

| Rule | Detail |
|------|--------|
| Primary | Only for interactive elements (links, buttons) and key accents |
| Never use primary for body text | Use `text` token |
| Never use color alone to convey meaning | Pair with icon or text |
| Dark mode | Handled via CSS variables in `global.css` (§19) — do NOT write `dark:` variants manually |
| Backgrounds | Use `bg` for page, `bg-subtle` for cards/sections |

### 3.4 Color Examples

```html
<!-- Link -->
<a href="/katalog" class="text-primary hover:text-primary-hover">Katalog</a>

<!-- Primary button -->
<button class="bg-primary text-white hover:bg-primary-hover">Contact Me</button>

<!-- Card -->
<div class="bg-bg-subtle border border-border rounded-lg p-6">
  <h3 class="text-text">Project Title</h3>
  <p class="text-text-muted">Description</p>
</div>
```

**Note:** These classes resolve to CSS variables defined in `global.css`. Dark mode is applied automatically — no `dark:` prefix needed.

---

## 4. Typography System

### 4.1 Font Family

| Token | Value | Fallback |
|-------|-------|----------|
| `font-sans` | Inter | `system-ui, -apple-system, sans-serif` |
| `font-mono` | — | `ui-monospace, SFMono-Regular, Menlo, monospace` |

### 4.2 Font Weights

| Weight | Tailwind | Usage |
|--------|----------|-------|
| 400 | `font-normal` | Body text |
| 500 | `font-medium` | Labels, nav links |
| 700 | `font-bold` | Headings |

### 4.3 Type Scale

| Token | Size | Line Height | Weight | Tailwind | Usage |
|-------|------|-------------|--------|----------|-------|
| `text-xs` | 12px | 1.5 | 400 | `text-xs` | Badges, labels |
| `text-sm` | 14px | 1.5 | 400 | `text-sm` | Secondary text |
| `text-base` | 16px | 1.6 | 400 | `text-base` | Body |
| `text-lg` | 18px | 1.6 | 400 | `text-lg` | Lead paragraph |
| `text-xl` | 20px | 1.4 | 700 | `text-xl font-bold` | H3 |
| `text-2xl` | 24px | 1.3 | 700 | `text-2xl font-bold` | H2 |
| `text-4xl` | 36px | 1.2 | 700 | `text-4xl font-bold` | H1 |
| `text-6xl` | 60px | 1.1 | 700 | `text-6xl font-bold` | Hero |

### 4.4 Heading Hierarchy

| Level | Tag | Size | Usage |
|-------|-----|------|-------|
| H1 | `<h1>` | `text-4xl` (36px) | Page title (one per page) |
| H2 | `<h2>` | `text-2xl` (24px) | Section title |
| H3 | `<h3>` | `text-xl` (20px) | Sub-section |
| H4 | `<h4>` | `text-lg` (18px) | Card title |
| Hero | `<h1>` | `text-6xl` (60px) | Home hero only |

### 4.5 Typography Rules

| Rule | Detail |
|------|--------|
| One H1 per page | Page title or hero |
| Never skip heading levels | H1 → H2 → H3 (not H1 → H3) |
| Max line length | 65–75 characters (`max-w-prose`) |
| Paragraph spacing | `space-y-4` between paragraphs |
| Link style | `text-primary underline hover:text-primary-hover` |
| Code inline | `font-mono text-sm bg-bg-subtle px-1 rounded` |

---

## 5. Spacing System

### 5.1 Spacing Scale

| Token | Value | Tailwind | Usage |
|-------|-------|----------|-------|
| `space-xs` | 4px | `p-1` `m-1` `gap-1` | Icon padding, tight gaps |
| `space-sm` | 8px | `p-2` `m-2` `gap-2` | Badge padding, small gaps |
| `space-md` | 16px | `p-4` `m-4` `gap-4` | Card padding, list gaps |
| `space-lg` | 24px | `p-6` `m-6` `gap-6` | Section padding |
| `space-xl` | 32px | `p-8` `m-8` `gap-8` | Large section padding |
| `space-2xl` | 48px | `p-12` `m-12` `gap-12` | Page section spacing |
| `space-3xl` | 64px | `p-16` `m-16` `gap-16` | Hero spacing |

### 5.2 Layout Spacing Rules

| Context | Value |
|---------|-------|
| Page horizontal padding (mobile) | `px-4` (16px) |
| Page horizontal padding (desktop) | `px-8` (32px) |
| Max content width | `max-w-6xl` (1152px) |
| Section vertical spacing | `py-12` (48px) mobile, `py-16` (64px) desktop |
| Card internal padding | `p-6` (24px) |
| Gap between cards | `gap-6` (24px) |
| Gap between sections | `space-y-12` (48px) |

### 5.3 Container Pattern

```html
<div class="max-w-6xl mx-auto px-4 md:px-8">
  <!-- content -->
</div>
```

Or use the `.container-page` utility defined in `global.css` (§19):

```html
<div class="container-page">
  <!-- content -->
</div>
```

---

## 6. Border Radius

| Token | Value | Tailwind | Usage |
|-------|-------|----------|-------|
| `radius-sm` | 4px | `rounded-sm` | Badges, small elements |
| `radius-md` | 8px | `rounded-md` | Buttons, inputs |
| `radius-lg` | 12px | `rounded-lg` | Cards, modals |
| `radius-full` | 9999px | `rounded-full` | Avatars, pills |

### 6.1 Radius Rules

| Element | Radius |
|---------|--------|
| Button | `rounded-md` |
| Input | `rounded-md` |
| Card | `rounded-lg` |
| Badge | `rounded-full` |
| Avatar | `rounded-full` |
| Image (thumbnail) | `rounded-lg` |
| Code block | `rounded-md` |

---

## 7. Shadow System

| Token | Value | Tailwind | Usage |
|-------|-------|----------|-------|
| `shadow-sm` | `0 1px 2px rgba(0,0,0,0.05)` | `shadow-sm` | Subtle elevation |
| `shadow-md` | `0 4px 6px rgba(0,0,0,0.1)` | `shadow-md` | Card default |
| `shadow-lg` | `0 10px 15px rgba(0,0,0,0.1)` | `shadow-lg` | Card hover, dropdown |

### 7.1 Shadow Rules

| Element | Default | Hover |
|---------|---------|-------|
| Card | `shadow-md` | `shadow-lg` |
| Button | `shadow-sm` | `shadow-md` |
| Header | `shadow-sm` | — |
| Dropdown | `shadow-lg` | — |
| Dark mode | Reduce opacity by 50% | — |

---

## 8. Breakpoints

| Token | Value | Tailwind | Target |
|-------|-------|----------|--------|
| `sm` | 640px | `sm:` | Large phone |
| `md` | 768px | `md:` | Tablet |
| `lg` | 1024px | `lg:` | Small laptop |
| `xl` | 1280px | `xl:` | Desktop |
| `2xl` | 1536px | `2xl:` | Large desktop |

### 8.1 Mobile-First Strategy

| Rule | Detail |
|------|--------|
| Base styles | Mobile (no prefix) |
| Enhancements | Add `sm:`, `md:`, `lg:` prefixes |
| Never desktop-first | Do not use `max-*` breakpoints |
| Test at 320px | Smallest supported width |

### 8.2 Responsive Patterns

```html
<!-- Grid: 1 col mobile, 2 col tablet, 3 col desktop -->
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
  <!-- cards -->
</div>

<!-- Hide on mobile, show on desktop -->
<nav class="hidden md:flex">...</nav>

<!-- Show on mobile, hide on desktop -->
<button class="md:hidden">☰</button>
```

---

## 9. Dark Mode

### 9.1 Strategy

| Property | Value |
|----------|-------|
| Method | `prefers-color-scheme` media query + CSS variables |
| Toggle | None |
| JavaScript | None required |
| Default | Light (if OS has no preference) |
| Single source of truth | `src/styles/global.css` (§19) — CSS variables overridden in `@media (prefers-color-scheme: dark)` |

**No `darkMode` key** — Tailwind 4 handles dark mode via CSS variables, not a config option.

### 9.2 How Dark Mode Works

**Do NOT write `dark:` variants manually.** All colors are defined via CSS variables in `global.css`. Tailwind 4 auto-generates utility classes from `@theme`, and those classes resolve to CSS variables. When the OS switches to dark mode, the variables change and every component updates automatically.

```html
<!-- Correct: uses token classes, dark mode automatic -->
<div class="bg-bg-subtle border border-border rounded-lg p-6">
  <h3 class="text-text">Project Title</h3>
  <p class="text-text-muted">Description</p>
</div>

<!-- Wrong: hardcoded dark variant -->
<div class="bg-white dark:bg-gray-900">
```

### 9.3 Dark Mode Color Mapping

| Element | Light | Dark | CSS Variable |
|---------|-------|------|--------------|
| Page background | `#ffffff` | `#0d1117` | `--color-bg` |
| Card background | `#f6f8fa` | `#161b22` | `--color-bg-subtle` |
| Body text | `#1f2328` | `#e6edf3` | `--color-text` |
| Muted text | `#656d76` | `#8b949e` | `--color-text-muted` |
| Border | `#d0d7de` | `#30363d` | `--color-border` |
| Primary | `#0969da` | `#58a6ff` | `--color-primary` |

### 9.4 Dark Mode Rules

| Rule | Detail |
|------|--------|
| Never hardcode colors | Always use token classes |
| Never use `dark:` prefix | Dark mode handled by CSS variables |
| Test both modes | Every component verified in light + dark |
| Images | Use `dark:opacity-90` only if photo is too bright (exception allowed) |
| Shadows | Reduce opacity in dark mode via CSS variable |

---

## 10. Layout Patterns

### 10.1 Page Shell

```
┌─────────────────────────────────────────┐
│  Header (sticky, shadow-sm)            │
├─────────────────────────────────────────┤
│                                         │
│  Main content (max-w-6xl, mx-auto)      │
│  (py-12 mobile, py-16 desktop)          │
│                                         │
├─────────────────────────────────────────┤
│  Footer (bg-subtle, border-t)           │
└─────────────────────────────────────────┘
```

### 10.2 Common Layouts

| Layout | Grid | Usage |
|--------|------|-------|
| Single column | `max-w-prose mx-auto` | Blog article, About bio |
| Two column | `grid md:grid-cols-2 gap-8` | About (photo + bio) |
| Three column | `grid md:grid-cols-2 lg:grid-cols-3 gap-6` | Katalog, Blog list |
| Four column | `grid grid-cols-2 lg:grid-cols-4 gap-4` | KPI cards, Skills |
| Sidebar | `grid lg:grid-cols-[1fr_300px] gap-8` | Blog with sidebar (future) |

### 10.3 Section Pattern

```html
<section class="py-12 md:py-16">
  <div class="container-page">
    <h2 class="text-2xl font-bold mb-8">Section Title</h2>
    <!-- content -->
  </div>
</section>
```

---

## 11. Component Styles

### 11.1 Button — Primary

```html
<button class="bg-primary text-white font-medium px-4 py-2 rounded-md
               hover:bg-primary-hover
               focus-visible:ring-2 focus-visible:ring-primary focus-visible:ring-offset-2
               transition-colors">
  Contact Me
</button>
```

| Property | Value |
|----------|-------|
| Background | `bg-primary` |
| Text | `text-white` |
| Padding | `px-4 py-2` |
| Radius | `rounded-md` |
| Hover | `hover:bg-primary-hover` |
| Focus | `focus-visible:ring-2` |
| Transition | `transition-colors` |

### 11.2 Button — Secondary

```html
<button class="bg-transparent text-primary font-medium px-4 py-2 rounded-md
               border border-primary
               hover:bg-primary hover:text-white
               focus-visible:ring-2 focus-visible:ring-primary focus-visible:ring-offset-2
               transition-colors">
  View Katalog
</button>
```

### 11.3 Button — Ghost

```html
<button class="bg-transparent text-text-muted font-medium px-4 py-2 rounded-md
               hover:bg-bg-subtle hover:text-text
               focus-visible:ring-2 focus-visible:ring-primary
               transition-colors">
  Cancel
</button>
```

### 11.4 Card

```html
<div class="bg-bg-subtle border border-border rounded-lg p-6
            shadow-md hover:shadow-lg transition-shadow">
  <!-- content -->
</div>
```

| Property | Value |
|----------|-------|
| Background | `bg-bg-subtle` |
| Border | `border border-border` |
| Padding | `p-6` |
| Radius | `rounded-lg` |
| Shadow | `shadow-md` |
| Hover | `hover:shadow-lg` |

### 11.5 Badge

```html
<span class="inline-flex items-center px-2 py-1 rounded-full
             text-xs font-medium
             bg-primary/10 text-primary">
  Astro
</span>
```

### 11.6 Nav Link

```html
<a href="/katalog" class="text-text-muted hover:text-text font-medium
                          px-3 py-2 rounded-md
                          focus-visible:ring-2 focus-visible:ring-primary
                          transition-colors">
  Katalog
</a>
```

### 11.7 Section Heading

```html
<div class="mb-8">
  <h2 class="text-2xl font-bold text-text">Katalog</h2>
  <p class="text-text-muted mt-2">Projects built by Arkan.</p>
</div>
```

---

## 12. Iconography

### 12.1 Icon Strategy

| Property | Value |
|----------|-------|
| Library | Inline SVG (no icon font) |
| Size | 16px (sm), 20px (md), 24px (lg) |
| Color | `currentColor` (inherits text color) |
| Stroke | 2px |
| Accessibility | `aria-hidden="true"` on decorative icons |

### 12.2 Icon Usage

```html
<!-- Decorative icon -->
<svg class="w-5 h-5" aria-hidden="true" fill="none" stroke="currentColor" viewBox="0 0 24 24">
  <!-- path -->
</svg>

<!-- Icon with label (button) -->
<button class="flex items-center gap-2">
  <svg class="w-5 h-5" aria-hidden="true">...</svg>
  <span>Download CV</span>
</button>

<!-- Icon-only button (needs aria-label) -->
<button aria-label="Open menu">
  <svg class="w-6 h-6" aria-hidden="true">...</svg>
</button>
```

### 12.3 Common Icons

| Icon | Usage |
|------|-------|
| Menu (hamburger) | Mobile nav toggle |
| X (close) | Close menu |
| External link | Demo link |
| GitHub | Repo link |
| Mail | Contact |
| Download | CV download |
| Arrow left | Back link |
| Calendar | Blog date |
| Tag | Category |

---

## 13. Motion & Animation

### 13.1 Principles

| # | Principle |
|---|-----------|
| 1 | Motion is functional, not decorative |
| 2 | Duration ≤ 200ms for interactions |
| 3 | Respect `prefers-reduced-motion` |
| 4 | No auto-playing animations |

### 13.2 Transitions

| Element | Property | Duration | Easing |
|---------|----------|----------|--------|
| Button | `background-color`, `color` | 150ms | `ease` |
| Card | `box-shadow` | 200ms | `ease` |
| Link | `color` | 150ms | `ease` |
| Nav link | `color`, `background-color` | 150ms | `ease` |

### 13.3 Reduced Motion

```css
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```

### 13.4 No Animation On

| Element | Reason |
|---------|--------|
| Page load | Distracting |
| Scroll | Performance |
| Auto-carousel | Accessibility |
| Parallax | Performance |

---

## 14. Focus & Interaction States

### 14.1 Focus Ring

| Property | Value |
|----------|-------|
| Style | `ring-2` |
| Color | `ring-primary` |
| Offset | `ring-offset-2` |
| Trigger | `focus-visible` only (not `focus`) |

```html
<button class="focus-visible:ring-2 focus-visible:ring-primary focus-visible:ring-offset-2">
```

### 14.2 Interaction States

| State | Visual Change |
|-------|---------------|
| Hover | Color shift, shadow lift |
| Focus | Ring (visible only for keyboard) |
| Active | Slight scale (`active:scale-95`) |
| Disabled | `opacity-50 cursor-not-allowed` |

### 14.3 Skip Link

```html
<a href="#main" class="sr-only focus:not-sr-only focus:absolute focus:top-4 focus:left-4
                       focus:bg-primary focus:text-white focus:px-4 focus:py-2 focus:rounded-md">
  Skip to content
</a>
```

---

## 15. Form Elements

### 15.1 Input

```html
<label for="email" class="block text-sm font-medium text-text mb-1">Email</label>
<input type="email" id="email" name="email"
       class="w-full px-3 py-2 rounded-md border border-border
              bg-bg text-text
              focus-visible:ring-2 focus-visible:ring-primary focus-visible:border-primary
              placeholder:text-text-muted"
       placeholder="you@example.com" />
```

### 15.2 Textarea

```html
<label for="message" class="block text-sm font-medium text-text mb-1">Message</label>
<textarea id="message" name="message" rows="5"
          class="w-full px-3 py-2 rounded-md border border-border
                 bg-bg text-text
                 focus-visible:ring-2 focus-visible:ring-primary focus-visible:border-primary
                 placeholder:text-text-muted"
          placeholder="Your message..."></textarea>
```

### 15.3 Form Rules

| Rule | Detail |
|------|--------|
| Every input has `<label>` | Required for accessibility |
| Label above input | Not placeholder-only |
| Error state | `border-danger` + error text below |
| Required fields | Mark with `*` and `required` attribute |
| Spacing | `space-y-4` between fields |

---

## 16. Image Treatment

### 16.1 Thumbnail (ProjectCard)

| Property | Value |
|----------|-------|
| Aspect ratio | 16:9 |
| Radius | `rounded-lg` |
| Object fit | `object-cover` |
| Width | 100% |
| Loading | `loading="lazy"` |

```html
<img src="/images/projects/example.png" alt="Project screenshot"
     class="w-full aspect-video object-cover rounded-lg" loading="lazy" />
```

### 16.2 Avatar

| Property | Value |
|----------|-------|
| Size | 40px (sm), 80px (md), 160px (lg) |
| Radius | `rounded-full` |
| Object fit | `object-cover` |

```html
<img src="/images/avatar.png" alt="Arkan"
     class="w-40 h-40 rounded-full object-cover" />
```

### 16.3 Image Rules

| Rule | Detail |
|------|--------|
| Always set `alt` | Descriptive or empty (`alt=""`) for decorative |
| Use `loading="lazy"` | Except hero image |
| No optimization at launch | Images served from `public/` as-is (see `content-guide.md` §6) |
| Max width | 100% of container |
| No stretching | Use `object-cover` |

---

## 17. Code & Prose

### 17.1 Prose (Markdown Content)

Blog articles and katalog detail use `@tailwindcss/typography`:

```html
<article class="prose dark:prose-invert max-w-none">
  <!-- Markdown content -->
</article>
```

**Exception:** `prose-invert` is used here because the typography plugin does not read CSS variables. This is the only allowed `dark:` variant.

### 17.2 Inline Code

```html
<code class="font-mono text-sm bg-bg-subtle px-1 py-0.5 rounded">npm run dev</code>
```

### 17.3 Code Block

```html
<pre class="bg-bg-subtle border border-border rounded-md p-4 overflow-x-auto">
  <code class="font-mono text-sm">npm run build</code>
</pre>
```

### 17.4 Prose Rules

| Rule | Detail |
|------|--------|
| Max width | `max-w-prose` (65ch) |
| Headings | Auto-styled by typography plugin |
| Links | Primary color, underline |
| Lists | Disc, decimal |
| Blockquote | Left border, italic |
| Tables | Bordered, striped |

---

## 18. Tailwind 4 Theme Reference

This section **must match `blueprint.md` §5.9 exactly**.

Tailwind 4 uses **CSS-first configuration**. There is **no `tailwind.config.mjs`**. All tokens are declared in `src/styles/global.css` via `@theme`.

```css
/* src/styles/global.css — @theme block */
@import "tailwindcss";
@plugin "@tailwindcss/typography";

@theme {
  --color-primary: #0969da;
  --color-primary-hover: #0550ae;
  --color-bg: #ffffff;
  --color-bg-subtle: #f6f8fa;
  --color-text: #1f2328;
  --color-text-muted: #656d76;
  --color-border: #d0d7de;
  --color-success: #1a7f37;
  --color-warning: #9a6700;
  --color-danger: #cf222e;

  --font-sans: "Inter", system-ui, -apple-system, sans-serif;
  --font-mono: ui-monospace, SFMono-Regular, Menlo, monospace;

  --container-prose: 65ch;
}
```

### 18.1 How Tailwind 4 Generates Utilities

| `@theme` declaration | Auto-generated utilities |
|----------------------|--------------------------|
| `--color-primary` | `bg-primary`, `text-primary`, `border-primary` |
| `--color-primary-hover` | `hover:bg-primary-hover`, `hover:text-primary-hover` |
| `--color-bg` | `bg-bg` |
| `--color-bg-subtle` | `bg-bg-subtle` |
| `--color-text` | `text-text` |
| `--color-text-muted` | `text-text-muted` |
| `--color-border` | `border-border` |
| `--font-sans` | `font-sans` |
| `--font-mono` | `font-mono` |
| `--container-prose` | `max-w-prose` |

### 18.2 Why No `tailwind.config.mjs`

| Concern | Tailwind 3 (old) | Tailwind 4 (current) |
|---------|------------------|----------------------|
| Config location | `tailwind.config.mjs` | `@theme` in `global.css` |
| Integration | `@astrojs/tailwind` | `@tailwindcss/vite` |
| Import | `@tailwind base/components/utilities` | `@import "tailwindcss"` |
| Plugin | `plugins: [typography]` | `@plugin "@tailwindcss/typography"` |

**Rule:** Do not create `tailwind.config.mjs`. Do not add `@astrojs/tailwind`. All tokens live in `@theme`.

---

## 19. Global CSS Reference

This section **must match `blueprint.md` §5.10 exactly**.

```css
/* src/styles/global.css */
@import "tailwindcss";
@plugin "@tailwindcss/typography";

@theme {
  --color-primary: #0969da;
  --color-primary-hover: #0550ae;
  --color-bg: #ffffff;
  --color-bg-subtle: #f6f8fa;
  --color-text: #1f2328;
  --color-text-muted: #656d76;
  --color-border: #d0d7de;
  --color-success: #1a7f37;
  --color-warning: #9a6700;
  --color-danger: #cf222e;

  --font-sans: "Inter", system-ui, -apple-system, sans-serif;
  --font-mono: ui-monospace, SFMono-Regular, Menlo, monospace;

  --container-prose: 65ch;
}

@layer base {
  :root {
    color-scheme: light dark;
  }

  @media (prefers-color-scheme: dark) {
    :root {
      --color-primary: #58a6ff;
      --color-primary-hover: #79c0ff;
      --color-bg: #0d1117;
      --color-bg-subtle: #161b22;
      --color-text: #e6edf3;
      --color-text-muted: #8b949e;
      --color-border: #30363d;
      --color-success: #3fb950;
      --color-warning: #d29922;
      --color-danger: #f85149;
    }
  }

  html {
    scroll-behavior: smooth;
  }

  body {
    background-color: var(--color-bg);
    color: var(--color-text);
    font-family: var(--font-sans);
    -webkit-font-smoothing: antialiased;
  }

  @media (prefers-reduced-motion: reduce) {
    * {
      animation-duration: 0.01ms !important;
      transition-duration: 0.01ms !important;
    }
  }
}

@layer components {
  .container-page {
    max-width: 72rem;
    margin-inline: auto;
    padding-inline: 1rem;
  }
  @media (min-width: 768px) {
    .container-page {
      padding-inline: 2rem;
    }
  }
}
```

**How it works:**

1. `@import "tailwindcss"` — loads Tailwind 4
2. `@plugin "@tailwindcss/typography"` — loads prose plugin
3. `@theme` — declares design tokens; Tailwind auto-generates utilities
4. `@layer base` — sets `color-scheme`, dark mode variable overrides, body styles, reduced motion
5. `@layer components` — defines `.container-page` utility

**Single source of truth:** `src/styles/global.css`. Do not duplicate these values elsewhere.

---

## 20. Do & Don't

### 20.1 Do

| # | Do |
|---|-----|
| 1 | Use semantic tokens (`bg-bg-subtle`, not `bg-gray-100`) |
| 2 | Let dark mode work via CSS variables — no `dark:` prefix |
| 3 | Use `focus-visible` not `focus` |
| 4 | Test at 320px, 768px, 1024px, 1440px |
| 5 | Use `max-w-prose` for text blocks |
| 6 | Add `alt` to every image |
| 7 | Use `loading="lazy"` on below-fold images |
| 8 | Respect `prefers-reduced-motion` |
| 9 | Use `prose dark:prose-invert` for Markdown (only allowed `dark:` variant) |
| 10 | Declare all tokens in `@theme` (no `tailwind.config.mjs`) |

### 20.2 Don't

| # | Don't |
|---|-------|
| 1 | Hardcode hex colors in components |
| 2 | Use `dark:` variants manually (except `dark:prose-invert`) |
| 3 | Create `tailwind.config.mjs` |
| 4 | Add `@astrojs/tailwind` integration |
| 5 | Use `!important` |
| 6 | Skip heading levels (H1 → H3) |
| 7 | Use color alone to convey meaning |
| 8 | Animate on page load |
| 9 | Use `focus:` instead of `focus-visible:` |
| 10 | Use desktop-first breakpoints (`max-*`) |

---

## 21. Change Log

| Version | Date | Changes |
|---------|------|---------|
| 1.3.0 | 2026-11-04 | Synced with `blueprint.md` v1.3.0 after Phase 5: `Project Version` bumped to 0.5.0; no changes to tokens, `@theme` block (§18), or `global.css` (§19) — already correct; verified `@theme` §18 and `global.css` §19 still match `blueprint.md` §5.9 and §5.10 exactly. |
| 1.2.0 | 2026-11-04 | Synced with `blueprint.md` v1.2.0: Tailwind 4 CSS-first config (`@theme` in `global.css`, no `tailwind.config.mjs`); removed `darkMode: 'media'` (Tailwind 4 uses CSS variables); §18 rewritten as "Tailwind 4 Theme Reference"; §19 full `global.css` with `@import "tailwindcss"` + `@plugin` + `@theme`; §11.4 card now uses `border-border`; `container-page` utility documented; Do/Don't updated. |
| 1.1.0 | 2026-10-26 | Dark mode via CSS variables; §18 Tailwind config uses `var(--color-*)`; §19 full CSS variables; §9.2 "How Dark Mode Works"; `prose dark:prose-invert` documented as only allowed exception. |
| 1.0.1 | 2026-10-26 | Document Info split into `Document Version` vs `Project Version`. |
| 1.0.0 | 2026-10-26 | Initial design system. |

---

*End of document.*