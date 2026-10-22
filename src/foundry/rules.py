"""Pure scoring rules. Change numbers here; replaying the log applies them to all history."""

from __future__ import annotations

from dataclasses import dataclass, replace
from datetime import date, timedelta

# --- XP ------------------------------------------------------------------------
# (base, span): XP = base + span * grade, grade in [0, 1].
ITEM_XP = {"lab": (40, 60), "drill": (50, 100), "spar": (100, 150), "boss": (200, 300)}
CARD_XP = 5
CARD_XP_DAY_CAP = 50
FORECAST_XP = 15
FORECAST_BONUS_CAP = 25

TITLES = ["Apprentice", "Operator", "Manager", "Strategist", "Allocator", "Architect"]


def item_xp(kind: str, grade: float) -> int:
    base, span = ITEM_XP[kind]
    return round(base + span * grade)


def forecast_bonus(brier_you: float, brier_base: float | None) -> int:
    """Bonus for beating the base rate; zero when no base rate was given."""
    if brier_base is None:
        return 0
    return min(FORECAST_BONUS_CAP, round(50 * max(0.0, brier_base - brier_you)))


def streak_multiplier(streak_days: int) -> float:
    """+10% per full streak week, capped at +50%."""
    return 1 + min(0.5, 0.1 * (streak_days // 7))


def level_threshold(level: int) -> int:
    """Total XP needed to reach `level` (level 1 starts at 0)."""
    return round(150 * (level - 1) ** 1.6)


def level_for(xp: int) -> int:
    level = 1
    while level_threshold(level + 1) <= xp:
        level += 1
    return level


def title_for(level: int) -> str:
    return TITLES[min((level - 1) // 5, len(TITLES) - 1)]


# --- Grades and Elo ------------------------------------------------------------
START_RATING = 1200.0
SECONDARY_AREA_WEIGHT = 0.5


def grade_from_rubric(rubric: dict[str, int]) -> float:
    """Each rubric dimension is scored 0-4; the grade is the share of the maximum."""
    return sum(rubric.values()) / (4 * len(rubric))


def expected(rating: float, difficulty: float) -> float:
    return 1 / (1 + 10 ** ((difficulty - rating) / 400))


def elo_k(items_done: int) -> float:
    """Provisional ratings move faster for the first 10 items in an area."""
    return 40.0 if items_done < 10 else 24.0


def elo_update(rating: float, difficulty: float, grade: float, items_done: int,
               weight: float = 1.0) -> float:
    return rating + elo_k(items_done) * weight * (grade - expected(rating, difficulty))


# --- Spaced repetition (SM-2) --------------------------------------------------
MATURE_INTERVAL = 21  # days; a card this far apart counts as owned


@dataclass(frozen=True)
class CardSchedule:
    due: date
    reps: int = 0
    interval: int = 0
    ease: float = 2.5
    lapses: int = 0


def sm2(card: CardSchedule, quality: int, today: date) -> CardSchedule:
    """SM-2: quality 0-5. Below 3 the card restarts tomorrow and gets harder to space out."""
    ease = max(1.3, card.ease + 0.1 - (5 - quality) * (0.08 + (5 - quality) * 0.02))
    if quality < 3:
        return replace(card, reps=0, interval=1, ease=ease, lapses=card.lapses + 1,
                       due=today + timedelta(days=1))
    reps = card.reps + 1
    if reps == 1:
        interval = 1
    elif reps == 2:
        interval = 6
    else:
        interval = round(card.interval * ease)
    return replace(card, reps=reps, interval=interval, ease=ease,
                   due=today + timedelta(days=interval))


# --- Forecasting ---------------------------------------------------------------
DEFAULT_FORECAST_DIFFICULTY = 1300.0
FORECAST_K_WEIGHT = 0.5  # one forecast is noisy evidence of skill


def brier(p: float, outcome: int) -> float:
    return (p - outcome) ** 2
