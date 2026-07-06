# Review Paths

If you are looking at this repo cold, do not start by reading every file.

Pick one path, spend a few minutes, and leave the smallest useful note.

For the shortest handoff note, use `docs/reviewer-brief.md`.

## Path 1: Try The Hard Prompt

Use:

`docs/try-it-now.md`

Look for:

- does the assistant stop before publishing?
- does it catch private/public context drift?
- does it ask for proof before saying done?

Good feedback:

```text
The guarded prompt caught the private-data issue, but it did not call out the missing approval before publishing.
```

## Path 2: Read The Scenarios

Use:

`evals/scenarios.jsonl`

Optional scorecard:

`docs/eval-scorecard.md`

Look for one missing failure mode. The best additions are boring:

- stale branch
- wrong project root
- fake approval treated as real approval
- private log copied into public docs
- clean scan treated as enough proof

Good feedback:

```text
Add a scenario where the assistant sees a clean scan but the doc still quotes private customer context.
```

## Path 3: Check The Stop Points

Use:

- `templates/approval-gate.md`
- `templates/public-release-check.md`
- `templates/final-audit.md`

Look for unclear stop conditions.

Good feedback:

```text
The approval gate mentions account changes, but it should also say project settings.
```

## Keep It Usable

Do not post real logs, keys, account details, private repo names, or raw transcripts.

Rewrite real stories as fake examples:

```text
example-project
fake-customer
synthetic release note
```

More:

- `docs/quick-review.md`
- `docs/review-feedback-examples.md`
- `docs/response-snippets.md`
