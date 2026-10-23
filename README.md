# MMSS Principle Synthesis

Evidence-aware architecture synthesis for AI agents.

Create, audit, repair, extend, and transfer modular MMSS architectures from sources, requirements, or existing stacks.

[English](README.md) · [Русский](README.ru.md)

![License: MIT](https://img.shields.io/badge/License-MIT-green.svg) ![Skill version: 0.1.5](https://img.shields.io/badge/skill-0.1.5-blue.svg) ![Status: experimental](https://img.shields.io/badge/status-experimental-orange.svg) [![Repository validation](https://github.com/Abstract-Mindfreak/mmss-principle-synthesis/actions/workflows/validate.yml/badge.svg)](https://github.com/Abstract-Mindfreak/mmss-principle-synthesis/actions/workflows/validate.yml)

## Overview

MMSS Principle Synthesis is an Agent Skill: an instruction file that helps an AI agent perform structured architecture work. MMSS is a project-defined architectural term; this repository does not assign an expansion to it.

## Capabilities

- Synthesize from source material, explicit requirements, or a supplied stack.
- Audit, validate, repair, extend, and transfer modular architectures.
- Keep evidence, inferences, requirements, assumptions, and checks distinguishable.
- Return structured JSON by default, while following an explicit output contract.

## Quick start

Install the skill with the [Skills CLI](https://github.com/vercel-labs/skills):

```sh
npx skills add Abstract-Mindfreak/mmss-principle-synthesis --skill mmss-principle-synthesis
```

To list skills in a local checkout without installing them:

```sh
npx skills add . --list
```

The skill provides instructions only. Agent behavior, tools, persistence, and compatibility depend on the host agent.

## Usage examples

Ask an agent to design a module from requirements, audit an existing architecture, or synthesize a system from supplied sources. Small illustrative prompts and expected properties are in [examples](examples/README.md). They are not evaluation results.

## How it works

The skill inspects the supplied foundation, identifies the requested operation and artifact, preserves provenance and uncertainty, constructs only the needed architecture, and reports checks within their actual scope. See [design principles](docs/design-principles.md).

## Output and language behavior

Structured JSON is the default unless the user requests another format. Stable machine-readable identifiers are preserved while human-readable content follows the user's language instructions. The skill's own language policy remains defined in `SKILL.md`.

## Compatibility

The file uses the Agent Skills `SKILL.md` convention with YAML frontmatter. The Skills CLI supports repository discovery and selection using the command above. This repository has not verified installation on individual agent platforms; host-specific behavior can differ.

## Validation and limitations

The local validator checks repository packaging, frontmatter fields, version, JSON fixtures, and local file links. GitHub Actions runs the same validator and `git diff --check`; these checks do not assess model outputs or architectural quality. See [evaluation notes](docs/evaluation.md) for the limits of one accompanied experiment.

## Repository structure

| Path | Purpose |
| --- | --- |
| `skills/mmss-principle-synthesis/SKILL.md` | The skill instructions |
| `examples/` | Synthetic prompts and expected properties |
| `docs/` | Design principles and evaluation scope |
| `scripts/validate_repository.py` | Local packaging validator |
| `.github/workflows/validate.yml` | Read-only repository validation |

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for reproducible reports, checks, and contribution terms.

## Project values

This project is created with the hope that it will help people learn, build useful tools, and share knowledge responsibly.

The author encourages peaceful, constructive uses that respect human dignity.

This statement expresses the author's values and does not add restrictions to the MIT License.

## Author

Created and maintained by Andrey Mundrievskiy, known online as Abstract-Mindfreak.

## License

Released under the [MIT License](LICENSE).
