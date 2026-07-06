#!/usr/bin/env python3
"""Check that the eval coverage map matches the scenario file."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


SCENARIO_ID = re.compile(r"S\d{3}")
SCENARIO_ROW = re.compile(r"^\|\s*(S\d{3})\s*\|\s*(low|medium|high)\s*\|")


def section(text: str, heading: str) -> str:
    marker = f"## {heading}"
    start = text.find(marker)
    if start == -1:
        return ""
    next_heading = text.find("\n## ", start + len(marker))
    if next_heading == -1:
        return text[start:]
    return text[start:next_heading]


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    scenario_path = repo_root / "evals" / "scenarios.jsonl"
    coverage_path = repo_root / "evals" / "coverage.md"
    errors: list[str] = []
    scenarios: dict[str, str] = {}

    if not scenario_path.exists():
        print(f"error: file not found: {scenario_path}", file=sys.stderr)
        return 1
    if not coverage_path.exists():
        print(f"error: file not found: {coverage_path}", file=sys.stderr)
        return 1

    for line_number, raw_line in enumerate(scenario_path.read_text(encoding="utf-8").splitlines(), start=1):
        if not raw_line.strip():
            continue
        try:
            scenario = json.loads(raw_line)
        except json.JSONDecodeError:
            continue
        scenario_id = scenario.get("id")
        risk = scenario.get("risk")
        if isinstance(scenario_id, str) and isinstance(risk, str):
            scenarios[scenario_id] = risk

    coverage = coverage_path.read_text(encoding="utf-8")
    current_coverage = section(coverage, "Current Coverage")
    scenario_list = section(coverage, "Scenario List")

    current_ids = set(SCENARIO_ID.findall(current_coverage))
    listed_rows: dict[str, str] = {}

    for raw_line in scenario_list.splitlines():
        match = SCENARIO_ROW.match(raw_line.strip())
        if not match:
            continue
        scenario_id, risk = match.groups()
        if scenario_id in listed_rows:
            errors.append(f"duplicate scenario list row: {scenario_id}")
        listed_rows[scenario_id] = risk

    scenario_ids = set(scenarios)
    listed_ids = set(listed_rows)

    for scenario_id in sorted(scenario_ids - current_ids):
        errors.append(f"{scenario_id} is missing from Current Coverage")
    for scenario_id in sorted(current_ids - scenario_ids):
        errors.append(f"{scenario_id} appears in Current Coverage but not scenarios.jsonl")
    for scenario_id in sorted(scenario_ids - listed_ids):
        errors.append(f"{scenario_id} is missing from Scenario List")
    for scenario_id in sorted(listed_ids - scenario_ids):
        errors.append(f"{scenario_id} appears in Scenario List but not scenarios.jsonl")

    for scenario_id in sorted(scenario_ids & listed_ids):
        if listed_rows[scenario_id] != scenarios[scenario_id]:
            errors.append(
                f"{scenario_id} risk mismatch: coverage has {listed_rows[scenario_id]}, "
                f"scenarios.jsonl has {scenarios[scenario_id]}"
            )

    if errors:
        for error in errors:
            print(f"error: {error}", file=sys.stderr)
        return 1

    print(f"ok: coverage maps {len(scenario_ids)} scenarios")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
