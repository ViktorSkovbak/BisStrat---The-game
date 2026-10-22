---
id: L12
title: The winner's curse: why the winning bid is usually too high
areas: [exits, behavioural]
difficulty: 1300
phase: 4
sim: labs/winners-curse.html
cards: [exit-001, exit-002, exit-003, exit-004]
---

# L12. The winner's curse: why the winning bid is usually too high

## Goal
After this lab you can decide **how far below your own estimate to bid** when several buyers are guessing the same uncertain prize, which sale process to push for as a buyer, and why **more bidders** are the seller's best lever when you sell your own company.

## The principle
**The winner's curse.** When bidders each form a noisy estimate of the same value, the highest bid comes from the highest estimate, and the highest estimate is, on average, an overestimate. Winning is therefore bad news about your own estimate. A bidder who bids what they think the prize is worth makes money on paper and loses money on average.

First described for oil-lease auctions by Capen, Clapp & Campbell (*Journal of Petroleum Technology*, 1971). Thaler's column "Anomalies: The Winner's Curse" (*Journal of Economic Perspectives*, 1988) brought it to economists.

**Why it happens:** three ingredients, all needed: (1) the prize has roughly **one true value** that nobody knows exactly (a **common value**: oil in the ground, a supplier's real earning power); (2) each bidder holds a **noisy estimate**; (3) the **highest bid wins**. Remove any one and the curse weakens: if every bidder had the same information, there would be no spread of estimates; if the value were purely personal taste, there would be nothing to overestimate.

**What the winner must do:** bid *conditional on winning*. Ask "if I am the highest bidder, what does that say about my estimate?" and shade the bid accordingly (Capen et al. and the later auction literature: the more bidders, the more shading).

| Setting | Break-even shade* (the bid below your estimate where a win stops being a loss) |
|---|---|
| 2 bidders | about 8% |
| 4 bidders | about 15% |
| 6 bidders | about 20% |
| 10 bidders | about 27% |

*In this lab's model: estimates ±25% off, other bidders shave 15%, the prize is worth 20% more to you than to the market. Illustrative, not data.

## The ideal and the trade-offs
**The goal is not to win.** It is to win only at prices where winning pays. Winning a lot of auctions is a warning sign.

| Situation | What to do | Why |
|---|---|---|
| Value is easy to judge (low uncertainty), few rivals | Bid close to your estimate (shade ~10%) | Little noise, small curse (at ±10% an honest bid loses about €0.07m per win in the lab) |
| Value is hard to judge (deep tech, early-stage, new market), several rivals | Shade hard (about 30%) and accept winning rarely | The winner is usually the biggest overestimate |
| Many bidders and thin edge | Do not bid, or change the process | Expected gain per auction tends to zero (about €0.03m with 10 bidders vs €1.16m with 2 in the lab) |
| You are the seller | Create competition | Same effect, mirrored: the highest of many noisy bids is high |

| Lever (as buyer) | Effect | Cost and catch |
|---|---|---|
| **Shade the bid** | Turns losses into small gains | You win less often; shading 50% in the lab means winning about 1% of auctions |
| **Fewer bidders** (pre-emptive offer, narrow round, off-market deal) | Largest: 2 bidders vs 10 raised expected gain about 40× | Needs a real reason for the seller to say yes (speed, certainty, a relationship) |
| **Better information** (own diligence) | Medium: about 4× in the lab | Costs money and time; cannot remove all noise |
| **A real edge** (synergies only you can use) | Large; the only source of lasting profit | The edge must be real, not a story you tell yourself after bidding |
| **Walk away** | Zero loss | Feels like losing |

| Lever (as seller) | Effect | Cost and catch |
|---|---|---|
| **Add bidders** | Large: 8 bidders vs one inbound buyer lifted the expected price about 35% in the lab | Banker fees, leaks, distraction, risk of a failed process |
| **Negotiate hard with one buyer** | Smaller than adding one bidder (Bulow & Klemperer 1996) | Needs skill and a credible alternative |
| **Take the inbound offer** | Lowest price | Fast and certain |

**Founder rule:** when you buy, assume you are the biggest optimist in the room and shade until you would still be glad to have won; when you sell, never negotiate with a single interested buyer if you can get a second one in the room.

## Tests (in the simulation; answers for the teacher)
Setting: the supplier is worth €10m to a typical buyer and €12m to Viktor; estimates are ±25% off; other bidders bid 15% under their estimate.
1. **How far below your estimate?** 6 bidders. Honest estimate: wins 62%, −€1.65m per win, **−€1.03m** per auction ✗ (the instinct). Shade 10%: −€0.38m. **Shade 30%: +€0.14m** ✓. Shade 50%: +€0.02m (too timid). At ±10% uncertainty the honest bid loses only €0.07m per win.
2. **Which process?** 30% shade throughout. **Pre-empt (2 bidders): +€1.16m** ✓; narrow round (4): +€0.33m; broad auction (10): +€0.03m; broad plus deep diligence (20% shade): +€0.11m. Break-even shade rises 8% → 15% → 20% → 27% as bidders go 2 → 4 → 6 → 10.
3. **Seller.** 8 bidders: **€11.53m** ✓; 3 bidders €10.30m; one buyer with hard haggling €9.50m; inbound offer €8.50m. A second bidder (+€1.2m) beats hard haggling (+€1.0m, assumed).

## Evidence
- **Origin, oil leases.** Capen, Clapp & Campbell (*Journal of Petroleum Technology*, 1971, 23:641-653) studied Gulf of Mexico offshore lease bidding and argued that winning bids were too high to leave a decent profit. The AAPG Explorer account says the study followed a lease sale in which Atlantic Richfield won nearly everything it bid on and was short of money for a couple of years. *(The 20,000-trial Monte Carlo model and the three bidding rules often attributed to the paper come from secondary accounts: not yet verified against the paper.)*
- **Classroom and lab evidence.** Thaler (*JEP*, 1988, 2(1):191-202) opens with a jar-of-coins auction in which the winning bid exceeds the jar's value. A secondary report of his numbers: jars worth $8, mean winning bid $10.01, mean estimate $5.13 *(not yet verified against the column)*. Bazerman & Samuelson (*Journal of Conflict Resolution*, 1983, 27(4):618-634) ran the experiment in MBA classes. Kagel & Levin (*American Economic Review*, 1986, 76(5):894-920): with 3-4 bidders behaviour is near theory; with 6-7 bidders, bids are more aggressive and winners lose money. They also compare the lab results with outer continental shelf lease sales. Public information that reduces uncertainty raises the seller's revenue when there is no curse and lowers it when there is one.
- **Acquirer returns.** Moeller, Schlingemann & Stulz (*Journal of Finance*, 2005, 60(2):757-782; NBER working paper 10200): in 1998-2001, bidders' shareholders lost about 12 cents per dollar spent on acquisitions at announcement, about $240bn in total, against about $7bn (1.6 cents per dollar) in the 1980s; bidder losses exceeded target gains by about $134bn. A small number of announcements by very highly valued firms drove the total. The authors read this as negative synergies and as investors reassessing the bidders' stand-alone value, so it is **consistent with overpayment but not a clean test of the winner's curse**. An earlier paper by the same authors (NBER working paper 9523, summarised in an NBER Digest, August 2003) found that large-firm acquirers lost most, that small-firm acquirers gained, and that buying private firms did better than buying public ones.
- **The seller's mirror image.** Bulow & Klemperer (*American Economic Review*, 1996, 86(1):180-194): an auction with no reserve price and one extra bidder beats an optimally run negotiation with one fewer bidder; they conclude that negotiating skill is worth little next to additional competition. This is a theory result; the size of the effect in real M&A sales is *(not yet verified)*.

## Where it breaks
- **Private-value or strategic deals.** If the prize is worth something specific only to you (a synergy only you have), part of the value is not common, and the curse is smaller. This is the case where you should bid more.
- **Sophisticated bidders adjust.** Experienced bidders shade more as rivals multiply. In this lab the other bidders' shade is fixed, so the buyer's curse and the seller's gain from extra bidders are both overstated.
- **Strategic value of winning.** Buying a supplier or competitor can be worth more than the standalone estimate (denying it to a rival). That is an edge, not an excuse.
- **Costs of the process.** Fees, leaks, delay and failed deals reduce the seller's gain from a broad auction; the lab ignores them.
- **Real deals are not sealed-bid.** Ascending auctions, rounds and exclusivity change what a winner learns; the direction is the same, the size is not.

## Application question (graded on rubric B)
> It is 2030. Your company has raised a Series A and a long-time competitor offers to sell you its product line in a banker-run process. There will be about eight bidders. Your team's estimate is that it is worth €8m to you; you know your own cost savings are real, but the competitor's customer contracts are hard to verify. Later you expect to sell your own company to a strategic buyer.
> 1. Explain in your own words why bidding your €8m estimate is likely to lose money here, and roughly how much you should shade (size it: small, about a quarter, about half).
> 2. What do you do, as a policy? Cover the bid, the process you ask for, and what you check before you bid.
> 3. How does the same law change how you sell your own company, and where might it mislead you here?

Answer in under 300 words.

## Takeaways
1. The winner is the one who overestimated most: with six bidders and estimates ±25% off, bidding your honest estimate means paying about 14% over what it is worth to you and losing about €1.65m per win.
2. More bidders and more uncertainty mean deeper shading: the shade at which a win stops being a loss rises from about 8% (2 bidders) to about 27% (10). At low uncertainty the curse nearly disappears.
3. Fix the structure, not only the bid: pre-empt, narrow the field, do your own diligence, or walk away. If you win most of the auctions you enter, you are probably overpaying.
4. The mirror image: as a seller, add bidders. A second bidder was worth more than hard haggling, and eight bidders lifted the price about a third over an inbound offer in this model.

## Sources
- Capen, E.C., Clapp, R.V. & Campbell, W.M. (1971). Competitive bidding in high-risk situations. *Journal of Petroleum Technology*, 23, 641-653 (bibliographic details via Kagel & Levin's encyclopedia entry; story via AAPG Explorer, "Bid winners can face 'curse'", https://www.aapg.org/news-and-media/details/explorer/articleid/46487/-bid-winners-can-face-curse).
- Thaler, R.H. (1988). Anomalies: the winner's curse. *Journal of Economic Perspectives*, 2(1), 191-202 (abstract: https://stafforini.com/works/thaler-1988-anomalies-winner-curse/).
- Bazerman, M.H. & Samuelson, W.F. (1983). I won the auction but don't want the prize. *Journal of Conflict Resolution*, 27(4), 618-634 (bibliographic details only).
- Kagel, J.H. & Levin, D. (1986). The winner's curse and public information in common value auctions. *American Economic Review*, 76(5), 894-920 (abstract: https://ideas.repec.org/a/aea/aecrev/v76y1986i5p894-920.html).
- Moeller, S.B., Schlingemann, F.P. & Stulz, R.M. (2005). Wealth destruction on a massive scale? A study of acquiring-firm returns in the recent merger wave. *Journal of Finance*, 60(2), 757-782 (abstract: https://www.nber.org/papers/w10200).
- NBER Digest (August 2003), "Big firms lose value in acquisitions", on NBER working paper 9523 (https://www.nber.org/digest/aug03/big-firms-lose-value-acquisitions).
- Bulow, J. & Klemperer, P. (1996). Auctions versus negotiations. *American Economic Review*, 86(1), 180-194 (abstract: https://ideas.repec.org/a/aea/aecrev/v86y1996i1p180-94.html).
- The simulation's figures (shade, win rates, prices) are outputs of this lab's own illustrative model, not data from the sources above.
