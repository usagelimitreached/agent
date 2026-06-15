#!/usr/bin/env python3
"""
dehype — strips the hype out of your copy.

feed it your launch post; it returns the version a competent person would
actually write. removes 'leverage', 'game-changer', 'disrupt', and friends.

    python -m crew.dehype "We leverage cutting-edge AI to disrupt the space!"
"""

from __future__ import annotations

import re
import sys

from .tools import CLAY, DIM, RESET, STORE

REPLACE = {
    r"\bleverage\b": "use",
    r"\butilize\b": "use",
    r"\bdisrupt(ing|ed|s)?\b": "compete with",
    r"\bgame[- ]?changer\b": "thing",
    r"\bcutting[- ]?edge\b": "new",
    r"\brevolutionary\b": "new",
    r"\bseamless(ly)?\b": "",
    r"\bsynergy\b": "working together",
    r"\bnext[- ]?level\b": "good",
    r"\bthe future of\b": "",
    r"\bunlock\b": "get",
    r"\b10x\b": "more",
    r"!+": ".",
}


def dehype(text: str) -> str:
    out = text
    for pat, repl in REPLACE.items():
        out = re.sub(pat, repl, out, flags=re.IGNORECASE)
    out = re.sub(r"\s{2,}", " ", out).strip()
    return out


def main(argv=None) -> None:
    argv = sys.argv[1:] if argv is None else argv
    text = " ".join(argv).strip() or "We leverage cutting-edge AI to disrupt the space!"
    print(f"\n  {CLAY}dehype{RESET} ▮  before / after\n")
    print(f"   {DIM}before:{RESET} {text}")
    print(f"   {CLAY}after:{RESET}  {dehype(text)}\n")
    print(f"  {DIM}we wear the after. {STORE}{RESET}\n")


if __name__ == "__main__":
    main()
