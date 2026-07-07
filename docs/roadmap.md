# Roadmap

This roadmap keeps the kit small enough to actually use.

## v0.1

Status: published

What shipped:

- basic workflow-safety templates
- editing, publishing, submitting, and shared-token checklists
- synthetic examples for common assistant failure modes
- a starter eval scenario file and rubric
- Codex and general agent adaptation notes

## v0.2

Status: in progress

What has landed:

- expanded synthetic eval scenarios
- a demo walkthrough
- public-release checks
- model-use notes for cheap drafts, stronger review, and approval gates
- a no-install try-it-now test
- example result receipts for the try-it-now prompts
- documented false-positive and false-negative categories
- docs indexes for templates, checklists, examples, and guides
- quick review paths, reviewer prompts, and a reviewer scorecard
- public-safe issue templates and support guidance
- local checks for scenarios, doc links, and obvious public-surface mistakes
- maintainer flow for reviewing AI-assisted PRs without private context

Still worth improving:

- sharper synthetic scenarios from public feedback
- clearer wording where a first-time visitor gets stuck
- smaller copy sets for specific repo types
- better examples of weak versus useful receipts
- better rubric notes for borderline assistant behavior

Good enough to count:

- a new user can copy the quick start without needing a meeting about it
- eval scenarios cover safe, blocked, and approval-needed cases
- public release checks catch private data before publishing
- model-use guidance keeps public/synthetic drafting separate from risky review
- someone can compare guarded and unguarded assistant behavior on fake tasks
- example receipts make pass/fail review easier to compare
- scanner hits and clean scans are both treated as clues, not proof
- visitors can leave one public-safe review note without reading the whole repo

## v0.3

After that:

- more examples from real public feedback
- more focused copy packs for common repo setups
- lightweight before/after examples showing how the guardrails change assistant behavior
- clearer maintainer flow for turning feedback into one small change

Good enough to count:

- feedback gets turned into sanitized scenarios, not copied private stories
- project claims remain narrow and evidence-backed
- examples remain public-safe and reusable
- small contributors can find a useful task without project context

## Not The Thing

- real secrets, logs, or private repository content
- offensive security testing
- account, billing, or production tooling
- pretending this guarantees safety
