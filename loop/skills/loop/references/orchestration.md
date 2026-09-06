# Codex multi-agent orchestration

## Goal

Use multiple agents only where specialization or parallelism improves the engineering result. The orchestrator owns the whole-task state; workers own bounded tasks.


## Brief-request handoff

The orchestrator may receive only a short product intent rather than a PRD. Before decomposition, synthesize the minimum Intent Spec from repository evidence. Do not ask workers to invent product behavior independently; the orchestrator should resolve or record material assumptions first and pass bounded acceptance criteria to workers.

## Decomposition sequence

1. Expand the user intent/PRD into acceptance criteria and determine project lifecycle stage.
2. Map requirements to current architecture/code, distinguishing real compatibility contracts from pre-production historical implementation.
3. Identify shared contracts: schemas, public APIs, applied migrations, state machines, generated types, configuration.
4. Build a dependency DAG.
5. Mark each task as one of:
   - `explore`
   - `contract`
   - `implement`
   - `test`
   - `integrate`
   - `review`
   - `repair`
6. Mark likely file/interface overlap.
7. Schedule ready tasks with bounded concurrency.

## A good task boundary

A worker task should ideally have:

- one coherent product outcome;
- explicit requirement IDs;
- a small ownership surface;
- known input/output interfaces;
- a locally runnable verifier;
- minimal dependency on another concurrently edited area.

Bad delegation:

> Implement the PRD.

Better delegation:

> Implement R4/R5: persistent session preferences in `packages/settings` only. Do not edit API auth. Preserve `SettingsStore` public methods. Add tests for default, persistence, invalid serialized input. Return changed files, tests run, and any contract assumption.

## Shared-contract gate

Before parallel implementation that depends on a new/changed interface, schema, protocol, migration, or type:

1. have the architect/orchestrator define the contract;
2. validate it against PRD + existing callers;
3. land or otherwise stabilize the contract;
4. then fan out consumers/producers.

This prevents multiple workers from inventing incompatible interfaces.

## Worktree/isolation behavior

Use the isolation mechanism exposed by the active Codex runtime. Do not assume all subagents share one working tree and do not assume all subagents have independent worktrees.

If edits are isolated:

- collect each result;
- inspect the patch;
- integrate in dependency order;
- re-run checks after integration.

If edits share a working tree:

- never parallelize overlapping write scopes;
- reserve files/modules per task;
- ask read-only reviewers/explorers to avoid edits.

## Orchestrator duties during worker execution

Useful concurrent orchestration work includes:

- preparing requirement traceability;
- inspecting a dependency for the next batch;
- constructing test fixtures;
- checking interfaces used by multiple tasks;
- reviewing a finished task while others run;
- classifying a failure;
- updating the schedule based on elapsed times.

Avoid repeatedly polling agents when there is no useful state change.

## Review fan-out

For a substantial final change, independent read-only review can be split into:

- **requirements reviewer** — missing PRD behavior, acceptance gaps;
- **correctness/test reviewer** — logic defects, edge cases, regression gaps;
- **security reviewer** — auth, permissions, secrets, injection, data exposure, unsafe parsing, destructive behavior;
- **maintainability reviewer** — only if complexity or architecture changed materially.

Do not use all reviewers mechanically for tiny changes.

## Critical path

The orchestrator should know which tasks block the most downstream work. Prefer stronger attention and earlier execution for critical-path tasks.

If a critical-path task stalls:

- do not simply add more workers to the same shared problem;
- first improve diagnosis or split independent subproblems;
- run read-only parallel investigation if it can produce distinct evidence;
- then assign one owner for the actual shared write.
