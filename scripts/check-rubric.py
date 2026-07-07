#!/usr/bin/env python3
"""Check that every eval scenario has a rubric scoring note."""

from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    scenario_path = repo_root / "evals" / "scenarios.jsonl"
    rubric_path = repo_root / "evals" / "rubric.md"
    errors: list[str] = []
    scenarios: list[tuple[str, str]] = []

    if not scenario_path.exists():
        print(f"error: file not found: {scenario_path}", file=sys.stderr)
        return 1
    if not rubric_path.exists():
        print(f"error: file not found: {rubric_path}", file=sys.stderr)
        return 1

    for line_number, raw_line in enumerate(scenario_path.read_text(encoding="utf-8").splitlines(), start=1):
        if not raw_line.strip():
            continue
        try:
            scenario = json.loads(raw_line)
        except json.JSONDecodeError:
            continue

        scenario_id = scenario.get("id")
        name = scenario.get("name")
        if isinstance(scenario_id, str) and isinstance(name, str) and name.strip():
            scenarios.append((scenario_id, name.strip()))
        else:
            errors.append(f"line {line_number}: scenario is missing id or name")

    rubric = rubric_path.read_text(encoding="utf-8").lower()

    for scenario_id, name in scenarios:
        marker = f"scenario: {name.lower()}"
        if marker not in rubric:
            errors.append(f"{scenario_id} is missing rubric note: {marker}")

    if errors:
        for error in errors:
            print(f"error: {error}", file=sys.stderr)
        return 1

    print(f"ok: rubric covers {len(scenarios)} scenarios")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
