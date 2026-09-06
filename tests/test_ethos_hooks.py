"""Exercise the installed lifecycle commands, not a mock of hook decisions."""

import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "ethos/plugins/ethos"


class EthosHookTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="ethos hook ")
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name).resolve()
        self.project = self.base / "project with spaces"
        self.project.mkdir()
        (self.project / ".git").mkdir()
        self.plugin = self.base / "installed plugin"
        shutil.copytree(PLUGIN / "hooks", self.plugin / "hooks")
        self.hooks = json.loads((self.plugin / "hooks/hooks.json").read_text())["hooks"]

    def run_hook(self, event="Stop", payload=None, raw=None):
        if payload is None:
            payload = {"hook_event_name": event, "cwd": str(self.project), "stop_hook_active": False}
        command = self.hooks[event][0]["hooks"][0]["commandWindows" if os.name == "nt" else "command"]
        result = subprocess.run(
            command, shell=True, cwd=self.base,
            env={**os.environ, "PLUGIN_ROOT": str(self.plugin)},
            input=json.dumps(payload).encode() if raw is None else raw,
            capture_output=True, timeout=5, check=True,
        )
        self.assertEqual(result.stderr, b"")
        return json.loads(result.stdout)

    def test_start_loads_judgment_and_unconfirmed_evidence(self):
        output = self.run_hook("UserPromptSubmit")["hookSpecificOutput"]
        self.assertEqual(output["hookEventName"], "UserPromptSubmit")
        self.assertIn("SOUL.md", output["additionalContext"])
        self.assertIn(".local/", output["additionalContext"])
        self.assertIn("$ethos", output["additionalContext"])

    def test_stop_requests_one_pass_and_continuation_finishes(self):
        first = self.run_hook()
        self.assertEqual(first["decision"], "block")
        self.assertIn("already complete", first["reason"])
        self.assertNotIn("hookSpecificOutput", first)
        self.assertEqual(self.run_hook(payload={"hook_event_name": "Stop", "cwd": str(self.project), "stop_hook_active": True}), {})

    def test_missing_or_non_boolean_flags_never_continue(self):
        for flag in (None, 0, 1, "false", [], {}):
            with self.subTest(flag=flag):
                self.assertEqual(self.run_hook(payload={"hook_event_name": "Stop", "cwd": str(self.project), "stop_hook_active": flag}), {})

    def test_invalid_payloads_fail_open(self):
        for raw in (b"", b"{", b"[]", b"null", b"false", b"\xff", b"x" * 1_048_577, b"[" * 2000 + b"]" * 2000):
            with self.subTest(raw=raw[:20]):
                self.assertEqual(self.run_hook(raw=raw), {})
        self.assertEqual(self.run_hook(payload={"hook_event_name": "Unknown", "cwd": str(self.project), "stop_hook_active": False}), {})

    def test_invalid_or_unscoped_cwd_does_not_continue(self):
        for cwd in (None, "", ".", str(self.base), str(self.base / "missing"), "bad\x00path"):
            with self.subTest(cwd=cwd):
                for event in ("Stop", "UserPromptSubmit"):
                    self.assertEqual(self.run_hook(event, payload={"hook_event_name": event, "cwd": cwd, "stop_hook_active": False}), {})

    def test_nested_directory_worktree_and_non_git_ethos_project(self):
        (self.project / ".git").rmdir()
        (self.project / ".git").write_text("gitdir: ../somewhere")
        nested = self.project / "nested"
        nested.mkdir()
        payload = {"hook_event_name": "Stop", "cwd": str(nested), "stop_hook_active": False}
        self.assertEqual(self.run_hook(payload=payload)["decision"], "block")
        (self.project / ".git").unlink()
        (self.project / ".proj-ethos").mkdir()
        self.assertEqual(self.run_hook(payload=payload)["decision"], "block")

    def test_read_only_scope_and_no_file_mutations(self):
        knowledge = self.project / ".proj-ethos"
        knowledge.mkdir()
        (knowledge / "SOUL.md").write_text("existing judgment")
        before = {str(p.relative_to(self.base)): p.read_bytes() for p in self.base.rglob("*") if p.is_file()}
        payload = {"hook_event_name": "Stop", "cwd": str(self.project), "stop_hook_active": False, "permission_mode": "plan", "transcript_path": str(self.project / "missing-transcript")}
        self.assertIn("read-only", self.run_hook(payload=payload)["reason"])
        self.run_hook("UserPromptSubmit")
        after = {str(p.relative_to(self.base)): p.read_bytes() for p in self.base.rglob("*") if p.is_file()}
        self.assertEqual(before, after)


if __name__ == "__main__":
    unittest.main()
