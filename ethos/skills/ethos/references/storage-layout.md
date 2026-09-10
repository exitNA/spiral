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

Create files and directories only when qualifying content needs them. A small project normally needs only `SOUL.md`; skip empty directories, placeholder sections, and a redundant README/index. The project mind links to the actual domain, decision, and topic documents that exist.

Keep principles, taste, collaboration, and engineering practice as sections of the project mind initially. Split a coherent subject into `topics/` only when it has become substantial enough to obscure the overview. Leave a concise summary and relative link in the project mind, and move the detailed rules so each meaning has one owner.

Keep domain definitions in `CONTEXT.md`. Record consequential historical rationale in `decisions/`, using the next unused four-digit sequence and a descriptive lowercase hyphenated name. Preserve accepted decisions and mark replacements explicitly; reconcile current judgment in the project mind. Use relative links such as `decisions/0001-storage-layout.md` from the project mind and `../SOUL.md` from decisions.

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
