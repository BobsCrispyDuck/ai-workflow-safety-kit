# Template: Private / Public Data Split

Use before giving context to an AI system, creating examples, or preparing anything public.

## Public Or Synthetic Lane

Allowed:

- fake project names
- fake paths
- fake tokens
- public docs
- synthetic examples
- generic lessons
- intentionally open-sourceable templates

## Private Lane

Do not expose without explicit approval:

- private repo contents
- raw assistant transcripts
- secrets or API keys
- production logs
- deployment configs
- user/customer data
- account identifiers
- wallet/session/auth/billing data
- private creative/IP material

## Rewrite Pattern

Replace specific private details with generic equivalents.

Examples:

- `/workspace/real-private-project` -> `/workspace/example-project`
- real API key -> `[example API key omitted]`
- real user record -> `synthetic user`
- private product name -> `PrivateProject`

## Receipt Snippet

```text
Data lane:
- public/synthetic:
- private data excluded:
- replacements made:
- safe to share externally: yes/no
```
