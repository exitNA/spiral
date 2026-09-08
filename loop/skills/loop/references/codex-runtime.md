# Codex runtime notes

This skill targets current Codex behavior but must tolerate runtime/version differences.

## Skills

Codex can explicitly invoke a skill with `$<skill-name>`. A skill can include scripts and references and is loaded progressively.

The skill name is `loop`, so the intended explicit invocation is:

`$loop ...`

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

General policy:

- use the current strong parent/orchestrator model for synthesis and critical-path reasoning;
- use faster/lower-cost agents for read-heavy exploration or mechanical scans when available;
- use stronger/higher-reasoning agents for architecture, difficult debugging, and independent review when the runtime permits;
- do not spend expensive agent contexts on trivial tasks.

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
