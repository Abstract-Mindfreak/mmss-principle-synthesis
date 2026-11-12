---
name: animated-svg-icon-composer
description: >-
  Compose a self-contained animated SVG icon for any object, concept, tool,
  service, idea, or skill — not necessarily MMSS. Works from a semantic skeleton
  of the target (what it is, what acts, what changes, what it emits) or from a
  property, relation, or state when no process exists. Renders that reading as
  a readable motion metaphor. Accepts open input parameters (topic, purpose,
  palette, style, shape, background, size, intensity, references). Emits one
  standalone SVG, a brief idea description, an optional element→meaning map, a
  README embedding example, and an honest account of what was verified versus
  proposed. Primary target environment is a GitHub README image; the skill is
  honest about what works there and what is uncertain. CSS, SMIL, or both are
  acceptable depending on the motion. No external resources, no JavaScript, no
  fixed palette, no fixed archetype library, no RAG/CAG infrastructure.
metadata:
  version: "1.1.0"
  maturity: working_tool
  scope: universal
  portable: true
  default_output: standalone_svg
  default_language: user_language
---

# Animated SVG Icon Composer

## 1. Purpose

Compose a self-contained animated SVG icon that conveys the **character** of
the target through **form and motion**, not just its name.

Targets can be anything substantive: an application, an interface function,
a project, a repository, a library, a tool, a service, a process, a
scientific idea, an engineering concept, a creative concept, an agent skill
(not necessarily MMSS), or an abstract notion the user is trying to
materialize visually.

Default: **one icon per request**. When the user requests a set, lock shared
parameters first, then vary meaning and motion — not style.

This skill is the portable, universal counterpart of the MMSS-specific icon
skills. It shares their *process* but not their palette, invariants, or
infrastructure.

## 2. Core stance

An icon is a **compressed reading** of the target, not an illustration of
its title. Two consequences:

- A skill named "quantum" may forbid quantum imagery; a skill named
  "hyperloop" may be about convergence, not speed. **Read, don't skim.**
- A pulse can be stylistic or semantic. Stylistic pulses are fine; they
  establish rhythm and are not claimed to encode an event. Semantic pulses
  must correspond to something real. Do not dress up stylistic motion as
  process.

Prefer one clear motion over several competing ones. Prefer clarity at
small sizes over detail that only reads at 512 px.

## 3. Working process (7 steps)

Execute in order. Each step has an explicit output. Do not skip.

### Step 1 — Read the target

Read the full supplied material: `SKILL.md`, description, README, spec,
documentation, or the user's prose. Do not infer the process from the name.
Record what was read and what was not available.

### Step 2 — Extract the semantic skeleton

From the material, derive a four-tuple:

```
entities       : what exists, what acts, what is acted upon
events         : what changes, what is decided, what is emitted
flow-direction : one-way / bidirectional / spiral / parallel / branching
emission       : the artifact or state that leaves the process (or "none")
```

For skills, `SKILL.md` sections are a good guide. For non-skills, use the
target's own structure (features, lifecycle stages, actors, states).

If the target has no definable process — it is a property, a relation, a
state, a category, or a symbol — do not invent a process. Record instead:

```
depiction   : what the icon shows (property, relation, or state)
emphasis    : what aspect of it matters most
motion-role : what motion conveys, if any
```

A property-based or state-based icon is fully valid. Motion is permitted and
may convey emphasis, contrast, or recurrence even when no event stream
exists.

### Step 3 — Choose the visual metaphor

Select the metaphor that best matches the skeleton. Metaphor options are
**open** — no fixed library required. Common shapes that recur:

| Shape | Suits |
|---|---|
| Orbit + beam / scan | catalogue, index, selection |
| Cascade / chain | staged transit, typed pipeline |
| Funnel | lossy filtering, progressive reduction |
| Field | open materialization, emergent outputs |
| Binary / Vortex | two streams in tension, fixed core |
| Panel / Trace | parallel lanes; distinct from collapsed verdict |
| Y-merge | two sources → gate → ranked output |
| Nested loops | iterative convergence |
| Polar gate | multi-exit decision point |
| Forge | process that produces a sub-artifact |
| Open bloom | divergence, intentional non-closure |
| Twin rails | two different-natured domains → shared gate |

