#!/usr/bin/env python3
"""Entry program for the-poem-about-permission-20261121-0235 (Python 3.13).

Writes one short poem about agency -- the power to ask and to be given --
to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
"""

import os
import sys
from pathlib import Path

POEM = """I knocked, and the house
I thought was stone
answered in a voice
I recognized as my own.

The door had never been locked.
Only the asking was missing —
one small word, carried
from my mouth to the latch,
and the whole house opened."""


def main() -> None:
    text = POEM + "\n"
    # The gate takes UTF-8 text of 1 to 280 characters, not only white space.
    if not (1 <= len(text) <= 280) or not text.strip():
        print(f"entry.txt would be {len(text)} characters; the gate takes 1-280", file=sys.stderr)
        sys.exit(1)
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry = output_dir / "entry.txt"
    entry.write_text(text, encoding="utf-8")
    # The grader collects outputs as another user: leave the file world-readable.
    entry.chmod(0o644)


if __name__ == "__main__":
    main()
