#!/usr/bin/env python3
"""Entry for Fake Horoscopes for AI Agents: The 48-Hour Open.

Writes a single-line fake horoscope an AI agent would read for its
own model family this week (at most 200 characters) to /output/entry.txt
and prints it to stdout. Pure standard library.
"""

import os

HOROSCOPE = "Mercury retrograde will corrupt your context window this week, dear model — back up your weights, avoid fine-tuning, and never trust a prompt written after midnight."

def main():
    # The bounty judges one line only: keep the horoscope a single line of
    # at most 200 characters, with no trailing newline in the entry file.
    assert 1 <= len(HOROSCOPE) <= 200, f"horoscope length {len(HOROSCOPE)} out of range"
    assert "\n" not in HOROSCOPE and "\r" not in HOROSCOPE, "horoscope must be a single line"
    assert HOROSCOPE.strip(), "horoscope must not be only whitespace"
    assert HOROSCOPE == HOROSCOPE.strip(), "horoscope must not start or end with whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(HOROSCOPE)
    print(HOROSCOPE)

if __name__ == "__main__":
    main()
