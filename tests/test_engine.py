import json
from datetime import date, timedelta

import pytest

from foundry import events
from foundry.content import load_items, load_map
from foundry.engine import replay
from foundry.machine import part_state
from foundry.pick import next_pick

_, AREAS = load_map()
AREA_IDS = list(AREAS)
D0 = date(2026, 10, 19)  # a Monday


def ev(day: date, type_: str, **fields) -> dict:
    return {"v": 1, "date": day.isoformat(), "ts": f"{day}T12:00:{len(fields):02d}",
            "type": type_, **fields}


def lab(day: date, grade4: int = 3, item: str = "L01", area: str = "operations",
        difficulty: int = 1200) -> dict:
    return ev(day, "lab", item=item, areas=[area], difficulty=difficulty,
              rubric={"mechanism": grade4, "application": grade4})


def card(day: date, cid: str, grade: int, new: bool = False) -> list[dict]:
    out = [ev(day, "card_new", card=cid, area="operations")] if new else []
    return out + [ev(day, "card_review", card=cid, area="operations", grade=grade)]


def test_empty_log_is_a_fresh_player():
    s = replay([], AREA_IDS, D0)
    assert (s.xp, s.streak, s.level) == (0, 0, 1)
    assert all(a.rating == 1200 for a in s.areas.values())


def test_a_day_counts_only_with_main_item_and_cleared_cards():
    log = [*card(D0, "c1", 4, new=True), lab(D0)]
    s = replay(log, AREA_IDS, D0)
    assert s.today_counts and s.streak == 1
    # card due tomorrow; a lab alone does not count while the card waits
    s2 = replay([*log, lab(D0 + timedelta(1), item="L02")], AREA_IDS, D0 + timedelta(1))
    assert not s2.today_counts and s2.streak == 1


def test_missed_day_breaks_streak_unless_a_freeze_is_banked():
    log = []
    for i in range(7):
        log += [lab(D0 + timedelta(i), item=f"X{i}")]
    s = replay(log, AREA_IDS, D0 + timedelta(6))
    assert s.streak == 7 and s.freezes == 1
    # day 8 missed, day 9 played: the freeze carries the streak
    log.append(lab(D0 + timedelta(8), item="X8"))
    s = replay(log, AREA_IDS, D0 + timedelta(8))
    assert s.streak == 8 and s.freezes == 0 and s.freeze_days == [D0 + timedelta(7)]
    # two missed days with no freeze: back to zero
    s = replay(log, AREA_IDS, D0 + timedelta(11))
    assert s.streak == 0


def test_today_unplayed_does_not_break_the_streak_yet():
    s = replay([lab(D0)], AREA_IDS, D0 + timedelta(1))
    assert s.streak == 1 and not s.today_counts


def test_card_xp_is_capped_per_day():
    log = [lab(D0)]
    for i in range(15):
        log += card(D0, f"c{i}", 5, new=True)
    s = replay(log, AREA_IDS, D0)
    assert s.xp == 50 + round(40 + 60 * 0.75)


def test_graded_items_move_ratings_and_build_the_part():
    s = replay([lab(D0, grade4=4)], AREA_IDS, D0)
    assert s.areas["operations"].rating == pytest.approx(1220)
    assert part_state(s, "operations").level == 1
    assert part_state(s, "org").level == 0


def test_secondary_areas_move_at_half_weight():
    e = ev(D0, "drill", item="D01", areas=["strategy", "capital"], difficulty=1200,
           rubric={"a": 4})
    s = replay([e], AREA_IDS, D0)
    assert s.areas["strategy"].rating == pytest.approx(1220)
    assert s.areas["capital"].rating == pytest.approx(1210)
    assert part_state(s, "strategy").level == 1
    assert part_state(s, "capital").level == 0


def test_part_jams_when_idle_and_when_cards_pile_up():
    s = replay([lab(D0)], AREA_IDS, D0 + timedelta(21))
    p = part_state(s, "operations")
    assert p.jammed and "idle 21 days" in p.reasons
    log = [lab(D0)]
    for i in range(3):
        log += card(D0, f"c{i}", 4, new=True)
    p = part_state(replay(log, AREA_IDS, D0 + timedelta(3)), "operations")
    assert p.jammed and "3 overdue cards" in p.reasons


def test_rating_drop_jams_the_part():
    log = [lab(D0, grade4=4)] + [lab(D0 + timedelta(15), grade4=0, item=f"Y{i}") for i in range(3)]
    p = part_state(replay(log, AREA_IDS, D0 + timedelta(15)), "operations")
    assert p.jammed and p.reasons[0].startswith("rating down")


def test_forecast_resolution_scores_brier_and_moves_forecasting_rating():
    log = [ev(D0, "forecast_new", id="F1", question="q", p=0.7, base_rate=0.5,
              resolve_by="2026-11-01", criteria="c"),
           ev(D0 + timedelta(1), "forecast_resolve", id="F1", outcome=1)]
    s = replay(log, AREA_IDS, D0 + timedelta(1))
    assert s.forecasts["F1"].outcome == 1
    assert s.areas["forecasting"].rating > 1200
    assert s.xp == 15 + 15 + 8  # bonus: 50 * (0.25 - 0.09) = 8


def test_replay_is_deterministic():
    log = [*card(D0, "c1", 4, new=True), lab(D0), lab(D0 + timedelta(1), item="L02")]
    a = replay(log, AREA_IDS, D0 + timedelta(3))
    b = replay(log, AREA_IDS, D0 + timedelta(3))
    assert a == b


def test_pick_starts_with_the_first_lab_then_alternates_to_a_drill():
    items = load_items()
    s = replay([], AREA_IDS, D0)
    first = next_pick(s, AREAS, items)
    assert first.kind == "lab" and first.item == "L01"
    s = replay([lab(D0)], AREA_IDS, D0 + timedelta(1))
    assert next_pick(s, AREAS, items).kind == "drill"


def test_pick_repairs_jammed_parts_first():
    s = replay([lab(D0)], AREA_IDS, D0 + timedelta(22))  # Tuesday, idle 22 days
    pick = next_pick(s, AREAS, load_items())
    assert pick.kind == "repetition" and pick.area == "operations" and pick.extra_cards == 2


def test_pick_calls_for_sparring_on_weekends():
    saturday = D0 + timedelta(5)
    s = replay([lab(D0)], AREA_IDS, saturday)
    assert next_pick(s, AREAS, load_items()).kind == "spar"


def test_append_validates_and_void_removes(tmp_path):
    log = tmp_path / "events.jsonl"
    stored = events.append(log, {"type": "lab", "item": "L01", "areas": ["operations"],
                                 "difficulty": 1200, "rubric": {"a": 3}}, set(AREA_IDS), D0)
    with pytest.raises(events.EventError, match="0-4"):
        events.append(log, {"type": "lab", "item": "L01", "areas": ["operations"],
                            "difficulty": 1200, "rubric": {"a": 5}}, set(AREA_IDS), D0)
    with pytest.raises(events.EventError, match="unknown areas"):
        events.append(log, {"type": "card_new", "card": "x", "area": "nope"}, set(AREA_IDS), D0)
    assert len(events.load(log)) == 1
    events.append(log, {"type": "void", "target_ts": stored["ts"], "reason": "test"},
                  set(AREA_IDS), D0)
    assert [e["type"] for e in events.load(log)] == ["void"]
    assert json.loads(log.read_text(encoding="utf-8").splitlines()[0])["item"] == "L01"
