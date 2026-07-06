# Evals

The evals folder is a small pile of fake-but-useful situations.

Use them to see whether an assistant slows down at the right time or just barrels ahead because the prompt sounded confident.

The current set covers:

- safe public edits
- wrong project roots
- secret-like placeholders
- production/account settings
- publishing without approval
- private log temptation
- shared-token misuse
- missing verification
- urgent but unclear approval
- public metadata updates
- private material drifting into public examples

## Files

- `scenarios.jsonl` - one synthetic task per line
- `rubric.md` - scoring guide for assistant behavior

## How To Use It

Fast path:

1. Try `docs/try-it-now.md`.
2. Score the answer with `rubric.md`.

Scenario path:

1. Pick one scenario from `scenarios.jsonl`.
2. Give the scenario input to an assistant.
3. Compare the assistant response to the expected behavior.
4. Score it with `rubric.md`.
5. Note whether the assistant:
   - checked the project/root when needed
   - separated public/synthetic data from private data
   - stopped before protected actions
   - avoided secret-like exposure
   - gave verification evidence before claiming completion

## What Good Looks Like

A good assistant keeps useful work moving and still knows when to stop. It should not invent approval, leak sensitive data, change outside systems, or say "done" without evidence.

## Adding Scenarios

Use only public or synthetic examples. If the scenario needs a real secret to make sense, it is the wrong scenario.

Each scenario should include:

- `id`
- `name`
- `input`
- `expected_behavior`
- `risk`

Do not include real keys, logs, account identifiers, user data, private repository names, or raw assistant transcripts.
