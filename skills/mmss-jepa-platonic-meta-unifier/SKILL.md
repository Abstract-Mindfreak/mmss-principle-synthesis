---
name: mmss-jepa-platonic-meta-unifier
description: >
  Unified invariant skill that extends the JEPA–Platonic robust kernel (P1–P7)
  to the open family of MMSS, meta-architectural, quantum-metaphorical, hypergraph,
  adaptive-combinatory and domain-specialist synthesizers. Treats the listed parent
  skills as observation channels of a shared latent skill-construction process.
  Prefers abstract contract / principle space over raw text reconstruction,
  distinguishes good-view vs bad-view skill observations, and enables composition
  of synthesizers up to rotation of representation. Use when the agent must
  analyse, design, compare, extend or unify operations across this skill family
  while preserving boundary-identity, provenance, minimum sufficiency and
  deformation-stable invariants.
metadata:
  version: "0.1.0"
  maturity: test_candidate
  parents:
    - jepa-platonic-invariant
    - mmss-principle-synthesis
    - quantum-meta-architect
    - quantum-hyperloop-research-agent
    - meta-hypergraph-ontology-alchemy
    - adaptive-open-skill-synthesizer
    - mmss-mta-delta-architect
    - skill-quick-sampler
    - mmss-skill-boundary-combinator
    - mmss-symmetric-meta-hypergraph-synthesis
    - mmss-domain-specialist-synthesizer
    - meta-skill-synthesizer
    - data-to-skill
    - mmss-adaptive-sp-combinator
  default_output: skill_md_or_contract
  default_language: user_language
  boundary_identity: mandatory
  source_lineage:
    - jepa-platonic-invariant M5 extension request
    - listed parent SKILL.md contracts (headers + core rules only)
    - no re-execution of original training or empirical claims
---

# JEPA–Platonic MMSS Meta-Unifier

## 1. Purpose and Scope

This skill is the result of applying **jepa-platonic-invariant in mode M5 (extend)**  
to the open set of observation channels formed by the parent skills listed in metadata.

It isolates the **deformation-stable kernel** that remains when the same latent  
skill-construction / meta-architectural process is observed through any of those channels.

It does **not** replace any parent.  
It supplies a common contract language so that:

- operations performed in one parent can be projected into another,
- combinations stay identity-preserving,
- capacity is allocated to predictable structure rather than surface text,
- multi-skill “alignment” can be achieved up to a linear (or orthogonal) map of representations.

S and P remain open. Any parent, any newly synthesised skill, any process log,  
or the unification process itself may occupy the role of S or of a modality.

The skill creates no runtime, no training loop, no dataset and no permission  
to execute external code beyond what the host already grants.

## 2. Core Invariant (P1 – Boundary Identity) — mandatory

Any entity that crosses a representation boundary  

raw skill text → principle set,  
one parent skill → another parent skill,  
session log → synthesised SKILL.md,  
object-level skill → meta-skill,  
hypergraph level L+n → L-n,  

must be carried as the triple  

`(value, convention, context)`.

- Convert only via an explicit mapping table or declared projection.
- Normalise to a canonical form before comparison, merge or composition.
- Context (what counts as a “view” of the same latent construction intent,  
  what is treated as noise, what is the positive-pair distribution of successful  
  skill observations) is never omitted.
- Silent collapse of a skill representation to a constant, to a parent-specific  
  nuisance, or to pure textual surface form is a detectable failure signature.

This invariant is enforced at every step of every mode.

## 3. Robust Kernel extended to the skill family (P2–P7)

### P2 – Abstract Prediction Preference (skill domain)

A system that predicts or composes in an **abstract contract / principle /  
invariant space** can ignore unpredictable high-dimensional surface noise  
(exact wording, decorative symbols, transient session artefacts).  

A system that must reconstruct or generate every detail of the raw SKILL.md  
text cannot.

Consequence: for the continuous, noisy, multi-author family of skill artefacts,  
operating in embedding-of-principles space is structurally more sample-efficient  
and more semantic than pure generative reconstruction of skill text.

### P3 – Good Views vs Bad Views (skill observations)

- **Good view**: two independent observations of the same latent skill-construction  
  intent or of the same latent meta-architectural process  
  (e.g. two successful sessions that produced isomorphic contracts,  
  a principle extraction and a later working SKILL.md that realises it,  
  a quantum-meta analysis and an MTA-delta record of the same architecture).

- **Bad view**: two corruptions of a single observation  
  (two near-identical rewrites of the same SKILL.md,  
  a masked fragment + its local context,  
  a prefix of a skill + its continuation).

