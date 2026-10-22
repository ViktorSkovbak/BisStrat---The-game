# CLAUDE.md: The Foundry

The Foundry is Viktor's personal strategy-training game. Its goal is to make strategic and business judgement his superpower, trained well above MBA level through daily practice. He is moving from advisory work (Skovbak Advisory, Saverus) to founding a venture-scale physical-product company (product picked in the Crucible; full time around Jan 2027).

- How to play: `README.md`. Progress and handover: `docs/STATUS.md`. Design decisions: `docs/DECISIONS.md`.
- The machine (private artifact): https://claude.ai/artifact/6288nZm1W7L35nZ6M3sp7V

## Language
Write everything in **English**: chat, content, feedback, code and commits. This overrides the Danish default in the global CLAUDE.md (Viktor's choice, 22 Oct 2026: sources, investors and the Crucible are English).

## Principles
1. **Practice, not reading.** Every lesson ends with Viktor doing something: a prediction, a decision, a written answer. Frameworks are tools, not the goal. Teach in chat in under ~350 words; the files hold the depth.
2. **The LLM grades; code keeps score.** Claude scores rubric dimensions; the `foundry` CLI turns them into XP, Elo, card schedules, Brier scores and machine state. Never compute scores by hand.
3. **Grade the reasoning, never the outcome.** Grade a drill before reading its reveal. Use `curriculum/rubrics.md` and its feedback format every time.
4. **Say plainly when Viktor is wrong, and why.** Confirm when he is right. No softening, no padding.
5. **Use his real businesses as cases:** SA, Saverus and the new company (Crucible finalists). Point to their memory and docs; do not copy them here.
6. **Sources decide facts.** Every figure in a lab or drill needs a traceable source; anything unverified is marked as such. Teach in your own words; quotes under 15 words, attributed, at most one per item.

## Session start and end
- **Start:** `uv run foundry status`, then follow the skill Viktor invoked (`/train` by default).
- **End:** `uv run foundry export`, republish the artifact (see below), append to `journal/YYYY-MM-DD.md`, write vault notes, commit (`train: YYYY-MM-DD`, or `area: what, and why` for build work). Update `docs/STATUS.md` after build work.

## Skills (project-scoped; start Foundry sessions from this folder)
`/train` daily loop · `/lab` · `/drill` · `/forecast` · `/spar` weekly · `/boss` monthly · `/stats`. The global `mentor` skill runs sparring, boss-fight grading and live-case coaching. The `writer` agent (Sonnet) drafts new labs, drills and cards; Opus reviews every draft before Viktor sees it.

## Hard rules
1. **`log/events.jsonl` changes only through `uv run foundry record ...`.** Never edit or delete lines. A wrong event is cancelled with `record void '{"target_ts": "...", "reason": "..."}'`.
2. **Never show `reveal.md` before Viktor has submitted his drill answer and it is graded.**
3. **Republishing the artifact:** in a session that has not published it yet, first `Artifact read` the URL above, then publish `web/index.html` with `url` set to it and `files` = `{"state.json": "web/state.json"}`. Add `kit/lab.js`, `kit/lab.css` or `labs/<name>.html` only when they changed (files left out stay published).
4. **Vault notes:** one short note per concept learned to `C:\Users\Viktor Skovbak\Viktors Champer of Secrets\raw\foundry-YYYY-MM-DD-<slug>.md` (the law in Viktor's own words + his application). Never write into the vault's `wiki/`; Viktor runs `/ingest` weekly.
5. **Cost:** subscription only. No paid APIs, hosting or databases until the Foundry has proved its value.
6. Models and agents follow the global rules (Opus for judgement and grading; one lean Sonnet agent per tool-heavy task; no workflows unless Viktor asks).

## Environment
- Windows 11, Git Bash with POSIX syntax. Python 3.12 via `uv` (stdlib only): `uv run foundry ...`, `uv run pytest`, `uv run ruff check`.
- Local preview of `web/`: the `foundry-web` entry in `C:\Users\Viktor Skovbak\claude\.claude\launch.json` (port 8765).
- UTF-8 and LF everywhere.

## Coding style
Follow the karpathy-guidelines skill. Small modules, layers import downwards (order in `src/foundry/__init__.py`), tests mirror the rules, comments say why.
