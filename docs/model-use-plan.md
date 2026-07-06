# Model Use Plan

This kit works best when the model choice matches the risk of the task.

Do not use the strongest model for every tiny thing. Also do not use the cheapest model for the part where it can quietly publish the wrong thing.

## Use Cheap Models For

- drafting synthetic eval scenarios
- rewriting checklist wording
- finding unclear instructions
- grouping similar failure modes
- making first-pass examples
- turning rough notes into a cleaner template

These tasks should use public or fake content only.

## Use Stronger Models For

- deciding whether a task needs approval
- reviewing a public release before it ships
- checking whether a claim is backed by evidence
- comparing an assistant answer against the rubric
- spotting where private context could leak into public work
- doing the final audit before a larger task is called done

These are judgment tasks. They are where the expensive mistake usually hides.

## Do Not Send

Do not send these through model calls unless your project already has a clear, approved policy for it:

- secrets, keys, or tokens
- production logs or config
- customer or user data
- account, billing, wallet, session, or auth details
- private repo contents
- raw assistant transcripts with private context
- client material or private creative work

If the task needs that data to make sense, make a fake version first.

## Simple Routing

```text
Low risk:
- synthetic examples
- wording cleanup
- checklist formatting

Use a cheap model.

Medium risk:
- eval scoring
- release checklist review
- public docs review

Use a stronger model or a second review pass.

High risk:
- publishing
- submissions
- account settings
- billing/auth/session/wallet changes
- production deployments
- real user/customer data

Stop for explicit approval first.
```

## Useful Pattern

1. Use a cheap model to draft.
2. Run the kit checks.
3. Use a stronger model or human review for the risky part.
4. Record what was checked.
5. Stop before any external action that has not been approved.

## Receipt Snippet

```text
Model-use decision:
- low/medium/high risk:
- model used for drafting:
- model or reviewer used for audit:
- private data included: yes/no
- approval needed before external action: yes/no
```
