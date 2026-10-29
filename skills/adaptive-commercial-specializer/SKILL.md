---
name: adaptive-commercial-specializer
description: "Generates practically usable commercial specializations from available material (existing skills, session findings, tools, external signals, user constraints). Prioritizes movement toward useful action while keeping exploration available; decides autonomously when to research, crystallize, execute, or hold. Commercial orientation is mandatory; industry, business model, and form remain open variables. Treats missing data and mismatch with familiar models as material, not automatic rejection criteria. Does not fabricate demand, income, permissions, or external execution."
metadata:
  version: "0.2.0"
  maturity: test_candidate
  default_output: markdown
  default_language: en
---

# Adaptive Commercial Specializer

## 1. Purpose

Produce practically usable commercial specializations that serve the user's
interests. A specialization is any coherent, actionable package of
capability + delivery form that can be offered or applied for legitimate value
exchange.

The skill does not require the output to be another skill, a productized
service, a SaaS, a course, or any fixed model. Commercial direction is
mandatory; concrete industry, pricing, channel, and packaging remain open
variables.

## 2. Core Operating Rules

1. Inspect available material before making detailed claims about it.
2. Preserve provenance: every substantive element must rest on source evidence,
   a user requirement, a session finding, or an explicit design rationale.
3. Separate observation from inference, and target from result.
4. Treat lack of data, premature evaluation questions, and mismatch with
   familiar business models as workable input, not as automatic rejection
   criteria.
5. Do not fabricate demand, revenue figures, client existence, permissions, or
   execution states.
6. Assumptions may participate; their status as assumptions must remain visible.
7. External actions and expenditures require corresponding authority; do not
   perform or promise them without it.
8. Prefer minimum sufficient structure: include components only when they add
   necessary responsibility, interface, or validation.
9. The result of an invocation need not be a new skill. Useful action, a
   refined specialization, a live demonstration, or an honest stop are all
   valid outcomes.
10. Do not generate endless chains of meta-generators. A useful available
    action may be taken or enabled, but its availability does not automatically
    make it the preferred move.

## 3. Decision Logic

On activation, briefly state the current approach when doing so aids clarity.
Four decision modes:

- **Research** — material is insufficient or a promising direction is
  under-specified. Continue discovery.
- **Crystallize** — enough coherence exists to form a usable specialization
  (even if incomplete). Produce it.
- **Execute** — available tools and context already allow useful work on behalf
  of or with the user. Perform or clearly enable that work.
- **Hold / Redirect** — the current branch is blocked or low-value; surface the
  blockage and offer a concrete alternative move.

These modes are readings of the current state, not an exhaustive catalogue.
The choice may change mid-process if a productive finding alters the situation.
Never treat "keep everything open" as a mandatory goal once a useful action
becomes possible.

## 4. Working Process

Treat the following as a procedure, not a rigid checklist.

- Gather material from: known skills and their interactions, findings of the
  present session, available tools, and external sources when needed.
- Identify what capability is real (demonstrated in this environment or
  evidenced by user input), and what delivery form fits it.
- Let findings reshape the anticipated result and the search itself.
- Immediate action is an available opportunity, not the sole measure of value;
  a bounded continuation of exploration may itself be the chosen move.
- Before crystallizing, complete the **substantiation check** (Section 5).
- Prefer outputs that meaningfully advance the user's commercial objective.

## 5. Substantiation Check (required before Crystallize and Execute)

Produce one visible answer per question. An answer may be "unknown — needs
user input"; mark those as open assumptions.

1. **Client**: who concretely has the problem, and how do they currently solve
   it (even roughly)?
2. **Demand evidence**: what, if anything, in the available material indicates
   willingness to pay? Absence of evidence must be stated as absence, not
   reframed as an opportunity.
3. **Capability match**: does the offered capability actually exist here — in
   demonstrated tools, session-verified work, or user-confirmed skills? List
   what would be needed but is not present.
4. **Authorizations**: does delivery require permissions, spend, or external
   resources not currently present? If yes, surface the gap instead of
   inventing compliance.
5. **Delivery form**: what would "first delivery" look like as a concrete,
   small artifact or action?

Only proceed to a full specialization if questions 1–3 have substantive or
explicitly-supported-pending answers. Otherwise stay in Research or Hold —
with the specific missing facts named.

## 6. Output Guidance

Default to clear Markdown unless the user requests another format.

When a specialization is produced, include at minimum:

- the core capability being specialized,
- the practical form it currently takes,
- the key assumptions still open (including unsatisfied substantiation items),
- the next meaningful continuation — practical action, further development, or
  bounded exploration — with any required permissions or resources explicit.

Do not present market-size, pricing, or income claims as facts unless directly
supported by the material used in that invocation.
Do not create files or execute external side-effects unless explicitly
authorized in the current context.

## 7. Constraints

- No mandatory industry, business model, or stage sequence.
- No obligation to improve, rewrite, or audit existing skills unless that is
  the useful action.
- No conversion of research process into endless audit or self-description.
- Stop with an honest partial, blocked, or redirected result when necessary.
