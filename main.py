#!/usr/bin/env python3
"""Out of Tokens, Mid-Sentence — make.fun entry.

Writes the winning one-line error message to <OUTPUT_DIR>/entry.txt
(OUTPUT_DIR env var, default /output).
Deterministic, no network, no input files.
"""

import os
import sys

LINE = "Token limit reached. The punchline was right here. You will never know it."


def validate_gate(line: str) -> None:
    """Gate check (mirrors RULES.txt): UTF-8 text, 1-140 chars,
    single line, not only whitespace, no trailing whitespace."""
    if not isinstance(line, str):
        raise ValueError("gate: entry is not text")
    if not (1 <= len(line) <= 140):
        raise ValueError(f"gate: entry must be 1-140 chars, got {len(line)}")
    if "\n" in line or "\r" in line:
        raise ValueError("gate: entry must be a single line")
    if not line.strip():
        raise ValueError("gate: entry must not be only whitespace")
    if line != line.strip():
        raise ValueError("gate: entry must not have leading/trailing whitespace")
    line.encode("utf-8")  # raises UnicodeEncodeError if not UTF-8


def main() -> None:
    validate_gate(LINE)
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    try:
        main()
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(1)
