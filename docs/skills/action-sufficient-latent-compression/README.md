# Action Sufficient Latent Compression

<p align="center"><img src="action-sufficient-latent-compression-icon.svg" width="128" height="128" alt="Action Sufficient Latent Compression"></p>


Compresses long, noisy tool observations into a fixed block of continuous latent tokens that preserve decision-critical information for the agent's next action. Trains and applies a context-aware encoder + latent adapter against a frozen target agent using action-preserving loss (KL divergence on next-action distributions + cross-entropy). Rejects text reconstruction as the primary success criterion. Enables 70–89% token reduction and significant runtime savings while keeping the main agent frozen. Use when an agent must handle multi-step tool use without context explosion, or when continuous latent representations are preferred over discrete text summaries. Triggers include latent compression, action-preserving tokens, Coca-Cola-style observation bottleneck, continuous latent tokens for agents, tool observation compression.

## Skill file

[`SKILL.md`](../../../skills/action-sufficient-latent-compression/SKILL.md) contains the complete instructions.
