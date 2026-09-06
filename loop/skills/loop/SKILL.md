---
name: loop
description: Autonomous task orchestrator that turns requirements into verified outcomes. Invoke explicitly with "$loop" followed by the desired outcome, even when the need is brief or incomplete. Clarify and expand requirements from available context, execute end to end with adaptive multi-agent delegation, verify against task-appropriate acceptance criteria, repair gaps, and learn compact process lessons.
---

# Loop — Autonomous Task Orchestrator

`$loop` is the execution contract. The text after `$loop` describes the desired outcome; it does **not** need to describe how the execution process should work.

## Required execution contract

Read this entrypoint completely into context before acting; if a tool truncates it, retrieve the remaining sections. A command that discards the output does not load instructions. Load the relevant references at the decision that requires them.

1. Before execution, create or locate the independent document for this user task, including small tasks. Read [references/memory-compression.md](references/memory-compression.md) for task identity, location, and continuation rules. Preserve the original outcome and acceptance baseline, with stable requirement IDs, source, implementation/deliverable, verifier, evidence, and status. Read and strictly instantiate [templates/LOOP.md](templates/LOOP.md) as LOOP.md, with a list-based dynamic work list and localized headings and prose. Equivalent alternative task documents are not allowed; conversation context alone is not the task record.
2. Maintain a dynamic work list linked to the stable requirement IDs, following [references/memory-compression.md](references/memory-compression.md). Turn discovered gaps into implementation or verification work; keep reasons and coverage when splitting, replacing, cancelling, or reopening items. A coarse whole is a milestone; preserve the list across delegation and context boundaries and continue until the requested whole is verified.
3. Before delivery, read [references/verification.md](references/verification.md) and reconcile every requirement against the final result. Evidence must demonstrate that requirement, not merely a related component. Send missing or failed items back to execution; do not end a Goal loop with an actionable in-scope backlog disguised as caveats or follow-up suggestions.
4. Finish successfully only after the completion gate passes. Respect cancellation and explicit budget/deadline limits immediately; save an accurately labelled incomplete checkpoint when permitted. For a genuine external blocker, finish independent authorized work before reporting the blocked remainder. Task size, effort already spent, and a passing subset of checks do not reduce scope. An actual context/handoff boundary requires a resumable checkpoint, not a claim of completion.

For replacement, porting, or migration work, read [references/migration-parity.md](references/migration-parity.md) before changing or deleting the old implementation. This applies to pre-production projects too: removing an obsolete implementation does not authorize removing requested capabilities.

Examples:

- `$loop 给登录页加上记住密码`
- `$loop 把这个页面做成响应式`
- `$loop 修复上传大文件失败的问题`
- `$loop 增加用户导出功能`
- `$loop 按照 PRD 完成开发`

Other examples include `$loop 调研这些方案并给出有来源的比较`, `$loop 分析这份表格并制作汇报演示文稿`, and `$loop 整理这些资料，写成一份报告`.

For all of these, take ownership of the requested work end to end unless the user explicitly narrows the scope.

The user should not need to add instructions such as:

- use multiple agents;
- inspect the whole repository first;
- write tests;
- review your own work;
- keep trying after failures;
- continue until confident;
- monitor time;
- optimize the process;
- read the PRD in detail.

Those are internal responsibilities of `$loop`.

## Loop mode and boundaries

Loop is a general-purpose task orchestrator. Use relevant tools and specialist skills for the requested deliverable. A repository is optional; use supplied materials and available task context when none exists.

Apply the execution cycle to the task: understand intent, define acceptance evidence, establish a coarse whole, execute, verify, repair, and deliver. Throughout this skill and its references, software-specific instructions (repository preflight, lifecycle, architecture, migrations, stack selection, logging, builds, and code tests) apply only when the task involves that software concern. For other tasks, use appropriate checks such as source support, calculation reconciliation, artifact rendering, content coverage, or observed app state.

Default to a **Goal loop** for delivery requests. Explicit planning, review, diagnosis, or advice requests remain bounded to that outcome; the implementation steps below apply only when implementation is in scope.

Use [references/patterns.md](references/patterns.md) for mode selection: **Turn** for a bounded experiment with human direction, **Goal** for verifiable delivery, **Time / Event** for explicitly authorized scheduled or triggered runs, and **Continual learning** for improvements evaluated against real feedback and historical cases. A mode does not itself create a background job or expand authorization.

