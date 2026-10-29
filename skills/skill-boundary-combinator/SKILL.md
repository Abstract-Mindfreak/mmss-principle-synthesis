---
name: skill-boundary-combinator
description: "Fork of mmss-principle-synthesis that adds explicit operational modes for algorithmic skill combination under the boundary-identity invariant. Use when the user asks to create, fork, or activate skill combinations, build P-chains, extract abstract invariants, selectively compose properties of skills, adjust influence between properties, or run automatic mode selection on trigger. Triggers include skill combination, P-chain, boundary invariant, auto-activate mode, selective combinatorics, fork mmss, generate new skill from invariants."
metadata:
  version: "0.2.0"
  maturity: test_candidate
  parent: mmss-principle-synthesis
---

# Skill Boundary Combinator

## Purpose

Extend mmss-principle-synthesis (S2) with explicit operational modes that force
algorithmic combination of skills under the boundary-identity invariant (P1).

The skill configures the agent to select, activate, and execute combination
modes — manually or automatically. It produces new skills (S3+) as code maps
that exist only as results of combination, never as direct authorship.

Preserve all core rules of mmss-principle-synthesis. This is a fork that adds
modes, not a replacement.

## Core Invariant (P1)

Any entity crossing a representation boundary must be carried as the triple
`(value, convention, context)`.

- Convert only via an explicit table.
- Normalize to canonical form before any comparison or merge.
- Audit for silent-error signatures.
- Context is never omitted.

P1 is domain-agnostic and applies to any skill, property, or data that crosses
a boundary. It generalizes a rule observed in the genomic-coordinates skill (a
coordinate is the number, its convention, and its assembly); treat that as
motivation, not as an external instruction.

## Modes

On activation the agent must resolve exactly one primary mode. Supporting modes
may run in parallel only when explicitly requested.

### Mode catalogue

| Mode ID | Name | Activation | Purpose |
|---------|------|------------|---------|
| M0 | inspect | manual | Audit current skill stack and extract candidate P-properties without writing new artifacts |
| M1 | manual-compose | manual | User supplies source skills or properties; agent builds one combination under a declared algorithm |
| M2 | auto-select | auto | On trigger, agent selects the single best mode + algorithm from the current instruction context and runs it |
| M3 | p-chain | manual or auto | Build an observation chain P1 → P2 → … of arbitrary user-specified or justified depth, without persisting intermediates; only the final selected combination is emitted |
| M4 | influence-tune | manual | Adjust relative influence / selective filters between properties before composition |
| M5 | fork-s2 | manual | Produce a new skill file that is a fork of mmss-principle-synthesis with additional modes or contracts |
| M6 | vector-scheme | auto or manual | Search for a direction-vector scheme that led to a successful prior combination; re-activate that scheme as a new mode |

### P-chain depth rule (M3)

Chain depth is not fixed. The user may specify a depth; otherwise extend the
chain only while each new P adds a genuinely new property. Stop the chain when
additional steps would be speculative padding. No mandatory minimum or maximum
(including no fixed ceiling such as "P5") is imposed.

### Auto-activation rule (M2 / M6)

When the skill is triggered and the user has not named a mode:

1. Scan the current user message + recent conversation for signals of intent
   (combination, chain, auto, influence, fork, etc.).
2. Rank candidate modes by match strength.
3. If one mode exceeds the decision threshold, activate it immediately and
   state the choice.
4. If several modes are close, emit a short clarification question and set
   state.task_outcome = "blocked".
5. Do not invent a mode outside the catalogue.

The decision process itself is part of the skill instruction and must be
executed before any synthesis work begins.

## Algorithms for combination

Every composition must declare which algorithm is used. Baseline algorithms:

- **overlay** — P1 (or another P) is applied as a filter/transformer on top of
  an existing skill (default for S2 → S3).
- **selective-merge** — only properties that pass an explicit filter are taken
  from each source.
- **chain-derivation** — successive extraction of Pi without storing
  intermediates; only the terminal combination is materialized.
- **swap-and-test** — temporary exchange of roles (S_i ⇄ S_j or P_a ⇄ P_b),
  evaluate, keep or discard.
- **signature-audit-first** — run silent-error signature scan before any write.

`weighted-sum` is not a baseline: numeric weighting of abstract properties is
rarely grounded. Use it only when the user supplies actual assessable weights,
and record how each weight was determined.

New algorithms may be proposed only inside mode M1 or M5 and must be recorded
as an explicit design rationale with provenance.

## P-chain construction (M3)

When mode M3 is active:

- Extract P1 (boundary-identity) from the designated source skill or from the
  invariant already present.
- Derive further P's by successive abstraction or specialization, per the
  depth rule above.
- Do **not** write intermediate P's to disk or to the final JSON unless the
  user explicitly requests the full chain.
- Emit only the final selected combination (or the observation set the user
  asked for).
- Turning individual source skills on or off, swapping their order, or changing
  influence settings is permitted and must be logged in the process record.

Any data source (not only skills) may be treated as an S-entity for property
extraction.

## Output contract

Default output is one valid JSON object following the mmss-principle-synthesis
envelope.

Required top-level keys when producing a combination:

- `meta` (skill, version, mode, algorithm, language, p1_source)
- `state` (task_outcome, validation, limitations)
- `SYNTHESIZED_MMSS_SYSTEM` or `COMBINATION_RESULT` containing the produced
  skill map or the selected vector scheme

When the user requests a new skill file, write a complete `SKILL.md`. Resolve
the target directory in this order: (1) a path the user explicitly names in the
current request, (2) the user's configured skills directory from the current
environment, (3) otherwise ask the user — never write to a hard-coded path.
Validate the written file's frontmatter after creation.

Human-readable explanations are localized according to the user's language.
JSON keys and stable identifiers remain English.

## Process on every invocation

1. Resolve language (parent rule).
2. Resolve primary mode (catalogue + auto-select rule).
3. If the mode requires clarification → block and ask.
4. Extract or confirm P1.
5. Execute the declared algorithm.
6. Run signature-audit on the result.
7. Emit the JSON (and optional new skill files, with resolved directory).
8. Record which intermediate entities were deliberately omitted.

## Constraints inherited from parent

All core rules of mmss-principle-synthesis remain in force. Especially:
preserve provenance, do not fabricate execution state, minimum sufficient
architecture, preserve unknowns, no silent replacement of contracts, no fixed
numeric metrics unless actually required by the task.

## References

- Parent skill: mmss-principle-synthesis
- Motivation for P1: genomic-coordinates (boundary-identity triple)
- This skill may load additional reference files from its own `references/`
  directory when such files are present.
