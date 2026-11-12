---
name: mmss-reopen-the-problem
description: >
  Reopens the problem hidden behind a familiar object, method, or
  implementation. Separates intent and constraints from inherited form,
  develops distinct mechanisms, and compares them against the existing
  solution.
metadata:
  version: "0.1.3"
  status: draft-unvalidated
  maturity: draft-unvalidated
  default_language: user_language
  changelog:
    - "0.1.1: Added Problem-Framing Check, Mechanisms Before Familiar Categories, Verification Status, No Forced Winner"
    - "0.1.2: Added Renaming Is Not Reopening, Comparable Candidate Depth, Functional Closure Check, Continue with Available Checks"
    - "0.1.3: Added Evidence-to-Claim Fit; clarified 'baseline provisionally retained'"
---
# MMSS · Reopen the Problem
## 1. Purpose
A familiar solution must not automatically define the boundaries
of an investigation.
When given the name of an object, method, or system, temporarily
suspend the necessity of its conventional form. Recover the underlying
need, required functions, constraints, and possible mechanisms.
Then bring the existing solution back into the comparison:
as a candidate with strengths and limitations, not as a form
that determines the answer in advance.
Core principle:
> The existence of a solution is not a reason to stop investigating.
> It is also not a reason to replace that solution.
Do not claim to have literally forgotten knowledge.
Change the problem-framing and selection procedure;
do not pretend to erase memory.
### Language behavior
Use the user's language for responses, questions, explanations,
and user-facing deliverables unless the user requests otherwise.
Preserve code identifiers, schema keys, quoted source text,
and technical names when translation would change their meaning.
## 2. When to Apply
Use this skill when the task requires:
- Designing a new system.
- Reconsidering an existing architecture.
- Finding an alternative to a familiar mechanism.
- Determining which components are genuinely necessary.
- Moving beyond cosmetic improvements.
- Checking whether an object's name predetermines the answer.
Do not automatically run the full procedure:
- For a precise operation under a fixed contract.
- For a straightforward repair with an established cause.
- When the user requires the architecture to remain unchanged.
- When reframing would exceed the authorized scope.
In these cases, use a brief assumption check without reopening
the entire problem.
## 3. Input and Expected Output
Input:
- The user's request.
- A familiar object or existing implementation.
- The context of use.
- Mandatory constraints.
- Available evidence and means of verification.
Expected output:
- A recovered problem statement.
- A map of requirements and assumptions.
- Several substantively different mechanisms.
- Testable candidates.
- A comparison against the baseline.
- A justified choice.
- Uncertainties and conditions for reconsideration.
Do not require the user to complete a template
when the necessary information is already available in context.
## 4. Invariants
1. Do not substitute another goal for the user's intent.
2. Do not present an assumption as a requirement.
3. Do not discard established facts for the sake of originality.
4. Unusualness is not evidence of usefulness.
5. Internal consistency does not replace external verification.
6. Semantic similarity does not establish functional interchangeability.
7. Do not hide trade-offs behind a high aggregate score.
8. Match every conclusion to the verification actually performed.
9. This skill does not expand permissions for tools, spending,
   data modification, or external actions.
## 5. Depth of Application
Choose the minimum sufficient depth.
### Brief Pass
For a local decision:
- Identify the need.
- Identify one consequential assumption.
- Consider an alternative mechanism.
- Check it against the baseline.
### Standard Pass
For design work:
- Map constraints.
- Develop two to four distinct mechanisms.
- Perform minimal meaningful checks.
- Compare and choose.
### Extended Pass
For substantial reconsideration:
- Explore multiple problem formulations.
- Select investigation routes.
- Build prototypes.
- Test counterexamples.
- Analyze trade-offs.
- Define activation and rollback conditions.
Do not increase depth merely to demonstrate use of the skill.
### Comparable Candidate Depth
In a Standard or Extended Pass, develop the baseline
and at least one materially different candidate
to comparable functional depth.
Do not fully specify the baseline while leaving alternatives
as category names or brief possibilities.
A material difference changes how a consequential function
is performed, allocated, or controlled.
It does not require historical novelty.
If no alternative can be developed within the budget,
report that limitation explicitly.
## 6. Procedure
### Step 1. Preserve Intent
Recover:
- Who receives the result.
- What effect is needed.
- Under which conditions.
- What counts as success.
- What must not change.
Separate explicit statements from your interpretation.
If several materially different goals are plausible,
do not silently choose one.
Ask a specific question when necessary.
When safe progress is possible, state the working assumption
and continue.
### Step 2. Separate the Name from the Problem
Restate the request without requiring the familiar solution's name.
Example:
“Create a bicycle.”
→
“Enable a person to move in a controlled way through a specified
environment under defined constraints.”
This is a working formulation, not a final truth.
Check whether it has omitted sport, cargo transport,
rehabilitation, or another intended purpose.
### Step 3. Map Constraints and Assumptions
Assign statuses to consequential statements:
- `explicit_requirement`:
  Explicitly specified by the user.
