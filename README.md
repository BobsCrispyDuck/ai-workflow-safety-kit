# AI Workflow Safety Kit

Version: v0.1

This kit helps solo builders and small teams use AI coding agents more safely. It focuses on simple workflow guardrails, not heavyweight compliance.

The core idea:

Before an AI assistant edits, submits, publishes, or changes settings, it should check the project, data sensitivity, approval state, and evidence required to prove the work is actually done.

## What This Kit Includes

- reusable templates for project-root checks, data-safety boundaries, approval gates, verification receipts, and final audits
- checklists for editing, submitting, publishing, and using shared-token projects
- synthetic examples that show safe, blocked, and approval-needed tasks
- evaluation scenarios and a rubric for testing assistant behavior
- short adaptation notes for Codex and other AI coding agents

## What This Kit Is Not

This is not a replacement for security review, legal advice, compliance review, production approval, or good engineering judgment.

It does not guarantee safety. It gives teams a practical way to slow down at the moments where AI-assisted work usually goes sideways.

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

1. Read `templates/project-root-check.md`.
2. Read `templates/private-public-data-split.md`.
3. Use `templates/approval-gate.md` before external or irreversible action.
4. Use `templates/verification-receipt.md` after a task.
5. Use `templates/final-audit.md` before calling a larger goal complete.

## Suggested Workflow

```text
request -> root check -> data-safety check -> approval gate -> local work -> verification receipt -> final audit
```

If a task involves production, account settings, API keys, user data, billing, private logs, or publication, stop and require explicit approval.

## Repository Status

This is an early public version. It is not a security product, compliance framework, or guarantee. Treat it as a practical starting point for safer AI-assisted workflow habits.

## Contributing

Contributions should use synthetic or public examples only. See `CONTRIBUTING.md`.

## Security

Do not open public issues containing secrets, credentials, logs, account identifiers, wallet/session/auth/billing data, user data, or private repository content. See `SECURITY.md`.

## License

This project uses the MIT License.
