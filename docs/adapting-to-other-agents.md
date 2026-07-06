# Adapting To Other Agents

This kit is not tied to one AI tool.

For any coding assistant, preserve the same core loop:

```text
root -> data lane -> approval gate -> local work -> verification receipt -> final audit
```

## What To Configure

- where the project lives
- which paths are protected
- what counts as private data
- what actions need approval
- what evidence proves completion

## What To Avoid

- relying on memory alone
- letting the assistant infer approval
- using real secrets in examples
- treating a successful build as proof the product works
- calling work complete without checking current state

For a copyable starter rule, use `docs/copy-into-your-repo.md`.
