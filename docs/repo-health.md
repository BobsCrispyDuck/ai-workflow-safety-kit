# Repo Health

This page is for the quick trust check.

If you are deciding whether this repo is worth reading, here is what I try to keep true.

## What Gets Checked

Every push runs the local checks in GitHub Actions:

```text
python scripts/check-all.py
```

That checks:

- public-surface residue that should not be in a clean public repo
- every local check script is documented and wired into the main runner
- eval scenarios are valid JSONL
- eval coverage notes still map to the scenario file
- docs, templates, examples, and checklists show up in their folder indexes
- local doc links still point somewhere real
- issue-template links still point at existing public templates

These checks are small on purpose. They catch boring drift before it turns into cleanup work.

## What The Checks Do Not Prove

They do not prove the repo is safe, complete, or production-ready.

They also do not replace a human skim. A clean check run can still miss:

- a vague checklist line
- an overconfident claim
- a missing scenario
- a public-safe example that teaches the wrong habit
- a link that works but points to the wrong path for a new visitor

That is why the repo asks for one small review note instead of a big audit.

## Manual Review Habit

Before public-facing changes, I look for:

- private paths, real logs, raw transcripts, or account-ish details
- grant, funding, or submission notes that do not belong in the public repo
- generated-by-tool residue
- claims that sound bigger than the kit really is
- review paths that ask too much from a cold visitor

If something feels off, the fix should usually be small:

- rewrite one line
- add one synthetic scenario
- sharpen one checklist item
- point one link at a better starting page

## Current Status

The repo is early.

The useful question is not "is this done?"

It is:

```text
Does this catch one more preventable mistake than an unguarded workflow?
```

If the answer is no, open one public-safe issue with the smallest example you can.

Start here:

- `docs/quick-review.md`
- `docs/reviewer-brief.md`
- `docs/reviewer-scorecard.md`
- `docs/issue-guide.md`
