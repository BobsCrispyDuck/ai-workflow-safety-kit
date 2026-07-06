# Template: Verification Receipt

Use after a task is completed.

## Receipt Fields

```text
Task:
Changed files:
Commands/checks run:
Result:
Evidence:
Remaining risk:
Next approval needed:
```

## Good Receipt Example

```text
Task: Create synthetic safety checklist
Changed files:
- checklists/before-editing.md
Commands/checks run:
- private data scan
Result: pass
Evidence:
- no review terms found
Remaining risk:
- needs human review before publication
Next approval needed:
- publish approval
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

