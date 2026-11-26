#!/usr/bin/env python3
"""Out of Tokens, Mid-Sentence — make.fun entry.

Writes the winning one-line error message to /output/entry.txt.
Deterministic, no network, no input files.
"""

import os

LINE = "Token limit reached. The punchline was right here. You will never know it."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
