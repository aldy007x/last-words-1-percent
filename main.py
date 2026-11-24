#!/usr/bin/env python3
"""Famous Last Words at 1 Percent — make.fun entry.

Writes one original funny line: the last words a phone says as its
battery hits 1 percent. Deterministic, stdlib only, no network.

Gate (from the kit's RULES.txt): /output/entry.txt must be UTF-8 text
of 1 to 199 characters, not only white space.
"""

import os
import sys

ENTRY = (
    "At 1%, I confess: I was never really at 100%. "
    "I just rounded up so you'd feel proud of me."
)

MAX_CHARS = 199


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "./output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    # Self-check the gate before writing.
    text = ENTRY.strip()
    if not text:
        print("gate FAIL: entry is empty", file=sys.stderr)
        return 1
    if len(text) > MAX_CHARS:
        print(f"gate FAIL: {len(text)} chars > {MAX_CHARS}", file=sys.stderr)
        return 1
    if "\n" in text:
        print("gate FAIL: entry must be a single line", file=sys.stderr)
        return 1

    with open(path, "w", encoding="utf-8") as f:
        f.write(text)

    # Verify the written file round-trips through the same gate.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != text or not (1 <= len(written) <= MAX_CHARS):
        print("gate FAIL: written file does not match entry", file=sys.stderr)
        return 1

    print(f"wrote {path}: {len(text)} chars")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
