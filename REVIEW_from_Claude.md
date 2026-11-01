# Review of breakout_check (2026-11-01) - before it is published under the owner's name

Good work: clean, small, honest README, limits named. Three things to do next:

1. A baseline. 63% means little alone. Run the same "falls back below the level within K days" check from RANDOM days
   (or from every day, using its own prior N-day high as the level) and print both rates side by side. The tool is only
   interesting if breakouts differ from that baseline.
2. Do not publish the Yahoo data file (republishing their data may break their terms). Remove data/ from what gets
   published; explain in the README how anyone can download the same public file themselves.
3. Overlapping signals: a breakout on day i and again on day i+1 are counted as two events. Count only the first breakout
   after a quiet period (no new breakout for K days), or report both counts.

Publishing: the owner is creating a GitHub account for you. Publishing will be a request card he approves.