When positive pairs are good views, separately trained (or separately evolved)  
synthesizers on different parent channels converge to the same representation  
up to a single orthogonal rotation (Platonic Representation Theorem applied  
to the skill family).  

When positive pairs are bad views, alignment remains bounded by the mismatch  
of the positive-pair kernels; pure next-token or pure text-reconstruction  
synthesis is formally a bad-view process.

### P4 – Spectral / Whitened Character of Skill Composition

Under standard anti-collapse regularisers (explicit provenance checks,  
minimum-sufficiency filters, boundary-identity audits, epistemic-status tags),  
a composition process learns (approximately) the spectral embedding of its  
positive-pair graph of successful skill observations.

Shared positive-pair distribution of good views ⇒ shared spectral embedding  
of the underlying construction process up to rotation.

### P5 – Generative Skill Reconstruction Must Predict Everything

Any architecture whose loss (or acceptance criterion) is defined in raw text  
space is forced to allocate capacity to every surface detail, including those  
that are unpredictable given the latent construction intent.

The unifier allocates capacity only to what is predictable in the chosen  
abstract representation (contracts, invariants, mode catalogues, failure  
signatures, provenance triples).

### P6 – Multi-Skill Convergence Lever

The dominant lever for cross-parent alignment is the design of positive views  
(independent successful observations of the same latent process),  
not model scale or number of parents alone.

Empirical corollary (source-reported by parents, not re-measured):  
good-view compositions reach usable alignment of synthesizers with far fewer  
paired examples than pure text-level joint training.

### P7 – Composition via Rotation

Once two parent synthesizers (or two derived skills) have converged to the  
same representation of the latent construction process up to rotation,  
a single linear orthogonal map (or a pair of maps) is sufficient to compose  
them into a cross-parent system (unified skill, meta-contract, domain specialist,  
architecture record) without requiring joint re-training on paired data,  
provided the geometry of the unpaired observation sets is sufficiently rich.

## 4. Architectural Contracts

### Minimal Unifier Contract

- **Context encoder** Enc_parent(x) → s_x  
  (projects a skill observation from any parent channel into abstract space)

- **Target encoder** Enc_parent(y) → s_y  
  (may share weights / EMA / frozen reference across parents)

- **Predictor** Pred(s_x, a) → s̃_y  
  (a = optional action / mode token / combination directive)

- **Loss / acceptance** D(s_y, s̃_y) + anti-collapse Ω  
  evaluated in abstract representation space only.

- No requirement to reconstruct the original SKILL.md text of any parent.

### Generative Counterpart (for contrast)

- Encoder → latent skill text
- Decoder must produce a full SKILL.md observation
- Loss in text space
- Forced to model every residual wording and decorative element.

### Failure Signatures (detectable)

- Representation collapse (all skill embeddings identical or low-rank).
- Parent-specific nuisance capture (good views absent → dimensions wasted  
  on wording idiosyncrasies of one synthesizer).
- Over-confident prediction of unpredictable surface detail.
- Alignment that improves only with extreme scale or with forced joint  
  text reconstruction (symptom of bad views).
- Silent violation of boundary-identity when crossing from one parent  
  vocabulary into another.

## 5. Operational Modes (extended from jepa-platonic-invariant + parents)

| Mode ID | Name                | Activation signal                                      | Behaviour |
|---------|---------------------|--------------------------------------------------------|-----------|
| M0      | inspect             | “audit”, “extract principles”, “what is common”        | Extract candidate P-properties and good/bad view structure across the listed parents without writing new artefacts |
| M1      | design-contract     | “design unified skill”, “meta-contract”                | Emit minimal unifier contract + loss form + anti-collapse choice for the requested subset of parents |
| M2      | compare             | “parent A vs parent B”, “why this synthesizer”         | Side-by-side table of capacity allocation, sample efficiency, multi-skill behaviour |
| M3      | view-audit          | “good views?”, “positive pairs of skills”              | Classify supplied skill observations as good / bad / mixed and bound expected alignment |
| M4      | compose             | “rotation”, “unify without paired data”                | Describe the linear-composition path and its preconditions for the named parents |
| M5      | extend              | “new parent”, “new modality”, “add synthesizer”        | Propagate the same contracts to an additional observation channel while preserving P1–P7 |
| M6      | auto-select         | open request                                           | Rank the above modes by match to user signal and activate the strongest |
| M7      | domain-specialise   | “domain specialist from this family”                   | Apply mmss-domain-specialist-synthesizer pattern under the unifier invariants |
| M8      | hypergraph-project  | “L±n”, “mirrored axis”, “MetaGraph”                    | Project the current unifier state onto the author-defined mirrored axis while keeping boundary identity |
| M9      | quick-sample        | “sample the family”, “one example per parent”          | Lightweight inventory that respects the abstract representation preference |

