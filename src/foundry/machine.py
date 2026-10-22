"""Machine-part state per area: blueprint, built, upgraded (levels 2-4) or jammed."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date, timedelta

from foundry import rules
from foundry.engine import State

# (level, minimum rating, minimum mature cards in the area)
UPGRADES = ((2, 1400, 3), (3, 1600, 6), (4, 1800, 10))
JAM_RATING_DROP = 50
JAM_WINDOW_DAYS = 14
JAM_OVERDUE_CARDS = 3
JAM_IDLE_DAYS = 21


@dataclass(frozen=True)
class Part:
    area: str
    level: int  # 0 = blueprint
    jammed: bool
    reasons: tuple[str, ...]
    mature_cards: int
    overdue_cards: int


def part_state(state: State, area_id: str) -> Part:
    area = state.areas[area_id]
    today = state.today
    cards = [c for c, a in state.card_area.items() if a == area_id]
    mature = sum(state.cards[c].interval >= rules.MATURE_INTERVAL for c in cards)
    overdue = sum(state.cards[c].due < today for c in cards)

    level = 1 if area.passed else 0
    if level:
        for lvl, min_rating, min_mature in UPGRADES:
            if area.rating >= min_rating and mature >= min_mature:
                level = lvl

    reasons: list[str] = []
    if level:
        window_start = today - timedelta(days=JAM_WINDOW_DAYS)
        before = [r for d, r in area.history if d <= window_start]
        baseline = before[-1] if before else rules.START_RATING
        if baseline - area.rating >= JAM_RATING_DROP:
            reasons.append(f"rating down {baseline - area.rating:.0f} in {JAM_WINDOW_DAYS} days")
        if overdue >= JAM_OVERDUE_CARDS:
            reasons.append(f"{overdue} overdue cards")
        if area.last_active and (today - area.last_active).days >= JAM_IDLE_DAYS:
            reasons.append(f"idle {(today - area.last_active).days} days")
    return Part(area_id, level, bool(reasons), tuple(reasons), mature, overdue)


def all_parts(state: State) -> dict[str, Part]:
    return {a: part_state(state, a) for a in state.areas}


def days_since(day: date | None, today: date) -> int | None:
    return None if day is None else (today - day).days
