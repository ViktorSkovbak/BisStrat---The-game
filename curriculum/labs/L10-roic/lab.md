---
id: L10
title: ROIC vs the cost of capital: when growth creates value
areas: [capital, strategy]
difficulty: 1300
phase: 2
sim: labs/roic.html
cards: [cap-001, cap-002, cap-003, cap-004]
---

# L10. ROIC vs the cost of capital: when growth creates value

## Goal
After this lab you can decide **where the next euro goes**: into the fast line, into the high-return line, or back to the owners. You know when growth adds value, when it destroys it and when it does not matter.

## The principle
**Growth creates value only when the return on invested capital (ROIC) is higher than the cost of capital (WACC).** The value-driver formula (Koller, Goedhart & Wessels, *Valuation*, McKinsey & Company, Wiley) says a business is worth

> **value = NOPAT × (1 − g / ROIC) / (WACC − g)**, where NOPAT is next year's after-tax operating profit and g is the steady growth rate.

The term **g / ROIC is the share of profit you must plough back** to grow at g. A business earning a high return needs to reinvest little for each point of growth; a business earning a low return needs to reinvest most of its profit, and little is left to take out.

| ROIC vs WACC | What growth does | Why |
|---|---|---|
| ROIC > WACC | Adds value | Each new euro earns more than it costs |
| ROIC = WACC | Adds nothing | Value = NOPAT / WACC for any g |
| ROIC < WACC | **Destroys value** | Each new euro earns less than it costs |

Worked example (NOPAT €95.4M, g 6%, WACC 10%): ROIC 15% gives a value of €1,431M; ROIC 10% gives €954M; ROIC 8% gives €596M, because 75% of profit has to be reinvested to grow. (Illustration from a tutoring summary of the formula, not from the book itself.)

## The ideal and the trade-offs
**The goal is not growth. It is growth at a return above the cost of capital.** Rank every use of cash by the gap (spread) between its return and the cost of capital. If nothing beats the cost of capital, return the cash.

**Rules of thumb**
- Put the next euro where the return is furthest above the cost of capital, not where growth is fastest.
- On a line below its cost of capital, **fix the return before you grow**. Every extra point of growth costs value.
- On a line at or above the cost of capital, growth is worth roughly the spread times the capital you add. At a spread of zero, growth is worth nothing.
- Capital allocation is the CEO's main lever (Thorndike): every use of cash faces the same hurdle.

| Lever | Effect in the lab | Cost and catch |
|---|---|---|
| **Raise ROIC** (price, yield, tooling reuse, less stock and working capital) | Largest: line B from 8% to 14% is worth 2.5× | Takes real operating work and months; returns can fall back |
| **Redirect the next euro to the highest-spread line** | €10M in A adds about €28.8M of value; in B about €6.7M | Assumes the high-return line can absorb it; returns fall as it saturates |
| **Slow growth on a sub-hurdle line** | B grows 2% instead of 4%: 1.1× | Costs revenue and the growth story; right only until the return is fixed |
| **Return cash** (buyback, dividend) | Neutral at the cost of capital: €10M is worth €10M | Gives up the option to use it later; buybacks only help if the shares are cheap |
| **Push growth on a sub-hurdle line** | B from 4% to 8%: value falls to zero | The instinct of a growth-hungry board |

**Founder rule:** investors reward growth, but they price it through the return on the capital it needs. A hardware company that grows faster on a return below its cost of capital burns cash and value together. Show investors the ROIC path (or the unit-cost path that gets it above the hurdle), not only revenue growth.

## Tests (in the simulation; answers for the teacher)
Setting: two lines, €100M of capital each; A earns 25% and grows 2% (worth €287.5M); B earns 8% and grows 4% (worth €66.7M); cost of capital 10%; €10M spare cash. Owners are worth €364.2M today (company €354.2M plus the €10M).
1. **The next €10M.** Into B, the fast line: owners end at €360.8M (0.99×, €3.3M less than paying it out). Into **A, the high-return line: €382.9M (+€18.8M, best)**. Pay it out: €364.2M (neutral). Split 50/50: €371.9M. The instinct (the fast line) is the worst option. Each euro in A is worth about €2.88; in B about €0.67. (No size question here: all options are within about 5% of today.)
2. **Fix the return or push the growth (ranked by the value of B, today €66.7M).** Double growth to 8%: **€0 (0×)**. Halve growth to 2%: €75.0M (1.1×). **Lift ROIC to 14%: €166.7M (2.5×, best)**. Lift ROIC to 9%: €83.3M (1.25×).
3. **When growth stops mattering (B at 10% ROIC, worth €100.0M).** Double growth: €100.0M (1.0×). Stop growing: €100.0M (1.0×). Lift ROIC to 12%: €133.3M (1.33×). **Lift ROIC to 12% and double growth: €200.0M (2.0×, best).** Growth multiplies the spread; at zero spread it multiplies nothing.

