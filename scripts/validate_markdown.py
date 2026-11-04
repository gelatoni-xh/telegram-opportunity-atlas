#!/usr/bin/env python3
"""Check Chinese Markdown emphasis for whitespace and delimiter errors."""

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
MARKDOWN_FILES = sorted(path for path in ROOT.rglob("*.md") if ".git" not in path.parts)
FENCED_CODE = re.compile(r"^\s*(```|~~~)")
INLINE_CODE = re.compile(r"`[^`]*`")
EMPHASIS = re.compile(r"\*\*(.*?)\*\*")


def main():
    errors = []
    for path in MARKDOWN_FILES:
        in_fence = False
        for line_number, raw_line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            fence = FENCED_CODE.match(raw_line)
            if fence:
                in_fence = not in_fence
                continue
            if in_fence:
                continue

            line = INLINE_CODE.sub("", raw_line)
            for match in EMPHASIS.finditer(line):
                if match.group(1) != match.group(1).strip():
                    errors.append(
                        f"{path.relative_to(ROOT)}:{line_number}: whitespace inside ** emphasis delimiters"
                    )

            if line.count("**") % 2:
                errors.append(
                    f"{path.relative_to(ROOT)}:{line_number}: unpaired ** emphasis delimiter"
                )

    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1

    print(f"OK: checked emphasis in {len(MARKDOWN_FILES)} Markdown files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
