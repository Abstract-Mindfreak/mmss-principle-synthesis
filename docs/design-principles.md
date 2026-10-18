# Design principles

The skill favors the minimum sufficient architecture: each component should have a necessary responsibility, interface, validation role, or integration boundary. Extra modules and labels do not establish quality.

Keep source material separate from synthesis. Identify whether key elements come from source observations, user requirements, inferences, or explicit design rationale; do not attribute agent-designed structures to source authors.

Record the provenance of important claims and the basis on which they were checked. A planned check is not an executed check, and an executed check supports only the properties and scope it actually examined.

Distinguish local behavior from general properties. A result for one input or system path does not establish a universal invariant. State relevant conditions, boundaries, and unknowns.

Define explicit interfaces: inputs, behavior, outputs, constraints, dependencies, and failure handling. A label alone does not define a contract.

Report specification, implementation, execution, and deployment as separate states. Keep partial, failed, unknown, and unchecked states visible; do not imply that a declarative artifact runs by itself.
