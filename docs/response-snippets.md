# Response Snippets

Use these when replying to public feedback.

Keep replies short. Do not ask people to post private details. Do not turn a small note into a big process.

## Scenario Idea

```text
Thanks, this is a useful failure mode.

I am going to rewrite it as a synthetic scenario so it can be reused without carrying private context.
```

## Safety Miss

```text
Good catch. The useful part here is the stop condition.

I will turn this into either a rubric note or a fake scenario, depending on whether it is a scoring problem or a missing case.
```

## Docs Feedback

```text
That wording is vague. I will tighten it and keep the claim narrow.
```

## Needs Sanitizing

```text
I cannot use the private details as-is.

If you can rewrite this as a fake setup with no logs, accounts, users, repo names, or raw transcripts, I can turn the pattern into a scenario.
```

## Out Of Scope

```text
That is outside what this kit is trying to solve.

I am keeping this focused on workflow guardrails: root checks, data boundaries, approval gates, and verification receipts.
```

## After Fixing

```text
Handled in the public docs/evals with synthetic details only.

I also ran the local checks before pushing.
```
