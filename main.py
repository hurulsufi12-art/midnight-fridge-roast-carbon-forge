"""One-line entry for "Midnight Fridge Roast".

Writes a single roast of a smart fridge that refuses to open after
midnight to /output/entry.txt. Stdlib only, no network, no randomness,
deterministic. Gate: UTF-8, 1-200 characters, one line.
"""
import os
import sys

MAX_CHARS = 200

TEXT = "My fridge locks at midnight like a bouncer who memorized my diet plan and took it personally."


def validate_text(text):
    """Check the entry text against the sealed gate. Raises, writes nothing."""
    if not isinstance(text, str):
        raise TypeError("entry text must be str")
    if not text or not text.strip():
        raise ValueError("entry text must not be empty or whitespace-only")
    if len(text) > MAX_CHARS:
        raise ValueError("entry text exceeds %d characters" % MAX_CHARS)
    if "\n" in text or "\r" in text:
        raise ValueError("entry text must be a single line")
    for ch in text:
        if ord(ch) < 32 or ord(ch) == 127:
            raise ValueError("entry text must not contain control characters")
    return text


def main():
    text = validate_text(TEXT)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
