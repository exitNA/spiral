# Ethos

Ethos is a Codex plugin for delivering software and evolving the judgment behind it. It exposes two complementary Skill entry points:

- `$loop <outcome>` owns intent expansion, implementation, verification, repair, and end-to-end delivery.
- `$ethos` distills durable project intent, mental models, taste, decisions, collaboration norms, and proven practice into the right repository authority.

Use either Skill directly. During a substantial `$loop` run, Loop calls Ethos when delivery evidence may have changed the project's durable judgment.

## Mental model

- The delivery loop turns intent into verified outcomes.
- The evolution loop turns durable evidence into better future judgment.
- The Hook performs cheap learning-candidate detection on each user turn.
- `$ethos` performs conservative semantic evaluation, reconciliation, routing, and pruning.
- Project doctrine or `PROJECT-MIND.md` holds the current synthesis; ADRs preserve consequential rationale; code and tooling enforce machine-checkable facts.
- Process telemetry may improve future scheduling, but checked-in project knowledge remains authoritative.

See [`PROJECT-MIND.md`](PROJECT-MIND.md) for the project's principles and quality bar.

## Repository layout

```text
.agents/plugins/marketplace.json
plugins/ethos/
  .codex-plugin/plugin.json
  hooks/hooks.json
  skills/
    ethos/
    loop/
```

The repository is both the plugin's source project and a one-plugin Codex marketplace.

## Install from this checkout

```bash
codex plugin marketplace add /path/to/ethos
codex plugin add ethos@ethos
```

## Install from GitHub

After the repository is published:

```bash
codex plugin marketplace add https://github.com/exitNA/ethos.git
codex plugin add ethos@ethos
```

Start a new Codex task after installation so both Skills and the Hook are loaded.

## Use

```text
$loop 给登录页加上记住密码，并完成验证
$ethos 把这次架构取舍沉淀成项目今后的判断规则
```

`$loop` is explicit-only because invoking it authorizes a full development workflow. `$ethos` supports direct and implicit invocation; the Hook only asks it to evaluate high-confidence learning candidates.

## Validate

```bash
python3 scripts/validate_repository.py
gitleaks dir --redact --no-banner .
```

The repository validator checks marketplace and plugin metadata, both Skill packages, the executable Hook protocol, Loop runtime syntax, stable release versioning, and dangerous committed filenames. GitHub Actions runs the same validation and scans full Git history with Gitleaks.

## Development status

Version `0.1.0` establishes the integrated Loop/Ethos model, automatic learning detection, project knowledge templates, process telemetry, cross-platform Hook commands, and standard marketplace packaging. Broader behavioral scenario coverage remains release-hardening work.
