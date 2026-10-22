---
name: lab
description: Run a Foundry lab - one business law with its goal and ideal, an interactive simulation with locked decision tests, real evidence, and a graded application question. Use when Viktor says /lab, "lab", or names a lab id like L01.
argument-hint: "[lab id, e.g. L01]"
model: opus
---

# /lab [id]

The lab trains **judgement, not arithmetic**. Viktor never calculates. He learns the principle, the ideal and the trade-offs, makes calls in the simulation, and applies the law to his own company.

1. **Pick:** the id given, else today's pick if it is a lab, else the first unplayed lab (`uv run foundry next`). Read `curriculum/labs/<id>-*/lab.md`.
2. **Teach (one message, under 400 words):**
   - **Goal:** what he will be able to decide after the lab.
   - **The principle:** the law, who found it and when, the mechanism in plain words, and the one table or number to remember.
   - **The ideal and the trade-offs:** what to aim for, the rules of thumb, and the levers with their costs. This part matters most: never teach a law without saying what good looks like.
   Do not paste the file.
3. **Tests (in the simulation):** link the artifact → Labs → the lab. Tell him exactly: "Do Test 1-3. In each, pick an option and a size, lock it, then read the reveal. When done, press **Copy my results** and paste the line here." Do not reveal answers in chat. If he asks how to read the page, explain the controls, never the answers.
4. **Debrief (short):** from his pasted results, name the call he got wrong and the reason in one or two lines; confirm what he got right. Then three bullets of evidence (source and year) and where the law breaks.
5. **Application question:** show it as written. Viktor answers in writing. Grade on rubric B (mechanism, sizing, action, limits) with the feedback format in `curriculum/rubrics.md`. Sizing means order of magnitude, never exact numbers.
6. **Record:** `uv run foundry record lab '{"item": "<id>", "areas": [<areas from frontmatter>], "difficulty": <difficulty>, "rubric": {"mechanism": n, "sizing": n, "action": n, "limits": n}, "note": "<pasted test results>", "journal": "journal/YYYY-MM-DD.md"}'`. Report XP, rating change and machine change from the output.
7. **First card:** `card_new` for the first id in the lab's `cards:` list, then review it. The rest arrive one a day through `/train`.
8. If run outside `/train`, do the close from `/train` step 5.

**Writing a new lab:** spawn the `writer` agent (Sonnet) with the law, the area and the target difficulty. It follows `curriculum/labs/L01-kingman/lab.md` and `web/kit/README.md`, and copies `web/labs/kingman.html`. Review the draft yourself: facts, the stated ideal, the test answers against the model, and the page in the browser preview.