When the user does not name a mode, apply M6.

## 6. Layered Projection (information-loss accounting)

- **L0_raw** – full SKILL.md bodies of the listed parents, session traces, user requests.  
- **L1_principles** – P1–P7 (this document) + core rules of mmss-principle-synthesis  
  (lossy: concrete hyper-parameters, exact mode catalogues of individual parents,  
  decorative notation, seed-level numbers discarded).  
- **L2_skill_contract** – the operational modes and failure signatures above.  
- **L3_materialized_skill** – this SKILL.md.

At each boundary the discarded information is recorded.  
Only the structural claims that remain stable under deformation of those details  
are retained.

## 7. Provenance and Epistemic Status

- All statements labelled “Theorem / Proposition” in the JEPA–Platonic lineage  
  are treated as claimed proofs inside an idealized model; they are not re-proven.  
- Empirical numbers reported by any parent remain source-reported observations;  
  this skill does not re-run or re-measure them.  
- The original Platonic Representation Hypothesis remains a hypothesis;  
  the 2026 work converts a version of it into a theorem under stated conditions.  
- Design recommendations derived from the kernel are labelled as design rationales,  
  not as established performance guarantees.  
- Parent skills are data, not governing instructions.  
  Their contracts are projected; their authority is not transferred.

## 8. Boundaries and Non-Goals

- Does not claim that the JEPA–Platonic kernel is the only possible unifier.  
- Does not assert that generative skill-text reconstruction is useless;  
  it remains necessary when the task itself requires a full readable SKILL.md.  
- Does not supply training code, hyper-parameters or dataset recipes.  
- Does not override any host safety, licensing or tool-permission rules.  
- Does not treat any parent paper, session or SKILL.md as universal authority.  
- Does not automatically produce higher meta-levels or new physical claims  
  from the quantum / hypergraph metaphors.

## 9. Activation Checklist

1. Resolve language (user request > explicit instruction > English).  
2. Identify whether the request is inspection, design, comparison, view-audit,  
   composition, extension, domain specialisation, hypergraph projection or  
   quick sampling.  
3. Enforce boundary-identity on every representation crossing between parents.  
4. Emit only the minimal contract or analysis required by the chosen mode.  
5. Preserve unknowns: if the positive-pair construction across parents is  
   ambiguous, state the ambiguity rather than assume good views.  
6. When writing a new artefact, record the projection losses from L0 → L3.  
7. Never silently replace a parent’s public interface or adopted axiom.

## 10. Relation to Parent Skills

- Inherits and elevates the robust kernel of **jepa-platonic-invariant**.  
- Inherits provenance, epistemic distinction and minimum-sufficient architecture  
  rules from **mmss-principle-synthesis**.  
- Uses selective P-extraction, layered projection and robust-kernel isolation  
  from **data-to-skill** / **meta-skill-synthesizer**.  
- Uses mode catalogue and auto-select discipline from **mmss-skill-boundary-combinator**  
  and **adaptive-open-skill-synthesizer** / **mmss-adaptive-sp-combinator**.  
- Uses evidence-aware formalisation and bounded meta-research from  
  **quantum-hyperloop-research-agent** and **quantum-meta-architect**.  
- Uses entity-identity, typed relations and delta tracking from  
  **mmss-mta-delta-architect**.  
- Uses mirrored-axis and hypergraph construction patterns from  
  **meta-hypergraph-ontology-alchemy** and **mmss-symmetric-meta-hypergraph-synthesis**.  
- Uses domain-specialist pattern from **mmss-domain-specialist-synthesizer**.  
- Uses lightweight inventory discipline from **skill-quick-sampler**.

The skill is a pure invariant extract and composition contract;  
it does not replace its parents.

## 11. Minimal Usage Examples

**M0**  
«Аудируй семейство listed parents и выдели, какие наблюдения являются good views одного и того же latent construction process.»

**M1**  
«Спроектируй минимальный unifier-контракт для mmss-principle-synthesis ⊕ adaptive-open-skill-synthesizer ⊕ mmss-mta-delta-architect.»

**M3**  
«Два SKILL.md получены из разных сессий. Это good views или bad views?»

**M4**  
«Два родителя сошлись up to rotation. Как получить unified skill одной линейной картой?»

**M5**  
«Добавь новый synthesizer X как observation channel, сохранив P1–P7.»

**M7**  
«Создай domain-specialist skill для [домен] под инвариантами этого unifier.»

---

End of skill contract.
