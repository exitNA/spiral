# Ethos Project Mind

This is the current best synthesis of Ethos. Revise it when evidence changes; do not use it as a chronological learning log.

## Purpose

Ethos helps a project deliver outcomes while developing continuity of judgment across conversations and implementation work. It couples reliable software execution with the durable evolution of project intent, mental models, taste, decisions, collaboration norms, and proven practices.

## Mental Model

Ethos contains two coupled loops with distinct entry points:

1. **Delivery through `$loop`:** expand intent, understand the repository, establish a coarse whole, implement, verify independently, repair, and deliver.
2. **Evolution through `$ethos`:** observe possible learning, decide whether it is durable, locate the narrowest authority, reconcile evidence, integrate the current judgment, and prune stale guidance.

The delivery loop produces evidence and outcomes. The evolution loop improves the judgment used by future delivery. `$loop` may invoke `$ethos`, but `$ethos` can operate independently and remains the only authority for canonicalization.

Detection and canonicalization remain separate. The Hook cheaply notices candidates on each turn; `$ethos` performs semantic, conservative, evidence-aware integration.

Project knowledge is an authority system rather than a note collection. Doctrine holds current judgment, `CONTEXT.md` holds domain meaning, ADRs preserve consequential rationale, `AGENTS.md` carries compact operational guidance, and code or tooling enforces machine-checkable facts. Skills describe reusable methods; they are not the default memory store.

## Principles

- **One system, two entry points:** `$loop` delivers the work; `$ethos` evolves the project's judgment.
- **Coarse whole before local polish:** validate architecture, main flow, and product direction before deep refinement.
- **Evidence-based completion:** objective checks and independent review determine done, not subjective confidence.
- **Coherence over capture:** improve the existing model instead of appending detached observations.
- **Automatic detection, conservative writing:** examine every turn, but canonize only explicit or well-supported learning.
- **One meaning, one authority:** route each insight to the narrowest source of truth and remove superseded guidance.
- **Current synthesis over history:** keep active doctrine focused on present judgment; preserve history only when its rationale remains useful.
- **Project ownership:** durable project knowledge belongs in the repository so people and agents can inspect, review, and version it together.

## Taste

Good output is end-to-end, evidence-backed, integrated, specific, and decision-relevant. Delivery should establish the whole shape early and refine by risk and impact. Learning should make a future choice easier without forcing the reader to reconstruct context from scattered notes.

The system should prefer one clean implementation and one sharpened knowledge model over compatibility layers, duplicated procedures, or comprehensive capture without demonstrated value. Automatic behavior should remain legible, bounded, and reversible.

## Engineering Practice

- Package the capability as one standard Codex plugin containing the complementary `loop` and `ethos` Skills.
- Keep `$loop` explicit-only; keep `$ethos` directly invokable and available for high-confidence automatic learning evaluation.
- Keep project-judgment rules, templates, and authority routing under Ethos; keep execution orchestration and process telemetry under Loop.
- Keep Hook semantics aligned across the POSIX command and its Windows-specific override.
- Keep the source in an independent Git repository that is also installable as a Codex marketplace.
- Protect the repository in layers: ignore local secrets and generated noise, validate distributable structure and dangerous filenames, and scan full Git history for leaked credentials in CI.
- Keep release versions stable and use cachebusters only for local iteration.

## Open Tensions

- Behavioral tests need to distinguish useful canonicalization from over-eager documentation changes and verify Loop-to-Ethos handoff.
- Local process telemetry can improve scheduling, but must remain optional supporting evidence rather than canonical project state.
- Submission to the OpenAI curated plugin repository should follow successful independent use and release hardening.
