# State, learning, and compression

## Three different stores

| Store | Contents | Lifetime / owner |
| --- | --- | --- |
| Run state | Goal, current checkpoint, evidence pointers, failures, next action, blockers. | Resumable task state owned by Loop. |
| Execution learning | Proven test ordering, contention boundaries, useful decomposition, tooling improvements. | Compact process guidance in the narrowest existing project/tool authority. |
| Project judgment | Intent, mental model, taste, domain meaning, collaboration norms, consequential decisions. | Repository authorities reconciled by Ethos. |

## One document per user task

Every independent user task, including a small task, needs a dedicated persistent document before execution. Use an existing task-document convention when available; otherwise use `.loop/<task-id>/LOOP.md` in the project or task workspace. Without a repository, use the designated durable output/workspace directory. Keep one canonical document per task; shared project requirements may be linked as baselines but cannot replace the task's own record.

- Name each new task ID `YYYYMMDD-HHmmss-short-semantic-slug`, using the actual creation time in the user's configured timezone (UTC if unavailable) and a short, lowercase, hyphen-separated description of the objective, for example `20260906-161115-loop-completion`. Record the timezone and ISO creation time in the document. Allocate the directory without overwriting an existing one; if the same timestamp and slug collide, append `-02`, `-03`, etc. Keep the ID stable when the title changes or work resumes. Rename an existing ID only when the user requests a naming migration, updating references and recording the previous ID.
- Record the title, original request or source pointer, scope, acceptance criteria, status, evidence, remaining work, and next action. Record the conversation/task identifier when exposed by the host separately from the document ID; never invent one.
- A correction, clarification, added acceptance detail, retry, or cross-session resumption of the same objective updates the same document. Preserve the original request and separately record authorized changes. A new independent objective gets a new ID and document even in the same conversation. Link related or superseded tasks instead of overwriting them. Ask only when available context cannot resolve a materially consequential identity ambiguity.
- On continuation, resolve the explicit task ID/document pointer first, then check that the goal matches. Do not select a record merely because it is the newest or belongs to this repository. Carry the ID and document path in delegation briefs and handoffs.
- Subagents work under the parent task ID with bounded subtasks; their notes do not become competing top-level task documents. The orchestrator owns updates to the canonical record and serializes writes. Independent user tasks use separate directories, not a shared mutable `current.md`.
- Keep small records concise. Use [../templates/LOOP.md](../templates/LOOP.md) as a shape and omit irrelevant sections. A separate `STATE.md` is optional; if used, keep it in the same directory with the same task ID and link it from the canonical document.
- Update status, requirement evidence, and next action at meaningful checkpoints and before completion or handoff. Retain completed records so later work cannot silently reuse their identity. Completion must agree with the verification gate.

Respect explicit no-write instructions and filesystem permissions. If the normal location is unwritable, use an already-authorized durable output location and record its path. If none exists, report that persistent task tracking is unavailable; do not claim a document was saved, broaden permissions solely for tracking, or violate a read-only request. Never store credentials or copy sensitive raw conversations; retain only necessary task content and safe source pointers. Check repository policy before versioning task records.

## Resume with fresh context

Read the identified task document and latest state, then retrieve only the evidence and code needed for the next decision. Verify that the task ID, goal, checkout, and observed behavior still match the snapshot. Reconcile intervening human instructions and other changes before resuming writes.

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