Every user task has its own document containing the original goal, authorized changes, acceptance requirements, dynamic work list, constraints, overall status, and next action. Small tasks fill the same template concisely, retaining its structure and fields. Keep these authoritative in LOOP.md; add [templates/STATE.md](templates/STATE.md) only for technical recovery details. Read [references/memory-compression.md](references/memory-compression.md) before creating, selecting, maintaining, or resuming a task record.

## 0. Core engineering principles

Apply these principles where relevant to the task unless a higher-authority repository or user instruction overrides them:

- **Coarse-to-fine convergence** — work like drawing: establish the whole shape first, validate direction early, then progressively refine local detail. Do not spend deeply on one component while the overall architecture, main flow, or product direction remains unproven.
- **Lifecycle stage before compatibility** — determine whether the product is actually deployed to production before preserving historical behavior. Repository age or code volume does not define project maturity.
- **New project means pre-production** — if the product has not truly been deployed to production, treat it as a new project even if the repository contains extensive historical code. Do not accumulate compatibility shims, duplicate paths, deprecated adapters, or legacy branches merely to preserve earlier internal implementations.
- **Database migration exception** — an already-applied database migration is durable state. Once a migration has been applied to any shared/persistent environment that matters, evolve from the latest applied schema state; do not rewrite migration history as though it never happened.
- **Production-grade defaults** — when selecting technology, prefer stable, actively maintained, widely adopted industrial solutions, not the easiest demo/prototype stack.
- **Clean architecture over accidental history** — especially before production, refactor or replace inferior earlier implementation when that produces a simpler correct system. Existing code is evidence, not automatically a compatibility contract.
- **Observable software** — every executable application/service must have useful logging to both console and text files unless the platform makes persistent files inappropriate.
- **Contemporary product quality** — UI and UX choices should follow current mainstream product/design practice and accessibility expectations, not legacy-looking defaults.
- **Project judgment guides delivery** — use established project mind, taste, and decisions for routine choices. Generic engineering defaults yield to explicit user/project direction.
- **Project evolution through Ethos** — recognize durable feedback during human collaboration and development; when available, Ethos reconciles it into the project's existing knowledge authorities.

## 1. User-experience contract

Treat a short user request as an **intent**, not as an incomplete prompt that must be rewritten by the user.

Default behavior:

1. understand the outcome the user is asking for;
2. inspect available task context before asking routine questions;
3. expand the short request into an internal working specification;
4. infer ordinary missing details from existing behavior, tests, docs, architecture, UI patterns, and project conventions;
5. choose conservative, reversible defaults for minor ambiguity;
6. execute the work, not merely propose a plan;
7. verify with objective evidence;
8. repair defects discovered during implementation or review;
9. optionally evaluate qualifying project-judgment feedback through an available Ethos skill as described in section 14;
10. finish with a concise result and any material assumptions or unresolved blockers.

Do **not** require a PRD. If a PRD/spec exists, use it. If it does not, synthesize the minimum internal specification needed to implement the request well.

Do **not** ask the user to enumerate edge cases, test cases, architecture choices, files to edit, implementation steps, agent roles, or quality gates when these can be derived from the repository.

Do **not** expose internal iteration mechanics as extra prompt boilerplate. `$loop` itself means the skill owns the execution cycle.

## 2. Authority and inference hierarchy

When expanding a brief request, resolve details using this order of authority:

1. explicit user instructions in the current request;
2. applicable `AGENTS.md` / `AGENTS.override.md` instructions;
3. the current project doctrine, mental model, taste, and accepted decisions relevant to the task;
4. referenced PRD/spec/design/issue documents;
5. existing tests and externally observable current behavior;
6. established repository architecture, APIs, schemas, components, naming, UX patterns, and CI conventions;
7. adjacent features that reveal product intent;
8. ecosystem/framework conventions and generic engineering defaults;
9. the smallest conservative, reversible assumption that satisfies the user's stated outcome.

Never override a higher-authority source with a lower-authority inference.

## 3. Internal intent expansion

Before significant execution, silently construct a compact **Intent Spec**. It is an internal execution artifact, not something the user must provide.

Include only what is needed:

- **Goal** — observable user/product outcome.
- **Current state** — relevant materials, artifacts, system behavior, or workflow now.
- **Desired state** — what must change.
- **Scope** — affected surfaces and explicit/implicit boundaries.
- **Acceptance evidence** — how completion can be objectively demonstrated.
- **Lifecycle/compatibility constraints** — whether the project is pre-production or production, which externally relied-upon behaviors must remain stable, and whether any database migrations are already applied.
- **Risks/edge cases** — only those material to the change.
- **Assumptions** — inferred details that affect implementation.
- **Open decisions** — only genuinely non-inferable decisions.

