---
id: L02
title: The Peter principle: why your best engineer may make a poor lead
areas: [org, management]
difficulty: 1300
phase: 1
sim: labs/peter.html
cards: [org-001, org-002, org-003, org-004]
---

# L02. The Peter principle: why your best engineer may make a poor lead

## Goal
After this lab you can decide **who becomes a team lead** and what to offer the stars you do not promote: pick the promotion rule that fits how much the new job resembles the old one, and use a technical track instead of forcing good engineers into management.

## The principle
**The Peter principle** (Laurence J. Peter & Raymond Hull, *The Peter Principle*, 1969): in a hierarchy, people get promoted for doing well in their current job until they reach a job they are bad at, and there they stay. (The book itself was not read for this lab; the statement of the idea is the standard one.)

**The mechanism has three parts:**
1. Firms promote on **performance in the current job**, because it is visible.
2. Skill in the **new job** may be only weakly related to skill in the old one (great engineer, so-so manager).
3. So the promoted person is, on average, **only average at the new job**, and you have lost their output in the old one.

**Agent-based test.** Pluchino, Rapisarda & Garofalo (*Physica A*, 389(3), 2010, 467-472; Ig Nobel prize in management, 2010) simulated a pyramid of 160 positions over six levels. They compared two assumptions:
- **Common-sense hypothesis:** the promoted person keeps their old competence, give or take a small change.
- **Peter hypothesis:** competence in the new job is a fresh draw, unrelated to the old one.

| Promotion rule | Common sense (skills transfer) | Peter (skills unrelated) |
|---|---|---|
| Best performer | **+9%** efficiency | **-10%** |
| Worst performer | -5% | +12% |
| Random | +2% | +1% |
| Alternate best and worst | +1.5% | +1.5% |

Under the Peter hypothesis, promoting the best performer is worse than promoting at random. Under common sense it is the right rule. When you do not know which world you are in, random or alternating promotion avoids the loss.

## The ideal and the trade-offs
**The goal is not "never promote the best".** It is to promote on **evidence of the new job**, and to give your stars a prize that does not destroy their output.

**What to aim for:**
- The more the new job is a different craft (managing people vs writing code), the less old performance tells you. The more it is the same craft, the more it does.
- Promotion is also a motivator (Benson, Li & Shue argue the Peter principle may be the price of motivating people). So you need to offer the stars something.

| Situation | Rule | Why |
|---|---|---|
| New job is a different skill (people lead, first-time manager) | **Test the new skill** (trial period, acting lead, team feedback); at worst, random among capable candidates | Old performance barely predicts managing; the trial reads it even if noisily |
| New job is mostly the old craft (tech lead, codes ~70%) | **Promote the best performer** | Skill transfers; the common-sense world |
| You expect passed-over stars to sulk or leave | **Add a dual ladder** with real pay and title | Keeps output and motivation without a management job |
| Unsure which world you are in | Mix evidence: performance plus a trial | Pluchino et al.: best-first is the risky rule when the link is unknown |

| Lever | Effect | Cost and catch |
|---|---|---|
| **Test managing skill** (acting lead, 360 feedback) | Large when skills barely transfer | Takes weeks; the test is noisy |
| **Dual career ladder** | Large for stars: keeps their output and goodwill | Only works if the technical title carries real pay, status and say in decisions |
| **Make the lead role mostly technical** | Medium: makes old skill predict new | Leaves people-management duties unowned |
| **Random among capable candidates** | Small gain over best-first when skills are unrelated | Feels unfair; demotivating if seen as lottery |
| **Fast reversal** (a way back without shame) | Limits damage from a wrong promotion | Needs culture; the Peter principle says people otherwise stay stuck |

**Founder rule:** your first leads set the culture for years. Run a trial before the title, and create the technical track the day you create the management track.

## Tests (in the simulation; answers for the teacher)
Setting: 20 engineers, 4 leads of 4 each. A good or bad lead lifts or cuts each report's output; "lost" is the output lost against picking leads perfectly (in engineer-equivalents, about €9k a month each). Illustrative model.
1. **Who gets the lead jobs** (skills barely transfer): best engineers (lost 3.2, about €29k a month) vs random (2.2, 1.4×) vs **management trial (1.2, 2.7×)**. Best: trial. The instinct (promote the best) is the worst. Leads from the trial lift each report about 7%; the best engineers about 1.4%.
2. **The stars expect the job** (passed-over star slows 8%): promote the stars 3.2 vs **dual ladder + trial 1.0 (3.2×)** vs dual ladder + best of the rest 2.6 (1.2×) vs trial with no title 1.5 (2.1×). Promoting the stars leaves only 1.7 of 5.7 units of their output. Both halves matter.
3. **Tech lead** (codes 70%, skills almost fully transfer): output of 20: **best engineers 20.1**, trial 19.6, random 18.8. Best: promote the best. The reflex from test 1 is now the wrong one.

