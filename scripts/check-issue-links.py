#!/usr/bin/env python3
"""Check GitHub issue-template links used in docs."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import parse_qs, urlparse


MARKDOWN_EXTENSIONS = {".md", ".yml", ".yaml"}
ISSUE_LINK = re.compile(r"https://github\.com/BobsCrispyDuck/ai-workflow-safety-kit/issues/new\?([^\s)]+)")
SKIP_DIRS = {".git", ".pytest_cache", "__pycache__"}


def should_scan(path: Path, repo_root: Path) -> bool:
    rel_parts = path.relative_to(repo_root).parts
    return path.suffix in MARKDOWN_EXTENSIONS and not any(part in SKIP_DIRS for part in rel_parts)


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    template_dir = repo_root / ".github" / "ISSUE_TEMPLATE"
    errors: list[str] = []
    checked = 0

    for path in sorted(repo_root.rglob("*")):
        if not path.is_file() or not should_scan(path, repo_root):
            continue

        rel_path = path.relative_to(repo_root).as_posix()
        text = path.read_text(encoding="utf-8")

        for line_number, line in enumerate(text.splitlines(), start=1):
            for match in ISSUE_LINK.finditer(line):
                query = match.group(1)
                parsed = parse_qs(urlparse(f"https://example.invalid/?{query}").query)
                template_names = parsed.get("template", [])
                if not template_names:
                    errors.append(f"{rel_path}:{line_number}: issue link has no template query")
                    continue

                for template_name in template_names:
                    checked += 1
                    if "/" in template_name or "\\" in template_name:
                        errors.append(f"{rel_path}:{line_number}: invalid issue template path: {template_name}")
                        continue
                    template_path = template_dir / template_name
                    if not template_path.exists():
                        errors.append(f"{rel_path}:{line_number}: missing issue template: {template_name}")

    if errors:
        for error in errors:
            print(f"error: {error}", file=sys.stderr)
        return 1

    print(f"ok: {checked} issue-template links")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
