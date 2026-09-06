# Fast iteration: coarse-to-fine convergence

## Objective

Minimize the amount of work invested before discovering that the overall direction is wrong.

Fast iteration is not "make one tiny part perfect quickly." It is **progressive convergence**:

`rough whole -> validate whole -> refine major areas -> validate -> refine details`

Think like drawing. First establish composition, proportions, and major shapes. Only after the picture reads correctly should you spend time on anatomy, texture, lighting, and tiny details.

Software development should follow the same pattern.

## Core rule: breadth before depth

At every point ask:

> Is the whole relevant system/flow sufficiently established and validated to justify deeper local work?

If not, move outward/upward before going deeper.

Bad pattern:

`deep local design -> polished implementation -> many tests -> discover global architecture/product direction is wrong`

Preferred pattern:

`global sketch -> coarse real end-to-end flow -> direction evidence -> progressively finer passes`

## Pass 1 — sketch the whole

Build a compact global model before deep implementation:

- desired user/product outcome;
- major components and boundaries;
- main user/data/control flow;
- persistence and external integrations;
- shared contracts/interfaces;
- lifecycle/compatibility constraints;
- deployment/runtime shape;
- logging/observability path;
- highest-risk assumptions.

Do not attempt to specify every class, field, function, screen state, or error branch yet.

The goal is to expose architectural mistakes cheaply.

## Pass 2 — build a coarse but real whole

Create the smallest implementation that uses the intended production architecture and connects the main path end to end.

"Coarse" means incomplete refinement, not fake/demo quality.

Do not substitute:

- fake persistence for the real persistence architecture;
- temporary throwaway frameworks;
- hard-coded paths that bypass intended interfaces;
- unsafe shortcuts that would need to be discarded immediately;
- placeholder architecture that proves nothing about the real solution.

The first runnable whole should be structurally representative of the final system.

### Examples

#### New UI/application

Prefer:

`app shell -> primary screen -> real action -> service/data -> visible result -> logs/error visibility`

Before deeply polishing one component, confirm the whole interaction can work.

#### Backend/service

Prefer:

`startup -> endpoint -> domain path -> persistence/integration -> response -> logs`

Before building every validation and optimization branch, prove the runtime wiring and contracts.

#### Desktop application

Prefer:

`launch -> main workflow -> native/platform integration/storage -> visible result -> diagnostics`

Before spending heavily on one panel or custom control, validate the application architecture and main workflow.

#### Multi-component system

Connect the major components with real contracts early. Avoid completing one subsystem in isolation while the cross-system contract is still hypothetical.

## Pass 3 — validate direction

The first important checkpoint is not "is this module polished?" but:

- does the real application/service start?
- does the primary end-to-end flow work?
- do major modules fit together naturally?
- are interfaces/data models viable?
- does the selected technology satisfy the actual requirements?
- is the UX/product direction correct enough to continue?
- is the riskiest assumption now supported by evidence?

If not, change direction immediately.

Early coarse code is cheap to delete. Late polished code is expensive to unwind.

## Pass 4+ — progressively refine

Once global direction is validated, deepen in layers rather than randomly:

1. primary correctness;
2. data integrity/security/concurrency/failure paths;
3. important edge cases and integrations;
4. performance/resource usage;
5. UX states/accessibility/responsiveness/visual quality;
6. local cleanup and low-risk polish.

After each pass, the whole system should remain runnable and better verified.

Avoid local perfection while major neighboring areas are still structurally uncertain.

## Bug fixes

For a bug, scope "the whole" to the **complete affected flow**.

Use:

`reproduce whole affected flow -> map upstream/downstream contracts -> identify cause -> fix -> targeted regression -> nearby integration check`

Do not rewrite the whole product for a local issue, but do not patch one line without understanding the flow around it.

## Multi-agent scheduling

### Early passes

Use parallel agents primarily to broaden understanding:

- repository/product exploration;
- runtime/reproduction inspection;
- UI flow inspection;
- data/schema/integration inspection;
- architecture/risk analysis;
- existing test/CI behavior.

The orchestrator must synthesize these into one coherent whole-system model.

Keep early write concurrency low until architecture/shared contracts/main flow are validated.

### After direction validation

Fan out more aggressively across clean boundaries:

- independent features/modules;
- test coverage;
- failure/edge cases;
- UI refinement;
- performance work;
- review/security review.

Parallelism should accelerate convergence, not multiply speculative detail.

## Verification scheduling

Match verification to refinement level.

### Whole-direction checks

Run early:

- build/start;
- primary smoke/end-to-end flow;
- contract/schema sanity;
- representative UI/runtime check;
- highest-risk architecture assumption.

### Local refinement checks

Run continuously once direction is validated:

- static/type/compiler checks;
- focused unit/contract tests;
- targeted integration tests;
- regression tests;
- performance/resource checks where relevant.

### Broad gates

Run at meaningful integration/completion boundaries:

- broader regression/full suite;
- independent review;
- E2E/runtime validation;
- requirement reconciliation.

## Process signals

Watch for signs that the team/agents are refining too early:

- a large amount of code exists before the main path runs;
- one module is heavily polished while major interfaces are unproven;
- many local tests pass but end-to-end behavior has not been exercised;
- repeated local fixes are caused by changing shared contracts;
- late architectural reversals delete large amounts of polished code;
- agent fan-out is high before the global model is stable.

When these occur, reduce local depth, move up a level, re-establish the whole, and validate direction again.

## Fast iteration is not lower quality

The purpose is to discover wrong direction **earlier**, so more time is available for quality after the direction is proven.

Use production-grade technology and architecture from the beginning, but reveal and validate it progressively instead of attempting to fully detail every local part upfront.
