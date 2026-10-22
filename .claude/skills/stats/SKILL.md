---
name: stats
description: Show Viktor's Foundry progress (level, XP, streak, ratings per area, calibration, jammed parts) and republish the machine artifact. Includes a weekly review on request. Use when Viktor says /stats, "stats", "progress", "how am I doing" or "weekly review".
argument-hint: "[week]"
---

# /stats [week]

1. `uv run foundry status`: show it as a compact table (areas with items only).
2. `uv run foundry export`, then republish the artifact (CLAUDE.md hard rule 3) and give the link.
3. **Weekly review** (argument `week`, or on the weekend):
   - rating change per active area over 7 days (from `web/state.json` histories);
   - the weakest area and the most common lost rubric dimension in the journal this week;
   - calibration so far;
   - one focus for next week, stated as a behaviour ("state a confidence in every drill").
   - Remind Viktor to run `/ingest` in the vault for this week's Foundry notes.
