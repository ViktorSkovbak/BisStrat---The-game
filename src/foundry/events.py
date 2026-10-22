"""The event log: schema, validation and append. log/events.jsonl is the single source of truth.

Every line is one JSON object with `v` (schema version), `date` (the play day), `ts` and `type`.
Never edit or delete lines; a wrong event is corrected by a later `void` event.
"""

from __future__ import annotations

import json
from datetime import date, datetime
from pathlib import Path

SCHEMA_VERSION = 1
GRADED = ("lab", "drill", "spar", "boss")

# type -> (required fields, optional fields)
SCHEMA: dict[str, tuple[set[str], set[str]]] = {
    "card_new": ({"card", "area"}, set()),
    "card_review": ({"card", "area", "grade"}, {"note"}),
    "forecast_new": ({"id", "question", "p", "resolve_by", "criteria"},
                     {"base_rate", "difficulty", "note"}),
    "forecast_resolve": ({"id", "outcome"}, {"note"}),
    "void": ({"target_ts", "reason"}, set()),
    **{kind: ({"item", "areas", "rubric", "difficulty"}, {"note", "journal"}) for kind in GRADED},
}


class EventError(ValueError):
    pass


def load(path: Path) -> list[dict]:
    if not path.exists():
        return []
    events = []
    for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if line.strip():
            try:
                events.append(json.loads(line))
            except json.JSONDecodeError as exc:
                raise EventError(f"{path}:{n}: not valid JSON ({exc})") from exc
    voided = {e["target_ts"] for e in events if e.get("type") == "void"}
    return [e for e in events if e.get("ts") not in voided]


def validate(event: dict, area_ids: set[str]) -> None:
    """Raise EventError with a plain message if the event is malformed."""
    kind = event.get("type")
    if kind not in SCHEMA:
        raise EventError(f"unknown type {kind!r}; expected one of {sorted(SCHEMA)}")
    required, optional = SCHEMA[kind]
    fields = set(event) - {"v", "ts", "date", "type"}
    if missing := required - fields:
        raise EventError(f"{kind}: missing {sorted(missing)}")
    if extra := fields - required - optional:
        raise EventError(f"{kind}: unknown fields {sorted(extra)}")
    if kind in ("void", "forecast_resolve"):
        if kind == "forecast_resolve" and event["outcome"] not in (0, 1):
            raise EventError("forecast_resolve: outcome must be 0 or 1")
        return
    if kind == "forecast_new":
        for key in ("p", "base_rate"):
            if key in event and not 0 <= event[key] <= 1:
                raise EventError(f"forecast_new: {key} must be a probability 0-1")
        date.fromisoformat(event["resolve_by"])
        return

    areas = event.get("areas", [event["area"]] if "area" in event else [])
    if not isinstance(areas, list) or not areas:
        raise EventError(f"{kind}: areas must be a non-empty list")
    if unknown := set(areas) - area_ids:
        raise EventError(f"{kind}: unknown areas {sorted(unknown)}")

    if kind in GRADED:
        rubric = event["rubric"]
        if not isinstance(rubric, dict) or not rubric:
            raise EventError(f"{kind}: rubric must be a non-empty {{dimension: 0-4}} object")
        for dim, score in rubric.items():
            if not isinstance(score, int) or not 0 <= score <= 4:
                raise EventError(f"{kind}: rubric[{dim!r}] must be an integer 0-4")
        difficulty = event["difficulty"]
        if not isinstance(difficulty, int | float) or not 600 <= difficulty <= 2600:
            raise EventError(f"{kind}: difficulty must be a number 600-2600")
    elif kind == "card_review" and (
            not isinstance(event["grade"], int) or not 0 <= event["grade"] <= 5):
        raise EventError("card_review: grade must be an integer 0-5")


def append(path: Path, payload: dict, area_ids: set[str], today: date) -> dict:
    """Validate and append one event. Returns the stored event."""
    event = {"v": SCHEMA_VERSION, "date": today.isoformat(),
             "ts": datetime.now().isoformat(timespec="microseconds"), **payload}
    validate(event, area_ids)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8", newline="\n") as f:
        f.write(json.dumps(event, ensure_ascii=False) + "\n")
    return event
