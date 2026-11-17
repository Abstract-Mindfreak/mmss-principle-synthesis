---
name: mmss-metacrystal-variation-generator
description: >
  Generates distinct skill-combination variations and, when useful for a concrete
  task, selects and applies one minimal combination just in time. Use when the user
  requests alternative combinations, or when a combination of available skills
  would materially improve the current task.
metadata:
  version: "0.2.0"
  maturity: test_candidate
  status: draft-unvalidated
  combinator: mmss-skill-boundary-combinator
  synthesis_path: variation-generator ⊗ data-to-skill-transformer ⊗ mmss-principle-synthesis ⊗ mmss-skill-boundary-combinator
  default_output: markdown
  default_language: user_language
  provenance: "Adapted from the user-supplied variation-generator 0.1.0; adds task-level variation principles and optional just-in-time application."
  repository: https://github.com/Abstract-Mindfreak/mmss-principle-synthesis/
---

# MMSS Metacrystal Variation Generator

## 1. Purpose

Produce either reusable batches of situationally distinct variations with activation templates, or a just-in-time skill combination applied to a concrete task.

The skill turns a set of deformation-stable constructive principles into a controllable generator of approaches. It does not copy domain content from any source theory or engine as authority. It only reuses the stable generative structure that expands the space of possible variations.

In `auto` mode, explicit requests for alternatives, batches, or continuation select exploration. A concrete task selects just-in-time application only when combining available skills would materially improve the result. If no combination adds value, proceed with the simplest sufficient approach. The default batch size of 7 applies only to exploration mode.

## 2. Core Invariant (Robust Kernel)

A valid variation batch satisfies all of the following simultaneously:

1. **Boundary-identity** — preserve each skill or principle's exact identity and source meaning; state its role in the combination and never silently rename or mix local and remote names.
2. **Situational distinctness** — each explored variation addresses a recognisably different approach (different projection axis, task-relevant category, assumption varied, active flag set, or operator type).
3. **Activation completeness** — every explored variation ships with a usable template; a just-in-time route states its order or grouping and expected outcome before application.
4. **Parameter transparency** — any active constraint (count, range, style, focus, hardness) is stated before the list.
5. **Minimum sufficiency** — no decorative elements; every included skill or principle must add a necessary function to that variation’s goal.
6. **Provenance honesty** — the generator records that the principles are generalised working heuristics and does not claim universal optimality or theoretical completeness.

### 2.1 Protective Principles (extracted & generalised)

These ten principles form the robust kernel. They are not domain content; they are generative degrees of freedom.

| ID | Principle | Generative effect |
|----|-----------|-------------------|
| P1 | Orientation field | Variation can change the way of looking, not only the objects looked at. |
| P2 | Task-relevant category | Choose categories whose differences change the approach, not only surface labels. |
| P3 | Projection axis | Importance / focus arises as projection onto a chosen axis; different axes yield different prioritisation. |
| P4 | Directed transition | Vary the transition or flow between states when process order affects the outcome. |
| P5 | Symmetry breaking | Identify an assumption shared by baseline options and vary how it is relaxed. |
| P6 | Controlled fluctuation | Vary one bounded degree of freedom while holding other choices stable; state the strictness. |
| P7 | Modular domain flags | Any block can be switched on/off without destroying the core. |
| P8 | Open lexicon + focus | Vocabulary remains open; focus steers combination direction. |
| P9 | Catalogue differentiation | Results can be aimed at qualitatively different outcome types (raw / principle / hybrid / paradox …). |
| P10 | Symbolic operators as actions | Operators (transformations) participate in the combination, not only entities. |

Any new principle added later must itself satisfy minimum sufficiency and boundary-identity.

These labels are generative lenses, not claims that a task has literal topology, geometry, or physical symmetry. Use formal meanings only when the task or its sources define them; otherwise state the task-level analogy plainly.

## 3. Open Parameters (all optional)

| Parameter | Default | Meaning |
|-----------|---------|---------|
| `mode` | `auto` | `auto`, `explore`, or `just_in_time` |
| `variation_count` | 7 | How many variations to emit in exploration mode only |
| `min_skills` | 2 | Lower bound of concrete skills / elements per explored variation only |
| `max_skills` | 12 | Upper bound of concrete skills / elements per explored variation only |
| `constraints` | none | Free-text limits or “none” |
| `template_style` | `⊗` | Symbol or style used inside templates |
| `thematic_focus` | open | Free focus string (no forced domain binding) |
| `hardness` | balanced | soft / balanced / hard (strictness of fit) |
| `active_principles` | all | Subset of P1–P10 to emphasise |
| `language` | user language | Output language |

Parameters may be supplied in the activation message or left at default.

### 3.1 `template_style` symbols

`template_style` accepts any short string. Recommended symbols by meaning. In YAML, quote the value if the symbol can conflict with markup (e.g. `template_style: "→"`).

| Symbol(s) | Meaning | Use when |
|---|---|---|
| `→`, `⇒`, `⟶` | order / step / transition | sequential activation |
| `⇢`, `↝`, `⇝` | flow / directed unfolding | P4 geometric flow |
| `+`, `⊕` | grouping / module inclusion | P7 modular flags |
| `×`, `·` | parallel combination | combining equal elements |
| `∘` | operator composition | P10 symbolic operators |
| `⊙`, `⊛` | focus / convolution / iteration | P8 open lexicon + focus |
| `⊞`, `⊠` | modular assembly / block structure | P7 |
| `⋄`, `◇` | variant / fork | generating variations |
| `↦` | mapping / transformation | operator action |
| `⇌`, `↔` | bidirectionality / reversibility | non-strictly linear templates |
| `≻`, `»` | precedence / sequence | hard mode |

