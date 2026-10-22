"""Replay the event log into the current State. Pure: same log + same today = same State."""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass, field
from datetime import date, timedelta

from foundry import rules
from foundry.events import GRADED

MAIN_TYPES = (*GRADED, "forecast_new", "forecast_resolve")
REVIEWS_THAT_CLEAR_A_BACKLOG = 20  # after a break, 20 reviews count as "cards cleared"


@dataclass
class AreaState:
    id: str
    rating: float = rules.START_RATING
    items: int = 0
    passed: bool = False
    last_active: date | None = None
    history: list[tuple[date, float]] = field(default_factory=list)
    grades: list[float] = field(default_factory=list)


@dataclass
class Forecast:
    id: str
    question: str
    p: float
    resolve_by: date
    criteria: str
    created: date
    base_rate: float | None = None
    difficulty: float = rules.DEFAULT_FORECAST_DIFFICULTY
    outcome: int | None = None
    resolved: date | None = None


@dataclass
class Played:
    item: str
    kind: str
    date: date
    grade: float
    areas: list[str]
    rubric: dict[str, int]
    xp: int


@dataclass
class State:
    today: date
    xp: int = 0
    streak: int = 0
    best_streak: int = 0
    freezes: int = 0
    today_counts: bool = False
    today_main: bool = False
    areas: dict[str, AreaState] = field(default_factory=dict)
    cards: dict[str, rules.CardSchedule] = field(default_factory=dict)
    card_area: dict[str, str] = field(default_factory=dict)
    forecasts: dict[str, Forecast] = field(default_factory=dict)
    played: list[Played] = field(default_factory=list)
    xp_by_day: dict[date, int] = field(default_factory=dict)
    freeze_days: list[date] = field(default_factory=list)

    @property
    def level(self) -> int:
        return rules.level_for(self.xp)

    def due_cards(self, on: date | None = None) -> list[str]:
        on = on or self.today
        return sorted((c for c, s in self.cards.items() if s.due <= on),
                      key=lambda c: (self.cards[c].due, c))


def replay(events: list[dict], area_ids: list[str], today: date) -> State:
    state = State(today=today, areas={a: AreaState(a) for a in area_ids})
    by_day: dict[date, list[dict]] = defaultdict(list)
    for e in events:
        by_day[date.fromisoformat(e["date"])].append(e)
    if not by_day:
        return state

    day = min(by_day)
    while day <= today:
        streak_before = state.streak
        day_xp, card_xp, reviews, main_done = 0, 0, 0, False
        for e in by_day.get(day, []):
            kind = e["type"]
            if kind == "card_new":
                state.cards.setdefault(e["card"], rules.CardSchedule(due=day))
                state.card_area[e["card"]] = e["area"]
            elif kind == "card_review":
                card = state.cards.get(e["card"], rules.CardSchedule(due=day))
                state.cards[e["card"]] = rules.sm2(card, e["grade"], day)
                state.card_area[e["card"]] = e["area"]
                _touch(state, e["area"], day)
                gained = min(rules.CARD_XP, rules.CARD_XP_DAY_CAP - card_xp)
                card_xp += gained
                day_xp += gained
                reviews += 1
            elif kind in GRADED:
                day_xp += _graded(state, e, day)
                main_done = True
            elif kind == "forecast_new":
                state.forecasts[e["id"]] = Forecast(
                    e["id"], e["question"], e["p"], date.fromisoformat(e["resolve_by"]),
                    e["criteria"], day, e.get("base_rate"),
                    e.get("difficulty", rules.DEFAULT_FORECAST_DIFFICULTY))
                day_xp += rules.FORECAST_XP
                main_done = True
            elif kind == "forecast_resolve":
                day_xp += _resolve(state, e, day)
                main_done = True

        cleared = not state.due_cards(day) or reviews >= REVIEWS_THAT_CLEAR_A_BACKLOG
        counts = main_done and cleared
        if counts:
            state.streak += 1
            if state.streak % 7 == 0:
                state.freezes = min(2, state.freezes + 1)
        elif day < today:
            if state.freezes and state.streak:
                state.freezes -= 1
                state.freeze_days.append(day)
            else:
                state.streak = 0
        if day == today:
            state.today_counts, state.today_main = counts, main_done
        state.best_streak = max(state.best_streak, state.streak)

        gained = round(day_xp * rules.streak_multiplier(streak_before))
        if gained:
            state.xp_by_day[day] = gained
        state.xp += gained
        day += timedelta(days=1)
    return state


def _touch(state: State, area: str, day: date) -> None:
    if area in state.areas:
        state.areas[area].last_active = day


def _graded(state: State, e: dict, day: date) -> int:
    grade = rules.grade_from_rubric(e["rubric"])
    for i, area_id in enumerate(e["areas"]):
        area = state.areas[area_id]
        weight = 1.0 if i == 0 else rules.SECONDARY_AREA_WEIGHT
        area.rating = rules.elo_update(area.rating, e["difficulty"], grade, area.items, weight)
        area.items += 1
        area.passed = area.passed or grade >= 0.5
        area.grades.append(grade)
        area.history.append((day, area.rating))
        area.last_active = day
    xp = rules.item_xp(e["type"], grade)
    state.played.append(Played(e["item"], e["type"], day, grade, list(e["areas"]),
                               dict(e["rubric"]), xp))
    return xp


def _resolve(state: State, e: dict, day: date) -> int:
    fc = state.forecasts.get(e["id"])
    if fc is None or fc.outcome is not None:
        return 0
    fc.outcome, fc.resolved = e["outcome"], day
    you = rules.brier(fc.p, fc.outcome)
    base = None if fc.base_rate is None else rules.brier(fc.base_rate, fc.outcome)

    area = state.areas.get("forecasting")
    if area is not None:
        area.rating = rules.elo_update(area.rating, fc.difficulty, 1 - you, area.items,
                                       rules.FORECAST_K_WEIGHT)
        area.items += 1
        area.history.append((day, area.rating))
        area.last_active = day
    return rules.FORECAST_XP + rules.forecast_bonus(you, base)
