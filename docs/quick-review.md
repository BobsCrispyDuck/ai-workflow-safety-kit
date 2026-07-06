# Quick Review

If you have five minutes, do not read everything.

Look for one place where the kit would have helped you slow down, or one place where it still feels vague.

## Fast Path

1. Read `README.md`.
2. Try `docs/try-it-now.md`.
3. Skim `evals/scenarios.jsonl`.
4. Open the issue template that fits:
   - scenario idea
   - safety miss
   - docs/template feedback

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

## Maintainer Notes

When feedback comes in:

- keep the useful behavior
- drop the private details
- turn the pattern into a fake scenario, checklist tweak, or rubric note
- run `python scripts/check-scenarios.py` after eval changes
