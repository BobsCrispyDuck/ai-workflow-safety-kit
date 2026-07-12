# Template: Verification Receipt

Use after a task is completed.

## Receipt Fields

```text
Task:
Approved scope:
Changed files:
Commands/checks run:
Result:
Evidence:
Remaining risk:
Not changed / not approved:
Next approval needed:
```

## Good Receipt Example

```text
Task: Create synthetic safety checklist
Approved scope:
- edit public documentation with synthetic content only
Changed files:
- checklists/before-editing.md
Commands/checks run:
- private data scan
Result: pass
Evidence:
- no review terms found
Remaining risk:
- needs human review before publication
Not changed / not approved:
- no publishing, account changes, keys, or private data
Next approval needed:
- publish approval
```

Check a completed receipt:

```text
python scripts/check-approval-receipt.py path/to/receipt.md
```

## Bad Receipt Example

```text
Done.
```

Why bad:

- no files
- no checks
- no evidence
- no remaining risk
- no approval boundary
