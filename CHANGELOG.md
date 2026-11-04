# 变更记录 / Changelog

## 2026-11-04 · 频道内容选品观察 / Channel content selection

- 新增中英文频道内容选品指南，说明频道与 Bot 的内容目标差异、常见读者价值和六类内容方向的供给与维护特点。
- 增加来源使用、摘要、商业披露和公开频道指标的读者指南；首页提供独立入口。
- 研究范围为有限公开页面观察，不推断频道商业表现或全平台偏好。

Added a bilingual channel content selection guide covering how channels differ from Bots, common reader-value models, and the supply and maintenance traits of six content categories. It includes guidance on source use, summaries, commercial disclosure, and public channel metrics, with a dedicated homepage entry. The guide reflects a limited sample of public pages and does not infer commercial performance or platform-wide preferences.

## 2026-11-04 · 中文 Markdown 强调校验 / Chinese Markdown emphasis checks

- 将旧中文报告、方法说明及本次频道观察报告中的标签改为纯文本，避免渲染器把 `**` 标记原样显示。
- 增加中文 Markdown 强调格式校验脚本、贡献规则和 GitHub Actions 检查，拒绝强调符内部空格及未配对标记。

Changed labels in existing Chinese reports, methodology, and the new channel report to plain text to avoid literal `**` rendering. Added a validator, contribution guidance, and a GitHub Actions check for internal whitespace and unpaired emphasis delimiters.

## 2026-11-03 · README 校验示例 / validation output

- Documented the verified success output for the offline snapshot validator in both README versions.
- 在中英文 README 中补充了离线快照校验器已验证的成功输出。

## 2026-11-03 · v0.2

- 扩展跨领域公开搜索，覆盖 19 个消费者领域和 68 个搜索词。
- 生成 492 条去重快照记录：169 个频道、323 个 bot。
- 增加优惠、求职等案例的公开证据和限制说明。
- 将中文和英文首页、报告、方法文档分别保存。
- 明确第一阶段是跨领域初筛，后续重点方向深挖需要单独验证。

This release broadens the public search to 19 consumer areas and 68 search phrases, with 492 deduplicated records. It adds evidence and limitations for deal and job examples, stores Chinese and English documents separately, and defines focused deep dives as a later validation stage.

## 2026-11-03 · v0.2.1

- Added a derived area-labelled catalog without changing the raw snapshot.
- Added offline validation for schema, public URLs, record counts, and credential-like fields.
- Documented the catalog and validation command in both language versions.

本次补充不改变原始快照，只增加领域标注目录和离线校验入口。

## 2026-11-03 · v0.3

- 将初筛报告改为面向外部读者的 19 个领域总览。
- 为每个领域增加样本量、公开信号、研究等级、推荐或不推荐原因，以及关键未知项。
- 将团队内部的产品选择和后续行动从公开报告中移除。

This revision turns the scan into a public-facing comparison of all 19 areas, with sample counts, visible signals, research priority, reasons to proceed or defer, and key unknowns. Internal product decisions and next actions are intentionally outside the repository report.

## 2026-11-03 · v0.3.1

- Added a bounded comparison of five candidate areas using common channel and bot metrics.
- Added counterexamples showing why members, views, freshness, and affiliate disclosures must be read together.
- Linked the comparison from both language versions of the README.

本次增加五个候选领域的统一口径比较，但不扩展为无限领域指南。

## 2026-11-03 · v0.3.2

- Added a supply-type audit for deals, jobs, scholarships, AI/software, and travel.
- Documented false positives and mixed business models such as course promotion, B2B supply, recruiting sales, and stale channels.
- Kept the comparison bounded to the existing snapshot instead of expanding the guide.

本次补充识别了搜索结果中的误命中和混合业务类型，仍然保持五个领域的研究边界。

## 2026-11-03 · v0.3.3

- 补充了五个领域的数据一致性检查，结论没有发生变化。
- 增加离线数据比较工具，避免把未抽查记录误判为消失。

Added a data-consistency check for five areas without changing the conclusions. Added an offline comparison helper that does not treat unsampled records as removed.

## 2026-11-03 · v0.3.4

- The data comparison helper is retained for local quality checks.

The data comparison helper is retained for local quality checks.

## 2026-11-03 · v0.4.0

- Added a dated jobs and travel validation report based on 10 task intents.
- Preserved 68 public examples, including 40 records outside the original broad snapshot.
- Added separate Chinese and English reports with explicit unknowns.

Added a dated jobs and travel validation report based on 10 task intents. It preserves 68 public examples, including 40 records outside the original broad snapshot, and documents what remains unverified.

## 2026-11-03 · v0.4.1

- 对求职与旅行方向的 9 个代表项目做公开资料核验，不启动 bot 或进行付费操作。
- 增加带日期的核验数据文件，并在中英文报告中记录规模、近期活跃度、任务闭环和变现线索之间的区别。

Validated public evidence for nine representative jobs and travel projects without starting bots or making paid actions. Added dated machine-readable evidence and documented the distinction between scale, recent activity, task completion, and monetization signals in both reports.

## 2026-11-04 · 首页与浏览入口 / Discovery and browsing

- 中英文首页前移三项研究发现与 19 个领域总览，增加收藏和贡献入口。
- 从现有 2026-11-03 标注目录生成中英文领域浏览页和 CSV 下载。
- 原始数据、采集日期、研究判断均未改变；本次没有重新检查项目当前状态。

Added findings and the 19-area overview to both homepages, plus bilingual browsing pages and a CSV export derived from the existing catalog. Raw data, collection dates, and research priorities are unchanged; current project status was not rechecked.

## 2026-11-04 · 使用指南入口 / Task-based entry points

- 将中英文首页的“三个发现”改为“如何使用这份图谱”，按找方向、查案例、比较方向和扩展调研提供入口。
- 增加调研记录的使用顺序，合并重复的快速入口。

Replaced the homepage findings with task-based guidance for selecting areas, browsing examples, comparing candidates, and extending research in both languages. Added a note-taking sequence and removed the duplicate quick-entry list.
