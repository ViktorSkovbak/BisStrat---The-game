---
id: L07
title: Bass diffusion: why sales peak and word of mouth wins
areas: [growth, operations]
difficulty: 1300
phase: 2
sim: labs/bass.html
cards: [grow-001, grow-002, grow-003, grow-004]
---

# L07. Bass diffusion: why sales peak and word of mouth wins

## Goal
After this lab you can decide **where growth money goes** (marketing or making customers talk), **when sales will peak**, and **how to plan factory capacity for the peak** instead of the average.

## The principle
**The Bass model** (Frank M. Bass, Management Science, 1969): the timing of a new product's first purchases depends on how many people have already bought. Buyers come from two sources:

- **Innovators** (coefficient **p**): reached by your own marketing and their own curiosity, at a steady rate whatever others do.
- **Imitators** (coefficient **q**): reached by word of mouth, in proportion to how many have already bought.

> New buyers in a period ≈ (p + q × share already bought) × buyers still to come.

**Why it happens:** at launch there are no customers, so only p works and sales are slow. As customers accumulate, word of mouth takes over and sales accelerate. Later few untouched buyers remain, so sales fall. The cumulative curve is an S; sales per period are a bell that **peaks when about (q − p) / 2q of the market has bought** (about 47% at p = 0.02, q = 0.40), at time ln(q/p) / (p + q). With q much larger than p, that is a little before half the market.

| Term | Plain meaning | Typical size |
|---|---|---|
| p | Share of untouched buyers your own marketing converts per year | 0.01-0.03 |
| q | Pull of existing customers on untouched buyers | 0.3-0.5 |
| m | Total potential buyers | Your market |

## The ideal and the trade-offs
**The goal is not fastest adoption at any price.** It is the right growth lever at each stage, and capacity that is there at the peak without sitting idle for years before it.

| Situation | Lean on | Why |
|---|---|---|
| No customers yet (first year) | Marketing and pilots (p) | Word of mouth has nobody to work with |
| A base of customers exists and they are happy | Referrals, case studies, introductions (q) | q is usually about ten times p; each percent on q moves more buyers |
| Customers are unhappy | Fix the product first | Word of mouth multiplies what customers say, good or bad |

| Lever | Effect in the lab (+40% each, baseline p 0.02, q 0.40) | Cost and catch |
|---|---|---|
| **Marketing** (raise p) | Year-5 sales about 1.2× (300 vs 247); ahead for years 1-3 | Reach is capped by the market size; fades as the market saturates |
| **Referenceable customers** (raise q) | Year-5 sales about **1.6×** (395); overtakes marketing in year 4 | Needs real customer success; pilots cost engineering time; slower to start |
| **Both** (20% each) | About 1.4× (347) | Hedge against being wrong about the product |
| **Seed customers** at launch | 10: about 2 months earlier; 30: about 5 months; 100: about 1.3 years | Each costs a discounted unit; value per euro roughly flat |

**Capacity rule:** plan for the peak plus slack, but buy it in modules timed to the curve. Sizing for the average loses customers; sizing exactly for the peak runs at about 100% (Kingman: waits blow up above about 85%).

## Tests (in the simulation; answers for the teacher)
Setting: a market of 3,000 potential buyers, p = 0.02, q = 0.40, ten years. Today: customers by year 3 about 322, sales in year 5 about 247 a year, half the market bought by year 7.4, peak about 328 a year in year 8.
1. **Marketing or word of mouth?** (+40% on either lever, €300k.) Marketing (p): year-5 sales 300 (1.2×); **referenceable customers (q): 395 (1.6×)**; split: 347 (1.4×). Marketing leads to the end of year 3 (438 customers vs 418), then word of mouth overtakes in year 4 and reaches 1,116 by year 5 vs 987. Marketing would need to be about 3.2× stronger to match year-5 sales. Best: B. The instinct (marketing) is not the best.
2. **Factory for the average or the peak?** Needs: serve everyone, never above 85% load, fewest unit-years bought. Average-sized (230): loses 377 customers (17%). Peak-sized (330): 99% load in the peak year and above 85% in years 6-9. Peak plus a fifth (400): safe (82%) but 4,000 unit-years, 57% average load. **Staged (190, +105 in year 4, +105 in year 6): serves all, busiest year 84%, 3,160 unit-years (21% less than C).** Best: D.
3. **Launch with reference customers?** Budget €1.2M, €40k each (assumed). None: 322 customers by year 3. 10 refs: 350 (1.1×; about 2 months earlier). **30 refs: 405 (1.3×; about 5 months earlier).** 100 units: 584 (1.8×; peak moves from year 8 to 6) but costs €4M. Best within budget: C. Each reference is worth about 5-6 days of the marketing flow; value per euro is about flat (€14-15k per extra customer by year 3).

