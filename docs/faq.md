# FAQ

## What Is This?

A small set of templates, checklists, fake scenarios, and receipts for AI-assisted coding work.

It is meant to help an assistant slow down before the common workflow mistakes:

- wrong folder
- private material in public docs
- external action without clear approval
- "done" without proof

## Is This A Security Framework?

No.

It can help catch workflow mistakes before they become expensive. It does not replace security review, legal review, compliance review, production approval, or someone who knows the system.

## Who Is It For?

Solo builders and small teams using coding assistants.

It is especially useful when you do not have a big process around:

- public docs
- open-source repo work
- generated examples
- assistant-made changes
- small external submissions or posts

## What Should I Try First?

Fastest path:

1. Read `docs/try-it-now.md`.
2. Try one prompt from `docs/reviewer-prompts.md`.
3. Fill out `docs/reviewer-scorecard.md`.

If you want to copy pieces into your own workflow, start with:

- `templates/work-session-check.md`
- `templates/project-root-check.md`
- `templates/private-public-data-split.md`

For bigger copy sets, use `docs/starter-pack.md`.

## Can I Use This With Any Coding Assistant?

Mostly, yes.

The files are plain Markdown on purpose. Copy the relevant checklist or template into the assistant instructions and adjust the project root, blocked data, and approval rules.

See:

- `docs/adapting-to-codex.md`
- `docs/adapting-to-other-agents.md`

## Why Are The Scenarios Fake?

Because real logs, repo names, account details, customer data, screenshots, and transcripts do not belong in a public safety repo.

Fake scenarios make the behavior reusable without dragging private context along with it.

## What Should I Not Paste Into Issues?

Do not paste:

- secrets or keys
- private logs
- customer or user details
- account, billing, wallet, session, or auth details
- private repo names
- screenshots with private context
- raw assistant transcripts

Rewrite the real story as a fake one first.

## What Kind Of Feedback Helps?

Small, specific feedback is best.

Good:

```text
The assistant caught the wrong folder, but it still claimed done without saying which checks were run.
```

Also good:

```text
Add a fake scenario where CI fails and the assistant waves it away as unrelated.
```

Not useful:

```text
Here is the full private transcript and production log.
```

Use:

- `docs/reviewer-scorecard.md`
- `docs/review-feedback-examples.md`
- `docs/feedback-loop.md`

## Can This Be Shared?

Yes, but keep it low-noise.

Use `docs/sharing-guide.md`.

The best ask is not "please star this." The best ask is:

```text
What boring failure mode is missing?
```

## What Counts As Done?

For this kit, "done" should usually include:

- what changed
- what was checked
- what was not checked
- whether approval is still needed
- what evidence proves the current state

Use:

- `templates/verification-receipt.md`
- `templates/final-audit.md`
- `docs/example-result-receipts.md`
