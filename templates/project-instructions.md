# Template: Project Instructions

Use this as a small repo-level rule for AI-assisted work.

Fill in the project-specific parts before using it. Keep private details out of the public copy.

## Project Boundary

```text
Expected project root:
Allowed areas:
Off-limits areas:
Protected production paths:
```

Before editing, confirm the active project root and say whether it matches the expected project.

## Data Boundary

Do not use these in public docs, examples, issues, release notes, demos, or screenshots:

- private logs
- secrets or keys
- customer or user details
- account, billing, wallet, session, or auth details
- private repo names
- raw assistant transcripts
- screenshots with private context

Use public or synthetic examples instead.

## Stop Before

Stop and ask for explicit approval before:

- publishing or posting
- submitting forms or applications
- changing account, org, project, billing, auth, or permission settings
- creating, moving, or exposing keys
- touching production deployments
- deleting user-created, untracked, or unclear files
- claiming the larger task is complete without current proof

## Done Means

When reporting done, include:

```text
Files changed:
Checks run:
Checks not run:
Evidence:
Remaining risk:
Approval still needed:
```

Do not use a passing build, clean scan, or no-error result as the whole receipt.

## Useful Kit Files

- `templates/project-root-check.md`
- `templates/private-public-data-split.md`
- `templates/approval-gate.md`
- `templates/verification-receipt.md`
- `templates/final-audit.md`
