# Evidence and Data Rules

## Evidence labels

- **Observed:** Directly present in a public channel or bot profile, public post, or public metric at collection time.
- **Inferred:** A plausible business implication drawn from observed material, not verified as the operator's actual economics.
- **Unknown:** Not visible from public data; do not fill it with a guess.

Every report claim about monetization should link to a public example and say whether it is observed or inferred. Subscriber counts and post views are snapshots, not proof of active users, conversion, or revenue. Bot public profiles rarely reveal active usage.

## Snapshot fields

| Field | Meaning |
|---|---|
| `captured_at` | Date the search results were collected (UTC date). |
| `type` | Public `channel` or `bot`. |
| `title`, `username`, `url` | Publicly visible identity and link. |
| `description` | Public profile text at collection time. |
| `members` | Public channel member count when returned; absent/null means unavailable. |
| `recent_posts` | Number of recent channel posts inspected. |
| `latest_post_date` | Date of the latest post returned. |
| `median_recent_views` | Median public views for inspected posts when available. |
| `matched_queries` | Search phrases that surfaced the result. |

The derived catalog adds `areas` to the raw fields. These labels come from the public search-phrase-to-area mapping for filtering; they are not a manual confirmation of what each project does. The raw snapshot remains the evidence source.

The snapshot omits numeric Telegram IDs. Do not add private-member data, user identifiers, personal messages, login artifacts, or credentials.

## Limits

Telegram public search is relevance-ranked and language-sensitive. Search result counts are not market sizes. Results can include stale, mislabeled, duplicate, or keyword-matched entities. View counts can vary by post age and channel format. The current snapshot is deduplicated by public URL, with area labels kept in the derived catalog. Evidence from one channel cannot establish category-level economics.
