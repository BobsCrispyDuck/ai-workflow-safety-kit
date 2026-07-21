# Local Checks

These checks are small on purpose.

They do not prove the repo is safe. They catch the easy-to-miss stuff before a change gets pushed.

Run everything:

```text
python scripts/check-all.py
```

Run one check:

```text
python tests/test-audit-workflow.py
python tests/test-inspect-codex-instructions.py
python scripts/inspect-codex-instructions.py path/to/repo/subdirectory
python scripts/check-agent-instructions.py
python scripts/check-approval-receipt.py
python scripts/check-checks-index.py
python scripts/check-scenarios.py
python scripts/check-coverage.py
python scripts/check-scenario-index.py
python scripts/check-rubric.py
python scripts/check-docs-index.py
python scripts/check-links.py
python scripts/check-issue-links.py
python scripts/check-public-surface.py
```

## What The Checks Do

`scripts/audit-workflow.py`

Runs a read-only smoke audit against a supplied repository and synthesizes the existing agent-instruction theme checks into one human result. Use `--json` for deterministic machine-readable output:

```text
python scripts/audit-workflow.py path/to/repo
python scripts/audit-workflow.py --json path/to/repo
```

Exit code `0` means all four boundaries were detected, `1` means findings, `2` means invalid usage, and `3` means an internal/read error. A passing result does not prove a repository is safe.

`tests/test-audit-workflow.py`

Runs the synthetic regression suite for the unified audit, including a complete pass, no instruction file, and one fixture missing each guardrail boundary. The suite also checks deterministic JSON and the under-one-minute runtime requirement.

`scripts/inspect-codex-instructions.py`

Predicts the Codex project instruction chain for a starting directory. It reports the nearest configured root marker, one selected file per directory in override/base/fallback order, shadowed same-directory files, byte accounting, and truncation:

```text
python scripts/inspect-codex-instructions.py path/to/repo/subdirectory
python scripts/inspect-codex-instructions.py --json path/to/repo/subdirectory
python scripts/inspect-codex-instructions.py --root-marker .git --fallback TEAM_GUIDE.md --max-bytes 32768 path/to/repo/subdirectory
```

The defaults model Codex with `.git` as the project root marker, no fallback filenames, and a 32 KiB project-document limit. Use `--no-parent-search` to model an empty `project_root_markers` list. The tool reads no global configuration and does not claim to show global, system, developer, session, memory, or other-agent instructions.

`tests/test-inspect-codex-instructions.py`

Builds synthetic temporary repositories and checks root-to-directory order, override and fallback precedence, nested root markers, missing roots, empty selected files, byte-level truncation, exhausted budgets, disabled parent search, and deterministic JSON.

`scripts/check-agent-instructions.py`

Checks common agent instruction files for the four guardrail themes this kit expects to see before an assistant edits a repo:

- project root
- private data
- approval gate
- verification receipt

By default it checks known instruction files in this repo. You can also point it at another repo or one file:

```text
python scripts/check-agent-instructions.py path/to/repo
python scripts/check-agent-instructions.py path/to/AGENTS.md
```

This is a smoke check, not a quality score. It catches missing themes so a repo can fix the boring omission before a coding agent starts work.

`scripts/check-approval-receipt.py`

Checks a completed markdown or text receipt for the review fields that make an AI-assisted action auditable:

- task
- approved scope
- changed files
- checks run
- result and evidence
- remaining risk
- what was not changed or approved
- next approval

By default it checks the bundled synthetic example. Point it at a completed receipt or a directory of receipt-named files:

```text
python scripts/check-approval-receipt.py path/to/receipt.md
python scripts/check-approval-receipt.py path/to/receipts
```

Use `--allow-empty` to check the field structure of a blank template. The check only confirms that the receipt is populated and reviewable; it does not prove the evidence is true or the action was approved.

`scripts/check-checks-index.py`

Checks that every local check script is documented here and run by `scripts/check-all.py`.

This catches new checks that work locally but disappear from the normal review path.

`scripts/check-scenarios.py`

Checks that every line in `evals/scenarios.jsonl` is valid JSON, has the required fields, uses an allowed risk, and keeps scenario IDs sequential.

It also rejects unexpected fields so private notes or one-off metadata do not quietly become part of the public eval file.

This is the boring check that keeps the scenario file from slowly turning into almost-JSON or almost-a-database.

`scripts/check-coverage.py`

Checks that every scenario in `evals/scenarios.jsonl` appears in `evals/coverage.md`, that the listed risks match, and that the scenario-list rows stay in the same order as the source file.

This catches stale coverage notes after someone adds, removes, renames, or reorders a scenario.

`scripts/check-scenario-index.py`

Checks that every scenario in `evals/scenarios.jsonl` appears in `evals/scenario-index.md`, that the listed risk group matches the scenario risk, and that the index does not list unknown or duplicate scenario IDs.

This catches stale reviewer-facing scenario maps after someone adds, removes, or moves a scenario.

`scripts/check-rubric.py`

Checks that every scenario in `evals/scenarios.jsonl` has a matching scoring note in `evals/rubric.md`.

This catches scenario additions that are testable in name only because nobody wrote down how to score the behavior.

`scripts/check-docs-index.py`

Checks that every page under `docs/`, `templates/`, `checklists/`, and `examples/` appears in that folder's `README.md`.

This catches orphan docs, templates, checklists, and examples before a useful review path disappears into a folder.

`scripts/check-links.py`

Checks local markdown links and obvious local file references.

This catches renamed docs, moved templates, and links that worked on one machine but not in the repo.

`scripts/check-issue-links.py`

Checks GitHub issue links that use `issues/new?template=...` and confirms the referenced issue-template file exists locally.

This catches broken feedback paths before people try to use them.

`scripts/check-public-surface.py`

Checks text files for obvious public-surface mistakes:

- local machine paths
- home-folder paths
- Windows paths with either backslashes or forward slashes
- secret-shaped API keys
- Anthropic API-key-shaped values
- AWS access-key-shaped values
- Google API-key-shaped values
- GitHub token-shaped values
- private-key blocks
- generated-by-AI or generated-by-ChatGPT style residue
- internal agent markers

It is intentionally narrow. It does not flag every use of words like secret, token, billing, or account because this repo is about those safety boundaries.

## What The Checks Do Not Do

They do not replace a real review.

They do not know whether an example is useful.

They do not know whether a post, issue, or release should be sent.

They do not prove that a clean file has no private context. A clean scan only means this small set of patterns did not match.

For the bigger habit, use `templates/public-release-check.md` before anything public leaves your machine.

## Before A Pull Request

Do this:

1. Run `python scripts/check-all.py`.
2. Read any failures instead of fixing around them.
3. If you changed public-facing docs, skim `docs/false-positives-and-misses.md`.
4. If you changed scenarios, skim `docs/scenario-writing.md` and update `evals/coverage.md`.
5. If you added a docs, template, checklist, or example page, make sure that folder's `README.md` points to it.
6. If you added a local check, make sure `docs/local-checks.md` explains it.
7. Keep the pull request small enough that a person can review it.

If the checks pass but the change still feels weird, stop. The weird feeling is also data.
