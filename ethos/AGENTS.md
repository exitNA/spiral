# Project guidance

Read `PROJECT-MIND.md` before changing the plugin's delivery model, learning model, routing rules, trigger behavior, or public interface. Use `$ethos` when evidence changes the project's durable judgment.

Keep one standard marketplace plugin at `plugins/ethos/` with two Skills: `$loop` owns intent-to-verified-code delivery, and `$ethos` owns durable project-judgment evolution. Loop may invoke Ethos; it must not duplicate Ethos's knowledge model.

Keep Hook detection separate from canonicalization. The Hook may surface candidates; only `$ethos` decides whether and where durable knowledge is written.

Before release, run `python3 scripts/validate_repository.py` and Gitleaks. Keep development-only material outside the distributable plugin directory, never commit real credentials or local environment files, and keep CI green.
