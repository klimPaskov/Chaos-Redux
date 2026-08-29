# Event 35 Great Depression 2.0 AI and probability matrix

## Audit contract

Use the same scenario IDs before and after tuning. Start every weighted-surface review with `hoi4.probability_inspect`. Record whether the candidate pool and external factors are complete.

Classify every result as:

- Exact.
- Bounded.
- Sampled.
- Score-only.
- Unresolved.

Do not state exact probabilities from an incomplete pool.

## Surface inventory

| Surface | Owner | Required evidence |
| --- | --- | --- |
| Independent country selection | Event framework and Event 35 target adapter | Inspect, evaluate, sweep, compare |
| Opening doctrine choice | Event 35 AI | Inspect, evaluate, compare |
| Ordinary decision choice | Event 35 decisions | Inspect, evaluate, compare |
| Depression Center target | Event 35 state selector | Inspect, evaluate, sweep where useful |
| Contagion relationship and action | Evolution I | Inspect, evaluate, compare |
| Full contagion conversion | Evolution I | Inspect, evaluate, timing sweep |
| Baseline strike, government crisis, and National Breakdown | Baseline Event 35 | Complete gate audit and bounded probability |
| Organized social incident and response | Evolution II | Inspect, evaluate, compare |
| Coup, separatism, and movement-specific civil conflict | Evolution II | Complete gate audit and bounded probability |
| Evolution timing | Event 35 evolution effects | Inspect, evaluate, sweep, scheduled comparison |
| Evolution III country conversion | Global episode | Inspect, evaluate, sweep |
| Bloc, supplier, and conference choice | Evolution III | Inspect, evaluate, compare |
| Random incident pools | Event 35 and evolutions | Full-pool normalization and dominance audit |

## Scenario table

| ID family | IDs | Purpose |
| --- | --- | --- |
| Targeting | `TGT-01` to `TGT-10` | Fairness, eligibility, recent-history suppression, cluster actor |
| Doctrine | `DOC-01` to `DOC-07` | Material fit of all six recovery philosophies |
| Actions | `ACT-01` to `ACT-05` | Phase priority, emergency replacement, center risk |
| Contagion | `CTG-01` to `CTG-10` | Aid, ring-fence, abandonment, anti-loop, supplier restraint |
| Baseline breakdown | `BDP-01` to `BDP-04` | Ordinary unrest, strict civil-conflict gate, nonwar fallbacks, recent-war blocking |
| Social Collapse | `SOC-01` to `SOC-05` | Negotiation, force, coup, separatism, recent-war blocking |
| Global | `GLB-01` to `GLB-10` | World episode, local conversion, suppliers, global recovery |
| Evolution timing | `EVO-01` to `EVO-08` | Acceleration, slowing, inheritance, disabled state |

The full inputs and expected orderings are in specification part 9.

## Dominance limits

- No target country should dominate comparable candidates only through raw factory count.
- No doctrine should rank first in every scenario.
- Emergency actions should dominate only in emergency conditions.
- Market Clear and Austerity must be viable in suitable conditions and unsafe in unsuitable conditions.
- Force should not dominate every Social Collapse incident.
- Civil war should remain a rare gated outcome.
- One generic incident must not dominate every Severity band.
- One major ally should not receive every contagion aid package when other valid relationships exist.
- Supplier booms must stop accepting world orders as Overheating approaches danger.

## Starvation checks

Confirm that:

- Player non-majors remain valid targets.
- Small economies have at least one affordable recovery action.
- Finance and Trade can act when a valid partner exists.
- Austerity and Market Clear receive nonzero weight under safe conditions.
- Negotiation remains possible under broad movement support.
- A stable self-sufficient country can resist full Evolution III conversion.
- Global recovery actions become available before every country has already recovered.

## Sequence evidence

Use probability sequence analysis only when the complete Event 35 cadence is declared, including:

- Phase-scaled national evaluation cadence and elapsed-day normalization.
- Incident cooldowns.
- Mission durations.
- Evolution timing.
- Target removal.
- Recovery and relapse transitions.
- Global episode stages.
- Terminal and cleanup states.

Without the complete manifest, use local timing and score evidence instead.

## Required comparison output

For every changed weighted surface, return:

| Field | Required content |
| --- | --- |
| Surface | Exact file, block, and owner |
| Baseline revision | Commit or source hash |
| Patched revision | Commit or source hash |
| Scenario IDs | Same IDs before and after |
| Pool completeness | Complete or missing factors |
| Evidence type | Exact, bounded, sampled, score-only, unresolved |
| Before result | Ordering or probability |
| After result | Ordering or probability |
| Intended relationship | Design target from part 9 |
| Dominance finding | Any option overrepresented |
| Starvation finding | Any valid route underrepresented |
| Remaining uncertainty | External factor or engine limitation |
