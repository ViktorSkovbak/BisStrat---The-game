"""state.json for the web artifact: everything the machine page needs, nothing it must compute."""

from __future__ import annotations

from datetime import datetime

from foundry import rules
from foundry.content import Area, Item
from foundry.engine import State
from foundry.machine import all_parts
from foundry.pick import Pick


def calibration(state: State) -> dict:
    resolved = [f for f in state.forecasts.values() if f.outcome is not None]
    bins = []
    for lo in range(0, 100, 10):
        inside = [f for f in resolved
                  if lo / 100 <= f.p < (lo + 10) / 100 or (lo == 90 and f.p == 1)]
        if inside:
            bins.append({"bin": lo, "n": len(inside),
                         "mean_p": round(sum(f.p for f in inside) / len(inside), 3),
                         "observed": round(sum(f.outcome for f in inside) / len(inside), 3)})
    briers = [rules.brier(f.p, f.outcome) for f in resolved]
    return {
        "resolved": len(resolved),
        "open": sum(f.outcome is None for f in state.forecasts.values()),
        "brier_mean": round(sum(briers) / len(briers), 4) if briers else None,
        "bins": bins,
    }


def labs(state: State, items: dict[str, Item]) -> list[dict]:
    best = {}
    for p in state.played:
        best[p.item] = max(best.get(p.item, 0.0), p.grade)
    return [{"id": i.id, "title": i.title, "areas": list(i.areas), "sim": i.sim,
             "difficulty": i.difficulty, "played": i.id in best,
             "grade": round(best[i.id], 2) if i.id in best else None}
            for i in sorted(items.values(), key=lambda i: i.id) if i.kind == "lab"]


def build(state: State, tracks: list[dict], areas: dict[str, Area], pick: Pick,
          items: dict[str, Item]) -> dict:
    parts = all_parts(state)
    lab_list = labs(state, items)
    # The lab that builds each area's part: its first lab whose primary area it is.
    builds = {}
    for lab in lab_list:
        builds.setdefault(lab["areas"][0], lab["id"])
    drills = {i.areas[0]: i.id for i in sorted(items.values(), key=lambda i: i.id, reverse=True)
              if i.kind == "drill"}
    level = state.level
    floor, ceiling = rules.level_threshold(level), rules.level_threshold(level + 1)
    return {
        "generated": datetime.now().isoformat(timespec="seconds"),
        "today": state.today.isoformat(),
        "player": {"xp": state.xp, "level": level, "title": rules.title_for(level),
                   "level_floor": floor, "next_level_at": ceiling},
        "streak": {"days": state.streak, "best": state.best_streak, "freezes": state.freezes,
                   "today_done": state.today_counts},
        "cards": {"total": len(state.cards), "due": len(state.due_cards()),
                  "mature": sum(c.interval >= rules.MATURE_INTERVAL
                                for c in state.cards.values())},
        "tracks": tracks,
        "areas": [
            {"id": a.id, "name": a.name, "track": a.track, "phase": a.phase, "part": a.part,
             "part_name": a.part_name, "plot": list(a.plot),
             "rating": round(state.areas[a.id].rating), "items": state.areas[a.id].items,
             "level": parts[a.id].level, "jammed": parts[a.id].jammed,
             "reasons": list(parts[a.id].reasons), "mature_cards": parts[a.id].mature_cards,
             "build_with": builds.get(a.id) or drills.get(a.id),
             "history": [[d.isoformat(), round(r)] for d, r in state.areas[a.id].history]}
            for a in areas.values()
        ],
        "labs": lab_list,
        "forecasts": calibration(state),
        "recent": [{"date": p.date.isoformat(), "kind": p.kind, "item": p.item,
                    "grade": round(p.grade, 2), "xp": p.xp, "areas": p.areas}
                   for p in state.played[-10:]][::-1],
        "next": pick.to_dict(),
    }
