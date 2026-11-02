# Telegram 机会图谱

[![中文](https://img.shields.io/badge/阅读中文-README.md-1677ff?style=flat-square)](README.md) [![English](https://img.shields.io/badge/Read%20English-README.en.md-555?style=flat-square)](README.en.md) [![数据日期](https://img.shields.io/badge/数据日期-2026--11--03-0a7?style=flat-square)](reports/2026-11-consumer-opportunity-scan.zh.md) [![License](https://img.shields.io/badge/代码-MIT-555?style=flat-square)](LICENSE)

这个仓库用公开 Telegram 频道和 bot 的案例，整理消费者任务、现有供给和可观察的商业信号，帮助独立开发者和研究者判断哪些领域值得继续验证。

它不试图列出 Telegram 上所有项目，也不把订阅数当作市场规模或收入。

许可：[LICENSE](LICENSE)。代码使用 MIT；报告、方法文档和数据使用 CC BY 4.0。

## 快速入口

如果你是第一次来，按这个顺序读：

1. [消费者机会初筛报告](reports/2026-11-consumer-opportunity-scan.zh.md)：查看 19 个领域的统一判断，包括推荐、暂缓和不推荐的原因。
2. [五个领域比较](reports/2026-11-five-area-comparison.zh.md)：查看五个候选领域的统一指标和反例。
3. [求职与旅行方向核验](reports/2026-11-jobs-travel-validation.zh.md)：查看定向搜索发现的公开供给，以及仍未验证的关键问题。
4. [覆盖矩阵](methodology/coverage-matrix.zh.md)：查看调查范围和搜索词。
5. [证据与数据说明](methodology/evidence-and-data.zh.md)：了解快照字段、证据标准和数据限制。

## 报告提供什么

- 优惠频道公开披露了联盟营销，但现有样本没有点击、转化或收入数据。
- 求职频道有可见互动，不过明确案例偏向招聘和企业合作，不能直接当作消费者产品模式。
- 每个领域都记录了公开样本、可见信号、当前研究等级和主要未知项。
- “暂不推荐”表示本轮不适合作为优先研究对象，不表示该领域没有市场。

详细判断和案例数据见[调研报告](reports/2026-11-consumer-opportunity-scan.zh.md)。本仓库不包含任何特定团队的产品路线或内部机会决策。

## 这批数据的范围

2026-11-03 的快照有 492 条记录，来自 68 个搜索词，覆盖 19 个消费者领域：169 个频道、323 个 bot。其中 491 条有公开 Telegram 链接，另 1 条结果没有公开用户名或链接。这是按关键词发现的样本，不代表 Telegram 的整体分布。

## 重新执行搜索

搜索脚本基于 Telegram 官方 API/TDLib 接口。运行前需要安装 TDLib，并准备 [Telegram API 应用](https://my.telegram.org/apps)：

```sh
python3 scripts/search_public.py "food deals" "local events" --output data/new-scan.jsonl
```

首次运行时，脚本会在本地终端提示输入 API 凭据和 Telegram 登录信息；API hash 使用隐藏输入。登录会话保存在仓库之外的本地目录。不要把凭据或登录码写入仓库或聊天记录。搜索结果是公开供给样本，不代表用户规模、留存或收入。更多字段说明见[证据与数据说明](methodology/evidence-and-data.zh.md)。

## 文件导航

- `reports/`：按日期保存的调研报告，中英文各一份。
- `methodology/`：覆盖范围、证据标准和数据字段说明，中英文各一份。
- `data/`：去重后的公开搜索快照；简介等原始内容保留采集时的语言。
- `data/catalog-2026-11-03.jsonl`：由原始快照派生的领域标注目录；`areas` 只根据 `matched_queries` 映射，不改变原始证据。
- `data/representative-validation-2026-11-03.json`：对少量代表项目的公开资料核验，包含日期、观察字段和明确未知项。
- `scripts/`：用于重复公开搜索、生成目录和校验数据的脚本。
- `CHANGELOG.md`、`CONTRIBUTING.md`：版本变化和提交证据的规则。

中英文版本分开保存。更新结论、数字、范围或方法时，请同步修改对应的两份文档。Telegram 名称、链接和搜索词保留原文，方便读者自行核对。

本地校验：

```sh
python3 scripts/validate_snapshot.py data/snapshot-2026-11-03.jsonl \
  --derived data/catalog-2026-11-03.jsonl
```
