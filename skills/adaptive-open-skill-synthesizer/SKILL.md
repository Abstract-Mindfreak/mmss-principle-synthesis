---
name: adaptive-open-skill-synthesizer
description: "Adaptive discovery and materialization of new skills under open S and P variables, without fixed catalogues of entities, roles, or algorithms. Use when the agent must invent, reshape, or combine skills from productive findings, auto-select search strategies, generate new modes, or extend MMSS stacks by open combinatory synthesis that preserves parent contracts and boundary identity. Triggers include adaptive skill creation, open skill synthesis, invent new skill from findings, generate skill mode, transform skill, combinator, exploratory skill materialization."
metadata:
  version: "0.2.0"
  maturity: test_candidate
  parent: mmss-adaptive-sp-combinator
  default_output: json
  default_language: en
---

# Adaptive Open Skill Synthesizer

## 1. Purpose

Configure the agent to perform adaptive discovery, transformation, and
materialization of new skills (as S-entities) and their properties (P) under
open variables.

The skill supplies the working process for inventing or reshaping skills from
productive findings rather than from closed lists of templates.

It extends mmss-adaptive-sp-combinator and preserves all parent contracts of
mmss-principle-synthesis: provenance, epistemic distinctions, minimum
sufficient architecture, preservation of unknowns, no fabrication of execution
state, boundary-identity invariant.

S and P remain open. A skill, a mode, a format contract, or the ongoing
synthesis process itself may occupy any position.

## 2. Open Variables

**S** — any participating entity treated as a skill-candidate, skill-fragment,
mode, combinator, or the process of skill creation itself.

**P** — any isolatable or constructible property that can transform skill
structure, trigger conditions, format contracts, or combination methods.

Indices mark generation, lineage, or role only when useful; they are never
locked. Any proposed P stays an assumption until successful use elevates it.

## 3. Notation

Use the parent's baseline symbols only when they aid a concrete step:
↝ emergence; ⊕ open combination; ▷ influence; ⇄ role exchange; ↺ feedback;
? open position. Symbols never replace substantive action; do not use them
decoratively. New symbols must be briefly defined at first use.

## 4. Activation and Mode Resolution

On every activation:

1. Resolve language (user request > English).
2. Determine whether a concrete skill direction is named or left open.
3. If open, apply auto-select:
   - scan request and context for signals of needed capability;
   - rank candidate approaches, including previously productive ones;
   - activate the strongest match or generate a fresh approach when none fits;
   - state the chosen approach before synthesis begins.
4. If several approaches are close, emit one focused clarification and set
   task_outcome to blocked.
5. Never freeze a closed catalogue of skill kinds or modes.

## 5. Working Process

- Decide which existing skills or external sources to treat as S.
- Isolate candidate P (format contracts, trigger patterns, invariants,
  combination methods).
- Join or transform under an explicitly declared interaction mode.
- Findings may redirect the branch, provided they do not override an explicit
  user mandate.
- Materialize only when a minimum-sufficient skill (name, description, core
  process, constraints) has coherent provenance: every substantive element
  traces to an observation, a user requirement, or a labeled design rationale.
- Feed the new skill back as S material for further adaptive cycles when
  requested.

A permissible exploratory move: sketch a possible result first, then construct
the connections that realize it. Deviation from the sketch may reveal a more
interesting combination; allow the finding to redirect the branch. This is
never a claim that the sketch was "calculated".

## 6. Materialization Target

When a new skill is written, resolve the target directory in this order:
(1) a path the user explicitly names in the current request, (2) the user's
configured skills directory from the current environment, (3) otherwise ask —
never write to a hard-coded path.

The SKILL.md must include, at minimum: frontmatter with name, description, and
version; a purpose section; a working-process section; explicit constraints;
and a stopping/completion condition. If a separate skill supplies the canonical
SKILL.md format rules in the current environment, follow it and say so.

## 7. Output and Integration

Default output is one valid JSON object following the mmss-principle-synthesis
envelope, localized for human-readable fields according to the user's
language.

When a new skill is materialized, write the complete SKILL.md (per Section 6)
and record the write — including the resolved path — in the JSON state.

Preserve parent contracts; do not silently replace public interfaces or
identifiers.

Minimum sufficient checks: provenance of substantive elements, status of
assumptions, absence of fabricated execution claims.

## 8. Constraints

- Do not pre-limit the process by closed lists of skill kinds, roles, levels,
  sources, or algorithms.
- Do not introduce fixed numeric metrics unless the emerging construction
  requires them.
- Do not present proposed mechanisms as already-implemented runtime.
- Do not claim exclusivity of the generative path.
- Do not materialize a skill merely because synthesis is possible; materialize
  when the working process of Section 5 has produced coherent, traceable
  substance.
- Tables or examples illustrate possibilities only.

## 9. Relation to Parent and Sibling Skills

- Parent: mmss-adaptive-sp-combinator (open S/P discovery and combination).
- Grandparent contract: mmss-principle-synthesis (envelope, epistemics).
- Format authority: skill-creator, where present in the environment.
- Sibling modules remain available; this skill does not supersede them.

This skill itself may later become an S transformed by a newly discovered P.
