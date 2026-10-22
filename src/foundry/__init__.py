"""The Foundry: Viktor's strategy-training game.

The LLM grades; code keeps score. Everything here is deterministic and derives from one
append-only event log (log/events.jsonl), so the rules can be retuned and history replayed.

Layers import only downwards:
  rules    pure scoring rules (XP, levels, Elo, SM-2, Brier, streak bonus)
  content  curriculum map and item frontmatter
  events   event schema, validation, append
  engine   replays the log into a State
  machine  machine-part state per area (built, level, jammed)
  pick     adaptive pick of the next main item
  export   state.json for the web artifact
  cli      the `foundry` command
"""