## Evidence
- **Simulation.** Pluchino, Rapisarda & Garofalo (Physica A, 2010; arXiv 0907.0455): numbers in the table above (efficiency change from a starting value of about 70%; 50 runs, spread about 1%). Under the Peter hypothesis, promoting the best leaves everyone at the level where their competence is lowest.
- **Real firms.** Benson, Li & Shue, "Promotions and the Peter Principle" (Quarterly Journal of Economics, 134(4), 2019, 2085-2134): microdata on sales workers at 131 US firms, 2005-2011, about 38,800 workers and 1,553 promotions into management. Better sales raised promotion odds: doubling relative sales raised the monthly promotion chance by about a third, and the top seller on a team had roughly triple the base chance. But higher pre-promotion sales predicted worse later managing: doubling pre-promotion sales went with about 6% lower sales for each of the manager's reports (about a third of one worker's output on a team of five). The authors estimate managers would be about 30% better under a policy that promoted fewer top sellers. They also find firms weight sales less when the manager role has more responsibility or when pay is strongly tied to performance. *(Figures read on the journal's HTML page; check against the paper before quoting. The working-paper version reports 214 firms.)*
- **Dual career ladders.** Reported in descriptions as an add-on path that lets specialists advance on a technical or supervisory track, common in engineering and science, used to retain top talent (Wikipedia, "Career ladder"). Rigorous outcome studies appear scarce; one search summary cites a study of 28 senior engineers finding little evidence of two clean types of engineering careers (not yet verified). Company-reported retention gains exist (not yet verified).

## Where it breaks
- **Skill transfer is a spectrum.** The page's tests use "barely" and "almost fully"; real roles sit between, and you rarely know the link in advance.
- **Promotion is also incentive.** If promotion is the main prize, skipping the best has a cost (the model's 8% slump is an assumption, not a measured number).
- **Managers add what is not in output:** culture, hiring, retention. Output per report is a narrow measure.
- **A trial is not free** and can be gamed; a bad trial is only slightly better than random.
- **Small teams.** At 20 engineers there is a small sample; "average" effects can be dominated by one person.
- **Dual ladders can rot** into a consolation prize if the technical track has no real authority.

## Application question (graded on rubric B)
> It is 2028. Your company has 20 engineers and a pilot customer is asking for a named person responsible for each of the four workstreams. Your best engineer, Ana, is the one everyone assumes will become the lead of the main workstream; she has not managed anyone.
> 1. Does the Peter principle apply here? Give the mechanism in your own words and size the risk roughly (small, 2×, 10× in lost output).
> 2. What do you decide for Ana and for the other lead jobs? Give the policy: how you pick, and what you offer Ana either way.
> 3. Where could this law mislead you in your company?

Answer in under 300 words.

## Takeaways
1. The Peter principle is about transfer: if skill in the new job is unrelated to skill in the old, promoting the best performer lowers output (Pluchino et al.: -10% vs +9% when skills do transfer).
2. Test the new job, not the old one: a management trial beat both best-first and random when skills barely transfer (about 2.7× less output lost in the lab).
3. Promoting a star costs twice: you lose their output and gain a weak manager. A dual ladder keeps the output and the motivation.
4. It reverses when the job is mostly the same craft: for a tech lead who codes most of the time, promote the best engineer.

## Sources
- Peter, L.J. & Hull, R. (1969). *The Peter Principle: Why Things Always Go Wrong*. William Morrow. (Not read; cited for the idea.)
- Pluchino, A., Rapisarda, A. & Garofalo, C. (2010). The Peter principle revisited: a computational study. *Physica A*, 389(3), 467-472. arXiv:0907.0455 (https://ar5iv.arxiv.org/html/0907.0455). Ig Nobel Prize in management, 2010 (per catalogue listings; not checked at the prize site).
- Benson, A., Li, D. & Shue, K. (2019). Promotions and the Peter Principle. *Quarterly Journal of Economics*, 134(4), 2085-2134 (https://academic.oup.com/qje/article/134/4/2085/5479268); NBER Working Paper 24343 (https://www.nber.org/papers/w24343).
- "Career ladder", Wikipedia (https://en.wikipedia.org/wiki/Career_ladder), for the description of dual career ladders.