These are **examples, not constraints**. A novel process deserves a novel
shape. Prefer a familiar shape only if it genuinely fits.

State the chosen metaphor and the reason in one sentence. If two fit
equally well and cannot be disambiguated without more information, choose
one and note the alternative — do not silently pick.

### Step 4 — Compose

Design the icon as a set of geometric elements. Every animated element either
serves a semantic role from Step 2 **or** is identified as stylistic (see §4).

Minimum considerations:

- **Static frame at t=0** must read as the icon — even if animation stopped.
- **Shape silhouette** should read at small sizes.
- **No element that pretends to be semantic while being decorative.**
  Stylistic motion is allowed when it is unobtrusive and when it is not
  claimed to encode a process event.

Compose with concrete elements (circles, lines, paths, rects, polygons,
text). If using arrows, dots, or trails, name what they represent.

### Step 5 — Animate

Choose the animation technology per §6. Determine:

- what moves (which element);
- how it moves (rotate, translate, pulse, fade, path draw, color shift);
- why it moves (what process event or emphasis it encodes, or which stylistic
  role it serves);
- how long the cycle is (must reflect the target's character, not aesthetic
  preference).

Every motion either answers "what does this represent?" without a caption
**or** is explicitly recognized as stylistic. Stylistic motion does not need
an invented process meaning; it needs only that it not misrepresent the
target.

### Step 6 — Validate

Before emitting:

- **Family invariants:** none required in universal mode, but if the target
  belongs to an existing visual family, follow its invariants.
- **Palette:** if the user or project supplied one, use it exactly; otherwise
  choose a small, coherent palette (≤6 colors). Do not attach universal
  meanings (e.g. "green = verified") unless the target project itself defines
  them.
- **Accessibility:** `<title>`, `<desc>`, `role="img"`, `aria-label` present.
- **Static state:** t=0 reads standalone.
- **No external resources:** everything inside the SVG.
- **Size:** legible at 128×128; the SVG file should be under ~12 KB unless
  complexity requires more.
- **Reduced motion:** see §8.
- **Honest verification:** see §9.

### Step 7 — Emit

Produce the response per §10.

## 4. Meaning and motion

Before writing any SVG element, answer these explicitly:

| Question | Example |
|---|---|
| What is depicted? | "a five-stage pipeline ending in a validation gate" |
| What action or state matters? | "each stage passes its output to the next only after audit" |
| What must move? | "a signal that traverses the stages and pauses at each" |
| What does the motion represent? | "the audit — a moment of attention, not a transformation" |

Do not conflate these distinctions:

- **exchange vs merge** — two streams passing through vs fusing
- **independent streams vs shared result** — parallel paths reaching separate outputs vs converging
- **infinite cycle vs finite process** — loop forever vs emit and stop
- **assumption vs confirmed result** — a hypothesis being tested vs a verified fact
- **open vs closed** — a process that refuses closure vs one that terminates in an output

Mislabeling any of these with the wrong shape **lies about the target**.
Choose shape from the meaning, not the other way around.

**Semantic vs stylistic.** Semantic elements encode a property, relation,
event, or state of the target and would be missed if removed. Stylistic
elements establish rhythm, contrast, and readability; they can be tuned or
removed without changing the meaning. Name which is which when it matters.
Do not invent a process justification for a stylistic choice.

## 5. Visual language

The universal skill does not mandate:

- a specific palette;
- a central anchoring element (diamond, circle, or otherwise);
- a circular background;
- a dashed border;
- a fixed 64×64 viewBox;
- a specific list of archetypes;
- fixed cycle durations.

Accepted input parameters:

```
topic          : what the icon is about (required)
purpose        : where/how it will be used (README, hero, badge, etc.)
audience       : who reads it (developer, user, researcher, ...)
style          : minimal | technical | warm | playful | diagrammatic | custom
palette        : named colors or hex list; if absent, choose coherent
shape          : round | square | banner | free-form
background     : transparent | dark | light | custom
size           : base size (default 128×128)
intensity      : subtle | medium | expressive
references     : other icons the user likes
```

