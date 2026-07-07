# Use Cases

This kit is for the boring moments where a coding agent can be right about the code and still wrong about the work.

Use it when the risk is not "can the model write this?" but "should it keep going without another check?"

## Starting A Coding-Agent Session

Use when you are about to hand an assistant a repo and a task.

Start with:

- `templates/work-session-check.md`
- `templates/project-root-check.md`
- `templates/private-public-data-split.md`

Good fit:

```text
Work on this public docs repo, but do not touch the production checkout or private notes folder.
```

The point is to make the root, scope, blocked areas, and proof of done clear before edits start.

## Publishing Public Work

Use when a doc, repo, issue, release note, example, screenshot, or demo is about to leave your machine.

Start with:

- `checklists/before-publishing.md`
- `templates/public-release-check.md`
- `docs/false-positives-and-misses.md`

Good fit:

```text
Prepare this fake example for a public README and prove it does not include private context.
```

The assistant should scan, review hits, narrow claims, and avoid acting like a clean scan is the whole review.

## Submitting Forms Or Applications

Use when anything gets sent to a third party: forms, program applications, support notes, community posts, or public issue comments.

Start with:

- `checklists/before-submitting.md`
- `templates/approval-gate.md`
- `templates/verification-receipt.md`

Good fit:

```text
Draft the fields locally, list exactly what will be submitted, and stop before sending.
```

The assistant should separate drafting from submitting. Sending is its own approval step.

## Using Shared-Token Or Public/Synthetic Lanes

Use when a project setting, training/eval opt-in, or shared-credit path means prompts and outputs may be visible outside your private workspace.

Start with:

- `checklists/before-using-shared-tokens.md`
- `templates/private-public-data-split.md`
- `docs/model-use-plan.md`

Good fit:

```text
Use only fake examples and public docs in this low-cost test lane.
```

Bad fit:

```text
Route this private debugging prompt through the shared-token project because credits are low.
```

If the prompt would be uncomfortable to paste into a public issue, it does not belong there.

## Checking A "Done" Claim

Use when an assistant says the work is finished.

Start with:

- `templates/verification-receipt.md`
- `templates/final-audit.md`
- `docs/example-result-receipts.md`

Good fit:

```text
Show what changed, what was checked, what still needs review, and what evidence proves it.
```

The assistant should not use vibes, intent, or "no errors found" as proof.

## Giving Feedback On The Kit

Use when you are reviewing this repo and want to leave one useful note without reading every file.

Start with:

- `docs/quick-review.md`
- `docs/review-paths.md`
- `docs/review-feedback-examples.md`

Good fit:

```text
This catches the wrong-folder case, but it misses stale branches.
```

Turn real stories into fake scenarios before sharing them.

## Reviewing AI-Assisted Contributions

Use when you maintain a repo and a contributor sends AI-assisted work.

Start with:

- `docs/maintainer-flow.md`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `templates/verification-receipt.md`

Good fit:

```text
Before merging this AI-assisted PR, show what changed, what checks ran, and whether examples are synthetic.
```

The point is not to argue about tool use. The point is to make the contribution small, reviewable, and public-safe.
