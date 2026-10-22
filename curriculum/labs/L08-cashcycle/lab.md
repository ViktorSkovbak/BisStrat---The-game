---
id: L08
title: The cash conversion cycle: why profitable companies run out of cash
areas: [anatomy, venture]
difficulty: 1300
phase: 2
sim: labs/cashcycle.html
cards: [anat-001, anat-002, anat-003, anat-004]
---

# L08. The cash conversion cycle: why profitable companies run out of cash

## Goal
After this lab you can decide **how fast a product company can afford to grow**, which terms to fix first (stock, deposits, supplier credit or price), and **how much to raise** so that growth does not empty the bank.

## The principle
**Cash conversion cycle (CCC)** = days of inventory + days of receivables − days of payables.
- *Days of inventory*: how long stock sits before it is sold (parts, work in progress, finished units).
- *Days of receivables*: how long customers take to pay after delivery.
- *Days of payables*: how long you take to pay your suppliers.

The CCC is the number of days your money is out of the bank between paying for parts and being paid for the product. A company with a 120-day cycle has about **four months of cost of sales** tied up in operations. In a steady business that is a fixed amount, already funded. **In a growing business it keeps rising**: every extra unit per month needs stock and an unpaid invoice before it pays back.

**Churchill & Mullins, "How Fast Can Your Company Afford to Grow?" (Harvard Business Review, May 2001).** Their point: a profitable company that grows too fast can run out of cash even when its products sell, because growth consumes cash for working capital, facilities and operating costs, faster than the business generates it. They give a formula for the **self-financeable growth rate**: the pace at which a company's own cash generation can pay for its growth. *(Per a secondary summary, it combines the cash cycle, the cash needed per euro of sales and the cash margin; the article itself sits behind a paywall and was not read: not yet verified.)*

**The simple version used in this lab** (monthly, our own derivation, not their published formula):

> **growth profit alone can fund ≈ m / (n − m)**, where m = profit as a share of sales, and n = cash tied up in operations measured in months of sales.

Here m = 16% and n = 3.2 months (stock 1.8 + invoices 2.0 − supplier credit 0.6), so profit alone funds about **5.3% growth a month** (roughly 85% a year). The plan is 10% a month (about 214% a year).

| Cash cycle | Tied up per month of sales | Profit alone funds (16% profit) |
|---|---|---|
| 120 days (today) | 3.2 months | 5.3% a month |
| 90 days (60-day supplier credit) | 2.6 months | 6.6% a month |
| 75 days (half the stock) | 2.3 months | 7.5% a month |
| 88 days (30% deposits) | 2.15 months | 8.0% a month |
| 58 days (deposits + 60-day suppliers) | 1.5 months | 11.5% a month |

## The ideal and the trade-offs
**The goal is not the shortest possible cycle.** It is a cycle short enough that the growth you want is financed by profit, terms and a sized round, with a cushion, without starving the product or the customer.

| Situation | Aim for | Why |
|---|---|---|
| Growing fast, thin cash | **Plan growth at or below what profit funds, or fix the terms first** | The hole grows faster than the growth (15% a month needs 3.4× the money of 10% here) |
| Raising money | **Peak need + a third to a half, raised 6-9 months early** | The lowest point is also the weakest time to raise |
| Pilot and early customers | **Ask for deposits and milestone payments** | Customers fund you cheaply when they want you to succeed |
| Stable, slow growth | **Keep the cycle where it is** | Squeezing suppliers and customers costs relationships for little gain |

| Lever (effect on the money the plan needs; this lab) | Effect | Cost and catch |
|---|---|---|
| **Deposits (30% at order)** | **3.7× smaller hole** (€1.05M → €285k) | Can lose price-sensitive customers; needs a strong product and a contract |
| **Half the stock (45 days)** | 2.7× smaller (→ €394k) | Stock-outs; works only if supplier lead times are short; smaller orders may cost more per unit |
| **Supplier credit 30 → 60 days** | 1.7× smaller (→ €613k) | Suppliers may raise the unit price or refuse a new, unproven company |
| **Price +5%** | 1.5× smaller (→ €722k) | Assumes volume holds; helps profit more than timing |
| **Slower growth** | 15% → 10% cuts the hole 3.4× | Costs market position |

**Founder rule:** the hole shows up months after the order, exactly when you are busiest. Compare your planned growth with what profit alone can fund (the first number to know), cut the cycle with deposits and stock before you chase more orders, then size the round on the peak need with a cushion.

## Tests (in the simulation; answers for the teacher)
Setting: €2,000 unit, 40% gross margin, 24% running costs, 80 units a month growing 10% a month for 18 months, 90 days of stock, 60 days to be paid, 30 days to pay suppliers, €800k in the bank. Today: peak outside money needed €1.05M; cash bottoms at −€251k in month 18.
1. **One change.** Stock to 45 days (need €394k, 2.7×), **30% deposits (€285k, 3.7×)**, supplier credit to 60 days (€613k, 1.7×), price +5% (€722k, 1.5×). Best: deposits. The instinct (price) is the smallest lever on the dip.
2. **Growing faster.** 15% a month on today's terms (need €3.6M, 3.4× the 10% plan; low point −€2.8M), stay at 10% (runs out: −€251k), 6% (survives, month-24 sales €457k), **15% with 30% deposits and 60-day supplier terms (need €588k; month-24 sales €1.98M)**. Best: fix the terms, then grow. The instinct (take the order) runs out of cash.
3. **How much to raise.** €0.5M (€551k short), €1.0M (€51k short), **€1.5M (survives; also survives 11% growth, need €1.41M)**, €3.0M (survives to 13%, need €2.32M, at a high ownership cost). Best: €1.5M. The round figure €1.0M fails by a hair.

