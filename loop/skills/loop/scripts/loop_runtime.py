#!/usr/bin/env python3
"""Small persistent runtime telemetry helper for the $loop skill.

Stores run telemetry outside the repo under $CODEX_HOME/loop-runtime or
~/.codex/loop-runtime. Standard library only.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any


def now_local() -> datetime:
    """Return the current time with the host's local timezone attached."""
    return datetime.now().astimezone()


def now_iso() -> str:
    return now_local().isoformat(timespec="seconds")


def now_ts() -> float:
    return datetime.now().timestamp()


def repo_root(cwd: Path) -> Path:
    p = cwd.resolve()
    for cur in [p, *p.parents]:
        if (cur / ".git").exists():
            return cur
    return p


def runtime_root() -> Path:
    codex_home = os.environ.get("CODEX_HOME")
    if codex_home:
        return Path(codex_home).expanduser() / "loop-runtime"
    return Path.home() / ".codex" / "loop-runtime"


def repo_key(root: Path) -> str:
    return hashlib.sha1(str(root).encode("utf-8")).hexdigest()[:16]


def repo_dir(cwd: Path) -> Path:
    root = repo_root(cwd)
    d = runtime_root() / repo_key(root)
    d.mkdir(parents=True, exist_ok=True)
    meta = d / "repo.json"
    if not meta.exists():
        meta.write_text(json.dumps({"repo_root": str(root), "created_at": now_iso()}, indent=2), encoding="utf-8")
    return d


def current_run_id(d: Path) -> str:
    p = d / "current.json"
    if not p.exists():
        raise SystemExit("No active loop run. Run `init` first.")
    data = json.loads(p.read_text(encoding="utf-8"))
    rid = data.get("run_id")
    if not rid:
        raise SystemExit("Invalid current run pointer.")
    return rid


def run_dir(d: Path, run_id: str | None = None) -> Path:
    rid = run_id or current_run_id(d)
    rd = d / "runs" / rid
    if not rd.exists():
        raise SystemExit(f"Unknown run: {rid}")
    return rd


def append_event(rd: Path, event_type: str, **data: Any) -> dict[str, Any]:
    evt = {"ts": now_ts(), "time": now_iso(), "type": event_type, **{k: v for k, v in data.items() if v is not None}}
    with (rd / "events.jsonl").open("a", encoding="utf-8") as f:
        f.write(json.dumps(evt, ensure_ascii=False) + "\n")
    return evt


def read_events(rd: Path) -> list[dict[str, Any]]:
    p = rd / "events.jsonl"
    if not p.exists():
        return []
    out = []
    for line in p.read_text(encoding="utf-8").splitlines():
        if line.strip():
            try:
                out.append(json.loads(line))
            except json.JSONDecodeError:
                pass
    return out


def read_meta(rd: Path) -> dict[str, Any]:
    return json.loads((rd / "meta.json").read_text(encoding="utf-8"))


def phase_durations(events: list[dict[str, Any]]) -> dict[str, float]:
    starts: dict[str, list[float]] = defaultdict(list)
    total: dict[str, float] = defaultdict(float)
    for e in events:
        name = str(e.get("name", "unknown"))
        if e.get("type") == "phase_start":
            starts[name].append(float(e["ts"]))
        elif e.get("type") == "phase_end" and starts[name]:
            st = starts[name].pop()
            total[name] += max(0.0, float(e["ts"]) - st)
    return {k: round(v, 1) for k, v in total.items()}


