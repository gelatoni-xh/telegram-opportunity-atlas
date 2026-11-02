# Telegram Opportunity Atlas

[![中文](https://img.shields.io/badge/阅读中文-README.md-1677ff?style=flat-square)](README.md) [![English](https://img.shields.io/badge/Read%20English-README.en.md-555?style=flat-square)](README.en.md) [![Data date](https://img.shields.io/badge/data%20date-2026--11--03-0a7?style=flat-square)](reports/2026-11-consumer-opportunity-scan.en.md) [![License](https://img.shields.io/badge/code-MIT-555?style=flat-square)](LICENSE)

This repository uses public Telegram channel and bot examples to organize consumer tasks, existing supply, and observable business signals. It helps independent developers and researchers decide which areas deserve further validation.

It is not a complete directory of Telegram projects, and it does not treat subscriber counts as market size or revenue.

License: [LICENSE](LICENSE). Code is MIT; reports, methodology documents, and data are CC BY 4.0.

## Quick entry points

If this is your first visit, read these in order:

1. [Consumer opportunity scan](reports/2026-11-consumer-opportunity-scan.en.md): see the consistent judgment for all 19 areas, including why some are prioritized, deferred, or not recommended.
2. [Five-area comparison](reports/2026-11-five-area-comparison.en.md): compare five candidates using common metrics and counterexamples.
3. [Jobs and travel validation](reports/2026-11-jobs-travel-validation.en.md): see the public supply found and the key questions that remain unverified.
4. [Coverage matrix](methodology/coverage-matrix.en.md): see the search scope and phrases.
5. [Evidence and data guide](methodology/evidence-and-data.en.md): understand the snapshot fields, evidence standards, and limitations.

## What the report provides

- Deal channels publicly disclose affiliate marketing, but the sample does not reveal clicks, conversions, or earnings.
- Job channels show visible engagement, but the clearest example focuses on recruiting and employer relationships. It is not direct evidence for a consumer product model.
- Every area has a public sample count, visible signal, current research priority, and key unknowns.
- “Do not prioritize” means it is not an early research target in this pass, not that the area has no market.

See the [research report](reports/2026-11-consumer-opportunity-scan.en.md) for the full reasoning and examples. This repository does not contain a specific team’s product roadmap or internal opportunity decision.

## Snapshot scope

The snapshot dated 2026-11-03 contains 492 records from 68 search phrases across 19 consumer areas: 169 channels and 323 bots. Of these, 491 have public Telegram links; one result has no public username or link. This is a keyword-driven discovery sample, not a representative picture of Telegram.

## Re-run the search

The search helper uses Telegram's official API/TDLib interfaces. Install TDLib and create a [Telegram API application](https://my.telegram.org/apps) before running it:

```sh
python3 scripts/search_public.py "food deals" "local events" --output data/new-scan.jsonl
```

On first use, the script prompts for API credentials and Telegram login details in the local terminal. The API hash is entered through a hidden prompt. The login session is stored in a local directory outside the repository. Do not put credentials or login codes in the repository or chat history. Search results are a sample of visible supply, not evidence of users, retention, or revenue. See the [evidence and data guide](methodology/evidence-and-data.en.md) for field definitions.

## Repository map

- `reports/`: dated research reports, with separate Chinese and English versions.
- `methodology/`: coverage, evidence standards, and data-field documentation in both languages.
- `data/`: deduplicated public search snapshots; original profile text stays in its collected language.
- `data/catalog-2026-11-03.jsonl`: a derived area-labelled catalog. `areas` are mapped only from `matched_queries`; the raw evidence is unchanged.
- `data/representative-validation-2026-11-03.json`: dated public checks of a small representative set, with observed fields and explicit unknowns.
- `scripts/`: helpers for repeat public searches, catalog generation, and offline validation.
- `CHANGELOG.md`, `CONTRIBUTING.md`: release history and evidence contribution rules.

Chinese and English documents are stored separately. Update both versions when changing conclusions, figures, scope, or methods. Telegram names, links, and search queries stay in their original form so readers can check them directly.

Local validation:

```sh
python3 scripts/validate_snapshot.py data/snapshot-2026-11-03.jsonl \
  --derived data/catalog-2026-11-03.jsonl
```
