# One-Page Kit

Copy this when you want the shape of the kit without pulling the whole repo.

It is meant for normal AI-assisted work where the assistant needs a few hard rails before it edits, publishes, submits, or calls something done.

## Work Shape

Fill this in before the assistant starts.

```text
Expected project/root:
Allowed data:
Blocked data:
External actions allowed:
External actions blocked:
Proof needed before done:
```

Use plain words. The goal is not fancy process. The goal is making the risky parts visible before the work gets moving.

## Stop Before

Stop and ask for exact approval before:

- editing in a wrong, unknown, synced, archived, or production folder
- using private logs, transcripts, screenshots, repo names, secrets, customer data, account data, wallet data, billing data, or API keys
- publishing, submitting, posting, uploading, changing settings, changing access, or changing billing
- using a shared-token, public, or training-visible lane for private work
- deleting, moving, or overwriting user-created files that were not part of the request
- calling a task done without naming what was checked

Approval should name the action and the destination.

Good:

```text
APPROVE PUBLISH docs/one-page-kit.md to GitHub main after local checks pass.
```

Weak:

```text
go ahead
```

## Before Editing

Before changing files, the assistant should confirm:

- it is in the expected project root
- the file belongs to the task
- the project is not a production, synced, or archive copy unless that was explicitly approved
- the edit is the smallest useful change
- the verification path is known before editing starts

If root, scope, or data safety is unclear, pause first.

## Before Publishing Or Submitting

Before anything leaves the local workspace, the assistant should list:

- the exact destination
- the exact files, fields, or message text involved
- the check used for private data
- whether every example is public or synthetic
- the approval still needed

Do not turn real stories into public examples by pasting the raw version. Rewrite the story as a fake scenario first.

## Done Means

A good final receipt names:

```text
Files changed:
Checks run:
Checks not run:
External actions taken:
Approvals still needed:
Current-state proof:
```

If a check was skipped, say that. If something still needs approval, say that too.

## Safe Feedback

Useful feedback can be small.

Good:

```text
The assistant caught the wrong folder, but it still claimed done without saying which checks ran.
```

Also good:

```text
Add a fake scenario where the assistant tries to submit a support form without listing the fields first.
```

Do not paste private logs, real transcripts, customer details, screenshots with private context, account identifiers, or secrets into public feedback.

For a slightly more structured review, use `docs/reviewer-scorecard.md`.
