# Codex runtime notes

This skill targets current Codex behavior but must tolerate runtime/version differences.

## Skills

Codex can explicitly invoke a skill with `$<skill-name>`. A skill can include scripts and references and is loaded progressively.

The skill name is `loop`, so the intended explicit invocation is:

`$loop ...`

If an invocation points to a missing versioned cache, resolve the same skill from the active catalog or an available installation and read it. Preserve the resolved path/version in the task's recovery context and revalidate it after a session change; do not repeatedly retry a known-stale path or infer the loaded version from a directory name alone. If discovery finds no usable skill, disclose the limitation and preserve the existing task record and acceptance obligations while continuing authorized work supported by available instructions.

## Native plan/checklist tool

The visible work-list projection depends on host capabilities and is not supplied by this plugin. Inspect the tools actually exposed in the current task before publishing:

1. Check direct native tool declarations first.
2. When the host exposes a code-mode registry, inspect it for a native plan/checklist tool. Searching MCP or connector tools alone does not prove that a native tool is absent.
3. Use the exposed native tool and its live schema. Do not switch collaboration modes or create a separate task or goal merely to obtain a checklist.

Current Codex hosts may expose this capability as `update_plan`. Its known schema accepts `plan` entries containing `step` and `status`, plus an optional top-level `explanation`; known status values are `pending`, `in_progress`, and `completed`, with at most one `in_progress` entry. Treat those names as a runtime example, not a portable plugin API: prefer the live schema whenever it differs. Localize human-readable text, not tool enum values.

If no native checklist tool is exposed, use tool discovery when available. If discovery is exhausted or a call fails, do not invent a tool, claim publication from plain text, or repeatedly retry an unchanged missing capability. Return to the projection contract in [memory-compression.md](memory-compression.md): keep the canonical document current, record native synchronization as blocked/unverified, and continue independent authorized work.

## Subagents

Current Codex versions support subagent workflows and can be instructed by a skill/`AGENTS.md` to delegate independent work. Activity is surfaced in Codex clients.

Built-in roles include `default`, `worker`, and `explorer`. Custom agents can be configured separately in Codex agent TOML files.

Subagent implementations and exact exposed tools can vary by client/version. Therefore:

- express delegation intent semantically rather than depending on a hard-coded internal tool name;
- if a requested custom role is unavailable, use a built-in role plus role-specific task instructions;
- if subagent spawning fails, reduce concurrency or fall back to the primary thread;
- never abandon requirement tracking or verification because the collaboration feature is degraded.

## Models/reasoning

Do not assume one specific model exists in every environment.

Apply the task-tier policy in [orchestration.md](orchestration.md). Resolve capabilities from the active tool declarations and runtime model catalog rather than a model list embedded in this plugin. Use advertised capabilities to map lightweight, balanced, and advanced tiers; use published cost/latency information only when available, not guesses from model names. Explicit user model constraints override automatic selection.

Before spawning:

1. Check whether the live subagent tool exposes per-agent model and reasoning controls, and which model/effort combinations it permits. Do not infer subagent support from a separate top-level task-creation tool.
2. When controls are available, pass the exact supported model ID and effort through those controls. Raising effort on an inherited model is not a model switch. If effort selection is unsupported, omit it while retaining any supported model choice.
3. Honor context-inheritance restrictions. For example, a runtime may forbid model overrides with a full-history fork. Choose an allowed bounded/no-history fork and supply a self-contained task brief with relevant instructions, requirements, ownership, inputs, and verifiers. Use the live schema, not this example, as the authority.
4. Optional role TOML assets describe specialization; they do not establish model availability. Use a compatible role/override or a built-in role with the same task instructions when a preset conflicts with the selected model or supported effort.
5. If selection is unavailable or rejected, use a supported adequate alternative or inherit the parent where appropriate. Record the actual selection or inherited/unknown state and limitation; never claim a model switch from prompt text alone. Do not repeatedly retry an unchanged unsupported combination, alter global model settings, or create user-facing tasks to work around missing subagent controls.

On promotion or follow-up, change the worker's model only if the runtime supports it. Otherwise create a replacement worker with the selected model and a compact evidence handoff, observing the ownership rule in orchestration.md. Record requested selection separately from runtime-confirmed metadata; if the runtime does not expose the effective model, mark it unconfirmed.

## Permissions

Subagents inherit or are constrained by the active Codex permission/sandbox configuration. The skill does not weaken permissions.

## Repository instructions

Applicable `AGENTS.md` instructions remain authoritative project guidance. The loop must obey them for every touched file.

## Graceful fallback matrix

| Capability | Preferred | Fallback |
|---|---|---|
| subagents | parallel bounded roles | sequential role passes |
| custom agent role | named custom role | built-in worker/explorer + explicit role prompt |
| runtime timer helper | `loop_runtime.py` | shell/manual timestamps |
| native plan/checklist | exposed native tool and live schema | current LOOP.md + explicit blocked/unverified synchronization |
| full tests unavailable | full + targeted | targeted evidence + explicit environment blocker |
| isolated worker edits | parallel isolated work | serialize overlapping writes |
