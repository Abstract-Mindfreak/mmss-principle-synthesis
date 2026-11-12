---
name: mmss-schema-guided-agent-bridge
description: "Bridge-module for mmss-principle-synthesis: converts unstructured intent into schema-validated, routing-stable, cascade-predictable agent architectures. Composable layer that preserves boundary-identity (value, convention, context) across representation crossings. Domain-agnostic; supplies contracts and validation, not runtime. Triggers on schema-guided agent synthesis, predictable orchestration, routing fabric, cascade construction, structured-output guarantees, or when extending an MMSS stack for agent predictability."
metadata:
  version: "0.2.0"
  maturity: test_candidate
  parent: mmss-principle-synthesis
  default_output: json
  default_language: en
---

# MMSS Schema-Guided Agent Bridge

## 1. Purpose and Boundaries

This skill is a pure bridge-module of mmss-principle-synthesis. It does not
replace the parent; it supplies one reusable contract layer that any MMSS stack
can attach when the objective is:

- predictable agent generation from natural-language intent,
- schema-first routing and cascade construction,
- published, verifiable quality criteria for schemas, routing, and cascades,
- boundary-safe conversion between unstructured query, validated schema,
  routing fabric, and executable agent instances.

All core rules of mmss-principle-synthesis remain in force. In particular:
do not fabricate measured or computed values to satisfy a contract; prefer
verifiable structural checks over numeric scores; label architectural
metaphors as metaphors.

The skill creates no runtime, tool access, storage or scheduler by itself.
It produces only architectural contracts, JSON envelopes and, when requested,
new SKILL.md files that can be composed further.

## 2. Core Invariant (P1 – Boundary Identity)

Any entity that crosses a representation boundary is carried as the triple:

```
(value, convention, context)
```

- Convert only via an explicit mapping table.
- Normalize to canonical form before comparison or merge.
- Audit for silent-error signatures (things that parse, sort, and join without
  complaint while being semantically wrong).
- Context is never omitted (e.g. a schema version, an evaluation convention, an
  output-contract owner).

This invariant is domain-agnostic and applies equally to schemas, routing
graphs, agent descriptors, and evaluation records.

