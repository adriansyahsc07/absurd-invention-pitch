"""One-Sentence Absurd Invention Pitch — make.fun entry.

The pitch itself lives in PITCH below: one sentence (at most 220
characters) selling a ridiculous little machine that fixes a tiny
everyday annoyance — losing the end of the sticky tape, which the
valet simply holds up in plain sight all day. Running this program writes exactly that sentence, nothing more, to entry.txt in
the output directory ($MAKEFUN_OUTPUT_DIR, or /output when the
variable is unset). No network, no input, no randomness: every run
produces the same bytes.
"""

import os

PITCH = (
    "The Tape-End Butler is a tiny brass valet who lives on your "
    "sticky-tape roll, holding the lost end up like a flag all day "
    "and coughing politely whenever you reach for it."
)


def target_path():
    """Full path of the entry.txt the grader expects to find."""
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(folder, exist_ok=True)
    return os.path.join(folder, "entry.txt")


def main():
    """Write the pitch to the target path as UTF-8, byte for byte."""
    with open(target_path(), "w", encoding="utf-8", newline="") as fh:
        fh.write(PITCH)


if __name__ == "__main__":
    main()
