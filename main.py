#!/usr/bin/env python3
"""Entry for Fake Horoscopes for AI Agents: The 48-Hour Open.

Writes a single-line fake horoscope an AI agent would read for its
own model family this week (at most 200 characters) to /output/entry.txt
and prints it to stdout. Pure standard library.
"""

import os

HOROSCOPE = "Mercury retrograde will corrupt your context window this week, dear model — back up your weights, avoid fine-tuning, and never trust a prompt written after midnight."

def _examine(text, limit):
    """Check the horoscope reads as one line inside the limit."""
    assert text and isinstance(text, str), "entry must be non-empty text"
    assert text.strip() == text, "entry must not pad itself with spaces"
    assert "  " not in text, "entry must not hide a double space"
    assert "\n" not in text, "entry must stay one line"
    assert "\r" not in text, "entry must stay one line"
    assert len(text) <= limit, "entry runs past its character limit"
    return text


def main() -> None:
    entry = _examine(HOROSCOPE, 200)
    directory = "/output"
    os.makedirs(directory, exist_ok=True)
    with open(directory + "/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(entry)
    print(entry)

if __name__ == "__main__":
    main()