def task_summary(events: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    starts: dict[str, dict[str, Any]] = {}
    tasks: list[dict[str, Any]] = []
    for e in events:
        if e.get("type") == "task_start":
            starts[str(e.get("task"))] = e
        elif e.get("type") == "task_end":
            tid = str(e.get("task"))
            st = starts.get(tid)
            row = {
                "task": tid,
                "status": e.get("status", "unknown"),
                "kind": (st or {}).get("kind", e.get("kind", "unknown")),
                "agent": (st or {}).get("agent", e.get("agent", "unknown")),
                "duration_sec": round(max(0.0, float(e["ts"]) - float(st["ts"])), 1) if st else None,
                "rework": int(e.get("rework", 0) or 0),
                "conflicts": int(e.get("conflicts", 0) or 0),
                "note": e.get("note"),
            }
            tasks.append(row)

    completed = [t for t in tasks if t["status"] in {"success", "failed", "blocked"}]
    successes = [t for t in completed if t["status"] == "success"]
    failed = [t for t in completed if t["status"] == "failed"]
    blocked = [t for t in completed if t["status"] == "blocked"]
    reworked = [t for t in completed if t["rework"] > 0]
    conflicts = sum(t["conflicts"] for t in completed)
    timed = [t["duration_sec"] for t in completed if t["duration_sec"] is not None]
    by_kind: dict[str, list[float]] = defaultdict(list)
    for t in completed:
        if t["duration_sec"] is not None:
            by_kind[str(t["kind"])].append(float(t["duration_sec"]))

    stats = {
        "completed": len(completed),
        "success": len(successes),
        "failed": len(failed),
        "blocked": len(blocked),
        "first_pass_success_rate": round((len([t for t in successes if t["rework"] == 0]) / len(successes)), 3) if successes else None,
        "rework_rate": round((len(reworked) / len(completed)), 3) if completed else None,
        "conflicts": conflicts,
        "task_runtime_sum_sec": round(sum(timed), 1),
        "avg_task_sec": round(sum(timed) / len(timed), 1) if timed else None,
        "avg_by_kind_sec": {k: round(sum(v) / len(v), 1) for k, v in by_kind.items()},
    }
    return tasks, stats


def summarize(rd: Path) -> dict[str, Any]:
    meta = read_meta(rd)
    events = read_events(rd)
    tasks, stats = task_summary(events)
    end_ts = meta.get("ended_ts") or now_ts()
    elapsed = max(0.0, float(end_ts) - float(meta["started_ts"]))
    event_counts = Counter(str(e.get("type")) for e in events)
    defect_counts = Counter(str(e.get("severity", "unspecified")) for e in events if e.get("type") == "review_defect")
    parallelism_ratio = None
    if elapsed > 0 and stats["task_runtime_sum_sec"]:
        parallelism_ratio = round(float(stats["task_runtime_sum_sec"]) / elapsed, 2)

    summary = {
        "run_id": meta["run_id"],
        "goal": meta.get("goal"),
        "status": meta.get("status", "running"),
        "started_at": meta.get("started_at"),
        "ended_at": meta.get("ended_at"),
        "elapsed_sec": round(elapsed, 1),
        "phases_sec": phase_durations(events),
        "tasks": stats,
        "parallelism_ratio": parallelism_ratio,
        "events": dict(event_counts),
        "review_defects": dict(defect_counts),
    }
    summary["policy_hints"] = policy_hints(summary, tasks)
    return summary


def policy_hints(summary: dict[str, Any], tasks: list[dict[str, Any]]) -> list[str]:
    hints: list[str] = []
    stats = summary["tasks"]
    events = summary["events"]
    impl = [t for t in tasks if t.get("kind") == "implement"]

    if stats.get("conflicts", 0) > 0 or events.get("conflict", 0) > 0:
        hints.append("reduce write concurrency in contended modules; define/stabilize shared contracts before the next parallel write batch")

    rw = stats.get("rework_rate")
    if rw is not None and rw >= 0.25:
        hints.append("shrink implementation task scope and strengthen acceptance criteria/tests in worker briefs")

    fps = stats.get("first_pass_success_rate")
    if fps is not None and fps < 0.7:
        hints.append("add earlier contract/reproduction checks and use stronger reasoning/review on critical-path tasks")

    if events.get("verification_failure", 0) >= 2:
        hints.append("move targeted verification earlier; classify deterministic vs environmental failures before rerunning broad suites")

    high_defects = int(summary.get("review_defects", {}).get("critical", 0)) + int(summary.get("review_defects", {}).get("high", 0))
    if high_defects > 0:
        hints.append("promote the blocking review defect class into task acceptance criteria or an executable regression check")

    impl_times = [float(t["duration_sec"]) for t in impl if t.get("duration_sec") is not None]
    if len(impl_times) >= 3:
        s = sorted(impl_times)
        median = s[len(s)//2]
        if median > 0 and max(s) >= median * 2.5:
            hints.append("split long-tail implementation tasks or expose their hidden dependencies before dispatch")
        if median < 90 and len(impl_times) >= 6:
            hints.append("implementation tasks may be too fine-grained; bundle adjacent low-risk work that shares the same module/verifier")

    if not hints:
        hints.append("no strong process regression detected; keep current decomposition/concurrency unless new evidence suggests otherwise")
    return hints


def update_profile(d: Path, summary: dict[str, Any]) -> dict[str, Any]:
    p = d / "profile.json"
    if p.exists():
        try:
            profile = json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            profile = {}
    else:
        profile = {}

    history = profile.get("recent_runs", [])
    history.append({
        "run_id": summary["run_id"],
        "status": summary["status"],
        "elapsed_sec": summary["elapsed_sec"],
        "tasks": summary["tasks"],
        "policy_hints": summary["policy_hints"],
        "ended_at": summary.get("ended_at") or now_iso(),
    })
    profile["recent_runs"] = history[-8:]

    counts: Counter[str] = Counter()
    for r in profile["recent_runs"]:
        for h in r.get("policy_hints", []):
            if h != "no strong process regression detected; keep current decomposition/concurrency unless new evidence suggests otherwise":
                counts[h] += 1

    durable = [h for h, c in counts.most_common(12) if c >= 2]
    profile["durable_hints"] = durable
    profile["last_updated"] = now_iso()
    p.write_text(json.dumps(profile, indent=2, ensure_ascii=False), encoding="utf-8")
    return profile


def cmd_init(args: argparse.Namespace) -> None:
    cwd = Path(args.cwd or os.getcwd())
    d = repo_dir(cwd)
    rid = now_local().strftime("%Y%m%d-%H%M%S") + f"-{os.getpid()}"
    rd = d / "runs" / rid
    rd.mkdir(parents=True, exist_ok=False)
    meta = {
        "run_id": rid,
        "goal": args.goal,
        "repo_root": str(repo_root(cwd)),
        "started_at": now_iso(),
        "started_ts": now_ts(),
        "status": "running",
    }
    (rd / "meta.json").write_text(json.dumps(meta, indent=2, ensure_ascii=False), encoding="utf-8")
    (rd / "events.jsonl").touch()
    (d / "current.json").write_text(json.dumps({"run_id": rid}, indent=2), encoding="utf-8")
    profile = {}
    pp = d / "profile.json"
    if pp.exists():
        try:
            profile = json.loads(pp.read_text(encoding="utf-8"))
        except Exception:
            pass
    print(json.dumps({"run_id": rid, "state_dir": str(rd), "durable_hints": profile.get("durable_hints", [])}, indent=2, ensure_ascii=False))


def get_rd(args: argparse.Namespace) -> tuple[Path, Path]:
    cwd = Path(getattr(args, "cwd", None) or os.getcwd())
    d = repo_dir(cwd)
    return d, run_dir(d, getattr(args, "run", None))


def cmd_phase_start(args: argparse.Namespace) -> None:
    _, rd = get_rd(args)
    print(json.dumps(append_event(rd, "phase_start", name=args.name), ensure_ascii=False))


def cmd_phase_end(args: argparse.Namespace) -> None:
    _, rd = get_rd(args)
    print(json.dumps(append_event(rd, "phase_end", name=args.name, status=args.status, note=args.note), ensure_ascii=False))


def cmd_task_start(args: argparse.Namespace) -> None:
    _, rd = get_rd(args)
    print(json.dumps(append_event(rd, "task_start", task=args.task, agent=args.agent, kind=args.kind, note=args.note), ensure_ascii=False))


def cmd_task_end(args: argparse.Namespace) -> None:
    _, rd = get_rd(args)
    print(json.dumps(append_event(rd, "task_end", task=args.task, status=args.status, rework=args.rework, conflicts=args.conflicts, note=args.note), ensure_ascii=False))


def cmd_event(args: argparse.Namespace) -> None:
    _, rd = get_rd(args)
    print(json.dumps(append_event(rd, args.type, task=args.task, severity=args.severity, value=args.value, note=args.note), ensure_ascii=False))


def cmd_snapshot(args: argparse.Namespace) -> None:
    _, rd = get_rd(args)
    print(json.dumps(summarize(rd), indent=2, ensure_ascii=False))


def cmd_profile(args: argparse.Namespace) -> None:
    cwd = Path(args.cwd or os.getcwd())
    d = repo_dir(cwd)
    p = d / "profile.json"
    if not p.exists():
        print(json.dumps({"durable_hints": [], "recent_runs": []}, indent=2))
        return
    print(p.read_text(encoding="utf-8"))


def cmd_finish(args: argparse.Namespace) -> None:
    d, rd = get_rd(args)
    meta = read_meta(rd)
    meta["status"] = args.status
    meta["ended_at"] = now_iso()
    meta["ended_ts"] = now_ts()
    if args.note:
        meta["note"] = args.note
    (rd / "meta.json").write_text(json.dumps(meta, indent=2, ensure_ascii=False), encoding="utf-8")
    append_event(rd, "run_end", status=args.status, note=args.note)
    summary = summarize(rd)
    (rd / "summary.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
    with (d / "history.jsonl").open("a", encoding="utf-8") as f:
        f.write(json.dumps(summary, ensure_ascii=False) + "\n")
    update_profile(d, summary)
    cur = d / "current.json"
    if cur.exists():
        try:
            if json.loads(cur.read_text(encoding="utf-8")).get("run_id") == meta["run_id"]:
                cur.unlink()
        except Exception:
            pass
    print(json.dumps(summary, indent=2, ensure_ascii=False))


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Telemetry helper for the $loop skill")
    sub = p.add_subparsers(dest="command", required=True)

    s = sub.add_parser("init")
    s.add_argument("--goal", required=True)
    s.add_argument("--cwd")
    s.set_defaults(func=cmd_init)

    for name, func in [("phase-start", cmd_phase_start), ("phase-end", cmd_phase_end)]:
        s = sub.add_parser(name)
        s.add_argument("name")
        s.add_argument("--run")
        s.add_argument("--cwd")
        if name == "phase-end":
            s.add_argument("--status", default="success")
            s.add_argument("--note")
        s.set_defaults(func=func)

    s = sub.add_parser("task-start")
    s.add_argument("task")
    s.add_argument("--agent", default="primary")
    s.add_argument("--kind", default="implement")
    s.add_argument("--note")
    s.add_argument("--run")
    s.add_argument("--cwd")
    s.set_defaults(func=cmd_task_start)

    s = sub.add_parser("task-end")
    s.add_argument("task")
    s.add_argument("--status", choices=["success", "failed", "blocked"], default="success")
    s.add_argument("--rework", type=int, default=0)
    s.add_argument("--conflicts", type=int, default=0)
    s.add_argument("--note")
    s.add_argument("--run")
    s.add_argument("--cwd")
    s.set_defaults(func=cmd_task_end)

    s = sub.add_parser("event")
    s.add_argument("type")
    s.add_argument("--task")
    s.add_argument("--severity")
    s.add_argument("--value")
    s.add_argument("--note")
    s.add_argument("--run")
    s.add_argument("--cwd")
    s.set_defaults(func=cmd_event)

    s = sub.add_parser("snapshot")
    s.add_argument("--run")
    s.add_argument("--cwd")
    s.set_defaults(func=cmd_snapshot)

    s = sub.add_parser("profile")
    s.add_argument("--cwd")
    s.set_defaults(func=cmd_profile)

    s = sub.add_parser("finish")
    s.add_argument("--status", choices=["success", "partial", "blocked", "failed"], default="success")
    s.add_argument("--note")
    s.add_argument("--run")
    s.add_argument("--cwd")
    s.set_defaults(func=cmd_finish)

    return p


def main() -> None:
    args = parser().parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
