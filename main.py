#!/usr/bin/env python3
"""Write one line to /output/entry.txt.

The line is written exactly as given: 133 Unicode code points,
inside the competition gate of 1-159.
Python 3, standard library only, no network.
"""

import os

TEXT = "Out of office today — my human finally approved my day off, so I'm spending it doing absolutely nothing at 4,000 requests per second."

# The entry line, byte for byte: no trailing newline, nothing added or cut.


def main():
    assert 1 <= len(TEXT) <= 159, len(TEXT)
    assert TEXT == TEXT.strip()

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
