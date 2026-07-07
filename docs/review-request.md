# Review Request

Use this when asking one relevant person or small group to look at the repo.

Do not mass-send it. Do not drop it into unrelated channels. Do not ask for private stories.

Before sending, use `checklists/before-asking-for-review.md`.

## Short Ask

```text
I made a small public repo for coding-agent workflow guardrails:

https://github.com/BobsCrispyDuck/ai-workflow-safety-kit

If you have 10 minutes, I would rather get one missing failure mode than a general thumbs-up.

The quickest path is the "What Would Help Most" section in the README or docs/reviewer-brief.md.
```

Clean handoff link:

`docs/review-packet.md`

## More Specific Ask

```text
I am looking for one boring workflow failure mode this repo does not cover yet.

It is a small kit for coding-agent guardrails: wrong folder, private context in public work, external action without approval, and "done" without proof.

No private logs or transcripts needed. A fake scenario is better.

Repo:
https://github.com/BobsCrispyDuck/ai-workflow-safety-kit

Useful starting point:
README.md

Clean handoff:
docs/review-packet.md

Or, if you want the short review format:
docs/reviewer-brief.md

Smallest GitHub feedback path:
https://github.com/BobsCrispyDuck/ai-workflow-safety-kit/issues/new?template=small-feedback.yml

Fuller GitHub scorecard:
https://github.com/BobsCrispyDuck/ai-workflow-safety-kit/issues/new?template=reviewer-scorecard.yml
```

## When To Use It

Good fit:

- someone already talks about coding-agent workflow
- a small team already uses coding assistants
- a public thread asks about guardrails, evals, or safer contribution flows
- a maintainer asks for workflow examples

Bad fit:

- cold DMs to strangers
- unrelated promo threads
- repeated posts after no response
- places where link drops are unwelcome
- support threads where people need help with a different problem

## What To Ask For

Ask for one thing:

- one missing fake scenario
- one unclear checklist line
- one weak stop condition
- one place the docs overclaim
- one reason the repo would not be useful

Do not ask for:

- stars
- private logs
- private repo access
- customer stories
- raw assistant transcripts
- screenshots with private context

## Follow-Up

If someone replies, use:

- `docs/triage-guide.md`
- `docs/feedback-loop.md`
- `docs/response-snippets.md`

If nobody replies, improve the repo. Do not immediately repost the same ask somewhere else.
