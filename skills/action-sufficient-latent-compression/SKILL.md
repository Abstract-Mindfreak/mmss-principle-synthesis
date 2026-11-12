---
name: action-sufficient-latent-compression
description: >
  Compresses long, noisy tool observations into a fixed block of continuous latent tokens
  that preserve decision-critical information for the agent's next action. Trains and applies
  a context-aware encoder + latent adapter against a frozen target agent using
  action-preserving loss (KL divergence on next-action distributions + cross-entropy).
  Rejects text reconstruction as the primary success criterion. Enables 70–89% token reduction
  and significant runtime savings while keeping the main agent frozen. Use when an agent
  must handle multi-step tool use without context explosion, or when continuous latent
  representations are preferred over discrete text summaries. Triggers include latent
  compression, action-preserving tokens, Coca-Cola-style observation bottleneck,
  continuous latent tokens for agents, tool observation compression.
metadata:
  version: "0.1.0"
  maturity: test_candidate
  parents:
    - mmss-principle-synthesis
    - data-to-skill
    - jepa-platonic-mmss-meta-unifier
    - mmss-skill-boundary-combinator
    - mmss-adaptive-sp-combinator
    - mmss-jepa-compaction-monolithic
  default_output: latent_tokens_or_contract
  default_language: user_language
  boundary_identity: mandatory
  source_lineage:
    - "arXiv:2611.06500 (Tools Need Not Speak in Text: Latent Context Compression for Agents, Tsinghua AI Agent Group, 2026-11-04)"
    - "User-supplied screenshots of architecture, loss, insertion protocol and comparison tables"
    - "Projected invariants only; no claim of re-implementation of original training or empirical results"
  invariant: P_ACTION_SUFFICIENCY
---

# Action-Sufficient Latent Compression

## 1. Purpose and Scope

Provide a reusable, provenance-preserving skill that turns long tool observations into a compact continuous latent representation judged solely by its ability to support the correct next action of a frozen agent.

The skill does **not**:
- train or modify the target agent policy;
- claim to reconstruct the original observation;
- guarantee that every fact useful for a future (non-next) decision is retained;
- produce human-readable summaries by default.

It does:
- keep the main agent frozen;
- enforce action-sufficiency as the sole training / evaluation criterion;
- expose explicit boundary markers and insertion protocol;
- preserve the known limitations (auditability, possible loss of later-needed facts).

S and P remain open. Any tool observation, agent trajectory, or compression policy may occupy the role of S or P.

## 2. Core Invariant (mandatory)

**P_ACTION_SUFFICIENCY**

A compressed representation \(z_t\) is valid if and only if the next-action distribution of the frozen target agent under the compressed input stays sufficiently close to the distribution under the full observation.

Formally the training objective is:

\[
L = \lambda_{KL}\, D_{KL}(p_{\text{full}} \,\|\, p_{\text{latent}}) + \lambda_{CE}\, \text{CE}(y_{t+1}, p_{\text{latent}})
\]

where both paths share the identical frozen target agent \(p_\psi\).

Any entity that crosses a representation boundary (raw observation → latent tokens → agent embedding space) must be carried as the triple `(value, convention, context)`.

- Convert only via an explicit mapping (encoder + adapter).
- Never silently collapse status, provenance or decision-criticality.
- Context (task instruction \(q\) + current reasoning trajectory \(r_t / h_t\)) is never omitted from the conditioning.

## 3. Architecture Contract

### 3.1 Components

| Component              | Role                                                                 | Trainable |
|------------------------|----------------------------------------------------------------------|-----------|
| Context-Aware Encoder \(C_\theta\) | Reads \(q\), \(r_t\), \(o_t\) and produces hidden states             | Yes      |
| Latent Adapter \(A_\phi\)         | Maps hidden states into fixed-size continuous tokens \(z_t \in \mathbb{R}^{m \times d}\) | Yes |
| Target Agent \(p_\psi\)           | Frozen LLM agent that consumes either full observation or latent tokens | No       |

Default \(m = 128\). \(d\) matches the target agent’s input embedding dimension.

### 3.2 Insertion Protocol

The latent tokens are inserted into the agent’s input embedding sequence with special boundary markers:

\[
X_t = \bigl[ E_\psi(q, h_t);\ E_\psi(\langle\text{latent\_obs}\rangle);\ z_t;\ E_\psi(\langle/\text{latent\_obs}\rangle) \bigr]
\]

