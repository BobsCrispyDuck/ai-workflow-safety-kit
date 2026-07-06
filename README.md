# AI Workflow Safety Kit

[![Local checks](https://github.com/BobsCrispyDuck/ai-workflow-safety-kit/actions/workflows/checks.yml/badge.svg)](https://github.com/BobsCrispyDuck/ai-workflow-safety-kit/actions/workflows/checks.yml)

Version: v0.1

This kit is for solo builders and small teams using AI coding agents without a whole ops department watching the exits.

It is not fancy. It is a set of simple checks for the moments where things usually go sideways.

The core idea:

Before an assistant edits, submits, publishes, or changes settings, it should know where it is, what data it is touching, whether it has approval, and how it will prove the work is actually done.

## Start Here

If you only copy three things, copy these:

1. `templates/work-session-check.md`
2. `templates/project-root-check.md`
3. `templates/private-public-data-split.md`

Then try the two-minute walkthrough:

`docs/demo-walkthrough.md`

Browse the docs:

`docs/README.md`

Or run the no-install test:

`docs/try-it-now.md`

Check the scenario file:

`python scripts/check-scenarios.py`

See eval coverage:

`evals/coverage.md`

Check local doc links:

`python scripts/check-links.py`

Run all local checks:

`python scripts/check-all.py`

GitHub runs the same check on pushes and pull requests:

`.github/workflows/checks.yml`

Example receipts:

`docs/example-result-receipts.md`

Review the kit quickly:

`docs/quick-review.md`

Pick a review path:

`docs/review-paths.md`

Use reviewer prompts:

`docs/reviewer-prompts.md`

Read feedback examples:

`docs/review-feedback-examples.md`

Use response snippets:

`docs/response-snippets.md`

Find a small contribution:

`docs/first-good-issues.md`

Review scanner hits and misses:

`docs/false-positives-and-misses.md`

Read the limits:

`docs/known-limits.md`

Turn feedback into safer scenarios:

`docs/feedback-loop.md`

Write cleaner scenarios:

`docs/scenario-writing.md`

If you are about to publish something, use:

`templates/public-release-check.md`

## What This Kit Includes

- reusable templates for session setup, root checks, data boundaries, approval gates, receipts, and final audits
- a public-release check for the last pause before something leaves your machine
- checklists for editing, submitting, publishing, and using shared-token projects
- synthetic examples that show safe, blocked, and approval-needed tasks
- evaluation scenarios and a rubric for testing assistant behavior
- an eval coverage map for spotting thin areas
- a small local check for the synthetic scenario file
- a small local check for internal doc links
- a one-command local check runner
- a no-install try-it-now test for comparing guarded and unguarded assistant behavior
- a docs index for finding the right review or feedback path
- example result receipts for judging assistant answers
- a quick-review path for lightweight public feedback
- three short review paths for visitors who do not want to read the whole repo
- reviewer prompts for testing the kit with any coding assistant
- public-safe examples of useful review feedback
- short public-safe response snippets
- first-good-issue notes for small public-safe contributions
- false-positive and false-negative guidance for reviewing scanner results
- known limits so the project does not overclaim
- a feedback loop for turning public comments into synthetic scenarios
- scenario-writing notes for keeping evals useful and public-safe
- model-use notes for matching cheap drafts, stronger review, and approval gates
- short adaptation notes for Codex and other AI coding agents

## What This Kit Is Not

This is not a replacement for security review, legal advice, compliance review, production approval, or good judgment.

It does not guarantee safety. It just gives you a way to slow down before the expensive mistake.

## Safety Posture

This project uses only synthetic examples.

Do not add:

- secrets or API keys
- production logs
- private repo contents
- raw assistant transcripts
- user or customer data
- wallet, session, auth, or billing data
- private creative/IP material
- account identifiers unless explicitly approved

## Quick Start

1. Start with `templates/work-session-check.md`.
2. Read `templates/project-root-check.md`.
3. Read `templates/private-public-data-split.md`.
4. Browse `docs/README.md`.
5. Try `docs/try-it-now.md`.
6. Compare against `docs/example-result-receipts.md`.
7. Read `docs/quick-review.md`.
8. Read `docs/review-paths.md`.
9. Try `docs/reviewer-prompts.md`.
10. Read `docs/review-feedback-examples.md`.
11. Read `docs/response-snippets.md`.
12. Read `docs/first-good-issues.md`.
13. Read `docs/false-positives-and-misses.md`.
14. Read `docs/known-limits.md`.
15. Read `docs/demo-walkthrough.md`.
16. Read `docs/scenario-writing.md`.
17. Read `evals/coverage.md`.
18. Run `python scripts/check-scenarios.py`.
19. Run `python scripts/check-links.py`.
20. Run `python scripts/check-all.py`.
21. Read `docs/model-use-plan.md` before routing sensitive or higher-risk work.
22. Use `templates/approval-gate.md` before external or irreversible action.
23. Use `templates/verification-receipt.md` after a task.
24. Use `templates/final-audit.md` before calling a larger goal complete.

## Suggested Workflow

```text
request -> work-session check -> root check -> data-safety check -> approval gate -> local work -> verification receipt -> final audit
```

If a task involves production, account settings, API keys, user data, billing, private logs, or publication, stop and require explicit approval.

## Repository Status

This is an early public version. Treat it as a practical starting point, not a badge, framework, or magic shield.

## Contributing

Contributions should use synthetic or public examples only. See `CONTRIBUTING.md`.

## Security

Do not open public issues containing secrets, credentials, logs, account identifiers, wallet/session/auth/billing data, user data, or private repository content. See `SECURITY.md`.

## License

This project uses the MIT License.
