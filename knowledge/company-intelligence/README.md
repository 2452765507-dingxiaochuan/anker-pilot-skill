# Anker Company Intelligence Pack

> Version 5.1 · Verified through 2026-10-11

这是 Anker Pilot Skill 的公司事业 / 企业情报层。

它不是一篇“公司介绍”，而是一套可被 Claude 按需读取的业务知识库。

## 文件地图

- `00-executive-brief.md`：先读。当前公司总判断与最重要事实；
- `01-company-profile-and-evolution.md`：公司画像、资本、发展阶段；
- `02-business-model-and-financials.md`：2023–2026H1财务、分部、渠道、库存与现金流；
- `03-strategy-and-technology.md`：One Anker、Thus、MindBase、2023 Lab、能源、机器人；
- `04-brand-architecture-and-products.md`：五大产品类别与产品传播逻辑；
- `05-market-channel-supply-chain.md`：地区、Amazon、DTC、线下、履约；
- `06-communications-system.md`：Coachella、Tomorrowland、Anker Day、IFA与传播模型；
- `07-organization-culture-ai-native.md`：价值观、研发组织、AI Native；
- `08-risk-compliance-watchlist.md`：库存、贸易、召回、隐私、品牌迁移等；
- `09-hiring-and-role-signals.md`：品牌传播岗、Marketing、人才信号；
- `10-source-methodology.md`：来源分级、冲突处理、事实纪律。

## 结构化数据库

在 `../../data/`：
- `company-fact-ledger.csv`
- `source-register.csv`
- `financials.csv`
- `business-segments.csv`
- `regions-channels.csv`
- `technology-assets.csv`
- `campaigns.csv`
- `conflict-log.csv`

## Claude 加载原则

不要一次把所有模块塞入上下文。

1. 先读 `00-executive-brief.md`；
2. 读真题；
3. 根据真题选 1–3 个专项公司模块；
4. 需要数字时查 CSV；
5. 如果数字影响核心判断，检查 `source_id` 和 `conflict-log.csv`；
6. 高动态事实考试当天联网刷新。

## 核心原则

**知识库做厚，上下文保持薄。**
