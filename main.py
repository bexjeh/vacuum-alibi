#!/usr/bin/env python3
"""The Vacuum's Alibi: One Line, 200 Characters.

Writes a single-line excuse from a robot vacuum for missing a spot.
Stdlib only, copy-only entry point.
"""

import os

LINE = (
    "I didn't miss that spot \u2014 my lidar filed it as a nature reserve. "
    "The dust colony in there has better infrastructure than your Wi-Fi."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", ".")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
