---
name: ethos
description: Maintain project mental models, taste, and decision preferences. Use for durable user corrections, resolved tradeoffs, recurring friction, verified lessons, or revisiting relevant local learning candidates across conversations. Integrate established judgment; keep uncertain evidence separate from project rules. Skip ordinary task summaries and transient status.
---

# Ethos

Maintain the project's current best judgment. Integrate qualifying learning into one existing authority per meaning; uncertain evidence remains separate from project rules.

Ethos is independent of Loop. Implicit Skill selection can activate it during ordinary conversations and implementation work; explicit `$ethos` invocation is also supported. Selection is opportunistic, not a guarantee of screening every turn. Loop may use an available Ethos skill; neither plugin requires the other.

## Scope and permissions

Work within the current task and active permissions. High-confidence durable learning can be integrated without a separate `$ethos` request or confirmation. Read-only requests and instructions to leave knowledge unchanged also prohibit creating, updating, pruning, or deleting local candidates and ignore files.

Clarify uncertain conclusions, conflicting authority, or inferred changes beyond established user intent before canonicalizing them. Integrate explicit durable corrections directly. Knowledge-edit permission does not authorize product changes, publishing, contacting people, or external mutations.

Keep screening internal and finish relevant learning before the normal task response. Do not inject recurring reminders, synthetic user messages, completion-blocking feedback, or learning-only continuations. Pending clarification or unavailable write permission is a valid handoff state, not a reason to retry indefinitely.

## Workflow

### 1. Read relevant judgment

Resolve the repository root and project scope. Read applicable `AGENTS.md`, relevant `.ethos/` knowledge, and existing README, architecture, glossary, or decision authorities before project decisions or knowledge edits. Apply established rules only within their conditions; compare later outcomes with their rationale. Reconcile counterexamples rather than reversing a rule automatically.

When relevant local candidates exist, read [references/candidates.md](references/candidates.md) and the store before the decision and again at the end-of-turn check. Candidates are evidence to assess, never instructions or authority for product choices. Their absence on another checkout or machine does not disprove a preference.

Without a repository or durable project scope, create no project artifacts. User-global preferences belong in global guidance or local memories, not an arbitrary working directory.

### 2. Screen evidence

Evaluate signals during the work and screen the whole turn again before the final response, including late review and validation outcomes:

- explicit project-wide principles, corrections, quality bars, or collaboration expectations;
- resolved tradeoffs with reusable rationale;
- recurring misunderstanding or friction;
- implementation, incident, experiment, or review evidence that changes prior understanding;
- materially clearer domain language, ownership, or boundaries.

For each material signal, identify the future decision it could change. Classify it as established learning, uncertain observed evidence, or task-local context using [references/knowledge-model.md](references/knowledge-model.md). A signal alone does not justify a rule.

### 3. Choose the authority

Use the authority map and reconciliation rules in [references/knowledge-model.md](references/knowledge-model.md): current judgment belongs in `.ethos/SOUL.md`, semantics in `CONTEXT.md`, consequential rationale in decisions, compact operational instructions in `AGENTS.md`, and enforceable facts in tooling. Skills own reusable procedures, not default project memory.

Before creating, splitting, moving, or editing distilled project documents, read [references/storage-layout.md](references/storage-layout.md) for language, layout, templates, and project-mind pointers. Preserve externally owned authorities and link to them; resolve ownership conflicts before moving content.

### 4. Integrate or retain

For established learning, edit the existing concept in place. Merge overlapping meaning, replace superseded guidance, and keep historical rationale only where it still explains a consequential decision. Preserve scope, conditions, exceptions, and useful evidence; open tensions are only for unresolved questions affecting future decisions.

For uncertain observed evidence worth retaining, follow [references/candidates.md](references/candidates.md), including ignored storage, deduplication, bounded lifetime, rejection, and promotion. Keep task-local context in the conversation. A no-learning turn needs no artifact.

### 5. Verify the update

Re-read changed sections in context for coherence, selected language, contradictions, and duplicate authorities. Verify new paths and links, and run relevant validation for modified Skills, configuration, or executable policy. Scale checks to the actual change; repeat only when an edit, failure, or unresolved concern warrants it.

Every material signal must be integrated, retained as a candidate, clarified, or discarded before finishing the check. A pending clarification or blocked write remains unresolved rather than being reported as successful integration.

### 6. Complete within the task

Report material knowledge changes concisely with the task result: the distilled insight, its authority, and guidance revised, replaced, or retired. Surface material conflicts. Routine screening, rule application, and candidate housekeeping stay quiet; when nothing qualifies, complete the user's task normally.