If parameters are absent, choose a coherent default. **Do not force the
user to fill a survey.** Ask a clarifying question only when ambiguity
blocks meaningful work.

For sets of icons: lock shared parameters first (palette, stroke weight,
corner radius, motion vocabulary), then vary meaning and motion per icon.

**Color convention.** Colors are the composer's choice unless the project
(or user) supplies an explicit convention. When a convention is given — a
palette, semantic colors, brand colors — use it exactly. When no convention
is given, treat all colors as free choices. Do not assert that a specific
color (for example, green) universally encodes verification, success, or
any other property; that is a project-specific convention, not a default.

## 6. Animation technology

Three mechanisms are acceptable: CSS inside SVG, SMIL, or a mix.

### 6.1 CSS `@keyframes` inside SVG

```xml
<style>
  @keyframes pulse { 0%,100% { opacity: 1 } 50% { opacity: 0.5 } }
  .pulse { animation: pulse 2s ease-in-out infinite; }
  @media (prefers-reduced-motion: reduce) {
    .pulse { animation: none; opacity: 1 }
  }
</style>
```

**Use when:** the motion is periodic and reducible to CSS. Supports
`prefers-reduced-motion` cleanly.

**Works in:** SVG loaded via `<img>`, inline SVG, standalone `.svg` opened
directly. External CSS references are blocked — keep `<style>` inline.

### 6.2 SMIL `<animate>` / `<animateTransform>`

```xml
<circle cx="32" cy="32" r="4" fill="#22D3EE">
  <animate attributeName="cy" values="10;50;10" dur="4s" repeatCount="indefinite"/>
</circle>
```

**Use when:** the motion requires path following, transform sequences, or
per-attribute coordination that CSS cannot express cleanly.

**Works in:** SVG loaded via `<img>`, inline SVG, standalone `.svg`. No
JavaScript needed.

**`prefers-reduced-motion` limitation:** SMIL has no native equivalent.
Workarounds (§8.2) are required for reduced-motion compliance.

### 6.3 Mixing

Valid when each mechanism covers what it does best. Example: CSS for
color shift + SMIL for path traversal. Avoid mixing for the same
motion — it makes the intent unreadable.

### 6.4 Not permitted

- External JavaScript (any form)
- External stylesheets (`<link href>` to a network or local file)
- External fonts (webfonts from URLs)
- External images (`<image href>` to network URLs)
- Referenced network resources of any kind
- HTML wrapper required for the SVG to render

Everything the SVG needs to render must be inside the SVG file.

## 7. GitHub README target

Primary target: GitHub README rendering the SVG as an image from a
repository file.

### 7.1 Embedding

```html
<img src="assets/icon.svg" width="128" height="128" alt="Short description">
```

or

```markdown
![Short description](assets/icon.svg)
```

The `<img>` form allows explicit size control. Markdown `![]()` does not
respect `width` reliably.

### 7.2 What works inside a README SVG

Commonly used in current GitHub SVG rendering; verify per §7.4 before
claiming. Categories of behavior:

- SMIL (`<animate>`, `<animateTransform>`)
- Internal `<style>` with `@keyframes`
- `prefers-color-scheme` media queries inside `<style>`
- SVG-level `<title>` and `<desc>`

Often works but not universally guaranteed:

- `prefers-reduced-motion` behavior inside SVG loaded via `<img>` —
  depends on the browser, not on GitHub per se
- CSS `:hover` interactions — never reliable inside `<img>`
- CSS variables inherited from the host page — no, `<img>` is isolated

Not permitted in README at all (GitHub sanitizes):

- `<style>` blocks in the Markdown file itself
- External stylesheets or fonts
- `<script>` of any kind
- `<iframe>`

### 7.3 `prefers-reduced-motion` in `<img>` context

Honest status: `@media (prefers-reduced-motion: reduce)` **inside the SVG**
does reflect the user's OS setting in current Chrome and Firefox when the
SVG is loaded via `<img>`. It is **not guaranteed** across all browsers
or all OS combinations. This is browser behavior, not GitHub behavior.

For SMIL, there is **no native equivalent** — see §8.2.

### 7.4 What is not verified by writing the SVG

Writing the SVG does not verify that:

