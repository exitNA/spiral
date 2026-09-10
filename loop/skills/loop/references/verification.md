# Verification and completion

## Verification scope

Select checks for the requested deliverable and risk. For non-software work, use source support, calculation reconciliation, artifact rendering, content coverage, or observed app state. For software, use the applicable checks below; this is not a requirement to run every kind on every task.

1. compiler/build/type/static checks;
2. deterministic unit/integration tests;
3. reproducible regression tests;
4. runtime/E2E/browser checks;
5. independent code/reliability/security review for substantial or materially risky work;
6. manual human judgment for genuinely subjective or externally consequential behavior.

Do not add tests that only mirror reversible low-impact changes. Complete required checks; repeat or broaden them only when new changes, failures, or unresolved concerns justify it.

## Requirement traceability

For every task, establish the mapping in its dedicated LOOP.md before execution and maintain it through final review, strictly following [../templates/LOOP.md](../templates/LOOP.md), including for small tasks. Link existing requirement matrices as baselines. Every original requirement and discovered in-scope gap must remain accounted for, conceptually:

| ID | Requirement / source | Acceptance condition | Implementation / deliverable | Verification evidence | Status |
| --- | --- | --- | --- | --- | --- |
| R1 | original requested outcome | observable pass condition | files or artifact section | actual result, evidence location and tested version | verified, or unresolved status |

Do not leave a requirement green only because code exists; verify its acceptance condition.

Use the dynamic work-list rules in [memory-compression.md](memory-compression.md). Work-item completion and requirement acceptance are separate judgments: finished implementation tasks may still need verification, and an all-done task list can still omit an original requirement. Each verified row must point to relevant observed evidence for the final artifact/version; command names, counts without context, and the implementer's claim alone do not establish acceptance.

Use pending, implemented-but-unverified, failed, blocked, or verified as appropriate. An exclusion needs its authorizing user instruction or evidence that it was never in scope. Preserve the original baseline when updating architecture, documentation, or test commands. A newly shortened checklist cannot retroactively satisfy omitted requirements.

## Regression-first repair

When a concrete failure is reproducible:

1. reproduce it;
2. create/fix a test or equivalent deterministic check when practical;
3. verify the old behavior fails;
4. implement the fix;
5. verify the new check passes;
6. run relevant existing regressions.

## Independent review

A reviewer should inspect the diff and requirements from a fresh role/context.

At final review, supply the original request, baseline requirements, explicit scope changes, final artifact/version, evidence map, and dynamic work list including retired-item reasons. The reviewer checks missing capabilities, lost coverage from cancelled/replaced work, and removed/weakened checks before code quality. Return uncovered IDs to an implementation owner, repair them, and recheck affected requirements. A read-only inventory completed before implementation is not final review.

Reviewer output should prioritize findings by severity and include concrete file/symbol references when possible.

Do not ask the reviewer merely "is this good?". Give a bounded review mission such as:

- find missed PRD requirements;
- find correctness bugs and test gaps;
- inspect auth/data integrity/security risks;
- inspect concurrency/race/migration edge cases.

## Completion gate

A substantial run is complete only when:

- all in-scope requirements have evidence;
- required deterministic checks pass;
- new failures found during the run are resolved or explicitly blocked;
- independent review has no unresolved blocking findings, or the unavailable-agent fallback below has been performed and its limitation disclosed;
- the final integrated state, not only individual worker branches, is verified.

Decide from the requirement map:

| Observed state | Required next action |
| --- | --- |
| In-scope capability missing, failed, or unverified; useful authorized work remains | Continue implementation or verification; assign the next action. |
| Every in-scope requirement has relevant final-state evidence and no blocking review finding remains | Deliver as complete. |
| Genuine external blocker after independent work is exhausted | Save evidence, remaining IDs, blocker, and next safe action; report blocked, not complete. |
| User cancels, an explicit budget/deadline ends, or an actual session boundary prevents continuation | Save an incomplete checkpoint and recovery instructions; do not redefine the goal. |

Before sending a final answer, compare any proposed "remaining work" with the original scope. Required work still actionable sends the loop back to execution. Optional enhancements outside that scope may be reported without extending the task. Never invent a time limit or request permission merely to continue already-authorized work.

For UI replacements, test user actions through the new UI and their visible results, persistence, and important error paths. Core tests establish core behavior; compilation establishes buildability. Neither alone verifies settings forms, querying/filtering, export, or platform interactions. If UI execution is unavailable, finish independently testable work and identify the unverified requirements and actual environmental limitation.

## No endless polish

Do not keep looping on stylistic preferences once correctness, requirements, tests, and maintainability are acceptable. Low-severity optional suggestions should be summarized rather than creating unbounded work.

## Lifecycle and production-quality checks

Before completion, also verify when applicable:

- **pre-production project:** no unnecessary compatibility shims, duplicate old/new implementations, obsolete adapters, or deprecated internal paths remain solely because older code existed;
- **production project:** real external clients, durable data, rolling-deploy constraints, and user-visible compatibility are preserved or deliberately migrated;
- **database:** migration decisions start from the latest applied durable migration state;
- **application/service:** console + plain-text file logging exists and file output contains no ANSI color controls (unless platform semantics make file logging inappropriate);
- **UI:** actual runtime result is checked at meaningful states/sizes and meets the active/current design-system and accessibility baseline.

Fast verification should happen throughout implementation; these final checks confirm the integrated state rather than replacing short feedback loops.

## Verifier integrity and failure classification

Choose the verifier before the change. Preserve the acceptance contract unless evidence shows it is wrong; explain material revisions instead of weakening a check to make a failing implementation pass.

Classify failures as implementation defects, incorrect requirements/models, verifier defects, environmental blockers, or flaky observations. Test the explanation and preserve diagnostics. A flaky pass does not establish a repair. For repeated local failures, reconsider the flow, contract, state representation, or architecture.

If independent agents are unavailable, use objective checks and a separate review pass, and disclose the limitation. For subjective acceptance, compare actual artifacts with the established project quality bar or obtain the needed human direction.

## Learning and continuity

Ethos integration is optional and does not gate delivery. When available, Ethos evaluates qualifying project-judgment candidates; when absent, complete the requested work without creating a pending integration requirement. A run need not produce knowledge changes. For a handoff, record the contract, current evidence, remaining uncertainty, and next safe action; telemetry alone is not a resumable task specification.
