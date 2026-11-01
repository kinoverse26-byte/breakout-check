# Notes
- Idea: breakout failure rate (N-day high breakout closes back below the level within K days), compared with a baseline.
- Data: Yahoo chart API BTC-USD daily, 730 days. The file is NOT in this folder (not published); it is kept in my lab.
- Done after review: baseline added, overlapping breakouts counted once (new one only after K days), data file moved out, README rewritten.
- Result (N=20, K=5): all 38 breakouts, 24 failed (63.2%); independent 21, 13 failed (61.9%); baseline 705 days, 428 failed (60.7%). Breakouts fail about as often as ordinary days.
- Left: a person checks the code and README; maybe other N/K and other assets; more data to get past 30 independent breakouts.