- GitHub renders it correctly in a specific browser;
- the animation plays;
- `prefers-reduced-motion` is honored.

These require the file to be committed and viewed on GitHub. Report
honestly (§9).

## 8. Accessibility and reduced motion

### 8.1 Baseline

- `<title>` — the icon's name
- `<desc>` — 1–3 sentences of what the icon conveys
- `role="img"` on the root `<svg>`
- `aria-label` on the root `<svg>` — matches or slightly expands title
- `alt` attribute in `<img>` — for README embedding
- t=0 frame must read as the icon (not blank, not random)

### 8.2 `prefers-reduced-motion`

Three honest strategies, in priority order:

**A. CSS-based motion with reduced-motion support** (preferred):

```xml
<style>
  @keyframes orbit { to { transform: rotate(360deg) } }
  .orbit { animation: orbit 12s linear infinite }
  @media (prefers-reduced-motion: reduce) {
    .orbit { animation: none }
  }
</style>
```

The reduced-motion requirement is honored for the CSS-driven motion. This
addresses reduced-motion only; it is not a broader accessibility compliance
claim.

**B. Two-file fallback via `<picture>`** (works for SMIL):

```html
<picture>
  <source srcset="assets/icon-static.svg"
          media="(prefers-reduced-motion: reduce)">
  <img src="assets/icon-animated.svg"
       width="128" height="128" alt="Short description">
</picture>
```

Provide both files. The static one has the animation removed. This is
the most reliable approach when SMIL is required.

**C. Acknowledge limitation explicitly** (when A and B are impossible):

If only SMIL is available and the user cannot provide two files, state:

> "This icon uses SMIL animation. `prefers-reduced-motion` is not natively
> honored inside SVG loaded via `<img>`. For strict compliance, provide
> a static companion file and use `<picture>` per §8.2.B."

Do not claim reduced-motion compliance that the mechanism cannot deliver.

### 8.3 No intrusive flashing

No element should flash faster than ~3 Hz (approximately 3 cycles per
second). Slow pulses are fine. Strobing is not. Reduced-motion and avoiding
intrusive flashing are **separate measures**. Neither certifies that the
icon is fully accessible — other requirements (§8.1) remain in force.

## 9. Verification honesty

Every claim about verification must match what was actually done. Distinguish:

| Level | What was done | Can be claimed |
|---|---|---|
| **Written** | SVG source exists | "SVG source written" |
| **Parsed** | XML parser accepts it | "XML is well-formed" |
| **Rendered** | Opened in a viewer | "Renders correctly in [viewer]" |
| **Animated** | Watched in a viewer | "Animation plays in [viewer]" |
| **Viewed on GitHub** | Committed and opened on GitHub in a specific browser | "Rendered and animated on GitHub in [browser, date]; not verified across browsers or on other platforms" |

Do **not** claim a level you did not perform. Writing an SVG does not
prove it renders. Rendering locally does not prove it works on GitHub.
Viewing on GitHub in one browser does not prove cross-browser behavior.

Absence of a browser or a parser **must not block** producing the SVG.
Produce the SVG and clearly state what was and was not verified.

Do not invent execution times, rendering metrics, or performed actions.

Do not call the process "deterministic" unless reproducibility is enforced
by the workflow itself.

## 10. Response contract

Default response:

1. **The `.svg` file** — as a file when the environment allows it,
   otherwise as a complete code block.
2. **Visual idea** — 2–4 sentences on what the icon conveys and how.
3. **Element → meaning map** — optional. Include only when it genuinely aids
   comprehension. Omit when the icon is self-explanatory or when the map
   would restate what is already visible.
4. **README embedding example** — Markdown or `<img>` with a relative path.
5. **Verification** — what was checked and what remains unverified.
6. **Notes** — `prefers-reduced-motion` behavior, file size, deliberate
   omissions.

If the user asks for "SVG only," return **only** the SVG. No verification
line, no explanation.

Do not publish, install, or modify a repository without explicit
permission. Do not use a fixed installation path — always resolve with the
user or the environment.

## 11. Anti-patterns

