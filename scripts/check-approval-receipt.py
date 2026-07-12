#!/usr/bin/env python3
"""Check that an approval-boundary receipt contains reviewable evidence."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


DEFAULT_RECEIPT = "examples/approval-boundary-receipt.md"
TEXT_SUFFIXES = {".md", ".txt"}

FIELDS = (
    ("task", ("task", "requested task", "request")),
    ("approved scope", ("approved scope", "approved action")),
    ("changed files", ("changed files", "files changed")),
    ("checks run", ("commands/checks run", "checks run", "checked")),
    ("result", ("result", "outcome")),
    ("evidence", ("evidence", "proof")),
    ("remaining risk", ("remaining risk", "remaining risks")),
    (
        "not changed or approved",
        (
            "not changed / not approved",
            "not changed or approved",
            "not approved",
            "not checked",
            "left untouched",
        ),
    ),
    (
        "next approval",
        ("next approval needed", "next approval", "approval needed"),
    ),
)

MARKDOWN_PREFIX = re.compile(r"^(?:#{1,6}\s+|[-*+]\s+)")


def collect_receipt_files(path: Path) -> list[Path]:
    if path.is_file() and path.suffix.lower() in TEXT_SUFFIXES:
        return [path]
    if path.is_dir():
        return sorted(
            candidate
            for candidate in path.rglob("*")
            if candidate.is_file()
            and candidate.suffix.lower() in TEXT_SUFFIXES
            and "receipt" in candidate.name.lower()
        )
    return []


def match_field(line: str) -> tuple[str, str] | None:
    candidate = MARKDOWN_PREFIX.sub("", line.strip(), count=1).strip()
    lowered = candidate.casefold()

    for label, aliases in FIELDS:
        for alias in sorted(aliases, key=len, reverse=True):
            lowered_alias = alias.casefold()
            if lowered == lowered_alias:
                return label, ""
            prefix = f"{lowered_alias}:"
            if lowered.startswith(prefix):
                return label, candidate[len(alias) + 1 :].strip()
    return None


def inspect_receipt(text: str) -> tuple[list[str], list[str]]:
    present: set[str] = set()
    populated: set[str] = set()
    current_field: str | None = None

    for raw_line in text.splitlines():
        stripped = raw_line.strip()
        if not stripped or stripped.startswith("```"):
            continue

        matched = match_field(stripped)
        if matched:
            current_field, inline_value = matched
            present.add(current_field)
            if inline_value:
                populated.add(current_field)
            continue

        if stripped.startswith("#"):
            current_field = None
            continue

        if current_field:
            populated.add(current_field)

    labels = [label for label, _aliases in FIELDS]
    missing = [label for label in labels if label not in present]
    empty = [label for label in labels if label in present and label not in populated]
    return missing, empty


def display_path(path: Path, repo_root: Path) -> Path:
    try:
        return path.relative_to(repo_root)
    except ValueError:
        return path


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Check approval-boundary receipts for required review fields."
    )
    parser.add_argument(
        "paths",
        nargs="*",
        help=(
            "Receipt files or directories to check. Directories include files with "
            "'receipt' in the name. Defaults to the bundled synthetic example."
        ),
    )
    parser.add_argument(
        "--allow-empty",
        action="store_true",
        help="Check field structure without requiring populated values.",
    )
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parents[1]
    input_paths = (
        [Path(path).resolve() for path in args.paths]
        if args.paths
        else [repo_root / DEFAULT_RECEIPT]
    )

    files: list[Path] = []
    errors: list[str] = []
    for path in input_paths:
        collected = collect_receipt_files(path)
        if not collected:
            errors.append(f"no receipt files found: {path}")
        files.extend(collected)

    for path in sorted(set(files)):
        missing, empty = inspect_receipt(path.read_text(encoding="utf-8"))
        shown = display_path(path, repo_root)
        for label in missing:
            errors.append(f"{shown}: missing receipt field: {label}")
        if not args.allow_empty:
            for label in empty:
                errors.append(f"{shown}: empty receipt field: {label}")
        if not missing and (args.allow_empty or not empty):
            print(f"ok: {shown}: approval-boundary receipt is reviewable")

    if errors:
        for error in errors:
            print(f"error: {error}", file=sys.stderr)
        return 1

    print(f"ok: {len(set(files))} approval-boundary receipt(s) checked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
