#!/usr/bin/env python3
"""Regression tests for the dependency-free workflow audit command."""

from __future__ import annotations

import json
import subprocess
import sys
import time
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "audit-workflow.py"
FIXTURES = ROOT / "tests" / "fixtures"


def run_audit(fixture: str, *options: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPT), *options, str(FIXTURES / fixture)],
        check=False,
        capture_output=True,
        text=True,
    )


class AuditWorkflowTests(unittest.TestCase):
    def test_complete_fixture_passes_in_human_mode(self) -> None:
        result = run_audit("pass-complete")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("AI workflow audit: pass", result.stdout)
        self.assertIn("Boundaries: 4/4 detected", result.stdout)
        self.assertIn("does not prove the repository is safe", result.stdout)

    def test_complete_fixture_has_deterministic_json(self) -> None:
        first = run_audit("pass-complete", "--json")
        second = run_audit("pass-complete", "--json")
        self.assertEqual(first.returncode, 0, first.stderr)
        self.assertEqual(first.stdout, second.stdout)
        payload = json.loads(first.stdout)
        self.assertEqual(payload["status"], "pass")
        self.assertEqual(payload["summary"], {"checks": 4, "findings": 0, "passed": 4})

    def test_each_required_finding_fixture(self) -> None:
        expected = {
            "no-instructions": "instruction-file-missing",
            "missing-root": "root-boundary-missing",
            "missing-private-data": "private-data-boundary-missing",
            "missing-approval": "approval-boundary-missing",
            "missing-verification": "verification-boundary-missing",
        }
        for fixture, finding_id in expected.items():
            with self.subTest(fixture=fixture):
                result = run_audit(fixture, "--json")
                self.assertEqual(result.returncode, 1, result.stderr)
                payload = json.loads(result.stdout)
                self.assertEqual([item["id"] for item in payload["findings"]], [finding_id])

    def test_missing_repository_is_a_usage_error(self) -> None:
        result = run_audit("does-not-exist", "--json")
        self.assertEqual(result.returncode, 2)
        self.assertIn("repository directory not found", result.stderr)

    def test_fixture_suite_finishes_under_one_minute(self) -> None:
        started = time.monotonic()
        for fixture in (
            "pass-complete",
            "no-instructions",
            "missing-root",
            "missing-private-data",
            "missing-approval",
            "missing-verification",
        ):
            run_audit(fixture, "--json")
        self.assertLess(time.monotonic() - started, 60)


if __name__ == "__main__":
    unittest.main(verbosity=2)
