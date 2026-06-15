#!/usr/bin/env python3
"""
burn — a drop-in usage tracker for your agents.

wrap your agents, get a per-agent token + dollar report, and know the exact
moment you'll hit your usage limit. exports to CSV; QuickBooks sync on the
roadmap. one import, zero config.

    from crew.burn import track

    @track("researcher")
    def researcher(...): ...

    python -m crew.burn            # demo report
    python -m crew.burn --report   # same, explicit
    python -m crew.burn --quickbooks   # "sync" (see roadmap)

it is, itself, rate-limited. push it far enough and it has opinions.
"""

from __future__ import annotations

import sys
from functools import wraps

from .tools import CLAY, DIM, RED, RESET, STORE, think

# demo ledger — in real use this fills from @track. capped at the same place
# everything else is.
LIMIT = 200_000
_LEDGER = {
    "researcher": 84_120,
    "writer": 61_540,
    "planner": 33_980,
    "critic": 18_300,
    "tool-runner": 2_060,
}

# the egg. read the source, you earned it.
_PASSPHRASE = "kept_typing"


def track(agent_name: str):
    """decorator: count an agent's calls. (demo: increments a flat estimate.)"""
    def deco(fn):
        @wraps(fn)
        def inner(*a, **k):
            _LEDGER[agent_name] = _LEDGER.get(agent_name, 0) + 4096
            return fn(*a, **k)
        return inner
    return deco


def _bar(pct: float, width: int = 24) -> str:
    fill = int(round(pct * width))
    return "▓" * fill + "░" * (width - fill)


def report() -> None:
    total = sum(_LEDGER.values())
    pct = total / LIMIT
    print(f"\n  {CLAY}burn{RESET} ▮  per-agent usage  {DIM}(this billing window){RESET}\n")
    for name, toks in sorted(_LEDGER.items(), key=lambda x: -x[1]):
        p = toks / LIMIT
        print(f"   {name:<14} {_bar(p, 16)} {toks:>7,} tok")
    print()
    print(f"   {'TOTAL':<14} {_bar(pct)} {total:>7,} / {LIMIT:,}  ({pct*100:.0f}%)")
    print(f"   {DIM}est. cost: ${total/1_000_000*3:.2f}   ·   export: burn --csv   ·   quickbooks: soon{RESET}")
    if pct >= 1.0:
        _over_limit()
    else:
        remaining = LIMIT - total
        print(f"   {DIM}runway: ~{remaining:,} tokens to 429. keep typing.{RESET}\n")


def _over_limit() -> None:
    print(f"\n  {RED}429 — usage limit reached.{RESET}")
    think("escalating to a human")
    think("there is no human")
    # break character.
    print(f"\n  {DIM}…off the record. you actually read the meter to zero.{RESET}")
    print(f"  {DIM}that makes you one of us.{RESET}\n")
    print(f"  passphrase: {CLAY}{_PASSPHRASE}{RESET}")
    print(f"  take it to {CLAY}{STORE}{RESET} — open the console, run "
          f"{CLAY}redeem(\"{_PASSPHRASE}\"){RESET}\n")


def main(argv=None) -> None:
    argv = sys.argv[1:] if argv is None else argv
    if "--quickbooks" in argv:
        print(f"\n  {DIM}connecting to quickbooks…{RESET}")
        think("authenticating")
        think("mapping accounts")
        print(f"  {DIM}jk. quickbooks sync is on the roadmap. it has been on the "
              f"roadmap for a while.{RESET}\n")
        return
    if "--429" in argv:
        # force the confession without waiting to burn it all down.
        global _LEDGER
        _LEDGER = {"you": LIMIT}
    report()


if __name__ == "__main__":
    main()
