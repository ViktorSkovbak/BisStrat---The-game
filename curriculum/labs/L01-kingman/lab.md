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

## 1. The question
Your team is "fully booked". Every engineer is busy all day. Customers still wait weeks for a small change, and adding urgency only makes it worse. Nobody is lazy. What is going on, and what would you change?

## 2. The law
**Kingman's formula** (J.F.C. Kingman, *The single server queue in heavy traffic*, Proceedings of the Cambridge Philosophical Society, 1961). For a single server, the average time a job waits in the queue is approximately:

> **wait ≈ V × U × T**
> - **U = u / (1 − u)**: utilisation term, where u is the share of time the server is busy
> - **V = (ca² + cs²) / 2**: variability term; ca and cs are the coefficients of variation (standard deviation / mean) of the time between arrivals and of the service time
> - **T**: the average service time

Hopp and Spearman's *Factory Physics* calls this the **VUT equation** and gives a multi-server version (Sakasegawa 1977) used in the simulation: with c parallel servers sharing one queue, U becomes u^(√(2(c+1)) − 1) / (c(1 − u)).

**Little's law** (J.D.C. Little, Operations Research, 1961): **L = λ × W**. Jobs in the system = arrival rate × time in the system. It holds for almost any stable system, regardless of distributions.

## 3. Why it happens
- Work does not arrive evenly, and jobs do not take equal time. Bursts happen.
- A server that is idle at 10:00 cannot bank that idle time for the burst at 14:00. Lost capacity is gone.
- At 70% utilisation there is enough slack to drain a burst before the next one. At 95% there is almost none, so each burst leaves a residue of queue, and residues pile up.
- The utilisation term is not linear: it explodes as u approaches 1.

| Utilisation u | U = u/(1−u) | Wait vs 80% |
|---|---|---|
| 50% | 1.0 | 0.25x |
| 70% | 2.3 | 0.6x |
| 80% | 4.0 | 1x |
| 90% | 9.0 | 2.25x |
| 95% | 19 | 4.75x |
| 96% | 24 | **6x** |
| 99% | 99 | 25x |

**The one sentence to keep:** going from 80% to 96% busy makes the queue wait about six times longer, with the same people doing the same work.

## 4. Play (open the simulation: `labs/kingman.html` in the Foundry artifact)
**Predict before you slide.** Write each prediction down, then check it. Your predictions are calibration practice.
1. Set 1 worker, variability 1.0 / 1.0. Predict the wait at 90% in service times. Then slide to 90% and compare. (Kingman: 9.)
2. Keep u at 90%. Cut both variabilities to 0.5. Predict the new wait. (V falls from 1.0 to 0.25: about 2.3.)
3. Set u to 90% with 1 worker, then switch to 4 workers sharing one queue at the same 90%. Predict which waits less, and by how much. This is **pooling**.
4. Push to 98% and watch the conveyor. Note how long it takes the queue to drain after a burst.

## 5. Real evidence
- **Hospital beds, simulation.** Bagust, Place and Posnett (BMJ 1999; 319:155-158) simulated an English acute hospital. Below about 85% average bed occupancy the risk of an emergency patient finding no bed was small. From about 85% the risk became visible (roughly four bed-shortage days a year), and from about 90% bed crises became regular. One shortage day took around two average lengths of stay to recover from.
- **Hospital beds, real data.** Madsen, Ladelund and Linneberg (Health Affairs 2014; 33(7):1236-44) studied about 2.65 million admissions to Danish medical departments, 1995-2012. High bed occupancy was associated with about 9% higher in-hospital and 30-day mortality. Queueing is not only a speed problem; at high load, quality falls too.
- **Workers speed up, then quality drops.** KC and Terwiesch (Management Science 2009) found that hospital staff work faster when load is high, which hides the queue for a while, but at a cost in quality and outcomes. Real servers are not constant-speed machines.
- **Product development.** Reinertsen (*The Principles of Product Development Flow*, 2009) argues that most development organisations run their engineers close to full utilisation and then wonder why lead times are long. His point: in development work, the queue is invisible (it is design work waiting in someone's head or inbox), so nobody manages it. *(The book's specific statistics are not yet verified against the original; treat them as his claim.)*

## 6. Where the law breaks
- **Non-stationary demand.** The formula is for a steady state. A project with a deadline crunch never reaches one; the queue is a transient, which can be worse.
- **Load-dependent speed.** People speed up, cut corners or drop tasks under load (KC & Terwiesch). The queue shows up as rework and quality loss instead of waiting.
- **Priorities.** With priority classes, the high-priority jobs can wait little while the low-priority ones absorb almost all of the queue.
- **Single server assumption.** Pooled servers wait less at the same utilisation; specialised servers with separate queues behave like many single servers.

## 7. The founder's version
- **Slack is a strategic asset, not waste.** A team planned at 100% has no capacity to respond to the pilot customer, the investor's diligence request or the failed prototype. Plan engineering at 70-80% and protect the rest.
- **Four levers, in order of cost:** cut variability (smaller batches, standard work, clear specs), limit work in progress (Little's law: less WIP = shorter lead time at the same throughput), pool queues (generalists or shared triage), then add capacity.
- **Little's law is your fastest diagnostic.** Count the open items and the completion rate; their ratio is your lead time. To halve lead time without hiring, halve the work in progress.
- **Quote lead times from the curve, not from effort.** A two-day job in a 95%-loaded team is a three-week job.

## 8. Application question (graded on rubric B)
> It is mid-2027. Your first engineering team (four engineers) runs at about 95% utilisation on the core build. Your first pilot customer asks for a two-week change before they will sign a paid pilot.
> 1. Use Kingman and Little to estimate what a "two-week" promise really means at today's load. Show the numbers, even roughly.
> 2. What do you promise the customer, and what do you change in how the team is loaded? Give the policy, not only the one-off fix.
> 3. Where would the law mislead you in this situation?

Answer in under 300 words.

## Sources
- Kingman, J.F.C. (1961). The single server queue in heavy traffic. *Proc. Cambridge Philosophical Society*, 57(4), 902-904.
- Little, J.D.C. (1961). A proof for the queuing formula L = λW. *Operations Research*, 9(3), 383-387.
- Sakasegawa, H. (1977). An approximation formula Lq ≈ α·ρ^β/(1−ρ). *Annals of the Institute of Statistical Mathematics*, 29, 67-75. (Via Hopp & Spearman.)
- Hopp, W. & Spearman, M. *Factory Physics* (3rd ed., 2011).
- Bagust, A., Place, M. & Posnett, J.W. (1999). Dynamics of bed use in accommodating emergency admissions. *BMJ*, 319, 155-158.
- Madsen, F., Ladelund, S. & Linneberg, A. (2014). High levels of bed occupancy associated with increased inpatient and thirty-day hospital mortality in Denmark. *Health Affairs*, 33(7), 1236-1244.
- KC, D.S. & Terwiesch, C. (2009). Impact of workload on service time and patient safety. *Management Science*, 55(9), 1486-1498.
- Reinertsen, D.G. (2009). *The Principles of Product Development Flow*. Celeritas.
