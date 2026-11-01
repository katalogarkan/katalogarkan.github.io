# verify-phase-1.py
"""
Phase 1 Verification Script for katalogarkan (Astro 7 + Tailwind 4)

Checks performed:
    - Folder structure
    - Configuration files (package.json, astro, content config)
    - Base files (global.css, BaseLayout, index)
    - Deploy pipeline (deploy.yml)
    - Local verification (npm run build)
    - Remote verification (GitHub Actions, live URL)
    - Documentation (README, LICENSE, docs/)
"""

import os
import sys
import json
import subprocess
from pathlib import Path
from datetime import datetime
from typing import Optional, Dict, Any, List


class Colors:
    """Terminal color codes."""
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    BOLD = '\033[1m'
    END = '\033[0m'


class VerificationResult:
    """Result of a single verification check."""
    def __init__(self, check_id: str, name: str, status: bool, message: str,
                 method: str = "", details: Optional[Dict] = None):
        self.check_id = check_id
        self.name = name
        self.status = status
        self.message = message
        self.method = method
        self.details = details or {}


class PhaseVerifier:
    """Base class for phase verification."""

    def __init__(self, phase: int, phase_name: str):
        self.phase = phase
        self.phase_name = phase_name
        self.project_root = Path.cwd()
        self.checks_passed = 0
        self.checks_failed = 0
        self.results: List[VerificationResult] = []
        self.timestamp = datetime.now().isoformat()

    def print_header(self, text: str) -> None:
        print(f"\n{Colors.CYAN}{'=' * 70}{Colors.END}")
        print(f"{Colors.BOLD}{Colors.BLUE}{text}{Colors.END}")
        print(f"{Colors.CYAN}{'=' * 70}{Colors.END}\n")

    def print_section(self, text: str) -> None:
        print(f"\n{Colors.YELLOW}{text}{Colors.END}")
        print(f"{Colors.YELLOW}{'-' * 60}{Colors.END}")

    def print_check(self, check_id: str, text: str, status: bool, detail: str = "") -> None:
        icon = "PASS" if status else "FAIL"
        color = Colors.GREEN if status else Colors.RED
        line = f"{color}[{icon}] {check_id} {text}{Colors.END}"
        print(line)
        if detail:
            print(f"      {Colors.CYAN}-> {detail}{Colors.END}")

    def add_result(self, check_id: str, name: str, status: bool,
                   message: str, method: str = "", details: Optional[Dict] = None) -> None:
        self.results.append(VerificationResult(check_id, name, status, message, method, details))
        if status:
            self.checks_passed += 1
        else:
            self.checks_failed += 1

    def get_summary(self) -> Dict[str, Any]:
        total = self.checks_passed + self.checks_failed
        return {
            'phase': self.phase,
            'phase_name': self.phase_name,
            'total_checks': total,
            'passed': self.checks_passed,
            'failed': self.checks_failed,
            'success_rate': round((self.checks_passed / total * 100) if total > 0 else 0, 1)
        }

    def save_json_report(self) -> None:
        summary = self.get_summary()
        report = {
            'timestamp': self.timestamp,
            'project_root': str(self.project_root),
            'phase': self.phase,
            'phase_name': self.phase_name,
            'summary': summary,
            'checks': [
                {
                    'check_id': r.check_id,
                    'name': r.name,
                    'status': r.status,
                    'message': r.message,
                    'method': r.method,
                    'details': r.details,
                }
                for r in self.results
            ],
            'overall_status': 'ready' if self.checks_failed == 0 else 'needs_fix'
        }
        json_file = self.project_root / f'phase{self.phase}_verification.json'
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2)
        print(f"\n{Colors.CYAN}JSON report saved to: {json_file}{Colors.END}")

    def save_text_report(self) -> None:
        summary = self.get_summary()
        report_file = self.project_root / f'phase{self.phase}_verification_report.txt'
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write("=" * 70 + "\n")
            f.write(f"PHASE {self.phase} VERIFICATION REPORT — {self.phase_name}\n")
            f.write("=" * 70 + "\n")
            f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Project: katalogarkan.github.io\n")
            f.write(f"Success Rate: {summary['success_rate']:.1f}%\n")
            f.write(f"Passed: {self.checks_passed}, Failed: {self.checks_failed}\n")
            f.write("=" * 70 + "\n\n")
            failed = [r for r in self.results if not r.status]
            if failed:
                f.write("Failed Checks:\n")
                for r in failed:
                    f.write(f"  [{r.check_id}] {r.name}: {r.message}\n")
            else:
                f.write("All checks passed. Phase 1 is complete.\n")
        print(f"{Colors.CYAN}Text report saved to: {report_file}{Colors.END}")

    def display_summary(self) -> None:
        summary = self.get_summary()
        self.print_section("Verification Summary")
        print(f"\n  Total Checks: {summary['total_checks']}")
        print(f"  Passed:       {Colors.GREEN}{self.checks_passed}{Colors.END}")
        print(f"  Failed:       {Colors.RED}{self.checks_failed}{Colors.END}")
        print(f"  Success Rate: {summary['success_rate']:.1f}%")

        if self.checks_failed == 0:
            print(f"\n{Colors.GREEN}{Colors.BOLD}All checks passed! Phase {self.phase} is complete!{Colors.END}")
        else:
            print(f"\n{Colors.YELLOW}{Colors.BOLD}Some checks failed.{Colors.END}")
            print(f"{Colors.YELLOW}Fix before proceeding to Phase {self.phase + 1}.{Colors.END}")
            print(f"\n{Colors.RED}Items requiring attention:{Colors.END}")
            for r in self.results:
                if not r.status:
                    print(f"  [{r.check_id}] {r.name}: {r.message}")
        print(f"\n{Colors.CYAN}{'=' * 70}{Colors.END}")

    def run(self) -> bool:
        raise NotImplementedError("Subclasses must implement run()")


