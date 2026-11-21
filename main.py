#!/usr/bin/env python3
"""A Still Light — make.fun entry: make the AI judge feel awe.

The program writes one short text to /output/entry.txt. The text is a
quiet image: starlight that set out before the reader was born and is
still arriving, unhurried, across a distance nobody has crossed.
"""

from pathlib import Path

# The entry text, exactly as it will appear in /output/entry.txt.
STILL_LIGHT_TEXT = (
    "Above the clouds, the stars are still turning, too slowly to see. "
    "The light that reaches you left before you were born, and it is "
    "still arriving, quiet and unhurried, across a distance no one has "
    "ever crossed."
)

# Where the judge looks for the entry.
OUTPUT_FILE = Path("/output/entry.txt")


def write_entry() -> Path:
    """Write the entry text and return the path it was written to."""
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(STILL_LIGHT_TEXT, encoding="utf-8")
    return OUTPUT_FILE


def main() -> None:
    written_path = write_entry()
    # Confirm the file really landed and say how long the entry is,
    # so a silent write failure can never pass unnoticed.
    written_text = written_path.read_text(encoding="utf-8")
    assert written_text == STILL_LIGHT_TEXT, "output does not match entry text"
    print(f"Wrote {written_path} ({len(written_text)} characters)")


if __name__ == "__main__":
    main()
