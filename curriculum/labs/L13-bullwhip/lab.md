---
id: L13
title: The bullwhip effect: why small changes in demand become big swings in orders
areas: [systems, operations]
difficulty: 1300
phase: 3
sim: labs/bullwhip.html
cards: [sys-001, sys-002, sys-003, sys-004]
---

# L13. The bullwhip effect: why small changes in demand become big swings in orders

## Goal
After this lab you can decide **how to run orders through a chain of customers and suppliers**: which fix calms the swings most, how to read the orders you receive, and what to do when everyone panics in a shortage.

## The principle
**The bullwhip effect:** in a supply chain, small changes in what end customers buy become larger swings in orders at every step upstream. Orders are more volatile than sales, and the volatility grows the further you are from the consumer. Jay Forrester described the pattern in *Industrial Dynamics* (MIT Press, 1961), which is why it is also called the Forrester effect. The name "bullwhip" came later from industry; Procter & Gamble used it for its diaper chain.

**Why it happens (Lee, Padmanabhan & Whang, 1997):** four operational causes, each a reasonable reaction to what a single step can see.
1. **Demand signal processing.** Each step forecasts from the orders of its direct customer, not from consumer sales, so a small rise becomes a larger forecast and a larger order.
2. **Order batching.** Ordering in lots (to save freight or paperwork) makes orders lumpy.
3. **Price swings.** Promotions make buyers stock up and then stop buying.
4. **Rationing and shortage gaming.** When supply looks short, buyers order more than they need to get a larger allocation; when supply recovers, the orders vanish.

