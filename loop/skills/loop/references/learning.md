# Execution-process learning for future loop runs

The loop should learn from engineering feedback without depending on model-weight updates or ever-growing chat context.

Project purpose, mental model, domain meaning, taste, collaboration norms, and consequential decisions belong to Ethos and the repository's existing project authorities. This reference covers execution-process learning only.

## Learning assets

Prefer converting feedback into, in order of strength:

1. reproducible test/eval;
2. explicit interface/contract;
3. improved task decomposition rule;
4. project process hint;
5. tooling/script improvement;
6. compact memory note.

## What to persist

Persist process knowledge when it is:

- repeated across tasks/runs;
- strongly supported by measured failures or conflicts;
- likely to save significant future time;
- necessary to prevent a severe class of defect.

Examples:

- modules that should not be edited concurrently;
- expensive checks and the best targeted precursor checks;
- generated-code ordering constraints;
- recurring setup needed before tests;
- repository-specific contract boundaries;
- task sizes that historically produce excessive rework.

## What not to persist

- speculative explanations;
- one-off transient failures;
- secrets or sensitive outputs;
- long raw logs;
- full conversation transcripts;
- arbitrary per-agent performance judgments based on one task.

## State and compression

Read [memory-compression.md](memory-compression.md) when persisting or resuming state, compressing learning, or handing project-judgment evidence to Ethos. Runtime profiles are compact process hints; task checkpoints and project doctrine have separate owners.

## Feedback loop

`run -> measure -> detect bottleneck -> change scheduling/task contract/test strategy -> verify improvement -> persist compact lesson`

This makes the orchestration system itself an object of engineering and learning.
