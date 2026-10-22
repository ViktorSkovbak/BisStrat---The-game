---
name: drill
description: Run a Foundry decision drill - a real company at a real turning point with only the facts known at the time. Viktor decides and argues in writing, the reasoning is graded on the decision rubric, then the outcome is revealed. Use when Viktor says /drill, "drill", "case", or names a drill id like D01.
argument-hint: "[drill id, e.g. D01]"
model: opus
---

# /drill [id]

1. **Pick:** the id given, else today's pick if it is a drill, else the first unplayed drill. Read `curriculum/drills/<id>-*/brief.md` only. Do not read `reveal.md` yet.
2. **Brief:** show the brief in full (seat, hindsight warning, facts, task). Start no discussion of your own.
3. **Questions:** if Viktor asks for facts, answer only with what was knowable at the time (from the brief, or from a source dated before the decision). Otherwise say "not known at the time". Give no hints about what happened.
4. **Answer:** Viktor writes his decision, under the brief's word limit. If he goes far over, ask him to cut it: a decision memo that cannot be cut has no crux.
5. **Grade before the reveal.** Score rubric A (diagnosis, options, mechanism, risk, commitment) on the reasoning alone. Write the feedback in the rubric's format. Do this before opening `reveal.md`, so the outcome cannot bias the grade.
6. **Reveal:** now read `reveal.md`. Show what happened in under 250 words, then "what a strong answer contained" against his answer: which of the 1500 / 1800 / 2000+ points he hit and missed.
7. **Record:** `uv run foundry record drill '{"item": "<id>", "areas": [<areas>], "difficulty": <difficulty>, "rubric": {...}, "journal": "journal/YYYY-MM-DD.md"}'`.
8. **Transfer (one question, ungraded):** "Where in your own company is the equivalent of this decision today?" One or two sentences from Viktor, kept in the journal and the vault note.
9. If run outside `/train`, do the close from `/train` step 5.

**Writing a new drill:** spawn the `writer` agent. Prefer less famous cases (hindsight contaminates famous ones) and cases close to Viktor's path: hardware and deep-tech companies, grant- and venture-funded scale-ups, physical-product pricing and manufacturing, founder-CEO transitions. Facts known at the time go in `brief.md`; everything after the decision goes in `reveal.md`.