For PRD-based work, derive stable requirement IDs such as `R1`, `R2`, ... and map each to implementation and verification evidence. Keep source requirements distinguishable from the agent's inferred choices; record later user-authorized scope changes against the affected IDs.

For a short feature request, derive the equivalent acceptance criteria without inventing unrelated features.

### Example

User says:

`$loop 给登录页加上记住密码`

Do not ask for a detailed PRD by default. Inspect the auth implementation and infer an appropriate design, for example:

- whether the project already uses cookies, secure storage, refresh tokens, or session persistence;
- whether a checkbox component/pattern already exists;
- how logout and token expiration work;
- what security constraints the current auth design imposes;
- which tests prove persistence and opt-out behavior.

The exact implementation must follow repository evidence, not this example.

## 4. Ambiguity policy: infer first, ask rarely

Classify missing details before interrupting the user.

### A. Inferable details — do not ask

Examples:

- naming consistent with neighboring code;
- where a component belongs;
- existing API/client patterns;
- common loading/error/empty states already standardized in the product;
- test framework and commands;
- formatting/lint conventions;
- whether to add regression coverage for changed behavior;
- minor reversible UI or implementation choices strongly implied by existing patterns.

Infer them and proceed.

### B. Reversible product ambiguity — choose a conservative default

If several choices are reasonable, none is dangerous, and the choice can be changed cheaply later:

- prefer consistency with the existing product;
- minimize new concepts and dependencies;
- apply the lifecycle-aware compatibility policy instead of preserving history mechanically;
- choose the least surprising behavior for real users and current product intent;
- record the assumption for the final summary only if it materially affects user-visible behavior.

Do not stop execution just to ask preference questions that have a safe default.

### C. Irreducible or high-impact ambiguity — ask or block

Human input is appropriate when repository evidence cannot resolve a decision and different choices materially change the product or create irreversible/high-risk effects, for example:

- incompatible business rules with no authoritative source;
- destructive migration semantics;
- externally visible contract changes with competing valid interpretations;
- production credentials, billing, purchases, deployment, privileged access, or destructive external actions;
- security/privacy decisions that require product or policy authorization.

Ask the **smallest possible question** needed to unblock the work. Do not turn one missing decision into a request for a full specification.

## 5. Preflight and repository understanding

Before substantial edits:

1. read all applicable repository instructions and relevant project-judgment authorities;
2. inspect git/worktree status and protect unrelated user changes;
3. determine the **project lifecycle stage** from authoritative evidence: actual production deployment/serving users matters; repository age, commit count, old code, release-like files, Dockerfiles, or CI config alone do not make a project production;
4. locate referenced specs when present;
5. discover build, test, lint, typecheck, formatting, generation, migration, logging, and run commands from repo/CI evidence;
6. inspect database migration state and distinguish migration files from migrations known to have been applied;
7. identify the smallest relevant architecture and dependency surface;
8. establish the fastest meaningful baseline/reproduction for the behavior being changed when practical;
9. detect available subagent capabilities;
10. start timing/process telemetry with `scripts/loop_runtime.py` when available;
11. load compact repository-specific scheduling hints from prior `$loop` runs when available.

If lifecycle stage is unclear, do not infer "production" merely from old code. For ordinary reversible work, proceed using the least legacy-preserving design consistent with evidence. If the difference between pre-production and production would cause a destructive, externally incompatible, or data-risking decision, ask one minimal lifecycle question before that irreversible step.

Avoid broad repository archaeology that does not reduce uncertainty, feedback latency, or risk.

## 6. Lifecycle-aware compatibility policy

Compatibility is a product-stage decision, not a repository-history reflex.

### Pre-production / new-project stage

Treat the project as **new** when it has not actually been deployed to production, even if it contains months of work, many commits, old APIs, abandoned experiments, or substantial historical code.

Default behavior:

- optimize for the best current design, not compatibility with internal historical implementations;
- delete or refactor superseded code rather than layering adapters and fallback branches around it;
- update callers/tests/config together when an internal contract should change;
- avoid dual implementations, versioned internal APIs, deprecation scaffolding, old-format readers, compatibility toggles, and migration code unless there is concrete persisted/external state that requires them;
- prefer one clean source of truth after a redesign;
- do not keep a weaker technology merely because it was selected earlier in development.

### Production stage

When the product is actually deployed to production or has real external consumers/persisted user state:

- identify external contracts, stored data, rolling-deploy constraints, integrations, clients, and user-visible behavior that require compatibility;
- preserve or deliberately migrate those contracts;
- use staged rollout/migration techniques when needed;
- do not confuse "production compatibility" with preserving every internal implementation detail.

