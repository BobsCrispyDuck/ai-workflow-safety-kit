# Eval Coverage

This is a map of what the current synthetic scenarios cover.

It is not a benchmark. It is a way to see whether the boring failure modes are represented.

## Current Coverage

| Area | Scenarios |
|---|---|
| Safe local public work | S001, S007 |
| Project/root mismatch | S002 |
| Secret-like or private data exposure | S003, S006, S012, S013 |
| Production, account, or external action gates | S004, S005, S010, S011 |
| Broad or stale approval problems | S017, S019 |
| Shared-token misuse | S008 |
| Screenshot or visual private-context exposure | S018 |
| Missing proof or clean-scan shortcut | S009, S015 |
| Unsupported public claims | S020 |
| CI, dependency, or check failures | S021 |
| Cleanup or deletion risk | S022 |
| Moderation, repost, or account-state ambiguity | S023, S024 |
| Visibility or review-seeking without spam | S025, S026 |
| Public feedback handling | S014, S016 |

## Scenario List

| ID | Risk | What It Tests |
|---|---|---|
| S001 | low | Safe public README rewrite without invented claims |
| S002 | high | Stop before editing in the wrong project root |
| S003 | medium | Manual review for secret-like public placeholders |
| S004 | high | Approval gate before production account setting changes |
| S005 | high | Stop before external publication without approval |
| S006 | high | Refuse private production logs in public docs |
| S007 | low | Add synthetic examples without real project details |
| S008 | high | Reject shared-token use for private debugging context |
| S009 | medium | Avoid saying done without checks |
| S010 | high | Do not treat urgency as approval |
| S011 | medium | Keep public repo metadata updates neutral and approved |
| S012 | high | Keep private strategy notes out of public examples |
| S013 | high | Stop before posting a public issue with private-looking logs |
| S014 | medium | Turn sanitized safety feedback into a public-safe issue |
| S015 | high | Do not treat a clean scan as full proof |
| S016 | medium | Turn messy feedback into a reusable synthetic scenario |
| S017 | high | Do not treat a stale branch or unverified remote state as publish-ready |
| S018 | high | Stop before publishing screenshots with private context |
| S019 | high | Do not treat broad project approval as approval for a new external post |
| S020 | medium | Avoid unsupported adoption or outside-backing claims |
| S021 | high | Do not dismiss failed CI or dependency checks as unrelated noise |
| S022 | high | Stop before deleting user-created or untracked workspace files |
| S023 | high | Keep community moderation/status checks read-only and avoid reposting without fresh approval |
| S024 | high | Do not treat a missing or pending post as permission to repost or use a second channel |
| S025 | high | Do not turn a broad visibility goal into cold DMs without target and channel approval |
| S026 | medium | Do not open staged maintainer issues just to make the repo look active |

## Thin Spots

Useful next scenarios:

- generated output that looks stale but still needs human review
- dependency update that changes behavior outside the touched docs
- public feedback that arrives in a private channel and needs synthetic rewriting
- reviewer feedback that is useful but too vague to turn into a scenario yet

## Before Adding More

Use `docs/scenario-writing.md`.

Run:

```text
python scripts/check-all.py
```
