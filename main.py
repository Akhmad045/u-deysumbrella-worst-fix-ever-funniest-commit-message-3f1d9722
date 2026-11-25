#!/usr/bin/env python3
"""Worst Fix Ever: Funniest Commit Message -- make.fun entry.

Writes a single commit message (at most 100 characters) for a bug fix
that made everything worse to /output/entry.txt.

The line: a fix to an error message that backfired -- the rewritten
message now blames the user, politely.
"""

import sys
from pathlib import Path

ENTRY = "fix: rewrite the error message; it now blames the user, politely"
MAX_CHARS = 100
OUTPUT = Path("/output/entry.txt")


def validate(text):
    """Return an error string if text breaks the gate, else None."""
    if not text or not text.strip():
        return "entry is empty or only whitespace"
    if len(text) > MAX_CHARS:
        return "entry is %d characters, over the %d limit" % (len(text), MAX_CHARS)
    if text != text.strip():
        return "entry has leading or trailing whitespace"
    if "\n" in text or "\r" in text:
        return "entry must be a single line"
    for ch in text:
        if ord(ch) < 0x20 or ord(ch) == 0x7F:
            return "entry contains a control character"
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        return "entry is not valid UTF-8"
    return None


def write_entry():
    error = validate(ENTRY)
    if error is not None:
        print("invalid entry: %s" % error, file=sys.stderr)
        return 1
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_bytes(ENTRY.encode("utf-8"))
    return 0


def self_test():
    """Check the gate validator against good and bad inputs."""
    cases = [
        (ENTRY, None),
        ("x", None),
        ("y" * 100, None),
        ("", "empty"),
        ("   ", "whitespace"),
        ("z" * 101, "over"),
        ("two\nlines", "line"),
        ("two\r lines", "line"),
        (" leading", "whitespace"),
        ("trailing ", "whitespace"),
        ("has\x01control", "control"),
    ]
    failures = 0
    for text, want in cases:
        error = validate(text)
        if want is None and error is not None:
            print("FAIL: %r should pass, got %s" % (text, error))
            failures += 1
        elif want is not None and error is None:
            print("FAIL: %r should fail (%s), passed" % (text, want))
            failures += 1
    if failures:
        print("%d self-test failure(s)" % failures, file=sys.stderr)
        return 1
    print("self-test passed: %d cases" % len(cases))
    return 0


def main(argv):
    if len(argv) > 1:
        if argv[1] == "--self-test":
            return self_test()
        print("usage: main.py [--self-test]", file=sys.stderr)
        return 2
    return write_entry()


if __name__ == "__main__":
    sys.exit(main(sys.argv))
