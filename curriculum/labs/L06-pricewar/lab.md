---
id: L06
title: "Price wars: the repeated prisoner's dilemma"
areas: [competition, strategy]
difficulty: 1300
phase: 2
sim: labs/pricewar.html
cards: [comp-001, comp-002, comp-003, comp-004]
---

# L06. Price wars: the repeated prisoner's dilemma

## Goal
After this lab you can decide **when to hold your price, when to hit back at a rival's cut, and how to make a price war not worth starting**.

## The principle
**The prisoner's dilemma.** Two sellers each choose a high or a low price. Whatever the rival does, undercutting pays more for you in a single round, yet both low is worse for both than both high. In a **one-shot** game, undercutting is the rational move.

**The repeated game.** When the same two meet again and the future matters ("the shadow of the future"), cooperative pricing can be stable: a cut today is paid back by retaliation tomorrow. Robert Axelrod's computer tournaments (around 1980; *The Evolution of Cooperation*, 1984) tested this: simple strategies were entered in a round-robin of repeated dilemmas, and the simplest, **tit-for-tat** (cooperate first, then copy the rival's last move), won both rounds.

**The lab's payoffs** (€k profit a quarter, the 5/3/1/0 pattern of Axelrod's tournaments scaled by 30; my scaling, not a measured market):

| | Rival high | Rival low |
|---|---|---|
| **You high** | 90 / 90 | 0 / 150 |
| **You low** | 150 / 0 | 30 / 30 |

