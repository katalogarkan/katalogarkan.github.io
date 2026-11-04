# Security Policy

## Supported Versions

Currently, only the latest version of this project is supported with security updates.

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |
| < 1.0   | :x:                |

## Reporting a Vulnerability

If you discover a potential security vulnerability in this project, please **do not** create a public GitHub issue.

Instead, please send an email directly to **arkantsabit025@gmail.com** with the following details:
- Type of vulnerability
- Steps to reproduce the issue
- Potential impact

I will acknowledge your email within 48 hours and provide a timeline for a fix if the vulnerability is confirmed.

## Security Best Practices Implemented

This project is a static website but still adheres to the following security practices:

1. **No Hardcoded Secrets:** Sensitive information (such as Form IDs or API endpoints) is handled securely.
2. **Serverless Forms:** The contact and testimonial forms use Google Apps Script, keeping the backend logic out of the client-side code.
3. **Dependencies:** Dependencies are regularly updated to their latest secure versions. `npm audit` is run before major deployments.
4. **External Links:** All external links use `target="_blank"` with `rel="noopener noreferrer"` to prevent tabnabbing.
5. **HTTPS:** The site is served exclusively over HTTPS via GitHub Pages.
6. **No Third-Party Trackers:** No invasive third-party analytics or tracking scripts are used.