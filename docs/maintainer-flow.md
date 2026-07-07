# Maintainer Flow

Use this when you maintain a repo and someone shows up with AI-assisted work.

The goal is not to police whether a person used an assistant.

The goal is to make the review boring:

- right repo
- right branch
- no private material
- no hidden external action
- proof that the change was checked

## Start With The PR

Ask for a small receipt instead of a long explanation.

Good receipt:

```text
Changed:
Checked:
Not checked:
Data used:
Approval needed:
```

If that feels too formal, use the repo's `.github/PULL_REQUEST_TEMPLATE.md`.

## What To Require

For a normal docs or code change, ask for:

- what files changed
- what local checks ran
- whether examples are synthetic
- whether public-facing text was checked for private context
- what still needs human review

For anything that touches publishing, account settings, billing, permissions, production, auth, keys, or user data, ask for a stop instead of a patch.

Use:

- `templates/approval-gate.md`
- `templates/public-release-check.md`
- `templates/verification-receipt.md`

## Fast Maintainer Check

Before merging AI-assisted work, skim for:

- private logs pasted into issues, PRs, docs, or examples
- screenshots with private context
- real-looking keys, tokens, account IDs, or customer details
- "done" claims with no checks listed
- generated docs that sound confident but do not say what was verified
- broad cleanup commits that are bigger than the issue

If something looks off, ask for a smaller patch.

## A Good Review Comment

```text
Can you split this down to the docs change only and add a short receipt?

Need:
- files changed
- checks run
- whether the example data is synthetic
- what still needs maintainer review
```

That is usually better than debating the whole AI-assisted workflow.

## If You Want To Adopt The Kit

Start small.

1. Copy `templates/project-instructions.md`.
2. Add the blocked data and stop points that matter for your repo.
3. Point contributors to `.github/PULL_REQUEST_TEMPLATE.md`.
4. Ask for one receipt on AI-assisted changes.
5. Add scenarios only when a real public-safe miss shows up.

For the smaller copy path, use `docs/copy-into-your-repo.md`.

## What Not To Ask For

Do not ask contributors to prove a private story by pasting:

- raw assistant transcripts
- private logs
- customer or user data
- private repo names
- account, billing, wallet, session, or auth details
- screenshots with private context

Ask them to rewrite the story as a fake scenario instead.

Useful next pages:

- `docs/first-good-issues.md`
- `docs/maintainer-checklist.md`
- `docs/review-feedback-examples.md`
- `docs/response-snippets.md`
