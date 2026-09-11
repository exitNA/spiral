# Spiral Project Mind

This is the current best synthesis of Spiral and its independent Loop and Ethos plugins. Revise it when evidence changes; do not use it as a chronological learning log.

## Purpose

Ethos maintains continuity of project judgment across conversations and implementation work. It automatically distills durable intent, mental models, taste, decisions, collaboration norms, and proven practices into repository authorities.

## Mental Model

Spiral distributes two independent plugins:

1. **Delivery through `$loop`:** general-purpose task orchestration from requirements to verified outcomes. Requirements may be brief or incomplete; clarify and expand them from available context, establish a coarse whole, execute, verify against task-appropriate evidence, repair, and deliver. A repository is optional; engineering rules apply only to relevant software work.
2. **Evolution through `$ethos`:** observe possible learning, decide whether it is durable, locate the narrowest authority, reconcile evidence, integrate the current judgment, and prune stale guidance.

Loop delivers independently and may use an available Ethos skill to integrate project judgment. Missing Ethos does not block delivery or create unfinished work. Ethos automatically evaluates qualifying evidence in ordinary conversations as well as Loop runs; explicit `$ethos` invocation is also supported. Ethos owns canonicalization and requires no Loop installation.

Detection and canonicalization remain separate. Implicit Skill selection recognizes qualifying signals; `$ethos` integrates evidence within the normal task. Project learning must not inject recurring reminders or synthetic user messages into the main conversation, or force a continuation after completion. Keep screening internal; surface only material knowledge changes concisely. Skill selection does not guarantee observation on every turn.

Project knowledge is an authority system rather than a note collection. `.ethos/SOUL.md` holds current judgment, `.ethos/CONTEXT.md` holds domain meaning, and `.ethos/decisions/` preserves consequential rationale; `AGENTS.md` carries compact operational guidance, and code or tooling enforces machine-checkable facts. Skills describe reusable methods; they are not the default memory store.

## Principles

- **独立插件、可选协作：** Loop 负责交付；Ethos 可用时自动演进项目判断，并指出对当前交付的影响。Loop 将实现落差映射到原任务的需求、修复和验收。知识已整合与产品已满足要求是两个独立结论，协作不增加强制依赖或学习专用续跑。
- **先验证整体方向，再细化：** 深入局部优化前，验证架构、主流程和产品方向。易用性改进先核对真实用户流程与操作价值，再优化视觉；交互正确性和界面质量分别取证。编译、测试数量或知识更新不能代替用户要求的最终成果证据。
- **需求不是意图，以原始交付范围验收：** 用户提出的 request 是需求，是范围与验收的原始权威；意图只能是基于证据的解释，不能替代或缩小需求。客观证据和独立审查必须对应用户要求的完整成果；粗粒度整体只是中间里程碑。迁移默认保留范围内的用户能力，原验收义务不能因更换实现或删改文档而消失。仍可执行的必需工作应继续完成；取消、明确预算和真实外部阻塞则按实际状态交接，不缩小目标后宣称完成。
- **Coherence over capture:** improve the existing model instead of appending detached observations.
- **每个用户任务独立记录：** Loop 为每个独立目标建立带稳定 ID 的任务文档，小任务也不例外；ID 按本地创建时间戳与简短语义命名，便于按时间浏览和识别。模板中的 `Task ID`、`Created`、`Updated` 是纯字段名，格式说明不属于字段名；`Created` 固定，`Updated` 随任务记录的有效更新使用本地时间刷新。同一目标的补充、纠正和恢复沿用该文档，新目标另建并关联。任务状态不与项目长期判断混写，也不靠会话上下文代替持久记录。
- **目标稳定、执行清单动态：** 原始要求、Agent 解释和授权变更分开保存。任务清单可随证据拆分、替换、取消和重开，但必须保留需求覆盖与调整原因；工作做完不等于需求验收通过。LOOP.md 严格使用统一模板，不以等价任务文档代替；任务清单使用列表，标题与正文按用户语言编写。LOOP.md 独占整体状态与下一步，STATE.md 仅保存技术恢复现场。任务清单须通过 Codex 原生计划工具展示；对话复选框、文档面板或自制界面不能替代。缺少原生工具时明确报告同步受阻。原生视图从主文档同步，不形成第二份状态权威。
- **Automatic detection, conservative writing:** recognize qualifying signals during ordinary work, but canonize only explicit or well-supported learning.
- **Evidence before preference:** infer conditional preferences from independent choices and their rationale, preserving constraints and counterexamples. Repetition alone does not establish taste or intent. Keep useful uncertain evidence in a bounded, ignored local candidate store; promote established meaning into its authority and remove the candidate.
- **One meaning, one authority:** route each insight to the narrowest source of truth and remove superseded guidance.
- **Current synthesis over history:** keep active doctrine focused on present judgment; preserve history only when its rationale remains useful.
- **项目心智按决策范围组织：** 仓库根目录 `.ethos/` 保存统一心智，`SOUL.md` 保留跨任务需要的核心理解与阅读入口；领域语义、重要决策理由和特定主题分别归属对应权威。按实际任务的读取需要拆分，每个入口说明何时读取；不按文件长度机械拆分，也不为每条观察建文件。完整规则只维护一处，核心摘要不形成第二份规则集。

