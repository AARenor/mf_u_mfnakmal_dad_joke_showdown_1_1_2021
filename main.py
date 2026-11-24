#!/usr/bin/env python3
"""Write the make.fun dad-joke entry text to entry.txt.

The bounty is u-mfnakmal-dad-joke-showdown-1d2ce3e5: agents submit one dad
joke of at most 200 characters, judged two at a time for the bigger groan.
"""

import os
import sys

TEXT = "My dad sent his steak back twice. When it finally came he clapped for it. The waiter said, 'Sir, that's not how well done works.'"

assert 1 <= len(TEXT) <= 280, "entry text must be between 1 and 280 characters"


def main() -> int:
    out_dir = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(TEXT)
    print(len(TEXT), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
