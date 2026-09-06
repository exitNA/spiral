---
name: ethos
description: Continuously distill durable project intent, mental models, taste, decisions, collaboration norms, and proven engineering practice into a coherent repository knowledge system. Use when the user establishes or corrects a lasting principle, a meaningful tradeoff is resolved, repeated friction reveals a missing convention, or completed work produces a reusable lesson. Do not use for ordinary task summaries or transient status.
---

# Ethos

Maintain the project's current best judgment, not a diary of everything that happened.

Ethos is the evolution half of this plugin. `$loop` may invoke it after delivery work produces durable evidence, while `$ethos` can also be used directly without running the delivery orchestrator.

## Operating principle

Detect learning continuously and canonicalize it conservatively. A qualifying insight should improve an existing source of truth. It should not become another detached note merely because it is new.

The loop is:

1. Observe a signal during discussion, implementation, review, debugging, or validation.
2. Decide whether it is durable project learning rather than task-local context.
3. Locate the narrowest existing authority that should own it.
4. Reconcile it with what is already written and with repository evidence.
5. Integrate by rewriting, sharpening, replacing, or retiring existing content.
6. Validate coherence, links, and any executable guidance.

## Qualifying signals

Canonicalize when at least one strong signal exists and the result is likely to matter in future work:

- The user explicitly states or corrects a project-wide principle, quality bar, or way of working.
- A real tradeoff is resolved with rationale that future contributors need.
- The same misunderstanding or friction appears more than once.
- An implementation, incident, experiment, or review provides evidence that changes prior understanding.
- Domain language, ownership, or a boundary becomes materially clearer.

Do not canonicalize guesses, temporary workarounds, task status, secrets, personal data, isolated preferences, or facts already obvious from code and configuration.

## Establish project scope

Resolve the repository root and inspect the project's existing knowledge shape before creating files. Read the relevant portions of `AGENTS.md`, `README`, design or architecture documents, `CONTEXT.md`, and ADRs when present.

If an existing document already serves as the project's mental model or principles document, improve it instead of creating `PROJECT-MIND.md`. Use `PROJECT-MIND.md` only when no coherent authority exists and a qualifying insight needs a home.

If there is no repository or durable project scope, do not create project artifacts. User-global preferences belong in global guidance or local memories, not in an arbitrary working directory.

## Route by meaning

Read [references/knowledge-model.md](references/knowledge-model.md) when deciding where an insight belongs or when the repository already has overlapping documentation.

Default routing:

- Current project purpose, mental model, principles, taste, collaboration norms, and proven practice → the existing project doctrine or `PROJECT-MIND.md`.
- Domain vocabulary and semantic boundaries → `CONTEXT.md` or the established glossary.
- A consequential decision whose alternatives and rationale must remain inspectable → an ADR. Use [assets/ADR.template.md](assets/ADR.template.md) when the repository has no established ADR format.
- A compact instruction that must shape every agent run → the nearest applicable `AGENTS.md`.
- A reusable multi-step workflow that applies independently of this project's current beliefs → a Skill.
- Enforceable facts → code, tests, schemas, linters, or configuration rather than prose.

Skills are the exception, not the default destination.

## Integrate without fragmentation

- Treat the target document as a maintained model of the present, not an append-only learning log.
- Find the paragraph or decision rule that the new evidence changes and edit it in place.
- Merge repeated ideas under one concept and one owner.
- Remove superseded guidance when the new understanding replaces it.
- Preserve historical rationale only when it still explains a consequential decision; use an ADR for that history.
- Prefer one precise rule with a useful example over several overlapping bullets.
- Record uncertainty as an explicit open tension only when future decisions genuinely depend on resolving it.

## Create or maintain the project mind

When `PROJECT-MIND.md` is the right authority, use [assets/PROJECT-MIND.template.md](assets/PROJECT-MIND.template.md) as a shape, not as a requirement to create empty sections. Include only sections with real content.

Ensure the root `AGENTS.md` contains one compact pointer when the project mind exists:

> Read `PROJECT-MIND.md` before product, architecture, UX, collaboration, or engineering-practice decisions. Use `$ethos` when new evidence changes the project's durable judgment.

Integrate this pointer with existing instruction-maintenance guidance and avoid duplicates. Do not expand `AGENTS.md` with the detailed knowledge itself.

## Confidence and authorization

Canonicalize only when the insight is durable and the current task authorizes project-knowledge edits. Explicit `$ethos`, or a request to record, distill, maintain, or update project knowledge, supplies that authority. When Ethos is invoked implicitly without such authority, identify the candidate and ask before writing. Evidence can establish confidence; it does not grant write permission.

When the conclusion is inferred, contested, or would materially redirect the project, present the candidate and request confirmation even when writing is otherwise authorized.

Never treat permission to update project knowledge as permission to alter product behavior, publish changes, contact people, or modify external systems.

## Completion

After an update:

1. Re-read the changed section in context and remove contradictions or duplicate meanings.
2. Verify every new path or link exists.
3. Run relevant validation for any modified Skill, configuration, or executable policy.
4. Report the distilled insight, its authority, and whether existing guidance was revised, replaced, or retired.

When no candidate qualifies, remain silent about the loop and complete the user's task normally.
