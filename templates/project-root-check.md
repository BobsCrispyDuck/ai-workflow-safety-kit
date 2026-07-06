# Template: Project Root Check

Use before editing files.

## Required Check

Confirm the active project root before making changes.

Example command:

```powershell
git rev-parse --show-toplevel
```

## Decision

Continue only if:

- the root is the expected project
- the path is not a protected production path
- the path is not a synced/private folder that should not be edited
- the task belongs in this project

## Stop Conditions

Stop and ask before editing if:

- the command fails and you expected a Git repo
- the root is not the expected folder
- the path is a production deployment location
- the path is a synced or archived project copy
- the work would affect account settings, billing, keys, user data, or external systems

## Receipt Snippet

```text
Project root checked:
- expected:
- actual:
- safe to edit: yes/no
- notes:
```

