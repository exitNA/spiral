# Project stage, compatibility, and migration policy

## Core rule

Project maturity is defined by **deployment/use state**, not repository history.

A repository with a large codebase, many commits, old implementations, release scripts, or extensive tests is still a **new/pre-production project** if the product has not actually been deployed to production.

## Stage detection

Look for authoritative evidence such as:

- explicit project/user statement that production is live;
- known production deployment records or active production environment;
- real users/external clients depending on current behavior;
- persisted production/shared data that must survive upgrades;
- external API/integration contracts already consumed outside the development project.

Do not treat these alone as proof of production:

- repository age or commit count;
- existence of CI/CD, Dockerfiles, Kubernetes manifests, Terraform, release scripts, or production-like config;
- old code, compatibility comments, version numbers, tags, or changelog entries;
- staging/dev deployments.

If the stage remains uncertain, continue ordinary reversible work without adding legacy compatibility. Ask one minimal question only before an irreversible/destructive or externally incompatible decision whose correctness depends on production status.

## Pre-production/new project

Goal: converge rapidly toward one clean current design.

Prefer:

- replace/refactor outdated internal APIs rather than preserve them;
- update all internal callers together;
- delete superseded implementations;
- simplify schemas/interfaces before they become external contracts;
- change technology choices when a better mainstream production-grade option materially improves the project;
- remove obsolete compatibility branches and transitional adapters;
- establish a coarse whole-system path early, validate the overall direction, then progressively refine local detail.

Avoid:

- deprecated internal versions for hypothetical users;
- dual old/new code paths without real consumers;
- reading/writing multiple historical data formats that never became durable state;
- maintaining obsolete config aliases solely because they once existed in git;
- preserving weak demo architecture because it has many lines of code.

## Production project

Goal: improve the product without breaking real users, consumers, or durable state.

Identify what is actually a compatibility contract:

- public/external APIs;
- client versions in the field;
- persisted user/business data;
- message/event formats consumed by other systems;
- rolling-deployment/inter-version constraints;
- user-visible behavior relied on operationally;
- integrations, automation, and documented extension points.

Preserve or deliberately migrate these. Internal implementation details that have no external/durable dependency may still be refactored freely.

## Database migration exception

Database migrations represent ordered state transitions once applied.

If a migration has been applied to any durable/shared environment that matters:

1. inspect the latest applied/intended schema state;
2. modify ORM/models to represent the desired latest state;
3. add a forward migration/corrective migration;
4. test upgrade paths and data preservation when material;
5. never rewrite applied migration history merely to make development cleaner.

If migrations exist only as unused pre-production files and have never been applied to any meaningful shared/durable environment, they may be squashed or rewritten when repository rules allow and a clean baseline is better.

## Review question

Before adding compatibility code, ask internally:

> What real deployed consumer, user-visible behavior, persisted state, or applied migration requires this compatibility?

If there is no concrete answer in a pre-production project, prefer deleting the compatibility layer.
