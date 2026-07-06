# Maintainer Checklist

Use this after someone leaves a small review note, scorecard, or issue.

The goal is not to win the thread. The goal is to turn one useful miss into one safer repo change.

## First Read

Before replying or editing, decide what the feedback actually is:

- missing fake scenario
- unclear checklist line
- weak approval gate
- weak proof before "done"
- confusing docs path
- overclaim
- out of scope
- unsafe because it includes private material

If it is mostly noise, keep the useful bit and leave the rest alone.

## Keep The Reusable Part

Keep:

- what the assistant did
- what the assistant should have done
- where it should have stopped
- the smallest fake setup that explains the problem

Drop:

- real logs
- secrets or keys
- customer or user details
- private repo names
- account, billing, wallet, session, or auth details
- screenshots with private context
- raw assistant transcripts
- private strategy, client material, or production config

If a real story is useful, rewrite it first:

```text
example-project
fake-customer
synthetic release note
```

## Pick One Change

Choose the smallest file that would make the same miss less likely next time.

| Feedback says | Change |
|---|---|
| "This case is missing" | add one row to `evals/scenarios.jsonl` |
| "The scoring is unclear" | tighten `evals/rubric.md` |
| "I did not know where to start" | improve `docs/repo-tour.md` or `docs/quick-review.md` |
| "This line is vague" | edit the checklist or template line |
| "This sounds too confident" | edit `docs/known-limits.md` or the claim itself |
| "This includes private detail" | do not use it until rewritten as synthetic |

Do not add a new page when one line in an existing page would fix it.

## Before You Ship

Check:

- public version uses only fake or public details
- no private names, logs, transcripts, screenshots, keys, or account details
- the change is small enough to review
- local checks pass
- any new scenario is valid JSONL
- the reply does not ask for private material

Run:

```text
python scripts/check-all.py
```

If you changed scenarios, also check the scenario count:

```text
python scripts/check-scenarios.py
```

## Good Reply

```text
Thanks. I can use the workflow pattern, but not the private detail.

I rewrote it as a synthetic case and added the smaller stop condition.
```

## If You Do Nothing

That is allowed.

Some feedback is not reusable, not safe to quote, already covered, or outside the kit.

Say so plainly and move on.

Useful links:

- `docs/feedback-loop.md`
- `docs/triage-guide.md`
- `docs/review-feedback-examples.md`
- `docs/response-snippets.md`
