# AI Workflow Safety Kit

[![Local checks](https://github.com/BobsCrispyDuck/ai-workflow-safety-kit/actions/workflows/checks.yml/badge.svg)](https://github.com/BobsCrispyDuck/ai-workflow-safety-kit/actions/workflows/checks.yml)

Version: v0.1

This kit is for solo builders and small teams using AI coding agents without a whole ops department watching the exits.

It is not fancy. It is a set of simple checks for the moments where things usually go sideways.

The core idea:

Before an assistant edits, submits, publishes, or changes settings, it should know where it is, what data it is touching, whether it has approval, and how it will prove the work is actually done.

## Pick A Path

| If you are here to... | Start with |
|---|---|
| copy the guardrails into your own workflow | `docs/one-page-kit.md` |
| understand the repo fast | `docs/repo-tour.md` |
| test the kit with an assistant | `docs/try-it-now.md` |
| leave one useful review note | `docs/reviewer-brief.md` |
| suggest a small public-safe change | `docs/first-good-issues.md` |
| handle feedback as maintainer | `docs/maintainer-checklist.md` |

## Who This Helps

Good fit:

- solo builders using AI coding agents
- small teams adding AI assistants to normal repo work
- open-source maintainers accepting AI-assisted contributions
- people publishing docs, examples, demos, issues, or release notes
- anyone who needs a plain stop-before-you-send checklist

Bad fit:

- replacing security, legal, compliance, or production review
- handling real secrets, logs, customer data, account data, or private repos in public
- proving a system is safe just because a scan passed
- moving fast through account, billing, API-key, or deployment changes

## Failure Modes Covered

| Failure mode | Start with |
|---|---|
| wrong folder, stale branch, or unclear workspace | `templates/project-root-check.md` |
| private context drifting into public work | `templates/private-public-data-split.md` |
| publishing, posting, or submitting without approval | `templates/approval-gate.md` |
| "done" without proof | `templates/verification-receipt.md` |
| clean scan treated as full review | `docs/false-positives-and-misses.md` |
| reposting or second-channel posting after unclear moderation state | `docs/sharing-guide.md` |

For the current synthetic scenario map, see `evals/coverage.md`.

## Start Here

If you only copy three things, copy these:

1. `templates/work-session-check.md`
2. `templates/project-root-check.md`
3. `templates/private-public-data-split.md`

Need a bigger copy set?

`docs/starter-pack.md`

Want one copyable page?

`docs/one-page-kit.md`

Template guide:

`templates/README.md`

Checklist guide:

`checklists/README.md`

Then try the two-minute walkthrough:

`docs/demo-walkthrough.md`

Browse the docs:

`docs/README.md`

Take a quick repo tour:

`docs/repo-tour.md`

Read the FAQ:

`docs/faq.md`

See common use cases:

`docs/use-cases.md`

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

Example tasks:

`examples/README.md`

Review the kit quickly:

`docs/quick-review.md`

Send a reviewer brief:

`docs/reviewer-brief.md`

Pick a review path:

`docs/review-paths.md`

Use reviewer prompts:

`docs/reviewer-prompts.md`

Use the reviewer scorecard:

`docs/reviewer-scorecard.md`

Pick an issue template:

`docs/issue-guide.md`

Read feedback examples:

`docs/review-feedback-examples.md`

Use response snippets:

`docs/response-snippets.md`

Share it safely:

`docs/sharing-guide.md`

Ask for one review:

`docs/review-request.md`

Find a small contribution:

`docs/first-good-issues.md`

Review scanner hits and misses:

`docs/false-positives-and-misses.md`

Read the limits:

`docs/known-limits.md`

Turn feedback into safer scenarios:

`docs/feedback-loop.md`

Triage public feedback:

`docs/triage-guide.md`

Maintain feedback safely:

`docs/maintainer-checklist.md`

Write cleaner scenarios:

`docs/scenario-writing.md`

If you are about to publish something, use:

`templates/public-release-check.md`

## What This Kit Includes

- reusable templates for session setup, root checks, data boundaries, approval gates, receipts, and final audits
- a template index for choosing the right pause point
- a public-release check for the last pause before something leaves your machine
- checklists for editing, submitting, publishing, and using shared-token projects
- a checklist index for choosing the right pre-action pause
- synthetic examples that show safe, blocked, and approval-needed tasks
- evaluation scenarios and a rubric for testing assistant behavior
- an eval coverage map for spotting thin areas
- a small local check for the synthetic scenario file
- a small local check for internal doc links
- a one-command local check runner
- a no-install try-it-now test for comparing guarded and unguarded assistant behavior
- a repo tour for time-boxed review paths
- a docs index for finding the right review or feedback path
- a FAQ for quick orientation
- a starter pack for choosing what to copy
- a one-page kit for copying the core rails quickly
- a use-case guide for matching the kit to a real workflow moment
- an examples index for fake tasks
- example result receipts for judging assistant answers
- a quick-review path for lightweight public feedback
- a reviewer brief for one small useful note
- three short review paths for visitors who do not want to read the whole repo
- reviewer prompts for testing the kit with any coding assistant
- a reviewer scorecard for reporting one small test
- an issue guide for choosing the right public-safe template
- public-safe examples of useful review feedback
- short public-safe response snippets
- a sharing guide for low-noise public posts
- a review request for asking one relevant person without spam
- first-good-issue notes for small public-safe contributions
- false-positive and false-negative guidance for reviewing scanner results
- known limits so the project does not overclaim
- a feedback loop for turning public comments into synthetic scenarios
- a triage guide for handling public feedback safely
- a maintainer checklist for turning one review note into one small safe change
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
4. Read `templates/README.md`.
5. Read `checklists/README.md`.
6. Browse `docs/README.md`.
7. Read `docs/repo-tour.md`.
8. Read `docs/faq.md`.
9. Read `docs/starter-pack.md`.
10. Read `docs/one-page-kit.md`.
11. Read `docs/use-cases.md`.
12. Try `docs/try-it-now.md`.
13. Compare against `docs/example-result-receipts.md`.
14. Read `examples/README.md`.
15. Read `docs/quick-review.md`.
16. Read `docs/reviewer-brief.md`.
17. Read `docs/review-paths.md`.
18. Try `docs/reviewer-prompts.md`.
19. Use `docs/reviewer-scorecard.md`.
20. Read `docs/issue-guide.md`.
21. Read `docs/review-feedback-examples.md`.
22. Read `docs/response-snippets.md`.
23. Read `docs/sharing-guide.md`.
24. Read `docs/review-request.md`.
25. Read `docs/first-good-issues.md`.
26. Read `docs/false-positives-and-misses.md`.
27. Read `docs/known-limits.md`.
28. Read `docs/triage-guide.md`.
29. Read `docs/maintainer-checklist.md`.
30. Read `docs/demo-walkthrough.md`.
31. Read `docs/scenario-writing.md`.
32. Read `evals/coverage.md`.
33. Run `python scripts/check-scenarios.py`.
34. Run `python scripts/check-links.py`.
35. Run `python scripts/check-all.py`.
36. Read `docs/model-use-plan.md` before routing sensitive or higher-risk work.
37. Use `templates/approval-gate.md` before external or irreversible action.
38. Use `templates/verification-receipt.md` after a task.
39. Use `templates/final-audit.md` before calling a larger goal complete.

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