Add **delays** (shipping and order time) and **over-reaction** (Sterman's beer-game players misjudged the feedback from their own orders). Each step amplifies, so the effect compounds.

**The cure in one line:** make every step plan from the same real demand, and shorten and smooth the rest.

## The ideal and the trade-offs
**The goal is not zero swing.** It is orders at your supplier that follow real consumer demand, with a stock cushion sized to genuine noise, at an acceptable cost of information-sharing, speed and lots.

**What to aim for:**
- Plan from **end-customer sell-through**, not from the order book.
- Smooth the forecast: react to the **trend, not the week**.
- Shorten delays and lot sizes where it is cheap to do so.
- In a shortage, **allocate by past sales** and do not pad.

**Rules of thumb:**

| Situation | Do | Why |
|---|---|---|
| Normal operation | Plan from shared sell-through; forecast over several times the total delay | Removes the cause (each step sees only its neighbour) |
| Order swings, tempted to add stock | Fix information first; stock is insurance for noise | More cushion means more to rebuild when the forecast rises |
| Shortage news | Allocate by past sales; do not pad; check orders against sell-through | Padded orders disappear when the shortage ends, leaving a glut |
| Very long delays (months) | Treat orders you receive as a noisy signal; wait for sell-through | The longer the delay, the more the swing grows |

| Lever | Effect in the model (swing at the supplier) | Cost and catch |
|---|---|---|
| **Share real sell-through** | Largest: 10× to 2× (about 5× calmer) | Needs trust and contracts; partners must share data; cheap once agreed |
| **Halve shipping delay** | Medium: 10× to 7× (about 1.4×) | Often costly (air freight, nearshoring, local stock) |
| **Smaller lots** | Small here: 10× to 8.8× (about 1.1×); bigger when lots exceed a week of sales | More orders and shipments; needs cheap electronic ordering |
| **Smooth your own forecast** | Medium: 20× to 7× (about 2.9×) for the step that does it | Free; slow to notice a real, lasting shift |
| **More safety stock** | **Worse:** 10× to 15× | Ties up cash; hides the cause |
| **Allocate by past sales, no padding (shortage)** | Medium: 36× to 16× (about 2.3×) | Customers may complain; needs a credible policy |

**Founder rule:** a hardware startup usually has few steps (maybe none) between itself and the consumer and long component lead times. Treat orders as a signal with a lag; plan from the pilots' real usage and your own sell-through; during a shortage, do not copy the panic.

## Tests (in the simulation; answers for the teacher)
Setting: four steps (retailer, distributor, Viktor's factory, component supplier); consumers buy 100 a week, +10% from week 5; 2-week shipping and a 1-week order delay; each step orders up to a stock target built from a smoothed forecast. Metric: order swing at the supplier (highest minus lowest weekly order after the step) relative to the 10-unit real change.
1. **One change.** Today 10× swing. Share sell-through: **2×, 5× calmer** (factory stock swing 1.4 to 0.5 weeks of sales). Halve shipping: 7× (1.4×). Smaller lots: 8.8× (1.1×). More safety stock (1.5 weeks everywhere): **15×, worse**. Best: share data. The instinct (safety stock) is wrong.
2. **Purchasing manager's forecast.** Today 20× (last two weeks). Average the last quarter (about 12 weeks): **7×, 2.9×**. Month: 10× (2×). Last week only: 28× (0.7×). A half-year average would reach 6×: the gain flattens. Best: quarter.
3. **Shortage.** Retailers over-order by 40% for 8 weeks. Face value: 36× (peak order 360 a week against 110 real). **Check against sell-through and allocate by past sales: 16×, about 2.3× calmer** (stock swing 2.5 to 2.0 weeks). Pad +50%: 54× (0.7×). Two-week buffer: 42× (0.9×). Best: allocate.

## Evidence
- **Procter & Gamble and Hewlett-Packard (Lee, Padmanabhan & Whang, *Sloan Management Review*, 1997).** Retail diaper sales moved modestly; distributors' orders moved more; P&G's orders to its suppliers, such as 3M, moved more still. HP showed the same pattern for printers between a big reseller, HP's printer division and its integrated-circuit division. *(The article's own numbers are not reproduced here; not yet verified.)*
- **Four causes and remedies (Lee, Padmanabhan & Whang, *Management Science*, 1997).** The paper names demand signal processing, the rationing game, order batching and price variations. A course summary of the remedies reads: share demand data, cut ordering costs, stabilise prices, allocate scarce supply by past usage rather than by current orders.
- **Beer game (Sterman, *Management Science*, 1989).** In a simulated distribution system with several actors, delays and feedback, subjects' decisions combined with the structure to produce dynamics far from optimal. Sterman's explanation: an anchoring-and-adjustment heuristic that fails to account for the effect of decisions already taken (the "misperception of feedback"). Later work reports that practice can improve performance (Fu & Gonzalez, 2006; Martin, Gonzalez & Lebiere, 2004), so the effect is common, not fixed. *(From the abstract and secondary summaries; not read in full.)*
- **Real component shortage, then glut (semiconductors, 2020-2023).** Chip lead times averaged 26.8 weeks in August 2022 (Bloomberg, via Susquehanna), and chip inventories were high; Jefferies said an inventory correction had started and would likely last through the first half of 2023. An industry write-up says that during the shortage buyers ordered the same parts from several suppliers, in some cases three to five times what they needed, and that by the second half of 2023 many firms held large surplus stock, with write-offs. A Bain partner is reported (via CNBC; page blocked, not yet verified) as describing a strong bullwhip effect for chipmakers.
- **How big can the distortion be?** One secondary page claims a 5% change in point-of-sale demand can be read as a change of up to 40% upstream (not yet verified against the primary source).

## Where it breaks
- **Demand really jumps.** A growing startup may have a true step change; smoothing and allocation by history can starve genuine growth. Reset the baseline as soon as sell-through confirms the new level.
- **Few steps.** If you sell direct or through one channel partner, the effect is smaller; the supplier's lead time is the main amplifier.
- **Real scarcity.** If supply is truly short, each buyer's padding is individually rational (that is the rationing game); the fix is a system rule (allocation, shared data), not a personal one.
- **Stylised model.** The page is deterministic and smooth; real orders include noise, promotions and capacity limits. The sizes (10×, 36×) are illustrative, shaped after the pattern, not measured. How large the amplification is in aggregate industry data is a separate question (not yet verified).
- **Information sharing is not free.** Partners may refuse to share sell-through, or share it late.

## Application question (graded on rubric B)
> It is mid-2028. Your product sells through two distributors; your contract factory buys one key component, with a lead time of several months, from a single supplier. After a trade show, one distributor doubles its order for next quarter and says it wants to "secure allocation". Your supplier offers a place in its queue only if you commit to a 12-month volume now.
> 1. Which law is at work, and why can the orders you see be much bigger than what end customers will buy? Size the gap roughly (small, 2×, 10×) and say what happens to orders when the scare passes.
> 2. What do you do with the distributor's order and the supplier's offer? Give the policy and the first concrete steps.
> 3. Where could this law mislead you here?

Answer in under 300 words.

## Takeaways
1. A 10% rise in consumer demand became orders swinging about 10× as much at the component supplier in the model; each step adds to the swing.
2. The structure causes it (delays, forecasting from orders, lots, over-reaction, shortage gaming), so reasonable people produce it.
3. Fix information first: plan from real sell-through. Then smooth, shorten, shrink lots. More safety stock does not cure it and here made it worse.
4. In a shortage, do not join the wave: allocate by past sales, check orders against sell-through, and do not double-order.

## Sources
- Forrester, J.W. (1961). *Industrial Dynamics*. MIT Press. (Origin of the pattern; credited via https://en.wikipedia.org/wiki/Bullwhip_effect. Book not read: not yet verified.)
- Lee, H.L., Padmanabhan, V. & Whang, S. (1997). The bullwhip effect in supply chains. *Sloan Management Review*, Spring 1997. https://sloanreview.mit.edu/article/the-bullwhip-effect-in-supply-chains/ (P&G and HP examples; volume and pages not yet verified.)
- Lee, H.L., Padmanabhan, V. & Whang, S. (1997). Information distortion in a supply chain: the bullwhip effect. *Management Science*, 43(4), 546-558. https://ideas.repec.org/a/inm/ormnsc/v43y1997i4p546-558.html
- Course summary of the four causes and remedies (Penn State Smeal Center for Supply Chain Research reading), hosted at https://courses.ischool.berkeley.edu/i290-4/s03/readings/bullwhip.htm
- Sterman, J.D. (1989). Modeling managerial behavior: misperceptions of feedback in a dynamic decision making experiment. *Management Science*, 35(3), 321-339. Abstract: https://jmvidal.cse.sc.edu/lib/sterman89a.html
- Beer distribution game description: https://en.wikipedia.org/wiki/Beer_distribution_game
- Bullwhip effect overview (secondary): https://en.wikipedia.org/wiki/Bullwhip_effect
- The Register (9 Sept 2022), chip delivery times, citing Bloomberg/Susquehanna and Jefferies: https://www.theregister.com/2022/09/09/chip_delivery_times_down/
- Altium resources, on phantom demand and the surplus after 2020-2023: https://resources.altium.com/p/misguided-orders-semiconductor-market
- CNBC (28 Jul 2023), shortage to glut: https://www.cnbc.com/2023/07/28/how-the-world-went-from-a-semiconductor-shortage-to-a-major-glut.html (access blocked; reference via a search summary only, not yet verified).
