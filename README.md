# MMSS Principle Synthesis

Evidence-aware architecture synthesis for AI agents.

Create, audit, repair, extend, and transfer modular MMSS architectures from sources, requirements, or existing stacks.

[English](README.md) · [Русский](README.ru.md)

![License: MIT](https://img.shields.io/badge/License-MIT-green.svg) ![Skill versions: 0.3.0 and 0.1.5](https://img.shields.io/badge/skills-0.3.0%20%7C%200.1.5-blue.svg) ![Status: experimental](https://img.shields.io/badge/status-experimental-orange.svg) [![Repository validation](https://github.com/Abstract-Mindfreak/mmss-principle-synthesis/actions/workflows/validate.yml/badge.svg)](https://github.com/Abstract-Mindfreak/mmss-principle-synthesis/actions/workflows/validate.yml)

## Overview

MMSS Principle Synthesis is an Agent Skill: an instruction file that helps an AI agent perform structured architecture work. MMSS is a project-defined architectural term; this repository does not assign an expansion to it.

## Capabilities

- Synthesize from source material, explicit requirements, or a supplied stack.
- Audit, validate, repair, extend, and transfer modular architectures.
- Keep evidence, inferences, requirements, assumptions, and checks distinguishable.
- Return structured JSON by default, while following an explicit output contract.

## Skill editions

This repository provides two separately installable editions:

- **Composite v0.3.0** (`mmss-principle-synthesis`): core instructions plus reference material in `ALL_REFERENCES.md`, indexed by `DISPATCH.md`. The files form one package and should stay together. The guide describes how an agent can find and read a section; the package does not include executable loader code.
- **Monolithic v0.1.5** (`mmss-principle-synthesis-monolithic`): the earlier single-file edition, kept available as a separate skill. Its skill name is unique so both editions can be discovered side by side.

The two editions are maintained as distinct versions. The monolithic copy preserves the v0.1.5 text, with its frontmatter name changed to avoid a duplicate skill identity. No behavioral equivalence claim is made.

## Related skills

Ten related skills are available as independent sibling packages under [`skills/`](skills/):

| Skill | Role |
| --- | --- |
| [`adaptive-commercial-specializer`](skills/adaptive-commercial-specializer/SKILL.md) | Builds commercial specializations from source material. |
| [`adaptive-open-skill-synthesizer`](skills/adaptive-open-skill-synthesizer/SKILL.md) | Creates or reshapes skills around open variables. |
| [`adaptive-sp-combinator`](skills/adaptive-sp-combinator/SKILL.md) | Explores and combines skills, systems, and properties. |
| [`data-to-skill`](skills/data-to-skill/SKILL.md) | Turns supplied data into a skill. |
| [`data-to-skill-transformer`](skills/data-to-skill-transformer/SKILL.md) | Transforms data into a skill specification. |
| [`mmss-schema-guided-agent-bridge`](skills/mmss-schema-guided-agent-bridge/SKILL.md) | Connects schemas, routing, and agent architectures. |
| [`session-process-logger`](skills/session-process-logger/SKILL.md) | Records a process from a session. |
| [`session-to-skill`](skills/session-to-skill/SKILL.md) | Derives a skill from session material. |
| [`skill-boundary-combinator`](skills/skill-boundary-combinator/SKILL.md) | Combines skills while tracking boundaries. |
| [`skill-quick-sampler`](skills/skill-quick-sampler/SKILL.md) | Samples and inventories skill catalogues. |

These are standalone skill packages. Their descriptions of relationships and contracts are maintained in each skill; their listing here does not assert that they all share identical contracts.

## Quick start

Install the composite edition with the [Skills CLI](https://github.com/vercel-labs/skills):

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

Structured JSON is the default unless the user requests another format. Stable machine-readable identifiers are preserved while human-readable content follows the user's language instructions. The skill's own language policy remains defined in its `SKILL.md`.

## Compatibility

Each package uses the Agent Skills `SKILL.md` convention with YAML frontmatter. The Skills CLI supports repository discovery and skill selection. This repository has not verified installation on individual agent platforms; host-specific behavior can differ.

## Validation and limitations

The local validator checks repository packaging, skill frontmatter, JSON fixtures, and local file links. GitHub Actions runs the same validator and `git diff --check`; these checks do not assess model outputs or architectural quality. See [evaluation notes](docs/evaluation.md) for the limits of one accompanied experiment.

## Repository structure

| Path | Purpose |
| --- | --- |
| `skills/mmss-principle-synthesis/` | Composite v0.3.0 package: `SKILL.md`, `ALL_REFERENCES.md`, and `DISPATCH.md` |
| `skills/mmss-principle-synthesis-monolithic/SKILL.md` | Monolithic v0.1.5 edition |
| `skills/<related-skill>/SKILL.md` | Ten standalone related skill packages |
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
