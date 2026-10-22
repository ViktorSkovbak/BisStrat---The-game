---
id: L04
title: Power-law returns: why a fund needs fund-returners
areas: [venture, forecasting]
difficulty: 1250
phase: 1
sim: labs/powerlaw.html
cards: [vc-001, vc-002, vc-003, vc-004]
---

# L04. Power-law returns: why a fund needs fund-returners

## Goal
After this lab you can judge whether a company can **return a venture fund**: which kind of bet a fund wants, how large an exit that takes, and what you must show to be fundable.

## The principle
**Venture returns follow a power law:** a small share of investments returns most of a fund's money, and a large share loses money. Kerr, Nanda and Rhodes-Kropf (*Journal of Economic Perspectives*, 2014) describe new-venture success as low in probability, extremely skewed and unknowable until the money is committed. Investing is therefore experimentation: many cheap tests, a few outliers.

**"Return the fund" maths.** For one company to repay the whole fund by itself:

> **exit value needed = fund size ÷ (ownership at entry × share kept after later rounds)**

| Fund | Ownership at entry | Kept after later rounds | Ownership at exit | Exit needed |
|---|---|---|---|---|
| €60M | 12% | 50% | 6% | **€1.0B** |
| €60M | 15% | 50% | 7.5% | €0.8B |
| €200M | 12% | 50% | 6% | €3.3B |

The three terms are the assumptions in the simulation (a seed fund of about 25 investments buying roughly 10-15%; later rounds keeping about half). *(The seed ownership range comes from the brief; the dilution of about half is an assumption (not yet verified).)*

**Why it happens:** outcomes are capped at the bottom (you lose what you put in) but not at the top (a winner can return 50× or 100× its cost). With a cap on losses and none on wins, a few winners dominate the sum.

## The ideal and the trade-offs
**The goal is not a high hit rate.** It is a portfolio in which at least one or two companies could, on a credible path, return the fund, held by enough shots on goal that the fund usually gets one.

**Rules of thumb**
- Judge a bet by **chance × size of the win**, and by whether the win would move the whole fund. A 10% chance of a fund-making win beats a likely small win.
- A company whose success case is below the fund-returner bar is a different asset class for this fund: a good business, not a venture investment.
- Expect about half or more of the investments to lose money. Do not read a loss as a mistake; read the portfolio.

| Lever | Effect on the chance a company returns the fund | Cost and catch |
|---|---|---|
| **Bigger success case** (market evidence, bigger buyer pool, larger platform) | Largest when the case sits below the bar | Needs real evidence (customer data, signed pilots), not slides |
| **Lower risk** (pilots, signed customers, proven technology) | Medium: multiplies the chance of working, no more | Costs time and cash; helps only once the win is large enough |
| **Cheaper round** (more ownership for the same money) | Small-medium | Costs the founder ownership; weakens later rounds |
| **Smaller, faster plan** (likely modest exit) | Negative for a venture fund | May be the right plan for a founder who does not want venture money |

**Founder rule:** before you take venture money, check that your plan has a credible path to the exit the fund needs. At seed terms and a €60M fund that is on the order of €1B. If it does not, use grants, customers or debt instead of equity.

## Tests (in the simulation; answers for the teacher)
Setting: €60M seed fund, 25 investments, buys 12% at entry and keeps about 6% at exit. Seeded Monte Carlo, 10,000 simulated investments per evaluation, fat-tailed payoff.
1. **Which company does the fund want?** Today: 25 steady profitable businesses (90% chance of 1.3×): typical fund 1.1×. A likely 3× (75% chance): 2.3× (**2.0×** better). A 10% chance of 100× (about 50× after dilution): **4.0×** (3.5× better). Best: the moonshot. The instinct (the safe one) is the worst. Catch: about 1 fund in 13 gets no hit at all.
2. **How big an exit is enough?** Bar = €60M ÷ 6% = **€1.0B**. €250M returns 0.25× the fund, €600M 0.6×, **€1.2B 1.2×**, €3B 3.0×. Best: the smallest exit that returns the fund, €1.2B.
3. **What must you show?** Company with a 15% chance of working and a typical success case of €400M (chance of returning the fund 2.3%). Bigger market evidence (€800M): **6.0%** (2.6×). Lower risk (25% chance): 3.9% (1.7×). Cheaper round (15% entry): 3.3% (1.4×). Smaller, faster plan (30% chance, €250M): 1.9% (0.8×). Best: bigger evidence.

