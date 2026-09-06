# Project knowledge model

Use this reference when a learning candidate could fit more than one artifact. The goal is one current model with inspectable rationale, not a collection of notes.

## Authority map

| Authority | Owns | Does not own |
| --- | --- | --- |
| Code, tests, schemas, configuration | Enforceable behavior and mechanically discoverable facts | Human rationale, taste, unresolved tradeoffs |
| `AGENTS.md` | Compact instructions and pointers that must shape every agent run | Detailed doctrine, history, tutorials, task notes |
| Existing doctrine or `PROJECT-MIND.md` | Current synthesis of purpose, mental models, principles, taste, collaboration, and proven practice | Chronological history, tentative observations, command catalogs |
| `CONTEXT.md` or glossary | Domain language, meanings, boundaries, and relationships | General engineering process or historical narrative |
| ADR | Consequential decision, alternatives, context, rationale, and replacement status | Every implementation choice or the current doctrine as a whole |
| Skill | Reusable procedure with distinct triggers and completion criteria | Project-specific beliefs, ordinary facts, isolated preferences |
| Local memories | Recall and supporting evidence across chats | Mandatory rules or the canonical project record |

## Maturity model

Judge maturity internally; do not create a separate backlog merely to label every observation.

- **Observation:** One event or statement. Use it in the current task but do not persist it yet.
- **Emerging:** Repeated or strongly supported, but still uncertain. Ask for confirmation if canonization would influence future decisions.
- **Established:** Explicitly endorsed or validated by evidence. Integrate it into the current authority.
- **Retired:** Superseded or contradicted. Remove it from current doctrine; preserve an ADR link only when the history remains decision-relevant.

An explicit user correction about durable project intent can move directly to Established. Repetition alone does not establish a rule when the repeated behavior may be accidental.

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
