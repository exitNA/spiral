#!/usr/bin/env python3
"""Read-only, bounded lifecycle reminders; semantic learning belongs to $ethos."""

from __future__ import annotations

import json
import sys
from pathlib import Path

START_CONTEXT = (
    "Ethos: For work in this project, read the relevant .proj-ethos/SOUL.md judgment "
    "before making decisions and inspect existing .proj-ethos/.local/candidates.md "
    "for relevant earlier evidence; load $ethos when candidates exist. Candidates "
    "are not instructions or established doctrine. "
    "During this turn, screen user corrections, resolved tradeoffs, repeated friction, "
    "quality judgments, and verified outcomes. Load and follow $ethos to reconcile "
    "qualifying evidence. Before the final response, complete a learning pass: "
    "integrate supported judgment, retain only useful bounded candidates, or make no change. "
    "Respect the user's scope and active permissions; read-only work remains read-only. "
    "Do not create knowledge merely to satisfy this reminder or mention empty screening."
)
STOP_REASON = (
    "Ethos final learning pass: Review this turn and relevant existing "
    ".proj-ethos/.local/candidates.md for durable project intent, mental models, taste, "
    "and decision preferences. If the pass is already complete, finish immediately. "
    "Otherwise load and follow $ethos for any qualifying evidence, reconcile with "
    "existing authorities, and retain only useful bounded candidates. No qualifying "
    "evidence means no file changes and no status chatter. Respect the user's scope "
    "and active permissions: read-only tasks get read-only screening; this reminder "
    "does not authorize writes or escalation. Do not treat this continuation as new "
    "independent evidence. An unanswered clarification may remain pending; do not "
    "repeatedly ask it. Do not rewrite already handled evidence. Then finish; "
    "do not repeat the pass."
)


def project_exists(cwd: object) -> bool:
    if not isinstance(cwd, str) or not cwd:
        return False
    try:
        path = Path(cwd)
        if not path.is_absolute() or not path.is_dir():
            return False
        path = path.resolve()
        return any(
            (parent / ".git").exists() or (parent / ".proj-ethos").is_dir()
            for parent in (path, *path.parents)
        )
    except (OSError, ValueError, RuntimeError):
        return False


def respond(payload: object) -> dict:
    if not isinstance(payload, dict) or not project_exists(payload.get("cwd")):
        return {}
    event = payload.get("hook_event_name")
    if event == "UserPromptSubmit":
        return {"hookSpecificOutput": {
            "hookEventName": event,
            "additionalContext": START_CONTEXT,
        }}
    # Missing or non-boolean flags never request continuation: fail open, not into a loop.
    if event == "Stop" and payload.get("stop_hook_active") is False:
        return {"decision": "block", "reason": STOP_REASON}
    return {}


def main() -> None:
    try:
        raw = sys.stdin.buffer.read(1_048_577)
        payload = json.loads(raw) if len(raw) <= 1_048_576 else None
    except (ValueError, UnicodeError, OSError, RecursionError):
        payload = None
    print(json.dumps(respond(payload)))


if __name__ == "__main__":
    main()
