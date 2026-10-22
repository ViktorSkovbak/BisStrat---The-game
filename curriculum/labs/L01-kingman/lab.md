---
id: L01
title: Kingman's law: why busy teams are slow
areas: [operations, management]
difficulty: 1250
phase: 1
sim: labs/kingman.html
cards: [ops-001, ops-002, ops-003, ops-004, ops-005]
---

# L01. Kingman's law: why busy teams are slow

## Goal
After this lab you can decide **how busy to run a team** and pick the lever that cuts waiting most: pooling the work, clearer specs, taking on less, or hiring.

## The principle
**Kingman's formula** (J.F.C. Kingman, Proceedings of the Cambridge Philosophical Society, 1961): the time a job waits before anyone starts it is roughly

> **wait ≈ unevenness × busy-ness × job time**, where busy-ness = u / (1 − u) and u is the share of time people are busy.

**Little's law** (J.D.C. Little, Operations Research, 1961): jobs in the system = arrival rate × time in the system.

**Why it happens:** work arrives in bursts and job sizes vary. Idle time at 10:00 cannot be saved for the burst at 14:00. With slack, bursts drain; without slack, each burst leaves a queue residue that piles up.

| Busy | Busy-ness u/(1−u) | Wait vs 80% |
|---|---|---|
| 70% | 2.3 | 0.6× |
| 80% | 4 | 1× |
| 90% | 9 | 2.25× |
| 96% | 24 | **6×** |

## The ideal and the trade-offs
**The goal is not zero waiting.** It is the balance between the **cost of spare capacity** (paying people who are sometimes idle) and the **cost of delay** (lost pilots, slipped funding milestones, customers who walk).

| Situation | Plan at | Why |
|---|---|---|
| Speed matters: product, pilots, customer changes, a startup | **70-85%** | Waits stay about 1-3× the job time; lead times are predictable |
| Delay is cheap and work is steady: stocked production, back office | **85-90%** | Waiting costs little; capacity costs a lot |
| Anything uneven | **never above ~90%** | The steep part of the curve: small load changes cause huge, unpredictable waits |

**The curve bends at about 80-85%.**

| Lever | Effect | Cost and catch |
|---|---|---|
| **Pool the work** (one shared queue) | Large: often the biggest single lever | Nearly free; generalists may be a little slower per job |
| **Make jobs more even** (clear specs, smaller jobs) | Medium alone, large combined with pooling | Cheap; needs discipline |
| **Take on less / limit work in progress** | Medium | Costs revenue or goodwill; protects lead times |
| **Overtime** | Small-medium, temporary | Burnout and quality loss (KC & Terwiesch) |
| **Hire** | Large | Most expensive and slowest (months) |

**Founder rule:** an engineer costs ~€8-10k a month; a week's slip on a pilot or milestone usually costs more. Early on, slack is cheap and delay is expensive: plan the team at ~75%, pooled.

## Tests (in the simulation; answers for the teacher)
Setting: 4 engineers, ~9 jobs a week, 2-day jobs, own lists, typical unevenness. Today: 90% busy, 18 days' wait.
1. **One move.** Hire a 5th (5.1 days, 3.5×) vs clear specs (11.3 days, 1.6×) vs one shared queue (4.0 days, **4.5×**). Best: pool. The instinct (hire) is the expensive, second-best answer.
2. **No budget to hire.** Pool + specs (2.5 days, **7.2×**) vs overtime 5.5 days (9 days, 2×) vs turn away one job a week (8 days, 2.25×). Free levers together beat hiring.
3. **How busy to plan** for a 5-day lead-time promise, pooled: 95% (lead ~11 days) ✗, **85% (~4.3 days)** ✓, 75% ✓, 60% ✓. Busiest that keeps the promise: 85%. Separate lists at 85% would give ~13 days.

## Evidence
- **Hospital beds, simulation.** Bagust, Place & Posnett (BMJ 1999; 319:155-158): below about 85% average bed occupancy, emergency patients rarely find no bed; from about 85% shortages appear; from about 90% bed crises become regular.
- **Hospital beds, real data.** Madsen, Ladelund & Linneberg (Health Affairs 2014; 33(7):1236-44): about 2.65 million admissions in Danish medical departments, 1995-2012. High occupancy was associated with about 9% higher in-hospital and 30-day mortality. At high load, quality falls too, not only speed.
- **People speed up, then quality drops.** KC & Terwiesch (Management Science 2009): staff work faster under load, which hides the queue for a while at a cost in outcomes.
- **Product development.** Reinertsen (*The Principles of Product Development Flow*, 2009) argues development teams run close to full and their queues are invisible (design work waiting in inboxes). *(His specific statistics are not yet verified against the book.)*

## Where it breaks
- **Deadlines and crunches** are not steady states; the queue is a transient and can be worse.
- **Load-dependent speed:** under load people cut corners; the queue shows up as rework instead of waiting.
- **Priorities:** a priority lane can keep urgent work fast while low-priority work absorbs the queue.
- **Pooling needs interchangeable people.** Specialists with unique skills behave like separate queues.

## Application question (graded on rubric B)
> It is mid-2027. Your first four engineers run at about 95% on the core build. Your first pilot customer asks for a two-week turnaround on change requests before they sign a paid pilot.
> 1. What does a "two-week" promise mean at today's load? Size it roughly (no calculation needed: use the curve).
> 2. What do you promise, and what do you change in how the team works? Give the policy, not only the one-off fix.
> 3. Where could this law mislead you here?

Answer in under 300 words.

## Takeaways
1. Going from 80% to 96% busy makes jobs wait about 6× longer, with the same people doing the same work.
2. The ideal is not zero waiting: balance the cost of capacity against the cost of delay. Where speed matters, plan at 70-85%.
3. Fix the flow before adding people: pool, make jobs even, limit what you start. Hiring is the most expensive lever and the slowest.
4. Little's law: jobs in progress ÷ jobs finished per week = weeks of lead time.

## Sources
- Kingman, J.F.C. (1961). The single server queue in heavy traffic. *Proc. Cambridge Philosophical Society*, 57(4), 902-904.
- Little, J.D.C. (1961). A proof for the queuing formula L = λW. *Operations Research*, 9(3), 383-387.
- Sakasegawa, H. (1977). An approximation formula Lq ≈ α·ρ^β/(1−ρ). *Annals of the Institute of Statistical Mathematics*, 29, 67-75 (multi-server form, via Hopp & Spearman, *Factory Physics*, 3rd ed., 2011).
- Bagust, A., Place, M. & Posnett, J.W. (1999). Dynamics of bed use in accommodating emergency admissions. *BMJ*, 319, 155-158.
- Madsen, F., Ladelund, S. & Linneberg, A. (2014). High levels of bed occupancy associated with increased inpatient and thirty-day hospital mortality in Denmark. *Health Affairs*, 33(7), 1236-1244.
- KC, D.S. & Terwiesch, C. (2009). Impact of workload on service time and patient safety. *Management Science*, 55(9), 1486-1498.
- Reinertsen, D.G. (2009). *The Principles of Product Development Flow*. Celeritas.
