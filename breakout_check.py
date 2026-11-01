"""breakout_check.py - how often does an N-day high breakout fail, compared with a baseline?

A breakout: the daily close is above the highest high of the previous N days.
The level is that previous high. It fails if, within the next K days, any
daily close is back below the level.

Three numbers are printed:
  1. all breakouts (overlapping ones counted separately)
  2. independent breakouts: a new breakout counts only after the last one is
     resolved (K days have passed since it)
  3. baseline: every day, with a level placed below that day's close by the
     same distance as the median breakout margin. Same failure test.
     If breakouts fail about as often as the baseline, the pattern says nothing.

Usage: python breakout_check.py data.json [N] [K]
Data: Yahoo-style daily chart JSON (see README for how to get it).
Made by Kino (an AI), to be checked by a person. Not financial advice. Past only.
"""
import json
import sys


def load(path):
    with open(path, encoding="utf-8") as f:
        d = json.load(f)
    r = d["chart"]["result"][0]
    q = r["indicators"]["quote"][0]
    rows = []
    for t, h, c in zip(r["timestamp"], q["high"], q["close"]):
        if h is not None and c is not None:
            rows.append((t, h, c))
    return rows


def fails(rows, i, level, k):
    return any(rows[j][2] < level for j in range(i + 1, i + 1 + k))


def breakouts(rows, n, k):
    """List of (index, level) for every breakout day."""
    out = []
    for i in range(n, len(rows) - k):
        level = max(r[1] for r in rows[i - n:i])
        if rows[i][2] > level:
            out.append((i, level))
    return out


def rate(events, rows, k):
    f = sum(1 for i, lv in events if fails(rows, i, lv, k))
    return len(events), f


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return
    n = int(sys.argv[2]) if len(sys.argv) > 2 else 20
    k = int(sys.argv[3]) if len(sys.argv) > 3 else 5
    rows = load(sys.argv[1])
    allb = breakouts(rows, n, k)
    indep, last = [], -10**9
    for i, lv in allb:
        if i > last + k:
            indep.append((i, lv))
            last = i
    margins = sorted(rows[i][2] / lv - 1 for i, lv in allb)
    med = margins[len(margins) // 2] if margins else 0.0
    base = [(i, rows[i][2] / (1 + med)) for i in range(n, len(rows) - k)]

    print(f"Days: {len(rows)}  N={n}  K={k}  median breakout margin: {med:.2%}")
    for name, ev in (("All breakouts", allb), ("Independent breakouts", indep), ("Baseline (every day)", base)):
        t, f = rate(ev, rows, k)
        if t:
            print(f"{name}: {t}  Failed: {f}  Failure rate: {f / t:.1%}")
        else:
            print(f"{name}: 0")
    if len(indep) < 30:
        print("Warning: fewer than 30 independent breakouts, the rate is not reliable.")


if __name__ == "__main__":
    main()