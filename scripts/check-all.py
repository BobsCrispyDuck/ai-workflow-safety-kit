#!/usr/bin/env python3
"""Run the local repo checks."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


CHECKS = (
    ("public surface", "check-public-surface.py"),
    ("check script index", "check-checks-index.py"),
    ("scenario file", "check-scenarios.py"),
    ("eval coverage", "check-coverage.py"),
    ("rubric coverage", "check-rubric.py"),
    ("docs index", "check-docs-index.py"),
    ("local doc links", "check-links.py"),
    ("issue-template links", "check-issue-links.py"),
)


def main() -> int:
    scripts_dir = Path(__file__).resolve().parent
    failed = False

    for label, script_name in CHECKS:
        print(f"checking {label}...")
        result = subprocess.run(
            [sys.executable, str(scripts_dir / script_name)],
            check=False,
            text=True,
            capture_output=True,
        )
        if result.stdout:
            print(result.stdout.strip())
        if result.stderr:
            print(result.stderr.strip(), file=sys.stderr)
        if result.returncode != 0:
            failed = True

    if failed:
        print("error: one or more checks failed", file=sys.stderr)
        return 1

    print("ok: all local checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
