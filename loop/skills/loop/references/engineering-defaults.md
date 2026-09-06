# Production-grade engineering defaults

Use these defaults only when higher-authority user/project requirements do not already decide the stack.

## Technology selection

Do not optimize for the easiest demo. Optimize for a durable industrial solution.

Evaluate:

- current maintenance and ecosystem health;
- production adoption and operational maturity;
- security posture and update cadence;
- platform integration;
- performance/resource profile;
- observability/debuggability;
- packaging/deployment/upgrade story;
- long-term maintainability;
- fit with the repository/team.

Use current official/reliable evidence to confirm a new major framework is still healthy when practical.

## Default stack preferences

### Desktop

Single-platform desktop applications should prefer native languages and native frameworks.

Examples:

- macOS: Swift + current Apple-native UI/framework stack (SwiftUI/AppKit as appropriate);
- Windows: C#/.NET + current Windows-native UI stack;
- other platforms: prefer the platform's mature native stack when the target is truly platform-specific.

For cross-platform desktop requirements, prefer a **Rust-centered** architecture/toolchain. Select the mature Rust UI/application framework that best satisfies native integration, footprint, rendering/UI complexity, accessibility, and distribution. Do not default to Electron-style stacks simply because they are quick to demo.

### Web/backend service

Prefer **Go** for conventional HTTP/RPC services, daemons, gateways, infrastructure services, and network servers when no stronger ecosystem/domain constraint exists.

Use production conventions: explicit config, graceful shutdown, timeouts, health/readiness behavior where applicable, structured boundaries, tests, observability, and sane resource limits.

### AI / ML

Prefer **Python** with **uv** for environment/dependency/project management unless the project already has an authoritative different standard.

Require reproducible dependencies, clear model/runtime boundaries, testable preprocessing/postprocessing, and production-safe model/resource handling.

### Frontend

Prefer **TypeScript** and **pnpm**. Choose a current mainstream framework/build system suitable for the product rather than plain demo JavaScript or outdated scaffolding.

Use strict types where practical, current lint/format/test tooling, accessible components, and production build verification.

### Database

Prefer a mature **ORM/query framework** as the normal persistence layer for:

- model/schema mapping;
- migrations;
- transactions;
- parameterization;
- relationships;
- ordinary CRUD/query composition.

Use raw SQL selectively for database-native features, clarity, or measured performance needs. Keep it parameterized, tested, and integrated with transaction/migration conventions.

## Asking the user about stack choices

Do not ask about every library.

Ask only when:

- the project is greenfield or undergoing major re-platforming;
- multiple strong mainstream long-term stacks remain viable;
- the choice materially affects distribution, hiring/skills, runtime footprint, platform reach, or architecture;
- repository/user context does not resolve the tradeoff.

Provide one recommended default and a compact set of meaningful alternatives.

## Logging baseline

Every executable application/service should be diagnosable without attaching a debugger.

Default output:

1. **Console log** — human-readable, ANSI/color highlighting by level when supported.
2. **Text file log** — human-readable plain text with **no color/ANSI control codes**.

Recommended fields:

`timestamp | level | component/context | message | useful key=value context`

Requirements:

- startup/version/config summary without secrets;
- shutdown and major lifecycle events;
- actionable warning/error context;
- meaningful domain/operation transitions where useful;
- rotation/retention or an equivalent bounded strategy;
- configurable log level;
- no passwords, tokens, secrets, private keys, or unnecessary sensitive data;
- avoid high-volume spam in normal mode.

For environments that do not conventionally support text-file logs (for example browser-only frontend code), use platform-appropriate console plus existing telemetry/error reporting instead of forcing filesystem semantics.

## UI/UX baseline

When creating a new UI or materially revising one:

- follow current mainstream product design and the healthy existing design system;
- use contemporary typography, spacing, hierarchy, component states, and responsive/adaptive behavior;
- implement loading, empty, error, success, disabled, hover/focus/pressed states intentionally;
- meet accessibility fundamentals (semantic controls, keyboard navigation, focus visibility, contrast, readable scaling);
- use platform-native patterns in native desktop/mobile software;
- avoid legacy-looking default widgets/layouts when the product has no such established visual language;
- avoid decorative complexity that reduces clarity or performance.

A UI is not complete merely because it renders. Verify it at meaningful sizes/states and, when tools allow, inspect the actual runtime result.
