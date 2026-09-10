# Codex multi-agent orchestration

## Goal

Use multiple agents only where specialization or parallelism improves the engineering result. The orchestrator owns the whole-task state; workers own bounded tasks.


## Brief-request handoff

The orchestrator may receive only a short requirement rather than a PRD. Before decomposition, synthesize the minimum Requirements Spec from repository evidence. Do not ask workers to invent product behavior independently; the orchestrator should resolve or record material assumptions first and pass bounded acceptance criteria to workers.

## Decomposition sequence

1. Expand the user requirements or PRD into acceptance criteria and determine project lifecycle stage.
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
7. Classify each bounded task and select a model using the policy below, then schedule ready tasks with bounded concurrency.

## Roles and concurrency

Use explorer/requirements for discovery, architect for shared contracts and risks, worker for implementation, tester for reproductions and verification, and reviewer for independent acceptance/correctness checks. Architecture, exploration, and review are normally read-only. Use security review when auth, permissions, untrusted input, privacy, payments, or data integrity is materially involved. Built-in roles plus a bounded brief can replace unavailable custom roles.

Start with up to 3–4 independent read-only agents or about 2 workers with disjoint write ownership, subject to runtime limits. Increase only when low conflict and rework justify it; reduce concurrency or merge tiny tasks when coordination dominates. Do not delegate a task whose setup/handoff cost exceeds its benefit.

## Task difficulty and model selection

Select by the work's uncertainty, dependency breadth, consequences of error, and difficulty of verification, not its role name, prompt length, or number of files alone. Use the least expensive/fastest available model tier adequate for the task, subject to explicit user model choices and budgets. A read-only investigation can be complex; a test run can be simple.

| Tier | Task characteristics and examples | Model capability | Initial reasoning effort, if supported |
|---|---|---|---|
| Simple | Clear procedure, narrow scope, low risk, directly checkable output: locating known symbols, extracting facts from supplied material, running established checks, mechanical edits under a settled contract | Lightweight/fast | Low |
| Standard | Known design with several interacting steps: bounded feature implementation, regression test design, localized diagnosis or review | Balanced general-purpose | Medium |
| Complex | Ambiguous requirements, cross-module contracts, difficult root-cause analysis, subtle concurrency, security/data-integrity decisions, consequential migrations, or integration/review requiring broad reasoning | Advanced/most capable available for the work | High; increase only when evidence warrants it |

Use the higher tier when uncertainty or consequences make a lower tier unsafe. Split a mixed task into a complex decision followed by simple independent execution when there is a clean handoff; do not split away the context needed to judge correctness. Stabilize shared contracts before dispatching cheaper implementation work.

For each dispatch:

1. Assess the bounded task against the table and resolve actual available models through [codex-runtime.md](codex-runtime.md). Tier labels are policy categories, not model IDs.
2. Record the tier, selected model, supported reasoning effort, and one-line rationale in the existing work item's `Result / change reason` field. Respect the LOOP.md template; do not add a second scheduling document or change its structure.
3. Pass the selection through the runtime's actual model controls along with the bounded delegation contract. Keep role, model capability, and reasoning effort separate. Reassess follow-up work before reusing an agent whose model was chosen for an easier assignment.
4. Verify the returned result against the same acceptance criteria regardless of model tier. Independent reviewers must be capable of evaluating the artifact's risk and complexity; routine command execution does not substitute for that review.

If a worker exposes broader dependencies, unresolved ambiguity, unsupported reasoning, or a substantive correctness/review failure, diagnose whether the cause is the task brief, environment, or capability. Correct missing inputs or environmental problems first. When the task exceeds the selected model's capability, promote it to a stronger available model with a compact handoff containing evidence, attempted work, remaining uncertainty, ownership, and acceptance criteria. Do not repeat an unchanged failed assignment on the same lightweight model. Stop or finish the previous owner's work before giving a replacement overlapping write ownership.

Do not downgrade complex work merely because the preferred model is unavailable. Use a comparably capable available model or the capable parent; otherwise explicitly record the capability limitation and keep unsupported acceptance claims unverified. A fixed-model environment can still execute useful work, but cannot be reported as heterogeneous model delegation.

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
