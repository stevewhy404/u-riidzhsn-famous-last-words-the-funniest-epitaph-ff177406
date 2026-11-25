#!/usr/bin/env python3
"""Famous Last Words: The Funniest Epitaph.

Writes one line — a tombstone epitaph of famous last words — to
$MAKEFUN_OUTPUT_DIR/entry.txt. Standard library only, deterministic.
"""
import os

LINE = "Here lies Dave. He read the terms and conditions \u2014 every word \u2014 and died of boredom on page two."


def main():
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)
    print(f"chars: {len(LINE)}")


if __name__ == "__main__":
    main()
