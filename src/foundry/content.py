"""Curriculum map (curriculum/map.toml) and the frontmatter of labs, drills and cards."""

from __future__ import annotations

import tomllib
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CURRICULUM = ROOT / "curriculum"


@dataclass(frozen=True)
class Area:
    id: str
    name: str
    track: str
    phase: int
    part: str
    part_name: str
    plot: tuple[int, int]
    spine: str


@dataclass(frozen=True)
class Item:
    """A lab, drill or card. `areas[0]` is the primary area."""
    id: str
    kind: str
    title: str
    areas: tuple[str, ...]
    difficulty: int
    phase: int
    path: Path


def load_map(curriculum: Path = CURRICULUM) -> tuple[list[dict], dict[str, Area]]:
    data = tomllib.loads((curriculum / "map.toml").read_text(encoding="utf-8"))
    areas = {
        a["id"]: Area(a["id"], a["name"], a["track"], a["phase"], a["part"], a["part_name"],
                      tuple(a["plot"]), a["spine"])
        for a in data["area"]
    }
    return data["track"], areas


def parse_frontmatter(text: str) -> dict[str, object]:
    """Tiny parser for `key: value` frontmatter. Values: int, [a, b] list, or string."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    meta: dict[str, object] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            break
        key, _, raw = line.partition(":")
        value = raw.strip()
        if value.startswith("[") and value.endswith("]"):
            meta[key.strip()] = [v.strip() for v in value[1:-1].split(",") if v.strip()]
        elif value.lstrip("-").isdigit():
            meta[key.strip()] = int(value)
        else:
            meta[key.strip()] = value.strip('"')
    return meta


def _item(path: Path, kind: str) -> Item:
    meta = parse_frontmatter(path.read_text(encoding="utf-8"))
    areas = meta.get("areas") or [meta["area"]]
    return Item(str(meta["id"]), kind, str(meta.get("title", meta["id"])), tuple(areas),
                int(meta.get("difficulty", 1200)), int(meta.get("phase", 1)), path)


def load_items(curriculum: Path = CURRICULUM) -> dict[str, Item]:
    """All labs (labs/*/lab.md), drills (drills/*/brief.md) and cards (cards/*/*.md)."""
    items: dict[str, Item] = {}
    for path in sorted(curriculum.glob("labs/*/lab.md")):
        it = _item(path, "lab")
        items[it.id] = it
    for path in sorted(curriculum.glob("drills/*/brief.md")):
        it = _item(path, "drill")
        items[it.id] = it
    for path in sorted(curriculum.glob("cards/*/*.md")):
        it = _item(path, "card")
        items[it.id] = it
    return items
