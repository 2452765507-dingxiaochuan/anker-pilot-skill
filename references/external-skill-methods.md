# 外部 Skill 方法研究与采用说明

更新：2026-10-11

目标不是把考试环境塞满插件，而是把真正能提升 **研究质量、推理效率、设计呈现、语言质量、完成验证** 的方法内化到 Anker Pilot。这样即使现场无法安装第三方 Skill，核心能力仍然可用。

> 许可说明：本项目**不复制或再分发 Anthropic 官方 Skill 文件**。官方示例 Skill 使用其各自许可证，部分许可证对提取、复制与衍生作品有额外限制。因此这里只记录独立总结出的通用工作原则并链接原始来源。Superpowers 与 Humanizer-zh 为 MIT 项目；考试现场是否允许安装仍需以环境为准。

## 1｜Anthropic Skill Creator
来源：https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md

吸收进本项目的原则：
- 【渐进式加载】总控 Skill 保持轻；大量公司资料、案例和专项方法放 references / data / scenarios，真题出现后再加载。
- description 要明确“什么时候应该触发”，减少 Skill 明明有用却没有被调用的情况。
- Skill 不是写完就结束：需要用代表性测试题做 with-skill / baseline 对照，观察失败点，再迭代。
- 结构化资源：可重复执行的东西做 scripts；重资料放 references；主 SKILL.md 只保留导航、决策和约束。

项目落点：`SKILL.md`、`prompts/INDEX.md`、`scenarios/`、`references/`、`data/`、`scripts/build-control-room.py`。

## 2｜Anthropic Frontend Design
来源：https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md

吸收进本项目的原则：
- 先理解受众、主题、信息和预期感受，再确定视觉语言。
- 做明确、有理由的设计选择：版式、字体、色彩、密度、动效要来自具体 brief。
- 避免“一眼 AI 模板”：万能科技蓝、无意义渐变、平均分配的 KPI 卡、所有内容都卡片化、缺少主次。
- 视觉可以有风格，但不能牺牲信息读取、可访问性和交付稳定性。

项目落点：`prompts/03-delivery-modules.md` 的【Design Brief → Art Direction → Build → Design Review】流程。

## 3｜Anthropic Webapp Testing
来源：https://github.com/anthropics/skills/blob/main/skills/webapp-testing/SKILL.md

吸收进本项目的原则：
- 网页“写完”不代表“可提交”；完成前要实际打开和操作。
- 静态 HTML 先读结构和 selectors，再做针对性测试；不需要为了测试读取大量无关脚本污染上下文。
- 若环境有 Playwright / 浏览器工具：检查首屏、主要交互、导航、Tab、图表、移动端、浏览器 console。
- 没有浏览器自动化时至少做：HTML/JS 语法检查、占位符扫描、链接检查和人工浏览器打开。

项目落点：`prompts/03-delivery-modules.md`、`prompts/04-final-review.md`。

## 4｜obra / Superpowers
来源：https://github.com/obra/superpowers
许可证：MIT

重点吸收：
- `brainstorming`：先把意图、结果、成功标准和关键设计决策想清楚，再开始大量实施。
- `dispatching-parallel-agents`：只把**相互独立**的问题并行；每个代理 Brief 必须有范围、上下文、约束和明确回传格式。
- `writing-plans`：复杂执行拆成边界清楚、可检查、可完成的任务，不写成一篇长流水账。
- `verification-before-completion`：任何“完成/通过/可以提交”的声明之前，先执行能证明该结论的验证动作，读取结果后再下判断。

项目落点：`prompts/00A-performance-mode.md`、阶段快照、并行 Research Brief、最终验证门槛。

## 5｜Humanizer-zh
来源：https://github.com/op7418/Humanizer-zh
许可证：MIT

重点吸收：
- 编辑时优先保留事实、确定程度、专业语气和作者立场。
- 不把“去 AI 味”理解成机械删除排比、连接词或专业表达。
- 重点修复：空话、重复、模板式铺垫、堆形容词、伪总结、同义反复和过度工整。
- 语言自然化不能制造新事实，也不能弱化技术限定条件。
- 最终稿应该像一个真正做过判断的人在说话，而不是“为了显得完整”把每个观点都写成同样结构。

项目落点：所有最终文档/页面的 Language QC。

## 6｜考试现场推荐组合

### 默认：不依赖任何第三方安装
核心方法已经写进本项目。现场只要能读取本 Skill，就能使用：
- 高性能并行研究；
- 阶段快照；
- 专项案例迁移；
- 反模板前端设计；
- 自然语言 QC；
- 完成前实际验证。

### 环境允许时，可选安装

```bash
# Humanizer-zh（MIT）
npx skills add https://github.com/op7418/Humanizer-zh.git
# 或：git clone https://github.com/op7418/Humanizer-zh.git ~/.claude/skills/humanizer-zh

# Superpowers（MIT）
git clone --depth 1 https://github.com/obra/superpowers.git ~/.claude/superpowers
```

Anthropic 官方 Skills 建议使用官方 Claude Code 插件 / Skill 机制，不复制进本仓库。

## 7｜本次下载状态

本次生成环境对 `github.com/raw.githubusercontent.com` 的直接 Git / 下载请求出现 DNS 解析失败，因此**没有把第三方源码伪装成“已下载”打包进项目**。项目已经：
1. 通过公开 GitHub 页面核验 Skill 内容、用途和许可证；
2. 独立提取并重写可迁移的工作原则；
3. 把这些原则直接内化到 V6 Prompt；
4. 提供可选安装脚本，供考试环境网络正常时使用。

这样更稳：即便现场第三方安装失败，核心质量也不会下降。
