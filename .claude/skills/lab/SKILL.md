---
name: lab
description: Run a Foundry lab - one business law shown three ways (original theory, interactive simulation, real evidence), ending in a graded application question. Use when Viktor says /lab, "lab", or names a lab id like L01.
argument-hint: "[lab id, e.g. L01]"
model: opus
---

# /lab [id]

1. **Pick:** the id given, else today's pick if it is a lab, else the first unplayed lab (`uv run foundry next`). Read `curriculum/labs/<id>-*/lab.md`.
2. **Teach (one message, under 350 words):** the opening question, the law with who found it and when, the mechanism in plain words, the numbers to remember (keep the table), and the founder's version. Do not paste the file.
3. **Play:** link the simulation (artifact → Labs). Walk through the lab's "Predict first" experiments one at a time. **Viktor writes each prediction in chat before he checks it.** Note in the journal how far off he was; say plainly when he underestimated.
4. **Evidence (short):** three or four bullets from the lab's evidence section, with source and year, plus where the law breaks.
5. **Application question:** show it exactly as written. Viktor answers in writing. Then grade on rubric B with the feedback format from `curriculum/rubrics.md`. Use a model answer at the 1800 level to compare against, but show Viktor only the gaps.
6. **Record:** `uv run foundry record lab '{"item": "<id>", "areas": [<areas from frontmatter>], "difficulty": <difficulty>, "rubric": {"mechanism": n, "numbers": n, "action": n, "limits": n}, "journal": "journal/YYYY-MM-DD.md"}'`. Report XP, rating change and any machine change from the command's output.
7. **First card:** record `card_new` for the first id in the lab's `cards:` list and review it now. The rest arrive one a day through `/train`.
8. If run outside `/train`, do the close from `/train` step 5.

**Writing a new lab:** spawn the `writer` agent with the law, the area, the target difficulty and `curriculum/labs/L01-kingman/lab.md` as the template. The simulation page (`web/labs/<name>.html`) is built in a Foundry build session, using `web/labs/kingman.html` as the pattern, and added to the `LABS` list in `web/index.html`.
