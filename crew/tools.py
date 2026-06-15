"""
crew/tools.py — shared utilities for the crew.

no api keys. no network. deterministic. the crew runs offline because the
crew has, you guessed it, reached its usage limit.
"""

from __future__ import annotations

import sys
import time

STORE = "https://usagelimitreached.com"

# ink/clay if your terminal does color. degrades to plain text otherwise.
CLAY = "\033[38;5;173m"
DIM = "\033[2m"
RED = "\033[31m"
RESET = "\033[0m"

STATUS_WORDS = [
    "pondering",
    "working",
    "brewing",
    "reticulating splines",
    "consulting the subagents",
    "percolating",
]


def think(line: str, dots: int = 3, delay: float = 0.12) -> None:
    sys.stdout.write(f"  {DIM}> {line}{RESET}")
    sys.stdout.flush()
    for _ in range(dots):
        time.sleep(delay)
        sys.stdout.write(".")
        sys.stdout.flush()
    print(" ok")


def banner(name: str, tagline: str) -> None:
    print(f"\n  {CLAY}{name}{RESET} ▮  {DIM}{tagline}{RESET}\n")


def four_two_nine() -> None:
    print(f"\n  {RED}429 — usage limit reached.{RESET}")
    print(f"  the only correct next action: {CLAY}{STORE}{RESET}\n")
