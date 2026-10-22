"""The `foundry` command. Skills call it; Viktor can too.

  foundry status [--json]       XP, level, streak, due cards, forecasts, today's pick
  foundry due                   cards due today, oldest first
  foundry next                  today's adaptive pick (JSON)
  foundry record TYPE DATA      validate and append one event (DATA = JSON object, or - for stdin)
  foundry forecasts             open forecasts, due ones first
  foundry export [--out PATH]   write web/state.json for the artifact
  foundry check                 replay the whole log and report problems
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import date
from pathlib import Path

from foundry import events, export, rules
from foundry.content import ROOT, load_items, load_map
from foundry.engine import State, replay
from foundry.machine import all_parts
from foundry.pick import next_pick

DEFAULT_LOG = ROOT / "log" / "events.jsonl"
DEFAULT_OUT = ROOT / "web" / "state.json"


def _state(log: Path, today: date) -> State:
    _, areas = load_map()
    return replay(events.load(log), list(areas), today)


def cmd_status(args: argparse.Namespace) -> int:
    tracks, areas = load_map()
    items = load_items()
    state = _state(args.log, args.today)
    pick = next_pick(state, areas, items)
    data = export.build(state, tracks, areas, pick)
    due_fc = [f.id for f in state.forecasts.values()
              if f.outcome is None and f.resolve_by <= args.today]
    week_fc = [f for f in state.forecasts.values() if (args.today - f.created).days < 7]
    if args.json:
        data["forecasts_due"] = due_fc
        data["forecast_needed"] = not week_fc
        print(json.dumps(data, indent=2, ensure_ascii=False))
        return 0
    p, s, c = data["player"], data["streak"], data["cards"]
    print(f"Level {p['level']} {p['title']}  |  XP {p['xp']} (next level at {p['next_level_at']})")
    done = "done today" if s["today_done"] else "not yet today"
    print(f"Streak {s['days']} days ({done}), best {s['best']}, freezes {s['freezes']}")
    print(f"Cards: {c['due']} due, {c['total']} in deck, {c['mature']} mature")
    if due_fc:
        print(f"Forecasts to resolve: {', '.join(due_fc)}")
    if not week_fc:
        print("No forecast made in the last 7 days.")
    for a in data["areas"]:
        if a["items"] or a["level"]:
            flag = "  JAMMED: " + "; ".join(a["reasons"]) if a["jammed"] else ""
            print(f"  {a['name']:<42} {a['rating']:>5}  part L{a['level']}{flag}")
    n = data["next"]
    print(f"Next: {n['kind']} {n['item'] or ''} [{n['area']}, D{n['target_difficulty']}]: "
          f"{n['reason']}")
    return 0


def cmd_due(args: argparse.Namespace) -> int:
    state = _state(args.log, args.today)
    items = load_items()
    for card in state.due_cards():
        sched = state.cards[card]
        path = items[card].path.relative_to(ROOT).as_posix() if card in items else "?"
        print(f"{card}\t{state.card_area[card]}\tdue {sched.due}\treps {sched.reps}\t{path}")
    return 0


def cmd_next(args: argparse.Namespace) -> int:
    _, areas = load_map()
    state = _state(args.log, args.today)
    print(json.dumps(next_pick(state, areas, load_items()).to_dict(), indent=2))
    return 0


def cmd_record(args: argparse.Namespace) -> int:
    _, areas = load_map()
    raw = sys.stdin.read() if args.data == "-" else args.data
    payload = {"type": args.type, **json.loads(raw)}
    before = _state(args.log, args.today)
    try:
        stored = events.append(args.log, payload, set(areas), args.today)
    except events.EventError as exc:
        print(f"Not recorded: {exc}", file=sys.stderr)
        return 2
    after = _state(args.log, args.today)
    out: dict = {"recorded": stored["type"], "ts": stored["ts"],
                 "xp_gained": after.xp - before.xp, "xp": after.xp, "level": after.level}
    if after.level > before.level:
        out["level_up"] = f"{rules.title_for(after.level)} (level {after.level})"
    out["ratings"] = {a: f"{round(before.areas[a].rating)} -> {round(after.areas[a].rating)}"
                      for a in areas if after.areas[a].rating != before.areas[a].rating}
    if args.type == "card_review":
        sched = after.cards[payload["card"]]
        out["card_next_due"] = f"{sched.due} (interval {sched.interval}d, ease {sched.ease:.2f})"
    if after.played and args.type in events.GRADED:
        out["grade"] = round(after.played[-1].grade, 3)
    parts_before, parts_after = all_parts(before), all_parts(after)
    out["machine"] = [f"{areas[a].part_name}: L{parts_before[a].level} -> L{parts_after[a].level}"
                      for a in areas if parts_after[a].level != parts_before[a].level]
    out["streak"] = after.streak
    out["today_done"] = after.today_counts
    print(json.dumps(out, indent=2, ensure_ascii=False))
    return 0


def cmd_forecasts(args: argparse.Namespace) -> int:
    state = _state(args.log, args.today)
    open_fc = sorted((f for f in state.forecasts.values() if f.outcome is None),
                     key=lambda f: f.resolve_by)
    for f in open_fc:
        due = "DUE" if f.resolve_by <= args.today else "   "
        print(f"{due} {f.id}\tp={f.p:.2f}\tby {f.resolve_by}\t{f.question}")
    if not open_fc:
        print("No open forecasts.")
    return 0


def cmd_export(args: argparse.Namespace) -> int:
    tracks, areas = load_map()
    state = _state(args.log, args.today)
    data = export.build(state, tracks, areas, next_pick(state, areas, load_items()))
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(data, indent=1, ensure_ascii=False) + "\n", encoding="utf-8",
                        newline="\n")
    print(f"Wrote {args.out}")
    return 0


def cmd_check(args: argparse.Namespace) -> int:
    _, areas = load_map()
    problems = []
    for n, e in enumerate(events.load(args.log), start=1):
        try:
            events.validate(e, set(areas))
        except events.EventError as exc:
            problems.append(f"event {n}: {exc}")
    state = _state(args.log, args.today)
    items = load_items()
    problems += [f"card {c} has no file in curriculum/cards" for c in state.cards if c not in items]
    print("\n".join(problems) or f"OK: log replays cleanly ({state.xp} XP).")
    return 1 if problems else 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="foundry", description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--log", type=Path, default=DEFAULT_LOG, help="event log (dry runs)")
    parser.add_argument("--today", type=date.fromisoformat, default=date.today(),
                        help="play day, YYYY-MM-DD (dry runs)")
    sub = parser.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("status")
    p.add_argument("--json", action="store_true")
    p.set_defaults(fn=cmd_status)
    sub.add_parser("due").set_defaults(fn=cmd_due)
    sub.add_parser("next").set_defaults(fn=cmd_next)
    p = sub.add_parser("record")
    p.add_argument("type", choices=sorted(events.SCHEMA))
    p.add_argument("data", help="JSON object with the event fields, or - for stdin")
    p.set_defaults(fn=cmd_record)
    sub.add_parser("forecasts").set_defaults(fn=cmd_forecasts)
    p = sub.add_parser("export")
    p.add_argument("--out", type=Path, default=DEFAULT_OUT)
    p.set_defaults(fn=cmd_export)
    sub.add_parser("check").set_defaults(fn=cmd_check)
    args = parser.parse_args(argv)
    return args.fn(args)


if __name__ == "__main__":
    raise SystemExit(main())
