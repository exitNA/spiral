# Coarse-to-fine implementation

Use this for multi-component software work or uncertain architecture. Establish the real main flow before deep local refinement so wrong direction is discovered while changes are cheap. For other deliverables, apply the same principle through an outline or representative result, not software-specific gates.

## Establish and validate the whole

1. Sketch the outcome, main user/data/control flow, major boundaries, shared contracts, persistence/integrations, runtime shape, and highest-risk assumptions. Do not specify every class, field, or component state upfront.
2. Build the smallest structurally representative main path using the intended architecture. Coarse detail is acceptable; fake persistence, bypassed interfaces, unsafe shortcuts, and throwaway frameworks cannot prove the real solution.
3. Exercise that path end to end. Check runtime wiring, shared contracts, representative UX, and the riskiest assumption. If direction fails, change the architecture or contract before local polishing.
4. Refine by impact: primary correctness; data integrity/security/concurrency/failures; important edge cases and integrations; performance; UX/accessibility; low-risk cleanup. Keep the whole runnable after each pass.

Examples of a representative path:

| Deliverable | Early direction evidence |
| --- | --- |
| UI/application | Screen → real action → service/data → visible result and diagnostic/error path |
| Backend | Startup → endpoint → domain logic → persistence/integration → response/logs |
| Desktop | Launch → main workflow → native integration/storage → visible result/diagnostics |
| Multi-component system | Major producers and consumers exchange real data through agreed contracts |

A coarse whole is an intermediate milestone, not reduced acceptance. Completion still covers the original requirements through [verification.md](verification.md).

## Narrow bug fixes

Scope the whole to the complete affected flow:

`reproduce → inspect upstream/downstream contracts → identify cause → fix → targeted regression → nearby integration check`

Do not expand a local defect into a product rewrite. Preserve diagnostic evidence and reconsider the contract or representation when repeated local patches fail.

## Coordinate the passes

Early independent discovery may examine product, runtime, UI, data, and test surfaces in parallel. Synthesize one coherent model and stabilize contracts before increasing write concurrency. Follow [orchestration.md](orchestration.md) for ownership, roles, and model selection.

Match checks to the pass:

- **Direction:** start/build, main-flow smoke check, interface/schema sanity, representative runtime/UI, highest-risk assumption.
- **Refinement:** targeted static, unit/contract, integration, regression, or performance checks relevant to the changed area.
- **Integration/completion:** broader regressions, appropriate independent review, runtime checks, and final requirement reconciliation under [verification.md](verification.md).

## When to return to the whole

Revisit direction when shared-contract changes repeatedly invalidate local work, the main flow still cannot run despite many passing component tests, or polished areas remain connected through hypothetical interfaces. Reduce speculative fan-out, repair the global model, and validate it before resuming local detail.

Use [time-efficiency.md](time-efficiency.md) when measuring these bottlenecks or adjusting scheduling. Production quality comes from validating the intended solution progressively, not from perfecting disconnected parts.