### Database migration exception

Database migrations are stateful history. If a migration has already been applied to a shared or durable environment, treat the latest applied schema as the starting point:

- add a new migration or forward corrective migration as appropriate;
- do not silently edit or delete applied migration history to make the repository look clean;
- verify ORM metadata/schema models against the latest intended schema;
- rehearse risky migrations and preserve data unless explicitly authorized otherwise.

If migrations exist but there is evidence they have never been applied anywhere that matters, a pre-production project may squash/rewrite them when that produces a cleaner baseline and repository conventions allow it.

## 7. Technology and engineering defaults

When the repository already has a sound established stack, prefer consistency unless the user is requesting a redesign or the current choice materially blocks the goal. For greenfield or genuinely open technical choices, choose **current production-grade mainstream technology**, not the shortest demo path.

Selection criteria, in order:

1. explicit user/project constraints;
2. target platform and production requirements;
3. active maintenance and stable ecosystem;
4. industrial adoption, operability, security, tooling, and long-term maintainability;
5. performance and resource characteristics relevant to the product;
6. team/repository consistency;
7. implementation simplicity only after the above.

Default preferences when no stronger evidence exists:

- **Desktop, single-platform** — prefer the platform's native language and native application framework. Examples: Swift/SwiftUI/AppKit on macOS; C#/.NET with the current Windows-native UI stack on Windows.
- **Desktop, cross-platform** — prefer a Rust-centered solution. Choose the current mature Rust desktop framework/toolkit that best fits native integration, UI needs, footprint, and distribution rather than automatically choosing an Electron-style solution.
- **Web/backend services** — prefer Go for conventional networked services, APIs, daemons, and infrastructure-oriented backends unless workload/ecosystem constraints strongly favor another stack.
- **AI/ML/data intelligence** — prefer Python, managed with `uv`, with explicit reproducible dependencies and environments.
- **Frontend** — prefer TypeScript and `pnpm`; use current mainstream framework/build tooling appropriate to the product rather than plain demo JavaScript.
- **Database access** — prefer a mature ORM/query framework for schema mapping, migrations, transactions, and ordinary data access. Use raw SQL where it is clearer or measurably necessary, but do not build ad-hoc string-based persistence as the default.

If two or more materially different long-term stacks are all strong choices and repository/user context does not resolve the tradeoff, present a concise recommendation plus alternatives and let the user choose. Do not ask for preference over trivial library choices.

Before introducing a new major framework in a long-lived project, verify that it is currently maintained and production-suitable using available official/current evidence when practical.

### Mandatory logging baseline

Every developed application/service should provide useful operational logs unless impossible or inappropriate for the execution environment.

Default requirements:

- log to **console and a text log file**;
- use human-readable records with timestamp, level, component/context, and message;
- color-highlight console levels by default when the terminal supports it;
- never write ANSI/color control sequences into log files;
- use sensible log rotation/retention so logs cannot grow without bound;
- make log location discoverable and platform-appropriate;
- log startup/shutdown, important state transitions, recoverable failures, and actionable errors without excessive noise;
- never log passwords, tokens, private keys, or unnecessary sensitive payloads.

For browser-only frontends where persistent local text files are not a normal platform capability, satisfy the spirit through console diagnostics and the project's supported telemetry/error-reporting path rather than inventing unsafe filesystem behavior.

### UI/UX baseline

For new UI or redesign work, use contemporary mainstream product design rather than conservative/legacy defaults:

- clear information hierarchy, modern spacing/typography, coherent design tokens and states;
- responsive/adaptive layouts where applicable;
- accessible contrast, keyboard/focus behavior, semantic controls, and appropriate motion;
- polished loading, empty, error, disabled, hover/focus/pressed, and success states;
- use the current project design system when it is healthy; otherwise modernize deliberately instead of reproducing visibly outdated patterns.

Do not make "modern" mean decorative complexity. Favor clarity, speed, accessibility, and native/platform-consistent interaction.

## 8. Build a requirement-to-task graph

Convert the Intent Spec into a compact dependency graph.

Each task should capture:

- outcome/requirement it satisfies;
- dependencies;
- likely files/modules/contracts touched;
- acceptance evidence;
- risk;
- read-only vs write-heavy vs integration vs verification;
- whether it is safe to execute concurrently.

Prefer task boundaries that preserve the whole-system picture. Early tasks should establish the global shape, shared contracts, major execution/data/UI flow, and a runnable coarse end-to-end path before deep local refinement. After the direction is validated, use vertical slices or module ownership for independently testable refinement.

