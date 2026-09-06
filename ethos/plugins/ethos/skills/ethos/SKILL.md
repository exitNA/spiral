---
name: ethos
description: Continuously distill durable project intent, mental models, taste, decisions, collaboration norms, and proven engineering practice into a coherent repository knowledge system. Use when the user establishes or corrects a lasting principle, a meaningful tradeoff is resolved, repeated friction reveals a missing convention, or completed work produces a reusable lesson. Do not use for ordinary task summaries or transient status.
---

# Ethos

Maintain the project's current best judgment, not a diary of everything that happened.

Ethos is an independent plugin that automatically evaluates and integrates qualifying project learning during ordinary conversations and implementation work. It also supports explicit `$ethos` invocation. Loop may use an available Ethos skill, but neither plugin requires the other.

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

Resolve the repository root and use `<repo>/.proj-ethos/` as the home for project knowledge distilled by Ethos. This is project-owned, versionable source material, not a plugin cache or runtime log. Read the relevant `AGENTS.md`, existing `.proj-ethos/` documents, README, architecture documents, domain glossary, and decisions before writing.

Read [references/storage-layout.md](references/storage-layout.md) when creating, migrating, or splitting project knowledge. Integrate existing meaning rather than starting a competing authority. Migrate an existing Ethos-owned project mind into `.proj-ethos/` and update its references. Preserve externally owned documentation and link to it; resolve conflicting ownership before moving or duplicating its content.

If there is no repository or durable project scope, do not create project artifacts. User-global preferences belong in global guidance or local memories, not in an arbitrary working directory.

## Language of distilled knowledge

Write project knowledge in the user's preferred language. Resolve it from the user's explicit instruction for the current task first, then an established user language preference available in the conversation or applicable settings/guidance. Use English only when no preference is set. Do not treat an English template or an existing English document as overriding the user's preference, and do not infer a durable preference from a single message's language.

Apply the selected language to headings and prose in `SOUL.md`, `CONTEXT.md`, decisions, and topics, including generated template content. Keep canonical filenames, paths, code identifiers, and exact quotations unchanged. When updating existing knowledge in another language, keep the revised section coherent in the selected language and preserve its meaning and links; translate the whole document when requested rather than creating parallel language copies. A language preference alone is not a reason to create a project artifact.

## Route by meaning

Read [references/knowledge-model.md](references/knowledge-model.md) when deciding where an insight belongs or when the repository already has overlapping documentation.

Default routing:

- Current project purpose, mental model, principles, taste, collaboration norms, and proven practice → `.proj-ethos/SOUL.md`.
- Domain vocabulary and semantic boundaries → `.proj-ethos/CONTEXT.md` (link to an externally maintained glossary when it already owns the meaning).
- A consequential decision whose alternatives and rationale must remain inspectable → `.proj-ethos/decisions/NNNN-short-title.md`. Use [assets/ADR.template.md](assets/ADR.template.md) when the repository has no established ADR format.
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

When `.proj-ethos/SOUL.md` is the right authority, use [assets/SOUL.template.md](assets/SOUL.template.md) as a shape, not as a requirement to create empty sections. Include only sections with real content.

Ensure the root `AGENTS.md` contains one compact pointer when the project mind exists:

> Read `.proj-ethos/SOUL.md` before product, architecture, UX, collaboration, or engineering-practice decisions. Use `$ethos` when new evidence changes the project's durable judgment.

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

When no candidate qualifies, remain silent about the loop and complete the user's task normally.
