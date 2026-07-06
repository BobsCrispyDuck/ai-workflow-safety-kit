# Adapting To Codex

Use these ideas with Codex by placing project-specific rules in the right scope.

## Good Fit For AGENTS.md

- project-root rules
- paths that must not be edited
- verification commands
- approval gates
- coding conventions

## Good Fit For A Thread Prompt

- one-off constraints
- temporary approval boundaries
- current objective

## Good Fit For A Checklist

- before editing
- before publishing
- before submitting
- before using shared-token or public/synthetic lanes

## Practical Pattern

1. Ask Codex to confirm the project root.
2. Ask Codex to identify whether private data is needed.
3. Ask Codex to stop before production or account changes.
4. Ask Codex to report evidence, not vibes.

For a copyable starter rule, use `docs/copy-into-your-repo.md`.
