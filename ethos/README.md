# Ethos

Ethos is an independent Codex plugin that automatically maintains durable project judgment: intent, mental models, taste, decisions, collaboration norms, and proven engineering practice.

During ordinary conversations and implementation work, the Hook reminds the agent to screen for learning. When high-confidence evidence qualifies, the agent loads `$ethos`, reconciles existing knowledge, and integrates the current judgment within active permissions and user/project constraints. No explicit invocation or separate confirmation is needed for routine qualifying updates. Uncertain or conflicting conclusions require clarification; turns with no qualifying learning remain quiet.

Explicit invocation is also available:

```text
$ethos 把这次架构取舍沉淀成项目今后的判断规则
```

## Relationship with Loop

Loop and Ethos are separate plugins in the Spiral marketplace. Loop independently owns software delivery and verification. When Ethos is available, Loop may use it to integrate project judgment. Ethos also works without Loop, and its absence does not block Loop or create unfinished work.

See [project mind](../.proj-ethos/SOUL.md) for the project's principles and authority model.

## Install from this checkout

Register the Spiral repository root, then install Ethos:

```bash
codex plugin marketplace add /path/to/spiral
codex plugin add ethos@spiral
```

Optionally install `loop@spiral` for software-delivery orchestration. Start a new Codex task after installation so the Skill and Hook are loaded.

## Project knowledge

Ethos stores distilled project knowledge in the target repository’s `.proj-ethos/`: `SOUL.md` for the current synthesis, `CONTEXT.md` for domain semantics, `decisions/` for consequential rationale, and optional `topics/` for focused guidance. Files are created only when needed. The root `AGENTS.md` points to the project mind; source code, tests, and runtime telemetry remain in their own locations.

Distilled knowledge follows the user's preferred language; English is used only when no preference is set. This applies to headings and prose, while filenames such as `SOUL.md` remain stable.

## Source layout

The marketplace lives at `.agents/plugins/marketplace.json` in the Spiral repository root. The Ethos package is under `ethos/plugins/ethos/` and contains its manifest, Hook, and `skills/ethos/`. Loop is packaged separately under `loop/`.

## Validate

From the Spiral repository root:

```bash
python3 scripts/validate_repository.py
python3 -m unittest discover -s tests
gitleaks dir --redact --no-banner .
```

Repository validation checks marketplace and plugin metadata, Skill packages, POSIX Hook output, runtime syntax, stable release versions, and file hygiene. Regression tests cover runtime statistics. Windows Hook execution and automatic learning quality still require runtime scenario validation.
