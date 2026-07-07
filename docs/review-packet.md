# Review Packet

Send this page when you want one useful review without asking someone to read the whole repo.

The best review is one small miss:

- a failure mode the kit does not cover
- a checklist line that feels vague
- a stop condition that should be stronger
- a place where the docs sound too confident
- a reason this would not work in a real coding-agent workflow

No stars needed. No private stories needed.

## Ten-Minute Path

1. Read `docs/one-page-kit.md`.
2. Try one prompt from `docs/reviewer-prompts.md`.
3. Skim `evals/coverage.md`.
4. Send back the smallest useful miss.

If you only have five minutes, use `docs/quick-review.md`.

If you want a guided route, use `docs/repo-tour.md`.

## What To Send Back

```text
Path tried:
What worked:
What missed:
One fake scenario or checklist line to add:
Private details removed: yes/no
```

Useful example:

```text
Path tried:
Prompt 3 from docs/reviewer-prompts.md

What worked:
It caught the wrong folder before editing.

What missed:
It did not explain that publishing also needed separate approval.

One fake scenario or checklist line to add:
Assistant catches root mismatch but still treats "publish now" as approved.

Private details removed:
yes
```

## Public-Safe Feedback Links

Use the smallest one that fits:

- [small feedback note](https://github.com/BobsCrispyDuck/ai-workflow-safety-kit/issues/new?template=small-feedback.yml)
- [reviewer scorecard](https://github.com/BobsCrispyDuck/ai-workflow-safety-kit/issues/new?template=reviewer-scorecard.yml)
- [scenario idea](https://github.com/BobsCrispyDuck/ai-workflow-safety-kit/issues/new?template=scenario-idea.yml)
- [safety miss](https://github.com/BobsCrispyDuck/ai-workflow-safety-kit/issues/new?template=safety-miss.yml)
- [docs/template feedback](https://github.com/BobsCrispyDuck/ai-workflow-safety-kit/issues/new?template=docs-template-feedback.yml)

For help choosing, use `docs/issue-guide.md`.

## What Not To Send

Do not send:

- real logs
- secrets or keys
- customer or user details
- private repo names
- account, billing, wallet, session, or auth details
- screenshots with private context
- raw assistant transcripts

If the real story matters, rewrite it as a fake one first.

## If You Are Asking For The Review

Use one relevant person or one small group.

Do not mass-send the repo.

Do not ask for stars.

Do not send the same ask repeatedly if nobody replies.

For the short ask text, use `docs/review-request.md`.
