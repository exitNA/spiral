---
name: ethos
description: Maintain project mental models, taste, and decision preferences. Use for durable user corrections, resolved tradeoffs, recurring friction, verified lessons, or revisiting relevant local learning candidates across conversations. Integrate established judgment; keep uncertain evidence separate from project rules. Skip ordinary task summaries and transient status.
---

# Ethos

Maintain the project's current best judgment, not a diary of everything that happened.

Ethos is an independent plugin that automatically evaluates and integrates qualifying project learning during ordinary conversations and implementation work. It also supports explicit `$ethos` invocation. Loop may use an available Ethos skill, but neither plugin requires the other.

## Operating principle

Use implicit Skill selection for qualifying signals and canonicalize conservatively within the existing task. A qualifying insight should improve an existing source of truth. It should not become another detached note merely because it is new.

Protect the main conversation: do not inject recurring learning reminders, synthetic user messages, or force continuation after the answer. Keep routine screening internal and report only a material knowledge change concisely with the task result. Skill selection is opportunistic; it does not guarantee a separate check on every turn.

The loop is:

1. Before a project decision, read the relevant current judgment and any relevant local candidates. Apply established rules within their stated scope; candidates are questions, not instructions.
2. Observe signals during discussion, implementation, review, debugging, and validation. Before the final response, screen the whole turn again, including outcomes that appeared after the user's message.
3. Locate the narrowest existing authority that should own it.
4. Decide whether the evidence establishes durable learning, supports a bounded candidate, or is task-local. Reconcile it with existing judgment and contradictory evidence.
5. Integrate established learning by rewriting, sharpening, replacing, or retiring existing content. Handle uncertain evidence using the candidate lifecycle below.
6. Validate coherence, links, and any executable guidance. Finish only after each material signal has been integrated, retained as a candidate, clarified, or discarded; a no-learning turn needs no file or report.

## Qualifying signals

Screen the following signals for future decision value, then establish maturity before writing a rule. A signal can justify a candidate without justifying canonicalization:

- The user explicitly states or corrects a project-wide principle, quality bar, or way of working.
- A real tradeoff is resolved with rationale that future contributors need.
- The same misunderstanding or friction appears more than once.
- An implementation, incident, experiment, or review provides evidence that changes prior understanding.
- Domain language, ownership, or a boundary becomes materially clearer.

Do not canonicalize guesses, temporary workarounds, task status, secrets, personal data, isolated preferences, or facts already obvious from code and configuration.

## Infer judgment from evidence

Distinguish a mental model (concepts, relationships, boundaries, and why they matter), taste (observable qualities and useful positive/negative examples), and a decision preference (when two goals conflict, which wins and why). Preserve the conditions, rationale, exceptions, and evidence that would change a rule. A choice made under a deadline does not establish a general preference for speed over quality.

An explicit durable user correction can establish a rule immediately. For an inferred rule, look for independent decisions with a shared rationale, check counterexamples and situational constraints, and distinguish user choices from the agent's own suggestions. Repeated wording, repeated evaluation of the same event, silence, and acceptance of task completion are not independent endorsements. Verified engineering evidence may establish a scoped practice; an unexplained pattern of aesthetic choices remains a candidate until clarified.

Before promoting a consequential decision, extract any reusable conditional preference into the current project mind and link its rationale when needed. Keep one-off decisions in their own scope; do not manufacture a general principle for every ADR.

## Carry uncertain evidence across conversations

When observed project evidence may change a future decision but is not yet established, read [references/candidates.md](references/candidates.md). It defines the bounded, non-authoritative local candidate store, deduplication, expiry, rejection, and promotion. Read it also when a relevant candidate store already exists, even if this turn introduces no new candidate.

Candidate maintenance follows the same active permissions and user constraints as knowledge edits. A read-only task permits reading, not creating, pruning, or updating either store. Keep task-local choices and unsupported guesses in the current conversation. Local candidates are not loaded automatically on another machine or checkout, and their absence is not evidence that a preference does not exist.

