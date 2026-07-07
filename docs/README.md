# Docs Index

Start with the shortest path that matches what you need.

## New Here

- `docs/demo-walkthrough.md` - two-minute walkthrough
- `docs/repo-tour.md` - time-boxed paths through the repo
- `docs/repo-health.md` - what the public branch checks before pushing
- `docs/faq.md` - quick answers for new visitors
- `docs/starter-pack.md` - choose the smallest set of files to copy
- `docs/copy-into-your-repo.md` - adopt the smallest useful rules in another repo
- `docs/one-page-kit.md` - copy the core rails on one page
- `docs/use-cases.md` - where the kit fits in real workflow moments
- `docs/maintainer-flow.md` - review AI-assisted PRs without private context
- `docs/try-it-now.md` - no-install test prompt
- `docs/quick-review.md` - five-minute review path
- `docs/review-packet.md` - one clean handoff to send a reviewer
- `docs/reviewer-brief.md` - one small ask for reviewers
- `docs/review-paths.md` - three focused ways to review the repo
- `docs/known-limits.md` - what this kit does not claim to solve
- `docs/why-this-exists.md` - the basic reason for the project

## Testing The Kit

- `docs/reviewer-prompts.md` - prompts for testing with a coding assistant
- `docs/reviewer-scorecard.md` - copy/paste scorecard for one small test
- `docs/eval-scorecard.md` - copy/paste scorecard for one eval scenario
- `docs/example-result-receipts.md` - examples of good and weak receipts
- `examples/README.md` - fake task examples
- `evals/coverage.md` - what the current synthetic scenarios cover
- `evals/README.md` - how to use the eval folder
- `evals/rubric.md` - scoring guide

## Giving Feedback

- `docs/reviewer-scorecard.md` - short report format after trying a prompt
- `docs/review-packet.md` - send one useful review ask without making it a launch
- `docs/reviewer-brief.md` - quick note to send with the repo
- `docs/issue-guide.md` - choose the right public-safe issue template
- `docs/review-feedback-examples.md` - useful public-safe feedback examples
- `docs/response-snippets.md` - short maintainer replies
- `docs/feedback-loop.md` - turn feedback into a scenario, checklist, or rubric note
- `docs/triage-guide.md` - handle public feedback safely
- `docs/maintainer-flow.md` - small flow for maintainers reviewing AI-assisted work
- `docs/maintainer-checklist.md` - turn one review note into one small safe change
- `docs/first-good-issues.md` - small places to contribute
- `docs/sharing-guide.md` - share the repo without spammy link drops
- `docs/review-request.md` - ask one relevant person for a focused review

## Writing Or Changing Scenarios

- `docs/scenario-writing.md` - write fake-but-useful scenarios
- `evals/scenarios.jsonl` - current synthetic scenarios
- `evals/coverage.md` - thin spots worth filling
- `docs/eval-scorecard.md` - score one scenario without overthinking it

## Safety And Scope

- `docs/false-positives-and-misses.md` - review scanner hits and clean-scan misses
- `docs/repo-health.md` - what the public branch checks and what those checks do not prove
- `docs/model-use-plan.md` - match model strength to task risk
- `docs/adapting-to-codex.md` - use the kit with Codex
- `docs/adapting-to-other-agents.md` - use the kit with other assistants
- `docs/copy-into-your-repo.md` - copy the smallest useful project rule
- `checklists/before-asking-for-review.md` - ask for review without spam or private context
- `docs/roadmap.md` - current direction

## Templates And Checks

- `templates/README.md` - choose the right template
- `templates/project-instructions.md` - small repo-level rule for AI-assisted work
- `checklists/README.md` - choose the right checklist
- `docs/local-checks.md` - what the local checks catch and what they do not prove

Core templates live in `templates/`.

Quick checklists live in `checklists/`.

Local checks:

```text
python scripts/check-all.py
```

The local checks also make sure each public folder index lists its pages.
