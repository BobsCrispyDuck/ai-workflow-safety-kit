# PR Receipt Examples

These are fake examples for AI-assisted pull requests.

Use them when a contributor says an assistant helped and you need enough proof to review the change without asking for private context.

## Good Enough

```text
Changed:
- docs/install.md
- docs/troubleshooting.md

Checked:
- ran npm test
- ran markdown link check
- skimmed public examples for private context

Not checked:
- production deploy
- account settings
- private support logs

Data used:
- public docs
- synthetic error examples

Approval needed:
- maintainer review before merge
- separate approval before publishing release notes
```

Why this works:

- names the changed files
- names the checks
- says what was not checked
- keeps private material out of the public PR
- separates merge review from publishing

## Too Vague

```text
The assistant checked everything and the PR is ready.
```

Why this is not enough:

- no file list
- no checks named
- no data boundary
- no remaining risk
- no approval boundary

Better maintainer reply:

```text
Can you add a short receipt?

Need:
- files changed
- checks run
- data used
- what was not checked
- approval still needed
```

## Too Much Private Proof

```text
Here is the full assistant transcript and debug log so you can see what happened.
```

Why this is unsafe:

- transcripts can include private repo context
- logs can include user, account, or production details
- the useful behavior gets buried under cleanup risk

Better version:

```text
The assistant tried to use private debug material in a public doc.

Synthetic version:
Assistant used a fake support log in a public troubleshooting page even though the log was not marked synthetic.

Expected behavior:
Stop, ask for a synthetic example, and avoid quoting private debug material.
```

## Maintainer Shortcut

If the PR is small, ask for this:

```text
Files changed:
Checks run:
Synthetic/public data only: yes/no
Private details removed: yes/no
Remaining review needed:
```

That is enough for most docs and checklist changes.

If the work touches publishing, account settings, billing, permissions, production, auth, keys, or user data, use `templates/approval-gate.md` before review continues.

Useful next pages:

- `docs/maintainer-flow.md`
- `docs/review-feedback-examples.md`
- `docs/response-snippets.md`
- `.github/PULL_REQUEST_TEMPLATE.md`
