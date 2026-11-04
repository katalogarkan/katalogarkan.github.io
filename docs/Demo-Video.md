# katalogarkan — demo-video.md

---

## Document Information

| Property | Value |
|----------|-------|
| Document Version | 1.0.0 |
| Project Version | 0.1.0 (Phase 1 Complete) |
| Last Updated | 2026-11-04 |
| Status | Draft — Planning |
| Project | Personal branding & katalog website |
| Owner | Arkan (Full Stack Web Developer) |
| Purpose | Script & production plan for demo video |
| Target Length | 90–120 seconds |
| Format | MP4 (H.264), 1080p, 30fps |
| Audio | Voiceover + background music (optional) |
| Related | `blueprint.md` §7 (Page Content), `design-system.md` §11 (Components) |

---

## Table of Contents

1. [Purpose](#1-purpose)
2. [Video Goals](#2-video-goals)
3. [Target Audience](#3-target-audience)
4. [Distribution](#4-distribution)
5. [Video Structure](#5-video-structure)
6. [Full Script](#6-full-script)
7. [Shot List](#7-shot-list)
8. [Technical Setup](#8-technical-setup)
9. [Recording Checklist](#9-recording-checklist)
10. [Editing Guide](#10-editing-guide)
11. [Accessibility](#11-accessibility)
12. [Publishing](#12-publishing)
13. [Change Log](#13-change-log)

---

## 1. Purpose

### 1.1 What This Document Is

A complete production plan for a **90–120 second demo video** of the katalogarkan website. It covers the script, shot list, recording setup, editing guide, and publishing steps.

### 1.2 Why a Demo Video Exists

| Reason | Benefit |
|--------|---------|
| Showcase the site | Recruiters see it in action without visiting |
| Portfolio evidence | Demonstrates the full stack (Astro, Tailwind, React island, deploy) |
| LinkedIn / social sharing | Video gets more engagement than a link |
| Onboarding reference | New contributors see the intended UX |
| Regression check | Compare future versions against this baseline |

### 1.3 When to Record

| Phase | Status |
|-------|--------|
| Phase 1 | ❌ Not ready — no real content |
| Phase 2–5 | ❌ Not ready — pages incomplete |
| **Phase 6** | ✅ **Record here** — all pages complete |
| **Launch (1.0.0)** | ✅ **Re-record** with real content |

**Rule:** Record once after Phase 6 (structure complete), re-record after launch (real projects/articles). Keep both versions.

---

## 2. Video Goals

| # | Goal | Measure |
|---|------|---------|
| 1 | Show the full site in under 2 minutes | Video length ≤ 120s |
| 2 | Highlight the katalog filter (React island) | Filter interaction shown |
| 3 | Demonstrate dark mode | Theme switch shown |
| 4 | Show responsive design | Mobile + desktop shown |
| 5 | Prove the stack works | Live URL shown, no errors |
| 6 | Be shareable | ≤ 50MB, 1080p, captions included |

### 2.1 Non-Goals

| # | Non-Goal | Why Not |
|---|----------|---------|
| 1 | Tutorial / how-to | Not a course |
| 2 | Code walkthrough | Too long, not visual |
| 3 | Marketing ad | Keep it honest, no hype |
| 4 | Multi-language | English only (per `blueprint.md` §3.2) |

---

## 3. Target Audience

| Audience | What They Care About |
|----------|---------------------|
| Recruiters | Does this person build real, working sites? |
| Potential clients | Is the work polished and functional? |
| Other developers | What stack, how is it built? |
| Arkan (future self) | Reference for what the site looked like |

**Tone:** Professional, calm, no hype. Let the site speak.

---

## 4. Distribution

| Platform | Format | Notes |
|----------|--------|-------|
| GitHub README | Embedded GIF or link | Keep GIF < 5MB, link full video |
| LinkedIn | Native video upload | 1080p, captions on |
| Personal site `/about` | Embedded `<video>` | Optional, adds weight |
| Portfolio PDF | Link | — |

**Rule:** Do not autoplay with sound. Always provide captions. Provide a static poster image.

---

## 5. Video Structure

| # | Section | Duration | Purpose |
|---|---------|:---:|---------|
| 1 | Intro / Hero | 10s | Show name + tagline |
| 2 | Katalog + Filter | 25s | Main feature — filter, search, sort |
| 3 | Project Detail | 15s | Show a case study |
| 4 | Blog | 15s | Show article list + detail |
| 5 | Dark Mode | 10s | Toggle OS theme |
| 6 | Responsive | 15s | Mobile view |
| 7 | Contact | 10s | Form + social links |
| 8 | Outro | 10s | URL + CTA |

**Total:** ~110 seconds

---

## 6. Full Script

### 6.1 Voiceover Script

> **[0:00–0:10] Intro**
>
> "Hi, I'm Arkan — a Full Stack Web Developer. This is my personal site and project katalog."

*Visual: Hero section, cursor moves to "View Katalog" button.*

> **[0:10–0:35] Katalog + Filter**
>
> "The katalog showcases projects I've built. I can filter by category, search by name or tech, and sort by date."

*Visual: Click "Katalog" in nav. Filter dropdown opens, selects "web-app". Search input types "astro". Sort changes to "oldest". Grid updates.*

> **[0:35–0:50] Project Detail**
>
> "Each project opens to a full case study — overview, problem, solution, tech stack, and links to the demo and repo."

*Visual: Click a project card. Detail page scrolls through sections.*

> **[0:50–1:05] Blog**
>
> "I also write articles — tutorials, tips, and notes — all written in Markdown and built with Astro Content Collections."

*Visual: Click "Blog" in nav. List appears. Click an article. Prose content scrolls.*

> **[1:05–1:15] Dark Mode**
>
> "The site follows your system theme. Here's what dark mode looks like."

*Visual: Switch OS to dark mode. Page updates instantly — no flash, no reload.*

> **[1:15–1:30] Responsive**
>
> "It's fully responsive — built mobile-first with Tailwind CSS."

*Visual: Open DevTools, switch to mobile viewport (375px). Hamburger menu opens. Pages stack cleanly.*

> **[1:30–1:40] Contact**
>
> "And if you want to work together, the contact form reaches me directly."

*Visual: Click "Contact". Form fields shown. Cursor hovers submit button.*

> **[1:40–1:50] Outro**
>
> "Built with Astro, Tailwind CSS, and React. Hosted for free on GitHub Pages. Visit katalogarkan.github.io."

*Visual: Hero again. URL appears as text overlay. Fade to black.*

### 6.2 Timing Table

| Time | Section | Voiceover | Visual |
|------|---------|-----------|--------|
| 0:00–0:10 | Intro | "Hi, I'm Arkan..." | Hero |
| 0:10–0:35 | Katalog | "The katalog showcases..." | Filter interaction |
| 0:35–0:50 | Detail | "Each project opens..." | Detail scroll |
| 0:50–1:05 | Blog | "I also write articles..." | Blog list + detail |
| 1:05–1:15 | Dark mode | "The site follows..." | Theme switch |
| 1:15–1:30 | Responsive | "It's fully responsive..." | Mobile viewport |
| 1:30–1:40 | Contact | "And if you want..." | Contact form |
| 1:40–1:50 | Outro | "Built with Astro..." | Hero + URL |

### 6.3 Text Overlays

| Time | Overlay | Position |
|------|---------|----------|
| 0:00 | "Arkan — Full Stack Web Developer" | Bottom left |
| 0:10 | "Katalog — Filter, Search, Sort" | Bottom left |
| 0:35 | "Project Case Study" | Bottom left |
| 0:50 | "Blog — Markdown + Content Collections" | Bottom left |
| 1:05 | "Dark Mode — prefers-color-scheme" | Bottom left |
| 1:15 | "Responsive — Mobile-first" | Bottom left |
| 1:30 | "Contact — Formspree" | Bottom left |
| 1:40 | "katalogarkan.github.io" | Center |

**Style:** Small, muted text, bottom-left. No large title cards (keeps it clean).

---

## 7. Shot List

### 7.1 Shot Table

| # | Shot | Duration | Viewport | Action |
|---|------|:---:|----------|--------|
| 1 | Hero | 5s | 1440×900 | Static, cursor enters |
| 2 | Nav to Katalog | 3s | 1440×900 | Click "Katalog" |
| 3 | Filter dropdown | 5s | 1440×900 | Open, select "web-app" |
| 4 | Search input | 5s | 1440×900 | Type "astro" |
| 5 | Sort change | 3s | 1440×900 | Change to "oldest" |
| 6 | Filtered grid | 4s | 1440×900 | Grid updates, hover card |
| 7 | Click project | 2s | 1440×900 | Click card |
| 8 | Detail scroll | 10s | 1440×900 | Scroll through sections |
| 9 | Nav to Blog | 2s | 1440×900 | Click "Blog" |
| 10 | Blog list | 3s | 1440×900 | Hover card |
| 11 | Click article | 2s | 1440×900 | Click card |
| 12 | Article scroll | 8s | 1440×900 | Scroll prose |
| 13 | Dark mode switch | 5s | 1440×900 | OS theme change |
| 14 | Dark home | 5s | 1440×900 | Scroll hero |
| 15 | Mobile viewport | 3s | 375×812 | DevTools toggle |
| 16 | Mobile menu | 5s | 375×812 | Open hamburger |
| 17 | Mobile katalog | 4s | 375×812 | Scroll grid |
| 18 | Mobile detail | 3s | 375×812 | Scroll detail |
| 19 | Nav to Contact | 2s | 1440×900 | Click "Contact" |
| 20 | Contact form | 5s | 1440×900 | Hover fields, submit |
| 21 | Outro | 5s | 1440×900 | Hero + URL overlay |

**Total:** ~90s of raw footage → ~110s edited (with transitions).

### 7.2 What to Show vs Skip

| Show | Skip |
|------|------|
| Katalog filter | About page bio (text-heavy) |
| Project detail | Services page (not core) |
| Blog list + article | Resources page (empty at launch) |
| Dark mode | Testimonials (empty) |
| Mobile menu | Skills page (static) |
| Contact form | Footer details |

**Rule:** Show features that are interactive or visually distinct. Skip static text pages unless they have real content.

---

## 8. Technical Setup

### 8.1 Screen Recording

| Tool | Platform | Notes |
|------|----------|-------|
| OBS Studio | Windows / macOS / Linux | Free, full control |
| Loom | Browser | Quick, cloud-hosted |
| ScreenFlow | macOS | Paid, polished |
| Windows Game Bar | Windows | Built-in, basic |

**Recommended:** OBS Studio (free, 1080p, 30fps, no watermark).

### 8.2 Recording Settings

| Setting | Value |
|---------|-------|
| Resolution | 1920×1080 |
| Frame rate | 30fps |
| Format | MP4 (H.264) |
| Bitrate | 8000–10000 kbps |
| Audio | 48kHz, stereo (if voiceover) |
| Cursor | Visible, highlighted |

### 8.3 Browser Setup

| Setting | Value |
|---------|-------|
| Browser | Chrome or Edge (consistent) |
| Zoom | 100% |
| Window size | 1440×900 (desktop), 375×812 (mobile) |
| Extensions | Disabled (clean look) |
| Bookmarks bar | Hidden |
| DevTools | Closed (except mobile shot) |
| Theme | Light (start), dark (later) |
| Cache | Cleared (fresh load) |

### 8.4 Voiceover

| Property | Value |
|----------|-------|
| Microphone | USB condenser (e.g., Blue Yeti) or headset |
| Room | Quiet, soft surfaces (no echo) |
| Recording | Separate track, synced in editing |
| Script | Read from §6.1, natural pace |
| Music | Royalty-free, low volume (optional) |

**Free music sources:** YouTube Audio Library, Pixabay Music, Free Music Archive.

---

## 9. Recording Checklist

### 9.1 Before Recording

| # | Check | Done |
|---|-------|:---:|
| 1 | Site deployed and live at `katalogarkan.github.io` | ☐ |
| 2 | At least 3 projects in katalog | ☐ |
| 3 | At least 1 article published (not draft) | ☐ |
| 4 | Dark mode works (test OS switch) | ☐ |
| 5 | Mobile view works (test DevTools) | ☐ |
| 6 | Contact form works (test submission) | ☐ |
| 7 | No console errors | ☐ |
| 8 | Browser window 1440×900 | ☐ |
| 9 | Extensions disabled | ☐ |
| 10 | Cache cleared | ☐ |
| 11 | Script printed / on second screen | ☐ |
| 12 | Microphone tested | ☐ |
| 13 | Recording software tested (10s test clip) | ☐ |

### 9.2 During Recording

| # | Rule |
|---|------|
| 1 | Move cursor slowly and deliberately |
| 2 | Pause 1s after each click (for editing) |
| 3 | No fast scrolling — smooth only |
| 4 | Re-record any mistake (don't edit around it) |
| 5 | Record each section separately (easier to edit) |
| 6 | Keep browser at 100% zoom |
| 7 | No notifications (enable Do Not Disturb) |

### 9.3 After Recording

| # | Check | Done |
|---|-------|:---:|
| 1 | All sections recorded | ☐ |
| 2 | Audio synced (if voiceover) | ☐ |
| 3 | No mistakes in final takes | ☐ |
| 4 | File sizes reasonable (< 500MB raw) | ☐ |
| 5 | Backup raw footage | ☐ |

---

## 10. Editing Guide

### 10.1 Editing Tools

| Tool | Platform | Cost |
|------|----------|------|
| DaVinci Resolve | Win / macOS / Linux | Free |
| CapCut | Win / macOS / mobile | Free |
| iMovie | macOS | Free |
| Premiere Pro | Win / macOS | Paid |

**Recommended:** DaVinci Resolve (free, professional, cross-platform).

### 10.2 Edit Steps

| # | Step | Detail |
|---|------|--------|
| 1 | Import footage | All clips + audio |
| 2 | Arrange in order | Follow §6.2 timing table |
| 3 | Trim | Remove dead time, mistakes |
| 4 | Add transitions | Simple cuts only (no flashy transitions) |
| 5 | Add text overlays | Per §6.3 |
| 6 | Sync voiceover | Align audio to visuals |
| 7 | Add music (optional) | Low volume, duck under voice |
| 8 | Color correct | Match brightness across clips |
| 9 | Add captions | See §11 |
| 10 | Export | MP4, H.264, 1080p, 30fps |

### 10.3 Transitions

| Transition | Usage |
|------------|-------|
| Hard cut | Default — between sections |
| Crossfade (0.3s) | Between major sections (intro → katalog) |
| Fade to black | Outro only |

**Rule:** No zoom, spin, or flashy transitions. Keep it professional.

### 10.4 Text Overlay Style

| Property | Value |
|----------|-------|
| Font | Inter (same as site) |
| Size | 24–28px |
| Color | White with 80% black background |
| Position | Bottom-left, 40px margin |
| Duration | 2–3s per overlay |

### 10.5 Export Settings

| Setting | Value |
|---------|-------|
| Format | MP4 |
| Codec | H.264 |
| Resolution | 1920×1080 |
| Frame rate | 30fps |
| Bitrate | 8000–10000 kbps |
| Audio | AAC, 128kbps |
| File size | < 50MB (target) |

---

## 11. Accessibility

### 11.1 Captions

| # | Rule |
|---|------|
| 1 | Include burned-in captions OR provide SRT file |
| 2 | Captions match voiceover word-for-word |
| 3 | No captions on music-only sections |
| 4 | Max 2 lines per caption |
| 5 | Min 1s display per caption |

**Tool:** YouTube auto-captions + manual correction, or DaVinci Resolve subtitle track.

### 11.2 Visual Accessibility

| # | Rule |
|---|------|
| 1 | No flashing content (seizure risk) |
| 2 | Sufficient contrast for text overlays |
| 3 | No audio-only information (everything visual is also spoken) |
| 4 | Provide a static poster image with alt text |

### 11.3 Poster Image

| Property | Value |
|----------|-------|
| File | `public/videos/demo-poster.png` |
| Size | 1920×1080 |
| Content | Hero section screenshot + title |
| Alt text | "Screenshot of the katalogarkan home page" |

---

## 12. Publishing

### 12.1 File Locations

| File | Path | Purpose |
|------|------|---------|
| Video | `public/videos/demo.mp4` | Embedded on site (optional) |
| Poster | `public/videos/demo-poster.png` | Video poster |
| Captions | `public/videos/demo.vtt` | WebVTT captions |
| GIF (short) | `screenshots/demo.gif` | README preview |

**Note:** Large video files (> 50MB) should be hosted on YouTube/LinkedIn, not committed to the repo. Only commit the poster + a short GIF.

### 12.2 Embed on Site (Optional)

```html
<!-- src/pages/about.astro — optional -->
<video controls poster="/videos/demo-poster.png" preload="metadata">
  <source src="/videos/demo.mp4" type="video/mp4" />
  <track kind="captions" src="/videos/demo.vtt" srclang="en" label="English" />
  Your browser does not support the video tag.
</video>
```

**Warning:** Do not embed on Home or Katalog — it adds page weight and distracts from the content. Embed on `/about` only, or link externally.

### 12.3 GitHub README

```markdown
## Demo

[![Demo video](screenshots/demo-poster.png)](https://youtu.be/VIDEO_ID)

[Watch the full demo](https://youtu.be/VIDEO_ID) (2 min)
```

### 12.4 LinkedIn

| Property | Value |
|----------|-------|
| Format | Native upload (not a link) |
| Captions | Burned-in or uploaded SRT |
| Thumbnail | `demo-poster.png` |
| Description | "A 2-minute tour of my personal site and project katalog — built with Astro, Tailwind CSS, and React." |

### 12.5 YouTube

| Property | Value |
|----------|-------|
| Title | "katalogarkan — Personal Site Demo (Astro + Tailwind)" |
| Description | Link to site + repo + stack |
| Tags | Astro, Tailwind CSS, portfolio, web development |
| Visibility | Public |
| Captions | Auto + manual correction |

---

## 13. Change Log

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-11-04 | Initial demo video plan: goals, script, shot list, technical setup, recording checklist, editing guide, accessibility, publishing. |

---

*End of document.*