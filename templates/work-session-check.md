# Template: Work Session Check

Use this at the start of a coding-agent work session.

The point is not to make the session slower. The point is to make the risky parts obvious before the assistant starts editing.

## Session Shape

```text
Task:
Expected project:
Allowed files or folders:
Out of scope:
External actions allowed: yes/no
Approval needed before:
```

## Start Checks

Confirm:

- the active project root matches the task
- the work is not happening inside a protected, archived, or synced copy
- the task does not need private logs, private repo contents, user data, or account data
- the assistant knows what counts as done
- the assistant knows what must stop for approval

## Stop Before

Stop before:

- publishing
- submitting a form
- changing account, org, billing, auth, wallet, session, or project settings
- creating, moving, or exposing keys
- touching production deployments
- pulling private context into public work
- claiming completion without evidence

## Working Notes

```text
Root checked:
Data boundary:
Approval boundary:
Planned checks:
Known risks:
```

## End Receipt

```text
Files changed:
Checks run:
Result:
Evidence:
Remaining risk:
Next approval:
```