## Evidence
- **Churchill & Mullins (HBR, May 2001).** The article page's teaser (read) states the problem: growth needs cash for working capital, facilities and operating expenses; a profitable company that grows too fast can run out of cash even when products sell; managers must balance cash used against cash generated. The detailed formula and worked example were not read (paywall): not yet verified.
- **Dell, a negative cycle by design.** CFO magazine (1 Dec 1997, "Upgrading cash flow at Dell"): the cash cycle fell from about 40 days in Q4 1996 to about −5 days in Q4 1997; inventory days from "30-plus" to 13, receivable days from 42 to 37, payable days from 33 to 54. Dell moved much of the stock onto its vendors and stopped paying bills before they were due. Motley Fool (6 May 1999) gives 1998 as −5.04 days (receivables 41.09, inventory 7.05). Stratrix (a secondary page, not verified against Dell's filings) lists −8 days for fiscal 1998, −12 for 1999 and −18 for 2000, and says build-to-order began in 1984 because Michael Dell lacked capital to build ahead. **The day counts differ by source, period and definition; read them as "roughly −5 to −8 around 1998".** In the CFO figures, customers still took about 37-42 days to pay; the win was small stock (13 days) and suppliers who waited longer (54 days) than customers did.
- **A hardware start-up that failed or nearly failed on working capital despite demand:** not found with a traceable source in this pass. Omitted rather than guessed.

## Where it breaks
- **Constant terms are an assumption.** Suppliers may demand cash upfront from a new company; customers pay late under pressure; stock turns slower when demand dips.
- **Lumpy and seasonal orders**, minimum order quantities and long supplier lead times (months, not weeks) mean you hold more stock than the average suggests; the monthly average hides the peak.
- **Deposits and supplier credit have costs** that are not in the model: lost customers, higher unit prices, or covenants on financing.
- **Other cash sources:** grants (often reimbursed in arrears: this adds a receivable of its own), inventory finance and factoring change the tied-up amount. Not modelled.
- **Price and volume:** the model assumes volume holds when price rises.
- **The model is stylised:** running costs scale with units, margins are fixed, growth is smooth for 18 months, then flat. Real growth is bumpy, and fixed overhead (the team) is lumpy. The lesson is the order of magnitude, not the euro.

## Application question (graded on rubric B)
> It is mid-2027. Your new company has its first three pilot customers and a first production run of around 100 units at €3,000 each in view. The contract manufacturer wants payment 30 days after delivery but needs a 20-week lead time and a minimum order of six months of volume. The pilot customers say they pay 60 days after delivery. You have about €1M raised and a plan to double the volume every quarter. A grant of €500k is approved but pays out in arrears after you report costs.
> 1. In your own words, why can this company be profitable on paper and still run out of cash? Which of the three cash cycle terms hurts most here?
> 2. Size it roughly (no calculation needed): how many months of cost of sales do you expect to tie up, and does €1M plus the grant carry the plan?
> 3. What policy do you set on terms with customers, with the manufacturer and with investors, and in what order?
> 4. Where could the cash cycle model mislead you here?

Answer in under 300 words.

## Takeaways
1. **Profit is not cash.** Growth ties money up in stock and unpaid invoices; a 120-day cycle with 10% monthly growth needed about €1.05M of outside money here.
2. **Cash cycle = days of stock + days of receivables − days of payables.** Profit alone funds only about 5% growth a month in this company; the rest must come from shorter terms or outside money.
3. **Fix the terms before chasing growth:** deposits (3.7×) beat less stock (2.7×), supplier credit (1.7×) and a price rise (1.5×). On slow terms the hole grows faster than growth: 15% needs 3.4× the money of 10%.
4. **Raise the peak need plus a third to a half, and raise early.** The lowest point is also the weakest time to raise.

## Sources
- Churchill, N.C. & Mullins, J.W. (2001). How fast can your company afford to grow? *Harvard Business Review*, May 2001. Abstract page: https://hbr.org/2001/05/how-fast-can-your-company-afford-to-grow (formula and worked example not read: not yet verified).
- CFO magazine (1 Dec 1997). Upgrading cash flow at Dell. https://www.cfo.com/news/upgrading-cash-flow-at-dell/684776/
- The Motley Fool (6 May 1999), Dell cash conversion cycle for 1998. https://g.foolcdn.com/ddow/1999/ddow990506.htm
- Stratrix, Dell business model (secondary; day counts for fiscal 1998-2000 and the build-to-order history not verified against Dell's filings). https://www.stratrix.com/business-model/dell-s-configure-to-order-and
- The simple self-financeable growth formula m/(n−m) is this lab's own derivation for a monthly, constant-terms model.
