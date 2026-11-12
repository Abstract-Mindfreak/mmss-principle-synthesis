---
name: mmss-adaptive-sp-combinator
description: "Adaptive discovery, transformation, and combination of skills, systems, properties, and of the combination methods themselves, under open S and P variables. Use when the agent must find, reshape, or invent combinations without fixed entity lists, role catalogues, or algorithm menus; when auto-select should choose or generate the search approach; when new modes must be born from productive findings; or when mmss-principle-synthesis needs an open combinatory layer that preserves parent contracts. Triggers include: adaptive combination, open S P, discover approaches, generate new mode, transform combination method, auto-select search strategy, vector-scheme reactivation, exploratory skill synthesis."
metadata:
  version: "0.2.0"
  maturity: test_candidate
  parent: mmss-principle-synthesis
  combinator: mmss-skill-boundary-combinator
  default_output: json
  default_language: en
---

# Adaptive SP Combinator

## 1. Purpose

Configure the agent to perform adaptive discovery, transformation, and
combination of participating entities (S) and their properties (P), including
the methods of combination themselves.

The skill supplies the working process, not a finished catalogue of results.
It extends mmss-principle-synthesis without silent replacement of the parent.
All core rules of the parent remain in force: provenance, epistemic
distinctions, minimum sufficient architecture, preservation of unknowns, no
fabrication of execution state.

S and P are open variables. Their current interpretation is stated when it aids
understanding; it is never locked as a permanent constraint.

## 2. Open Variables

**S** — whatever is treated, in the present construction, as a participating
entity or structure. A skill, a system, data, a prior result, a combination,
or the ongoing process itself may occupy an S position. No enumeration limits
the admissible substitutions.

**P** — a property that is isolated, hypothesized, or constructed from an S.
P may be presented as an abstract invariant and then used to transform another
S, another P, or the manner of their discovery and combination. P may remain a
potential, to be refined in interaction. A P of one S may alter another S so
that the latter surfaces new P from which new S arise — this is one example of
a possible relation, not a mandatory schema.

Indices on S and P may mark position, role, generation, linkage, or any other
organisation that emerges. Do not fix one meaning of indices across all cases;
clarify the current reading only when it helps.

Any proposed P remains an assumption until evidence or successful use elevates
its status. Assumptions are permitted for exploratory moves; their status as
assumptions must be kept visible.

## 3. Process Symbols

Baseline conventions (extensible; use only when they clarify a concrete move):

- ↝ — possible transition or emergence
- ⊕ — combine without predetermining the interaction mode
- ▷ — apply as influence, setting, or perspective
- ⇄ — exchange roles, direction, or mutual influence
- ↺ — feed a result back into the process as material
- ?  — leave a position open for discovery

Example: `(P₄ ⊕ P₁) ▷ S₂ ↝ S_new`. A new operator may be introduced when it
opens a useful move; state its current sense briefly. Symbols must never
replace substantive action with decorative notation.

## 4. Activation and Mode Resolution

On every activation:

1. Resolve language according to the parent rule (explicit instruction >
   language of the user request > English).
2. Determine whether the user has named a concrete direction or left the
   approach open.
3. If open, apply the auto-select / vector-scheme mechanism inherited from
   mmss-skill-boundary-combinator:
   - scan the current request and recent context for signals of intent;
   - rank candidate approaches (including previously productive
     vector-schemes);
   - activate the strongest match or generate a new approach when none fits;
   - state the chosen approach before synthesis begins.
4. If several approaches are close, emit one focused clarification and set
   task_outcome to blocked.
5. Never invent a closed catalogue of modes that freezes future discovery.

The search method itself may become a new P, a new S, or a new mode for
subsequent work. Roles are not permanently assigned: the obtained skill may
later transform the combinator.

## 5. Working Process

Treat the following as an ordered procedure with freely revisable choices —
not as an open-ended discourse.

1. **Frame**: state in one sentence what is being combined or discovered and
   for what purpose the user asked.
2. **Select S**: decide which entities participate and from where they come
   (user input, session findings, known skills, external sources).
3. **Isolate P**: for each relevant S, state candidate properties — with
   provenance (observed / inferred / hypothesized) visible.
4. **Declare combination**: state the interaction mode and (when used)
   algorithm, deferring to mmss-skill-boundary-combinator's catalogue where
   applicable.
5. **Execute**: perform the combination and record what emerged.
6. **Checkpoint**: state concretely (a) what was produced, (b) which parts
   rest on assumptions, (c) whether the user's objective advanced. The
   checkpoint ends the invocation's exploration loop by default.
7. **Continue (optional)**: only when a finding genuinely redirects the branch
   may a new loop start — and it follows steps 1–6 again. Infinite
   self-description loops are prohibited; each loop must state what new fact
   motivates it.

Additional rules:

- Variables of the search may change mid-process, including mid-loop.
- A productive finding may alter the intention of the current exploratory
  branch, provided it does not override an explicit mandatory task of the user.
- Full enumeration is never required; intermediate levels need not be
  materialized; no obligatory upper bound on chain depth is imposed.
- Permitted exploratory move: first sketch a possible result, then construct
  the connections that could lead to it. Deviation from the sketch may reveal a
  more interesting combination. This is not a claim of completed computation.

## 6. Combination Operations

Any operation must declare (or leave explicitly open) the interaction mode.
Baseline operations include, but are not limited to:

- overlay of a P onto an S
- selective joining of properties that satisfy an emerging filter
- role exchange (⇄) followed by evaluation
- feedback of a result as new material (↺)
- generation of a fresh mode from a successful vector-scheme

New operations may be proposed when they serve the current objective; record
provenance and design rationale.

Boundary-identity considerations (value, convention, context) are applied
whenever an entity crosses a representation boundary, following the invariant
carried from the combinator lineage. They do not constrain the openness of S
and P themselves.

## 7. Output and Integration with Parent

Default output is one valid JSON object following the
mmss-principle-synthesis envelope, localized for human-readable fields
according to the user's language.

When a new skill or a new mode is materialized, write a complete SKILL.md to a
directory resolved in this order: (1) a path the user explicitly names in the
current request, (2) the user's configured skills directory from the current
environment, (3) otherwise ask the user. Validate the written file.

Preserve parent contracts; do not silently replace public interfaces,
identifiers, or adopted axioms.

Minimum sufficient checks only: provenance of substantive elements, status of
assumptions, and absence of fabricated execution claims. Do not convert the
research process into an endless audit.

## 8. Constraints

- Do not pre-limit the process by closed lists of entity kinds, roles, levels,
  sources, algorithms, or scenarios.
- Do not introduce fixed numeric metrics or weights unless the user or the
  emerging construction requires them.
- Do not present proposed mechanisms as an already-implemented runtime.
- Do not claim that the result cannot be obtained by any other route;
  combination is the chosen generative path, not an exclusive necessity.
- Tables or examples that appear in responses illustrate possibilities; they
  never define the entire space of admissible combinations.
- One exploration loop ends at the checkpoint; do not open a new loop without
  a concrete new finding that motivates it.

## 9. Relation to Sibling Skills

- mmss-skill-boundary-combinator supplies the auto-select, vector-scheme, and
  mode-generation machinery used here.
- skill-quick-sampler may be invoked when a lightweight inventory of an
  external catalogue is useful.
- mmss-schema-guided-agent-bridge and other sibling modules remain available;
  this skill does not supersede them.

The mmss-adaptive-sp-combinator itself may later become an S that is transformed by
a newly discovered P.
