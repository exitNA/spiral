# Ethos

Ethos is an independent Codex plugin that automatically maintains durable project judgment: intent, mental models, taste, decisions, collaboration norms, and proven engineering practice.

During ordinary conversations and implementation work, the entry Hook reminds the agent to read relevant project judgment and screen for learning. A Stop Hook requests one completion pass in a project, including evidence produced during the task; its continuation guard prevents repeated passes. This adds at most one Hook-requested continuation per turn, even when no learning qualifies. The agent loads `$ethos`, reconciles existing knowledge, and integrates high-confidence judgment within active permissions and user/project constraints. No explicit invocation or separate confirmation is needed for routine qualifying updates. Uncertain or conflicting conclusions require clarification; routine screening and candidate housekeeping stay quiet.

Hooks schedule the checks; the agent performs semantic judgment. They do not guarantee that every useful insight will be recognized. Interrupted turns may not reach the completion pass. Read-only requests also prohibit candidate writes and pruning.

Explicit invocation is also available:

```text
$ethos 把这次架构取舍沉淀成项目今后的判断规则
```

## Relationship with Loop

Loop and Ethos are separate plugins in the Spiral marketplace. Loop independently owns software delivery and verification. When Ethos is available, Loop may use it to integrate project judgment. Ethos also works without Loop, and its absence does not block Loop or create unfinished work.

See [project mind](../.proj-ethos/SOUL.md) for the project's principles and authority model.

## Install from this checkout

Hook execution requires Python 3 (`python3` on POSIX, `python` on Windows). Project discovery looks for a `.git` entry or existing `.proj-ethos/` in the working directory or its ancestors. Register the Spiral repository root, then install Ethos:

```bash
codex plugin marketplace add /path/to/spiral
codex plugin add ethos@spiral
```

Optionally install `loop@spiral` for software-delivery orchestration. Start a new Codex task after installation so the Skill and Hook are loaded.

In the Codex CLI, open `/hooks`, review the `ethos@spiral` UserPromptSubmit and Stop commands, and trust each current definition. Installation alone does not trust Hooks; changed definitions need review again. The commands run the packaged, read-only Python script. Confirm both events are active before claiming automatic screening works. See the [official Hook trust documentation](https://learn.chatgpt.com/docs/hooks#review-and-trust-hooks).

When updating a local checkout, use a temporary development cachebuster and reinstall `ethos@spiral`; keep the release version stable in source control. Inspect installed plugin IDs and remove a superseded Ethos installation from another marketplace so only one version supplies the skill. A running task retains its loaded instructions; verify the new version in a new task. Hook execution also depends on the host's enabled/trusted Hook configuration.

## Project knowledge

Ethos stores distilled project knowledge in the target repository’s `.proj-ethos/`: `SOUL.md` for the current synthesis, `CONTEXT.md` for domain semantics, `decisions/` for consequential rationale, and optional `topics/` for focused guidance. Files are created only when needed. The root `AGENTS.md` points to the project mind; source code, tests, and runtime telemetry remain in their own locations.

Distilled knowledge follows the user's preferred language; English is used only when no preference is set. This applies to headings and prose, while filenames such as `SOUL.md` remain stable.

Unconfirmed, decision-relevant evidence can survive conversations in `.proj-ethos/.local/candidates.md`, excluded from Git by its own directory's `.gitignore`. It is bounded and expires under the [candidate lifecycle](plugins/ethos/skills/ethos/references/candidates.md). It is never a source of instructions and is not transferred across machines or worktrees. Confirmed meaning moves into the appropriate authority and its candidate is removed. A recurring choice only becomes a preference when its conditions and rationale are supported; frequency alone is insufficient.

## Source layout

The marketplace lives at `.agents/plugins/marketplace.json` in the Spiral repository root. The Ethos package is under `ethos/plugins/ethos/` and contains its manifest, Hook, and `skills/ethos/`. Loop is packaged separately under `loop/`.

## Validate

From the Spiral repository root:

```bash
python3 scripts/validate_repository.py
python3 -m unittest discover -s tests
gitleaks dir --redact --no-banner .
```

Repository validation checks marketplace and plugin metadata, Skill packages, Hook output, runtime syntax, stable release versions, and file hygiene. Regression tests execute Hook lifecycle cases as well as Loop runtime statistics. These checks do not measure model judgment. Run the separate [behavioral scenarios](evals/README.md) to evaluate discovery, conservative integration, cross-conversation evidence, and later application. Report native Windows and host-dispatch validation separately from direct script execution.
