---
id: L05
title: Calibration and the outside view: how sure should you sound
areas: [forecasting, fundraising]
difficulty: 1200
phase: 1
sim: labs/calibration.html
cards: [fc-001, fc-002, fc-003, fc-004]
---

# L05. Calibration and the outside view: how sure should you sound

## Goal
After this lab you can decide **what probability to put on a call**: start from how often that kind of thing happens, adjust a little for what you know, and never sound surer than your record. The lab also launches the weekly **/forecast** habit.

## The principle
**Outside view** (Kahneman & Lovallo, Management Science, 1993): the inside view builds a forecast from the plan and the story of this case; the outside view starts from how comparable cases turned out (the **reference class**) and then adjusts. The inside view produces forecasts that are too bold; the outside view anchors on what usually happens.

**Calibration:** your forecasts are calibrated if the things you call 70% happen about 70% of the time, the 90% ones about 90%, and so on.

**Brier score** (Brier, Monthly Weather Review, 1950): the average of (stated probability − outcome)², where the outcome is 1 if it happened and 0 if not. For yes/no questions: 0 is perfect, **0.25 is what saying 50% every time scores**, 1 is worst. Lower is better. Large confident misses cost the most, because the miss is squared.

| You say | It happens | Score | It does not | Score |
|---|---|---|---|---|
| 90% | 1 | 0.01 | 0 | 0.81 |
| 70% | 1 | 0.09 | 0 | 0.49 |
| 50% | 1 | 0.25 | 0 | 0.25 |

**Why a good forecaster is not a bold one:** the Brier score rewards both calibration (the numbers mean what they say) and resolution (the numbers actually separate likely from unlikely cases). A forecaster who is bold without the information to back it up is miscalibrated and loses to someone who just says 50%.

## The ideal and the trade-offs
**What to aim for:** a **calibrated** record (the curve of "what I said" against "how often it happened" lies on the diagonal) with as much **resolution** as your information honestly allows.

**Rules of thumb**
- Start from the base rate of a reference class, then adjust in proportion to how predictive your evidence has been before.
- A strong feeling about this one case is an adjustment of a few points, not a new starting point. (House heuristic, not a sourced figure: on a single story, stay within about 10 points of the base rate unless you have hard, case-specific evidence.)
- Use 90% or more only if your own record of 90% calls shows about that many hits. Look at your record in bins, not at your feeling.
- Never use 0% or 100% on something that can still be decided by chance.

| Lever | Effect in the lab / evidence | Cost and catch |
|---|---|---|
| **Start from a reference-class base rate** | Large: 65% gut becomes about 10%, a Brier score about 4.4× better (Test 2) | Hours to find a class; what counts as "comparable" is arguable |
| **Adjust in proportion to evidence, not to feeling** | Medium: base rate alone 0.240, base rate plus adjustment 0.206 (Test 1) | Needs a record of how well your cues predicted before |
| **Fix overconfidence using your own record** | Large: 20 points too sure removes about 70% of the edge (Test 3) | Needs about 50+ resolved calls before the bins are readable |
| **Score every call, weekly** | Makes the two above possible | Discipline; questions must be sharp (date, yes/no) |
| **Training, teaming, tracking** | Improved calibration and resolution in the tournaments (Mellers et al. 2014); the size is disputed by a 2025 reanalysis | Teams and training cost time; a solo founder can approximate with an advisor or two |
| **Say 50% to be safe** | None: no edge at all | Useless for decisions, and costs you the learning |

**Founder rule:** plan runway and hiring on the reference-class rate (grants about 6-7%, see below), not on how the application feels. Every applicant's application feels strong.

