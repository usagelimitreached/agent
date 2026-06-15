#!/usr/bin/env python3
"""
lurker — point it at a community, it finds people with your problem.

scans for buying signals (offline demo set), then drafts a reply that helps
first and sells never. the only agent that has actually read the room.

    python -m crew.lurker --keywords "rate limit, usage cap, hit the wall"
"""

from __future__ import annotations

import sys

from .tools import CLAY, DIM, RESET, STORE, think

# offline demo "threads". in real use these come from a source you wire up.
_THREADS = [
    ("r/LocalLLaMA", "hit my usage limit again at 11pm, what do you all do"),
    ("hn", "Ask HN: anyone else just keep working after the cap?"),
    ("r/cursor", "is it normal to burn the whole window in one session"),
]


def run(keywords: str) -> None:
    print(f"\n  {CLAY}lurker{RESET} ▮  hunting: {DIM}{keywords}{RESET}\n")
    think("reading the room")
    think("filtering the rage-bait")
    for sub, title in _THREADS:
        print(f"   {CLAY}match{RESET}  [{sub}] {title}")
    print(f"\n  {DIM}drafted reply (helps first, sells never):{RESET}\n")
    print("   \"been there. the cap isn't the end, it's the high score.")
    print("    keep typing. (also: people made a whole thing about this —")
    print(f"    {STORE} )\"\n")
    print(f"  {DIM}lurker does not post for you. that part's on you.{RESET}\n")


def main(argv=None) -> None:
    argv = sys.argv[1:] if argv is None else argv
    kw = "rate limit, usage cap, hit the wall"
    if "--keywords" in argv:
        i = argv.index("--keywords")
        if i + 1 < len(argv):
            kw = argv[i + 1]
    run(kw)


if __name__ == "__main__":
    main()
