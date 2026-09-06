# Time and efficiency feedback

The objective is not maximum concurrency. The objective is high-quality completion with low avoidable wall-clock time and rework.

## What to measure

### Run-level

- total wall-clock time;
- phase wall time;
- number of tasks;
- number of subagents;
- successful/failed/blocked tasks;
- first-pass success rate;
- rework count;
- conflict count;
- verification failure count;
- review defect count by severity.

### Task-level

- start/end timestamp;
- kind (`explore`, `implement`, `test`, `review`, etc.);
- agent/role;
- status;
- retries/rework;
- conflict or integration issue;
- optional note describing the bottleneck.

### Derived signals

- **first-pass success**: successful task attempts without repair / all ended task attempts (success, failed, or blocked); an empty run has no rate;
- **rework rate**: tasks requiring meaningful repair / completed implementation tasks;
- **parallelism ratio**: sum of overlapping task durations divided by relevant wall span (diagnostic only, not a goal);
- **coordination smell**: many tiny tasks + high orchestration/merge time;
- **contention smell**: conflicts or repeated edits to shared interfaces;
- **verification bottleneck**: verification phase dominates total time while implementation is idle;
- **discovery duplication**: multiple agents spend time rediscovering the same repo facts.

## Adaptation rules

Rules are evidence-driven; thresholds are guides, not absolutes.

### Conflict detected

Immediately reduce write concurrency for the affected shared area. Repartition by module or serialize around a stabilized contract.

### High rework rate

If a batch has multiple failed first passes:

- narrow worker scope;
- include exact acceptance criteria;
- attach relevant interfaces/tests;
- use a pre-implementation contract review on risky tasks;
- increase reasoning quality for critical tasks if available.

### Long-tail task

If one task takes substantially longer than comparable tasks:

- inspect whether it contains multiple hidden tasks;
- split independent subtasks;
- identify dependency waits;
- avoid copying the same stalled work to many write agents;
- optionally parallelize diagnosis only.

### Too many tiny tasks

If tasks complete quickly but the run spends disproportionate time dispatching/integrating:

- merge adjacent tasks that share the same module and verifier;
- reduce agent count;
- reuse one repository/context map.

### Verification bottleneck

- targeted checks after local changes;
- full suite at integration gates;
- parallelize independent test suites if supported;
- do not rerun unchanged expensive checks needlessly;
- isolate flaky/environmental failures.

### Reviewer defect cluster

If independent review repeatedly finds the same class of defect, promote it into the next task template or an executable regression check.

Examples:

- missing null handling -> add explicit edge-case acceptance and test;
- API/client mismatch -> contract gate before parallel consumers;
- untested migration -> migration rehearsal/checklist becomes mandatory.

## Across-run learning

Persist only compact process lessons that are likely to help future runs in the same repository.

Good:

> Shared protobuf files are a contention point. Land schema first, regenerate once, then parallelize service/client work.

Bad:

> Agent 3 was slow today.

Old hints are hypotheses. New evidence can replace them.

## Runtime operation

Use `scripts/loop_runtime.py --help` for the command interface. Telemetry records events supplied by the orchestrator; it does not automatically instrument tools or certify correctness. The primary orchestrator should serialize telemetry writes, capture the run ID returned by `init`, and pass it with `--run` on later run commands so concurrent tasks do not use a different current-run pointer. Use unique task IDs per attempt and finish each run once.

Treat computed hints as heuristics. Keep task contracts/checkpoints and project judgment out of scheduling profiles. If the configured runtime directory is outside allowed write roots, use task-local/manual timing rather than broadening permissions just for telemetry.
