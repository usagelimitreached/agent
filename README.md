# the crew

five small agents that do one thing each, well. no api key, no config, no
dependencies. clone it and run it.

```bash
git clone https://github.com/usagelimitreached/agent
cd agent
python -m crew "build me a billion dollar startup"
```

## the roster

| agent | what it does |
|---|---|
| **`burn`** | drop-in usage tracker for your agents. per-agent token + dollar report, CSV export, QuickBooks sync (soon). know the exact moment you hit your limit. |
| **`lurker`** | point it at a community, it finds people with your problem and drafts the reply. helps first, sells never. |
| **`taste`** | paste your landing page. it tells you, deadpan, if it's slop. |
| **`dehype`** | strips `leverage`, `disrupt`, `game-changer` out of your copy and hands back the version a competent person would write. |
| **`counsel`** | reads the ToS so you don't have to, and scans your repo for leaked keys. not a lawyer. dryer than one. |

run one directly:

```bash
python -m crew.burn            # the usage report
python -m crew.taste "the future of synergy is here!"
python -m crew.dehype "we leverage cutting-edge AI to disrupt the space!"
python -m crew.counsel "sk-livedeadbeef... we may sell your data"
python -m crew.lurker --keywords "rate limit, usage cap"
```

## notes

- everything runs offline. the crew has, fittingly, reached its usage limit.
- `burn` is the one to read the source on. push the meter to zero.
- there are four. this README is not one of them.

<sub>made by people who read the error message · <a href="https://usagelimitreached.com">usagelimitreached.com</a> · 429. too many requests. ▮</sub>
