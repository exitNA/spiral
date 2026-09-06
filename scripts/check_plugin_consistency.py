#!/usr/bin/env python3
"""Read-only source/cache comparison. Exit 0=equal, 1=different, 2=error.

This checks disk contents, not installation enablement or session activation.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import sys


IGNORED = {".git", "__pycache__", ".DS_Store", "Thumbs.db"}


def manifest(root: Path) -> dict:
    value = json.loads((root / ".codex-plugin/plugin.json").read_text(encoding="utf-8"))
    if not isinstance(value, dict) or not all(
        isinstance(value.get(key), str) and value[key] for key in ("name", "version")
    ):
        raise ValueError(f"无效的插件清单：{root}")
    return value


def inventory(root: Path) -> dict[str, str]:
    result = {}

    def visit(directory: Path) -> None:
        for path in sorted(directory.iterdir()):
            if path.name in IGNORED:
                continue
            if path.is_symlink():
                raise ValueError(f"发现符号链接，请先确认真实文件边界：{path}")
            if path.is_dir():
                visit(path)
            elif path.is_file():
                digest = hashlib.sha256()
                with path.open("rb") as stream:
                    for chunk in iter(lambda: stream.read(1024 * 1024), b""):
                        digest.update(chunk)
                result[path.relative_to(root).as_posix()] = digest.hexdigest()
            else:
                raise ValueError(f"不支持的文件类型：{path}")

    visit(root)
    return result


def fingerprint(files: dict[str, str]) -> str:
    data = json.dumps(files, sort_keys=True, ensure_ascii=True, separators=(",", ":"))
    return hashlib.sha256(data.encode("utf-8")).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description="只读比较插件源码与缓存；不能证明当前任务已加载插件。")
    parser.add_argument("--source", type=Path, default=Path(__file__).resolve().parents[1] / "loop",
                        help="插件源码目录，默认本仓库 loop")
    parser.add_argument("--cache", type=Path, help="明确指定缓存版本目录；存在多个版本时必须指定")
    parser.add_argument("--marketplace", default="spiral", help="缓存 marketplace，默认 spiral")
    parser.add_argument("--codex-home", type=Path,
                        default=Path(os.environ.get("CODEX_HOME") or Path.home() / ".codex"))
    parser.add_argument("--json", action="store_true", help="输出包含逐文件 SHA-256 的 JSON")
    args = parser.parse_args()
    try:
        source = args.source.expanduser().resolve(strict=True)
        source_meta = manifest(source)
        if args.cache:
            cache = args.cache.expanduser().resolve(strict=True)
        else:
            for component in (args.marketplace, source_meta["name"]):
                if component in {".", ".."} or any(c in component for c in ("/", "\\")):
                    raise ValueError("marketplace 和插件名必须是单个目录名")
            parent = args.codex_home.expanduser() / "plugins/cache" / args.marketplace / source_meta["name"]
            candidates = sorted(p for p in parent.iterdir()
                                if p.is_dir() and (p / ".codex-plugin/plugin.json").is_file()) if parent.is_dir() else []
            if len(candidates) != 1:
                options = ", ".join(str(p) for p in candidates) or "无"
                raise ValueError(f"发现 {len(candidates)} 个缓存版本，不能推断当前使用版本。请用 --cache 指定。候选：{options}")
            cache = candidates[0].resolve(strict=True)
        if source == cache:
            raise ValueError("源码和缓存指向同一目录，无法验证独立安装副本")
        cache_meta = manifest(cache)
        left, right = inventory(source), inventory(cache)
        differences = []
        for name in sorted(left.keys() | right.keys()):
            if left.get(name) != right.get(name):
                kind = "cache_only" if name not in left else "missing_in_cache" if name not in right else "changed"
                differences.append({"path": name, "kind": kind,
                                    "source_sha256": left.get(name), "cache_sha256": right.get(name)})
        report = {
            "equal": not differences,
            "scope": "disk_contents_only",
            "session_loaded": "not_checked",
            "ignored_names": sorted(IGNORED),
            "source": {"path": str(source), "name": source_meta["name"],
                       "version": source_meta["version"], "fingerprint": fingerprint(left), "files": left},
            "cache": {"path": str(cache), "name": cache_meta["name"],
                      "version": cache_meta["version"], "fingerprint": fingerprint(right), "files": right},
            "differences": differences,
        }
        if args.json:
            print(json.dumps(report, ensure_ascii=False, indent=2))
        else:
            print(f"源码：{source}（{source_meta['name']} {source_meta['version']}，{len(left)} 文件）")
            print(f"缓存：{cache}（{cache_meta['name']} {cache_meta['version']}，{len(right)} 文件）")
            print(f"源码指纹：{fingerprint(left)}")
            print(f"缓存指纹：{fingerprint(right)}")
            print("忽略：" + ", ".join(sorted(IGNORED)))
            labels = {"cache_only": "缓存多出", "missing_in_cache": "缓存缺失", "changed": "内容不同"}
            for item in differences:
                print(f"  {labels[item['kind']]}：{item['path']}")
            print("结果：内容一致" if not differences else f"结果：不一致，共 {len(differences)} 项差异")
            print("范围：只检查磁盘内容；不证明插件已启用或当前任务已加载。")
        return 1 if differences else 0
    except (OSError, ValueError) as error:
        if args.json:
            print(json.dumps({"error": str(error)}, ensure_ascii=False))
        else:
            print(f"检查失败：{error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
