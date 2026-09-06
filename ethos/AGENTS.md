# Project guidance

Read `../.proj-ethos/SOUL.md` before changing the plugin's delivery model, learning model, routing rules, trigger behavior, or public interface. Use `$ethos` when evidence changes the project's durable judgment.

Keep Ethos and Loop as independent plugins in the Spiral marketplace. Loop owns delivery and optionally uses an available Ethos skill for project judgment. Ethos automatically evaluates and integrates qualifying learning in ordinary conversations and Loop runs, and also supports explicit invocation. Neither plugin requires the other.

Keep Hook detection separate from canonicalization. The Hook may surface candidates; only `$ethos` decides whether and where durable knowledge is written.

Before release, run `python3 scripts/validate_repository.py` from the Spiral repository root and Gitleaks. Keep development-only material outside the distributable plugin directory, never commit real credentials or local environment files, and keep CI green.
