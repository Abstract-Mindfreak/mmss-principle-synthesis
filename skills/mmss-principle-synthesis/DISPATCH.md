---
name: mmss-references-dispatch
description: "Index of section IDs and markers for locating reference text in ALL_REFERENCES.md. Contained in mmss-principle-synthesis package."
metadata:
  version: "0.1.0"
  maturity: test_candidate
  parent: mmss-principle-synthesis
  reference-source: "ALL_REFERENCES.md"
---

# MMSS Reference Section Index

This file documents section IDs and markers for reference text stored in the sibling `ALL_REFERENCES.md`. It is a reading guide, not an executable loader; the package does not provide runtime code for extracting sections.

## Section Markers

Reference sections use these markers:

- Start: `### <REF_ID> ===`
- End: `### END <REF_ID> ===` (for sections)
- For top-level blob boundaries: `### END SOURCES ===`, `### END PRINCIPLES ===`, etc.

Allowed reference IDs and their aliases:

- `SOURCES` → Sources and Provenance
- `PRINCIPLES` → Principles and Abstraction
- `INVARIANTS` → Invariants and Transfer
- `METAFORMULAS` → Meta-Formulas and Symbols
- `ARCHITECTURE` → Architecture and Contracts
- `ORCHESTRATION` → Orchestration and Repair
- `INTEGRATION` → Integration and Versioning
- `PERSISTENT` → Persistent Operation and Metrics
- `DEMONSTRATIONS` → Demonstrations
- `ACCEPTANCE` → Acceptance Examples

Agents can use this index to locate and read the requested section from `ALL_REFERENCES.md`.

## Missing section

When a reference is requested but not found:

Report that the requested section is unavailable.

No automated fallback or runtime loading behavior is defined.

## Usage

When `mmss-principle-synthesis` needs a reference, read the section bounded by the `SOURCES` markers in `ALL_REFERENCES.md`.

This convention helps an agent find reference text when the package files are available to it.

## Constraints

- The reference file must be present and complete. If it is truncated, section text may be incomplete.