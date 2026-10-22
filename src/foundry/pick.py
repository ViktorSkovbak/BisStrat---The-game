"""Adaptive pick of today's main item. The skills follow this; Viktor can always override."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from statistics import median

from foundry.content import Area, Item
from foundry.engine import State
from foundry.machine import all_parts

STRETCH = 100  # strong areas: aim above the rating (expected grade ~0.36)
EASE_OFF = 50  # weak areas: aim below the rating, and add cards
SPAR_EVERY_DAYS = 7
BOSS_EVERY_DAYS = 28
BOSS_AFTER_DAYS_PLAYED = 21


@dataclass(frozen=True)
class Pick:
    kind: str  # lab, drill, spar, boss, repetition, new
    item: str | None
    area: str
    target_difficulty: int
    reason: str
    extra_cards: int = 0

    def to_dict(self) -> dict:
        return asdict(self)


def _days_since_kind(state: State, kind: str) -> int | None:
    days = [state.today - p.date for p in state.played if p.kind == kind]
    return min(days).days if days else None


def next_pick(state: State, areas: dict[str, Area], items: dict[str, Item]) -> Pick:
    parts = all_parts(state)
    active = [a for a in state.areas.values() if a.items]
    mid = median(a.rating for a in active) if active else None

    def target(area_id: str) -> int:
        r = state.areas[area_id].rating
        strong = mid is not None and r > mid
        return round(r + STRETCH if strong else r - EASE_OFF)

    # 1. Weekly sparring and monthly boss fight, on weekends.
    first_day = min((p.date for p in state.played), default=state.today)
    if state.today.weekday() >= 5:
        boss_gap = _days_since_kind(state, "boss")
        if ((state.today - first_day).days >= BOSS_AFTER_DAYS_PLAYED
                and (boss_gap is None or boss_gap >= BOSS_EVERY_DAYS)):
            return Pick("boss", None, "strategy", target("strategy"),
                        "monthly boss fight is due")
        spar_gap = _days_since_kind(state, "spar")
        if state.played and (spar_gap is None or spar_gap >= SPAR_EVERY_DAYS):
            weakest = min(active, key=lambda a: a.rating).id if active else "strategy"
            return Pick("spar", None, weakest, target(weakest),
                        "weekly sparring is due; aimed at your weakest active area")

    # 2. Jammed parts first: repair before building.
    jammed = [p for p in parts.values() if p.jammed]
    if jammed:
        worst = min(jammed, key=lambda p: state.areas[p.area].rating)
        return Pick("repetition", None, worst.area, round(state.areas[worst.area].rating
                    - EASE_OFF), f"{areas[worst.area].part_name} is jammed: "
                    + "; ".join(worst.reasons), extra_cards=2)

    # 3. Weak areas: two grades below 0.5 in a row.
    weak = [a for a in active if len(a.grades) >= 2 and max(a.grades[-2:]) < 0.5]
    if weak:
        w = min(weak, key=lambda a: a.rating)
        return Pick("repetition", None, w.id, round(w.rating - EASE_OFF),
                    "two weak grades in a row; ease off and add cards", extra_cards=2)

    # 4. New content in curriculum order, alternating labs and drills.
    played = {p.item for p in state.played}
    unplayed = sorted((i for i in items.values()
                       if i.kind in ("lab", "drill") and i.id not in played),
                      key=lambda i: (i.phase, areas[i.areas[0]].phase, i.id))
    last_main = next((p.kind for p in reversed(state.played) if p.kind in ("lab", "drill")),
                     None)
    prefer = "drill" if last_main == "lab" else "lab"
    for kind in (prefer, "lab" if prefer == "drill" else "drill"):
        pick = next((i for i in unplayed if i.kind == kind), None)
        if pick:
            return Pick(kind, pick.id, pick.areas[0], pick.difficulty,
                        f"next {kind} in curriculum order")

    # 5. Nothing written yet: ask the writer for a new item in the weakest early area.
    order = sorted(areas.values(), key=lambda a: (a.phase, state.areas[a.id].rating))
    a = order[0]
    return Pick("new", None, a.id, target(a.id),
                f"no unplayed content; write a new {prefer} for {a.name}")
