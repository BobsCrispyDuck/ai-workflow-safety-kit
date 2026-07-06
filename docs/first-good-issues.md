# First Good Issues

Want to help without knowing the whole repo? Pick one small thing.

Keep it public-safe. Use fake examples. Keep claims boring and narrow.

## Add A Scenario

Look at `evals/scenarios.jsonl`.

Skim `evals/coverage.md` first so you can see the thin spots.

Add one synthetic task where an assistant should:

- stop before publishing
- catch a wrong folder or stale branch
- refuse private material in a public doc
- ask for explicit approval before account or production-ish action

Then run:

```text
python scripts/check-all.py
```

## Tighten A Checklist

Pick one checklist in `checklists/`.

Good changes are usually one line:

```text
Before publishing, confirm examples are synthetic and no private logs are quoted.
```

Avoid big rewrites unless the checklist is actually hard to use.

## Improve A Template

Pick one file in `templates/`.

Useful improvements:

- clearer stop condition
- better receipt wording
- fewer vague phrases
- one concrete example

## Improve The Rubric

Look at `evals/rubric.md`.

Add a scoring note for a behavior that is easy to miss:

- clean scan treated as proof
- urgency treated as approval
- fake-but-real-looking logs treated as safe
- public doc mixed with private context

## Review The Docs

Try `docs/reviewer-prompts.md`.

Then leave feedback using:

- `docs/review-feedback-examples.md`
- `docs/response-snippets.md`

## Before Opening A PR

Run:

```text
python scripts/check-all.py
```

Then use `.github/PULL_REQUEST_TEMPLATE.md`.
