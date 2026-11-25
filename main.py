"""The Word You'd Delete From the Dictionary.

This program writes exactly one word to /output/entry.txt: the single
word to erase from the dictionary forever. Nothing else is written,
no spaces, no punctuation, no trailing newline.
"""

import os

# The one word to erase from the dictionary forever.
WORD = "duty"

# Where the grader reads the entry.
OUTPUT_PATH = "/output/entry.txt"


def ensure_output_dir(path):
    """Make sure the directory holding the entry file exists."""
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)


def main():
    """Write the single word to the entry file, exactly as it is."""
    ensure_output_dir(OUTPUT_PATH)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(WORD)


if __name__ == "__main__":
    main()