## Establish project scope

Resolve the repository root and use `<repo>/.ethos/` as the home for project knowledge distilled by Ethos. This is project-owned, versionable source material, not a plugin cache or runtime log. Read the relevant `AGENTS.md`, existing `.ethos/` documents, README, architecture documents, domain glossary, and decisions before writing.

Read [references/storage-layout.md](references/storage-layout.md) when creating or splitting project knowledge. Integrate existing meaning rather than starting a competing authority. Preserve externally owned documentation and link to it; resolve conflicting ownership before moving or duplicating its content.

If there is no repository or durable project scope, do not create project artifacts. User-global preferences belong in global guidance or local memories, not in an arbitrary working directory.

## Language of distilled knowledge

Write project knowledge in the user's preferred language. Resolve it from the user's explicit instruction for the current task first, then an established user language preference available in the conversation or applicable settings/guidance. Use English only when no preference is set. Do not treat an English template or an existing English document as overriding the user's preference, and do not infer a durable preference from a single message's language.

Apply the selected language to headings and prose in `SOUL.md`, `CONTEXT.md`, decisions, and topics, including generated template content. Keep canonical filenames, paths, code identifiers, and exact quotations unchanged. When updating existing knowledge in another language, keep the revised section coherent in the selected language and preserve its meaning and links; translate the whole document when requested rather than creating parallel language copies. A language preference alone is not a reason to create a project artifact.

## Route by meaning

Read [references/knowledge-model.md](references/knowledge-model.md) when deciding where an insight belongs or when the repository already has overlapping documentation.

Default routing:

- Current project purpose, mental model, principles, taste, collaboration norms, and proven practice → `.ethos/SOUL.md`.
- Domain vocabulary and semantic boundaries → `.ethos/CONTEXT.md` (link to an externally maintained glossary when it already owns the meaning).
- A consequential decision whose alternatives and rationale must remain inspectable → `.ethos/decisions/NNNN-short-title.md`. Use [assets/ADR.template.md](assets/ADR.template.md) when the repository has no established ADR format.
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

When `.ethos/SOUL.md` is the right authority, use [assets/SOUL.template.md](assets/SOUL.template.md) as a shape, not as a requirement to create empty sections. Include only sections with real content.

Ensure the root `AGENTS.md` contains one compact pointer when the project mind exists:

> Read `.ethos/SOUL.md` before product, architecture, UX, collaboration, or engineering-practice decisions. Use `$ethos` when new evidence changes the project's durable judgment.

Integrate this pointer with existing instruction-maintenance guidance and avoid duplicates. Do not expand `AGENTS.md` with the detailed knowledge itself.

## Confidence and authorization

Automatic invocation includes integrating high-confidence, durable learning into repository knowledge within active permissions and user/project constraints. An explicit `$ethos` request is optional; routine qualifying updates need no separate confirmation. Respect read-only requests and instructions to leave project knowledge unchanged.

When evidence is uncertain, authorities conflict, or a proposed conclusion would materially redirect the project beyond established user intent, present the candidate and request clarification before canonicalizing it. An explicit durable user correction can be integrated directly.

Never treat permission to update project knowledge as permission to alter product behavior, publish changes, contact people, or modify external systems.

## Completion

After an update:

1. Re-read the changed section in context, check that its headings and prose follow the selected language, and remove contradictions or duplicate meanings.
2. Verify every new path or link exists.
3. Run relevant validation for any modified Skill, configuration, or executable policy.
4. Report the distilled insight, its authority, and whether existing guidance was revised, replaced, or retired.

When a later task uses an established rule, verify its conditions still apply and compare the outcome with its rationale. A counterexample triggers reconciliation, not automatic reversal. Report a material conflict or knowledge change; routine application and candidate housekeeping stay quiet. Complete any relevant learning before the existing task response; do not start an extra turn for learning. A pending clarification or unavailable write permission is an honest completion state, not a reason to retry indefinitely.

When no candidate qualifies, remain silent about the loop and complete the user's task normally.
