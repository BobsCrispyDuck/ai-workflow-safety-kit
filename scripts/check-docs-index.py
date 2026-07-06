#!/usr/bin/env python3
"""Check that docs/README.md lists every docs page."""

from __future__ import annotations

import sys
from pathlib import Path


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    docs_dir = repo_root / "docs"
    index_path = docs_dir / "README.md"

    if not index_path.exists():
        print(f"error: file not found: {index_path}", file=sys.stderr)
        return 1

    index_text = index_path.read_text(encoding="utf-8")
    errors: list[str] = []
    docs = sorted(path for path in docs_dir.glob("*.md") if path.name != "README.md")

    for path in docs:
        rel_path = path.relative_to(repo_root).as_posix()
        if rel_path not in index_text:
            errors.append(f"docs/README.md is missing {rel_path}")

    if errors:
        for error in errors:
            print(f"error: {error}", file=sys.stderr)
        return 1

    print(f"ok: docs index lists {len(docs)} docs")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
