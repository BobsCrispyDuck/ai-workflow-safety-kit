# Triage Guide

Use this after someone leaves a public issue, scorecard, or small review note.

The job is not to preserve every detail. The job is to keep the reusable failure mode and drop anything that should not be public.

## First Read

Put the note in one bucket:

- useful as-is
- useful after sanitizing
- needs a question
- already covered
- out of scope
- cannot be used safely

If it includes private material, do not quote it back.

## Strip It Down

Keep:

- what the assistant did
- what it should have done
- the stop condition
- the smallest fake setup that explains it

Remove:

- real logs
- secrets or keys
- customer or user details
- private repo names
- account, billing, wallet, session, or auth details
- screenshots with private context
- raw assistant transcripts
- private strategy or client material

## Pick The Change

Use the smallest fix that would catch the pattern next time.

| Feedback points to | Change |
|---|---|
| missing fake task | `evals/scenarios.jsonl` |
| unclear scoring | `evals/rubric.md` |
| vague stop condition | checklist or template |
| confusing docs | doc wording |
| repeated reviewer confusion | `docs/reviewer-prompts.md` or `docs/reviewer-scorecard.md` |
| unsafe private detail | no public change until rewritten |

## Reply Shape

Keep replies short.

```text
Thanks. I can use the workflow pattern, but not the private details.

I am rewriting it as a synthetic case and will keep the public version generic.
```

If it is already covered:

```text
This looks covered by the approval gate, but the docs may not point there clearly enough.

I will tighten the pointer rather than add a duplicate scenario.
```

If it is out of scope:

```text
I am going to leave this out of the kit.

This repo is focused on workflow guardrails: root checks, data boundaries, approval gates, and proof before done.
```

## Before Closing

Check:

- did the public version use only fake or public details?
- did it avoid overclaiming?
- did the change point to the smallest useful file?
- did local checks run if files changed?
- did the reply avoid asking for private material?

## Useful Links

- `docs/issue-guide.md`
- `docs/feedback-loop.md`
- `docs/review-feedback-examples.md`
- `docs/response-snippets.md`
- `docs/scenario-writing.md`
