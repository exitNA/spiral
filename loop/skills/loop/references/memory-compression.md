# State, learning, and compression

## Three different stores

| Store | Contents | Lifetime / owner |
| --- | --- | --- |
| Run state | Goal, current checkpoint, evidence pointers, failures, next action, blockers. | Resumable task state owned by Loop. |
| Execution learning | Proven test ordering, contention boundaries, useful decomposition, tooling improvements. | Compact process guidance in the narrowest existing project/tool authority. |
| Project judgment | Intent, mental model, taste, domain meaning, collaboration norms, consequential decisions. | Repository authorities reconciled by Ethos. |

## One document per user task

Every independent user task, including a small task, needs a dedicated persistent document before execution. Use `.loop/<task-id>/LOOP.md` in the project or task workspace. An explicitly designated task directory may change its location, but the filename must remain LOOP.md and its structure must follow the template; another task document cannot substitute for it. Without a repository, use the designated durable output/workspace directory. Keep one canonical document per task; shared project requirements may be linked as baselines but cannot replace the task's own record.

- Name each new task ID `YYYYMMDD-HHmmss-short-semantic-slug`, using the actual creation time in the user's configured timezone (UTC if unavailable) and a short, lowercase, hyphen-separated description of the objective, for example `20260906-161115-loop-completion`. Record the timezone and ISO creation time in the document. Allocate the directory without overwriting an existing one; if the same timestamp and slug collide, append `-02`, `-03`, etc. Keep the ID stable when the title changes or work resumes. Rename an existing ID only when the user requests a naming migration, updating references and recording the previous ID.
- Record the title, original request or source pointer, scope, acceptance criteria, status, evidence, remaining work, and next action. Record the conversation/task identifier when exposed by the host separately from the document ID; never invent one.
- A correction, clarification, added acceptance detail, retry, or cross-session resumption of the same objective updates the same document. Preserve the original request and separately record authorized changes. A new independent objective gets a new ID and document even in the same conversation. Link related or superseded tasks instead of overwriting them. Ask only when available context cannot resolve a materially consequential identity ambiguity.
- On continuation, resolve the explicit task ID/document pointer first, then check that the goal matches. Do not select a record merely because it is the newest or belongs to this repository. Carry the ID and document path in delegation briefs and handoffs.
- Subagents work under the parent task ID with bounded subtasks; their notes do not become competing top-level task documents. The orchestrator owns updates to the canonical record and serializes writes. Independent user tasks use separate directories, not a shared mutable `current.md`.
- Keep small records concise. Read and strictly follow [../templates/LOOP.md](../templates/LOOP.md): preserve section order, heading levels, fields, and list/table structure. Fill absent values with “none”, “not applicable”, or “pending verification” in the selected language. Write headings, labels, statuses, and prose in the user’s explicitly requested language, otherwise their established preference, otherwise the current conversation language (English only if none can be resolved). Preserve filenames, paths, stable IDs, and exact quotations. The template’s English is not an output-language preference. LOOP.md alone owns overall status, requirement statuses, work items, and the next action. An optional `STATE.md` in the same directory holds only technical recovery details, with the same task ID and the canonical revision it describes; link it from LOOP.md.
- Update status, requirement evidence, and next action at meaningful checkpoints and before completion or handoff. Retain completed records so later work cannot silently reuse their identity. Completion must agree with the verification gate.

Respect explicit no-write instructions and filesystem permissions. If the normal location is unwritable, use an already-authorized durable output location and record its path. If none exists, report that persistent task tracking is unavailable; do not claim a document was saved, broaden permissions solely for tracking, or violate a read-only request. Never store credentials or copy sensitive raw conversations; retain only necessary task content and safe source pointers. Check repository policy before versioning task records.

## Stable requirements, dynamic work

Keep the original request/baseline distinct from the agent's interpretation and later authorized changes. A scope change records its source, affected requirement IDs, and effect; a corrected inference records the authoritative evidence. Preserve enough original content or a durable versioned pointer to compare before and after. Shrinking work for convenience is not an authoritative correction.

Requirements describe outcomes and their acceptance conditions. Work items describe how to deliver or verify those outcomes. Keep both in the canonical document, using stable `R1` and `T1`-style IDs that are never reassigned. Every active requirement needs linked implementation and verification work, or existing relevant evidence that already satisfies it. Render work items as the template’s Markdown list, never a table; small tasks retain the same structure and fields.

Maintain the work list during execution:

- Add discovered in-scope work with its requirement IDs, action, done condition, dependencies, and status. Add owners only when useful for delegation.
- Split, merge, replace, or reorder work as evidence changes. Preserve retired IDs as superseded and link replacements that inherit their requirement coverage; update dependents to the active replacements. A retired item is not completed work and cannot satisfy a dependency merely by leaving the active list.
- Cancel an unnecessary item with a reason and the replacement/evidence satisfying its requirements. Cancelling work that removes an outcome requires an authorized scope-change reference. Retain excluded requirements with their justification rather than deleting them.
- On failed verification, mark the affected requirement failed and reopen or add repair and verification work. When an artifact changes after verification, reassess affected evidence and mark it unverified until the necessary checks pass for the new version; unchanged valid evidence may be reused with its scope made explicit.
- Mark a work item done only when its own done condition has evidence. Completing implementation does not automatically verify its requirement. Before delivery, apply [verification.md](verification.md) to the original requirements, current evidence, and unresolved work. A fully checked work list is not sufficient by itself.

