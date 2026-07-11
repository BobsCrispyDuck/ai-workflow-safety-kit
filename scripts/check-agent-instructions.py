#!/usr/bin/env python3
"""Check whether agent instruction files include the core guardrail themes."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


DEFAULT_FILES = (
    "AGENTS.md",
    "CLAUDE.md",
    ".github/copilot-instructions.md",
    ".cursor/rules",
    "templates/project-instructions.md",
    "examples/project-instructions-example.md",
)

TEXT_SUFFIXES = {".md", ".mdc", ".txt"}

THEMES = (
    (
        "project root",
        ("root", "workspace", "working directory", "cwd", "path", "folder"),
    ),
    (
        "private data",
        ("secret", "api key", "token", "private", "customer", "user data", "logs"),
    ),
    (
        "approval gate",
        ("approval", "approve", "confirm", "ask", "stop before", "do not"),
    ),
    (
        "verification receipt",
        ("verify", "test", "checked", "evidence", "receipt", "done"),
    ),
)


def collect_instruction_files(path: Path) -> list[Path]:
    if path.is_file():
        return [path]
    if path.is_dir():
        return sorted(
            candidate
            for candidate in path.rglob("*")
            if candidate.is_file() and candidate.suffix.lower() in TEXT_SUFFIXES
        )
    return []


def read_targets(paths: list[Path]) -> tuple[list[Path], list[str]]:
    files: list[Path] = []
    errors: list[str] = []

    for path in paths:
        if path.is_file():
            files.append(path)
            continue
        if path.is_dir():
            for name in DEFAULT_FILES:
                candidate = path / name
                files.extend(collect_instruction_files(candidate))
            continue
        errors.append(f"path not found: {path}")

    return sorted(set(files)), errors


def find_theme_hits(text: str) -> dict[str, list[str]]:
    lowered = text.lower()
    hits: dict[str, list[str]] = {}
    for label, keywords in THEMES:
        matches = [keyword for keyword in keywords if keyword in lowered]
        if matches:
            hits[label] = matches
    return hits


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Check agent instruction files for core AI-workflow guardrail themes."
    )
    parser.add_argument(
        "paths",
        nargs="*",
        help="Files or repo directories to check. Defaults to the repository root.",
    )
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parents[1]
    input_paths = [Path(path).resolve() for path in args.paths] if args.paths else [repo_root]
    files, errors = read_targets(input_paths)

    if errors:
        for error in errors:
            print(f"error: {error}", file=sys.stderr)
        return 1

    if not files:
        print("error: no known agent instruction files found", file=sys.stderr)
        print(
            "hint: pass a file path, or add AGENTS.md, CLAUDE.md, "
            ".github/copilot-instructions.md, or templates/project-instructions.md",
            file=sys.stderr,
        )
        return 1

    combined_text = "\n".join(path.read_text(encoding="utf-8") for path in files)
    hits = find_theme_hits(combined_text)
    missing = [label for label, _keywords in THEMES if label not in hits]

    print("checked instruction files:")
    for path in files:
        try:
            display = path.relative_to(repo_root)
        except ValueError:
            display = path
        print(f"- {display}")

    if missing:
        for label in missing:
            print(f"error: missing guardrail theme: {label}", file=sys.stderr)
        return 1

    for label, matches in hits.items():
        print(f"ok: {label}: {', '.join(matches[:3])}")

    print("ok: agent instructions mention the core guardrail themes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
