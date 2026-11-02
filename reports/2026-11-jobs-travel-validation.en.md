# Jobs and Travel Validation

**Data date:** 2026-11-03  
**Scope:** jobs and career discovery; travel and transport deals  
**Purpose:** record public supply, representative examples, and open questions for jobs and travel

## Result

The public sample covers 10 task intents and contains 68 deduplicated records: 34 channels and 34 bots. Forty records were not present in the original 492-record snapshot; 28 overlapped with it.

| Area | Queries | Results (channels / bots) | New records | Initial read |
|---|---:|---:|---:|---|
| Jobs and career discovery | 5 | 19 / 13 | 25 | Task queries expose niche job feeds and job-search tools, but mix recruiting supply, aggregation, and application management. |
| Travel and transport deals | 5 | 15 / 21 | 15 | Bot supply is prominent, especially flight alerts; data sources, geography, and alert quality need validation. |

## Visible signals

- Jobs produced niche feeds for developers, regions, and freelance writing, alongside CV and application-tracking bots.
- Travel additions were concentrated in flight-price alert bots, suggesting that automation is easier to discover through task queries than through broad travel-deal terms.
- A new record does not establish new user demand. It may be a duplicate operation, an inactive project, or a region-specific service.

## Representative validation

Without starting bots or making paid actions, nine representative projects were checked through public profiles and the latest ten channel posts where available. The result is that scale, recent activity, task completion, and monetization signals must be read together:

- `@internshiptojobs` has 48,465 members and a median of 4,804.5 views across the sampled posts. Posts link to external employer application pages, while the profile states promotion and ad-marketplace paths. This shows a visible publishing and advertising path, not successful applications or revenue.
- `@Remote_Software_Developer_Jobs` has 26,843 members and a sampled median of 43,139.5 views, but its latest sampled post is dated 2024-12-24. High views and current activity must be judged separately.
- `@writingwork` contains concrete freelance tasks and contact instructions, but task authenticity, payment outcomes, and dispute rates remain unknown.
- Public profiles for bots such as `@ApplyMyCVBot`, `@RoleTrackBot`, `@hotelbot`, and `@trip_itinerary_bot` describe task directions, but do not establish usage, data handling, retention, or paid conversion.
- `@besthoteldealz` has 4,763 members, but a sampled median of 256.5 views. The sample is mostly destination content and does not attribute bookings or affiliate revenue.

Details: [representative-validation-2026-11-03.json](../data/representative-validation-2026-11-03.json).

## Still unknown

- Bot usage, retention, alert accuracy, and paid conversion.
- Job authenticity, reposting rates, and outcomes for job seekers.
- Travel data sources, price validity, geographic availability, and referral economics.

## Data

- Public sample: [jobs-travel-public-sample-2026-11-03.jsonl](../data/jobs-travel-public-sample-2026-11-03.jsonl)
- Broad snapshot: [snapshot-2026-11-03.jsonl](../data/snapshot-2026-11-03.jsonl)
