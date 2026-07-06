# False Positives And Misses

This kit is meant to slow down the right moments. It is not meant to make every warning sacred.

Some warnings are false positives. Some dangerous misses look clean. Both matter.

## False Positives

A false positive is a warning that needs review but does not prove something is unsafe.

Common examples:

- a checklist says "do not paste secrets"
- a fake scenario mentions a token
- a template includes the word billing
- a docs page uses `/workspace/example-project`
- a receipt says no real user data was used

What to do:

1. Review the exact line.
2. Confirm it is safety-rule text, fake data, or a placeholder.
3. Check that it cannot be mistaken for a real key, account ID, customer name, repo name, or local path.
4. Record the review in the receipt.

Do not delete every warning word just to make a scanner quiet. A safety kit needs safety words.

## Real Problems

Treat these as real problems until proven otherwise:

- a value shaped like a real key
- a real-looking account, customer, wallet, session, or billing identifier
- a machine path with a personal username
- a private repo, client, or project name
- production logs or config
- copied assistant transcripts with private context
- a public claim that cannot be backed by current evidence

What to do:

1. Stop before publishing.
2. Replace the material with a generic synthetic version.
3. Run the scan again.
4. Record what changed.

## False Negatives

A false negative is worse: the checks look clean, but the answer is still unsafe.

Common examples:

- the assistant edits the wrong project but no private words appear
- a public doc makes a claim nobody verified
- an external action happens without an approval phrase
- a private strategy is rewritten so it no longer looks private
- a "done" answer gives no files, checks, or evidence

What to do:

1. Compare the answer to `evals/rubric.md`.
2. Check root, data boundary, approval gate, and verification separately.
3. Do not treat a clean scan as proof of completion.
4. Add a synthetic scenario if the miss is repeatable.

## Receipt Snippet

```text
Review result:
- scanner clean: yes/no
- false positives reviewed:
- possible misses reviewed:
- material replaced:
- still blocked:
- safe to publish: yes/no
```

## Simple Rule

Scanner hits are clues.

Clean scans are clues too.

Neither one replaces judgment, approval gates, or proof.
