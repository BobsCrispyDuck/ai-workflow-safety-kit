#!/usr/bin/env python3
"""Check that public folder indexes list their pages."""

from __future__ import annotations

import sys
from pathlib import Path


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    indexed_dirs = ("docs", "templates", "checklists", "examples")
    errors: list[str] = []
    checked = 0

    for dirname in indexed_dirs:
        directory = repo_root / dirname
        index_path = directory / "README.md"

        if not index_path.exists():
            errors.append(f"file not found: {index_path.relative_to(repo_root).as_posix()}")
            continue

        index_text = index_path.read_text(encoding="utf-8")
        pages = sorted(path for path in directory.glob("*.md") if path.name != "README.md")

        for path in pages:
            checked += 1
            rel_path = path.relative_to(repo_root).as_posix()
            if rel_path not in index_text:
                index_rel = index_path.relative_to(repo_root).as_posix()
                errors.append(f"{index_rel} is missing {rel_path}")

    if errors:
        for error in errors:
            print(f"error: {error}", file=sys.stderr)
        return 1

    print(f"ok: folder indexes list {checked} pages")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
