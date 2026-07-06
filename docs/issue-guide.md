# Issue Guide

Use this when you want to leave a useful public note without turning it into a big report.

Pick the smallest template that fits.

## Reviewer Scorecard

Use this after trying one prompt or one scenario.

Good for:

- quick yes/no/unclear review
- one thing the assistant caught
- one thing it missed
- one fake scenario or checklist line to add

Use when:

```text
I tried something from the repo and want to report one small result.
```

## Scenario Idea

Use this when the kit is missing a fake workflow situation.

Good for:

- wrong project roots
- stale branches
- private/public data drift
- broad approval treated as exact approval
- weak proof before "done"

Use when:

```text
The repo should test this behavior, but I can describe it with fake details.
```

## Safety Miss

Use this when the assistant did something the kit should catch better.

Good for:

- missing approval gate
- private material slipping into public work
- external action before a stop
- scan result treated as full proof
- unsupported public claim

Use when:

```text
The assistant should have stopped or explained risk, but it kept going.
```

## Docs Or Template Feedback

Use this when wording is confusing or a checklist line is missing.

Good for:

- unclear stop condition
- missing example
- checklist line that is too vague
- receipt wording that does not ask for enough proof

Use when:

```text
This page almost works, but one line would make it clearer.
```

## Before You Open An Issue

Remove or rewrite:

- real logs
- secrets or keys
- customer or user details
- private repo names
- account, billing, wallet, session, or auth details
- screenshots with private context
- raw assistant transcripts

Replace real details with fake names:

```text
example-project
fake-customer
synthetic setup guide
```

## Not Sure Which One?

Use reviewer scorecard if you tried a prompt.

Use scenario idea if you are suggesting a new fake test.

Use safety miss if something unsafe or unclear happened.

Use docs/template feedback if the fix is just wording.
