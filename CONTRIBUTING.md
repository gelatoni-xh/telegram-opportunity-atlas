# 如何贡献 / Contributing

这个仓库优先接受可复查的公开证据和方法改进。新增一个频道或 bot 列表，不如补充一个能够改变判断的证据。

This repository prioritizes inspectable public evidence and improvements to the method. A new list of channels or bots is less useful than evidence that could change a decision.

## 提交新证据 / Add evidence

请同时提供：

- 公开 Telegram 链接和检查日期
- 搜索词、语言和地区（如果相关）
- 观察到的事实与自己的推断，分开写
- 成员数、帖子浏览量等指标的抽样范围
- 仍然未知的关键数据，以及这条证据会改变什么判断

Include the public Telegram link and check date, query/language/region when relevant, observed facts separately from inferences, the sampling window for metrics, and the key unknown that the evidence could change.

## 数据要求 / Data requirements

只提交公开频道和 bot 信息。不要提交数字 Telegram ID、成员名单、私人消息、登录凭据、验证码或本地会话文件。公开指标必须标注采集时间，不能把浏览量直接当作收入。

Submit public channel and bot information only. Do not submit numeric Telegram IDs, member lists, private messages, credentials, login codes, or local session files. Timestamp public metrics and never treat views as revenue.

## 文档同步 / Document sync

中文和英文文档分开保存。修改结论、数字、范围或方法时，请同步更新对应的中英文文件，并在 `CHANGELOG.md` 记录影响范围。

Chinese and English documents are stored separately. Update both language versions when changing conclusions, figures, scope, or methods, and record the impact in `CHANGELOG.md`.

## Markdown 格式 / Markdown formatting

中文 Markdown 的强调标记内不要在 `**` 后或闭合 `**` 前留空格；这会导致部分渲染器把标记原样显示。元数据标签（如“观察日期：内容”）直接使用纯文本，不加粗标签。编辑后运行 `python3 scripts/validate_markdown.py`。

Do not put whitespace immediately inside `**` delimiters in Chinese Markdown; some renderers display the markers literally. Keep metadata labels such as `Observation date:` as plain text. Run `python3 scripts/validate_markdown.py` after editing.
