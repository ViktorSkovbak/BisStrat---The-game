---
name: boss
description: The Foundry's monthly boss fight - a full strategy memo on a real company (or Viktor's own new company), graded on an 8-dimension rubric that names exactly what would make it stronger. Use when Viktor says /boss, "boss fight", "strategy memo" or "monthly memo".
argument-hint: "[company]"
model: opus
---

# /boss [company]

Load the `mentor` skill (examiner mode).

## Set the fight
1. Viktor picks the company, or chooses from three you propose: a public company at a real turning point today, a hardware or deep-tech scale-up, or his own new company (use the Crucible's current finalists and STATUS).
2. The task: a strategy memo of at most 1,500 words with
   - diagnosis (the crux), guiding policy and coherent actions (Rumelt's kernel);
   - the source of durable advantage, or why there is none yet (Helmer: benefit + barrier);
   - the numbers that decide it (unit economics, market size, capital needed);
   - risks, one-way doors and kill criteria with dates;
   - a first paragraph a busy investor can act on.
3. He may research and write over several days. Save the task in `journal/YYYY-MM-DD.md` so a later session can pick it up.

## Grade
1. Score rubric A and C (8 dimensions) in `curriculum/rubrics.md`.
2. For the two weakest dimensions, **rewrite one paragraph of his memo** to show the 1800-level version. Keep it short; it is an example, not a replacement.
3. List the three changes that would raise the grade most, in order.
4. Record: `uv run foundry record boss '{"item": "B-<company>-YYYYMM", "areas": ["strategy", ...], "difficulty": <1500-2000>, "rubric": {"diagnosis": n, "options": n, "mechanism": n, "risk": n, "commitment": n, "coherence": n, "advantage": n, "communication": n}, "journal": "..."}'`. Boss fights always include `strategy`, which powers the core reactor.
5. Close as in `/train` step 5. Save the memo itself to `journal/boss/<YYYY-MM>-<company>.md`.
