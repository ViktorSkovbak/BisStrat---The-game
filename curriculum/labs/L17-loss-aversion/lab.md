---
id: L17
title: Loss aversion: why losses outweigh gains
areas: [behavioural, pricing]
difficulty: 1250
phase: 4
sim: labs/loss-aversion.html
cards: [beh-001, beh-002, beh-003, beh-004]
---

# L17. Loss aversion: why losses outweigh gains

## Goal
After this lab you can decide **how to word an offer, how to raise a price, and when to stop a failing project**, knowing that people (customers and founders alike) judge outcomes from a reference point and weigh a loss about twice as much as an equal gain.

## The principle
**Prospect theory** (Kahneman & Tversky, *Econometrica*, 1979): people do not value final wealth; they value **gains and losses measured from a reference point** (usually the status quo). The value curve has three features: it is measured from the reference point, it flattens as amounts grow (diminishing sensitivity), and it is **steeper for losses than for gains**.

**Cumulative prospect theory** (Tversky & Kahneman, *Journal of Risk and Uncertainty*, 1992) adds probability weighting (small chances are overweighted, large ones underweighted) and reports the often-cited estimates: curvature about 0.88 and a **loss-aversion coefficient of about 2.25**. A loss of €1 feels about as bad as a gain of €2.25 feels good.

> **value of a gain x = x^0.88; value of a loss x = −2.25 × x^0.88**

**Why it matters for a founder:**
- **Customers:** the same deal can feel like a gain or a loss depending on what they treat as "what I have now".
- **Yourself:** a sunk cost turns "stop" into a realised loss, so you take gambles to avoid admitting it (escalation of commitment, Staw 1976).

| Situation | The reference point is | What stopping or paying feels like |
|---|---|---|
| Customer in a free trial | "I have the product" | Paying is a loss, but so is losing the product; the second is bigger |
| Customer shown a list-price discount | The (believed) list price | A gain, but only if they believe the list price |
| Customer facing a price rise | Today's price | A loss, felt about 2× |
| Founder with €2M spent | "Break even on the project" | Stopping makes a €1.8M loss real; gambling keeps a chance of zero |

## The ideal and the trade-offs
**The goal is not to exploit the bias; it is to stop it from making your decisions for you and to stop your offers from creating needless losses.** For customers, frame from where they already stand and avoid creating losses. For yourself, judge only the future.

| Situation | Aim for | Why |
|---|---|---|
| Converting a user who already has the product | Word the offer around what they keep or lose by stopping (if true) | The loss weighs about 2× the price |
| First-time buyers with no reference | Build a reference first (anchors, comparisons) | Nothing to lose yet; the frame sets the reference |
| Raising prices | Give choice and a gain (a tier), do not take away | A rise is a loss from the old price |
| Stopping or continuing a project | Judge each option as if you inherited it today | Past spending is gone whichever you choose |

| Lever | Effect in the model | Cost and catch |
|---|---|---|
| **Loss framing for users** | About 1.9× more pilots say yes than the plain price | Only honest if they really have something to lose; overuse reads as pressure |
| **Lead with the saving** | About 1.7× | Works best when the cost is clearly tied to the benefit |
| **Discount off a list price** | About 1.1× for a customer who never paid list | Needs a believable list price; better for new buyers |
| **Premium tier instead of a rise** | About 4× fewer customers lost, same extra revenue | Costs product and pricing work; breaks if it strips features from the base plan |
| **Split a rise into slices** | About none (slightly worse) | Each slice is a fresh loss; the order versus one rise is uncertain |
| **Pre-agreed kill criteria** | Removes the sunk-cost pull | Needs discipline before you are in the hole |

**Founder rule:** write the kill criteria (date, threshold, who decides) **before** you spend the money. A person who has already spent €2M will not set them honestly.

