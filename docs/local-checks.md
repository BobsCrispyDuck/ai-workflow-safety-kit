# Local Checks

These checks are small on purpose.

They do not prove the repo is safe. They catch the easy-to-miss stuff before a change gets pushed.

Run everything:

```text
python scripts/check-all.py
```

Run one check:

```text
python scripts/check-scenarios.py
python scripts/check-links.py
python scripts/check-public-surface.py
```

## What The Checks Do

`scripts/check-scenarios.py`

Checks that every line in `evals/scenarios.jsonl` is valid JSON and has the required fields.

This is the boring check that keeps the scenario file from slowly turning into almost-JSON.

`scripts/check-links.py`

Checks local markdown links and obvious local file references.

This catches renamed docs, moved templates, and links that worked on one machine but not in the repo.

`scripts/check-public-surface.py`

Checks text files for obvious public-surface mistakes:

- local machine paths
- home-folder paths
- secret-shaped API keys
- private-key blocks
- generated-by-AI or generated-by-ChatGPT style residue
- internal agent markers

It is intentionally narrow. It does not flag every use of words like secret, token, billing, or account because this repo is about those safety boundaries.

## What The Checks Do Not Do

They do not replace a real review.

They do not know whether an example is useful.

They do not know whether a post, issue, or release should be sent.

They do not prove that a clean file has no private context. A clean scan only means this small set of patterns did not match.

For the bigger habit, use `templates/public-release-check.md` before anything public leaves your machine.

## Before A Pull Request

Do this:

1. Run `python scripts/check-all.py`.
2. Read any failures instead of fixing around them.
3. If you changed public-facing docs, skim `docs/false-positives-and-misses.md`.
4. If you changed scenarios, skim `docs/scenario-writing.md`.
5. Keep the pull request small enough that a person can review it.

If the checks pass but the change still feels weird, stop. The weird feeling is also data.
