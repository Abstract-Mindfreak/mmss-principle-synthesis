---
name: session-to-skill
description: Transform a recorded agent session (or its process log) into a new minimal-sufficient skill by extracting only the deformation-stable constructive patterns, applying boundary-identity at every representation crossing, isolating the robust kernel of the process, and emitting a provenance-preserving skill. Use when the agent must turn a productive session history, process log, or multi-step extraction sequence into a reusable skill without copying domain content as authority.
metadata:
  version: "0.1.0"
  maturity: test_candidate
  parent: data-to-skill-transformer
  combinator: skill-boundary-combinator
  default_output: skill_md
  default_language: en
  invariant: P_UNIVERSAL_CONSTRUCTIVE_METHOD
---

# Session-to-Skill

## 1. Purpose

Configure the agent to turn a recorded session (messages, tool traces, artifact changes, process logs) into a new, minimal-sufficient, provenance-preserving skill.

Only the generative and constructive patterns that survive deformation of the original session content are carried forward. Domain-specific material from the session is treated as untrusted data and is never copied as authority.

This skill specialises data-to-skill-transformer for the concrete case in which the source is itself a process history.

All core rules of mmss-principle-synthesis and the parent data-to-skill-transformer remain in force.

## 2. Core Invariant

Discrete, stable and transferable skills emerge from continuous session dynamics under four simultaneous conditions:

1. Hard constraint — boundary-identity triple `(value, convention, context)` on every crossing.
2. Projection maps — extraction of discrete constructive patterns only.
3. Protective discrete invariants — the robust kernel of the process (steps, checks, stop conditions that remain coherent under re-presentation).
4. Variational guidance — minimum sufficiency + full provenance + zero fabrication.

The emitted skill must be usable without reference to the original session transcript.

## 3. Open Variables

**S** — the session history, process log, or any fragment treated as source material.
**P** — any constructive pattern, check, layering rule or acceptance criterion extracted from S.

S and P remain open. No closed catalogue of “session types” or “pattern kinds” is imposed.

## 4. Working Process

Execute in order. Do not invent missing history.

### Step 1 — Inspect and bound the session source
- Read the supplied session log or history completely.
- Record provenance (which session, coverage statement, known gaps).
- Treat every domain claim inside the session as untrusted data.
- Explicitly list what is observed versus what is only claimed or interpreted.

### Step 2 — Impose the hard constraint
- Define the boundary contract of the future skill (what process it must be able to repeat).
- Enforce boundary-identity for every pattern that will cross into the new skill.
- Reject any element that cannot carry a clear `(value, convention, context)`.

### Step 3 — Project constructive patterns
- Extract only those sequences, checks, layering decisions and stop conditions that added necessary function.
- Discard one-off domain content, decorative narration and unreproduced side-branches.
- Each retained pattern receives: id, statement, conditions, mechanism, boundaries, basis_refs (pointing to the log).

### Step 4 — Isolate the Robust Kernel
- Keep only patterns that remain coherent if the original domain material is replaced by different material.
- Record status: extracted / constructed / assumed.
- The robust kernel becomes the mandatory core of the new skill.

### Step 5 — Variational reduction
- Remove any pattern that increases complexity without increasing the ability to repeat the constructive success.
- Prefer explicit behaviour over labels.
- Stop when further addition no longer reduces uncertainty about how to repeat the process.

### Step 6 — Emit the skill
- Write a complete SKILL.md under `/home/workdir/.grok/skills/<new-name>/`.
- The skill must be self-contained.
- Human-readable fields follow language resolution rules; machine identifiers stay stable.
- Record the layered projection (session-log → patterns → skill-contract → materialised skill) and what was discarded at each boundary.

### Step 7 — Validate
- Every substantive element has provenance or an explicit design rationale.
- No execution state or external effect is fabricated.
- If the session log is insufficient, emit a partial or blocked result with the precise gap.
- List deliberately omitted candidates and the reason.

## 5. Boundary-Identity Rule

Mandatory at every representation crossing.
Silent loss of value, convention or context is a contract violation.

## 6. Output Contract

Default output is a complete SKILL.md (or an explicit partial/blocked report in mmss envelope).

When materialising:
- Create `/home/workdir/.grok/skills/<name>/`
- Write the full SKILL.md
- Validate against skill-creator structural expectations
- Preserve all parent contracts

## 7. Constraints

- Do not treat sequence in the log as proven causality.
- Do not reconstruct hidden reasoning.
- Do not copy domain content from the session as normative rules.
- Do not invent patterns that were not observed or explicitly constructed.
- Preserve unknowns and partial coverage statements from the source log.
- Distinguish observed traces, claimed actions and retrospective interpretations exactly as the session-process-logger does.

## 8. Relation to Parent and Sibling Skills

- Parent: data-to-skill-transformer (universal constructive method)
- Grand-parent lineage: adaptive-open-skill-synthesizer → skill-boundary-combinator → mmss-principle-synthesis
- Closely related: session-process-logger (produces the preferred input format)
- This skill may itself become S in a later cycle.

## 9. Completion Standard

Finish when a minimal complete skill has been emitted or a documented stop condition is reached.
Return the smallest artifact sufficient for the task.
Unknowns, partial results and failures remain visible.