## Evidence
- **Bass's original fit.** Bass (Management Science 15(5), 1969, pp. 215-227; abstract read on IDEAS/RePEc): the model was tested on data for eleven consumer durables, predicted the sales peak and its timing well on historical data, and was used for a long-range colour-TV forecast.
- **Typical parameters, across studies.** Sultan, Farley & Lehmann (Journal of Marketing Research 27(1), 1990, pp. 70-77): a meta-analysis of 213 applications of diffusion models from 15 articles. Secondary sources (a 2015 System Dynamics Society paper by Kumar; the Wikipedia article on the Bass diffusion model) report average p of about 0.03 and average q of about 0.38 (typical ranges 0.01-0.03 and 0.3-0.5), with large variation. *(The 1990 paper itself was not read; the averages are not yet verified against it.)* Their conclusion, as relayed by the Kumar paper: diffusion is driven more by word of mouth than by innate innovativeness.
- **Business and industrial adopters.** Mansfield (Econometrica 29(4), 1961, pp. 741-766; abstract read): how fast firms in four industries adopted twelve important innovations; the abstract says the results fit an imitation-style model quite well. *(The abstract does not name the industries; which ones is not yet verified.)* Ryan & Gross (1943), via Wikipedia's article on diffusion of innovations: hybrid seed corn spread among Iowa farmers over more than ten years, with most farmers first planting only a small share of their fields with it. Wikipedia's Bass article also lists hybrid corn among applications in Sultan et al. *(Not yet verified in the primary sources.)*
- **Industrial adopters imitate more.** A course text summarising Chandrasekaran & Tellis (2006, Review of Marketing Research 3, 39-80) reports average q of 0.38-0.53, with industrial and medical innovations above consumer durables. *(Not yet verified against the review.)*
- **No B2B hardware p and q found.** We found no source giving fitted p and q for a B2B hardware product. The lab's baseline (p 0.02, q 0.40) is a judgement inside the typical ranges, not a measurement.

## Where it breaks
- **All buyers count the same.** The model assumes a fixed market and that every buyer is equally persuasive. In B2B a few reference customers (a big name, a trusted plant manager) are worth far more than an average adopter, and one bad reference can cost more than ten good ones.
- **Fixed p and q.** Price changes, new features, a competitor or a recession change the coefficients. Fitted on early data, a static Bass curve can mislead: a lecture-note summary of the literature says static fits bias market size and p downward and q upward *(not yet verified)*.
- **The market is not fixed.** Potential buyers (m) is a guess that moves with price and with how the product improves. Early fits of m are unreliable.
- **Supply and sales cycles.** The lab lets demand ignore the factory. In real life a shortage delays word of mouth and sends buyers to rivals, and long sales cycles blur the timing of p and q.
- **Repeat sales and replacement** are not modelled; the curve is first purchases only.

## Application question (graded on rubric B)
> It is mid-2027. Your new company has five paid pilots and the product works. About 3,000 companies could buy it. A grant of €300k can only be spent on **either** trade fairs and outbound sales, **or** turning three pilots into published, referenceable installations. Your contract manufacturer wants a capacity commitment for the next five years.
> 1. What shape do you expect sales to take, and roughly when do they peak? Size the peak against the first year (no calculation needed).
> 2. Where does the €300k go, and what do you commit to the manufacturer? Give the policy, not only the first move.
> 3. Where could the Bass picture mislead you here?

Answer in under 300 words.

## Takeaways
1. Two engines, one curve: your marketing (p) reaches a small steady share, and existing customers (q) pull in the rest. New customers per year rise, peak at roughly half the market, then fall.
2. Once happy customers exist, word of mouth is the bigger lever (q is usually about ten times p). Marketing leads for the first three years only.
3. Plan the factory for the peak, in stages: the peak year is about 1.4× the ten-year average and 4.5× year 1; averaging loses customers and exact-peak sizing runs near 100%.
4. A few reference customers are a small head start (5-6 days each at this market size); their real value is credibility, which acts on q.

## Sources
- Bass, F.M. (1969). A new product growth for model consumer durables. *Management Science*, 15(5), 215-227.
- Sultan, F., Farley, J.U. & Lehmann, D.R. (1990). A meta-analysis of applications of diffusion models. *Journal of Marketing Research*, 27(1), 70-77 (averages via secondary sources).
- Mansfield, E. (1961). Technical change and the rate of imitation. *Econometrica*, 29(4), 741-766.
- Chandrasekaran, D. & Tellis, G.J. (2006). A critical review of marketing research on diffusion of new products. *Review of Marketing Research*, 3, 39-80 (via secondary summary).
- Ryan, B. & Gross, N.C. (1943), hybrid seed corn in Iowa (via Wikipedia, "Diffusion of innovations").
- Kumar, A. (2015). The Bass diffusion model does not explain diffusion. System Dynamics Society conference paper (read only as search snippet).
- Wikipedia, "Bass diffusion model" (equations, parameter ranges).
- Kingman's law: see Lab L01.
