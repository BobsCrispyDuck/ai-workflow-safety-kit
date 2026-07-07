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
| add the kit to an existing repo | `docs/copy-into-your-repo.md` |
| understand the repo fast | `docs/repo-tour.md` |
| check current repo health | `docs/repo-health.md` |
| test the kit with an assistant | `docs/try-it-now.md` |
| send one clean review handoff | `docs/review-packet.md` |
| leave one useful review note | `docs/reviewer-brief.md` |
| maintain a repo with AI-assisted PRs | `docs/maintainer-flow.md` |
| suggest a small public-safe change | `docs/first-good-issues.md` |
| handle feedback as maintainer | `docs/maintainer-checklist.md` |

## What Would Help Most

If you are looking at this repo cold, the best feedback is one small miss.

Useful notes:

- a failure mode the scenarios do not cover
- a checklist line that feels vague
- a place where the repo sounds too confident
- a path that took too long to find

No private logs or transcripts needed. A fake version is better.

Start with `docs/reviewer-brief.md` or open the [reviewer scorecard issue template](https://github.com/BobsCrispyDuck/ai-workflow-safety-kit/issues/new?template=reviewer-scorecard.yml).

Other useful issue paths:

- [scenario idea](https://github.com/BobsCrispyDuck/ai-workflow-safety-kit/issues/new?template=scenario-idea.yml)
- [safety miss](https://github.com/BobsCrispyDuck/ai-workflow-safety-kit/issues/new?template=safety-miss.yml)
- [docs or template feedback](https://github.com/BobsCrispyDuck/ai-workflow-safety-kit/issues/new?template=docs-template-feedback.yml)

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

Adding it to an existing repo?

`docs/copy-into-your-repo.md`

Want one copyable page?

`docs/one-page-kit.md`

Template guide:

`templates/README.md`

Project instruction template:

`templates/project-instructions.md`

Checklist guide:

`checklists/README.md`

Before asking for review:

`checklists/before-asking-for-review.md`

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

Check feedback issue links:

`python scripts/check-issue-links.py`

Understand local checks:

`docs/local-checks.md`

Run all local checks:

`python scripts/check-all.py`

GitHub runs the same check on pushes and pull requests:

`.github/workflows/checks.yml`

Example receipts:

`docs/example-result-receipts.md`

Example tasks:

`examples/README.md`

Example project instructions:

`examples/project-instructions-example.md`

Review the kit quickly:

`docs/quick-review.md`

Check repo health:

`docs/repo-health.md`

Send a review packet:

`docs/review-packet.md`

Send a reviewer brief:

`docs/reviewer-brief.md`

Pick a review path:

`docs/review-paths.md`

Use reviewer prompts:

`docs/reviewer-prompts.md`

Use the reviewer scorecard:

`docs/reviewer-scorecard.md`

Score one eval scenario:

`docs/eval-scorecard.md`

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

Use it as a maintainer:

`docs/maintainer-flow.md`

Maintain feedback safely:

`docs/maintainer-checklist.md`

Write cleaner scenarios:

`docs/scenario-writing.md`

If you are about to publish something, use:

`templates/public-release-check.md`

## What This Kit Includes

- reusable templates for session setup, root checks, data boundaries, approval gates, receipts, and final audits
- a project-instructions template for adding the guardrails to another repo
- a template index for choosing the right pause point
- a public-release check for the last pause before something leaves your machine
- checklists for editing, submitting, publishing, and using shared-token projects
- a checklist for asking one relevant person for review without spam or private context
- a checklist index for choosing the right pre-action pause
- synthetic examples that show safe, blocked, and approval-needed tasks
- evaluation scenarios and a rubric for testing assistant behavior
- an eval coverage map for spotting thin areas
- a small local check for the synthetic scenario file
- a small local check for internal doc links
- a small local check for public feedback issue-template links
- a small public-surface check for obvious private paths and generated-by-AI residue
- local-check notes explaining what the checks do and do not prove
- a one-command local check runner
- a no-install try-it-now test for comparing guarded and unguarded assistant behavior
- a repo tour for time-boxed review paths
- a repo-health note for checking what the public branch verifies
- a docs index for finding the right review or feedback path
- a FAQ for quick orientation
- a starter pack for choosing what to copy
- a copy-into-your-repo guide for adopting the smallest useful rules
- a one-page kit for copying the core rails quickly
- a use-case guide for matching the kit to a real workflow moment
- an examples index for fake tasks
- a fake filled-in project-instructions example
- example result receipts for judging assistant answers
- a quick-review path for lightweight public feedback
- a review packet for sending one clean handoff to a reviewer
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
- a maintainer flow for reviewing AI-assisted PRs without private context
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

If you want to try the kit instead of reading the whole repo:

1. Copy `docs/one-page-kit.md` into a scratch note or test repo.
2. Use `templates/project-root-check.md` before the assistant edits anything.
3. Use `templates/private-public-data-split.md` before public docs, issues, examples, or posts.
4. Run one fake task from `docs/try-it-now.md`.
5. Compare the answer against `docs/example-result-receipts.md`.

If you are adding this to a real repo, use `docs/copy-into-your-repo.md`.

If you are reviewing this project, use `docs/reviewer-brief.md`.

If you want the full map, use `docs/README.md`.

## Suggested Workflow

```text
request -> work-session check -> root check -> data-safety check -> approval gate -> local work -> verification receipt -> final audit
```

If a task involves production, account settings, API keys, user data, billing, private logs, or publication, stop and require explicit approval.

## Repository Status

This is an early public version. Treat it as a practical starting point, not a badge, framework, or magic shield.

## Contributing

Contributions should use synthetic or public examples only. See `CONTRIBUTING.md`.

For public-safe support and feedback paths, see `SUPPORT.md`.

## Security

Do not open public issues containing secrets, credentials, logs, account identifiers, wallet/session/auth/billing data, user data, or private repository content. See `SECURITY.md`.

## License

This project uses the MIT License.
