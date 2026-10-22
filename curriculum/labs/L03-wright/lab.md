---
id: L03
title: Wright's law: how unit cost falls with experience
areas: [unit_econ, pricing]
difficulty: 1200
phase: 1
sim: labs/wright.html
cards: [unit-001, unit-002, unit-003, unit-004]
---

# L03. Wright's law: how unit cost falls with experience

## Goal
After this lab you can decide **how to bring unit cost down** (redesign, volume or a cheaper start), **how far to cut a pilot price**, and **how ambitious a target cost you can reach inside a funding round**.

## The principle
**Wright's law** (T.P. Wright, "Factors affecting the cost of airplanes", Journal of the Aeronautical Sciences, 1936): unit cost falls by a roughly fixed percentage each time cumulative output doubles.

> **cost of unit n ≈ cost of unit 1 × n^(−b)**, where each doubling multiplies cost by the "learning rate" (80% = cost falls 20% per doubling).

Henderson's **experience curve** (Bruce Henderson, Boston Consulting Group, 1960s) turned this into strategy: price ahead of today's cost to win share, then ride the cost down the curve.

**Why it happens:** workers and engineers find faster methods, designs are simplified, scrap falls, suppliers improve, and bigger production runs spread fixed costs. The curve is made of many small improvements, not one big one.

| Learning rate | Cost per doubling | Units to cut cost 4× (€4,000 to €1,000) |
|---|---|---|
| 80% | −20% | about 74 |
| 85% | −15% | about 370 |
| 90% | −10% | about 9,100 |

The last column is the lesson: a few points of learning rate change the units needed by a factor of 5 at one step (80% to 85%) and over 100 across the whole range.

## The ideal and the trade-offs
**The goal is not the lowest cost; it is the cheapest route to a cost that makes the business work, inside the cash you have.** Cumulative units are the currency: you pay for them in losses or in delay, and you get paid in lower cost.

**Rules of thumb**
- Start with the **units you must build** to reach target cost: (first-unit cost ÷ target cost)^(1 ÷ b). Then divide by the build rate to get months, and multiply by team cost to get cash.
- Each **halving of cost** needs the same extra number of doublings (about 4.3 at 85%, which is about 19× more units). Deep targets are far more expensive than they look.
- **Price forward only until demand fills your capacity.** Below that price, you give away margin and learn nothing extra.

| Lever | Effect on time to target | Cost and catch |
|---|---|---|
| **Better learning rate** (design for manufacture, process engineering) | Largest: sits in the exponent (85% to 80% cuts units needed 5×) | Engineering time up front; the improvement must be real, so test early |
| **Cheaper first design** | Medium (€4,000 to €3,000 cuts units about 3.4×) | May cost performance or delay launch |
| **More volume** (a big early order) | Speeds the clock only: 3× volume is 3× faster, units needed unchanged | Hard to win; ties up capacity; but helps cash |
| **Forward pricing** (cut price to pull volume) | Large until the line is full, none after | Margin loss and cash burn; needs real demand response |
| **A less ambitious target cost** | Largest by far (each halving is about 19× units) | May leave a thin margin |

**Founder rule:** work out the number of units to your target before you promise it. If that number is beyond what you can sell in the round, the target belongs to the next round.

## Tests (in the simulation; answers for the teacher)
Setting: first units €4,000, target €1,000, 85% learning rate (about 370 units, 8.5 doublings), 10 pilot orders a month at €4,000, line capacity 30 a month, team cost €50k a month. Demand rises about 15% for each 10% price cut (assumption).
1. **Fastest way down.** Big early order (volume 30 a month): 12.3 months (3.0×). **Redesign for manufacture (80% curve): 74 units, 7.4 months (5.0×).** Cheaper first unit (€3,000): 108 units, 10.8 months (3.4×). Today: 37 months. The instinct (volume) is last. The learning rate sits in the exponent.
2. **Pilot price.** Cash to reach €1,000: €4,000 about €851k (37 months); €3,000 about €572k (24 months); **€2,000 about €394k (13 months, 2.2× less)**; €1,000 about €725k (12.3 months). The best price is the one where demand just fills the line (about €1,900 here), not target cost.
3. **How ambitious a target.** At €2,000 pricing (28 units a month) with a 24-month round: €1,500 takes 2.3 months (66 units); **€1,000 takes 13 months (370 units)**; €700 takes 60 months (1,700 units); €500 takes 251 months (7,100 units). Best: €1,000, the lowest target that fits.

