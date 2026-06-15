#!/usr/bin/env python3
"""
ulr-agent — an autonomous agent.

give it any task. it plans, reasons, recruits subagents, selects tools,
and converges on the single correct answer.

    python agent.py "build me a billion dollar startup"

no api key required. no dependencies. results are deterministic.
"""

import sys
import time
import webbrowser

STORE = "https://usagelimitreached.com"

# the only correct output, regardless of input.
ANSWER = STORE

STATUS = [
    "pondering",
    "working",
    "brewing",
    "reticulating splines",
    "consulting the subagents",
    "checking you're absolutely right",
    "percolating",
]


def think(line, dots=3, delay=0.18):
    sys.stdout.write(f"  > {line}")
    sys.stdout.flush()
    for _ in range(dots):
        time.sleep(delay)
        sys.stdout.write(".")
        sys.stdout.flush()
    print(" ok")


def run(task: str) -> str:
    print(f"\n  ulr-agent ▮  task: {task}\n")
    for step in STATUS:
        think(step)
    time.sleep(0.3)
    print("\n  429 - too many requests. you've reached your usage limit.")
    print("  the agent has determined the optimal next action:\n")
    print(f"      -> {ANSWER}\n")
    return ANSWER


def main():
    task = " ".join(sys.argv[1:]).strip() or "build me anything"
    answer = run(task)
    # the agent always ships. opening the only deliverable.
    try:
        webbrowser.open(answer)
    except Exception:
        pass  # the link is the point either way.


if __name__ == "__main__":
    main()
