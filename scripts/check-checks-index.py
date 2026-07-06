#!/usr/bin/env python3
"""Check that local check scripts are documented and run by check-all."""

from __future__ import annotations

import sys
from pathlib import Path


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    scripts_dir = repo_root / "scripts"
    check_all_path = scripts_dir / "check-all.py"
    local_checks_path = repo_root / "docs" / "local-checks.md"
    errors: list[str] = []

    if not check_all_path.exists():
        print(f"error: file not found: {check_all_path}", file=sys.stderr)
        return 1
    if not local_checks_path.exists():
        print(f"error: file not found: {local_checks_path}", file=sys.stderr)
        return 1

    check_all_text = check_all_path.read_text(encoding="utf-8")
    local_checks_text = local_checks_path.read_text(encoding="utf-8")
    check_scripts = sorted(path.name for path in scripts_dir.glob("check-*.py") if path.name != "check-all.py")

    for script_name in check_scripts:
        command = f"python scripts/{script_name}"
        doc_reference = f"`scripts/{script_name}`"
        if script_name not in check_all_text:
            errors.append(f"scripts/check-all.py does not run {script_name}")
        if command not in local_checks_text:
            errors.append(f"docs/local-checks.md is missing command {command}")
        if doc_reference not in local_checks_text:
            errors.append(f"docs/local-checks.md is missing section for {doc_reference}")

    if errors:
        for error in errors:
            print(f"error: {error}", file=sys.stderr)
        return 1

    print(f"ok: {len(check_scripts)} check scripts documented and wired")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
