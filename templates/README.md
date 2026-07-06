# Templates

Use these when the work needs a clear pause point.

They are meant to be copied into a task, issue, or assistant instruction. Keep project-specific details out unless they are safe to share.

## Start A Work Session

- `templates/project-instructions.md` - small repo-level rule for AI-assisted work
- `templates/work-session-check.md` - define scope, blocked areas, and proof needed
- `templates/project-root-check.md` - confirm the assistant is in the right project before editing
- `templates/private-public-data-split.md` - separate public/synthetic material from private material

## Before Risky Action

- `templates/approval-gate.md` - stop before external, irreversible, account, billing, auth, production, or publishing action
- `templates/public-release-check.md` - last check before something leaves your machine

## After The Work

- `templates/verification-receipt.md` - record what changed and what proof exists
- `templates/final-audit.md` - check whether a larger task is really done

## Suggested Order

```text
work-session check -> project-root check -> data split -> approval gate -> verification receipt -> final audit
```

Not every task needs every template. The point is to use the smallest pause that catches the risky part.