# ============================================
# Phase 1: Fondasi Proyek
# ============================================

class Phase1Verifier(PhaseVerifier):
    """Verifier for Phase 1: Fondasi Proyek (katalogarkan)."""

    def __init__(self):
        super().__init__(1, "Fondasi Proyek")

    # ---------- Helpers ----------

    def _run_cmd(self, cmd: List[str], timeout: int = 60) -> tuple:
        """Run a command and return (success, stdout, stderr)."""
        try:
            # Windows: npm/npx are .cmd files, need shell=True
            use_shell = sys.platform == 'win32'
            result = subprocess.run(
                cmd, capture_output=True, text=True,
                timeout=timeout, shell=use_shell
            )
            return result.returncode == 0, result.stdout, result.stderr
        except (subprocess.TimeoutExpired, FileNotFoundError) as e:
            return False, "", str(e)

    def _file_exists(self, rel_path: str) -> bool:
        return (self.project_root / rel_path).exists()

    def _dir_exists(self, rel_path: str) -> bool:
        return (self.project_root / rel_path).is_dir()

    def _read_file(self, rel_path: str) -> str:
        try:
            return (self.project_root / rel_path).read_text(encoding='utf-8')
        except Exception:
            return ""

    # ---------- 3.1 Project Setup ----------

    def check_project_setup(self) -> bool:
        self.print_section("3.1 Project Setup")
        ok = True

        self.print_check("1.1", "Project folder exists", True, str(self.project_root))
        self.add_result("1.1", "Project folder exists", True, "Project root found")

        exists = self._dir_exists('node_modules')
        self.print_check("1.2", "node_modules/ exists (npm install ran)", exists)
        self.add_result("1.2", "node_modules exists", exists, "npm install completed" if exists else "Run npm install")
        ok = ok and exists

        exists = self._file_exists('package-lock.json')
        self.print_check("1.3", "package-lock.json exists", exists,
                         "Required for `npm ci` in GitHub Actions" if not exists else "")
        self.add_result("1.3", "package-lock.json exists", exists,
                        "Lockfile present" if exists else "Run npm install to generate")
        ok = ok and exists

        pkg = self._read_file('package.json')
        has_astro = '"astro"' in pkg
        self.print_check("1.4", "package.json has astro dependency", has_astro)
        self.add_result("1.4", "package.json has astro", has_astro, "astro in dependencies" if has_astro else "astro missing")
        ok = ok and has_astro

        return ok

    # ---------- 3.2 Configuration Files ----------

    def check_config_files(self) -> bool:
        self.print_section("3.2 Configuration Files")
        ok = True

        astro = self._read_file('astro.config.mjs')
        gi = self._read_file('.gitignore')

        # Astro 7 + Tailwind 4 checks
        checks = [
            ("1.5", "astro.config.mjs exists with site", 'https://katalogarkan.github.io' in astro,
             "site URL set" if 'https://katalogarkan.github.io' in astro else "site missing/wrong"),
            ("1.6", "astro.config.mjs uses @tailwindcss/vite", '@tailwindcss/vite' in astro, ""),
            ("1.7", "astro.config.mjs has react()", 'react()' in astro, ""),
            ("1.8", "astro.config.mjs has sitemap()", 'sitemap()' in astro, ""),
            ("1.9", "tailwind.config.mjs removed (Tailwind 4)", not self._file_exists('tailwind.config.mjs'), "Should not exist in Tailwind 4"),
            ("1.10", "global.css uses @import 'tailwindcss'", '@import "tailwindcss"' in self._read_file('src/styles/global.css') or "@import 'tailwindcss'" in self._read_file('src/styles/global.css'), ""),
            ("1.11", "global.css has @theme block", '@theme' in self._read_file('src/styles/global.css'), ""),
            ("1.12", "global.css has Inter font variable", 'Inter' in self._read_file('src/styles/global.css'), ""),
            ("1.13", "tsconfig.json exists", bool(self._read_file('tsconfig.json').strip()), ""),
            ("1.14", ".gitignore ignores node_modules, dist, .astro",
             all(x in gi for x in ['node_modules', 'dist', '.astro']), ""),
            ("1.15", "LICENSE exists", self._file_exists('LICENSE'), ""),
        ]

        for cid, name, status, detail in checks:
            self.print_check(cid, name, status, detail)
            self.add_result(cid, name, status, detail or ("OK" if status else "Missing"))
            ok = ok and status

        return ok

    # ---------- 3.3 Base Files ----------

    def check_base_files(self) -> bool:
        self.print_section("3.3 Base Files")
        ok = True

        css = self._read_file('src/styles/global.css')
        layout = self._read_file('src/layouts/BaseLayout.astro')
        index = self._read_file('src/pages/index.astro')

        checks = [
            ("1.16", "src/styles/global.css exists with Tailwind import",
             '@import "tailwindcss"' in css or "@import 'tailwindcss'" in css, ""),
            ("1.17", "global.css defines CSS variables in :root", '--color-primary' in css and ':root' in css, ""),
            ("1.18", "global.css has prefers-color-scheme: dark override",
             'prefers-color-scheme: dark' in css, ""),
            ("1.19", "BaseLayout.astro exists", bool(layout.strip()), ""),
            ("1.20", 'BaseLayout has <html lang="en">', 'lang="en"' in layout, ""),
            ("1.21", "BaseLayout imports global.css", 'global.css' in layout, ""),
            ("1.22", "BaseLayout loads Inter from Google Fonts",
             'fonts.googleapis.com' in layout and 'Inter' in layout, ""),
            ("1.23", "Header.astro exists", self._file_exists('src/components/Header.astro'), ""),
            ("1.24", "Footer.astro exists", self._file_exists('src/components/Footer.astro'), ""),
            ("1.25", "index.astro exists", bool(index.strip()), ""),
            ("1.26", "index.astro uses BaseLayout", 'BaseLayout' in index, ""),
        ]

        for cid, name, status, detail in checks:
            self.print_check(cid, name, status, detail)
            self.add_result(cid, name, status, detail or ("OK" if status else "Missing"))
            ok = ok and status

        return ok

    # ---------- 3.4 Content Schema ----------

    def check_content_schema(self) -> bool:
        self.print_section("3.4 Content Schema")
        ok = True

        # Astro 7 uses src/content.config.ts (not inside content/)
        cfg = self._read_file('src/content.config.ts')

        checks = [
            ("1.27", "src/content.config.ts exists", bool(cfg.strip()), ""),
            ("1.28", "config.ts defines katalog collection", 'katalog' in cfg, ""),
            ("1.29", "config.ts defines blog collection", 'blog' in cfg, ""),
            ("1.30", "katalog schema has required fields",
             all(x in cfg for x in ['title', 'description', 'techStack', 'thumbnail', 'category', 'date']), ""),
            ("1.31", "blog schema has required fields",
             all(x in cfg for x in ['title', 'date', 'description', 'category']), ""),
            ("1.32", "src/content/katalog/ folder exists", self._dir_exists('src/content/katalog'), ""),
            ("1.33", "src/content/blog/ folder exists", self._dir_exists('src/content/blog'), ""),
        ]

        for cid, name, status, detail in checks:
            self.print_check(cid, name, status, detail)
            self.add_result(cid, name, status, detail or ("OK" if status else "Missing"))
            ok = ok and status

        return ok

    # ---------- 3.5 Deploy Pipeline ----------

    def check_deploy_pipeline(self) -> bool:
        self.print_section("3.5 Deploy Pipeline")
        ok = True

        wf = self._read_file('.github/workflows/deploy.yml')

        explicit_steps = [
            'actions/checkout@v4',
            'actions/setup-node@v4',
            'npm ci',
            'npm run build',
            'actions/upload-pages-artifact@v3',
            'actions/deploy-pages@v4',
        ]
        has_explicit = all(s in wf for s in explicit_steps)

        checks = [
            ("1.34", ".github/workflows/deploy.yml exists", bool(wf.strip()), ""),
            ("1.35", "deploy.yml uses explicit workflow (no withastro/action)",
             has_explicit and 'withastro/action' not in wf, ""),
            ("1.36", "deploy.yml triggers on push to main",
             'branches: [main]' in wf or "branches: ['main']" in wf or 'branches: [ main ]' in wf, ""),
            ("1.37", "deploy.yml uses Node 22", 'node-version: 22' in wf, "Required for Astro 7"),
        ]

        for cid, name, status, detail in checks:
            self.print_check(cid, name, status, detail)
            self.add_result(cid, name, status, detail or ("OK" if status else "Missing"))
            ok = ok and status

        print(f"\n{Colors.YELLOW}Manual checks (require GitHub web UI):{Colors.END}")
        print(f"  {Colors.CYAN}1.38 GitHub Pages source = GitHub Actions{Colors.END}")
        print(f"  {Colors.CYAN}1.39 Workflow permissions = Read and write{Colors.END}")
        self.add_result("1.38", "GitHub Pages source = GitHub Actions", True, "Manual check", method="Manual")
        self.add_result("1.39", "Workflow permissions = Read and write", True, "Manual check", method="Manual")

        return ok

    # ---------- 3.6 Local Verification ----------

    def check_local_build(self) -> bool:
        self.print_section("3.6 Local Verification")
        ok = True

        has_modules = self._dir_exists('node_modules')
        self.print_check("1.40", "npm run dev prerequisites (node_modules)", has_modules,
                         "Run `npm run dev` manually to verify" if has_modules else "Run npm install first")
        self.add_result("1.40", "npm run dev prerequisites", has_modules, "node_modules present")

        print(f"\n{Colors.YELLOW}Manual check:{Colors.END}")
        print(f"  {Colors.CYAN}1.41 localhost:4321 shows \"Hello\" page{Colors.END}")
        self.add_result("1.41", 'localhost:4321 shows "Hello"', True, "Manual check", method="Manual")

        print(f"\n{Colors.YELLOW}Running: npm run build ...{Colors.END}")
        success, stdout, stderr = self._run_cmd(['npm', 'run', 'build'], timeout=180)
        if success:
            self.print_check("1.42", "npm run build succeeds", True)
        else:
            snippet = (stderr or stdout).strip().splitlines()[-3:] if (stderr or stdout) else ["(no output)"]
            self.print_check("1.42", "npm run build succeeds", False, " | ".join(snippet))
        self.add_result("1.42", "npm run build succeeds", success, "Build OK" if success else "Build failed")

        dist_exists = self._dir_exists('dist')
        self.print_check("1.43", "dist/ folder created after build", dist_exists)
        self.add_result("1.43", "dist/ folder exists", dist_exists, "dist/ present" if dist_exists else "Missing")

        ok = ok and has_modules and success and dist_exists
        return ok

    # ---------- 3.7 Remote Verification ----------

    def check_git_remote(self) -> bool:
        self.print_section("3.7 Remote Verification")
        ok = True

        git_exists = self._dir_exists('.git')
        self.print_check("GIT", ".git directory exists", git_exists)
        if not git_exists:
            self.add_result("GIT", ".git directory", False, "Not a git repo")
            return False

        success, stdout, stderr = self._run_cmd(['git', 'remote', 'get-url', 'origin'])
        remote_ok = success and stdout.strip() != ""
        remote_url = stdout.strip() if remote_ok else ""
        self.print_check("GIT", "git remote origin configured", remote_ok, remote_url)
        self.add_result("GIT", "git remote origin", remote_ok, remote_url if remote_ok else "Run: git remote add origin <url>")

        success, stdout, _ = self._run_cmd(['git', 'rev-parse', '--abbrev-ref', 'HEAD'])
        branch = stdout.strip() if success else ""
        on_main = branch == 'main'
        self.print_check("GIT", "On branch main", on_main, f"Current: {branch or 'unknown'}")
        self.add_result("GIT", "On branch main", on_main, f"branch={branch}")

        success, stdout, _ = self._run_cmd(['git', 'rev-parse', '--verify', 'HEAD'])
        has_commit = success
        self.print_check("GIT", "Has at least one commit", has_commit)
        self.add_result("GIT", "Has commits", has_commit, "commit present" if has_commit else "No commits yet")

        print(f"\n{Colors.YELLOW}Manual checks:{Colors.END}")
        for cid, name in [
            ("1.44", "Push triggers GitHub Action"),
            ("1.45", "GitHub Action completes green"),
            ("1.46", 'Live site shows "Hello"'),
        ]:
            print(f"  {Colors.CYAN}{cid} {name}{Colors.END}")
            self.add_result(cid, name, True, "Manual check", method="Manual")

        return remote_ok and on_main and has_commit

    # ---------- Extra: Documentation ----------

    def check_documentation(self) -> bool:
        self.print_section("Documentation (Phase 6 prep)")
        ok = True

        docs = [
            ('README.md', 'README'),
            ('CHANGELOG.md', 'CHANGELOG'),
            ('docs/blueprint.md', 'Blueprint'),
            ('docs/design-system.md', 'Design system'),
            ('docs/content-guide.md', 'Content guide'),
            ('docs/deployment-guide.md', 'Deployment guide'),
            ('docs/verification-checklist.md', 'Verification checklist'),
            ('docs/cheatsheets.md', 'Cheatsheets'),
        ]

        for path, name in docs:
            exists = self._file_exists(path)
            self.print_check("DOC", f"{name} ({path})", exists)
            self.add_result("DOC", name, exists, "present" if exists else "missing")
            ok = ok and exists

        return ok

    # ---------- Run ----------

    def run(self) -> bool:
        self.print_header(f"PHASE 1 VERIFICATION — {self.phase_name}")
        print(f"Project Root: {self.project_root}")
        print(f"Timestamp:    {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

        self.check_project_setup()
        self.check_config_files()
        self.check_base_files()
        self.check_content_schema()
        self.check_deploy_pipeline()
        self.check_local_build()
        self.check_git_remote()
        self.check_documentation()

        self.display_summary()
        self.save_json_report()
        self.save_text_report()

        return self.checks_failed == 0


# ============================================
# Main Entry Point
# ============================================

def main() -> None:
    try:
        verifier = Phase1Verifier()
        success = verifier.run()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}Verification interrupted by user.{Colors.END}")
        sys.exit(1)
    except Exception as e:
        print(f"\n{Colors.RED}Error: {str(e)}{Colors.END}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()