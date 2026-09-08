# Task title

<!-- Instantiate as LOOP.md. Preserve this section order, heading levels, fields, and list/table structure. Translate headings, field labels, statuses, and prose into the user’s language: explicit instruction, then established preference, then current conversation language. Keep filenames, paths, IDs, and exact quotations unchanged. Fill absent values with localized “none”, “not applicable”, or “pending verification”; remove these instructional comments in the task document. -->

## Task identity

<!-- Task ID value format: YYYYMMDD-HHmmss-short-semantic-slug. Created and Updated use the current environment's local time in ISO 8601 format with its UTC offset. Keep Created unchanged; refresh Updated when the task record meaningfully changes. -->

- Task ID:
- Created:
- Updated:
- Conversation identifier or source pointer, when available:
- Related / superseded task IDs, if any:

## Original objective and scope

- Original user request or durable source pointer:
- Agent's interpretation of the observable outcome:
- In-scope surfaces and explicit exclusions:
- Original behavior / acceptance baseline and its location:
- Relevant instructions, constraints, and user-specified budget/deadline:
- Allowed actions and remaining authorization boundaries:

## Authorized changes

Preserve the original baseline separately. If there are no changes, retain this section and record “none”.

| Change ID / date | User instruction or authoritative correction evidence | Change and affected requirement IDs |
| --- | --- | --- |

## Requirements and acceptance

| ID | Requirement / source | Acceptance condition | Implementation / deliverable | Verification evidence | Status |
| --- | --- | --- | --- | --- | --- |

Evidence identifies the observed result, location, and tested artifact/version; a command without its result is not evidence. Requirement statuses: pending / implemented-but-unverified / failed / blocked / verified / excluded (with justification).

## Current execution

- Overall status: active / blocked / complete / cancelled / budget exhausted
- Current phase / checkpoint:
- Blockers, if any:
- Next action (work-item ID):
- Mode and scheduling contract, only when relevant:

### Dynamic work list

- T1 — Action and done condition:
  - Requirement IDs:
  - Dependencies:
  - Status:
  - Result / change reason:
  - Owner (if delegated; otherwise not applicable):

After saving, publish this list through Codex’s native plan/checklist tool; follow ../references/memory-compression.md. Each projected item includes its T ID, requirement IDs, dependencies, and status; the sole active item matches “Next action”, and every update explanation names that next-action ID or its terminal/blocked condition together with blockers and retired-item changes. Record unavailable or failed native synchronization in blockers and handoff; conversation checkboxes and file panels do not satisfy this obligation. The native display is not a second authority.

Repeat this list item for each work item; never render the dynamic work list as a table. Work statuses: pending / in_progress / blocked / done / superseded / cancelled (localize display values). Keep implementation and verification work distinguishable. Retain superseded/cancelled IDs with their reason and replacement IDs or scope-change reference. Small tasks use the same fields and structure.

## Completion or handoff

- Delivered artifact / final version:
- Requirement evidence and final review conclusion:
- Outstanding requirement/work IDs, or none:
- Reason for completion, blockage, cancellation, budget exhaustion, or handoff:
- Recovery snapshot / baseline location, if needed:

For migrations, link the workflow-parity baseline and verified recovery copy. Add a separate STATE.md only for technical recovery details; overall status, requirements, work list, and next action remain authoritative here. Retain all template sections and fields, including for small tasks; fill irrelevant values with “not applicable”.
