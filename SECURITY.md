# Security Policy

---

## Document Information

| Property | Value |
|----------|-------|
| Document Version | 1.1.0 |
| Project Version | 1.0.0 (Production) |
| Last Updated | 2026-10-27 |
| Status | Active |
| Repository | `katalogarkan/katalogarkan.github.io` |
| Hosting | GitHub Pages (static) |
| Contact | (add when ready) |

---

## Table of Contents

1. [Supported Versions](#1-supported-versions)
2. [Reporting a Vulnerability](#2-reporting-a-vulnerability)
3. [Scope](#3-scope)
4. [Response Timeline](#4-response-timeline)
5. [Disclosure Policy](#5-disclosure-policy)
6. [Security Architecture](#6-security-architecture)
7. [Known Limitations](#7-known-limitations)
8. [Contributor Rules](#8-contributor-rules)
9. [Change Log](#9-change-log)

---

## 1. Supported Versions

Only the latest version (`main` branch) is supported.

| Version | Supported |
|---------|:---:|
| `main` (latest) | ✅ |
| `1.0.x` | ✅ |
| `< 1.0.0` | ❌ |

---

## 2. Reporting a Vulnerability

**Do NOT open a public issue for security vulnerabilities.**

| Method | How |
|--------|-----|
| **GitHub Security Advisory** (preferred) | [Open private advisory](https://github.com/katalogarkan/katalogarkan.github.io/security/advisories/new) |
| **Email** | (add when ready) — subject: `[SECURITY] katalogarkan` |
| **GitHub DM** | Contact [@katalogarkan](https://github.com/katalogarkan) directly |

### What to Include

| # | Information |
|---|-------------|
| 1 | Description of the vulnerability |
| 2 | Steps to reproduce |
| 3 | Affected URL(s) or file(s) |
| 4 | Potential impact |
| 5 | Proof of concept (screenshot, code, request) |
| 6 | Your environment (browser, OS) |
| 7 | Suggested fix (optional) |
| 8 | Credit preference (named / anonymous) |

For sensitive reports, request a PGP key by email first — do not include exploit details in the initial message.

---

## 3. Scope

### In Scope — Report These

| Category | Examples |
|----------|----------|
| Cross-Site Scripting (XSS) | Injected script in Markdown, search input, or URL params |
| Content injection | Malicious Markdown that executes code |
| Open redirect | Link redirecting to attacker domain |
| Sensitive data exposure | API keys, credentials, or personal data in repo/build |
| Dependency vulnerabilities | Known CVE in Astro, React, Tailwind, etc. |
| Form spam bypass | Bypassing Formspree honeypot or spam filter |
| Clickjacking | Missing `X-Frame-Options` or CSP `frame-ancestors` |
| Insecure headers | Missing CSP, HSTS, `X-Content-Type-Options` |
| Supply chain attack | Compromised dependency, typosquatting, malicious PR |
| Privacy leak | Third-party service leaking visitor data |

### Out of Scope — Do Not Report

| Item | Reason |
|------|--------|
| Missing CSP | Known limitation (see §7) |
| Missing HSTS preload | GitHub Pages handles HSTS |
| Form rate limiting | Formspree handles spam |
| Email spoofing of `@katalogarkan.github.io` | Not controlled by this project |
| Social engineering | Out of scope |
| Physical attacks | Out of scope |
| Self-XSS (user pastes code) | Not a real vulnerability |
| Outdated browser warnings | Not a security issue |
| Verbose dev-mode errors | Dev-only, not in production |
| Automated scanner reports without proof | Will be closed |
| Issues already in `docs/blueprint.md` §19 | Known and accepted |

**If in doubt, report it.** A false positive is better than a missed issue.

---

## 4. Response Timeline

| Stage | Target |
|-------|--------|
| Acknowledgment | 48 hours |
| Initial assessment | 5 business days |
| Fix — Critical | 7 days |
| Fix — High | 14 days |
| Fix — Medium | 30 days |
| Fix — Low | Next release |
| Public disclosure | After deploy + 7 days |

Solo-maintained project — timelines are best-effort. Critical issues prioritized.

### Severity Levels

| Severity | Description | Response |
|----------|-------------|----------|
| **Critical** | Site compromise, data theft, wide-impact XSS | 24 hours |
| **High** | Limited XSS, sensitive data exposure, dependency CVE | 7 days |
| **Medium** | Missing security headers, minor info leak | 30 days |
| **Low** | Best-practice improvements, theoretical issues | Next release |

---

## 5. Disclosure Policy

### Coordinated Disclosure

| Step | Detail |
|------|--------|
| 1 | Reporter submits privately |
| 2 | Maintainer acknowledges (48h) |
| 3 | Maintainer investigates + develops fix |
| 4 | Fix deployed to production |
| 5 | Reporter notified |
| 6 | Public disclosure after 7 days (or sooner if agreed) |

### Credit

| Preference | Result |
|------------|--------|
| Named | Listed in `CHANGELOG.md` + GitHub advisory |
| Anonymous | "Anonymous researcher" |
| No preference | Assumed anonymous |

### What We Ask

1. Do not publicly disclose before fix is deployed
2. Do not exploit beyond proof-of-concept
3. Do not access, modify, or delete data that isn't yours
4. Do not perform DoS attacks
5. Do not use automated scanners without manual verification
6. Give reasonable time to fix before disclosure

---

## 6. Security Architecture

### Static Site — No Server Runtime

katalogarkan is a static site. No server, no database, no auth, no API.

| Attack Vector | Present? | Why Not |
|---------------|:---:|---------|
| SQL Injection | ❌ | No database |
| SSRF | ❌ | No server |
| RCE | ❌ | No server runtime |
| Auth bypass | ❌ | No auth |
| Session hijacking | ❌ | No sessions |
| Privilege escalation | ❌ | No roles |
| File upload attacks | ❌ | No uploads |
| Server-side template injection | ❌ | Static HTML only |

### Remaining Attack Surface

| Vector | Mitigation |
|--------|------------|
| Client-side XSS | Astro escapes Markdown by default; no `dangerouslySetInnerHTML` |
| Content injection | Markdown files are owner-authored and reviewed |
| Dependency vulnerabilities | `npm audit` before each phase; Dependabot enabled |
| Third-party scripts | None — all JS bundled |
| Form spam | Formspree honeypot + spam filter |
| Clickjacking | GitHub Pages sends `X-Frame-Options: DENY` |
| HTTPS | Enforced by GitHub Pages (auto TLS) |
| Mixed content | All assets served over HTTPS |

### Supply Chain

| Control | Detail |
|---------|--------|
| Lockfile | `package-lock.json` committed |
| `npm ci` in CI | Installs exact versions |
| Dependabot | Enabled for security updates |
| `npm audit` | Run before each phase |
| Minimal dependencies | 8 direct dependencies |
| Pinned Node version | Node 20 in CI |

---

## 7. Known Limitations

Accepted limitations — **not vulnerabilities**:

| # | Limitation | Reason |
|---|------------|--------|
| 1 | No Content Security Policy (CSP) | Astro static + inline styles; can add later |
| 2 | No Subresource Integrity (SRI) | All JS/CSS bundled, same origin |
| 3 | No rate limiting on contact form | Formspree handles spam |
| 4 | No CAPTCHA | Honeypot + Formspree filter sufficient |
| 5 | Formspree endpoint is public | Required for client-side submission |
| 6 | Google Fonts from `fonts.googleapis.com` | Standard practice |
| 7 | No `Permissions-Policy` header | GitHub Pages limitation |
| 8 | No custom security headers | GitHub Pages limitation |
| 9 | Avatar and CV are public | Intentional — personal branding |
| 10 | No authentication | By design — static site |

**If you find a way to exploit any of these beyond accepted scope, report it.**

---

## 8. Contributor Rules

If you contribute, follow these:

### Code

| # | Rule |
|---|------|
| 1 | Never use `dangerouslySetInnerHTML` or `innerHTML` |
| 2 | Never `eval()` or `new Function()` |
| 3 | Always sanitize user input |
| 4 | Use Astro's built-in escaping — don't bypass |
| 5 | External links: `rel="noopener noreferrer"` + `target="_blank"` |
| 6 | No inline event handlers |
| 7 | No secrets in code |
| 8 | No `console.log` of sensitive data |
| 9 | Validate all frontmatter against Zod schema |
| 10 | Don't add dependencies without checking them |

### Dependencies

| # | Rule |
|---|------|
| 1 | Run `npm audit` before committing |
| 2 | Check package reputation before adding |
| 3 | Prefer recently-updated packages |
| 4 | Avoid postinstall scripts |
| 5 | Pin versions in `package.json` |
| 6 | Commit `package-lock.json` |
| 7 | Review Dependabot PRs before merging |

### Content

| # | Rule |
|---|------|
| 1 | Only add content you wrote or have rights to |
| 2 | Don't embed third-party scripts in Markdown |
| 3 | Don't link to suspicious domains |
| 4 | Don't include personal data of others without consent |
| 5 | Images must be from trusted sources |

### Pull Requests

| # | Rule |
|---|------|
| 1 | Security PRs get priority review |
| 2 | Don't include unrelated changes |
| 3 | Describe the vulnerability being fixed |
| 4 | Add regression test if possible |
| 5 | Update `CHANGELOG.md` under **Security** |

### Third-Party Services

| Service | Purpose | Data Shared | Risk |
|---------|---------|-------------|------|
| GitHub Pages | Hosting | None (static) | Low |
| GitHub Actions | CI/CD | Repo contents | Low |
| Formspree | Contact form | Name, email, message | Medium (PII) |
| Google Fonts | Inter font | IP address | Low |

**No tracking:** no analytics, no cookies, no fingerprinting.
---

*End of document.*