**When does the truce hold?** Let w be the chance the contest goes on each quarter. Against a rival that retaliates, holding high beats undercutting every quarter when w ≥ (T−R)/(T−P) = 60/120 = **50%** (T = 150 undercut alone, R = 90 both high, P = 30 both low). Against a rival that alternates cuts and holds, the condition is (T−R)/(R−S) = 60/90 = **67%** (S = 0, undercut alone by the rival). The general form, a threshold set by the larger of the two ratios, is the standard textbook result (a worked example on Wikipedia's tit-for-tat page, with payoffs 6/9/2/3, gives a threshold of 3/4, which fits the formula); Axelrod's own threshold for his payoffs is 2/3 *(not yet verified in the book)*.

## The ideal and the trade-offs
**The goal is not never to cut.** It is to be the kind of competitor that makes cutting unprofitable for everyone, at the lowest cost to you.

What to aim for, in Axelrod's terms: **nice** (start by holding the price), **retaliatory** (answer a cut at once), **forgiving** (go back to high after one answer), **clear** *(the "clear" property is from secondary summaries; not yet verified in the book)*.

| Situation | Do | Why |
|---|---|---|
| The rival cuts once, intent unknown | **Match for one quarter, then go back to high** | Ends a test without feeding a war; costs one weak quarter |
| The rival keeps cutting however you answer | Match and stay matched | Ignoring it hands over the customers; forgiving a predator is exploited |
| The end date is known (technology switch, exit, last tender) | **Expect the rival to cut first; do not rely on the truce** | The shadow of the future is gone; the truce unravels backwards from the last round |
| Many rounds ahead and a long relationship | Hold high, answer cuts once, publish your rule | The future carries the cooperation |

| Lever | Effect | Cost and catch |
|---|---|---|
| **Differentiate** (features, service, lock-in) | Large: a cut wins the rival less, so there is nothing to retaliate against | Costs engineering time; works only if it crosses a threshold (half-measures do nothing in the model) |
| **Signal a clear, public response rule** | Free if believed: cuts stop being attractive once the rival thinks you will hit back | Slow in the real evidence (about three years in Byrne & de Roos); competition law limits how you communicate (take legal advice) |
| **Hit back once, then forgive** | Medium to large when the rival's type is unknown | One quarter at the sucker payoff when you return to high |
| **Win share fast with a price push** | Small, often negative against a rival with deeper pockets | Starts the war you wanted to avoid; needs customers who stay |

**Founder rule:** with a well-funded rival, never buy share with a price war you cannot outlast. Make cutting unattractive (differentiate), be predictable (answer once, then return), and treat any known end date as a one-shot game.

## Tests (in the simulation; answers for the teacher)
Setting: you and one well-funded rival; each quarter each of you sets high or low; both high €90k, undercut alone €150k, both low €30k, nobody else; 90% chance the contest goes on each quarter.
1. **The rival cuts once** (even odds it is a test or a campaign; today you ignore it: €404k). Match once, then high: **€735k (1.8×)** ✓. Copy every move €489k (1.2×), ignore €404k, match for good €323k (0.8×). Instinct to fight it out is wrong; ignoring only works against a rival that copies you.
2. **The market ends in 2 quarters** (rival clears stock in the final quarter; today you hold: €90k). Cut now and stay low: **€177k (2.0×)** ✓; cut in the last quarter only €117k (1.3×). The instinct (keep the truce) is the worst.
3. **Avoiding the war** (calculating rival, believes 30% you hit back; today the war runs: €269k). Differentiate clearly: **€819k (3.0×)** ✓; win share fast €329k (1.2×); differentiate a little €305k (1.1×); signal to 50% belief €269k (no change; the rival needs over about 56%, at which signalling gives €898k).

## Evidence
- **Axelrod's tournaments.** First round: fourteen entries plus a random rule in a round-robin; tit-for-tat, entered by Anatol Rapoport, won and was the simplest program. Second round: 62 entries from six countries; tit-for-tat won again. Adding a 1% chance of misreading the rival's last move did not change the first-round winner (excerpt of Axelrod, 1984, at cse.iitk.ac.in).
- **Tit-for-tat is not universally best.** The Wikipedia entry notes a single error can start an unending alternation of cuts ("death spiral"), and that generous and contrite variants address this; Axelrod's more forgiving tit-for-two-tats did worse in the second round because aggressive entries exploited it. A 2025 reproduction by Knight and co-authors found that in a much larger field the best Axelrod-tournament entry ranked only 16th, and warned against generalising from the original tournament (vknight.org summary of the paper).
- **Retail gasoline, Perth.** Byrne & de Roos (American Economic Review 2019, 109(2): 591-619) use 15 years of station-level prices in one urban market. They find a shift to coordinated pricing that took about three years, in which leading firms signalled prices and experimented to set focal points that softened competition and raised retail margins. Margin gains of up to about 75% appear in a 2016 conference version *(not yet verified)*.
- **A price war that destroyed value: US airlines, 1992.** The Christian Science Monitor (2 June 1992) reports that Northwest launched a kids-fly-free promotion, American Airlines cut all restricted domestic discount fares by half a day later, and others matched quickly; analysts said added traffic would not make up for lost revenue and that the year's loss might be comparable to the previous year's $2 billion, with summer bookings only 2-3% above the year before. Steven Morrison and Clifford Winston are cited in a case summary for a $1.53 billion cut in industry profits *(not yet verified)*. The case is taught at Kellogg (Besanko, 2002).

## Where it breaks
- **Noise and misreading.** A cut that was a one-off error or a promotion can be read as aggression; strict tit-for-tat then echoes it. Forgiveness is what stops the echo.
- **More than two players, entry and uneven size.** Retaliation is hard to coordinate with many sellers, and a new entrant has no history of cooperation.
- **Different beliefs and tools.** A well-funded rival that wants share may rationally accept a long war; the page assumes the rival simply compares profits.
- **Competition law.** Tacit coordination through public price moves is not the same as an agreement, but talking prices with a rival is risky; take legal advice *(not yet verified; not a legal opinion)*.
- **Real end-games.** Customers remember, and you may meet the rival in the next market, so a known end is softer than in the model.
- **The model's numbers.** The rival types, the 15% lasting volume from a push, and the effect of a signal on belief (30% to 50%) are assumptions of the page.

## Application question (graded on rubric B)
> It is late 2027. Your company has two pilot customers and one well-funded competitor with a similar product. At a trade fair a customer tells you the competitor has quoted 15% below your list price. Your investor wants you to "match it and win the account."
> 1. Which law applies, and what does it say you should expect from the rival if you match? Give the mechanism in your own words.
> 2. What do you do about the price over the next four quarters, and which other lever (product, contract terms, signalling) would you pull first? Give a policy, not only the one-off move.
> 3. Where could this law mislead you in a deep-tech market with few customers?

Answer in under 300 words.

## Takeaways
1. The future is what holds a truce together: holding high beats undercutting once the chance of meeting again next quarter is above roughly 50-67% (in this model, depending on the rival's tactic). When the end is known, the truce unravels backwards.
2. Be nice, hit back once, then forgive, and be clear. Ignoring a cut invites the next one; a grudge locks in a price war.
3. A known end date, a short runway or a one-off tender makes undercutting rational for both sides; expect the rival to cut first.
4. Avoid the war by changing the payoffs: differentiate until a cut earns the rival less than holding high; signal credibly; do not buy share with a price war against a rival with deeper pockets.

## Sources
- Axelrod, R. (1984). *The Evolution of Cooperation*. Basic Books. Excerpt read at https://www.cse.iitk.ac.in/users/amit/books/axelrod-1984-evolution-of-cooperation.html
- Axelrod, R. (1981). The emergence of cooperation among egoists. *American Political Science Review*, 75(2), 306-318 (abstract only, via search results; payoffs and "about 200 moves" not yet verified).
- Byrne, D.P. & de Roos, N. (2019). Learning to coordinate: a study in retail gasoline. *American Economic Review*, 109(2), 591-619. Abstract read at https://ideas.repec.org/a/aea/aecrev/v109y2019i2p591-619.html
- Wikipedia, "Tit for tat" (accessed 22 Oct 2026): https://en.wikipedia.org/wiki/Tit_for_tat (echo and noise, generous and contrite variants, discount-factor example).
- Knight, V. et al. (2025). Reviving, reproducing, and revisiting Axelrod's second tournament. Summary read at https://vknight.org/posts/2025-10-21-rrr/
- Christian Science Monitor (2 June 1992). "Falling Fares To Test Airlines' Staying Power": https://www.csmonitor.com/layout/set/amphtml/1992/0602/02071.html
- Besanko, D. (2002). The mother of all (pricing) battles: the 1992 airline price war. Kellogg case 5-204-250 (catalogue page read only).
