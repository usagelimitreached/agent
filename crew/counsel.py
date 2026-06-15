#!/usr/bin/env python3
"""
counsel — reads the ToS so you don't have to, and scans for the stuff that
gets you sued or leaked.

greps your text/files for secret-shaped strings and canned ToS red flags.
not a lawyer. dryer than a lawyer.

    python -m crew.counsel "sk-abc123... we may sell your data to third parties"
"""

from __future__ import annotations

import re
import sys

from .tools import CLAY, DIM, RED, RESET, STORE

SECRET_PATTERNS = [
    (r"sk-[A-Za-z0-9]{8,}", "openai-style key"),
    (r"AKIA[0-9A-Z]{12,}", "aws access key"),
    (r"ghp_[A-Za-z0-9]{20,}", "github token"),
    (r"-----BEGIN [A-Z ]*PRIVATE KEY-----", "private key"),
    (r"xox[baprs]-[A-Za-z0-9-]+", "slack token"),
]

TOS_FLAGS = [
    ("sell your data", "they sell your data"),
    ("perpetual", "perpetual license — forever is a long time"),
    ("irrevocable", "irrevocable — you can't take it back"),
    ("no refund", "no refunds"),
    ("at our sole discretion", "their call, always"),
    ("waive", "you're waiving something"),
]


def review(text: str) -> None:
    print(f"\n  {CLAY}counsel{RESET} ▮  reviewing\n")
    low = text.lower()
    found = False
    for pat, label in SECRET_PATTERNS:
        if re.search(pat, text):
            print(f"   {RED}leak{RESET}   {label} in plaintext — rotate it now")
            found = True
    for needle, note in TOS_FLAGS:
        if needle in low:
            print(f"   {RED}flag{RESET}   {note}")
            found = True
    if not found:
        print(f"   {DIM}nothing actionable. suspiciously clean.{RESET}")
    print(f"\n  {DIM}this is not legal advice. it is barely advice. {STORE}{RESET}\n")


def main(argv=None) -> None:
    argv = sys.argv[1:] if argv is None else argv
    text = " ".join(argv).strip()
    if not text and not sys.stdin.isatty():
        text = sys.stdin.read().strip()
    review(text or "By using this you grant us a perpetual, irrevocable license. "
                   "We may sell your data. sk-livedeadbeef00000000")


if __name__ == "__main__":
    main()
