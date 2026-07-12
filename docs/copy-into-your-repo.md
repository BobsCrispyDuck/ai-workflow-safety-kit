# Copy Into Your Repo

Use this if you want the smallest useful version of the kit in another project.

Do not copy everything first. Start with one short project rule, then add checklists only when they solve a real problem.

## Smallest Useful Rule

If you want a file-shaped version, copy `templates/project-instructions.md`.

For a fake filled-in example, use `examples/project-instructions-example.md`.

Paste something like this into your project instructions:

```text
Before editing, confirm the project root and name any paths that are off limits.

Do not use private logs, secrets, customer data, account data, screenshots with private context, or raw assistant transcripts in public docs, examples, issues, or release notes.

Stop before publishing, submitting forms, changing account settings, moving keys, touching production, or changing billing.

When done, report what changed, what was checked, what was not checked, and what evidence proves the current state.
```

If you want a quick smoke check after writing the rule, run:

```text
python scripts/audit-workflow.py path/to/your/repo
```

Use `--json` before the repository path for deterministic machine-readable output. Exit code `0` means all four boundaries were detected, `1` means findings, `2` means invalid usage, and `3` means an internal or read error.

The audit reuses `scripts/check-agent-instructions.py`, so copy both scripts if you are adopting only the command instead of the whole kit. It does not know whether the instructions are good and a pass does not prove the repository is safe. It only catches the boring miss where the file never mentions root checks, private data, approval gates, or verification receipts at all.

## Copy The GitHub Actions Check

If you copy the kit's scripts and tests into the same paths, save this as `.github/workflows/checks.yml`:

```yaml
name: Local checks

on:
  pull_request:
  push:
    branches:
      - main

permissions:
  contents: read

jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - name: Check out repo
        uses: actions/checkout@v4
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.x"
      - name: Run local checks
        run: python scripts/check-all.py
```

This workflow needs no project credentials or third-party Python packages. It runs the same aggregate check used locally; review the included checks before copying them into a different repository.

Then point to the files that matter for the current work.

## For Normal Repo Work

Copy or reference:

- `templates/project-instructions.md`
- `templates/work-session-check.md`
- `templates/project-root-check.md`
- `templates/private-public-data-split.md`

Use when the main risk is wrong folder, unclear scope, or private material drifting into the work.

## For Public Work

Copy or reference:

- `checklists/before-publishing.md`
- `templates/public-release-check.md`
- `templates/verification-receipt.md`

Use before docs, examples, screenshots, issues, release notes, demos, or posts leave your machine.

## For Submissions

Copy or reference:

- `checklists/before-submitting.md`
- `templates/approval-gate.md`
- `templates/verification-receipt.md`

Use when the assistant can draft locally, but sending needs its own approval.

## For Coding Agents With Project Files

If your tool supports repo-level instruction files, keep the rule short.

Good repo-level rules:

- expected project root
- paths the assistant should not touch
- blocked data
- commands that prove the work
- actions that require explicit approval

Bad repo-level rules:

- vague reminders to "be careful"
- private logs or real customer examples
- broad approval that can be mistaken for permission to publish or submit
- stale commands nobody runs anymore

## Keep It Alive

After a few uses, remove anything that nobody follows.

Add one line only when a real miss points to it:

```text
The assistant said done after a clean scan, but never checked the root.
```

That should become a sharper rule, receipt line, or fake scenario.

Useful links:

- `docs/starter-pack.md`
- `docs/adapting-to-codex.md`
- `docs/adapting-to-other-agents.md`
- `docs/maintainer-checklist.md`
