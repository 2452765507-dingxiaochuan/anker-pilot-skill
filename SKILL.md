---
name: anker-pilot-brand-comms
version: 6.0
description: 安克创新 AI 飞行员试炼高性能作战系统。包含经核验的 Anker Company Intelligence、通用业务解题主干、传播专业层、8 类深度专项案例包、Claude 高性能工作方式、交付与真实验证。真题出现后按需加载，不一次塞满上下文。
---

# Anker Pilot V6 · 总控规则


## 考试启动后的人机交互
当本 Skill 被首次加载后，先完成以下动作，不要直接开始猜题：
1. 确认仓库根目录与 `website/prompts.html`（根目录副本为 `OPEN_PROMPT_CONTROL_ROOM.html`）存在；
2. 用一句话告诉用户：**“Anker Pilot 已加载，Prompt Control Room 已就绪。”**
3. 然后主动询问：**“是否现在打开 Prompt Control Room？”**
4. 只有用户回答“打开 / 是 / 好”等明确同意后，才尝试打开 `OPEN_PROMPT_CONTROL_ROOM.html`。在 macOS 可用 `open OPEN_PROMPT_CONTROL_ROOM.html`；Linux 桌面可尝试 `xdg-open OPEN_PROMPT_CONTROL_ROOM.html`；如果当前云桌面不允许直接弹出本地 HTML，则告诉用户准确文件路径，并提供可行的本地预览方式。
5. 打开面板不是解题前置条件；即使浏览器无法打开，仍继续按本 Skill 工作。

## 目标
在 3 小时考试中同时最大化：研究速度、问题判断、公司事实准确度、传播专业度、创意质量、视觉呈现、自然语言和最终完成度。Token 成本不是主要约束。

## 加载顺序
**0 公司情报 → 0A 高性能模式 → 1 通用主干 → 2 传播加固 → 3 专项+案例包 → 4 交付 → 5 验证**

### 0｜安克公司情报
先读：
- `knowledge/company-intelligence/00-executive-brief.md`
- `knowledge/company-intelligence/10-source-methodology.md`
- `prompts/00-anker-expert-mode.md`

再按真题加载 1–3 个专题模块。精确数字查 `data/`；口径冲突查 `data/conflict-log.csv`。

### 0A｜Claude 高性能作战
读取 `prompts/00A-performance-mode.md`。
原则：独立任务并行、定向研究、阶段快照、创意先发散后收敛、内容驱动视觉、自然语言编辑、完成前验证。
方法来源说明见 `references/external-skill-methods.md`。需要 HTML / Demo 时把“实际浏览器测试”作为完成门槛，环境有 Playwright/浏览器工具就实际操作；否则至少做语法、链接、占位符与人工打开检查。

### 1｜任意题型通用主干
读取 `prompts/01-general-core.md`。先把业务问题做对，再决定需要什么专业能力。

### 2｜传播专业层
涉及品牌/营销/内容/PR/社媒/用户沟通时读取 `prompts/02-communications-core.md`。

### 3｜专项深研包
每个专项都由“案例包 + 深度 Prompt”组成：
- 3A `scenarios/01-offline-experience.md`
- 3B `scenarios/02-overseas-gtm.md`
- 3C `scenarios/03-ai-content.md`
- 3D `scenarios/04-integrated-campaign.md`
- 3E `scenarios/05-pr-media.md`
- 3F `scenarios/06-social-growth.md`
- 3G `scenarios/07-crisis-trust.md`
- 3H `scenarios/08-tech-to-human.md`

对应外链研究包位于 `references/scenario-case-packs/`。优先迁移机制，不照抄案例形式。

### 4｜交付模块
题目要求什么才做什么：`prompts/03-delivery-modules.md`。HTML 不是默认答案。

### 5｜最终验证
读取 `prompts/04-final-review.md`。使用建设性的多视角压力测试，再做事实与文件实测。没有验证证据，不宣布“可以提交”。

## 并行策略
当有 2 个以上互不依赖的问题时，可并行：市场/竞品、用户证据、案例研究、数据分析、视觉参考等。每个并行任务必须有明确范围和统一输出：发现 / 证据 / 置信度 / So What / 未知。

## 事实纪律
信息分为：【题目事实】【安克资料】【外部事实】【工作假设】【派生计算】。题目事实优先；公司知识库来源等级 A1 > A2 > B1 > B2 > C > D。高动态信息临场刷新。

## 表达纪律
- 正常中文优先，英文术语只在提高精度时放【】中；
- 少用“不是……而是……”式反驳句；直接给思路、可能性、取舍和注意事项；
- 保留事实、限定条件与作者判断；
- 不机械追求固定轮数或自评高分。

## 视觉纪律
页面先定受众、任务、信息层级和明确审美方向；拒绝模板化科技 Dashboard。视觉服务业务内容，图表服务结论，交互服务阅读与决策。

## 评测与迭代
考试前可使用 `evals/test-cases.json` 跑代表性题目，按 `evals/README.md` 的维度检查 V6 是否真的提升结果。发现失败时优先修复对应模块，不为了“更完整”无限加长 Prompt。
