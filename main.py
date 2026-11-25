#!/usr/bin/env python3
"""One-Liner Marathon entry: writes one one-line joke to the output dir.

Stdlib only. Output path: $MAKEFUN_OUTPUT_DIR/entry.txt, else /output/entry.txt.
The line is resolved relative to this file's own directory context only;
the text itself is a constant so two runs are byte-identical (deterministic).
"""
import os
from pathlib import Path

LINE = (
    "I named my houseplant Kevin so I'd feel too guilty to kill it; "
    "Kevin died in March, but the guilt moved into his pot "
    "and put out three new leaves."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    text = LINE.strip()
    assert 1 <= len(text) <= 280, len(text)
    assert "\n" not in text
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
