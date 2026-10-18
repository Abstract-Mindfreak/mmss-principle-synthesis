# Contributing

Contributions should keep the skill's scope, provenance distinctions, and truthful reporting of checks intact.

## Bug reports

Include the task and skill version, a minimal reproducible prompt or input, expected and actual behavior, checks performed, and relevant limitations. Redact secrets and personal data. Do not attach private source code or correspondence.

## Proposals

Keep proposals small and explain the problem, intended behavior, compatibility impact, and evidence or rationale. Do not present a design goal as an observed result.

## Checks

Run from the repository root:

```sh
python scripts/validate_repository.py
git diff --check
```

The validator checks packaging and fixtures. It does not evaluate model quality or runtime behavior.

## Provenance and scope

Preserve the distinction between source observations, inferences, requirements, assumptions, and checks. State the scope and limitations of evidence; do not broaden a local test into a general guarantee.

## Contribution terms

By submitting a contribution, you make it available under the repository's MIT License unless separately agreed otherwise. No contributor agreement or transfer of exclusive rights is required.
