# 安克公司数据库挂载方法 V5.1

## 推荐：项目内结构化库

V5.1 已内置机器可读数据库：

- `data/company-fact-ledger.csv`：关键事实账本；
- `data/source-register.csv`：来源；
- `data/conflict-log.csv`：冲突口径；
- `data/financials.csv`；
- `data/business-segments.csv`；
- `data/regions-channels.csv`；
- `data/technology-assets.csv`；
- `data/campaigns.csv`。

让 Claude 先读 `knowledge/company-intelligence/00-executive-brief.md`，需要精确数据再查 CSV。

推荐指令：

```text
先读取 knowledge/company-intelligence/00-executive-brief.md 和 10-source-methodology.md。
读完真题后，判断你真正需要哪些公司模块与 CSV，不要一次加载全部。

引用关键公司事实时，尽量保留 fact_id / source_id。
遇到冲突先查 data/conflict-log.csv。
题目给定事实优先于知识库。
```

---

## 如果你另有 Excel 产品数据库

例如：
`安克创新产品与信息数据库.xlsx`

先让 Claude 读取并回报：

1. 实际找到的 Sheet；
2. 每个 Sheet 字段；
3. 记录数；
4. 日期范围；
5. 与内置公司数据库是否存在冲突。

然后再按真题选择 Sheet。

推荐：

```text
请读取工作目录中的安克产品 / 信息 Excel。
先不要做方案。

请输出：
- 实际读取到的文件名；
- Sheet 列表；
- 每个 Sheet 的字段与记录数；
- 数据最后更新时间；
- 与 data/company-fact-ledger.csv 中同名事实是否存在冲突。

后续事实分四层：
【题目事实】【安克资料】【外部事实】【工作假设】。

如果 Excel 与公司最新法定披露冲突：
财务、员工、上市等硬事实优先采用法定披露；
产品参数按更新日期和官方产品页判断；
无法确定时明确标记“待核验”。
```

---

## 网络受限时

优先保留：
- `00-executive-brief.md`
- `data/company-fact-ledger.csv`
- `data/conflict-log.csv`
- 与题目有关的一个专项模块。

这四类文件比一次性复制整份长报告更有效。

---

## 临场联网刷新

以下事实如果决定方案，建议重新搜：

- 2026Q3 及以后财务；
- 最新产品与价格；
- 目标市场政策 / 关税；
- 最新 Campaign；
- 最新门店；
- 社媒数据；
- 召回 / 合规；
- 机器人 / MindBase 等研发进度。

新查到的信息标记为【外部事实】，记录来源和时间。
