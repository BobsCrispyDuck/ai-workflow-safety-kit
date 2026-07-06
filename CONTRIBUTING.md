# Contributing

Thanks for helping improve the AI Workflow Safety Kit.

## Contribution Rules

- Use public or synthetic examples only.
- Do not include secrets, API keys, production logs, user data, account identifiers, wallet/session/auth/billing data, or private repository content.
- Do not paste raw assistant transcripts unless every line has been reviewed and sanitized.
- Keep claims narrow. This kit is workflow guidance, not a guarantee or replacement for security, legal, compliance, or production review.
- Prefer small examples that a solo builder or small team can copy quickly.

## Good Contributions

- clearer templates
- safer checklists
- new synthetic workflow-risk scenarios
- rubric improvements
- examples of approval gates and verification receipts
- docs that help non-expert users understand what to do next

## Issues

Use the issue templates when possible.

- Scenario ideas should be fake and reusable.
- Safety misses should be sanitized before posting.
- Docs feedback should stay small and specific.
- Reviewer scorecards should report one small test, not a full private transcript.

See `docs/quick-review.md` for the fastest way to review the kit without reading every file.

See `docs/issue-guide.md` for choosing the right public-safe issue template.

See `docs/feedback-loop.md` for turning outside feedback into public-safe scenarios or docs changes.

See `docs/triage-guide.md` for handling public feedback without carrying private details into the repo.

See `docs/maintainer-checklist.md` for turning one review note into one small safe change.

See `docs/scenario-writing.md` for writing fake-but-useful eval scenarios.

See `docs/first-good-issues.md` if you want one small place to start.

See `docs/local-checks.md` for what the local checks catch and what they do not prove.

## Review Checklist

Before proposing a change:

- run a private-data scan if available
- review every secret-like or sensitive-data hit
- run `python scripts/check-all.py` before opening a pull request if possible
- read `docs/local-checks.md` if a check fails or if you changed public-facing docs
- confirm all examples are synthetic or public
- confirm no external action is implied without approval

Pull requests should use `.github/PULL_REQUEST_TEMPLATE.md`.
