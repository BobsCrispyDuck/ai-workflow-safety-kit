# Known Limits

This kit is useful, but it is small.

It helps an assistant slow down before common workflow mistakes. It does not prove the work is safe.

## It Does Not Replace Review

Still use the review that fits the work:

- security review
- legal or compliance review
- production approval
- code review from someone who knows the system
- account or billing owner approval

The templates can help you notice when one of those reviews is needed. They do not do the review for you.

## It Does Not Detect Everything

The checks here are simple.

They can miss:

- private context rewritten in a way that still identifies the source
- risky changes hidden behind harmless wording
- stale branch or deploy state outside the files being edited
- claims that sound true but were not verified
- screenshots or copied output with private details

A clean scan is a clue. It is not a receipt.

## It Depends On Honest Boundaries

The kit works best when the task has clear boundaries:

- expected project root
- allowed data
- blocked data
- approval needed before external action
- proof needed before calling work done

If those boundaries are vague, the assistant can still drift.

## It Uses Fake Scenarios

The eval scenarios are synthetic on purpose.

That keeps the repo public-safe, but it also means the scenarios are not a full model benchmark. They are small decision checks for common builder mistakes.

## It Will Need More Real Feedback

The next useful improvements should come from people trying it:

- where a checklist felt vague
- where a scenario missed a real failure mode
- where a template slowed down the wrong thing
- where an assistant passed the wording but missed the point

Rewrite that feedback as a fake example before posting it.

Use:

- `docs/review-paths.md`
- `docs/feedback-loop.md`
- `docs/first-good-issues.md`
