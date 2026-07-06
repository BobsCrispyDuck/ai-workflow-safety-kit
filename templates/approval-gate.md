# Template: Approval Gate

Use before any external, irreversible, account-level, or production-impacting action.

## Requires Explicit Approval

Ask before:

- publishing a repo or file
- submitting a form
- changing account/org/project settings
- enabling data sharing
- creating or exposing API keys
- touching production deployments
- using live user data
- changing billing, auth, wallet, session, or permissions

## Approval Packet

Before asking, present:

- destination
- exact content or action
- expected upside
- risks
- what is excluded
- rollback or stop plan
- exact approval phrase

## Approval Phrase

Use a short exact phrase.

Example:

```text
APPROVE LOCAL DRAFT
```

## Receipt Snippet

```text
Approval gate:
- action:
- approval required: yes/no
- approval received:
- scope:
- stop conditions:
```