At checkpoints, reconcile both directions: each active requirement has work or valid evidence, and each active work item serves a requirement or a necessary delivery constraint. Preserve meaningful adjustment reasons in the work items; do not accumulate a transcript of routine status changes. Keep overall blockers and next action in the current-execution section and final evidence in the completion/handoff section.

## Show the work list in Codex

LOOP.md remains the sole task authority; the user-visible checklist is a projection, not another task document. After creating or resuming the record, and after meaningful changes to work, status, scope, blockers, dependencies, or the next action, save LOOP.md first and refresh the visible projection in the same checkpoint. Only the orchestrator publishes updates. Reconcile user corrections into the canonical record before projecting them. Resolve the native tool and its live schema through [codex-runtime.md](codex-runtime.md); keep host-version mechanics there rather than duplicating them here.

- Publish every active work item and every completed item from the current execution. Each displayed step must contain its T ID, requirement IDs, localized action title, and dependency T IDs (or localized “none”). Keep retired history in LOOP.md rather than presenting it as completed work.
- State the canonical `Next action (work-item ID)` explicitly in every update explanation. While work is active, that item is also the sole `in_progress` entry. When the task has no runnable next action, use no `in_progress` entry and state the blocked, complete, cancelled, or exhausted next-action condition in the explanation.
- Put overall blockers and changes that cannot be represented as item status in the same update explanation. If grouping is required by a host limit, the displayed step must list every member T ID and requirement ID; include the union of their unresolved dependencies, and mark the group complete only when every member is done.
- Map `done` to the native completed state and map pending/in_progress to their native equivalents. If the host lacks a blocked state, keep blocked work pending and include a localized blocked label and reason in its step. Remove cancelled/superseded items from active steps, explain their replacement or authorized exclusion in the update explanation, and retain them in LOOP.md. Never mark retired work completed to improve the progress indicator. A failed check reopens affected display items after updating canonical evidence.
- Provide a clickable absolute link to LOOP.md on first publication, resumption, and handoff for detailed cross-checking. Opening or linking the document is supplementary; it does not satisfy native checklist publication.
- If native publication is unavailable or fails after the runtime procedure is exhausted, preserve LOOP.md and report that synchronization is blocked/unverified. A prose update, Markdown checkbox list, document panel, or custom HTML view is not an equivalent replacement. Continue independently executable authorized work.
- Before handoff, compare the latest successful native-tool submission and result with LOOP.md in both directions: item IDs, requirement coverage, dependencies, statuses, blockers, retired-item explanations, and next action. Repair stale or missing projection data. Keep display verification separate from product acceptance; document edits alone do not establish native synchronization.

## Resume with fresh context

Read the identified canonical task document first, then its recovery snapshot if needed. Before continuing an older record, align it to the current LOOP.md template and selected language while preserving its task ID, original sources, changes, evidence, and retired work. If the old record has another filename, migrate its content to LOOP.md and leave a pointer at the old location; maintain only one active authority. Verify that the task ID, goal, snapshot revision, checkout, and observed behavior still match. Reconcile intervening human instructions and actual changes in LOOP.md before resuming writes; an older snapshot cannot select the next action or declare completion.

At a session or context boundary, save a checkpoint before handing off. Do not repeatedly inject full conversations or raw logs. A fresh agent should recover the goal, active hypothesis, evidence, and next safe action without replaying the whole history.

## Promote selectively

Prefer a regression test, explicit contract, or tooling correction over a prose reminder when the behavior is machine-checkable. Promote execution lessons when repeated, strongly evidenced, or needed to prevent a serious recurring defect. One incidental failure is not a universal rule.

When Ethos is available, pass qualifying project-judgment candidates to it:

- the observation and evidence location;
- the existing authority and judgment it may change;
- the proposed scope and whether the human made it explicit;
- uncertainty or conflicts that still need resolution.

Ethos integrates the current model in place. Loop keeps only the handoff status and evidence pointer, not a competing copy of doctrine. If Ethos is unavailable, skip this optional integration; its absence creates no pending work or delivery blocker.

## Compress at meaningful boundaries

After verified learning, on repeated rule growth, and before a session handoff:

1. Merge duplicate findings and keep one authoritative meaning.
2. Replace superseded guidance with the current supported rule.
3. Retain the evidence or decision rationale needed to audit a consequential choice.
4. Remove stale task status and irrelevant detail from active context.
5. Recheck contradictions, paths, and representative regression cases when executable behavior changed.

Keep detailed evidence separate and retrieve it on demand. Do not persist secrets, raw private conversations, or speculative conclusions as durable knowledge. Compression is semantic reconciliation, not indiscriminate deletion of history or tests.
