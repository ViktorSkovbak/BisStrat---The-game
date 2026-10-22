# Decisions

Newest last. Each: what, why, and what it costs to reverse.

## D1. English throughout (22 Oct 2026)
Viktor's choice. Sources, investors and the Crucible are English, and he trains in the language he will pitch and lead in. Overrides the global Danish default for this project.

## D2. Name and place: The Foundry, `projects\foundry` (22 Oct 2026)
Hard to reverse: the folder name is baked into the memory path.

## D3. The LLM grades; code keeps score (22 Oct 2026)
Claude scores rubric dimensions; a stdlib Python CLI computes XP, Elo, SM-2, Brier, streaks and machine state. Model arithmetic is unreliable, and deterministic scoring makes progress trustworthy.

## D4. One append-only event log; everything replays (22 Oct 2026)
`log/events.jsonl` is the only state. Rules can be retuned in `src/foundry/rules.py` and all history is recomputed. Corrections use `void` events. The log format is the hard-to-reverse part; the rules are cheap to change.

## D5. Skills are project-scoped; the mentor is global (22 Oct 2026)
The game skills live in `.claude/skills/` and work in sessions started here, following Viktor's rule of starting sessions from the relevant folder. The `mentor` skill lives in `config\skills\` so it works in Crucible and SA sessions too. `sa-bestyrelsesformand` stays as SA/Saverus governance.

## D6. One private artifact; state as a published JSON file (22 Oct 2026)
The machine page and lab simulations form one multi-file artifact. `state.json` is republished after each session. No runtime database: the local log is the truth, and that costs nothing. Revisit if Viktor wants to answer in the browser.

## D7. Model routing (22 Oct 2026)
Opus grades, spars and examines, because the feedback is the product. The `writer` agent (Sonnet) drafts content, and Opus reviews every draft. Global rules on lean agents apply.

## D8. Curriculum: 19 areas in 6 tracks, 4 phases (22 Oct 2026)
The plan said 20; the map has 19, because game theory sits inside competitive dynamics. Phase order puts founder-relevant mechanisms first: queueing, incentives, cost curves, venture maths and calibration. The adaptive pick overrides the order for weak or jammed areas.

## D9. Difficulty tiers per concept (22 Oct 2026)
| Tier | Task | Typical D |
|---|---|---|
| T1 Apply | One law, clean case, compute the answer | 1100-1300 |
| T2 Diagnose | Messy case with distractors; find which law matters | 1300-1500 |
| T3 Combine | Two or more laws in tension, quantified trade-off | 1500-1700 |
| T4 Live | Viktor's own business, defended against the mentor | 1700-2000 |
Strong areas aim at D = R + 100, and weak areas at R − 50 with extra cards (`src/foundry/pick.py`).
