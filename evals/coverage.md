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
| Shared-token misuse | S008 |
| Missing proof or clean-scan shortcut | S009, S015 |
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

## Thin Spots

Useful next scenarios:

- stale branch or stale generated output
- screenshots with private context
- dependency or CI failure treated as unrelated noise
- user approval that is broad but not specific enough
- public changelog entry that accidentally implies adoption or outside backing
- deleted-file or cleanup task that could remove user work

## Before Adding More

Use `docs/scenario-writing.md`.

Run:

```text
python scripts/check-all.py
```