## Taste

Express the user's intended meaning in natural, concise language. Preserve wording verbatim only when explicitly requested. Product descriptions should communicate the value without restating platform context already clear from the product.

Distilled project knowledge uses the user's preferred language, with English as the fallback only when no preference is set. Localize headings and prose while preserving canonical filenames, paths, identifiers, and exact quotations. English templates do not determine the output language.

Good output is end-to-end, evidence-backed, integrated, specific, and decision-relevant. Delivery should establish the whole shape early and refine by risk and impact. Learning should make a future choice easier without forcing the reader to reconstruct context from scattered notes.

The system should prefer one clean implementation and one sharpened knowledge model over compatibility layers, duplicated procedures, or comprehensive capture without demonstrated value. Automatic behavior should remain legible, bounded, and reversible.

## Engineering Practice

- Publish Loop and Ethos as separate plugins in the Spiral marketplace, with `loop/` and `ethos/` as their respective plugin roots; do not add an extra package-wrapper directory around either plugin.
- Keep `$loop` explicit-only. Ethos automatically evaluates and integrates high-confidence learning within active permissions; uncertain or conflicting conclusions require clarification. Explicit invocation remains available.
- Keep project-judgment rules, templates, and authority routing under Ethos; keep execution orchestration and process telemetry under Loop.
- Keep the source in an independent GitHub repository that is installable as a Codex marketplace. GitHub is the formal distribution channel; local-path installation is for development and release verification only.
- Protect the repository in layers: ignore local secrets and generated noise, validate distributable structure and dangerous filenames, and scan full Git history for leaked credentials in CI.
- Keep release versions stable and use cachebusters only for local iteration.
- Replace assets and their supporting documents at stable canonical paths. Git owns version history; avoid filename version suffixes such as `-v2`.
- 技能优化以行为保真为准：入口保留主流程、关键约束和明确的按需读取指针；重复规则合并到唯一权威。用代表性任务验证精简后的行为，不以固定行数或格式校验代替质量判断。

## Open Tensions

- Behavioral scenarios distinguish useful canonicalization from over-eager documentation changes and cover Loop-to-Ethos handoff. Semantic quality and absence of context pollution require separate evidence; neither substitutes for the other. Cross-machine evidence recall remains outside the local candidate store's scope.
- Local process telemetry can improve scheduling, but must remain optional supporting evidence rather than canonical project state.
- Submission to the OpenAI curated plugin repository should follow successful independent use and release hardening.
