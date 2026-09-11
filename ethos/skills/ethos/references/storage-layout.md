# Project knowledge storage

Use one `.ethos/` at the resolved repository root, independently of where the Ethos plugin is installed. Respect explicit project boundaries in a monorepo; keep scoped topics under this directory unless the user establishes independent project roots.

## Layout

```text
<repo>/
  AGENTS.md                         # Compact pointer to the project mind
  .ethos/
    SOUL.md                          # Current synthesis and links to deeper authorities
    CONTEXT.md                       # Domain vocabulary, relationships, invariants
    decisions/
      0001-short-title.md            # Consequential decision and rationale
    topics/
      short-topic.md                # Substantial focused guidance, only when needed
    .local/
      .gitignore                     # Excludes all local contents with *
      candidates.md                  # Optional uncertain evidence, never doctrine
```

Create files and directories only when qualifying content needs them. A small project may need only `SOUL.md`; file count and line count are not quality targets. The project mind is a coherent model across its authorities, with `SOUL.md` as the concise entrypoint. Keep enough purpose, relationships, and cross-cutting judgment there to orient a new task; it must remain useful without opening every linked document.

## Split by decision scope

Keep principles, taste, collaboration, and engineering practice in `SOUL.md` while they form a useful shared overview. Extract a topic when it has a distinct class of decisions or tasks, meaningful detail those tasks need, and a clear reading trigger that lets unrelated tasks skip it. Length can reveal a problem but is not itself a reason to split. Prefer one file when the proposed pieces must always be read together; merge fragmented topics when their boundaries no longer help retrieval.

For each extraction:

1. Identify the topic's scope and consumers; use an existing authority when one already owns the meaning.
2. Move its detailed judgment, conditions, exceptions, and useful rationale together. Keep project-wide invariants in the core and reference them from topics where needed.
3. Leave a short orientation and a relative link in `SOUL.md` that states when to read it, for example “Before changing event creation, correction, or deletion, read [event lifecycle](topics/event-lifecycle.md).” A bare filename or “more details” does not establish a retrieval rule.
4. Reconcile links and remove the superseded full explanation. The core summary routes readers to the authoritative detail; it must not become a second editable rule set. Keep each topic understandable with the core and only its necessary dependencies.
5. Verify that a relevant task can reach its full guidance and an unrelated task can proceed from the core without loading it. Preserve discoverability when moving or merging topics; avoid empty category folders and a document per observation.

Keep domain definitions in `CONTEXT.md`. Record consequential historical rationale in `decisions/`, using the next unused four-digit sequence and a descriptive lowercase hyphenated name. Preserve accepted decisions and mark replacements explicitly; reconcile current judgment in the project mind. Use relative links such as `decisions/0001-storage-layout.md` from the project mind and `../SOUL.md` from decisions.

## Read by task

Start from `SOUL.md`, follow the links whose triggers match the current decision, and load additional dependencies only when the topic requires them. Broaden reading when a decision crosses scopes or exposes a conflict. Do not recursively load the whole knowledge tree or select guidance by filename alone. A linked topic cannot silently override a core invariant; reconcile the conflict in its authority before relying on it.

## Existing knowledge

1. Identify the present authority and its consumers before moving it.
2. Move existing Ethos-owned project knowledge into `.ethos/`, preserving useful meaning and rationale. Merge with an existing destination by meaning rather than overwriting it.
3. Update AGENTS pointers, README links, and inbound and outbound relative links. Remove superseded copies; retain a forwarding pointer only when an external consumer needs the old path.
4. Preserve externally maintained specs, glossaries, architecture documentation, and ADR collections. Link to their authority rather than copying their content into the new directory. New Ethos-owned synthesis belongs in `.ethos/`.
5. Re-read the result, check links, and ensure one current authority per concept. Clarify uncertain ownership or conflicting direction before moving content.

## Boundaries

The directory is durable, reviewable project knowledge and can be versioned with the repository. Respect repository versioning policy. `AGENTS.md` stays at its applicable native location and carries compact operational rules and a pointer; code, tests, schemas, configuration, and reusable skills stay in their native locations.

Keep run state, task checklists, telemetry, raw logs, secrets, and unsupported guesses out of `.ethos/`. The sole local evidence exception is `.local/candidates.md`, governed by [candidates.md](candidates.md); exclude it from Git and from doctrine indexes. Its contents are not shared knowledge. Loop's checkpoints and runtime profiles retain their existing locations. Missing Ethos does not require Loop to create this directory.

## Create or maintain the project mind

When `SOUL.md` is the right authority, use [the project mind template](../assets/SOUL.template.md) as a shape, including only sections with real content. For a consequential decision, use [the ADR template](../assets/ADR.template.md) when the repository has no established ADR format.

When the project mind exists, integrate one compact pointer into the root `AGENTS.md`, adapting its scope to the project and preserving existing instruction-maintenance guidance:

> Read `.ethos/SOUL.md` before product, architecture, UX, collaboration, or engineering-practice decisions. Use `$ethos` when new evidence changes the project's durable judgment.

Keep detailed knowledge in its authority rather than expanding the pointer.

## Language of distilled knowledge

Write project knowledge in the user's preferred language. Resolve it from the user's explicit instruction for the current task first, then an established user language preference available in the conversation or applicable settings/guidance. Use English only when no preference is set. Do not treat an English template or an existing English document as overriding the user's preference, and do not infer a durable preference from a single message's language.

Apply the selected language to headings and prose in `SOUL.md`, `CONTEXT.md`, decisions, and topics, including generated template content. Keep canonical filenames, paths, code identifiers, and exact quotations unchanged. When updating existing knowledge in another language, keep the revised section coherent in the selected language and preserve its meaning and links; translate the whole document when requested rather than creating parallel language copies. A language preference alone is not a reason to create a project artifact.
