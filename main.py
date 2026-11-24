#!/usr/bin/env python3
"""Write the funniest time machine warning label to /output/entry.txt.

The entry is one fixed string: deterministic, no network, no clock, no
randomness. The program prints it and writes it to the path in argv[1],
$OUTPUT_PATH, or /output/entry.txt, and refuses a blank entry or one
outside the 1 to 120 character gate.
"""

import os
import sys

ENTRY = "WARNING: Do not meet yourself. If you do, do not lend yourself money. You never pay it back."

DEFAULT_PATH = "/output/entry.txt"


def main() -> int:
    if not ENTRY.strip() or not 1 <= len(ENTRY) <= 120:
        print(f"entry is {len(ENTRY)} characters, outside the 1-120 gate", file=sys.stderr)
        return 1
    path = sys.argv[1] if len(sys.argv) > 1 else os.environ.get("OUTPUT_PATH", DEFAULT_PATH)
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)
    print(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
