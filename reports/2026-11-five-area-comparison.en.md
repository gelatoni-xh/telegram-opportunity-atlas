# Focused Comparison of Five Consumer Areas

**Data date:** 2026-11-03  
**Purpose:** compare five candidates using the same evidence rules after the broad scan

Chinese version: [五个消费者领域比较](2026-11-five-area-comparison.zh.md)

## Summary

This is not a revenue ranking. It is a comparison of whether an area deserves more validation.

1. **Jobs and career discovery** has the largest public sample and the highest median channel membership, but member counts diverge sharply from views. Some results are clearly recruiting or sales channels. It merits more validation, but scale is not consumer-product proof.
2. **Travel and transport deals** has a smaller channel sample and many bots, with some promising recent-view signals. Check data sources, geography, and referral economics next.
3. **Scholarships and grants** includes channels with strong sampled views, but many examples are stale. Sustained demand is unproven.
4. **AI and software discovery** has steady supply but low median membership; many examples look like content or course promotion. Separate tool demand from content traffic.
5. **Deals and coupons** has the clearest affiliate disclosures, but the median channel views are low and public data does not show clicks or conversion.

## Common method

- Samples come from the same public search snapshot and are filtered by area label.
- Channel metrics use public member counts and the median views of sampled posts at collection time.
- “Recent” means the latest sampled post falls between 2026-11-01 and 2026-11-03. It shows new posting, not content quality or retention.
- Bots do not expose comparable public usage metrics, so bot counts are reported but are not treated as user scale.
- Search phrases overlap across areas. Samples are not mutually exclusive markets or market-size estimates.

## Comparison

| Area | Sample (channels / bots) | Median channel members | Median of channel-view medians | Recent channels | Research view | Main gap |
|---|---:|---:|---:|---:|---|---|
| Jobs and career discovery | 36 / 25 | 4,537.5 | 502.5 | 10 / 36 | Validate further | Information quality, job-seeker retention, employer-sales dependence |
| Travel and transport deals | 13 / 27 | 86 | 149 | 3 / 13 | Validate further | Data sources, geography, seasonality, referral conversion |
| Scholarships and grants | 10 / 11 | 292.5 | 114.5 | 1 / 10 | Conditional | Freshness, application outcomes, geography, application seasons |
| AI and software discovery | 22 / 16 | 20.5 | 79 | 3 / 22 | Conditional | Content versus tool demand, competition, referral transparency |
| Deals and coupons | 5 / 14 | 11 | 55.5 | 2 / 5 | Conditional | Clicks, conversion, audience quality, offer authenticity |

The median of medians reduces the effect of single outliers. It is not a typical-user metric and does not estimate revenue. The deals member median is especially affected by small channels and should not be compared with jobs as market size.

## Why counterexamples matter

- [@freelanceroff](https://t.me/Freelanceroff) has 32,836 members but a median of 2 sampled views; members alone do not establish active reach.
- [@Remote_Software_Developer_Jobs](https://t.me/Remote_Software_Developer_Jobs) has 26,843 members and 66,077 median sampled views, but its latest sampled post is dated 2024-12-24; high views still need a freshness check.
- [@scholarshipalertss](https://t.me/scholarshipalertss) has 2,899 members and 1,443 median sampled views, but its latest sampled post is dated 2026-06-13; one strong view signal does not establish sustained use.
- [@freekart_deals](https://t.me/freekart_deals) clearly discloses affiliate commissions, but 68,090 members correspond to 63 median sampled views; a visible monetization path does not prove that it works.

## What this comparison supports

It helps readers:

- avoid treating members, bot counts, or one high-view post as market size;
- separate public supply from a verifiable business path;
- check freshness, sources, and repeat use before estimating revenue;
- identify where stronger evidence is needed, such as job quality, travel-data reliability, and scholarship update cycles.

## Supply-type audit

Results for one search phrase do not necessarily represent one business model. This pass exposed several distinct supply types:

| Area | Visible path | Representative public examples | Interpretation |
|---|---|---|---|
| Deals | Affiliate links, deal aggregation, cashback bots | [@freekart_deals](https://t.me/freekart_deals), [@Roxk755_bot](https://t.me/Roxk755_bot) | The path is visible, but clicks and conversion are unknown; an affiliate disclosure is not proof of effectiveness. |
| Jobs | Job aggregation, recruiter contacts, ad inventory | [@lance_Jobs](https://t.me/lance_Jobs), [@stablegrambot](https://t.me/stablegrambot) | Supply is real and visible, but it may serve employers or sell ads rather than a paid job-seeker product. |
| Scholarships | Deadline alerts, application information, school registration | [@scholarshipalertss](https://t.me/scholarshipalertss), [@Kallamino_scholarship_bot](https://t.me/Kallamino_scholarship_bot) | The information task is clear, but update cycles and application outcomes need longer observation. |
| AI / software | Tool news, course waitlists, software discounts | [@Ai_Tools_bots](https://t.me/Ai_Tools_bots), [@learn_framer_for_designers](https://t.me/learn_framer_for_designers) | Search results mix tool discovery with course marketing; they should not be counted as one demand type. |
| Travel | Flight / hotel deals, itinerary organization, B2B supply | [@FlightDeals215axyn178](https://t.me/FlightDeals215axyn178), [@trip_itinerary_bot](https://t.me/trip_itinerary_bot), [@B2BHOTELDEAL](https://t.me/B2BHOTELDEAL) | Automation and transaction referrals both exist, but B2B, consumer, and stale supply must be separated. |

The next validation layer should therefore segment by user task and supply type rather than count search phrases alone.

It does not support revenue forecasts, success probabilities, Telegram-wide market-size estimates, or claims about active users, retention, clicks, payments, or application outcomes.

## Sources

- Raw snapshot: [snapshot-2026-11-03.jsonl](../data/snapshot-2026-11-03.jsonl)
- Area-labelled catalog: [catalog-2026-11-03.jsonl](../data/catalog-2026-11-03.jsonl)
- Search manifest: [search-manifest-2026-11-03.en.md](../methodology/search-manifest-2026-11-03.en.md)
- Fields and limits: [evidence-and-data.en.md](../methodology/evidence-and-data.en.md)