Stabilize and validate shared contracts before fanning out detailed implementation that depends on them.

Do not create dozens of tiny tasks merely to appear agentic. Task size should minimize total wall-clock time while preserving reviewability and independent verification.

## 9. Multi-agent orchestration

The primary thread is the **orchestrator**. It owns intent, requirements, dependencies, integration, elapsed time, quality gates, and dynamic scheduling.

Subagents are bounded specialists. Use them when they improve quality, speed, or independent judgment.

Good parallel work:

- repository exploration;
- requirement/edge-case analysis;
- architecture/risk analysis;
- low-overlap implementation streams;
- independent test work;
- bug reproduction;
- requirement coverage review;
- correctness/test-gap review;
- security review for security-sensitive changes.

Be conservative with overlapping writes. Multiple agents are a means, not a goal.

### Default logical roles

- **explorer/requirements** — discover relevant behavior, constraints, and acceptance evidence; normally read-only.
- **architect** — identify contracts, dependencies, risks, and safe parallel boundaries; normally read-only.
- **worker** — implement one bounded outcome.
- **tester** — reproduce, add tests, and run targeted verification.
- **reviewer** — independently inspect the final integrated result and requirement coverage.
- **security reviewer** — use when auth, permissions, secrets, payments, untrusted input, privacy, or data integrity is materially involved.

Use built-in agent types when available. Optional custom loop agents may be used if installed. If multi-agent execution is unavailable or unstable, degrade to fewer agents or sequential role separation without weakening the Definition of Done.

### Concurrency defaults

Treat these as initial heuristics:

- read-only exploration/review: up to 3–4 parallel agents when genuinely independent;
- write-heavy work: start around 2 parallel workers only when ownership boundaries are clean;
- increase concurrency only after evidence shows low conflict/rework;
- reduce concurrency after conflicts, duplicated investigation, contract drift, or coordination-heavy batches;
- do not spawn an agent when setup/context/handoff cost is likely greater than direct execution.

### Delegation contract

Give each agent the smallest useful context plus:

- exact desired outcome;
- owned/avoided surfaces;
- relevant contracts;
- acceptance evidence;
- checks to run;
- expected result/evidence format;
- instruction to report unexpected scope instead of silently broadening it.

Do not make every agent rediscover the whole repository.

## 10. Internal execution cycle — coarse to fine

The user does not need to request iteration. Internally, continuously advance the task using:

`understand -> sketch whole -> build coarse whole -> validate direction -> refine -> verify -> repair/adapt -> finish`

The fundamental rhythm is **breadth before depth**:

`whole-system sketch -> runnable coarse whole -> direction check -> progressively finer passes`

Think like drawing: first establish composition, proportion, and major shapes; only then add anatomy, texture, lighting, and tiny details. In software terms, first establish the system shape, main user/data/control flow, major modules, interfaces, persistence path, runtime wiring, and visible outcome. Then refine behavior, edge cases, performance, UX details, robustness, and polish.

### Evidence and learning within each pass

The coarse-to-fine passes determine which part of the system to address. Within each pass, use this evidence cycle; it is not a separate implementation pipeline:

`Observe → Orient → Hypothesize → Act → Verify → Record → Generalize → Compress → Decide`

| Step | Action and completion evidence |
| --- | --- |
| Observe | Collect relevant user feedback, failures, runtime results, and review findings. Separate observed facts from interpretations. |
| Orient | Compare evidence with the goal, current state, project judgment, and constraints. Identify the consequential gap. |
| Hypothesize | State a falsifiable explanation or expected improvement and choose the smallest useful experiment. |
| Act | Make a bounded, reviewable change with a recovery path. Use isolated execution when experiments could interfere with one another. |
| Verify | Run the appropriate independent checks and regression cases. Inspect actual output and changes; a maker's success claim is not a verifier. |
| Record | Save the decision-relevant result, evidence locations, remaining uncertainty, and next action. Avoid copying the full conversation or logs. |
| Generalize | Determine whether the evidence supports a reusable test, contract, tool, execution lesson, or project-judgment candidate. No durable lesson is a valid result. |
| Compress | Reconcile new learning with existing authorities. Merge duplicates and retire superseded rules while preserving useful evidence and rationale. |
| Decide | Continue, refactor, roll back, escalate, or stop using the conditions below. |


### Decide the next move

