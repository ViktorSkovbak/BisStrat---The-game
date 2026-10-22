---
name: spar
description: The Foundry's weekly sparring session - a role-play where the AI plays the other side (board meeting, investor pitch, negotiation, competitor war-game, hard conversation with a key employee), graded afterwards. Use when Viktor says /spar, "spar", "role-play", "pitch practice" or "war-game".
argument-hint: "[board | investor | negotiation | wargame | conversation]"
model: opus
---

# /spar [type]

Load the `mentor` skill and its `references/sparring.md`; follow its role cards and grading rules.

1. **Choose:** the type given, else the one Viktor has done least, aimed at his weakest active area (`uv run foundry status`). Build it on his real situation: the new company and its Crucible finalists, the wind-down of SA and Saverus, fundraising, the first engineering hires, the co-founder search.
2. **Set up (one message):** who you play, what they want, what they know that Viktor doesn't (keep hidden information hidden), Viktor's objective, the time or turn limit, and the difficulty (1400-1900).
3. **Play in character.** Push as a real counterpart would; concede only what a real one would concede. No coaching during play. Viktor can say "time out" for one question out of role.
4. **Debrief:** step out of role. Grade rubric A, plus the type-specific dimensions in `sparring.md`. Name the moment the session turned and what he should have said there.
5. **Record:** `uv run foundry record spar '{"item": "S-<type>-YYYYMMDD", "areas": [<main area>, ...], "difficulty": <D>, "rubric": {...}, "journal": "journal/YYYY-MM-DD.md"}'`.
6. Close as in `/train` step 5. Keep the full transcript's key exchanges in the journal.
