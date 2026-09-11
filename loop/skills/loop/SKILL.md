---
name: loop
description: Explicitly invoke "$loop" to turn a requirement into a verified outcome, including brief requests. Own task tracking, adaptive execution, multi-agent delegation, verification, and repair. Research, review, diagnosis, and planning stay within their requested scope.
---

# Loop — Autonomous Task Orchestrator

Own the requested outcome from requirements to verified delivery. A repository or PRD is optional. Use specialist skills and tools for the deliverable; apply engineering rules only to software work.

Read this entrypoint fully, then load references at the decision points below. If output is truncated, retrieve the missing section.

On resumption or a stale invocation path, resolve the available skill through [codex-runtime.md](references/codex-runtime.md#skills) and resume the same task record; a missing cache path does not cancel the task's acceptance obligations.

## Scope and authority

Treat the user's request as the requirement. Inferred intent may clarify it but must not replace or shrink it. Resolve choices in this order: explicit user instructions, applicable repository instructions, established project judgment, referenced specifications, observed behavior/tests, repository conventions, then conservative assumptions.

Requests to research, explain, review, diagnose, or plan authorize that bounded result. Requests to build, change, or fix authorize in-scope implementation and relevant local validation. Continue already-authorized work without routine confirmation. Respect read-only requests and active permissions. External writes, publication, destructive actions, purchases, external messaging, and scheduled execution require corresponding authorization; earlier authorization remains valid. Before a necessary approval, complete independent authorized preparation so the proposed action is concrete and reviewable.

Resolve routine gaps from context. Ask only when missing information materially changes the outcome and cannot be inferred safely; continue independent work while that decision is pending. Skill guidelines must not override explicit user requirements or introduce approval gates for hypothetical risks.

Use a **Goal loop** for verifiable delivery. For exploration, one-step experiments, scheduled/event work, or a bounded learning program, read [patterns.md](references/patterns.md) to select the corresponding mode and stopping conditions. A mode never creates scheduling or expands scope by itself.

## 1. Establish the task and acceptance

Before execution, read [memory-compression.md](references/memory-compression.md) and strictly instantiate or resume [templates/LOOP.md](templates/LOOP.md), including for small tasks. That reference owns task identity, timestamps, language, continuation, no-write fallbacks, and native-plan projection. Keep the record concise without changing its required structure.

- Preserve the original request, stable requirement IDs, acceptance evidence, and authorized changes separately from assumptions.
- Maintain the template's list-based work items with dependencies, done conditions, coverage, and adjustment reasons. Completing a work item does not verify its requirement.
- LOOP.md owns overall status and the next action; optional [STATE.md](templates/STATE.md) contains only technical recovery details.
- Save the record and synchronize its work list through the native plan/checklist tool at each meaningful checkpoint. Resolve the live tool through [codex-runtime.md](references/codex-runtime.md). If unavailable, report synchronization as blocked/unverified and continue independent authorized work; prose checkboxes, file panels, and custom views do not substitute for it.

For brief or materially incomplete requirements, read [requirements-expansion.md](references/requirements-expansion.md) and derive the minimum working specification from available evidence. Do not demand a PRD or turn a small request into a broad redesign.

For software work, inspect applicable instructions, git/worktree state, affected contracts, and available build/test/runtime checks before editing. Protect unrelated changes. Read [project-stage.md](references/project-stage.md) before compatibility or migration decisions: actual deployment/use and durable state determine obligations, not repository age. Before replacing, porting, or deleting an implementation, also read [migration-parity.md](references/migration-parity.md) and preserve the original capability baseline.

Read [engineering-defaults.md](references/engineering-defaults.md) when creating an executable application/service, choosing technology, changing operational diagnostics, or building/revising UI. It owns stack, logging, database, and design defaults; established user/project choices take priority.

## 2. Establish the whole, then refine

Use one execution cycle:

`understand → establish a coarse whole → verify direction → refine → verify/repair → deliver`

For multi-component implementation or uncertain architecture, read [fast-iteration.md](references/fast-iteration.md). Establish the real main flow and shared contracts before deep local polish. For a narrow bug, the whole is the complete affected flow; reproduce and identify its cause before changing it. For research, documents, and data work, use an outline, representative result, or reconciled calculation to check direction early.

Each pass should produce a bounded change or useful evidence:

1. Compare observations with the requirement and choose a falsifiable hypothesis or next deliverable.
2. Execute within the current ownership and scope, then inspect actual output and run the relevant verifier.
3. Record the result and update work, requirement evidence, blockers, and the next action in LOOP.md. Changed artifacts invalidate affected earlier evidence until rechecked. User rejection or corrected product judgment follows the reopening rules in [memory-compression.md](references/memory-compression.md#stable-requirements-dynamic-work) before further implementation.
4. Continue on useful progress. Repeated failures require a new diagnosis or a better task boundary, contract, or representation; do not repeat an unchanged attempt. Roll back only the loop's own regressing experiment, preserving other work and diagnostic evidence.

## 3. Delegate independent work

Use subagents when bounded independent work can improve quality, latency, or independent judgment. Keep direct execution for tasks where setup and handoff cost dominate. The primary agent owns requirements, the canonical record, integration, and final verification; workers own bounded subtasks.

Before dispatch, read [orchestration.md](references/orchestration.md) for task boundaries, ownership, concurrency, role selection, and difficulty-based model selection. Then use [codex-runtime.md](references/codex-runtime.md) to resolve actual model IDs and supported invocation parameters. Select lightweight, balanced, or advanced models according to each task's difficulty and risk; a role label or higher reasoning effort alone does not switch models.

Stabilize shared contracts before dependent workers start. Avoid overlapping writes, and use the runtime's actual isolation model. Give each worker the parent task identity, outcome and requirement IDs, relevant context/contracts, owned and avoided surfaces, acceptance checks, and expected evidence. Require it to report unexpected scope rather than silently broadening it.

Inspect worker results before integration and verify the combined artifact. When delegation is unavailable, use fewer agents or sequential role passes and report any material verification limitation. Keep useful independent work moving while workers run; avoid polling unchanged status.

## 4. Verify, repair, and finish

Read [verification.md](references/verification.md) before selecting acceptance checks and again before delivery. It owns verifier integrity, failure classification, independent review, and the completion gate.

Match verification to the deliverable and risk: relevant deterministic checks, reproductions/regressions, integration/runtime checks, source support, calculation reconciliation, or artifact inspection. Do not add tests that merely mirror a reversible low-impact edit. Once required checks pass, repeat or broaden them only for new changes, failures, or unresolved concerns. Use an independent reviewer for substantial work when available; otherwise use objective checks and a separate review pass with the limitation disclosed.

Re-read the saved LOOP.md and apply the completion gate to every original in-scope requirement and authorized correction. Reconcile the record, final artifact evidence, and proposed delivery claims before answering; missing, failed, or unverified capabilities return to execution while useful authorized work remains.

Stop when the completion gate passes, the requested bounded turn ends, the user cancels, an explicit budget/deadline ends, or a genuine external/context boundary prevents further progress. For incomplete work, save an accurate checkpoint with outstanding IDs, evidence, blocker, and next safe action; do not reduce the goal to declare success. Exhaust independent work before reporting an external blocker. Optional polish does not justify endless iteration.

The final response states the outcome, material changes, verification evidence, and any material assumptions or unresolved requirements. Mention elapsed time only when measured and useful. For a handoff, link the canonical task record and confirm its latest state and native projection or the synchronization limitation. Do not replace requested implementation with a plan or an offer to continue.

## 5. Improve execution without accumulating instructions

For multi-step or parallel runs, read [time-efficiency.md](references/time-efficiency.md) before starting available telemetry or changing scheduling based on bottlenecks. It owns the optional runtime helper, measurement rules, and fallbacks. Telemetry supports decisions; it does not replace task state or certify completion.

When evidence may improve future execution, read [learning.md](references/learning.md); when deciding whether to change code, tests, a representation, or project judgment, read [mental-model.md](references/mental-model.md). Preserve verified lessons in the narrowest authority and prefer executable checks to prose when possible.

Use established project judgment during delivery. If feedback may change durable judgment and Ethos is available, discover it through the active skill catalog and pass the observation, evidence, existing authority, and proposed scope. Ethos owns qualification, reconciliation, and storage; Loop owns execution and process telemetry. Missing Ethos creates no pending work, installation prompt, or delivery blocker. Keep any learning within the current task and report only material knowledge changes.
