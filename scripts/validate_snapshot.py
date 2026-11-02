#!/usr/bin/env python3
"""Validate the public snapshot and its derived catalog without network access."""

import argparse
import json
import re
from collections import Counter
from pathlib import Path
from typing import Optional, Tuple
from urllib.parse import urlparse


REQUIRED = {"type", "title", "username", "url", "matched_queries", "captured_at"}
FORBIDDEN = re.compile(r"(api[_ -]?hash|api[_ -]?id|phone|验证码|login code|password|secret)", re.I)


def read_jsonl(path: Path):
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            yield line_number, json.loads(line)
        except json.JSONDecodeError as exc:
            raise ValueError(f"{path}:{line_number}: invalid JSON: {exc}") from exc


def validate(path: Path, derived: Optional[Path] = None) -> Tuple[int, Counter]:
    rows = list(read_jsonl(path))
    if not rows:
        raise ValueError(f"{path}: no records")
    types = Counter()
    for line_number, row in rows:
        missing = REQUIRED - row.keys()
        if missing:
            raise ValueError(f"{path}:{line_number}: missing {sorted(missing)}")
        if row["type"] not in {"channel", "bot"}:
            raise ValueError(f"{path}:{line_number}: unsupported type {row['type']!r}")
        if row["url"] is not None:
            parsed = urlparse(row["url"])
            if parsed.scheme != "https" or parsed.netloc != "t.me":
                raise ValueError(f"{path}:{line_number}: non-public Telegram URL")
        if FORBIDDEN.search(json.dumps(row, ensure_ascii=False)):
            raise ValueError(f"{path}:{line_number}: credential-like field or text found")
        types[row["type"]] += 1
    if derived:
        derived_rows = list(read_jsonl(derived))
        if len(derived_rows) != len(rows):
            raise ValueError(f"{derived}: record count differs from {path}")
        for line_number, row in derived_rows:
            if not row.get("areas"):
                raise ValueError(f"{derived}:{line_number}: missing derived areas")
    return len(rows), types


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("snapshot", type=Path)
    parser.add_argument("--derived", type=Path)
    args = parser.parse_args()
    count, types = validate(args.snapshot, args.derived)
    print(f"OK: {count} records ({types['channel']} channels, {types['bot']} bots)")


if __name__ == "__main__":
    main()
