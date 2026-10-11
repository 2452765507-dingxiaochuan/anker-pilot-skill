# Anker Pilot V6 · 深度专项 + 高性能 Claude 版

V6 在 V5.1 的真实公司情报层上，重点补强两件事：

1. **3A–3H 专项不再只是三条简短 Prompt**：每类变成案例研究、专业推导、执行系统、成功标准和注意事项完整包。
2. **把高质量 Claude 工作方法内化进主 Skill**：并行研究、渐进式加载、内容驱动视觉、自然语言编辑、提交前真实验证。

## 考试建议路径

1. `SKILL.md`
2. 安克公司执行简报 + 真题相关公司模块
3. `prompts/00A-performance-mode.md`
4. `prompts/01-general-core.md`
5. 传播题再用 `02-communications-core.md`
6. 选 1 个主专项（必要时叠加 1 个辅助专项）
7. 需要什么交付再调用 `03-delivery-modules.md`
8. 最后 `04-final-review.md`

## 3A–3H
- 3A 线下体验空间：6 个标杆案例 + 5 个深度阶段
- 3B 海外 GTM：5 个上市案例机制 + 5 个深度阶段
- 3C AI 内容：4 个内容供应链案例 + 5 个深度阶段
- 3D 整合营销：Spotify / Anker / Duolingo / Samsung
- 3E PR 媒体：Anker / Apple / Dyson / Samsung
- 3F 社媒增长：Duolingo / Samsung / Spotify
- 3G 危机信任：Samsung Note7 全链路
- 3H 科技传播：Dyson / Samsung / Anker 的可视化证明机制

## 外部 Skill 方法
见 `references/external-skill-methods.md`。

- Anthropic Skill Creator：采用渐进式加载与测试迭代思想；不复制官方文件。
- Anthropic Frontend Design：采用内容驱动、反模板视觉原则；不复制官方文件。
- Anthropic Webapp Testing：采用“写完后实际打开、操作、看浏览器错误”的验证思想；不复制官方文件。
- obra/Superpowers（MIT）：采用并行任务、构思→执行、验证后完成等方法。
- Humanizer-zh（MIT）：采用保留事实与作者判断的自然语言编辑方法。

由于当前生成环境无法解析 github.com，本 ZIP **未打包第三方源码**。核心方法已独立内化，本项目不依赖它们才能运行。若考场允许，可运行 `scripts/install-optional-skills.sh` 尝试安装 MIT 第三方 Skill。

## 历史版本
保留 `archive-v4/` 和 V5.1 原公司层归档。

## 数据更新
公司情报核验截止 2026-10-11。考试当天对价格、产品、campaign、门店、社媒、财务新公告等高动态信息按需刷新。

## Skill 自测
`evals/test-cases.json` 内置 6 个代表性考试题和明确验收项，可用于考试前做 with-skill / baseline 对照，避免 Prompt 只变长却没有提高结果。

---

## 公共电脑考试部署（Public GitHub）

为了让未登录你个人 GitHub 的考试环境也能直接访问，考试用仓库请设为 **Public**。

推荐启动：

```bash
git clone https://github.com/<YOUR_GITHUB_USERNAME>/<YOUR_REPO>.git
cd <YOUR_REPO>
```

然后告诉 Claude：

```text
请完整读取 SKILL.md 并启用 Anker Pilot。加载完成后确认 OPEN_PROMPT_CONTROL_ROOM.html 存在，并询问我是否需要现在打开 Prompt Control Room；未经我确认不要自动弹出。
```

根目录的 `OPEN_PROMPT_CONTROL_ROOM.html` 与 `website/prompts.html` 内容一致，前者专门用于考试现场快速打开。