## Tests (in the simulation; answers for the teacher)
Setting: 40 pilot customers each saving about €3,000 a year at a €2,000 price; 100 paying customers at €1,000 a month; a product line with €2M already spent. All numbers are from an illustrative model (see Evidence).
1. **The pilot offer.** Plain "pay €2,000" 35% say yes (today); "save €3,000 a year" 60% (1.7×); **"you lose the €3,000 saving if you stop" 67% (1.9×, about €54k a year against €28k)**; "50% off €3,500 list" 39% (1.1×). Best: C. The instinct (discount) is nearly useless for a customer who already uses it free.
2. **Raising the price.** One 10% rise 4.2 of 100 lost (today, €1.26M a year); two 5% rises 4.5 lost (0.9×, €1.26M); **new premium tier, old price kept 1.0 lost (4.1×, €1.31M)**. Best: C. Slicing the rise is the gentle-sounding instinct and does not help.
3. **The €2M product line, judged on cash from here on.** Continue −€40k (spend 1,000, 30% chance of 3,200); **pivot +€300k** (spend 400, 50% chance of 1,400); kill +€200k (salvage). Best: pivot, then kill. Continuing needs a 38% chance just to match killing. The gut scale (sunk cost counted as a loss) ranks continue −1,484, pivot −1,500, kill −1,647: kill comes last on feel, second on cash. At a 35% pivot chance, pivot falls to +€90k and kill wins.

## Evidence
- **Prospect theory, 1979.** Kahneman & Tversky, *Econometrica* 47(2), 263-291. Value is defined on gains and losses from a reference point and is steeper for losses. Reflection effect: a sure €3,000 against an 80% chance of €4,000 is preferred by about 80%; with the signs flipped, only about 8% take the sure loss (via secondary summaries; the original payoffs were hypothetical). *(Figures not yet verified against the paper.)*
- **Cumulative prospect theory, 1992.** Tversky & Kahneman, *Journal of Risk and Uncertainty* 5(4), 297-323 (citation and abstract checked at IDEAS/RePEc). Median estimates of about 0.88 for curvature and **2.25 for loss aversion** are widely reported in course material. *(The 0.88 and 2.25, and the weighting parameters 0.61 and 0.69 used by the model, are not yet verified in the paper itself; one secondary source says the estimates came from a small student sample, also not yet verified.)*
- **Pooled estimates.** Brown, Imai, Vieider & Camerer (*Journal of Economic Literature* 2024; 62(2): 485-516) pool 607 estimates from 150 articles and report a mean loss-aversion coefficient of about 1.95 (interval about 1.8 to 2.1). *(Read through search summaries, not the paper; not yet verified.)* So "about 2×" is the right level; 2.25 is the headline, not a constant.
- **Golf.** Pope & Schweitzer, "Is Tiger Woods Loss Averse?", *American Economic Review* 101(1), 2011, 129-157. About 2.5 million putts by 421 professionals in 239 tournaments, 2004-2009: birdie putts are made about 2 percentage points less often than comparable par putts, after controlling for distance. The authors read par as the reference point: a missed par putt is a loss, a missed birdie putt a smaller gain foregone. They estimate the bias costs the average pro about one stroke per 72-hole tournament. (Wharton Knowledge write-up and search summaries.) An alternative explanation is attention (more focus on par putts), noted in a general encyclopedia article.
- **Escalation of commitment.** Staw, "Knee-deep in the big muddy", *Organizational Behavior and Human Performance* 16(1), 1976, 27-44. In a business-student role play, people committed the most resources to an earlier course of action when they had personally made the failed decision. A later meta-analysis (Sleesman et al., *Academy of Management Journal* 55(3), 2012, 541-562) lists sunk costs and time invested among the factors linked to escalation. *(Sample size and effect sizes not yet verified.)* The rational rule: only prospective costs and benefits matter to the next decision.
- **Robustness.** Gal & Rucker (2018) argue many "loss aversion" effects are better explained by inertia, and Yechiam & Zeif (2025) is listed as a re-meta-analysis titled "Loss aversion is not robust". *(Both only seen as references in an encyclopedia article; not read; not yet verified.)*
- **The model.** The value curve, the loss weight and the probability weights are from prospect theory; the mapping from felt value to "say yes" or "leave" (a logistic with spread 2.5), the churn rate (1.6% per unit of felt pain), the list-price credibility (0.3) and the premium tier's small felt loss (2%) are **assumptions**, not data.