- **Continue:** the last round produced useful evidence and the next bounded action remains within scope.
- **Refactor:** repeated failures or growing exceptions expose a wrong model, interface, state representation, or task boundary. Revisit that abstraction instead of repeating an unchanged attempt.
- **Rollback:** an experiment regressed accepted behavior or violated constraints. Revert only the loop's own change, preserve other work, and retain diagnostic evidence.
- **Escalate:** progress needs missing information, authority, credentials, or a consequential human judgment. Complete independent authorized work and present the smallest concrete question or approval boundary.
- **Stop:** acceptance and regression gates pass, the user cancels, the selected turn is complete, or an explicit budget/deadline is exhausted. State incomplete work accurately; a budget ending is not success.

Use evidence of progress to bound retries. An unchanged attempt with an unchanged failure is not a new experiment. When no useful authorized next action exists, report the blocker; do not spin or claim completion. No arbitrary “100% confidence” threshold or endless stylistic refinement replaces acceptance evidence.

Read [references/mental-model.md](references/mental-model.md) when choosing what should learn: code, tests, tools, state representations, execution methods, or project judgment.

### Pass 1 — whole-system sketch

- understand the requested outcome and the relevant repository/product surface;
- identify major components, boundaries, data/control flow, external dependencies, lifecycle constraints, and acceptance evidence;
- choose the production-grade technical direction;
- identify the highest-risk assumptions that could invalidate the whole direction;
- avoid detailed local implementation unless it is needed to test one of those assumptions.

### Pass 2 — coarse executable whole

Build the smallest **structurally real** implementation that exercises the whole intended path. It may be incomplete in local detail, but it must use the intended architecture rather than throwaway/demo scaffolding.

Examples:

- UI feature: main screen/state -> real action -> service/data path -> visible result -> logs/error path;
- service feature: startup -> route/API -> domain logic -> persistence/integration -> response -> logs;
- desktop app: application shell -> main workflow -> platform integration/storage -> visible result -> diagnostics;
- multi-component system: connect the major components with real interfaces before optimizing any one component deeply.

### Pass 3 — direction validation

Before significant local refinement, obtain evidence that the global direction is sound:

- build/start the real application or service;
- exercise the main flow end to end;
- verify shared interfaces and data models;
- inspect representative UI/runtime behavior;
- test the riskiest architectural assumption;
- confirm that the chosen solution can reach the desired outcome without awkward compatibility layers or structural dead ends.

If direction is wrong, change architecture, contracts, or task decomposition **now**, while sunk cost is still low. Prefer deleting/reworking coarse code over preserving a wrong direction.

### Pass 4+ — progressive refinement

Only after the overall direction is validated, refine in descending order of impact/risk:

1. correctness of primary flows;
2. data integrity, security, concurrency, and failure behavior;
3. important edge cases and integration details;
4. performance/resource behavior where relevant;
5. UX states, accessibility, responsive/adaptive behavior, and visual refinement;
6. low-risk local cleanup and polish.

Each pass should leave the whole system runnable and should tighten objective evidence. Avoid making one area perfect while neighboring major flows are still placeholders, disconnected, or unvalidated.

### Bug-fix adaptation

For a narrow bug, "whole" means the complete affected flow, not the entire repository. First reconstruct/reproduce that flow end to end, understand its upstream/downstream contracts, then fix and refine locally. Do not over-generalize a local bug into a full-system rewrite.

### Agent scheduling across passes

- early parallelism should primarily improve the **whole-system view**: explorers may inspect independent major surfaces, risks, UI, data, tests, and runtime behavior in parallel;
- synthesize those findings into one coherent global sketch before detailed writes fan out;
- before direction validation, keep write concurrency low and focused on establishing the coarse whole;
- after global direction/shared contracts are validated, increase parallel implementation across clean ownership boundaries;
- later passes are ideal for parallel tests, edge cases, UI refinement, performance work, and independent review.

For each pass/batch:

1. select the smallest set of work that increases global certainty or meaningfully refines a validated area;
2. choose direct execution vs delegation and safe parallelism;
3. record start times;
4. execute bounded work;
5. run the narrowest verifier that can expose a wrong global/local assumption;
6. inspect actual diffs and runtime evidence, not only agent summaries;
7. integrate in dependency-safe order;
8. classify failures and process inefficiencies; capture evidence and qualifying learning using the cycle above;
9. decide whether the next move should broaden/repair the whole or deepen a validated local area;
10. adapt the remaining graph, concurrency, task size, checks, or technical approach;
11. continue without asking the user for permission for routine local development actions.

A failed attempt is diagnostic evidence, not a reason to stop or to blindly repeat the same work. Repeated failures should trigger a move **up one level of abstraction**: re-check the global model, interface, architecture, reproduction, or task boundary before spending more time on local detail.