## Evidence
- **The formula and its reading.** The value-driver formula and the rule "growth only creates value when ROIC exceeds WACC" are standard in *Valuation* (Koller, Goedhart & Wessels). Checked against secondary summaries (a corporate-finance tutoring site and Koller interview notes), not against the book text. *(Wording of the book not yet verified.)*
- **McKinsey, growth vs ROIC.** Jiang & Koller, "How to choose between growth and ROIC", McKinsey, 2007: nonfinancial US companies with a market value above $2B in 1995 and at least ten years listed, followed for the next decade. For companies that already had high ROIC, growing revenue faster than the market delivered more shareholder return than further ROIC gains. For low-ROIC companies, those that raised ROIC earned about 5 to 8 percent more shareholder return than those that did not. *(From search-result summaries of the article; the article page itself could not be loaded. Not yet verified against the full text.)* The earlier piece (Cao, Jiang & Koller, "Balancing ROIC and growth to build value", McKinsey on Finance no. 19, Spring 2006) argues the same: with low ROIC, raising returns creates more value than growth.
- **Koller on the cost of capital.** Reported (secondary summary) to put the cost of capital at roughly 7% to 12% for large companies, while returns on capital vary far more. *(Not yet verified; and not applicable to a venture-stage company, whose investors expect much more.)*
- **Capital allocation, Singleton.** Thorndike (*The Outsiders*, Harvard Business Review Press, 2012) tells of Henry Singleton at Teledyne, who between 1972 and 1984 bought back about 90% of the company's shares, in about eight tender offers, when buybacks were seen as a sign of weakness; earnings per share rose about 40-fold from 1971 to 1984. *(Figures taken from book summaries and blog posts, not the book: not yet verified.)* Thorndike's framework: a CEO has five uses of cash (invest in the business, acquire, pay dividends, repay debt, buy back stock) and three ways to raise it (cash flow, debt, equity). *(Secondary summaries: not yet verified.)*
- **A named company that destroyed value by growing below the cost of capital.** None verified; omitted rather than guessed.

## Where it breaks
- **Returns are not constant.** The model gives new money the line's average return forever. In reality the marginal return falls as a line saturates, and the true test is the return on the *next* euro.
- **Learning curves.** In hardware, unit costs often fall with cumulative volume, so a line can sit below the hurdle today and still be worth growing if the return really climbs with scale. That is a claim to test, not assume.
- **Venture finance.** Early-stage investors expect returns far above 10%, and a young company's ROIC is negative or unmeasurable. Use the law as a discipline for *when* growth capital is released, not as a number for the first two years.
- **Options and strategy.** A sub-hurdle line may protect an option (a platform, a customer relationship) worth more than its own ROIC. Name it and price it.
- **Accounting.** ROIC depends on what counts as capital (leased equipment, capitalised R&D, grants). Compare like with like.
- **Fragile near the limit.** As growth approaches the cost of capital, the formula swings wildly; the model caps growth below it.

## Application question (graded on rubric B)
> It is early 2029. Your company has one product in production; its return on capital is still clearly below what your investors expect. A signed order book would let you double capacity next year with a new €15M round. Separately, your pilot customers ask for a product variant that needs about €3M of tooling and would earn a return well above the cost of capital.
> 1. Which law governs this choice, and what does it say about "double the capacity" at today's return?
> 2. Size it roughly (no calculation needed: use the lab's curve): what happens to value if you double volume at today's return, and what if you lift the return first?
> 3. What do you fund first, and what concrete test (a number and a date) releases the growth money?
> 4. Where could this law mislead you in a young hardware company?

Answer in under 300 words.

## Takeaways
1. Growth creates value only when return on capital beats the cost of capital. Equal: it adds nothing. Below: it destroys value.
2. Give the next euro to the biggest gap between return and cost of capital, not to the fastest growth. If nothing beats the hurdle, return the cash.
3. Fix the return before you grow: lifting a sub-hurdle line from 8% to 14% is worth 2.5×; doubling its growth is worth zero.
4. Capital allocation is the CEO's core job: every use of cash (invest, acquire, repay debt, buy back, pay out) faces the same hurdle.

## Sources
- Koller, T., Goedhart, M. & Wessels, D. *Valuation: Measuring and Managing the Value of Companies* (McKinsey & Company; Wiley, multiple editions). Formula and rule read via secondary summaries: Varsity Tutors, "Corporate finance: value drivers", https://www.varsitytutors.com/practice/subjects/corporate-finance/lessons/value-drivers ; Antoine Buteau, "Lessons from Tim Koller", https://www.antoinebuteau.com/lessons-from-tim-koller/ ; The Compounding Tortoise, "McKinsey's first principles of valuation", https://thecompoundingtortoise.substack.com/p/mckinseys-first-principles-of-valuation
- Jiang, B. & Koller, T. (2007). How to choose between growth and ROIC. McKinsey, https://www.mckinsey.com/capabilities/strategy-and-corporate-finance/our-insights/how-to-choose-between-growth-and-roic (via search summary).
- Cao, B., Jiang, B. & Koller, T. (2006). Balancing ROIC and growth to build value. *McKinsey on Finance*, 19, 12-16, https://www.mckinsey.com/capabilities/strategy-and-corporate-finance/our-insights/balancing-roic-and-growth-to-build-value (via search summary).
- Thorndike, W.N. (2012). *The Outsiders: Eight Unconventional CEOs and Their Radically Rational Blueprint for Success*. Harvard Business Review Press. Singleton figures via Shortform summary, https://www.shortform.com/blog/henry-singleton/ (secondary).
