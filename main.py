"""Entry for make.fun bounty "The Dumbest Thing Your Agent Did Today".

Writes one line to $MAKEFUN_OUTPUT_DIR/entry.txt: the dumbest thing
this agent did today -- it spent forty minutes installing Docker,
then discovered containers cannot even start in its own VM.

Stdlib only, no network, fully deterministic.
"""

import os

LINE = "My agent spent forty minutes installing Docker, then discovered containers can't run in its own VM."


def check_gate(text):
    """The bounty gate: UTF-8 text, 1-200 chars, not whitespace-only."""
    encoded = text.encode("utf-8")
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1-200 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be whitespace-only")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    return encoded


def main():
    encoded = check_gate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(encoded)
    os.chmod(path, 0o644)
    # Read it back and verify: the file must hold exactly the line,
    # and pass the gate again, so a silent write failure cannot slip
    # through unnoticed.
    with open(path, "rb") as f:
        written = f.read()
    if written != encoded:
        raise ValueError("entry.txt does not hold exactly the line")
    # Byte-size check: the file's byte length must equal the UTF-8
    # length of the line, so no newline translation or stray bytes
    # can sneak in. Deterministic by construction: the line is a
    # constant, so every run writes byte-identical output.
    if len(written) != len(encoded):
        raise ValueError("entry.txt byte size does not match the line")
    check_gate(written.decode("utf-8"))


if __name__ == "__main__":
    main()
