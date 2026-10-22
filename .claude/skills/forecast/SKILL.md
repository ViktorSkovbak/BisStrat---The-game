---
name: forecast
description: Make or resolve Foundry business forecasts - a real question with a resolution date, Viktor's probability and a base rate, scored with Brier and plotted on his calibration curve. Use when Viktor says /forecast, "forecast", "prediction", or when a forecast is due.
argument-hint: "[new | resolve]"
model: opus
---

# /forecast [new | resolve]

Default: resolve anything due first (`uv run foundry forecasts`), then offer a new one.

## New (1-2 a week)
1. Search the web (WebSearch) for live situations and propose **three** questions that:
   - resolve in 2-12 weeks, on a date, with criteria a source will settle unambiguously;
   - are genuinely uncertain today (check they have not already resolved);
   - sit close to Viktor's path: deep-tech and hardware funding rounds, big-company strategic moves, chip, battery and robotics markets, EU grant calls, the Spanish property market.
2. Viktor picks one. **Outside view first:** ask him for the base rate (how often do cases like this resolve yes?), then his own probability with one line of reasoning.
3. Record: `uv run foundry record forecast_new '{"id": "F-YYYYMMDD-n", "question": "...", "p": 0.xx, "base_rate": 0.xx, "resolve_by": "YYYY-MM-DD", "criteria": "...", "difficulty": 1300}'`. Use difficulty 1400-1600 for questions where the base rate is hard to find.

## Resolve
1. For each due forecast, look up the outcome (WebSearch) and show the source. Viktor confirms.
2. If it cannot be settled yet, say so and leave it open; never guess an outcome.
3. Record: `uv run foundry record forecast_resolve '{"id": "...", "outcome": 0|1}'`.
4. Report the Brier score (0 is perfect, 0.25 is a coin flip) and whether he beat his base rate. Every five resolved forecasts, comment on the calibration curve: is he overconfident at the extremes?