## Where it breaks
- **Small stakes and firms.** Loss aversion may not show up for small payoffs, and B2B buyers are firms with budgets, procurement rules and several decision makers.
- **Framing effects are usually smaller than the model shows.** The page ranks options; it does not predict your conversion. Test with real pilots.
- **The reference point is not fixed.** It can be the status quo, an expectation, a competitor's price or a past price. Check what your customer actually anchors on.
- **Loss framing can look like pressure** and cost trust if it is not true.
- **Discounts do work on first-time buyers** who have no reference price yet. Here the customer already uses the product free.
- **Continuing is sometimes right.** If the chance of success is genuinely above the break-even (38% here), keep going. The test is whether the *future* numbers justify it; the model gives you probabilities, real life does not, so set kill criteria in advance.
- **A pivot can be the same bias in disguise** (reusing sunk assets to avoid admitting failure). It must pass the same forward-only test.

## Application question (graded on rubric B)
> It is mid-2027. Your first three pilot customers have used your prototype free for three months; each says it saves them about 20% of a cost line, and you are about to ask them to pay. Separately, your second product bet is nine months late: you have put €1.5M of seed money into it and your lead engineer says "one more quarter".
> 1. How do you word the paid offer, and why does that wording work (or fail)? Size the effect roughly (no calculation needed).
> 2. What do you do about the late product bet, and what do you write down now so you decide properly in three months?
> 3. Where could loss aversion mislead you here, about your customers and about yourself?

Answer in under 300 words.

## Takeaways
1. Losses weigh about twice as much as equal gains, measured from a reference point. The 1992 estimate is 2.25; later pooled estimates are a little lower.
2. The wording sets the reference point. A customer who already has the product responds most to what they lose by stopping; a discount off a price they never paid moves little.
3. Every price rise is a loss from the old price. Offer a tier customers can step up to rather than taking from them; slicing one rise into two helps little.
4. Sunk costs are gone. Judge each option only on what happens next; if the money already spent changes your answer, that is the bias.

## Sources
- Kahneman, D. & Tversky, A. (1979). Prospect theory: an analysis of decision under risk. *Econometrica*, 47(2), 263-291.
- Tversky, A. & Kahneman, D. (1992). Advances in prospect theory: cumulative representation of uncertainty. *Journal of Risk and Uncertainty*, 5(4), 297-323. https://ideas.repec.org/a/kap/jrisku/v5y1992i4p297-323.html
- Brown, A.L., Imai, T., Vieider, F.M. & Camerer, C.F. (2024). Meta-analysis of empirical estimates of loss aversion. *Journal of Economic Literature*, 62(2), 485-516.
- Pope, D.G. & Schweitzer, M.E. (2011). Is Tiger Woods loss averse? Persistent bias in the face of experience, competition, and high stakes. *American Economic Review*, 101(1), 129-157. Summary: https://knowledge.wharton.upenn.edu/?p=8909
- Staw, B.M. (1976). Knee-deep in the big muddy: a study of escalating commitment to a chosen course of action. *Organizational Behavior and Human Performance*, 16(1), 27-44.
- Sleesman, D.J., Conlon, D.E., McNamara, G. & Miles, J.E. (2012). Cleaning up the big muddy: a meta-analytic review of the determinants of escalation of commitment. *Academy of Management Journal*, 55(3), 541-562.
- Encyclopedia articles on loss aversion, escalation of commitment and sunk cost (en.wikipedia.org), used for caveats and the forward-only decision rule; check against originals.
