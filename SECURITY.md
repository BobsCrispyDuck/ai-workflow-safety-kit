# Security

This project is a workflow-safety kit. It is not a vulnerability scanner, security product, compliance framework, or guarantee.

## Reporting Sensitive Issues

Do not open a public issue or pull request containing:

- secrets, API keys, access tokens, or private keys
- production logs or configs
- account identifiers
- wallet, session, auth, or billing data
- private repository content
- user, customer, or personal data
- raw assistant transcripts with private context

If a security concern requires sensitive details, share only a minimal sanitized description in public and keep private material out of the repository.

## Supported Scope

Supported:

- templates that reduce accidental data exposure
- approval gates for external or irreversible actions
- synthetic scenarios for testing assistant behavior
- verification receipts and final audits

Not supported:

- exploit development
- offensive testing against live targets
- handling real secrets or private logs
- emergency incident response