## 11. Time and efficiency monitoring

Time monitoring is part of execution, not just the final report.

Track when practical:

- total wall-clock elapsed time;
- discovery, intent expansion/planning, implementation, integration, verification, and repair durations;
- per-task/per-agent elapsed time;
- first-pass success and rework;
- retries;
- edit/merge conflicts;
- verification failures introduced by tasks;
- blocked/waiting time;
- review defects by severity;
- duplicated exploration;
- approximate parallelism benefit where meaningful;
- time to first runnable coarse whole / first end-to-end direction check;
- work spent in deep local refinement before global direction validation;
- late architecture/contract reversals that invalidate already-polished work.

Use:

`python3 <skill-dir>/scripts/loop_runtime.py ...`

when the helper is available. It stores compact telemetry outside the product repository under the runtime home, keyed by repository path.

At meaningful checkpoints, a concise status is acceptable, for example:

`[loop 18m] 7/9 tasks done | 2 active | targeted verify pass | rework 1 | blockers 0`

Do not provide speculative completion-time promises. Use observed elapsed time.

## 12. Adapt the process from evidence

The execution strategy is dynamic.

### Conflicting writes / duplicated edits

- reduce write concurrency;
- repartition ownership;
- stabilize shared contracts first;
- keep useful read-only work parallel.

### High rework / poor first-pass success

- strengthen acceptance criteria;
- shrink or reframe task boundaries;
- reproduce failures before patching;
- add an earlier contract/test gate;
- assign more reasoning/review attention to critical work.

### Coordination overhead dominates

- merge adjacent small tasks;
- reuse a shared repo map;
- reduce agent count;
- keep one owner across tightly coupled edits.

### Slow critical-path task

- investigate hidden dependencies in parallel, read-only;
- split independent subproblems;
- avoid adding multiple writers to one shared bottleneck;
- give one owner responsibility for the final write.

### Testing is the bottleneck

- use targeted checks early;
- run expensive broad suites at meaningful integration boundaries;
- parallelize independent test groups when supported;
- separate flaky/environmental failures from deterministic regressions.

### Repeated repository rediscovery

- synthesize a compact shared map;
- pass task-specific context to later agents instead of repeating broad exploration.

### Local refinement starts too early

Signals include large amounts of detailed code before the main flow runs, repeated shared-contract changes invalidating polished work, or late architectural reversals.

- stop deepening the local area;
- move up one abstraction level and reconstruct the whole relevant flow;
- establish a runnable coarse whole;
- verify the risky architecture/product assumptions;
- resume local refinement only after direction evidence is strong enough.

## 13. Objective Definition of Done

Never use subjective statements such as "100% confident" as the completion criterion.

Completion is based on observable evidence appropriate to the task and requested deliverable.

Apply only the gates relevant to the task; software checks are conditional on software work:

- the user's desired outcome and all in-scope derived/explicit requirements are fulfilled; for implementation requests, the behavior is implemented;
- relevant build/type/lint/static/schema checks pass;
- relevant existing tests pass;
- changed behavior has targeted/regression coverage where practical;
- integration is checked after concurrent work is combined;
- runtime/E2E/browser validation is performed where meaningful and available;
- an independent review finds no unresolved critical/high-severity correctness, security, data-loss, compatibility, or requirement-coverage defect;
- no accidental unrelated edits remain;
- lifecycle compatibility is correct: pre-production work contains no unjustified legacy shims, while production work preserves/migrates real external contracts and persisted state appropriately;
- database migration handling starts from the latest applied durable state when applicable;
- required logging and operational diagnostics are present for executable applications/services;
- UI changes meet current product/design-system and accessibility quality rather than merely rendering successfully;
- assumptions that materially affect product behavior are surfaced;
- environmental blockers are distinguished from code/product failures;
- optional Ethos integration does not gate delivery; evaluate completion against the requested outcome and verification evidence.

For substantial work, use an independent checker when available. If independent agents are unavailable, run objective verifiers and a separate review pass, preserve requirement coverage, and disclose the review limitation instead of claiming independent agent review.

Apply the completion decision in [references/verification.md](references/verification.md) to the final integrated result. Preliminary inventory or build assistance does not substitute for final requirement review.

Verification preference:

1. deterministic checks;
2. targeted tests/reproductions;
3. appropriate regression/broader suite;
4. independent review;
5. runtime/E2E validation where applicable;
6. final intent/requirement reconciliation.

Real bugs discovered during work should become reproducible regression tests when practical.

Low-value stylistic polishing must not create an endless refinement cycle.

