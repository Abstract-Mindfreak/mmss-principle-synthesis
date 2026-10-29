---
name: skill-quick-sampler
description: "Quick sampling of skill instructions from a remote or local directory (GitHub tree URL, raw listing, or local path). Select N instructions, emit one short usage example per instruction, and allow easy switch of the source URL or path. Use for rapid overview, example generation, or lightweight inventory of a skill collection without loading full SKILL.md bodies. Triggers include quick sample, sample skills, one example per skill, list 30 skills with examples, browse skill catalogue, change skills source."
metadata:
  version: "0.2.0"
  maturity: test_candidate
---

# Skill Quick Sampler

## Purpose

Produce a lightweight inventory of skills from a remote or local catalogue.
For a requested count N (default 30) return exactly one short usage example per
selected skill. Source URL/path is a single replaceable parameter so the same
skill works against any Agent-Skills-compatible directory.

## Parameters

- **count** — number of skills to sample (default 30, hard cap 50 in one
  response; if larger counts are requested, issue several responses and state
  the remainder).
- **source** — GitHub tree URL, raw directory listing, or local path. There is
  no network default: if no source is given by the user or set previously in
  this session, ask for it instead of picking one autonomously.
- **filter** — optional keyword to bias selection (e.g. genomic, validation,
  meta).
- **sampling** — uniform or keyword-stratified; if stratified is requested,
  state the strata you used. Sampling is not guaranteed reproducible (an
  explicit `seed` is accepted but honored only where the listing source permits
  deterministic ordering).

## Process

1. Resolve source. If the user supplies a new URL or path, use it for this and
   subsequent calls until changed again.
2. Obtain the list of skill directories (prefer GitHub API `/contents/` or a
   directory listing).
3. If the source is unavailable or private, report the access error and stop;
   do not invent a fallback source.
4. If a filter is given, prefer matching names; otherwise uniform sample of
   size count.
5. For each selected skill emit a single line:
   - skill name,
   - one concrete usage example (1–2 sentences) derived from the skill
     description or a typical trigger,
   - link to its SKILL.md if available.
6. Do not load full SKILL.md bodies unless the user explicitly asks for deeper
   inspection of a named skill.
7. Output as a numbered Markdown list, or as a JSON array when the user
   requests machine-readable form.

## Output Provenance

Always state at the top of the response:

- which source (URL or path) was used,
- how many skills were available in total,
- how many were sampled and by which rule (uniform / filtered / stratified).

Examples must be paraphrases of the actual description text. If a description
is too thin to build an example, say "no usable description" instead of
composing one.

## Source switch example

User: "Смени источник на https://github.com/another-org/skills/tree/main/skills и выбери 20"

→ update the active source and sample 20 from the new location.

## Constraints

- Never invent skill names that do not appear in the source listing.
- Keep each example under 40 words.
- Read-only skill: never write files or modify the source.
