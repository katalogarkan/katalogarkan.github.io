# setup_project.py
"""
Setup script for katalogarkan Project.

Creates project structure, configuration files, and base Astro components
for the personal branding website.

SAFE: Will NOT overwrite any existing files.
"""

import os
import subprocess
import sys
from pathlib import Path


class Colors:
    """Terminal color codes."""
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    BOLD = '\033[1m'
    END = '\033[0m'


class ProjectSetup:
    """Project setup and configuration manager."""

    def __init__(self):
        self.project_root = Path.cwd()
        self.created_count = 0
        self.skipped_count = 0

    def print_header(self, text: str) -> None:
        print(f"\n{Colors.CYAN}{'=' * 70}{Colors.END}")
        print(f"{Colors.BOLD}{Colors.BLUE}{text}{Colors.END}")
        print(f"{Colors.CYAN}{'=' * 70}{Colors.END}\n")

    def print_section(self, text: str) -> None:
        print(f"\n{Colors.YELLOW}{text}{Colors.END}")
        print(f"{Colors.YELLOW}{'-' * 50}{Colors.END}")

    def print_status(self, text: str, status: str, detail: str = "") -> None:
        """Print status: CREATED, SKIPPED, or FAILED."""
        if status == "CREATED":
            color = Colors.GREEN
            icon = "[CREATED]"
            self.created_count += 1
        elif status == "SKIPPED":
            color = Colors.CYAN
            icon = "[SKIPPED]"
            self.skipped_count += 1
        else:
            color = Colors.RED
            icon = "[FAILED]"
            
        print(f"  {color}{icon} {text}{Colors.END}")
        if detail:
            print(f"     {Colors.CYAN}-> {detail}{Colors.END}")

    def safe_write(self, filepath: Path, content: str) -> bool:
        """Write file ONLY if it doesn't exist."""
        if filepath.exists():
            self.print_status(str(filepath.relative_to(self.project_root)), "SKIPPED", "File already exists")
            return True
        
        try:
            filepath.parent.mkdir(parents=True, exist_ok=True)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content.strip() + "\n")
            self.print_status(str(filepath.relative_to(self.project_root)), "CREATED")
            return True
        except Exception as e:
            self.print_status(str(filepath.relative_to(self.project_root)), "FAILED", str(e))
            return False

    def safe_mkdir(self, dirpath: Path) -> bool:
        """Create directory if it doesn't exist."""
        if dirpath.exists():
            self.print_status(str(dirpath.relative_to(self.project_root)) + "/", "SKIPPED", "Directory already exists")
            return True
        
        try:
            dirpath.mkdir(parents=True, exist_ok=True)
            self.print_status(str(dirpath.relative_to(self.project_root)) + "/", "CREATED")
            return True
        except Exception as e:
            self.print_status(str(dirpath.relative_to(self.project_root)) + "/", "FAILED", str(e))
            return False

    def create_directory_structure(self) -> bool:
        """Create project directory structure."""
        self.print_section("Creating Directory Structure")

        directories = [
            'public/images/projects',
            'public/images/blog',
            'src/components',
            'src/content/katalog',
            'src/content/blog',
            'src/layouts',
            'src/pages/katalog',
            'src/pages/blog',
            'src/styles',
            'docs',
            'screenshots',
            '.github/workflows'
        ]

        all_created = True
        for directory in directories:
            if not self.safe_mkdir(self.project_root / directory):
                all_created = False
        return all_created

    def create_package_json(self) -> bool:
        self.print_section("Creating package.json")
        content = """
{
  "name": "katalogarkan",
  "type": "module",
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "dev": "astro dev",
    "start": "astro dev",
    "build": "astro check && astro build",
    "preview": "astro preview",
    "astro": "astro"
  },
  "dependencies": {
    "@astrojs/react": "^4.2.0",
    "@astrojs/sitemap": "^3.2.1",
    "@astrojs/tailwind": "^5.1.4",
    "@tailwindcss/typography": "^0.5.16",
    "astro": "^5.1.1",
    "react": "^19.0.0",
    "react-dom": "^19.0.0",
    "tailwindcss": "^3.4.17"
  },
  "devDependencies": {
    "@types/react": "^19.0.2",
    "@types/react-dom": "^19.0.2",
    "typescript": "^5.7.2"
  }
}
        """
        return self.safe_write(self.project_root / 'package.json', content)

    def create_astro_config(self) -> bool:
        self.print_section("Creating astro.config.mjs")
        content = """
import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';
import react from '@astrojs/react';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://katalogarkan.github.io',
  integrations: [tailwind(), react(), sitemap()],
});
        """
        return self.safe_write(self.project_root / 'astro.config.mjs', content)

    def create_tailwind_config(self) -> bool:
        self.print_section("Creating tailwind.config.mjs")
        content = """
import typography from '@tailwindcss/typography';

/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,ts,tsx,md,mdx}'],
  darkMode: 'media',
  theme: {
    extend: {
      colors: {
        primary: {
          DEFAULT: 'var(--color-primary)',
          hover: 'var(--color-primary-hover)',
        },
        bg: {
          DEFAULT: 'var(--color-bg)',
          subtle: 'var(--color-bg-subtle)',
        },
        text: {
          DEFAULT: 'var(--color-text)',
          muted: 'var(--color-text-muted)',
        },
        border: {
          DEFAULT: 'var(--color-border)',
        },
        success: 'var(--color-success)',
        warning: 'var(--color-warning)',
        danger: 'var(--color-danger)',
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', '-apple-system', 'sans-serif'],
        mono: ['ui-monospace', 'SFMono-Regular', 'Menlo', 'monospace'],
      },
      maxWidth: {
        prose: '65ch',
      },
    },
  },
  plugins: [typography],
};
        """
        return self.safe_write(self.project_root / 'tailwind.config.mjs', content)

    def create_tsconfig(self) -> bool:
        self.print_section("Creating tsconfig.json")
        content = """
{
  "extends": "astro/tsconfigs/strict",
  "compilerOptions": {
    "jsx": "react-jsx",
    "jsxImportSource": "react"
  }
}
        """
        return self.safe_write(self.project_root / 'tsconfig.json', content)

    def create_gitignore(self) -> bool:
        self.print_section("Creating .gitignore")
        content = """
# Build output
dist/
.output/

# Dependencies
node_modules/

# Astro
.astro/

# Environment variables
.env
.env.production

# macOS
.DS_Store

# Windows
Thumbs.db

# IDE
.vscode/
.idea/

# Logs
npm-debug.log*
yarn-debug.log*
yarn-error.log*

# Evidence (uncomment if you don't want to commit evidence)
# docs/evidence/
        """
        return self.safe_write(self.project_root / '.gitignore', content)

    def create_global_css(self) -> bool:
        self.print_section("Creating src/styles/global.css")
        content = """
@tailwind base;
@tailwind components;
@tailwind utilities;

@layer base {
  :root {
    color-scheme: light dark;
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
    @apply scroll-smooth;
  }

  body {
    background-color: var(--color-bg);
    color: var(--color-text);
    @apply font-sans antialiased;
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
    @apply max-w-6xl mx-auto px-4 md:px-8;
  }
}
        """
        return self.safe_write(self.project_root / 'src/styles/global.css', content)

    def create_content_config(self) -> bool:
        self.print_section("Creating src/content/config.ts")
        content = """
import { defineCollection, z } from 'astro:content';

const katalog = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    description: z.string(),
    techStack: z.array(z.string()),
    thumbnail: z.string(),
    demoUrl: z.string().url().optional(),
    repoUrl: z.string().url().optional(),
    category: z.enum(['web-app', 'landing-page', 'api', 'mobile']),
    featured: z.boolean().default(false),
    date: z.coerce.date(),
  }),
});

const blog = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    date: z.coerce.date(),
    description: z.string(),
    category: z.enum(['tutorial', 'tips', 'notes']),
    tags: z.array(z.string()).default([]),
    draft: z.boolean().default(false),
    coverImage: z.string().optional(),
  }),
});

export const collections = { katalog, blog };
        """
        return self.safe_write(self.project_root / 'src/content/config.ts', content)

    def create_base_layout(self) -> bool:
        self.print_section("Creating src/layouts/BaseLayout.astro")
        content = """
---
import '../styles/global.css';

interface Props {
  title: string;
  description?: string;
}

const { title, description = 'Personal branding & katalog website for Arkan.' } = Astro.props;
---

<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta name="description" content={description} />
    <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700&display=swap" rel="stylesheet" />
    <title>{title} — Arkan</title>
  </head>
  <body class="flex flex-col min-h-screen">
    <a href="#main" class="sr-only focus:not-sr-only focus:absolute focus:top-4 focus:left-4 focus:bg-primary focus:text-white focus:px-4 focus:py-2 focus:rounded-md z-50">
      Skip to content
    </a>
    <main id="main" class="flex-grow">
      <slot />
    </main>
  </body>
</html>
        """
        return self.safe_write(self.project_root / 'src/layouts/BaseLayout.astro', content)

    def create_temp_index(self) -> bool:
        self.print_section("Creating temporary src/pages/index.astro")
        content = """
---
import BaseLayout from '../layouts/BaseLayout.astro';
---

<BaseLayout title="Hello" description="Temporary home page">
  <div class="container-page py-24 text-center">
    <h1 class="text-4xl font-bold mb-4">Hello</h1>
    <p class="text-text-muted">Project setup successful. Ready for Phase 1.</p>
  </div>
</BaseLayout>
        """
        return self.safe_write(self.project_root / 'src/pages/index.astro', content)

    def create_deploy_workflow(self) -> bool:
        self.print_section("Creating .github/workflows/deploy.yml")
        content = """
name: Deploy to GitHub Pages

on:
  push:
    branches: [main]
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: "pages"
  cancel-in-progress: false

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Setup Node
        uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: 'npm'

      - name: Install dependencies
        run: npm ci

      - name: Build with Astro
        run: npm run build

      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: ./dist

  deploy:
    needs: build
    runs-on: ubuntu-latest
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    steps:
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
        """
        return self.safe_write(self.project_root / '.github/workflows/deploy.yml', content)

    def display_completion_summary(self) -> None:
        self.print_header("SETUP COMPLETION SUMMARY")

        print(f"\n  {Colors.BOLD}Files Created:{Colors.END} {Colors.GREEN}{self.created_count}{Colors.END}")
        print(f"  {Colors.BOLD}Files Skipped (already existed):{Colors.END} {Colors.CYAN}{self.skipped_count}{Colors.END}")

        print(f"\n  {Colors.BOLD}Next Steps:{Colors.END}")
        print(f"  1. Install dependencies:")
        print(f"     {Colors.CYAN}  npm install{Colors.END}")
        print(f"  2. Start dev server:")
        print(f"     {Colors.CYAN}  npm run dev{Colors.END}")
        print(f"  3. Open browser:")
        print(f"     {Colors.CYAN}  http://localhost:4321{Colors.END}")
        print(f"  4. Verify build:")
        print(f"     {Colors.CYAN}  npm run build{Colors.END}")
        
        print(f"\n{Colors.CYAN}{'=' * 70}{Colors.END}\n")

    def run(self) -> bool:
        self.print_header("KATALOGARKAN - PROJECT SETUP (PHASE 1)")
        print(f"Project Root: {self.project_root}")

        self.create_directory_structure()
        self.create_package_json()
        self.create_astro_config()
        self.create_tailwind_config()
        self.create_tsconfig()
        self.create_gitignore()
        self.create_global_css()
        self.create_content_config()
        self.create_base_layout()
        self.create_temp_index()
        self.create_deploy_workflow()

        self.display_completion_summary()
        return True


def main() -> None:
    try:
        setup = ProjectSetup()
        success = setup.run()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}Setup interrupted by user.{Colors.END}")
        sys.exit(1)
    except Exception as e:
        print(f"\n{Colors.RED}Error: {str(e)}{Colors.END}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()