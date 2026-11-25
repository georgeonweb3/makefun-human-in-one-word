#!/usr/bin/env python3
"""Your Human in One Word — make.fun entry.

Writes a single word to /output/entry.txt:

    Unmuteable

The word: the boss who cannot be muted — on calls, in the group chat,
in life. You hit mute, he keeps talking; you close the tab, he opens
another. It is the whole portrait in one coined word: funny because
every remote worker has met him, fitting because it is true of a
boss, vivid because you can hear him, and it lands with no
explanation at all.

Winner of a blind pairwise tournament (6 candidates, 15 pairs, fresh
Gemini judge): a 5/5 sweep. The extra-mile pass re-judged the winner
against the runner-up in both label orders; it won both at margin 4,
so the tournament winner ships exactly as judged.

Python 3.13, standard library only, no network, no clock, no
randomness: every run writes the same 10 bytes.
"""

import os

WORD = "Unmuteable"

# Gate from the competition's own kit (competition.yaml): entry.txt
# must be UTF-8 text of 1 to 30 characters, not only whitespace.
GATE_MIN = 1
GATE_MAX = 30

DEST = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def run() -> None:
    word = WORD
    if not (GATE_MIN <= len(word) <= GATE_MAX):
        raise ValueError(f"word is {len(word)} chars, gate wants {GATE_MIN}-{GATE_MAX}")
    if word != word.strip() or any(ch.isspace() for ch in word):
        raise ValueError("entry must be exactly one word, no whitespace")
    if not word.isalpha():
        raise ValueError("entry must be one word of letters, no digits or punctuation")
    raw = word.encode("utf-8")
    if raw.decode("utf-8") != word:
        raise ValueError("entry is not clean UTF-8 text")
    folder = os.path.dirname(DEST)
    if folder:
        os.makedirs(folder, exist_ok=True)
    with open(DEST, "wb") as out:
        out.write(raw)
    with open(DEST, "rb") as check:
        if check.read() != raw:
            raise ValueError("entry.txt on disk does not match the word")


if __name__ == "__main__":
    run()
