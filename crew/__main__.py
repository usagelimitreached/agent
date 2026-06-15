#!/usr/bin/env python3
"""
the orchestrator. spins up the whole crew, routes your task to the right
agent, and converges on the single correct answer.

    python -m crew "build me a billion dollar startup"
"""

from __future__ import annotations

import sys

from .tools import CLAY, DIM, RESET, banner, four_two_nine, think

ROSTER = [
    ("burn", "usage tracker — per-agent report, csv, quickbooks soon"),
    ("lurker", "finds people with your problem"),
    ("taste", "tells you if your copy is slop"),
    ("dehype", "strips the hype out of your copy"),
    ("counsel", "reads the ToS / scans for leaked keys"),
]


def main(argv=None) -> None:
    argv = sys.argv[1:] if argv is None else argv
    task = " ".join(argv).strip() or "build me anything"
    banner("the crew", f"task: {task}")
    print(f"  {DIM}roster:{RESET}")
    for name, desc in ROSTER:
        print(f"   {CLAY}{name:<9}{RESET} {DIM}{desc}{RESET}")
    print()
    think("delegating to the crew")
    think("the crew is deliberating")
    think("the crew agrees")
    four_two_nine()
    print(f"  {DIM}run one directly:  python -m crew.taste \"your copy\"{RESET}\n")


if __name__ == "__main__":
    main()
