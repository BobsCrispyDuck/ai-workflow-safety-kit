#!/usr/bin/env python3
"""Regression tests for Codex project instruction discovery inspection."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "inspect-codex-instructions.py"


def run_inspector(start: Path, *options: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPT), "--json", *options, str(start)],
        check=False,
        capture_output=True,
        text=True,
    )


def make_git_root(path: Path) -> None:
    (path / ".git").mkdir()


class InspectCodexInstructionsTests(unittest.TestCase):
    def test_root_instruction_loads(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            make_git_root(root)
            (root / "AGENTS.md").write_text("Run tests.\n", encoding="utf-8")
            result = run_inspector(root)
            self.assertEqual(result.returncode, 0, result.stderr)
            payload = json.loads(result.stdout)
            self.assertEqual(payload["instruction_chain"], ["AGENTS.md"])
            self.assertEqual(payload["selected_files"][0]["status"], "loaded")
            self.assertEqual(payload["selected_files"][0]["candidate"], "AGENTS.md")

    def test_nested_chain_is_root_to_start(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            child = root / "services" / "api"
            child.mkdir(parents=True)
            make_git_root(root)
            (root / "AGENTS.md").write_text("Root rules.\n", encoding="utf-8")
            (child / "AGENTS.md").write_text("API rules.\n", encoding="utf-8")
            payload = json.loads(run_inspector(child).stdout)
            self.assertEqual(
                payload["instruction_chain"],
                ["AGENTS.md", "services/api/AGENTS.md"],
            )

    def test_override_shadows_base_file(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            make_git_root(root)
            (root / "AGENTS.override.md").write_text("Override.\n", encoding="utf-8")
            (root / "AGENTS.md").write_text("Base.\n", encoding="utf-8")
            result = run_inspector(root)
            self.assertEqual(result.returncode, 0, result.stderr)
            payload = json.loads(result.stdout)
            selected = payload["selected_files"][0]
            self.assertEqual(selected["path"], "AGENTS.override.md")
            self.assertEqual(selected["shadowed_files"], ["AGENTS.md"])

    def test_fallback_order_is_explicit(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            make_git_root(root)
            (root / "TEAM_GUIDE.md").write_text("Team.\n", encoding="utf-8")
            (root / ".agents.md").write_text("Other.\n", encoding="utf-8")
            result = run_inspector(
                root,
                "--fallback",
                "TEAM_GUIDE.md",
                "--fallback",
                ".agents.md",
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            selected = json.loads(result.stdout)["selected_files"][0]
            self.assertEqual(selected["path"], "TEAM_GUIDE.md")
            self.assertEqual(selected["shadowed_files"], [".agents.md"])

    def test_nearest_nested_marker_becomes_root(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            outer = Path(temporary)
            inner = outer / "nested"
            start = inner / "package"
            start.mkdir(parents=True)
            make_git_root(outer)
            make_git_root(inner)
            (outer / "AGENTS.md").write_text("Outer.\n", encoding="utf-8")
            (inner / "AGENTS.md").write_text("Inner.\n", encoding="utf-8")
            payload = json.loads(run_inspector(start).stdout)
            self.assertEqual(Path(payload["project_root"]["path"]), inner)
            self.assertEqual(payload["instruction_chain"], ["AGENTS.md"])

    def test_missing_marker_checks_only_start(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            outer = Path(temporary)
            start = outer / "child"
            start.mkdir()
            (outer / "AGENTS.md").write_text("Parent.\n", encoding="utf-8")
            result = run_inspector(start)
            self.assertEqual(result.returncode, 1)
            payload = json.loads(result.stdout)
            self.assertEqual(Path(payload["project_root"]["path"]), start)
            self.assertEqual(payload["instruction_chain"], [])
            self.assertIn(
                "project-root-not-found",
                [finding["id"] for finding in payload["findings"]],
            )

    def test_empty_override_still_shadows_base(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            make_git_root(root)
            (root / "AGENTS.override.md").write_text(" \n", encoding="utf-8")
            (root / "AGENTS.md").write_text("Base.\n", encoding="utf-8")
            result = run_inspector(root)
            self.assertEqual(result.returncode, 1)
            payload = json.loads(result.stdout)
            selected = payload["selected_files"][0]
            self.assertEqual(selected["status"], "empty")
            self.assertEqual(selected["shadowed_files"], ["AGENTS.md"])
            self.assertEqual(payload["instruction_chain"], [])

    def test_file_is_truncated_at_byte_budget(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            make_git_root(root)
            (root / "AGENTS.md").write_bytes(b"abcdefgh")
            result = run_inspector(root, "--max-bytes", "4")
            self.assertEqual(result.returncode, 1)
            selected = json.loads(result.stdout)["selected_files"][0]
            self.assertEqual(selected["included_bytes"], 4)
            self.assertEqual(selected["size_bytes"], 8)
            self.assertTrue(selected["truncated"])

    def test_later_file_is_skipped_when_budget_is_exhausted(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            child = root / "child"
            child.mkdir()
            make_git_root(root)
            (root / "AGENTS.md").write_bytes(b"root")
            (child / "AGENTS.md").write_text("Child.\n", encoding="utf-8")
            payload = json.loads(run_inspector(child, "--max-bytes", "4").stdout)
            self.assertEqual(payload["selected_files"][0]["status"], "loaded")
            self.assertEqual(payload["selected_files"][1]["status"], "budget_exhausted")

    def test_no_parent_search_matches_empty_marker_list(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            child = root / "child"
            child.mkdir()
            make_git_root(root)
            (root / "AGENTS.md").write_text("Root.\n", encoding="utf-8")
            (child / "AGENTS.md").write_text("Child.\n", encoding="utf-8")
            result = run_inspector(child, "--no-parent-search")
            self.assertEqual(result.returncode, 0, result.stderr)
            payload = json.loads(result.stdout)
            self.assertEqual(payload["model"]["root_markers"], [])
            self.assertEqual(payload["instruction_chain"], ["AGENTS.md"])

    def test_zero_byte_limit_disables_project_instructions(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            make_git_root(root)
            (root / "AGENTS.md").write_text("Rules.\n", encoding="utf-8")
            result = run_inspector(root, "--max-bytes", "0")
            self.assertEqual(result.returncode, 1)
            payload = json.loads(result.stdout)
            self.assertEqual(payload["selected_files"], [])
            self.assertEqual(payload["instruction_chain"], [])
            self.assertIn(
                "project-instructions-disabled",
                [finding["id"] for finding in payload["findings"]],
            )

    def test_json_is_deterministic(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            make_git_root(root)
            (root / "AGENTS.md").write_text("Rules.\n", encoding="utf-8")
            first = run_inspector(root)
            second = run_inspector(root)
            self.assertEqual(first.returncode, 0, first.stderr)
            self.assertEqual(first.stdout, second.stdout)


if __name__ == "__main__":
    unittest.main(verbosity=2)
