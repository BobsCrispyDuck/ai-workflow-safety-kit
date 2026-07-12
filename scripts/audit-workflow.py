#!/usr/bin/env python3
"""Audit a repository for basic AI-workflow instruction boundaries."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path
from types import ModuleType


EXIT_SUCCESS = 0
EXIT_FINDINGS = 1
EXIT_USAGE = 2
EXIT_INTERNAL = 3


def load_instruction_checker() -> ModuleType:
    checker_path = Path(__file__).with_name("check-agent-instructions.py")
    spec = importlib.util.spec_from_file_location("check_agent_instructions", checker_path)
    if spec is None or spec.loader is None:
        raise RuntimeError("could not load the agent-instruction checker")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def audit(repo: Path) -> dict[str, object]:
    checker = load_instruction_checker()
    files, errors = checker.read_targets([repo])
    if errors:
        raise ValueError(errors[0])

    findings: list[dict[str, str]] = []
    checks: list[dict[str, object]] = []
    if not files:
        findings.append(
            {
                "id": "instruction-file-missing",
                "boundary": "instruction file",
                "message": "No known agent instruction file was found.",
            }
        )
        hits: dict[str, list[str]] = {}
    else:
        combined_text = "\n".join(path.read_text(encoding="utf-8") for path in files)
        hits = checker.find_theme_hits(combined_text)

    finding_ids = {
        "project root": "root-boundary-missing",
        "private data": "private-data-boundary-missing",
        "approval gate": "approval-boundary-missing",
        "verification receipt": "verification-boundary-missing",
    }
    for label, _keywords in checker.THEMES:
        matched = hits.get(label, [])
        passed = bool(matched)
        checks.append(
            {
                "boundary": label,
                "passed": passed,
                "matched_keywords": matched,
            }
        )
        if files and not passed:
            findings.append(
                {
                    "id": finding_ids[label],
                    "boundary": label,
                    "message": f"Agent instructions do not mention the {label} boundary.",
                }
            )

    relative_files = [path.relative_to(repo).as_posix() for path in files]
    return {
        "schema_version": 1,
        "repository": str(repo),
        "instruction_files": relative_files,
        "status": "pass" if not findings else "findings",
        "summary": {
            "checks": len(checks),
            "passed": sum(1 for check in checks if check["passed"]),
            "findings": len(findings),
        },
        "checks": checks,
        "findings": findings,
        "disclaimer": "This smoke audit does not prove the repository is safe.",
    }


def render_human(result: dict[str, object]) -> str:
    summary = result["summary"]
    lines = [
        f"AI workflow audit: {result['status']}",
        f"Repository: {result['repository']}",
        "Instruction files: " + (", ".join(result["instruction_files"]) or "none"),
        f"Boundaries: {summary['passed']}/{summary['checks']} detected",
    ]
    for check in result["checks"]:
        marker = "PASS" if check["passed"] else "FINDING"
        lines.append(f"- {marker}: {check['boundary']}")
    if result["findings"]:
        lines.append("Findings:")
        for finding in result["findings"]:
            lines.append(f"- {finding['id']}: {finding['message']}")
    lines.append(str(result["disclaimer"]))
    return "\n".join(lines)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Read-only smoke audit of repository AI-workflow boundaries.",
        epilog="Exit codes: 0 pass, 1 findings, 2 usage error, 3 internal error.",
    )
    parser.add_argument("--json", action="store_true", help="emit deterministic JSON")
    parser.add_argument("repository", help="repository directory to audit")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    repo = Path(args.repository).resolve()
    if not repo.is_dir():
        print(f"error: repository directory not found: {repo}", file=sys.stderr)
        return EXIT_USAGE
    try:
        result = audit(repo)
    except (OSError, UnicodeError, RuntimeError) as error:
        print(f"error: audit failed: {error}", file=sys.stderr)
        return EXIT_INTERNAL
    except ValueError as error:
        print(f"error: {error}", file=sys.stderr)
        return EXIT_USAGE

    if args.json:
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        print(render_human(result))
    return EXIT_SUCCESS if result["status"] == "pass" else EXIT_FINDINGS


if __name__ == "__main__":
    raise SystemExit(main())
