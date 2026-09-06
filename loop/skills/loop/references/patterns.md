# Loop modes

## Turn loop

Use when the user is exploring direction, judging alternatives, or requesting one bounded step. Establish what this turn should reveal, produce the experiment or comparison, verify what can be verified, and return the result for human direction. Do not convert an exploration into unlimited autonomous implementation.

## Goal loop

Use when completion can be observed: a reproduced defect is fixed, a feature satisfies its contract, or a migration passes defined checks. Define acceptance and relevant non-regression gates, then iterate until they pass or a real boundary blocks progress. Continue through routine failures by changing the hypothesis or approach.

For large goals, establish the whole main flow before refining individual parts. Decompose independent work with clear ownership; keep shared contracts coordinated. A component passing its tests does not establish that the integrated goal is complete.

## Time / event loop

Use only when the user requests scheduled or triggered work. Inspect supported scheduling facilities and reuse an existing matching job when appropriate. Persist a bounded run contract, trigger, scope, verifier, state location, and stop/cancellation conditions.

Each wakeup reloads the current state and checks whether work is still needed. Prevent overlapping writes and duplicate external effects. Retry a side effect only after determining whether the earlier attempt succeeded, using idempotency support when available. Preserve notification preferences and remain quiet on unchanged, non-actionable state unless periodic updates were requested.

If the environment cannot schedule or receive the trigger, describe that limitation accurately. Do not substitute a foreground infinite loop or claim monitoring is active.

## Continual-learning loop

Use for a bounded improvement program driven by real feedback. Maintain a baseline and representative historical regression/replay cases. For each candidate improvement:

1. Capture a reproducible failure or a well-supported opportunity.
2. Form a hypothesis and choose the learning target: code, contract, representation, tool, execution method, or project judgment.
3. Make a controlled change and evaluate the new case plus representative prior cases.
4. Accept, revise, or roll back based on the evidence.
5. Reconcile the durable lesson and compress obsolete guidance.

Keep evaluation cases independent enough to detect overfitting to the latest incident. Promotion to production remains subject to existing authorization and release requirements. Continual learning describes an update discipline; it does not by itself grant perpetual runtime or permission to modify installed skills.
