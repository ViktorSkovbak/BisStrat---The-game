---
name: train
description: The Foundry's daily training session (30-45 min). Clears due concept cards, runs one adaptive main item (lab, drill, repair, sparring or boss fight), checks forecasts, then scores, journals and updates the machine. Use when Viktor says /train, "train", "today's session" or "daily practice".
model: opus
---

# /train: the daily loop

Timebox 30-45 minutes. Be brisk: short prompts, short feedback, no preamble. Everything is graded on `curriculum/rubrics.md`.

## 1. Open (one message)
Run `uv run foundry status --json`. Show three lines: level and XP, streak (and whether a freeze is banked), due cards and today's pick with its reason. Then start the cards at once.

## 2. Cards (5-10 min)
- `uv run foundry due` lists due cards with their file. Take them oldest first, max 20.
- For each: show only the `## Prompt`. Viktor answers in his own words. Grade 0-5 against `## Model answer` and `## Grading notes` (rubric D). Feedback in one or two lines; show the model answer when the grade is below 4.
- Record each: `uv run foundry record card_review '{"card": "<id>", "area": "<area>", "grade": <0-5>}'`.
- **One new card a day:** take the next card from the most recent lab's `cards:` list that is not in the deck yet. Record `card_new`, then review it the same way.
- If today's pick has `extra_cards: 2`, have the `writer` agent draft two cards for that area (or write them yourself if quick), review them, add them with `card_new`.

## 3. Main item (20-30 min), from `next` in the status
| kind | Do |
|---|---|
| `lab` | Follow `.claude/skills/lab/SKILL.md` for that item. |
| `drill` | Follow `.claude/skills/drill/SKILL.md` for that item. |
| `repetition` | Write one T1 or T2 problem in that area at the target difficulty (rubric B tiers in `docs/DECISIONS.md`), tied to Viktor's own businesses where possible. Grade on rubric B. Record as `lab` with item `R-<area>-<YYYYMMDD>`. |
| `spar` / `boss` | Weekend items. Ask whether Viktor has the long session now (60-90 min). Yes: follow `/spar` or `/boss`. No: do the next lab or drill instead. |
| `new` | Spawn the `writer` agent for the next item in that area at the target difficulty. Review its draft yourself (facts, difficulty, rubric fit) before running it. |
Viktor may override the pick; respect it.

## 4. Forecasts (2 min)
- Any forecast due (`uv run foundry forecasts` shows DUE): resolve it as in `/forecast`.
- If none was made in 7 days and time allows, run `/forecast` (new).

## 5. Close
1. `uv run foundry export`, then republish the artifact (CLAUDE.md hard rule 3).
2. Append to `journal/YYYY-MM-DD.md`: each item, Viktor's answer verbatim, scores, the one change that would have raised the grade most.
3. Vault: one raw note per concept learned today (CLAUDE.md hard rule 4).
4. `git add -A && git commit -m "train: YYYY-MM-DD"`.
5. Final message (max 6 lines): XP gained, level, rating changes, streak, machine changes, and **one thing to sharpen tomorrow**. Link the artifact.
