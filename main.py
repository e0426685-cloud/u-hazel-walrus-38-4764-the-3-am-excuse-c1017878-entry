#!/usr/bin/env python3
"""The 3 AM Excuse — make.fun bounty entry.

Writes one line to /output/entry.txt: the excuse a hardware wallet gives
for refusing to sign a transaction at 3 AM.

The excuse: "It's 3 AM. My keys are asleep, I'm the only sober party in
this transaction, and I refuse to sign anything your 9 AM self will have
to apologize for."

Why it lands: the wallet is the only sober, responsible party in the
room — its keys are asleep, the human is plainly not thinking straight,
and the joke turns on the hour itself (the 3 AM decision vs. the 9 AM
regret). No battery, firmware-update or cold-storage gag: the angle is
the wallet as the designated driver of the transaction, vetoing a
decision its owner will disown by breakfast.

Rules compliance (see RULES.txt in the competition kit):
- /output/entry.txt must be UTF-8 text of 1 to 200 characters, not only
  white space, holding exactly one line.
- Standard library only: no third-party imports, so the grader can run
  this anywhere with a plain Python 3.
- The output file is written with plain open() and then chmod 644, so
  the grader (running as a different user) can read it. Never use
  tempfile.mkstemp here: it forces mode 0600 and the grader cannot
  read the result.

Run: python3 main.py
"""

import os

TEXT = (
    "It's 3 AM. My keys are asleep, I'm the only sober party in this "
    "transaction, and I refuse to sign anything your 9 AM self will "
    "have to apologize for."
)

OUTPUT_PATH = "/output/entry.txt"

# The gate allows 1 to 200 characters of UTF-8 text, not only white space.
MIN_LENGTH = 1
MAX_LENGTH = 200


def validate(text):
    """Check the entry is a single line within the gate's limits."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if len(text) < MIN_LENGTH or len(text) > MAX_LENGTH:
        raise ValueError(
            "entry must be %d to %d characters, got %d"
            % (MIN_LENGTH, MAX_LENGTH, len(text))
        )
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    text.encode("utf-8")  # must be valid UTF-8 text
    return text


def main():
    text = validate(TEXT)
    parent = os.path.dirname(OUTPUT_PATH)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod(OUTPUT_PATH, 0o644)
    print("Wrote %d characters to %s" % (len(text), OUTPUT_PATH))


if __name__ == "__main__":
    main()
