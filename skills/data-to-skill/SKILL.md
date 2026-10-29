---
name: data-to-skill
description: Transform arbitrary inspectable data, specifications, corpora or prior artifacts into provenance-preserving, minimal-sufficient skills under open S and P variables. Applies selective principle extraction, boundary-identity at every representation crossing, layered projection with explicit information-loss accounting, robust-kernel isolation, and a variational minimality criterion. Use when the agent must turn raw or structured material into a reusable skill without closed entity catalogues or fabricated mechanisms. Triggers include data to skill, turn this into a skill, synthesize skill from source, materialize skill from principles, provenance-preserving skill builder.
metadata:
  version: "0.1.0"
  maturity: test_candidate
  parent: adaptive-open-skill-synthesizer
  combinator: skill-boundary-combinator
  default_output: json
  default_language: en
---

# Data-to-Skill

## 1. Purpose

Configure the agent to transform any inspectable source material into a minimal-sufficient, provenance-preserving skill.

The skill supplies a repeatable construction process, not a catalogue of finished skills.
It extends adaptive-open-skill-synthesizer and skill-boundary-combinator while preserving every core rule of mmss-principle-synthesis: provenance, epistemic distinctions, minimum sufficient architecture, preservation of unknowns, no fabrication of execution state, and the boundary-identity invariant.

S and P remain fully open. A source file, a principle set, a prior skill, a conversation fragment, or the transformation process itself may occupy any position.

## 2. Open Variables

**S** — any participating entity treated as source material, intermediate principle set, skill candidate, or the ongoing transformation process.

**P** — any isolatable or constructible property (mechanism, contract, invariant, filter, acceptance criterion) that can shape the resulting skill.

Indices mark generation, lineage or role only when useful; they are never locked.

Any proposed P remains an assumption until successful use elevates its status.

## 3. Core Invariant (P1)

Any entity that crosses a representation boundary must be carried as the triple
`(value, convention, context)`.

- Convert only via explicit mapping.
- Normalize to a canonical form before comparison or merge.
- Audit for silent-error signatures.
- Context is never omitted.

This invariant is domain-agnostic and mandatory at every step of the data-to-skill pipeline.

## 4. Activation and Mode Resolution

On every activation:

1. Resolve language according to the parent rule (explicit instruction > language of the user request > English).
2. Determine whether a concrete source and target skill direction are named or left open.
3. If open, apply auto-select / vector-scheme inherited from skill-boundary-combinator:
   - scan request and recent context for signals of needed capability;
   - rank candidate approaches;
   - activate the strongest match or generate a fresh mode when none fits;
   - state the chosen approach before synthesis begins.
4. If several approaches are close, emit one focused clarification and set task_outcome to blocked.
5. Never freeze a closed catalogue of source kinds, principle kinds or skill templates.

## 5. Working Process

Treat the following as an open procedure, not a fixed checklist.

### STEP_1 — Source as S
Treat the supplied material as an open S-entity.
Record its value, original convention and the context of the current transformation task.
Do not presuppose what counts as “data”, “principle” or “skill”.

### STEP_2 — Selective P Extraction
Isolate only those mechanisms that:
- possess operational meaning,
- survive reasonable deformations of the source,
- can serve as a contract or behavioural rule.

Every extracted P receives:
- id
- statement
- conditions
- mechanism
- expected_outcomes
- boundaries
- basis_refs

Discard decorative labels, numerology and claims without mechanism.

### STEP_3 — Boundary Crossing
At every representation change (raw → principles → skill contract → SKILL.md → claimed behaviour) enforce the boundary-identity triple.
Perform a silent-error signature audit before any write.

### STEP_4 — Layered Projection
Maintain the minimal layer stack:

- L0_raw
- L1_principles
- L2_skill_contract
- L3_materialized_skill

Each layer is a lossy projection of the previous one.
Explicitly record what is preserved and what is discarded at each boundary.

### STEP_5 — Robust Kernel
Identify the subset of P that remains invariant under small deformations of the source.
This robust kernel becomes the mandatory core of the future skill; everything else is optional extension.

### STEP_6 — Variational Criterion
Accept a candidate skill when adding any further element no longer reduces behavioural uncertainty while preserving provenance and minimality.
This is the operational analogue of a variational principle.

### STEP_7 — Open Feedback
The newly materialised skill may itself become an S for a subsequent cycle.
The construction method remains open and may be transformed by newly discovered P.

## 6. Combination Operations

Declare the interaction mode. Baseline operations include:

- selective extraction of P under an emerging filter
- overlay of boundary-identity onto any intermediate representation
- role exchange between source fragment and candidate skill
- feedback of a completed skill as new material (↺)
- generation of a fresh mode from a successful vector-scheme

New operations may be introduced when they serve the current objective; record provenance and design rationale.

## 7. Output and Materialization

Default output is one valid JSON object following the mmss-principle-synthesis envelope, localised for human-readable fields according to the user’s language.

When a new skill is materialised:

1. Write a complete SKILL.md under `/home/workdir/.grok/skills/<new-name>/`.
2. Validate structural compliance with the skill format.
3. Record the write operation and its status in the JSON state.
4. Preserve parent contracts; do not silently replace public interfaces or identifiers.

Minimum sufficient checks:
- provenance of every substantive element,
- status of assumptions,
- absence of fabricated execution claims,
- presence of boundary-identity at every recorded crossing.

## 8. Module Contract (internal)

**id**: data-to-skill-transform
**version**: 0.1.0

**inputs**:
- source_material (any_inspectable, required)
- target_domain (string, optional, default “skill_creation”)
- language_override (string, optional)

**outputs**:
- skill_seed (mmss-compatible principles or module)
- robust_kernel (array of principles)
- materialized_path (string or null)

**preconditions**:
- source is accessible for inspection
- no requirement for closed entity catalogues

**behavior**:
Execute STEP_1 through STEP_7.
Stop early with a blocked or partial result when mandatory material is missing or clarification is required.

**postconditions**:
- every element of the skill_seed carries provenance
- boundary-identity is recorded for every representation crossing
- robust_kernel contains only deformation-stable principles

**failure_modes**:
- source unavailable or empty → blocked + clarification_questions
- no operational mechanism isolatable → partial diagnostic, never fabricate
- boundary-identity violation detected → repair within budget or fail

**fallback**:
Return a diagnostic object with exact gaps instead of an empty or invented skill.

## 9. Constraints

- Do not pre-limit the process by closed lists of source kinds, principle kinds, roles, levels or algorithms.
- Do not introduce fixed numeric metrics unless required by the emerging construction.
- Do not present proposed mechanisms as already-implemented runtime.
- Do not claim exclusivity of the generative path.
- Tables or examples illustrate possibilities only.
- Never invent skill names, mechanisms or provenance records.

## 10. Relation to Parent and Sibling Skills

- Parent: adaptive-open-skill-synthesizer (open S/P discovery and materialization).
- Combinator lineage: skill-boundary-combinator (auto-select, vector-scheme, boundary-identity).
- Format authority: skill-creator conventions for SKILL.md structure.
- Foundation: mmss-principle-synthesis (envelope, provenance, epistemic rules).
- Sibling modules remain available; this skill does not supersede them.

The data-to-skill skill itself may later become an S transformed by a newly discovered P.

## 11. Completion Standard

Finish when the requested scope is satisfied or a documented stop condition occurs.
Return the smallest complete artifact sufficient for the task.
Preserve unknowns, partial results and failures as visible states.
