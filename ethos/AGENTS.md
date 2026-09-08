# Project guidance

Read `../.ethos/SOUL.md` before changing the plugin's delivery model, learning model, routing rules, trigger behavior, or public interface. Use `$ethos` when evidence changes the project's durable judgment.

Keep Ethos and Loop as independent plugins in the Spiral marketplace. Loop owns delivery and optionally uses an available Ethos skill for project judgment. Codex can implicitly select Ethos to evaluate and integrate qualifying learning in ordinary conversations and Loop runs; explicit invocation is also supported. Implicit selection does not guarantee screening on every turn. Neither plugin requires the other.

Keep learning within the normal task. Do not add per-message Hook reminders, completion-blocking feedback, or learning-only continuations to the main conversation. The selected skill decides whether and where durable knowledge is written and completes its learning check before the normal final response.

Before release, run `python3 scripts/validate_repository.py` from the Spiral repository root and Gitleaks. Keep development-only material outside the distributable plugin directory, never commit real credentials or local environment files, and keep CI green.