where \(E_\psi\) is the target agent’s embedding function.

### 3.3 Inputs / Outputs

**Required inputs**
- `q` — task instruction
- `r_t` / `h_t` — current reasoning trajectory / history
- `o_t` — raw tool observation (text or structured)

**Outputs**
- `z_t` — continuous latent token block of shape \(m \times d\)
- optional diagnostic: estimated action-distribution divergence, compression ratio

**Failure modes (must be surfaced)**
- Insufficient decision-critical information retained → high KL / CE residual
- Target agent embedding dimension mismatch
- Observation too short to justify compression (policy may fall back to text)

## 4. Working Modes

### Mode A — Inference only (default for most users)
Agent calls the skill with `(q, r_t, o_t)` and receives ready-to-insert `z_t`. No training occurs.

### Mode B — Action-preserving training
Given a dataset of trajectories that already contain the correct next action \(y_{t+1}\), update only \(C_\theta\) and \(A_\phi\) under the loss in Section 2 while keeping \(p_\psi\) frozen. Supports LoRA on the encoder/adapter.

### Mode C — Audit / mixed mode
Produces both latent tokens and a short human-readable “decision-critical clues” summary. Used when the human requests explainability or when the next decision is high-stakes.

### Mode D — Adaptive policy
Higher-level orchestration decides, for each tool call, whether to compress, keep full text, or use mixed representation, based on remaining context budget, estimated criticality, and audit requirements.

## 5. Interaction Contract (how an agent should call the skill)

```text
skill.call(
  name = "action-sufficient-latent-compression",
  mode = "inference" | "train" | "audit" | "adaptive",
  inputs = {
    "q": <task string>,
    "reasoning_trajectory": <current r_t or h_t>,
    "tool_observation": <raw o_t>,
    "m": 128,                     # optional
    "return_diagnostics": false   # optional
  }
)
```

Expected return:
```text
{
  "latent_tokens": <tensor or serialised block>,
  "insertion_markers": ["<latent_obs>", "</latent_obs>"],
  "diagnostics": { ... } | null,
  "status": "ok" | "fallback_to_text" | "insufficient_signal"
}
```

The calling agent is responsible for:
- inserting the tokens correctly into its own embedding stream;
- deciding whether to fall back to text when status ≠ "ok";
- never treating the latent block as human-readable text.

## 6. Known Limits and Honesty Rules

1. **Auditability** — latent tokens are not directly readable. Prefer Mode C when a human must understand what was kept.
2. **Future decisions** — the representation is optimised only for the *immediate* next action. Facts needed many steps later may be discarded.
3. **Task specificity** — the compressor is normally trained or adapted per domain / tool family. Zero-shot transfer is not guaranteed.
4. **No fabrication** — the skill never invents observations, actions or performance numbers. All quantitative claims must carry provenance (paper, local experiment, or “not measured”).
5. **Boundary identity** — raw observation, latent tokens and agent embedding live in different conventions. Crossing always requires an explicit map.

## 7. Relationship to Parent Skills

- Inherits provenance, epistemic distinction and minimum-sufficiency rules from **mmss-principle-synthesis**.
- Uses selective principle extraction and robust-kernel isolation from **data-to-skill**.
- Treats continuous latent tokens as a deformation-stable representation under the **jepa-platonic-mmss-meta-unifier** kernel.
- Can be combined with other skills via **mmss-skill-boundary-combinator** / **mmss-adaptive-sp-combinator**.
- Compatible with long-session compaction via **mmss-jepa-compaction-monolithic** (latent tokens may themselves become the compacted state).

## 8. Installation Notes

- Place this file at  
  `/home/workdir/.grok/skills/action-sufficient-latent-compression/SKILL.md`
- No additional runtime, model weights or external services are required by the skill definition itself.
- Actual encoder/adapter weights (if used in Mode B) are external artefacts and must be supplied or trained by the host environment.
- The skill is ready for registration once the front-matter validates and the directory is present.

## 9. Provenance Statement

All architectural elements, loss formulation, insertion protocol and quantitative ranges (70–89 % token reduction, 24–56 % runtime) are taken from or directly projected from:

- arXiv:2611.06500v1 (Yuetong Liu et al., Tsinghua AI Agent Group, submitted 4 Nov 2026)
- User-provided screenshots of Figure 1, Figure 2, loss equation, latent insertion equation and comparison tables.

No original experimental results of the paper are re-claimed. Local performance must be measured independently.