## Tests (in the simulation; answers for the teacher)
Illustrative model: each question has a true chance that varies; you see only a noisy read of it (typical error 15 points). The Brier score is computed as an expectation, so the numbers below are exact for the model, not simulated. Setting: about 40% of such calls happen, questions very mixed.
1. **Which forecaster wins?** Bold 90/10 by gut **0.268** (7% worse than a coin flip; its 90% calls happen about 61%, its 10% calls about 29%) vs timid 50% **0.250** vs always the base rate 40% **0.240** vs **base rate then adjust 0.206** (about 18% better than a coin flip). Best: base rate then adjust. The instinct (the decisive, bold forecaster) is the worst of the four. No size question.
2. **The grant.** True chance assumed 10% (programme rate 6-7%, plus a nudge for strong preparation; the 10% is an assumption). Log 65% **0.393**; 35% **0.153** (2.6× better); **10% 0.090 (4.4× better)**; 3% 0.095 (4.1× better). Best: 10%. The instinct (65%, or splitting the difference at 35%) is wrong. At low chances, being a few points off costs little; being tens of points off costs a lot.
3. **Too sure by 20 points.** Edge over a coin flip: **calibrated 18%** (0.206), trim by 10 points 15% (0.213, 2.9× the edge of today), keep 20 points too sure **5%** (0.237), 50% on everything 0% (0.250). Best: say what the record says (about 3.5× the edge of today). Overconfidence costs about 70% of the edge, and going timid is worse still.

## Evidence
- **Outside view.** Kahneman & Lovallo (Management Science 39(1), 1993) argue that forecasts built on the plan and its scenarios (the inside view) are too optimistic, and that managers should supplement them with the record of comparable cases. *(Read from the abstract and secondary summaries; the full text has not been read.)*
- **Reference class forecasting for projects.** Flyvbjerg (Project Management Journal 37(3), 2006) presents reference class forecasting as a way to correct optimism bias in project forecasts, with a practical application to transport infrastructure. A study of 258 transport projects (Flyvbjerg, Holm & Buhl, Journal of the American Planning Association 68(3), 2002) reports average cost overruns of 45% for rail, 34% for bridges and tunnels and 20% for roads. *(Figures come from a search summary of the abstract, not from the paper: not yet verified against the paper.)*
- **Good Judgment Project.** The project took part in the US intelligence research agency IARPA's forecasting tournament (the ACE programme), starting in 2011 (end year 2015: not yet verified), and a secondary summary says it won both seasons it ran and was 35% to 72% more accurate than other research teams *(secondary source, not yet verified)*. Mellers et al. (Psychological Science 25(5), 2014; title: "Psychological strategies for winning a geopolitical forecasting tournament") report that **training, teaming and tracking** improved accuracy, both calibration and resolution. The abstract gives no effect sizes; none are quoted here. Mellers et al. (Perspectives on Psychological Science 10(3), 2015) describe how the top performers each year were grouped into elite teams of **superforecasters**, whose accuracy persisted over hundreds of questions. Tetlock & Gardner's *Superforecasting* (2015) is the popular account; it has not been read for this lab. The widely repeated claim that the top forecasters beat intelligence analysts with classified information by about 30% comes from secondary sources and is *(not yet verified)*.
- **The base rate for EU deep-tech grants (official EIC pages).** October 2025 cut-off of the EIC Accelerator: 923 full applications (EIC news, 17 Oct 2025); the February 2026 EIC release reports 61 start-ups selected out of 121 that reached the interview stage, so about **6.6%** of full applications were funded (my calculation; the release does not state the cut-off, and I match the figures by timing: *not yet verified* that they refer to the same round). October 2024 cut-off: 71 selected of 1,211 submitted, 431 invited to interview (EIC news, Feb 2025), about **5.9%**. A third-party page puts the end-to-end rate including a short first step near 3%, without a source (*not yet verified*). The brief behind this lab suggested 10-15%; the official counts say about 6-7%.

