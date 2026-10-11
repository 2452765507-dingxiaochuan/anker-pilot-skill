# data/｜结构化公司数据库

V5.1 将公司情报拆成可筛选的数据文件，避免 Claude 从长文章里凭印象取数。

## 文件
- `company-fact-ledger.csv`：核心事实，带来源与限定；
- `source-register.csv`：来源 URL 与等级；
- `conflict-log.csv`：官方口径冲突；
- `financials.csv`：2023–2026H1主要财务；
- `business-segments.csv`：三大财务分部；
- `regions-channels.csv`：地区 / Amazon / DTC / 线下；
- `technology-assets.csv`：Thus / MindBase / 2023 Lab / JML等；
- `campaigns.csv`：重要传播案例；
- `people-rd.csv`：员工与研发人员结构；
- `company-timeline.csv`：战略、上市、品牌节点；
- `risk-watchlist.csv`：业务风险与监测；
- `role-signals.csv`：品牌传播 / Marketing 官方岗位信号；
- `anker-database.md`：人工速查版。

## 读取规则
1. 先看题目；
2. 只筛相关 domain / tags；
3. 保留 source_id；
4. 自己计算的指标标【派生计算】；
5. 冲突先看 `conflict-log.csv`。