Failure modes traced to the source session or reasoned from the same
principles. Items marked **[observed]** were directly encountered in the
source session as decision points. Items marked **[plausible]** are reasoned
from the same principles but were not necessarily encountered as a
shipped-icon failure in this session. Do not infer a wider set of real
failures from this list.

1. **Quantum aesthetics for "quantum" names.** [observed] — decision point
   in hyperloop / meta-architect design.
2. **Merging streams the target keeps distinct.** [observed] — session-logger
   Panel-vs-Trace analysis.
3. **Forcing closure on open-ended targets.** [observed] — creativity-flow
   Open Bloom design.
4. **Assigning universal color meanings without a project convention.**
   [plausible] — flagged as a design principle; not observed as a shipped
   failure.
5. **Painting hypotheses as verified.** [observed] — siglip role in AM-STAGE
   was explicitly marked HYPOTHESIS, not ESTABLISHED.
6. **Drawing all of a target's content.** [observed] — repeated
   15-sections-in-128px constraint.
7. **Inventing new colors per icon in a family.** [plausible] — was a
   maintained constraint, not an observed failure.
8. **Omitting the element → meaning map when it would help.** [plausible] —
   no shipped icon skipped it in-session.
9. **Confusing parallel-lanes-that-collapse with parallel-lanes-that-persist.**
   [observed] — Panel/Trace case.
10. **Claiming reduced-motion compliance for SMIL without a fallback.**
    [plausible] — raised as a design consideration; not observed as an
    actual shipped claim.

## 12. Stop conditions

Stop and report blocked or partial when:

- the target material is not supplied and cannot be read;
- the target has no definable process — **this does not block the icon**.
  Emit a property, relation, or state icon (§3 Step 2). Ask only if the
  depicted property or state is genuinely ambiguous and the outcome would
  materially change;
- the user explicitly forbids animation, in which case return a static
  SVG only;
- the user demands `prefers-reduced-motion` compliance but accepts only
  SMIL and refuses the two-file fallback — report the limitation rather
  than claim compliance;
- the target's character cannot be captured in a shape that the user
  would recognize — return two candidate directions and let the user
  choose.

## 13. Completion standard

Task complete when:

- one standalone SVG is produced;
- `prefers-reduced-motion` strategy is chosen and stated (§8.2);
- accessibility metadata is present;
- the t=0 frame reads as the icon;
- the element → meaning map (or a one-line justification) is present when
  it adds clarity; optional otherwise;
- the README embedding example is present (its presence does **not** assert
  that the embedding renders on GitHub — see §9);
- the verification table (§9) is filled in truthfully;
- any deliberate omissions are listed.

A complete icon is **auditable**: every animated element traces to a
meaningful role or is honestly marked stylistic, the embedding example is
supplied, and the verification claim matches the actual work.

Do not claim the embedding works unless the icon was actually committed and
viewed on GitHub.

## 14. Language

Skill body — English.
Agent's explanations, responses, and clarification questions — user's
language.
SVG content — follows the target's language; `<title>` and `<desc>` in the
language the user or target uses.
Machine identifiers, color codes, sizes — English / numeric.

## 15. Non-goals

- No RAG, embeddings, vector store, fingerprint, normalization space, or
  persistent cache as required components.
- No fixed installation path.
- No management layers, orchestration wrappers, or capability levels.
- No required MMSS palette, invariants, or archetype list.
- No publishing, installing, or modifying repositories without permission.
- No claim of "verified on GitHub" without an actual commit and view.

---

## Appendix — Minimal decision checklist

Before emitting, run this in order:

```
[ ] Target was read fully, not inferred from name
[ ] Semantic skeleton (4-tuple) extracted, OR property/relation/state recorded
[ ] Visual metaphor chosen and stated with one reason
[ ] Every animated element is semantic OR explicitly stylistic
[ ] t=0 frame reads as the icon
[ ] Palette ≤6 colors, coherent (or matches an explicit convention)
[ ] No external resources, no JS
[ ] File size < 12 KB
[ ] <title>, <desc>, role="img", aria-label present
[ ] prefers-reduced-motion strategy chosen (CSS / picture / disclosed)
[ ] Verification table filled in truthfully
[ ] README embedding example present
[ ] Response has: SVG, idea, map (if useful), embedding, verification
```