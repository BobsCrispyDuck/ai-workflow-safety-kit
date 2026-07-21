#!/usr/bin/env python3
"""Predict the Codex project instruction chain for a starting directory."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


EXIT_SUCCESS = 0
EXIT_FINDINGS = 1
EXIT_USAGE = 2
EXIT_INTERNAL = 3

DEFAULT_ROOT_MARKERS = (".git",)
DEFAULT_MAX_BYTES = 32 * 1024
PRIMARY_FILENAMES = ("AGENTS.override.md", "AGENTS.md")


def nonnegative_int(value: str) -> int:
    number = int(value)
    if number < 0:
        raise argparse.ArgumentTypeError("must be zero or greater")
    return number


def validate_relative_name(parser: argparse.ArgumentParser, value: str) -> str:
    candidate = Path(value)
    if not value or candidate.is_absolute() or ".." in candidate.parts:
        parser.error(f"candidate names must be safe relative paths: {value!r}")
    return value


def unique_names(names: list[str]) -> list[str]:
    result: list[str] = []
    for name in names:
        if name and name not in result:
            result.append(name)
    return result


def detect_root(start: Path, markers: list[str]) -> tuple[Path, str | None]:
    if not markers:
        return start, None
    for directory in (start, *start.parents):
        for marker in markers:
            if (directory / marker).exists():
                return directory, marker
    return start, None


def directories_from_root(root: Path, start: Path) -> list[Path]:
    directories = [start]
    cursor = start
    while cursor != root:
        cursor = cursor.parent
        directories.append(cursor)
    directories.reverse()
    return directories


def display_path(path: Path, root: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return str(path)


def discover_selected_files(
    directories: list[Path], candidates: list[str], root: Path
) -> list[dict[str, object]]:
    selected: list[dict[str, object]] = []
    for directory in directories:
        existing = [
            (name, directory / name)
            for name in candidates
            if (directory / name).is_file()
        ]
        if not existing:
            continue
        selected_name, selected_path = existing[0]
        selected.append(
            {
                "path": selected_path,
                "display_path": display_path(selected_path, root),
                "candidate": selected_name,
                "shadowed_files": [
                    display_path(path, root) for _name, path in existing[1:]
                ],
            }
        )
    return selected


def inspect_chain(
    start: Path,
    root_markers: list[str],
    fallback_filenames: list[str],
    max_bytes: int,
) -> dict[str, object]:
    root, matched_marker = detect_root(start, root_markers)
    candidates = unique_names([*PRIMARY_FILENAMES, *fallback_filenames])
    selected = (
        discover_selected_files(directories_from_root(root, start), candidates, root)
        if max_bytes > 0
        else []
    )

    remaining = max_bytes
    instruction_chain: list[str] = []
    findings: list[dict[str, str]] = []
    observations: list[dict[str, object]] = []
    selected_output: list[dict[str, object]] = []

    if root_markers and matched_marker is None:
        findings.append(
            {
                "id": "project-root-not-found",
                "message": "No configured project root marker was found; Codex checks only the starting directory.",
            }
        )
    if not root_markers:
        observations.append(
            {
                "id": "parent-search-disabled",
                "message": "Parent traversal is disabled, matching an empty project_root_markers list.",
            }
        )

    for item in selected:
        path = item["path"]
        output = {
            "path": item["display_path"],
            "candidate": item["candidate"],
            "shadowed_files": item["shadowed_files"],
            "status": "budget_exhausted",
            "size_bytes": None,
            "included_bytes": 0,
            "truncated": False,
        }
        if item["shadowed_files"]:
            observations.append(
                {
                    "id": "same-directory-files-shadowed",
                    "path": item["display_path"],
                    "shadowed_files": item["shadowed_files"],
                }
            )

        if remaining == 0:
            findings.append(
                {
                    "id": "instruction-budget-exhausted",
                    "message": f"{item['display_path']} is selected but not read because the byte budget is exhausted.",
                }
            )
            selected_output.append(output)
            continue

        data = path.read_bytes()
        included = data[:remaining]
        text = included.decode("utf-8", errors="replace")
        truncated = len(data) > remaining
        output["size_bytes"] = len(data)
        output["truncated"] = truncated

        if text.strip():
            output["included_bytes"] = len(included)
            output["status"] = "truncated" if truncated else "loaded"
            instruction_chain.append(str(item["display_path"]))
            remaining -= len(included)
        else:
            output["status"] = "empty"
            findings.append(
                {
                    "id": "selected-instruction-empty",
                    "message": f"{item['display_path']} wins filename precedence but contributes no instructions.",
                }
            )

        if truncated:
            findings.append(
                {
                    "id": "instruction-truncated",
                    "message": f"{item['display_path']} is truncated to {len(included)} of {len(data)} bytes.",
                }
            )
        selected_output.append(output)

    if max_bytes == 0:
        findings.append(
            {
                "id": "project-instructions-disabled",
                "message": "A zero-byte project document limit disables Codex project instruction discovery.",
            }
        )
    elif not selected:
        findings.append(
            {
                "id": "project-instructions-not-found",
                "message": "No Codex project instruction file was found on the modeled path.",
            }
        )

    return {
        "schema_version": 1,
        "tool": "inspect-codex-instructions",
        "scope": "Codex project instructions only",
        "starting_directory": str(start),
        "project_root": {
            "path": str(root),
            "matched_marker": matched_marker,
            "search_mode": "nearest configured marker" if root_markers else "current directory only",
        },
        "model": {
            "root_markers": root_markers,
            "candidate_filenames": candidates,
            "max_bytes": max_bytes,
        },
        "instruction_chain": instruction_chain,
        "selected_files": selected_output,
        "status": "findings" if findings else "pass",
        "summary": {
            "selected": len(selected_output),
            "loaded": len(instruction_chain),
            "findings": len(findings),
            "remaining_bytes": remaining,
        },
        "findings": findings,
        "observations": observations,
        "disclaimer": "This predicts project-file discovery from explicit assumptions; it does not inspect global, system, developer, session, or memory instructions.",
    }


def render_human(result: dict[str, object]) -> str:
    root = result["project_root"]
    model = result["model"]
    lines = [
        f"Codex project instructions: {result['status']}",
        f"Start: {result['starting_directory']}",
        f"Project root: {root['path']}",
        f"Root marker: {root['matched_marker'] or 'none'}",
        f"Byte budget: {model['max_bytes']}",
        "Selected files:",
    ]
    selected_files = result["selected_files"]
    if not selected_files:
        lines.append("- none")
    for item in selected_files:
        size = "unknown" if item["size_bytes"] is None else str(item["size_bytes"])
        lines.append(
            f"- {item['status'].upper()}: {item['path']} "
            f"({item['included_bytes']}/{size} bytes)"
        )
        if item["shadowed_files"]:
            lines.append(f"  shadowed: {', '.join(item['shadowed_files'])}")
    if result["findings"]:
        lines.append("Findings:")
        for finding in result["findings"]:
            lines.append(f"- {finding['id']}: {finding['message']}")
    lines.append(str(result["disclaimer"]))
    return "\n".join(lines)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Predict Codex project AGENTS.md discovery without reading global configuration.",
        epilog="Exit codes: 0 pass, 1 findings, 2 usage error, 3 internal/read error.",
    )
    parser.add_argument("start", nargs="?", default=".", help="starting directory")
    parser.add_argument("--json", action="store_true", help="emit deterministic JSON")
    parser.add_argument(
        "--max-bytes",
        type=nonnegative_int,
        default=DEFAULT_MAX_BYTES,
        help="modeled project_doc_max_bytes value",
    )
    root_group = parser.add_mutually_exclusive_group()
    root_group.add_argument(
        "--root-marker",
        action="append",
        dest="root_markers",
        help="modeled project_root_markers entry; repeat for multiple markers",
    )
    root_group.add_argument(
        "--no-parent-search",
        action="store_true",
        help="model project_root_markers = []",
    )
    parser.add_argument(
        "--fallback",
        action="append",
        default=[],
        help="modeled project_doc_fallback_filenames entry; repeat for multiple names",
    )
    args = parser.parse_args(argv)
    raw_markers = [] if args.no_parent_search else args.root_markers or list(DEFAULT_ROOT_MARKERS)
    args.root_markers = unique_names(
        [validate_relative_name(parser, value) for value in raw_markers]
    )
    args.fallback = unique_names(
        [validate_relative_name(parser, value) for value in args.fallback]
    )
    return args


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    start = Path(args.start).resolve()
    if not start.is_dir():
        print(f"error: starting directory not found: {start}", file=sys.stderr)
        return EXIT_USAGE
    try:
        result = inspect_chain(start, args.root_markers, args.fallback, args.max_bytes)
    except OSError as error:
        print(f"error: inspection failed: {error}", file=sys.stderr)
        return EXIT_INTERNAL
    if args.json:
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        print(render_human(result))
    return EXIT_SUCCESS if result["status"] == "pass" else EXIT_FINDINGS


if __name__ == "__main__":
    raise SystemExit(main())
