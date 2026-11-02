#!/usr/bin/env python3
"""Compare two public Telegram JSONL snapshots without network access."""

import argparse
import json
from pathlib import Path


COMPARE_FIELDS = ("members", "median_recent_views", "latest_post_date", "recent_posts")


def read_rows(path: Path):
    rows = {}
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        row = json.loads(line)
        identity = row.get("username") or row.get("id")
        if identity in {None, ""} and row.get("title"):
            identity = f"title:{row['title']}"
        key = (row.get("type"), identity)
        if key[0] not in {"channel", "bot"} or key[1] in {None, ""}:
            raise ValueError(f"{path}:{line_number}: missing stable public identity")
        if key in rows:
            raise ValueError(f"{path}:{line_number}: duplicate identity {key!r}")
        rows[key] = row
    return rows


def compare(before: Path, after: Path, after_is_subset: bool = False):
    old = read_rows(before)
    new = read_rows(after)
    added = sorted(set(new) - set(old))
    removed = [] if after_is_subset else sorted(set(old) - set(new))
    changed = []
    for key in sorted(set(old) & set(new)):
        fields = {}
        for field in COMPARE_FIELDS:
            if old[key].get(field) != new[key].get(field):
                fields[field] = {"before": old[key].get(field), "after": new[key].get(field)}
        if fields:
            changed.append({"type": key[0], "identity": key[1], "fields": fields})
    return {
        "before": str(before),
        "after": str(after),
        "before_count": len(old),
        "after_count": len(new),
        "after_is_subset": after_is_subset,
        "unmatched_before_count": len(set(old) - set(new)),
        "added": [{"type": kind, "identity": identity} for kind, identity in added],
        "removed": [{"type": kind, "identity": identity} for kind, identity in removed],
        "changed": changed,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("before", type=Path)
    parser.add_argument("after", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument(
        "--after-is-subset",
        action="store_true",
        help="Treat missing records as not sampled instead of removed",
    )
    args = parser.parse_args()
    result = compare(args.before, args.after, args.after_is_subset)
    payload = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(payload, encoding="utf-8")
        print(f"Wrote comparison to {args.output}")
    else:
        print(payload, end="")
    print(
        f"Compared {result['before_count']} -> {result['after_count']}: "
        f"{len(result['added'])} added, {len(result['removed'])} removed, "
        f"{len(result['changed'])} changed"
    )


if __name__ == "__main__":
    main()