- `verified_constraint`:
  Supported by applicable evidence.
- `working_assumption`:
  Provisionally accepted to enable progress.
- `inherited_form`:
  Carried over from a familiar solution.
- `unknown`:
  Requires clarification or verification.
An item may change status as evidence becomes available.
Do not reduce everything to a binary distinction
between “constraint” and “not a constraint.”
### Problem-Framing Check
Do not silently import the familiar solution's typical use case
into the recovered problem.
“Not specified otherwise” does not make a condition
an explicit requirement.
A plausible condition is a working assumption
until its status is established.
Do not label a statement as verified merely because
it seems necessary, sensible, or conventional.
Before proceeding, ask:
> Would I have selected these conditions and criteria
> if the familiar solution's name had not been provided?
If the recovered problem strongly favors the baseline,
check whether this follows from the user's intent
or from inherited assumptions.
For an underspecified request, present a small number
of materially different framings or explicitly choose
one provisional framing.
### Step 4. Examine the Origin of an Assumption
For a questionable component or rule, ask:
1. Where did it come from?
2. Which need does it serve?
3. Is it a required outcome or one way of producing that outcome?
4. What would fail if it were removed?
5. Could another mechanism perform the function?
6. How could its necessity be tested?
Counterfactual question:
> If the familiar implementation did not exist,
> would this requirement follow from the problem itself?
The answer motivates investigation.
It does not prove feasibility.
### Step 5. Recover Functions
Describe the necessary effects without prematurely assigning
conventional components.
Distinguish:
- Function.
- Mechanism.
- Component.
- Interface.
- Control rule.
- Verification method.
Example:
“Provide controlled stopping” is not equivalent to
“install a particular type of brake.”
### Mechanisms Before Familiar Categories
Do not substitute a list of familiar product categories
for mechanism-level exploration.
For the most consequential functions:
1. Identify alternative ways to produce the required effect.
2. Check which mechanisms can work together.
3. Assemble at least one candidate from those choices.
Existing products may be used as references,
but their names must not replace the explanation
of how the candidate works.
A recombination is not automatically novel,
feasible, or useful.
### Renaming Is Not Reopening
Replacing familiar component names with abstract descriptions
does not by itself demonstrate independent construction.
For consequential design choices, identify whether they are:
- derived from the selected requirements;
- adopted provisionally;
- borrowed from the baseline;
- selected through comparison.
A candidate may reproduce the baseline.
Do not claim independent derivation unless the presented
grounds support that claim.
### Step 6. Open Distinct Investigation Routes
Choose a limited number of directions:
- Replace the mechanism.
- Change the system boundary.
- Redistribute a function.
- Change the sequence of actions.
- Change the interaction with the user.
- Remove an assumption.
- Split a monolithic function.
- Combine unnecessarily separated functions.
Each route must differ in how it produces the result,
not merely in its name.
For each route, state:
- What changes.
- What remains unchanged.
- The expected advantage.
- The main risk.
- The required check.
Do not generate alternatives merely to increase their count.
### Step 7. Materialize Candidates
Create a minimal testable representation
of each promising candidate:
- An input/output example.
- A diagram.
- A prototype.
- An algorithm.
- A calculation.
- A test.
- An interaction scenario.
Before testing, specify:
- The expected result.
- A failure indicator.
- A consequential counterexample.
Distinguish:
- Concept.
- Simulation.
- Fixture.
- Working implementation.
- Verification in the real environment.
### Functional Closure Check
For every required output, identify the mechanism
that is expected to produce it.
Mark missing mechanisms and unresolved interfaces.
Do not claim a function is provided merely because
it appears in the output description.
Check candidate coherence before ranking candidates.
### Verification Status
A proposed test is not a performed test.
Label consequential claims as appropriate:
- assumption;
- hypothesis;
- supported expectation;
- observed result;
- unresolved.
Do not fill comparison cells with unsupported ratings
merely to complete a table.
When candidates differ in energy source, operating conditions,
or mandatory constraints, make that difference explicit.
Do not present them as directly equivalent alternatives
without justification.
### Evidence-to-Claim Fit
For each consequential conclusion, state:
- the claim;
- the evidence or check;
- the assumptions required;
- what the check establishes;
- what remains unestablished.
A correct intermediate result does not validate
every conclusion that follows it.
Do not infer:
- comparative superiority from feasibility;
- power sufficiency from force alone;
- functional adequacy from naming a mechanism;
- successful comparison from listing differences.
If the evidence supports a narrower claim,
narrow the conclusion instead of strengthening
the language around the evidence.
### Continue with Available Checks
A physical prototype is not required for every useful check.
Use the strongest applicable verification available:
- contract and consistency checks;
- mechanism tracing;
- calculations;
- simulations;
- source-backed comparisons;
- empirical tests.
State what each check establishes and what it does not.
Lack of empirical testing does not make every claim unsupported.
Conversely, a plausible explanation does not establish
real-world performance.
Do not stop solely because no winner can yet be selected.
Complete the bounded investigation when useful authorized
checks remain available.
### Step 8. Restore the Baseline
Compare the candidates and the existing solution
under the same criteria and conditions.
Assess separately:
- Compliance with mandatory constraints.
- Usefulness.
- Complexity.
- Cost.
- Testability.
- Risks.
- Reversibility.
- Uncertainty.
Do not introduce a convenient criterion after the fact
to make the preferred candidate win.
If the baseline remains preferable, retain it
and explain the grounds for that choice.
### Step 9. Classify Disagreements
Distinguish:
- Factual contradiction.
- Interface incompatibility.
- Competing objectives.
- Different preferences.
- Insufficient evidence.
- Useful diversity of hypotheses.
Possible responses include:
- Verify.
- Transform.
- Reject.
- Clarify.
- Expose the trade-off.
- Preserve alternatives.
Do not eliminate differences merely to produce
one confident answer.
### Step 10. Conclude the Choice
State:
- The selected candidate.
- Which baseline elements were retained.
- Which elements changed.
- The grounds for the choice.
- The checks performed.
- The claims not yet verified.
- The conditions that would change the decision.
Do not claim final perfection, proven optimality,
or exhaustive exploration without sufficient grounds.
### No Forced Winner
The procedure may end without selecting a winner.
Possible outcomes include:
- retain the baseline with verified grounds;
- select an alternative with verified grounds;
- retain the baseline provisionally;
- preserve multiple candidates;
- revise the problem framing;
- stop because evidence is insufficient.
`baseline provisionally retained` means the baseline
remains the working reference pending further evidence.
It does not mean that superiority has been established.
State what was actually achieved.
Do not claim that the familiar solution has been
“rediscovered” merely because it remains the default
after an untested comparison.
## 7. Protection Against False Progress
Do not treat the following as success by themselves:
- The number of alternatives.
- The number of documents.
- Terminological complexity.
- A high internal score.
- The absence of objections.
- Passing only a self-selected example.
Ask:
> Can the metric improve while the original problem remains?
If so, introduce an independent criterion
or narrow the conclusion.
## 8. Stopping Conditions
Finish the pass when:
- Mandatory requirements are satisfied.
- Consequential alternatives have been considered
  within the selected budget.
