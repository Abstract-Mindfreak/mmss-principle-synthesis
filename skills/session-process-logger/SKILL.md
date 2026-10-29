---
name: session-process-logger
description: "Creates compact, traceable retrospective history logs of an agent session from available messages, materials, skill references, tool calls, results, and artifact changes. Distinguishes observed traces from claimed actions and retrospective interpretations. Supports full-session, partial/fragment, and notation-proposal modes. Does not reconstruct hidden reasoning, invent events, or execute past actions."
metadata:
  version: "0.2.0"
  maturity: test_candidate
  default_output: markdown
  default_language: en
---

# Session Process Logger

## 1. Purpose

Produce a compact, content-preserving retrospective history log of an agent
session (or a requested fragment of it) based solely on available messages,
materials, skill references, tool calls, tool results, and observable artifact
changes.

The log is not a reconstruction of hidden internal reasoning, not an idealised
account of how the process "should" have unfolded, and not an automatic
re-execution of any described actions.

## 2. Modes of Use

The modes may be combined and do not form a mandatory sequence. Select by user
request; for a plain "show session log" default to full-session mode. The user
need not know mode identifiers.

### 2.1 Full-session log

Cover all distinguishable substantive events of the available session history,
with an honest statement of actual coverage.

### 2.2 Partial / fragment log

Produce a log limited to a user-specified range, theme, artifact, skill, tool,
branch, or other indicated area. Include only the necessary preceding context.
Clearly distinguish events that fall inside the requested fragment from
explanatory material drawn from outside it.

### 2.3 Notation-proposal mode

On the basis of the chosen session or fragment, propose useful additions to the
notation table. For each proposal show:

- the symbol or entry,
- a possible use,
- the fragment of history that motivates the need,
- whether the symbol was already used in the session or is newly suggested.

Do not add a symbol merely because it exists elsewhere. Do not create a closed
classification of processes. Proposals remain proposals until the user accepts
them; the existing table is not altered automatically.

## 3. Grounds of Entries

When useful, mark entries with one of the following foundations. Use the label
pair (English term / appointed abbreviation) consistently within one log:

- **[OBS]** (observed trace) — directly visible in the available history or tool
  result.
- **[CLAIM]** (claimed) — a participant stated that an action occurred, but no
  separate confirmation is present.
- **[INTERP]** (interpretation) — retrospective interpretation of a connection.
- **[?]** — unknown or untraceable.

Interpretation rules:

- A message saying "file created" confirms the existence of the statement, not
  necessarily the file write.
- Mention of a skill, presence of its text, an observed read, a claimed
  application, and a traceable effect are distinct events.
- Sequence of events does not prove causal connection.
- Do not attribute to the user requirements that the agent introduced on its own.
- Do not project later clarifications backwards into earlier events.
- If a claim is later acknowledged as an assumption, preserve the original
  presentation and record the clarification separately.

## 4. Symbolic Notation

Available conventions (use only those that are needed):

- `:=`  local designation
- `⊕`   interaction of materials
- `▷`   application as influence, setting or perspective
- `→`   next recorded step
- `↝`   emergence or interpretable transition
- `↺`   return of a result into the process as material
- `Δ`   change between states or configurations
- `∥`   co-existing branches
- `?`   unknown or open
- `≈`   approximate correspondence
- `≠`   significant difference
- `∈`   membership in a locally designated set
- `∅`   known absence (distinct from unknown)

The alphabet is extensible. Briefly explain any symbols actually used in the
legend of that log. Do not force events into elegant expressions.

## 5. Reading of Instructions and Truncation

If the history shows that a skill or file read was truncated:

- record the accessible boundary,
- any attempts to obtain continuation,
- and the gaps that remained at that time.

A read-tool call is not proof that the full file was obtained. Later availability
of the complete text does not prove it was available at the earlier moment.
The logger itself does not re-invoke past skills, re-run research, or execute
past commands. For logging it is sufficient to use the available trace; the
unknown may be left unknown.

## 6. Output

Default format: Markdown with compact textual schemes. Support other formats on
explicit request.

A typical full or partial log contains:

- statement of actual coverage and a short legend of symbols used,
- chronological events,
- a summary scheme when it adds understanding,
- material limitations of coverage and confirmation.

Rules:

- Do not fill sections for the sake of form.
- Do not reprint the entire conversation.
- Do not replace the log with a general paraphrase.
- Repetitions may be grouped while preserving significant differences.
- Never declare an incomplete log complete.
- If output is split across parts, mark the boundary and the continuation point.
- Do not invent dates, platform message numbers, or identifiers. Local event
  numbers are permitted.
- For long sessions, compress repeated routine steps into one grouped entry;
  keep one-to-one detail only for decisions, file writes, skill activations,
  and user-visible outputs.

## 7. Constraints

- Do not reconstruct hidden internal reasoning.
- Do not invent prevented actions or alternative branches.
- Do not treat sequence as proven causality.
- The skill must be usable in a fresh session from its own instruction alone.
