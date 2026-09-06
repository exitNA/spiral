# State, learning, and compression

## Three different stores

| Store | Contents | Lifetime / owner |
| --- | --- | --- |
| Run state | Goal, current checkpoint, evidence pointers, failures, next action, blockers. | Resumable task state owned by Loop. |
| Execution learning | Proven test ordering, contention boundaries, useful decomposition, tooling improvements. | Compact process guidance in the narrowest existing project/tool authority. |
| Project judgment | Intent, mental model, taste, domain meaning, collaboration norms, consequential decisions. | Repository authorities reconciled by Ethos. |

Use existing state/document locations first. For multi-session work without a convention, keep the filled templates together in a task-specific directory such as `.loop/<task-id>/`. Check repository policy before creating or versioning runtime artifacts. Templates are optional shapes; omit sections that carry no useful information.

## Resume with fresh context

Read the compact run contract and latest state, then retrieve only the evidence and code needed for the next decision. Verify that the checkout and observed behavior still match the snapshot. Reconcile intervening human instructions and other changes before resuming writes.

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