## Where it breaks
- **The reference class is a choice.** "EIC full applications" and "deep-tech grants with a strong consortium" give different rates; pick the narrowest class with enough cases, and show the range.
- **Small samples.** A reference class of five cases tells you little; shrink toward a wider class.
- **Rare events and fat tails.** Brier scores say little about 1-in-1,000 outcomes; a calibrated 1% forecaster still has to survive the 1%.
- **Real change.** If the programme changes its rules or budget, the old base rate is stale; adjust for the change, not for your mood.
- **The score is not the decision.** A forecast of 10% only matters through what you do with it (spend, hire, apply again); it is meant to be used with payoffs.
- **The effect of training and teaming is contested.** A 2025 reanalysis in Psychological Science ("Rethinking the Role of Teams and Training in Geopolitical Forecasting") argues that once extra variables are modelled, the effects of teaming and training shrink or vanish in some models *(known from the abstract only)*.

## Application question (graded on rubric B)
> It is early 2027. You tell your co-founder you are "80% sure" your first paying pilot customer signs by the end of March. Three calls went well, the champion at the customer likes the demo, and you cannot picture it failing.
> 1. What is the outside view for this call? Name the reference class, how you would find its base rate with no data of your own, and roughly how far an 80% from your gut could be from it.
> 2. What probability do you log, and how did you get there? Describe the habit (what you record, when you score it, what you look at after a month and after a year).
> 3. Where could starting from a base rate mislead you here?

Answer in under 300 words.

## Takeaways
1. Start from the base rate of a reference class, then adjust. A grant programme that funds about 6-7% of full applications (EIC, 2024-25) tells you more than how strong your application feels.
2. Boldness is not skill. Saying 90% or 10% on gut scored worse than saying 50% every time (0.268 vs 0.250); base rate plus adjustment scored 0.206.
3. Calibration means your 70% calls happen about 70% of the time. Being 20 points too sure removed about 70% of the edge, because the Brier score punishes confident misses in squares.
4. Keep score every week. Log each call as a number, resolve it, and plot your record in bins; training, teaming and tracking improved accuracy in the forecasting tournaments.

## Sources
- Brier, G.W. (1950). Verification of forecasts expressed in terms of probability. *Monthly Weather Review*, 78(1), 1-3.
- Kahneman, D. & Lovallo, D. (1993). Timid choices and bold forecasts: a cognitive perspective on risk taking. *Management Science*, 39(1), 17-31. (Abstract level: https://ideas.repec.org/a/inm/ormnsc/v39y1993i1p17-31.html)
- Mellers, B. et al. (2014). Psychological strategies for winning a geopolitical forecasting tournament. *Psychological Science*, 25(5), 1106-1115. https://doi.org/10.1177/0956797614524255 (abstract only)
- Mellers, B. et al. (2015). Identifying and cultivating superforecasters as a method of improving probabilistic predictions. *Perspectives on Psychological Science*, 10(3), 267-281. https://doi.org/10.1177/1745691615577794 (abstract only)
- Tetlock, P.E. & Gardner, D. (2015). *Superforecasting: The Art and Science of Prediction*. Crown. (Not read.)
- Flyvbjerg, B. (2006). From Nobel Prize to project management: getting risks right. *Project Management Journal*, 37(3), 5-15. https://arxiv.org/abs/1302.3642 (abstract only)
- Flyvbjerg, B., Holm, M.S. & Buhl, S. (2002). Underestimating costs in public works projects: error or lie? *Journal of the American Planning Association*, 68(3), 279-295. (Figures via a search summary.)
- European Innovation Council. Strong interest in EIC Accelerator funding with 923 companies applying for the final 2025 cut-off (17 Oct 2025): https://eic.ec.europa.eu/news/strong-interest-eic-accelerator-funding-923-companies-applying-final-2025-cut-2025-10-17_en
- European Innovation Council. 61 start-ups and SMEs secure EIC support in latest round of the EIC Accelerator (17 Feb 2026): https://eic.ec.europa.eu/news/61-start-ups-and-smes-secure-eic-support-latest-round-eic-accelerator-2026-02-17_en
- European Innovation Council. EIC Accelerator: 71 companies selected (17 Feb 2025): https://eic.ec.europa.eu/news/eic-accelerator-71-companies-selected-most-competitive-funding-round-so-far-2025-02-17_en
- Wikipedia, "The Good Judgment Project" and "Superforecaster" (secondary, for tournament background only).