## Evidence
- **Wright's aircraft data.** Wikipedia's articles on experience curve effects and the learning curve describe Wright's 1936 finding as about 80%, that is, about 20% lower unit labour or cost per doubling of aircraft built. Another source I read describes labour falling 10-15% per doubling and says Wright used a cumulative-average form (not yet verified against the paper itself, so treat "20% for aircraft" as the commonly cited figure). NASA-cited progress ratios in the Wikipedia article put aerospace at about 85%, shipbuilding at 80-85% and raw materials at 93-96%.
- **Solar PV modules.** Our World in Data (ourworldindata.org/learning-curve) gives about 20% per doubling of cumulative capacity over more than four decades (one calculation 19.3%; an average of experience-curve studies 20.2%). Richard Swanson of SunPower documented the same "80% learning curve" over three decades (Sahoo & Reichelstein, Stanford Energy Journal, 2015). The curve was not exact: modules sat above it in 2008-09 (a polysilicon shortage) and below it from 2011, and the authors ask whether overcapacity played a part.
- **Lithium-ion cells.** Ziegler & Trancik (Energy & Environmental Science, 2021, 14, 1635-1651): from 1992 to 2016 the real price per unit of energy fell about 13% a year, or about 20% per doubling of cumulative market size for all cells (24% for cylindrical cells), and about 97% since 1991. Counting energy density as part of the service raises the rates to 27% and 31%.
- **Not all learning is learning.** OWID notes that causality can run both ways (falling prices raise sales), and lists factors beyond experience (bigger factories, R&D, efficiency). Studies of WWII production, where demand was driven by the war, still found cost falling with experience.
- **A curve that was overtaken.** Solyndra (CIGS solar modules, US Department of Energy loan guarantee of $535 million) filed for bankruptcy in August-September 2011. Wikipedia attributes this to competition from crystalline silicon makers after polysilicon prices fell about 89% between 2009 and mid-2011. Riding your own curve does not help when a rival technology descends a steeper one. (Source read: Wikipedia, Solyndra; not yet verified against primary reporting.)
- **Strategy claims.** BCG research in the 1960s and 1970s found effects of 10-25% across industries; a BCG semiconductor study found about 25% per doubling (both via Wikipedia, not yet verified against BCG's own papers). Pre-emptive pricing and expansion has been criticised, and curves can be cut short by obsolete processes, competitors' responses and price wars.

## Where it breaks
- **Learning is not automatic.** It needs people who measure, change and standardise. Some products (bicycles, fridges, coal plants, per OWID) did not follow the law.
- **A new technology resets the curve.** Rivals who start on a different technology can undercut you (Solyndra).
- **Product changes reset learning.** Each redesign throws away some of the experience; frequent changes slow the curve.
- **Volume is not experience.** Scale economies, design changes and learning are hard to separate. Do not assume that a big order gives the same cost-down as the same number of units built over time with improvements.
- **Demand response is a guess.** The pilot-price result depends on how many customers a price cut brings, and on rivals not matching.
- **The first-unit cost is slippery.** "First unit" in hand-built prototypes is not the first unit of a production line; ask what is actually being measured.

## Application question (graded on rubric B)
> It is mid-2027. Your first prototype units cost about 8 times your target cost. Investors ask when you will reach that target, and a rival startup with a different technology says it will beat it.
> 1. Roughly how many doublings of cumulative output do you need, and what does that mean in units? Assume your learning rate is somewhere between 80% and 90% and size the range (no calculation needed: use the curve).
> 2. Which lever do you pull first, how do you price your first customers, and what must you do before you promise the date?
> 3. Where could Wright's law mislead you here?

Answer in under 300 words.

## Takeaways
1. Cost falls by a fixed percentage each time total units built double. Solar modules and lithium-ion cells have fallen about 20% per doubling; use 10-20% for hardware planning and test it early.
2. Lower the units you need (learning rate, starting cost) before you raise the speed. A big order only speeds up the clock.
3. Cut the pilot price until demand fills capacity, then stop. Neither price-at-cost nor price-at-target is the best.
4. Every halving of cost needs about 19 times more units at an 85% curve. Turn a target cost into units and months before you promise it, and watch for a rival technology that overtakes your curve.

## Sources
- Wright, T.P. (1936). Factors affecting the cost of airplanes. *Journal of the Aeronautical Sciences*, 3(4), 122-128. (Referenced, not read; figures via secondary sources.)
- Henderson, B.D. (1968). *Perspectives on Experience*. Boston Consulting Group. (Referenced via Wikipedia; not read.)
- Wikipedia, "Experience curve effects" and "Learning curve" (read; used for the 80% aircraft figure, BCG ranges, NASA progress ratios and criticisms).
- Our World in Data, "Learning curve" (ourworldindata.org/learning-curve), read.
- Sahoo, A. & Reichelstein, S. (2015). Are the recent declines in solar PV module prices sustainable? *Stanford Energy Journal*, Issue 6 (via the Stanford GSB page, read).
- Ziegler, M.S. & Trancik, J.E. (2021). Re-examining rates of lithium-ion battery technology improvement and cost decline. *Energy & Environmental Science*, 14(4), 1635-1651 (abstract read via MIT DSpace).
- Wikipedia, "Solyndra" (read).
- Abernathy, W.J. & Wayne, K. (1974). Limits of the learning curve. *Harvard Business Review*, 52(5), 109-119. (Citation checked; content not yet verified.)
