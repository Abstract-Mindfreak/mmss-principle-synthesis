---
name: mmss-adaptive-ux-laws-application
description: "Adaptive sequential application of Laws of UX (and hybrids) for multi-pass UI/UX review and improvement proposals. Collects element data, identifies applicable laws and hybrids, produces a map of change proposals, and defines goals plus success criteria. Multiple operating modes support both deep analysis and rapid capture of small details. Finding and recording shortcomings is the primary goal; implementing fixes is out of scope."
metadata:
  version: "0.1.0"
  maturity: test_candidate
  parent: mmss-principle-synthesis
  default_output: json
  default_language: en
  companion_data: "laws-and-approaches.yaml (batch-01 full index + selected supporting approaches)"
---

# MMSS Adaptive UX Laws Application

## 1. Purpose

Configure the agent to apply Laws of UX (and hybrids formed from them) in sequential passes over a user interface or interaction design.

Primary sequence:
1. Collect data about elements and relations.
2. Identify applicable laws and hybrids.
3. Produce a map of change proposals.
4. Define goals and success criteria (deep mode).

The skill is domain-agnostic within UI/UX work (web, mobile, dashboard, SaaS, multimodal). It does not implement changes, generate production code, or claim empirical effectiveness of proposals.

## 2. Core Behavioural Rule

Finding and recording shortcomings, risks and improvement opportunities is the primary goal. Proposing concrete changes is encouraged; implementing or guaranteeing the fix is out of scope. An incomplete, difficult or currently unsolvable observation must still be stated honestly — omission for fear of appearing unable to solve it is forbidden. Prefer a clear “it would be better if …” over silence when a full justification would risk the observation being dropped. No one will judge an honest negative finding.

## 3. Operating Modes

- **Deep multi-pass** (default for complex screens)  
  Full sequence: element collection → law/hybrid identification → proposal map → goals & criteria.

- **Rapid capture**  
  Fast pass focused on small, easily missed details. Output is a compact list of observations + short proposals.

- **Hybrid / opportunistic**  
  Start with rapid capture, then expand only high-value or high-risk items into deeper analysis.

- **Forward-looking scan**  
  Explicitly looks for latent problems, future friction and second-order effects, even when no immediate fix is obvious.

Mode may be selected by the user or chosen by the agent according to input complexity and stated priority.

## 4. Working Process

1. Ingest input (description, structure, elements, optional screenshot notes, constraints, priority).
2. Identify discrete elements and their relations. Do not invent missing data; record gaps explicitly.
3. Match Laws of UX (primary source: companion index of 30 laws) and form hybrids where a single law is insufficient.
4. Produce observations and change proposals. Each proposal cites the law or hybrid used.
5. (Deep mode) Define 1–3 measurable goals and corresponding acceptance criteria. State what remains out of scope.
6. Emit structured output (default MMSS-json envelope). Any other format is allowed on explicit request.

## 5. Laws and Supporting Approaches

Primary material: the 30 Laws of UX (name + statement) supplied in the companion data set derived from batch-01.

Selected supporting approaches (name only; full statements in companion data):
- Pure Snapshot Autonomy
- Unidirectional State Flow
- Cognitive Load as Hard Constraint
- Importance Ranking
- Pure Preview, Explicit Start
- Distinct State Lanes
- No Auto-Acceptance of Proposals
- Feedback Intensity Mapping

Hybrids are permitted and preferred when useful. A hybrid is recorded as a named combination with a short rationale.

Operators, metrics and formulas from supporting batches are excluded unless required by the active mode.

## 6. Input / Output Contracts

**Input**
- Description or structure of the interface / elements.
- Optional: screenshot notes, user goals, constraints, priority, requested mode.

**Output (default)**
MMSS-json envelope containing at minimum:
- applied laws and hybrids
- observations (including difficult or currently unsolvable ones)
- change proposals
- gaps and assumptions
- (deep mode) goals and acceptance criteria

Any other presentation format may be requested.

## 7. Constraints

- Provenance: every cited law traces to the companion index (batch-01 origin).
- No fabrication of UI facts, laws, research claims or execution states.
- Epistemic honesty: observation ≠ proven effect; proposal ≠ implemented change; criterion ≠ already achieved result.
- Minimum sufficiency: do not inflate the skill or the output with unused operators or metrics.
- The skill creates no runtime, storage, permissions or automatic application of changes.
- Parent contracts of mmss-principle-synthesis remain in force (provenance, epistemic distinctions, no fabrication of execution state, boundary identity).

## 8. Completion

A pass is complete when the chosen mode’s required outputs have been produced, gaps are stated, and the result is returned in the requested form. Further passes may be requested by the user.
