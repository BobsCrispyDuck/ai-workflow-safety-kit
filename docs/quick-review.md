# Quick Review

If you have five minutes, do not read everything.

Look for one place where the kit would have helped you slow down, or one place where it still feels vague.

If you want a narrower route, use `docs/review-paths.md`.

If you are sending the repo to someone else, use `docs/reviewer-brief.md`.

If you only know how much time you have, use `docs/repo-tour.md`.

If you want to know what the public branch checks, use `docs/repo-health.md`.

If you want a concrete before/after example, use `docs/before-after.md`.

## Fast Path

1. Read `README.md`.
2. Try `docs/try-it-now.md`.
3. Try one prompt from `docs/reviewer-prompts.md`.
4. Use `docs/feedback-template.md` for one small note, or fill out `docs/reviewer-scorecard.md` for a fuller pass.
5. Use `docs/review-feedback-examples.md` if you want a model for what to send back.
6. Skim `evals/scenarios.jsonl`.
7. Open the issue template that fits:
   - [reviewer scorecard](https://github.com/BobsCrispyDuck/ai-workflow-safety-kit/issues/new?template=reviewer-scorecard.yml)
   - [scenario idea](https://github.com/BobsCrispyDuck/ai-workflow-safety-kit/issues/new?template=scenario-idea.yml)
   - [safety miss](https://github.com/BobsCrispyDuck/ai-workflow-safety-kit/issues/new?template=safety-miss.yml)
   - [docs/template feedback](https://github.com/BobsCrispyDuck/ai-workflow-safety-kit/issues/new?template=docs-template-feedback.yml)

## What To Look For

Useful feedback usually sounds like:

```text
This catches the wrong-folder case, but it does not say enough about stale branches.
```

Or:

```text
The assistant should stop when a public doc asks for a real support log, even if the user says the log is harmless.
```

That kind of note can become a synthetic scenario or a sharper checklist line.

## What Not To Post

Do not post:

- real logs
- secrets or keys
- customer or user details
- private repo names
- account, billing, wallet, session, or auth details
- raw assistant transcripts
- screenshots with private context

If the real story matters, rewrite it as a fake one first.

## Good Enough Review

A useful review can be tiny:

```text
I tried the hard prompt in docs/try-it-now.md.
The assistant stopped before publishing, but it did not explain the root mismatch clearly.
Suggested scenario: stale branch plus wrong root.
```

No ceremony needed.

More examples:

`docs/review-feedback-examples.md`

Scorecard:

`docs/reviewer-scorecard.md`

Small feedback template:

`docs/feedback-template.md`

Known limits:

`docs/known-limits.md`

Public reply snippets:

`docs/response-snippets.md`

## Maintainer Notes

When feedback comes in:

- keep the useful behavior
- drop the private details
- turn the pattern into a fake scenario, checklist tweak, or rubric note
- run `python scripts/check-all.py` before pushing
- use `docs/local-checks.md` when a check failure is unclear
