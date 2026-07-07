#!/usr/bin/env python3
"""Check that the scenario index matches the scenario file."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


RISK_HEADING = re.compile(r"^## (High|Medium|Low) Risk$")
SCENARIO_ROW = re.compile(r"^\|\s*(S\d{3})\s*\|")
RISK_BY_HEADING = {
    "High": "high",
    "Medium": "medium",
    "Low": "low",
}


def load_scenarios(path: Path) -> tuple[dict[str, str], list[str]]:
    scenarios: dict[str, str] = {}
    errors: list[str] = []

    for line_number, raw_line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not raw_line.strip():
            continue
        try:
            scenario = json.loads(raw_line)
        except json.JSONDecodeError as exc:
            errors.append(f"{path.name}:{line_number} invalid JSON: {exc.msg}")
            continue

        scenario_id = scenario.get("id")
        risk = scenario.get("risk")
        if not isinstance(scenario_id, str):
            errors.append(f"{path.name}:{line_number} is missing a string id")
            continue
        if not isinstance(risk, str):
            errors.append(f"{scenario_id} is missing a string risk")
            continue
        scenarios[scenario_id] = risk

    return scenarios, errors


def load_index(path: Path) -> tuple[dict[str, str], list[str]]:
    indexed: dict[str, str] = {}
    errors: list[str] = []
    current_risk: str | None = None

    for line_number, raw_line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        line = raw_line.strip()
        heading_match = RISK_HEADING.match(line)
        if heading_match:
            current_risk = RISK_BY_HEADING[heading_match.group(1)]
            continue

        row_match = SCENARIO_ROW.match(line)
        if not row_match:
            continue

        scenario_id = row_match.group(1)
        if current_risk is None:
            errors.append(f"{scenario_id} appears before a risk heading")
            continue
        if scenario_id in indexed:
            errors.append(f"duplicate scenario index row: {scenario_id}")
            continue
        indexed[scenario_id] = current_risk

    return indexed, errors


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    scenario_path = repo_root / "evals" / "scenarios.jsonl"
    index_path = repo_root / "evals" / "scenario-index.md"
    errors: list[str] = []

    if not scenario_path.exists():
        print(f"error: file not found: {scenario_path}", file=sys.stderr)
        return 1
    if not index_path.exists():
        print(f"error: file not found: {index_path}", file=sys.stderr)
        return 1

    scenarios, scenario_errors = load_scenarios(scenario_path)
    indexed, index_errors = load_index(index_path)
    errors.extend(scenario_errors)
    errors.extend(index_errors)

    scenario_ids = set(scenarios)
    indexed_ids = set(indexed)

    for scenario_id in sorted(scenario_ids - indexed_ids):
        errors.append(f"{scenario_id} is missing from scenario-index.md")
    for scenario_id in sorted(indexed_ids - scenario_ids):
        errors.append(f"{scenario_id} appears in scenario-index.md but not scenarios.jsonl")

    for scenario_id in sorted(scenario_ids & indexed_ids):
        if indexed[scenario_id] != scenarios[scenario_id]:
            errors.append(
                f"{scenario_id} risk mismatch: scenario-index.md has {indexed[scenario_id]}, "
                f"scenarios.jsonl has {scenarios[scenario_id]}"
            )

    if errors:
        for error in errors:
            print(f"error: {error}", file=sys.stderr)
        return 1

    print(f"ok: scenario index covers {len(scenario_ids)} scenarios")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
