# Intent expansion for brief `$loop` requests

The user should be able to describe the desired outcome in natural language without writing an engineering specification.

## Core rule

Treat missing prompt detail as a repository-understanding problem before treating it as a user-question problem.

## Evidence ladder

Use the authority and inference hierarchy in [SKILL.md](../SKILL.md#2-authority-and-inference-hierarchy). Apply project lifecycle evidence when deciding which historical behaviors are real compatibility obligations.

## Minimum internal Intent Spec

For a short request, derive only:

- observable goal;
- relevant current behavior;
- expected changed behavior;
- affected surfaces;
- lifecycle stage and real compatibility constraints;
- acceptance evidence;
- material edge cases;
- assumptions that could matter.

Do not manufacture a heavyweight PRD for a small change.

## Scope control

Brief prompts are not permission for arbitrary redesign.

Expand details only enough to deliver the requested outcome well. Preserve unrelated product behavior, but do not mistake historical internal code for a compatibility contract. In pre-production projects, prefer one clean current design; in production projects, preserve or migrate real user/external/durable contracts.

## When to ask

Ask only when all are true:

- the decision cannot be resolved from available evidence;
- multiple materially different outcomes remain plausible;
- choosing incorrectly would be costly, irreversible, unsafe, externally incompatible, or clearly surprising to the user.

Otherwise choose a conservative default and continue.

## Assumption handling

Assumptions should be:

- explicit internally;
- evidence-backed where possible;
- reversible where possible;
- tested when they affect behavior;
- surfaced to the user only when material.

## Examples

### `$loop 增加用户导出功能`

Inspect existing data models, permission rules, list/filter semantics, download patterns, file formats already used by the product, and test conventions. If CSV is already the product standard, use it. Do not ask the user to specify delimiter, controller path, filename convention, or test framework unless the repository leaves those genuinely unresolved.

### `$loop 把这个页面做成响应式`

Inspect the referenced/current page, design system, breakpoints, neighboring responsive pages, supported browsers, and visual test/runtime tooling. Preserve desktop behavior, implement consistent breakpoints, verify meaningful narrow widths, and avoid redesigning unrelated visuals.

### `$loop 修复上传大文件失败的问题`

Reproduce first. Locate client/server/proxy limits, streaming/buffering behavior, timeout paths, memory constraints, error handling, and existing upload tests. Fix the actual limiting layer(s), add regression evidence, and preserve security/size constraints rather than simply removing all limits.

## Established project judgment

Consult relevant project doctrine, mind, taste, and accepted decisions before inferring routine behavior. Explicit current user instructions remain authoritative. When feedback suggests a consequential durable shift, distinguish a local exception from a project-wide change and optionally route the evidence to an available Ethos skill; do not silently rewrite the project's judgment from an inference.