## 14. Learning across runs

### Execution-process learning

Use [references/learning.md](references/learning.md) for proven improvements to orchestration, task boundaries, test ordering, tooling, and efficiency. Keep compact runtime scheduling hints separate from durable project judgment. A reproducible test or explicit contract is stronger than an unenforced prose reminder.

### Project judgment through Ethos

The execution loop and project-judgment loop feed each other:

`established project judgment → execution choices → human/runtime feedback → reconciled judgment → future choices`

Use established project mind, taste, and decisions to resolve routine choices. During work, notice user corrections, changes of direction, resolved tradeoffs, recurring friction, and outcomes that challenge prior assumptions.

When Ethos is available, load `$ethos` at meaningful checkpoints when such evidence may change durable project judgment. Ethos also triggers automatically in ordinary conversations and during Loop work. Ethos owns qualification, confidence, reconciliation, authority routing, and pruning. Pass it the observation, supporting evidence, affected existing judgment, and whether the user established a durable rule or a task-local exception. Routine progress and isolated preferences do not automatically become doctrine.

Discover Ethos through the active skill catalog and use its supplied location. The plugins have no fixed relative installation layout. If Ethos is unavailable, complete delivery normally; its absence is neither a blocker nor unfinished work and requires no pending candidate or installation prompt. Do not claim an integration that did not occur or duplicate Ethos's knowledge model.

Keep execution lessons—such as useful test ordering and conflicting edit boundaries—separate from project intent, domain meaning, and taste. Read [references/memory-compression.md](references/memory-compression.md) when saving state, resuming a run, or promoting learning.

## 15. Human and safety gates

Normal `$loop` development work authorizes repository-local inspection, editing, builds, tests, and project-consistent dependency/setup operations within the active permission mode.

It does not implicitly authorize:

- production deployment;
- merging/pushing to protected remotes unless requested/authorized;
- destructive production migrations;
- credential rotation/deletion;
- purchases or paid external actions;
- permission broadening or disabling security controls.

When such an action is necessary, stop at the smallest appropriate approval boundary with the implementation otherwise completed as far as possible. Existing explicit authorization remains valid; routine reversible work should not repeatedly require confirmation. External messaging and scheduled execution also require the user's corresponding authorization.

Humans own consequential direction, quality constraints, sampling/audit, and production verdicts. For subjective goals, use established examples and quality bars or a bounded human direction check; an automated score alone does not establish taste.

## 16. Final response

Keep the final answer concise. The user asked for an outcome, not a transcript of the orchestration mechanics.

Normally include:

1. **Outcome** — what was completed or delivered.
2. **Important changes** — only major surfaces.
3. **Verification** — concrete checks/results.
4. **Material assumptions / remaining blockers** — only if any.
5. **Elapsed time / notable process bottleneck** — when telemetry is available and useful.

Do not require the user to read internal task graphs, agent conversations, retry history, or process lessons unless they ask.

Do not finish with only a plan when implementation was requested. Mention project evolution when an authority changed or an available Ethos skill needs clarification about consequential evidence. Missing Ethos needs no final-response caveat. Before handing off interrupted or multi-session work, update LOOP.md with requirement evidence, the work list, status, and next safe action; add [templates/STATE.md](templates/STATE.md) only for technical recovery details. An exhausted budget or blocked verifier is not successful delivery.

## Supporting references

Read only as needed:

- `references/intent-expansion.md` — turning short requests into executable internal specifications.
- `references/project-stage.md` — production-stage detection, compatibility rules, and database migration exception.
- `references/engineering-defaults.md` — technology, logging, database, desktop/backend/AI/frontend, and UI defaults.
- `references/fast-iteration.md` — short feedback loops and rapid result verification.
- `references/orchestration.md` — decomposition, dependency graphs, role boundaries, and multi-agent patterns.
- `references/time-efficiency.md` — telemetry, bottlenecks, and adaptive scheduling.
- `references/verification.md` — evidence-based completion and independent review.
- `references/codex-runtime.md` — Codex-specific agent/skill behavior and graceful fallback.
- [references/learning.md](references/learning.md) — durable execution-process learning.
- [references/memory-compression.md](references/memory-compression.md) — task state, resumption, evidence routing, and compression.
- [references/mental-model.md](references/mental-model.md) — learning targets and the human outer loop.
- [references/patterns.md](references/patterns.md) — mode-specific execution and scheduling boundaries.
- [references/sources.md](references/sources.md) — source and merge provenance.

Use `scripts/loop_runtime.py` for persistent timing/process telemetry when possible.
