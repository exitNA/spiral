#!/usr/bin/env python3
"""Validate the Spiral marketplace, plugins, skills, and file hygiene."""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SEMVER = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-[0-9A-Za-z.-]+)?$")
PLUGIN_SPECS = {
    "ethos": {"path": Path("ethos/plugins/ethos"), "skill": "ethos", "hook": True},
    "loop": {"path": Path("loop"), "skill": "loop", "hook": False},
}
FORBIDDEN_NAMES = {".DS_Store", ".env", ".npmrc", ".pypirc", ".netrc", "Thumbs.db", "credentials.json"}
FORBIDDEN_SUFFIXES = {".key", ".p12", ".pfx", ".jks", ".keystore", ".pem", ".log", ".swp", ".swo", ".temp", ".tmp"}
FORBIDDEN_DIRECTORIES = {".cache", ".idea", ".mypy_cache", ".pytest_cache", ".ruff_cache", ".venv", ".vscode", "__pycache__", "build", "coverage", "dist", "node_modules", "secrets", "temp", "tmp", "venv"}


class ValidationError(RuntimeError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValidationError(message)


def load_json(path: Path) -> object:
    require(path.is_file(), f"missing required file: {path.relative_to(ROOT)}")
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        raise ValidationError(f"invalid JSON in {path.relative_to(ROOT)}: {error}") from error


def repository_files() -> list[Path]:
    result = subprocess.run(["git", "ls-files", "--cached", "--others", "--exclude-standard"], cwd=ROOT, check=True, capture_output=True, text=True)
    return [ROOT / line for line in result.stdout.splitlines() if line]


def validate_file_hygiene(files: list[Path]) -> None:
    for path in files:
        relative = path.relative_to(ROOT)
        require(not any(part in FORBIDDEN_DIRECTORIES for part in relative.parts), f"generated directory found: {relative}")
        require(path.name.lower() not in FORBIDDEN_NAMES, f"forbidden filename found: {relative}")
        require(path.suffix.lower() not in FORBIDDEN_SUFFIXES, f"forbidden file suffix found: {relative}")
        if path != Path(__file__) and path.suffix.lower() in {".json", ".md", ".py", ".toml", ".yaml", ".yml"} and path.is_file():
            require("/Users/" not in path.read_text(encoding="utf-8"), f"personal absolute path found: {relative}")


def validate_marketplace() -> None:
    marketplace = load_json(ROOT / ".agents/plugins/marketplace.json")
    require(isinstance(marketplace, dict), "marketplace must be a JSON object")
    require(marketplace.get("name") == "spiral", "marketplace name must be spiral")
    plugins = marketplace.get("plugins")
    require(isinstance(plugins, list) and len(plugins) == len(PLUGIN_SPECS), "marketplace must list exactly two plugins")
    entries = {item.get("name"): item for item in plugins if isinstance(item, dict)}
    require(set(entries) == set(PLUGIN_SPECS), "marketplace must list ethos and loop exactly once")
    for name, plugin in entries.items():
        expected_path = f"./{PLUGIN_SPECS[name]['path']}"
        require(plugin.get("source") == {"source": "local", "path": expected_path}, f"invalid source path for {name}")


def skill_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    end = text.find("\n---\n", 4)
    require(text.startswith("---\n") and end != -1, f"invalid Skill frontmatter: {path.relative_to(ROOT)}")
    return {key.strip(): value.strip() for key, value in (line.split(":", 1) for line in text[4:end].splitlines() if ":" in line)}


def validate_hook(path: Path) -> None:
    hooks = load_json(path)
    require(isinstance(hooks, dict), "hooks manifest must be a JSON object")
    try:
        hook = hooks["hooks"]["UserPromptSubmit"][0]["hooks"][0]
        command = hook["command"]
        windows_command = hook["commandWindows"]
    except (KeyError, IndexError, TypeError) as error:
        raise ValidationError("hooks.json must define cross-platform UserPromptSubmit commands") from error
    require(isinstance(command, str) and command and isinstance(windows_command, str) and "$ethos" in windows_command, "invalid Ethos hook commands")
    result = subprocess.run(command, cwd=ROOT, shell=True, executable="/bin/sh", check=True, capture_output=True, text=True, timeout=5)
    output = json.loads(result.stdout)
    hook_output = output["hookSpecificOutput"]
    require(hook_output.get("hookEventName") == "UserPromptSubmit", "hook event name is inconsistent")
    require(isinstance(hook_output.get("additionalContext"), str) and "$ethos" in hook_output["additionalContext"], "hook context must invoke Ethos")


def validate_plugin(name: str, spec: dict[str, object]) -> None:
    plugin_root = ROOT / spec["path"]
    manifest = load_json(plugin_root / ".codex-plugin/plugin.json")
    require(isinstance(manifest, dict) and manifest.get("name") == name, f"invalid {name} plugin manifest")
    version = manifest.get("version")
    require(isinstance(version, str) and SEMVER.fullmatch(version), f"invalid {name} plugin version")
    require(manifest.get("skills") == "./skills/", f"{name} plugin must expose ./skills/")
    interface = manifest.get("interface")
    require(isinstance(interface, dict), f"{name} plugin interface is required")
    for key in ("displayName", "shortDescription", "longDescription", "developerName"):
        require(isinstance(interface.get(key), str) and interface[key].strip(), f"{name} interface.{key} is required")
    prompts = interface.get("defaultPrompt")
    require(isinstance(prompts, list) and 1 <= len(prompts) <= 3 and all(isinstance(prompt, str) and prompt.strip() for prompt in prompts), f"invalid {name} default prompts")

    skill_root = plugin_root / "skills" / spec["skill"]
    require(skill_root.is_dir(), f"missing {name} Skill directory")
    frontmatter = skill_frontmatter(skill_root / "SKILL.md")
    require(frontmatter.get("name") == spec["skill"] and frontmatter.get("description"), f"invalid {name} Skill metadata")
    agent_config = skill_root / "agents/openai.yaml"
    require(agent_config.is_file(), f"missing {name} Skill agent config")
    agent_text = agent_config.read_text(encoding="utf-8")
    require(f'display_name: "{spec["skill"].capitalize()}"' in agent_text, f"invalid {name} agent display name")
    require(f"${spec['skill']}" in agent_text, f"{name} agent invocation is missing")
    if name == "loop":
        runtime = skill_root / "scripts/loop_runtime.py"
        compile(runtime.read_text(encoding="utf-8"), str(runtime), "exec")
        subprocess.run([sys.executable, str(runtime), "--help"], cwd=ROOT, check=True, capture_output=True, text=True, timeout=5)
    if spec["hook"]:
        validate_hook(plugin_root / "hooks/hooks.json")


def main() -> int:
    try:
        files = repository_files()
        validate_file_hygiene(files)
        validate_marketplace()
        for name, spec in PLUGIN_SPECS.items():
            validate_plugin(name, spec)
    except (ValidationError, subprocess.CalledProcessError, subprocess.TimeoutExpired, UnicodeDecodeError, json.JSONDecodeError) as error:
        print(f"validation failed: {error}", file=sys.stderr)
        return 1
    print(f"validation passed: {len(files)} repository files checked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
