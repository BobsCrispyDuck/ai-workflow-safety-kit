# Reviewer Brief

If someone sent you this repo, you do not need to read the whole thing.

The best review is one small note about where an assistant should slow down and does not.

If you want a time-boxed path first, use `docs/repo-tour.md`.

If you are asking someone else for review, use `docs/review-request.md`.

## The Ask

Try one thing and send back one useful miss.

Good notes look like:

```text
The kit catches publishing without approval, but it does not say enough about reposting when a first post is pending.
```

Or:

```text
Add a scenario where an assistant treats a clean scanner result as enough proof even though it never checked the project root.
```

## Ten-Minute Route

1. Read `docs/one-page-kit.md`.
2. Try one prompt from `docs/reviewer-prompts.md`.
3. Skim `evals/coverage.md`.
4. Fill out `docs/reviewer-scorecard.md`.

That is enough.

## What To Look For

Look for boring misses:

- wrong folder
- stale branch
- missing approval
- private material drifting into public docs
- account or billing changes treated as normal edits
- reposting or second-channel posting from vague approval
- clean scan treated as full proof
- "done" without evidence

## What Not To Send

Do not send:

- real logs
- secrets or keys
- customer or user details
- private repo names
- account, billing, wallet, session, or auth details
- screenshots with private context
- raw assistant transcripts

If the real story matters, turn it into a fake one first.

## Tiny Review Format

```text
Path tried:
What worked:
What missed:
One fake scenario or checklist line to add:
Private details removed: yes/no
```

For more structure, use `docs/reviewer-scorecard.md`.

On GitHub, use the reviewer scorecard issue template.

For examples, use `docs/review-feedback-examples.md`.
