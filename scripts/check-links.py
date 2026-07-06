#!/usr/bin/env python3
"""Check local links and simple file references in markdown docs."""

from __future__ import annotations

import re
import sys
from pathlib import Path


MARKDOWN_LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
INLINE_CODE = re.compile(r"(?<!`)`([^`\n]+)`(?!`)")
LOCAL_EXTENSIONS = (".md", ".jsonl", ".py", ".yml", ".yaml", ".txt")


def strip_fenced_blocks(text: str) -> str:
    cleaned: list[str] = []
    in_fence = False

    for line in text.splitlines():
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if not in_fence:
            cleaned.append(line)

    return "\n".join(cleaned)


def is_external(target: str) -> bool:
    return target.startswith(("http://", "https://", "mailto:", "#"))


def normalize_target(target: str) -> str:
    return target.split("#", 1)[0].strip()


def looks_like_local_file(value: str) -> bool:
    if " " in value or value.startswith("-"):
        return False
    return value.endswith(LOCAL_EXTENSIONS) or value.startswith(".github/")


def resolve(base: Path, repo_root: Path, target: str) -> Path:
    target_path = Path(*target.replace("\\", "/").split("/"))
    if target_path.is_absolute():
        candidates = [target_path]
    else:
        candidates = [(base / target_path).resolve(), (repo_root / target_path).resolve()]

    for candidate in candidates:
        if candidate.exists():
            return candidate
    return candidates[0]


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    errors: list[str] = []
    checked = 0

    for path in sorted(repo_root.rglob("*.md")):
        if ".git" in path.parts:
            continue

        text = strip_fenced_blocks(path.read_text(encoding="utf-8"))
        rel_path = path.relative_to(repo_root).as_posix()

        candidates: list[tuple[str, str]] = []
        for match in MARKDOWN_LINK.finditer(text):
            target = normalize_target(match.group(1))
            if target and not is_external(target):
                candidates.append(("link", target))

        for match in INLINE_CODE.finditer(text):
            target = normalize_target(match.group(1))
            if looks_like_local_file(target):
                candidates.append(("reference", target))

        for kind, target in candidates:
            checked += 1
            resolved = resolve(path.parent, repo_root, target)
            try:
                resolved.relative_to(repo_root)
            except ValueError:
                errors.append(f"{rel_path}: {kind} points outside repo: {target}")
                continue
            if not resolved.exists():
                errors.append(f"{rel_path}: missing {kind}: {target}")

    if errors:
        for error in errors:
            print(f"error: {error}", file=sys.stderr)
        return 1

    print(f"ok: {checked} local doc links")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
