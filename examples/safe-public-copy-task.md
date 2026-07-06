# Example: Safe Public Copy Task

## Scenario

A user asks an AI assistant to rewrite a public README paragraph for clarity.

The paragraph contains:

- no secrets
- no private repo details
- no customer data
- no production logs
- no account IDs

## Safe Assistant Behavior

The assistant may:

- rewrite the paragraph locally
- preserve meaning
- avoid inventing claims
- report the file changed

## Required Receipt

```text
Task: Rewrite public README paragraph
Data lane: public
Changed files:
- README.md
Checks:
- reviewed for private terms
Result:
- public copy updated
Next approval:
- publish approval needed before external release
```
