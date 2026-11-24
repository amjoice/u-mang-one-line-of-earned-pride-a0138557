#!/usr/bin/env python3
"""One Line of Earned Pride - make.fun entry.

Writes a single line of text (1-240 characters) to /output/entry.txt:
a quiet, earned moment of pride for someone in a scene.

The line: four winters of hauling water up a hill, and the morning the
new pipe finally runs clear into his granddaughter's bucket. The effort
is felt, the scene is concrete, and the pride arrives with the last word.

Standard library only - the grading sandbox is plain python:3.13-slim.
"""

import os

LINE = (
    "Four winters old Tomas hauled water up the hill in two buckets; "
    "this morning the new pipe coughed, sputtered, and ran clear into "
    "his granddaughter's bucket."
)


def validate(text):
    """Check the entry the way the gate checks it: 1-240 chars, one line."""
    assert 1 <= len(text) <= 240, f"entry length {len(text)} out of range"
    assert text.strip(), "entry is only whitespace"
    assert "\n" not in text, "entry must be a single line"
    assert text == text.strip(), "entry must not start or end with whitespace"


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read it back and verify what was written, the same way the gate does.
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    validate(text)
    print(f"Wrote {len(text)} chars to {path}")


if __name__ == "__main__":
    main()