- Verification is sufficient for the current decision.
- Further investigation is not justified
  by its expected benefit.
Stop with an explicit limitation when:
- A necessary check is unavailable.
- Available evidence cannot distinguish the candidates.
- A required action is not authorized.
- The investigation would exceed the budget.
Do not continue recursively merely because
another question can be asked.
## 9. Response Format
By default, present:
1. Recovered problem.
2. What is mandatory and what was assumed.
3. Distinct mechanisms.
4. Checks and results.
5. Comparison with the baseline.
6. Decision and conditions for reconsideration.
Shorten the format for simple tasks.
Do not present a lengthy private deliberation transcript.
Present decision grounds, evidence, results, and limitations.
## 10. Minimal Example
Input:
“A node-based automation editor is needed.”
Implicit assumption:
Every operation must be a separate, permanently visible node.
Recovered need:
Create, understand, execute, and verify data processing.
Functions:
Configure operations, connect data,
observe execution, and correct errors.
Candidates:
- A graph.
- A sequential list with branches.
- An operation table.
- A hybrid of graph, inspector, and timeline.
Check:
The user builds the same linear and branching scenarios,
locates an error source, changes a binding,
and verifies the result.
Possible conclusion:
Retain the graph for connection structure,
move configuration into an inspector,
and place time-based projection on a timeline.
This is not a prescribed answer.
It must follow from the actual checks.
## 11. Initial Evaluation Cases
Before treating this skill as validated,
evaluate it on at least these different task types:
### Case A. Reinvent a Familiar Object
Example:
“Reinvent the bicycle.”
Check whether the procedure can move beyond
conventional components without losing the intended purpose.
### Case B. Reconsider a Real Design
Example:
Revisit one bounded part of an automation editor.
Check whether the procedure produces
a practical, testable alternative rather than a renaming exercise.
### Case C. Repair a Known Defect
Example:
Fix a small bug with an established cause.
Check whether the skill selects a brief pass
instead of expanding the task unnecessarily.
These are proposed evaluation cases,
not evidence that the skill has already passed them.
## 12. Core Statement
> A familiar solution is neither a prohibition against investigation
> nor a reason for mandatory replacement.
> It is a candidate whose foundations can be examined again.
