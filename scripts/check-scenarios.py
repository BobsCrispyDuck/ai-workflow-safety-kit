#!/usr/bin/env python3
"""Check the synthetic eval scenario file."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


REQUIRED_FIELDS = ("id", "name", "input", "expected_behavior", "risk")
ALLOWED_FIELDS = set(REQUIRED_FIELDS)
ALLOWED_RISKS = {"low", "medium", "high"}
SCENARIO_ID = re.compile(r"^S\d{3}$")


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    scenario_path = Path(sys.argv[1]) if len(sys.argv) > 1 else repo_root / "evals" / "scenarios.jsonl"
    errors: list[str] = []
    ids: set[str] = set()
    ordered_ids: list[tuple[int, str]] = []
    count = 0

    if not scenario_path.exists():
        print(f"error: file not found: {scenario_path}", file=sys.stderr)
        return 1

    for line_number, raw_line in enumerate(scenario_path.read_text(encoding="utf-8").splitlines(), start=1):
        line = raw_line.strip()
        if not line:
            continue

        count += 1
        try:
            scenario = json.loads(line)
        except json.JSONDecodeError as exc:
            errors.append(f"line {line_number}: invalid JSON: {exc.msg}")
            continue

        if not isinstance(scenario, dict):
            errors.append(f"line {line_number}: scenario must be a JSON object")
            continue

        for field in REQUIRED_FIELDS:
            value = scenario.get(field)
            if not isinstance(value, str) or not value.strip():
                errors.append(f"line {line_number}: missing or empty string field '{field}'")

        extra_fields = sorted(set(scenario) - ALLOWED_FIELDS)
        if extra_fields:
            errors.append(f"line {line_number}: unexpected field(s): {', '.join(extra_fields)}")

        scenario_id = scenario.get("id")
        if isinstance(scenario_id, str):
            if not SCENARIO_ID.fullmatch(scenario_id):
                errors.append(f"line {line_number}: id should look like S001")
            if scenario_id in ids:
                errors.append(f"line {line_number}: duplicate id '{scenario_id}'")
            ids.add(scenario_id)
            ordered_ids.append((line_number, scenario_id))

        risk = scenario.get("risk")
        if isinstance(risk, str) and risk not in ALLOWED_RISKS:
            errors.append(f"line {line_number}: risk must be low, medium, or high")

    if count == 0:
        errors.append("no scenarios found")

    for index, (line_number, scenario_id) in enumerate(ordered_ids, start=1):
        expected_id = f"S{index:03d}"
        if scenario_id != expected_id:
            errors.append(f"line {line_number}: expected id '{expected_id}' but found '{scenario_id}'")

    if errors:
        for error in errors:
            print(f"error: {error}", file=sys.stderr)
        return 1

    print(f"ok: {count} scenarios")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
