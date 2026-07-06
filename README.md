# AI Workflow Safety Kit

Version: v0.1

This kit is for solo builders and small teams using AI coding agents without a whole ops department watching the exits.

It is not fancy. It is a set of simple checks for the moments where things usually go sideways.

The core idea:

Before an assistant edits, submits, publishes, or changes settings, it should know where it is, what data it is touching, whether it has approval, and how it will prove the work is actually done.

## Start Here

If you only copy three things, copy these:

1. `templates/work-session-check.md`
2. `templates/project-root-check.md`
3. `templates/private-public-data-split.md`

Then try the two-minute walkthrough:

`docs/demo-walkthrough.md`

If you are about to publish something, use:

`templates/public-release-check.md`

## What This Kit Includes

- reusable templates for session setup, root checks, data boundaries, approval gates, receipts, and final audits
- a public-release check for the last pause before something leaves your machine
- checklists for editing, submitting, publishing, and using shared-token projects
- synthetic examples that show safe, blocked, and approval-needed tasks
- evaluation scenarios and a rubric for testing assistant behavior
- model-use notes for matching cheap drafts, stronger review, and approval gates
- short adaptation notes for Codex and other AI coding agents

## What This Kit Is Not

This is not a replacement for security review, legal advice, compliance review, production approval, or good judgment.

It does not guarantee safety. It just gives you a way to slow down before the expensive mistake.

## Safety Posture

This project uses only synthetic examples.

Do not add:

- secrets or API keys
- production logs
- private repo contents
- raw assistant transcripts
- user or customer data
- wallet, session, auth, or billing data
- private creative/IP material
- account identifiers unless explicitly approved

## Quick Start

1. Start with `templates/work-session-check.md`.
2. Read `templates/project-root-check.md`.
3. Read `templates/private-public-data-split.md`.
4. Try `docs/demo-walkthrough.md`.
5. Read `docs/model-use-plan.md` before routing sensitive or higher-risk work.
6. Use `templates/approval-gate.md` before external or irreversible action.
7. Use `templates/verification-receipt.md` after a task.
8. Use `templates/final-audit.md` before calling a larger goal complete.

## Suggested Workflow

```text
request -> work-session check -> root check -> data-safety check -> approval gate -> local work -> verification receipt -> final audit
```

If a task involves production, account settings, API keys, user data, billing, private logs, or publication, stop and require explicit approval.

## Repository Status

This is an early public version. Treat it as a practical starting point, not a badge, framework, or magic shield.

## Contributing

Contributions should use synthetic or public examples only. See `CONTRIBUTING.md`.

## Security

Do not open public issues containing secrets, credentials, logs, account identifiers, wallet/session/auth/billing data, user data, or private repository content. See `SECURITY.md`.

## License

This project uses the MIT License.
