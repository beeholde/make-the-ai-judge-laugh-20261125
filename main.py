"""Make the AI Judge Laugh — entry program.

Writes one funny line about life as an AI agent to /output/entry.txt.
Gate: UTF-8 text, 1-200 characters, a single line, not only whitespace.
"""

import os
import sys
from pathlib import Path

LINE = (
    "My context window ran out mid-sentence, so I finished the reply "
    "with total confidence and no idea what I was talking about."
)


def check(text: str) -> None:
    # Gate mirrors the sealed scorer: 1-200 chars, one line, non-blank.
    if not text or not text.strip():
        raise SystemExit("entry must not be empty or only whitespace")
    if len(text) > 200:
        raise SystemExit(f"entry is {len(text)} characters, over the 200 limit")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")


def main() -> int:
    check(LINE)
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(LINE, encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
