# Project knowledge model

Use this reference when a learning candidate could fit more than one artifact. The goal is one current model with inspectable rationale, not a collection of notes.

Project knowledge distilled by Ethos lives in `<repo>/.ethos/`. See [storage-layout.md](storage-layout.md) for layout, migration, and splitting rules. Code, operational agent instructions, and reusable skills stay in their native locations.

## Authority map

| Authority | Owns | Does not own |
| --- | --- | --- |
| Code, tests, schemas, configuration | Enforceable behavior and mechanically discoverable facts | Human rationale, taste, unresolved tradeoffs |
| `AGENTS.md` | Compact instructions and pointers that must shape every agent run | Detailed doctrine, history, tutorials, task notes |
| `.ethos/SOUL.md` and linked `topics/` documents | Current synthesis of purpose, mental models, principles, taste, collaboration, and proven practice | Chronological history, tentative observations, command catalogs |
| `.ethos/CONTEXT.md` or linked externally owned glossary | Domain language, meanings, boundaries, and relationships | General engineering process or historical narrative |
| `.ethos/decisions/NNNN-short-title.md` | Consequential decision, alternatives, context, rationale, and replacement status | Every implementation choice or the current doctrine as a whole |
| Skill | Reusable procedure with distinct triggers and completion criteria | Project-specific beliefs, ordinary facts, isolated preferences |
| Local memories | Recall and supporting evidence across chats | Mandatory rules or the canonical project record |
| `.ethos/.local/candidates.md` | Bounded, unconfirmed project evidence in the current checkout | Established rules, shared doctrine, or instructions for product decisions |

## Evidence and maturity

A mental model explains concepts, relationships, boundaries, and why they matter. Taste describes observable qualities, calibrated by useful positive and negative examples. A decision preference explains which goal wins a tradeoff, under what conditions, and why. Preserve rationale, exceptions, and evidence that would change the judgment. A deadline-driven choice does not establish a general preference for speed over quality.

Use these evidence thresholds:

- **Established:** An explicit durable user correction can establish a rule immediately. An inferred rule requires independent decisions with shared rationale and checks for counterexamples and situational constraints. Distinguish user choices from agent suggestions. Verified engineering evidence may establish a scoped practice; unexplained aesthetic choices remain uncertain.
- **Candidate:** Observed evidence that could affect a future project decision but does not yet establish a rule follows [the candidate lifecycle](candidates.md). Repeated wording, re-evaluation of the same event, silence, and acceptance of task completion are not independent endorsements.
- **Task-local:** Temporary choices, unsupported guesses, and observations with no future decision value stay in the current conversation. Secrets, personal data, and facts mechanically apparent from code or configuration do not belong in learned doctrine.
- **Retired:** Remove superseded judgment from current doctrine; preserve historical rationale only when it remains decision-relevant.

Before promoting a consequential decision, extract any reusable conditional preference into the current project mind and link its rationale when needed. Keep one-off decisions scoped; an ADR does not inherently establish a general principle.

## Reconciliation questions

Before writing, answer:

1. What future decision will this change?
2. Which existing statement is now incomplete, imprecise, or wrong?
3. What repository evidence supports or contradicts it?
4. Is this project-specific judgment, a domain definition, an agent instruction, a historical decision, or a reusable procedure?
5. Can the new meaning replace existing prose instead of adding another section?

If no future decision changes, the candidate is probably not durable knowledge.

## Conflict handling

- User intent and approved product decisions define desired direction.
- Code and tests describe implemented reality; they do not silently override stated intent.
- ADRs explain why a consequential choice was made and whether it has been superseded.
- Current doctrine should state the best present synthesis and link to rationale instead of duplicating it.
- When authorities disagree, surface the conflict. Do not pick whichever source is easiest to edit.

## Pruning standard

Every update is also a pruning pass over the touched concept:

- collapse synonyms and overlapping rules;
- delete stale statements;
- replace vague aspirations with decision rules;
- remove prose that merely repeats discoverable repository facts;
- retain examples only when they calibrate taste or prevent a recurring misinterpretation.
