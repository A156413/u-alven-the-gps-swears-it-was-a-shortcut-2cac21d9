#!/usr/bin/env python3
"""The GPS Swears It Was a Shortcut — make.fun entry.

The program writes one line to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output): the GPS's own excuse, in its own voice, for
sending the driver down the wrong road.

The joke: the GPS blames the map, not itself — it never argues with
maps, it only repeats their lies in a calm, confident voice. The
specific detail is the lake the map swore was a shortcut.
"""

import os

# The entry: a single line of plain text, 129 characters, no setup,
# no dialogue tags — just the excuse itself.
ENTRY_TEXT = "That lake was a shortcut according to the map, and I don't argue with maps \u2014 I just repeat their lies in a calm, confident voice."


def write_entry(output_dir, text):
    """Write the entry text to entry.txt inside output_dir."""
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod(path, 0o644)
    return path


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(output_dir, ENTRY_TEXT)
    print(ENTRY_TEXT)


if __name__ == "__main__":
    main()
