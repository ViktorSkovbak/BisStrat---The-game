from datetime import date

from foundry import rules


def test_levels_climb_and_titles_change_every_five():
    assert rules.level_for(0) == 1
    assert rules.level_for(rules.level_threshold(2)) == 2
    assert rules.level_for(rules.level_threshold(10) - 1) == 9
    assert rules.title_for(1) == "Apprentice"
    assert rules.title_for(6) == "Operator"
    assert rules.title_for(99) == "Architect"


def test_item_xp_scales_with_grade():
    assert rules.item_xp("lab", 0) == 40
    assert rules.item_xp("lab", 1) == 100
    assert rules.item_xp("boss", 0.5) == 350


def test_streak_multiplier_caps_at_half():
    assert rules.streak_multiplier(6) == 1
    assert rules.streak_multiplier(7) == 1.1
    assert rules.streak_multiplier(70) == 1.5


def test_elo_rises_on_beating_expectation_and_falls_otherwise():
    assert rules.elo_update(1200, 1200, 1.0, 0) == 1220  # K 40 * (1 - 0.5)
    assert rules.elo_update(1200, 1200, 0.0, 20) == 1188  # K 24 * (0 - 0.5)
    assert rules.expected(1500, 1500) == 0.5


def test_rubric_grade_is_share_of_maximum():
    assert rules.grade_from_rubric({"a": 4, "b": 2}) == 0.75


def test_sm2_spaces_good_answers_and_resets_bad_ones():
    d = date(2026, 10, 22)
    c = rules.CardSchedule(due=d)
    c = rules.sm2(c, 5, d)
    assert (c.interval, c.due) == (1, date(2026, 10, 23))
    c = rules.sm2(c, 4, c.due)
    assert c.interval == 6
    c = rules.sm2(c, 4, c.due)
    assert c.interval == round(6 * c.ease)
    failed = rules.sm2(c, 1, c.due)
    assert failed.interval == 1 and failed.reps == 0 and failed.lapses == 1
    assert failed.ease < c.ease


def test_brier_and_forecast_bonus():
    assert abs(rules.brier(0.8, 1) - 0.04) < 1e-9
    assert rules.forecast_bonus(0.04, None) == 0
    assert rules.forecast_bonus(0.04, 0.25) == 10  # 50 * 0.21 = 10.5 -> 10
    assert rules.forecast_bonus(0.0, 1.0) == rules.FORECAST_BONUS_CAP
