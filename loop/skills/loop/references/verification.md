# Verification and completion

## Evidence hierarchy

1. compiler/build/type/static checks;
2. deterministic unit/integration tests;
3. reproducible regression tests;
4. runtime/E2E/browser checks;
5. independent code/reliability/security review;
6. manual human judgment for genuinely subjective or externally consequential behavior.

## PRD traceability

Every requirement should end with an evidence mapping, conceptually:

| Requirement | Implementation | Verification | Status |
|---|---|---|---|
| R1 | files/modules | tests/checks | pass |

Do not leave a requirement green only because code exists; verify its acceptance condition.

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
- independent review has no unresolved blocking findings;
- the final integrated state, not only individual worker branches, is verified.

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

Before completion, qualifying project-judgment candidates must be reconciled through Ethos or explicitly marked pending. A run need not produce knowledge changes. For a handoff, record the contract, current evidence, remaining uncertainty, and next safe action; telemetry alone is not a resumable task specification.