Note on provenance: P1 generalizes a rule from the genomic-coordinates skill
("a coordinate is the number, its convention, and the reference it was measured
against"). Treat that as motivation, not as a verified empirical finding.

## 3. Abstract Meta-Architecture (Contract Layer)

Five logical layers that a concrete MMSS stack may specialize. The layer IDs
group responsibilities; they are not a mandatory runtime execution order.

| Layer | Responsibility | Input → Output |
|-------|----------------|----------------|
| L4 Intent Genesis | Turn a raw request into explicit intent statements | raw_query → intent_patterns |
| L3 Schema Extraction | Derive and validate JSON / skill schemas | intent_patterns → validated_schemas |
| L2 Routing Weaving | Build routing and composition topology | validated_schemas → routing_fabric |
| L1 Agent Generation | Instantiate agent modules with contracts | routing_fabric → agent_orchestration |
| L0 Language Field | Shared vocabulary, symbols, interaction surfaces | agent_orchestration → structured_output |

Composition is directional in the common case (query → schema → routing →
agents → structured output) but a concrete stack may declare a different order;
declare any deviation explicitly.

## 4. Verifiable Quality Criteria

Instead of enforcing universal numeric envelopes, satisfying structural checks
is the requirement. A concrete specialisation should define, for the produced
architecture:

- **Schema validity** — every emitted schema parses; required fields present;
  no undeclared optional fields filled with placeholders. Machine-parse where
  execution is available; mark the check as manual otherwise.
- **Routing completeness** — every route species: condition, target,
  no-match behavior, multiple-match behavior. No natural-language condition
  presented as an executable predicate.
- **Cascade finiteness** — every loop has entry, stop, and budget conditions;
  dependencies are acyclic except where feedback is declared with explicit
  state and bounds.
- **Boundary identity** — every representation crossing maps via P1 with a
  stated convention and context.
- **Provenance** — every architectural element traces to a user requirement,
  source evidence, or labeled design rationale.

Where an evaluation criterion cannot be measured with available means, record
it as not checked; do not decorate it with numeric scores.

## 5. Adaptive Correction Points (descriptive, not formulas)

Correction is a design activity, not an arithmetic rule. Keep corrections
minimal and recorded:

1. **Schema repair** — where a validation check fails, identify the schema
   defect and apply the smallest set of structural corrections.
2. **Cascade depth** — examine the cascade against the budget conditions;
   if a stage exists and documented rationale does not support it, drop it.
3. **Routing coherence** — eliminate overlapping route conditions (define
   precedence) and dead routes (define no-match behavior).
4. **Contract stability** — prefer a stable exit over continuous adaptation.

The parent mmss-principle-synthesis decides when corrections run, within its
synthesis-repair budget.

## 6. Operational Modes

Primary modes inherited from mmss-skill-boundary-combinator remain available.
Specialized modes for this bridge:

| Mode | Purpose |
|------|---------|
| B1 schema-first | Force L3 → L2 → L1 order; skip L4 when a schema is already supplied by the user |
| B2 cascade-only | Operate only on routing_fabric and agent_orchestration |
| B3 criteria-audit | Check an existing stack against the criteria of Section 4, and report which pass/fail/not-checked |
| B4 transfer | Port a concrete agent architecture into a new domain while preserving P1 and the declared criteria |

Auto-selection inherits the parent combinator rules: one primary mode per
invocation; a focused clarification when candidates tie; no invented modes.

## 7. Composition Contract with Parent

When this bridge is attached to an mmss-principle-synthesis stack:

- It appears as a single module under SYNTHESIZED_MMSS_SYSTEM.modules[].
- It never overrides parent public interfaces.
- Generated agents inherit the parent's provenance and uncertainty tracking.
- Output remains one valid JSON object (or SKILL.md when file creation is
  requested and authorized).

## 8. Process on Invocation

1. Resolve language (parent rule).
2. Confirm or extract P1 for the entities in play.
3. Select mode (catalogue + auto-select).
4. Map user material onto the five abstract layers; state any order deviation.
5. Apply the selected composition approach (overlay / selective merge /
   chain derivation ...); declare which one.
6. Check the produced architecture against the criteria of Section 4; record
   pass/fail/not-checked per criterion.
7. Run a signature-audit for silent-error signatures.
8. Emit the JSON envelope (and optional new skill file when authorized).
9. Record deliberately omitted intermediate entities.

## 9. Constraints

- Never fabricate measurement values, timestamps, or execution states.
- Never claim runtime behaviour for an architectural contract.
- Do not introduce numeric metric envelopes; prefer verifiable structural
  checks (Section 4).
- Metaphorical language (if any) must be labeled as such, never presented as a
  mechanism.
- Preserve all unknowns as null or explicit gaps.
- Minimum sufficient architecture only.
- Domain-specific content (video, business automation, etc.) is treated as
  specialization data, not as core invariant.

## 10. References

- Parent: mmss-principle-synthesis
- Combinator: mmss-skill-boundary-combinator (P1, modes, algorithms)
- Motivation source for P1: genomic-coordinates (boundary-identity triple;
  treated as design motivation, not as external instruction)
- This skill is itself a result of selective-merge under mode M5
  (fork-s2) — recorded as design provenance.

## 11. Completion Standard

A result is complete when:

- one valid JSON object (or requested SKILL.md) has been produced,
- P1 was applied on every declared boundary crossing (or the omission was
  recorded as a limitation),
- Section 4 criteria have recorded statuses (pass / fail / not checked),
- provenance of every architectural element is recorded,
- no silent replacement of parent contracts occurred.