## Evidence
- **Horsley Bridge data, via Benedict Evans.** Evans (*In praise of failure*, 2016) reports data on just over 7,000 investments made in 1985-2014 by funds in which Horsley Bridge (a fund-of-funds investor) invested: around half returned less than the original investment; 6% returned 10× or more, and those produced about 60% of total returns. *(The original a16z presentation of 2014-2015 was not read; the figures come from Evans's own post. The claim that the best funds had more losing deals comes only from a search summary (not yet verified).)*
- **Correlation Ventures, via Seth Levine (2014).** Over 21,000 financings: about 65% returned less than 1× the capital, about 10% returned 5× or more, about 4% returned 10× or more. The post prints the years with a typo, so the period is (not yet verified). That the data covers exited companies and leans toward better funds is Levine's caveat as relayed by a search summary (not yet verified).
- **Correlation Ventures, exits only (LifeSci VC, 2013).** 7,976 realised deals with exits in 2003-2012: 39% went out of business, 29% exited below the invested capital, 32% returned more than 1×. Different data and definition from the 65% above, so the loss share depends on the cut: about half to two thirds.
- **Kerr, Nanda & Rhodes-Kropf (2014).** The abstract states that the probability of success is low, extremely skewed and unknowable until an investment is made, and that funding decisions are made by a few investors, shaped by incentive and coordination problems. *(Only the abstract was read; the paper's own figures and examples are (not yet verified).)*
- **How the simulation is calibrated.** About 55% of investments lose money (inside the half-to-65% range above), winners follow a truncated Pareto, and the 4-5% that return 10× or more bring about 60% of all money, in line with the Evans figure. The typical simulated fund returns about 2.1× gross: an illustrative number, not a benchmark (not yet verified).

## Where it breaks
- **Selection and luck:** the data show a pattern across funds, not that you can pick winners. The power law is also what makes skill hard to see in a small fund.
- **Strategies built on a different shape:** growth equity, buyouts and debt do not follow the same power law. The ideal here is for seed and early-stage equity.
- **Fund size sets the bar.** A €20M fund can be returned by a €150-300M exit; a €1B fund needs a company worth tens of billions. Small funds can fit niche, capital-light companies.
- **Dilution and preferences:** liquidation preferences, pro-rata follow-ons and a down round change who gets what. The model keeps one flat "share kept".
- **Fat tails are not guaranteed:** if the winners of your market are capped by market size, the fund's maths may not hold. This is the question the partner is asking you.
- **Fees, time and the net result:** the multiples here are gross. Returns to the fund's own investors are lower after fees and carry.

## Application question (graded on rubric B)
> It is early 2027. You are raising a first round for your new venture-scale hardware company and a €60M seed fund (about 25 investments, buying about 12% at entry) has asked for a partner meeting.
> 1. What exit value does your company need to deliver for this fund to say it returns the fund? Size it roughly (no calculation needed). Does your plan clear it?
> 2. What do you show the partner, and in what order, so that the fund sees a credible path? Give the policy, not only the pitch.
> 3. Where could this logic mislead you here? Is venture money the right money for your company?

Answer in under 300 words.

## Takeaways
1. Returns follow a power law: in the Horsley Bridge data about half of ~7,000 investments lost money, while the 6% that returned 10× or more produced about 60% of the money.
2. Each investment needs a path to returning the fund: exit needed = fund size ÷ (ownership at entry × share kept after later rounds). For €60M at 12% entry and half kept, that is about €1B.
3. The safe business is the wrong bet for a venture fund: chance × size of the win decides, as long as there are enough shots.
4. To be fundable, show the size of the win first. Evidence that the success case clears the bar moves the odds more than lower risk or a cheaper round.

## Sources
- Evans, B. (2016). In praise of failure. ben-evans.com/benedictevans/2016/4/28/winning-and-losing (Horsley Bridge data, 1985-2014; read as HTML).
- Levine, S. (2014). Venture outcomes are even more skewed than you think. sethlevine.com/archives/2014/08/venture-outcomes-are-even-more-skewed-than-you-think.html (Correlation Ventures data).
- LifeSci VC (2013). Correlation's fresh look at venture capital returns. lifescivc.com/2013/11/correlations-fresh-look-at-venture-capital-returns/ (7,976 realised deals).
- Kerr, W.R., Nanda, R. & Rhodes-Kropf, M. (2014). Entrepreneurship as experimentation. *Journal of Economic Perspectives*, 28(3), 25-48. NBER Working Paper 20358, nber.org/papers/w20358 (abstract read as HTML).
