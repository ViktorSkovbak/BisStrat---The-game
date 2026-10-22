# Rubrics

One standard for every grade in the Foundry. The grader (Opus, in the session or via the
`mentor` skill) scores each dimension 0-4 and writes the event; the CLI turns scores into the
grade (share of the maximum), XP and Elo. **Grade the reasoning, never the outcome.**

## Difficulty and rating scale
A difficulty D is the rating at which a player is expected to score 0.5 on that item.

| Rating / D | Who answers like this |
|---|---|
| 1000 | Smart newcomer: names the obvious, no mechanism |
| 1200 | Able generalist: right instinct, thin reasoning, few numbers (start rating) |
| 1500 | **Solid top-MBA answer:** right framework, right crux, rough numbers, a clear call |
| 1800 | **Strong strategy partner or experienced operator:** finds the non-obvious crux, quantifies the trade-off, sequences moves, names kill criteria |
| 2000+ | **Rare, investor-grade judgement:** sees second- and third-order effects, reframes the question, knows exactly what evidence would change the call |

Set D for new items by asking: "what rating would a player need to have even odds of 3/4 on each dimension?"

## Score anchors (all rubrics)
| Score | Meaning |
|---|---|
| 0 | Missing or wrong |
| 1 | Present but generic; could be pasted into any case |
| 2 | Correct and specific, but shallow (1200-1400 level) |
| 3 | Sharp: specific, quantified where it matters, defensible (1500-1700 level) |
| 4 | Exceptional: non-obvious, precise, would change a real board's mind (1800+ level) |

## A. Decision rubric (drills, sparring, boss fights)
1. **diagnosis**: found the real crux, not a symptom. A 4 names the one constraint everything else depends on.
2. **options**: at least three real alternatives, including the uncomfortable one. A 4 includes an option nobody in the room proposed.
3. **mechanism**: causal logic with rough sizes. A 4 names the one number that decides it and gets its order of magnitude right; precise arithmetic is never required.
4. **risk**: what kills the plan, which moves are one-way doors, explicit kill criteria with dates or thresholds.
5. **commitment**: a clear call, a stated confidence (%), the first moves in order, and what would change the decision.

Event: `"rubric": {"diagnosis": n, "options": n, "mechanism": n, "risk": n, "commitment": n}`.

## B. Lab application rubric
1. **mechanism**: states the law and why it holds, in own words.
2. **sizing**: sizes the effect roughly right (small, 2×, 10×; which lever is biggest). Order of magnitude from the curve, never exact calculation.
3. **action**: turns it into a concrete decision or policy for the case, aimed at the lab's stated ideal.
4. **limits**: names where the law's assumptions break in this case.

Event: `"rubric": {"mechanism": n, "sizing": n, "action": n, "limits": n}`.

The lab's in-page tests (calls and sizes) are not graded events; they are practice. Note the result line Viktor copies from the page in the journal.

## C. Boss-fight memo rubric (adds to A)
6. **coherence** (Rumelt's kernel): diagnosis, guiding policy and actions fit together; nothing is a goal dressed up as strategy.
7. **advantage**: names the source of durable advantage (Helmer's power: benefit + barrier) or admits there is none yet.
8. **communication**: a busy investor gets the point in the first paragraph; numbers in tables; no fluff.

## D. Card grades (0-5, SM-2)
| Grade | Meaning |
|---|---|
| 5 | Perfect: correct, own words, applied |
| 4 | Correct with a small hesitation or gap |
| 3 | Correct but effortful or partly vague |
| 2 | Wrong, but the model answer felt familiar |
| 1 | Wrong; only vaguely recognised |
| 0 | Blank |

## Feedback format (every graded item)
1. Scores per dimension, one line of reason each.
2. **The single change that would have raised the grade most.**
3. What a 1800 answer would have contained that this one did not (two or three bullets).
4. Plain verdict where Viktor was wrong, and why. No softening.
