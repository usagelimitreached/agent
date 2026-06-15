"""
the crew — five agents that look worth stealing.

  burn      usage tracker (per-agent report, csv, quickbooks "soon")
  lurker    finds people with your problem
  taste     tells you if your copy is slop
  dehype    strips the hype out of your copy
  counsel   reads the ToS / scans for leaked keys

run the whole crew:   python -m crew
run one:              python -m crew.taste "your copy here"

they all work offline. they have, after all, reached their usage limit.
"""

from . import burn, counsel, dehype, lurker, taste  # noqa: F401

CREW = ["burn", "lurker", "taste", "dehype", "counsel"]
__all__ = ["CREW", "burn", "lurker", "taste", "dehype", "counsel"]