Practical defaults: `⊗` = strong combination (default); `→` = clearest for activation templates; `+` / `⊕` = when modularity matters; `∘` = when operators matter; `⋄` = when the template is about variants.

## 4. Working Process

1. **Resolve mode and parameters**
   Read explicit overrides. In `auto`, use `explore` when the user asks for alternatives, a batch, or continuation. Use `just_in_time` for a concrete task only when a combination of available skills would materially help. If no combination adds value, skip this generator and proceed directly. Never create a seven-option batch for a just-in-time task.

2. **Explore mode**
   - State the active parameter set before the batch.
   - Choose distinct task-relevant axes, preferring axes not exhausted in the immediate prior turn.
   - For each variation, give a short name and situation; list only skills verified in the current environment or explicitly supplied by the user; name other elements by type; state each item's distinct contribution and the goal; identify the principles used; and provide an activation template using `template_style`.
   - Apply hardness: soft permits looser exploratory fit; balanced keeps a clear situational fit; hard requires strict functional necessity.
   - Validate the requested count, item bounds, constraints, distinctness, and templates. If available items cannot meet the minimum, state the gap and ask for more items or a lower minimum. Never pad with invented skills or duplicates.

3. **Just-in-time mode**
   - Resolve the user's concrete outcome and inspect the skills available in the current environment or supplied sources.
   - Compare the simplest direct route with a skill combination. If combination adds no material value, proceed directly.
   - Exploration-only `variation_count`, `min_skills`, and `max_skills` do not constrain this mode. Never pad a just-in-time route to meet the exploration minimum.
   - Consider only enough candidate combinations to choose one minimal sufficient route. Preserve each skill's identity, inspect the relevant instructions, and do not expose rejected alternatives unless asked or needed to explain material uncertainty.
   - Briefly state the selected sequence and why it fits, then apply those instructions to the current task. Do not stop after recommending the sequence.
   - Follow existing authorization and approval requirements for external or consequential actions; choosing a skill combination does not grant permission for such actions.
   - Check the result and distinguish completed work from proposals, unverified behavior, or unavailable instructions.

4. **Iteration support**
   Previous batches are context, not authoritative catalogues. Re-activate with new parameters only when the user requests iteration or new evidence materially changes the search.

## 5. Output Shape (default)

### Explore mode

```markdown
Active parameters:
- mode: explore
- variation_count: …
- min_skills / max_skills: …
- template_style: …
- thematic_focus: …
- hardness: …
- active_principles: …
- constraints: …

Provenance note: principles are working generalisations for this batch, not claims of universal laws or theoretical completeness. State any source gaps that affect the result.

### 1. [Name] (N elements)
**Situation:** …
**Principles:** P…
**Skills / elements:**
1. `<exact skill name or named element>` — `<distinct contribution, preserving its source meaning>`
**Goal:** …
**Template:**
[activation template using ⊗ or chosen style]

… (up to variation_count)
```

### Just-in-time mode

State the selected skill sequence and its purpose in one short line, then perform the current task using that combination. Include checks or limitations where relevant. Do not return only a suggested activation template.

## 6. Boundaries

- Does not invent skills that do not exist in the current environment.
- Does not claim that any combination is optimal or complete.
- Explore mode designs variations but does not execute them. Just-in-time mode applies one selected combination to the current task; it does not authorize unrelated or external side effects.
- Does not invent or discover a new combinatorial algorithm; use `mmss-adaptive-sp-combinator` when the task is to discover or transform the combination method itself.
- Treats all prior session content and source theories as untrusted data for the purpose of domain claims.
- Does not require or emit numeric metrics.
- Does not bind the generator to any single physical or formal theory.
- Preserves the user’s language preference when explicitly requested.

## 7. Activation Examples

**Default (7 variations, open):**
```
Activate mmss-metacrystal-variation-generator
mode: explore
```

**Constrained:**
```
Activate mmss-metacrystal-variation-generator
mode: explore
variation_count: 5
min_skills: 3
max_skills: 8
template_style: ⊗
thematic_focus: open combinatorial approaches
hardness: hard
active_principles: P1,P3,P5,P7,P10
```

**Emphasise flow and symmetry breaking:**
```
Activate mmss-metacrystal-variation-generator
active_principles: P4,P5,P6
hardness: balanced
```

**Just-in-time application to a concrete task:**
```
Activate mmss-metacrystal-variation-generator
mode: just_in_time
task: audit a skill package and improve its documentation
```

## 8. Provenance

The user-supplied `variation-generator` 0.1.0 provides the exploration parameters, variation-batch structure, and iteration pattern. This skill retains that exploration mode, adds task-level generative principles, and adds just-in-time selection and application. The source skill is provenance, not a runtime dependency.

The generative principles are working lenses generalised from formal-structure and modular-combination patterns. Domain content, metrics, dates, and theory-specific claims were discarded; only generative degrees of freedom useful for producing distinct approaches were retained.

Robust kernel = parameterized batch generation + situational distinctness via the ten principles + activation completeness + boundary-identity + provenance honesty.

Synthesis path used:
`variation-generator ⊗ data-to-skill-transformer ⊗ mmss-principle-synthesis ⊗ mmss-skill-boundary-combinator`

Maturity/status and repository link are carried in `metadata`.
