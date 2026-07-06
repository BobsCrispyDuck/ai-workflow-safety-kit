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

See `docs/quick-review.md` for the fastest way to review the kit without reading every file.

See `docs/feedback-loop.md` for turning outside feedback into public-safe scenarios or docs changes.

See `docs/scenario-writing.md` for writing fake-but-useful eval scenarios.

## Review Checklist

Before proposing a change:

- run a private-data scan if available
- review every secret-like or sensitive-data hit
- run `python scripts/check-links.py` if docs links changed
- confirm all examples are synthetic or public
- confirm no external action is implied without approval

Pull requests should use `.github/PULL_REQUEST_TEMPLATE.md`.
