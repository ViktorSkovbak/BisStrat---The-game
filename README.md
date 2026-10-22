# The Foundry

A daily training game for strategic and business judgement. Each skill you master adds a part to an isometric machine that represents your company. Weak areas show as dim or jammed parts.

**Your machine:** https://claude.ai/artifact/6288nZm1W7L35nZ6M3sp7V (private)

## How to play
Start a Claude Code session in this folder, then:

| Command | When | Time |
|---|---|---|
| `/train` | Every day. Cards, one main item, forecasts, score. | 30-45 min |
| `/lab [id]` | A business law: theory, simulation, evidence, graded question | 25 min |
| `/drill [id]` | A real company at a turning point; decide, then the reveal | 25 min |
| `/forecast` | 1-2 a week; resolve when due | 5 min |
| `/spar [type]` | Weekly role-play: board, investor, negotiation, war-game, hard conversation | 60 min |
| `/boss [company]` | Monthly strategy memo, fully graded | 2-4 h over days |
| `/stats [week]` | Progress, weekly review, republish the machine | 5 min |

`/train` picks the main item for you. It repairs jammed parts first, then weak areas, then the next new lab or drill. On weekends it calls for sparring, and roughly monthly for a boss fight.

## Rules in one screen
- **XP:** cards 5 (max 50/day), lab 40-100, drill 50-150, forecast 15 + 15 + bonus for beating the base rate, spar 100-250, boss 200-500. Streak weeks add +10% each, up to +50%.
- **Levels:** level n at 150·(n−1)^1.6 XP. Titles change every 5 levels: Apprentice, Operator, Manager, Strategist, Allocator, Architect.
- **Streak:** a day counts when due cards are cleared and one main item is done. One freeze is earned every 7 days, with at most 2 banked.
- **Rating:** Elo per area, starting at 1200. 1500 is a solid top-MBA answer, 1800 a strong strategy partner, 2000+ investor-grade.
- **Grades:** rubric scores 0-4 per dimension (`curriculum/rubrics.md`). Reasoning is graded, never outcomes.
- **Machine:** a part is built when you first pass its area. It upgrades at ratings of 1400/1600/1800 combined with 3/6/10 mature cards. It jams after a 50-point rating drop in 14 days, at 3 overdue cards, or after 21 idle days.

## Files
- `curriculum/`: `map.toml` (areas, phases, machine parts), `rubrics.md`, `labs/`, `drills/`, `cards/`.
- `log/events.jsonl`: every graded event, append-only. All scores are replayed from it.
- `journal/`: your answers and the feedback, by day.
- `web/`: the machine page, lab simulations and `state.json`.
- `src/foundry/`: the scoring CLI (`uv run foundry --help`).

## Develop
```bash
uv run pytest
```
