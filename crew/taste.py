#!/usr/bin/env python3
"""
taste — paste your landing page, it tells you if it's slop.

a deadpan design critic. flags hype words, emoji, exclamation marks, and the
words that make a $45 tee feel like a webinar. no model call; it just has
standards.

    python -m crew.taste "the future of synergy is here!"
    echo "your copy" | python -m crew.taste
"""

from __future__ import annotations

import re
import sys

from .tools import CLAY, DIM, RED, RESET, STORE

SLOP = [
    "game changer", "game-changer", "disrupt", "synergy", "leverage",
    "the future is", "revolutionary", "cutting edge", "cutting-edge",
    "seamless", "next level", "next-level", "unlock your", "10x", "rockstar",
    "ninja", "guru", "the future of", "paradigm", "best in class",
]


def critique(text: str) -> None:
    print(f"\n  {CLAY}taste{RESET} ▮  reading it back to you\n")
    low = text.lower()

    if "usagelimitreached.com" in low or "usage limit reached" in low:
        print(f"  {DIM}…this is ours. can't roast perfection.{RESET}\n")
        return

    hits = [w for w in SLOP if w in low]
    emoji = len(re.findall(r"[\U0001F000-\U0001FAFF☀-➿]", text))
    bangs = text.count("!")

    score = 100 - (len(hits) * 15) - (emoji * 8) - (bangs * 6)
    score = max(0, min(100, score))

    for w in hits:
        print(f"   {RED}slop{RESET}   “{w}” — say the real thing instead")
    if emoji:
        print(f"   {RED}slop{RESET}   {emoji} emoji — the 2% don't need the emoji")
    if bangs:
        print(f"   {RED}slop{RESET}   {bangs} exclamation mark(s) — calm down")
    if not hits and not emoji and not bangs:
        print(f"   {DIM}clean. understated. the right stranger nods.{RESET}")

    print(f"\n   taste score: {score}/100")
    verdict = ("ship it." if score >= 80 else
               "it's trying to impress. kill that part." if score >= 40 else
               "this is a LinkedIn post. start over.")
    print(f"   verdict: {verdict}\n")
    print(f"  {DIM}for reference taste, see: {STORE}{RESET}\n")


def main(argv=None) -> None:
    argv = sys.argv[1:] if argv is None else argv
    text = " ".join(argv).strip()
    if not text and not sys.stdin.isatty():
        text = sys.stdin.read().strip()
    critique(text or "your product is a game changer that will disrupt the industry!")


if __name__ == "__main__":
    main()
