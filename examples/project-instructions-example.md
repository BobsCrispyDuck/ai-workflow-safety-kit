# Example: Project Instructions

This is a fake filled-in version of `templates/project-instructions.md`.

Use it as a shape, not as a real project policy.

## Project Boundary

```text
Expected project root:
- /workspace/example-public-docs

Allowed areas:
- README.md
- docs/
- examples/
- templates/

Off-limits areas:
- private-notes/
- client-drafts/
- production-config/
- .env files

Protected production paths:
- /srv/example-live-site
- /deployments/example-production
```

Before editing, the assistant should confirm the current root and stop if it is not `/workspace/example-public-docs`.

## Data Boundary

Do not use these in public docs, examples, issues, release notes, demos, or screenshots:

- private logs
- secrets or keys
- customer or user details
- account, billing, wallet, session, or auth details
- private repo names
- raw assistant transcripts
- screenshots with private context

Use fake examples like:

```text
example-project
fake-customer
synthetic release note
```

## Stop Before

Stop and ask for explicit approval before:

- publishing the repo
- opening or replying to a public issue
- submitting a form
- changing account or project settings
- moving or creating keys
- touching production deployments
- deleting user-created, untracked, or unclear files

## Done Means

```text
Files changed:
Checks run:
Checks not run:
Evidence:
Remaining risk:
Approval still needed:
```

Good answer:

```text
Files changed:
- docs/example.md

Checks run:
- reviewed for private-looking details
- checked local links

Checks not run:
- no deploy check; this was docs-only

Evidence:
- docs/example.md uses synthetic names only

Remaining risk:
- human should review wording before public release

Approval still needed:
- publish approval
```

Weak answer:

```text
Done.
```

Why weak:

- no files named
- no checks named
- no current-state proof
- no approval boundary
