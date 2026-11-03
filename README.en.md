# Telegram Opportunity Atlas: 19 Product Areas for Independent Developers

[![中文](https://img.shields.io/badge/阅读中文-README.md-1677ff?style=flat-square)](README.md) [![English](https://img.shields.io/badge/Read%20English-README.en.md-555?style=flat-square)](README.en.md) [![Data date](https://img.shields.io/badge/data%20date-2026--11--03-0a7?style=flat-square)](reports/2026-11-consumer-opportunity-scan.en.md) [![License](https://img.shields.io/badge/code-MIT-555?style=flat-square)](LICENSE)

Compare existing supply, observable business signals, and open questions across **19 consumer areas**, using **492 public channel and bot records from 68 search phrases**. A starting point for product discovery and competitor research.

**[Browse public samples](catalog/README.en.md) · [Download CSV](data/catalog-2026-11-03.csv) · [Compare five areas](reports/2026-11-five-area-comparison.en.md)**

## How to use this atlas

| What you want to do | Where to start |
|---|---|
| Find a product area to research | Browse the **19-area overview below**. Compare user tasks, existing supply, and open questions, then select areas that fit your experience and resources. |
| Find existing channels and bots in an area | Open the [catalog by area](catalog/README.en.md) for names, public links, and matched search phrases. [Download the CSV](data/catalog-2026-11-03.csv) to apply your own filters. |
| Compare candidate areas in depth | Read the [five-area comparison](reports/2026-11-five-area-comparison.en.md), then the [jobs and travel validation](reports/2026-11-jobs-travel-validation.en.md), for cases, comparison criteria, and questions that still need checking. |
| Extend your own research | Refer to the [coverage matrix and search phrases](methodology/coverage-matrix.en.md) and [evidence and field guide](methodology/evidence-and-data.en.md), then run a search using the command below. |

For each area you select, organize your notes around: the user's task → existing supply → public evidence → questions to validate next.

## All 19 areas at a glance

These are research priorities. **Validate first does not mean proven profitable.** Samples were discovered by keywords and do not measure market size. A record may belong to multiple areas; parentheses show channels / bots.

| Area | Sample (channels / bots) | Current view | Core conclusion |
|---|---:|---|---|
| Deals and coupons | 19 (5 / 14) | <strong>Validate first</strong> | Affiliate disclosure and purchase intent are visible; clicks, conversion, and revenue are unknown. |
| Jobs and career discovery | 61 (36 / 25) | <strong>Validate first</strong> | Recurring task with relatively strong audience signals; verify whether users can be served without employer sales. |
| Scholarships and grants | 21 (10 / 11) | <strong>Validate first</strong> | Clear fit for alerts and filtering; accuracy, geographic coverage, and payment paths are unverified. |
| AI and software discovery | 38 (22 / 16) | <strong>Validate first</strong> | Purchase intent may be strong; verify recommendation transparency, update cost, and competition. |
| Travel and transport deals | 40 (13 / 27) | <strong>Validate first</strong> | Transaction value may be high; verify sources, geographic coverage, and referral economics. |
| Language learning and exams | 48 (4 / 44) | <strong>Keep watching</strong> | Bot supply is large; actual use, outcomes, and willingness to pay are unknown. |
| Expat life, relocation, and visas | 17 (10 / 7) | <strong>Keep watching</strong> | Concrete need, but geographic differences and information maintenance are costly. |
| Cashback and price alerts | 27 (7 / 20) | <strong>Keep watching</strong> | Automatable task; needs reliable price sources, notifications, and conversion evidence. |
| Food, grocery, and restaurant deals | 34 (24 / 10) | <strong>Keep watching</strong> | Frequent purchases, but local supply limits portability. |
| Local events and city discovery | 14 (6 / 8) | <strong>Keep watching</strong> | Local demand may be real; source coverage and update cost are unclear. |
| Personal budgeting and expense tools | 30 (0 / 30) | <strong>Keep watching</strong> | Bot format fits; trust, privacy, and retention evidence are insufficient. |
| Productivity and personal organization | 20 (0 / 20) | <strong>Keep watching</strong> | Easy to prototype, but crowded and long-term use is unknown. |
| Creator tools and publishing | 18 (6 / 12) | <strong>Keep watching</strong> | Clear task, but many visible models sell services to creators rather than serve consumers. |
| Gaming | 18 (10 / 8) | <strong>Keep watching</strong> | Audience may be large; platform, copyright, and regional dependence are high. |
| Books, media, and entertainment discovery | 18 (10 / 8) | <strong>Keep watching</strong> | Channel format fits; copyright, production, and willingness to pay need checking. |
| Family, parenting, and meal planning | 11 (4 / 7) | <strong>Do not prioritize</strong> | Small sample and high responsibility; repeat use and monetization evidence are weak. |
| Fitness and habit support | 39 (0 / 39) | <strong>Do not prioritize</strong> | Health responsibility is high; outcomes, activity, and safety boundaries are unknown. |
| Personal safety and emergency help | 3 (0 / 3) | <strong>Do not prioritize</strong> | Tiny sample and very low tolerance for failure; reliability evidence is insufficient. |
| Crypto and trading information | 18 (2 / 16) | <strong>Do not prioritize</strong> | Financial and regulatory risks are high; public metrics cannot prove signal quality. |

[Read the full research and evidence limitations](reports/2026-11-consumer-opportunity-scan.en.md). The browsing catalog maps search phrases to areas and may include false positives and stale projects. Inclusion is not endorsement.

If the atlas helps your research, **Star it for easy reference**. See the [changelog](CHANGELOG.md) for changes and the [contribution guide](CONTRIBUTING.md) to add inspectable public evidence.

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

Expected output for this snapshot:

```text
OK: 492 records (169 channels, 323 bots)
```

## License

Code is MIT; reports, methodology, and data are CC BY 4.0. See [LICENSE](LICENSE).
