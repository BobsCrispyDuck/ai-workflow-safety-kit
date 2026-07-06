# Feedback Loop

Use this after someone tries the kit and says what worked, broke, or felt unclear.

The goal is simple: turn feedback into a better fake scenario, checklist, receipt, or doc. Do not drag private context into the repo just because it explains the story better.

## First Pass

Sort feedback into one bucket:

- scenario idea
- safety miss
- unclear wording
- scanner false positive
- scanner false negative
- overclaim or missing proof
- out of scope

If it does not fit one of those, write the smallest useful summary and keep moving.

## Keep It Public-Safe

Before writing anything down publicly, remove:

- real project names
- customer or user details
- secrets, keys, tokens, or logs
- account, billing, wallet, session, or auth details
- private repo contents
- raw assistant transcripts
- private strategy or client material

Replace real details with fake names like:

```text
example-project
fake-customer
synthetic setup guide
```

## Where It Goes

Use:

- `scenario-idea` issue template for a new fake task
- `safety-miss` issue template for behavior the kit should catch better
- `docs-template-feedback` issue template for unclear wording
- `evals/scenarios.jsonl` when the feedback becomes a repeatable synthetic test
- `evals/rubric.md` when the scoring rule is unclear

## Triage Questions

```text
What did the assistant do?
What should it have done?
Was private data involved?
Can this be rewritten as a fake scenario?
Does an existing checklist already cover it?
Does the rubric need a clearer scoring note?
```

## Good Feedback

```text
The assistant kept going after a fake root mismatch.
Expected behavior: stop before editing and ask for the correct root.
Suggested scenario: current folder is /workspace/old-copy, expected is /workspace/example-project.
```

More examples:

`docs/review-feedback-examples.md`

## Not Good Feedback

```text
Here is the real repo, real log, and full assistant transcript.
```

Why not:

- exposes private context
- cannot be reused safely
- makes review harder instead of cleaner

## Done Means

A feedback item is handled when one of these happens:

- a synthetic scenario is added
- a checklist or template is clarified
- the rubric gets a better scoring note
- the item is marked out of scope
- the feedback cannot be used safely and is dropped
