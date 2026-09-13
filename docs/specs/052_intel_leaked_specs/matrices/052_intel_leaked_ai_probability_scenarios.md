# Event 052 AI and Probability Scenario Matrix

This matrix defines the weighted-behavior evidence required during implementation. It does not assign final script weights.

Every weighted surface must begin with `hoi4.probability_inspect`. The implementation should establish a baseline audit, apply the owner-approved balance change, then run `hoi4.probability_compare` against the same named scenarios. Exact probabilities are valid only when the candidate pool and external factors are complete.

## Scenario set

| Scenario ID | Situation | Weighted surfaces | Expected ordering | Evidence type |
| --- | --- | --- | --- | --- |
| IL-AI-01 | Player target at peace, strong agency, several hostile rivals, no imminent war | Target-route selection, action scores, poison entry | Player route remains competitive, compartmentation and selective containment outrank blanket shutdown, poison becomes viable after containment | Inspect, evaluate, sweep, compare |
| IL-AI-02 | AI major target at war, weak agency, land plans and personnel files exposed, invasion danger high | Damage-control actions, foreign exploiter selection | Rewrite land plans and recall or shutdown dominate reform, land enemies dominate named exploiter pool | Inspect, evaluate, compare |
| IL-AI-03 | Naval major target, naval and convoy files exposed, one strong naval enemy and several irrelevant land powers | Named exploiter profile and response action | Strong naval enemy dominates naval exploitation, irrelevant land powers do not starve it, naval replan outranks unrelated actions | Inspect, evaluate, sweep, compare |
| IL-AI-04 | Target has a close ally, neutral states, and one hostile rival | Friendly behavior, ally-copy variant, named exploiter selection | Ally warning or quarantine dominates aggressive ally use, hostile rival remains preferred named exploiter | Inspect, evaluate, compare |
| IL-AI-05 | Total Compromise affects two current war enemies | Target count, participant selection, reciprocal exploitation, action scores | Wartime pair is strongly preferred when valid, each side replans and exploits independently, neither side gains automatic dominance | Inspect, evaluate, compare, render |
| IL-AI-06 | Strong target service has three hostile high-Reliance recipients and a valid land deception | Poison outcome, target choice, foreign reaction | Poison entry becomes high priority, highest-Reliance relevant recipients dominate, unrelated recipients receive no strong penalty | Inspect, evaluate, sweep, compare |
| IL-AI-07 | No agency mechanics available | Target selection, action scores, exploitation profiles | Event remains fully playable, base intelligence and military actions dominate, agency-only actions are absent and do not distort weights | Inspect, evaluate, compare |
| IL-AI-08 | Total Compromise active with only one valid target | Target-count selection and fallback | Severe single-target profile resolves cleanly, invalid multi-target branches have zero effective weight, event remains available | Inspect, evaluate, compare |
| IL-AI-09 | Same player country was targeted twice before and completed compartmentation | Target selection, initial Exposure, recurrence flavor | Country remains eligible, lasting resilience lowers opening within cap, old incident state does not affect new exploiters or duration | Inspect, evaluate, compare |
| IL-AI-10 | Deep Files activates during an incident at Exposure 40 | Second-tranche timing and content selection | Second tranche remains possible after delay, adds sensitive domains once, does not reset the entire incident | Inspect, evaluate, timing render |
| IL-AI-11 | Deep Files activates during an incident at Exposure 10 | Second-tranche gate | Near-resolved incident normally closes without a new tranche, unless a rare explicit profile proves remaining live material | Inspect, evaluate, compare |
| IL-AI-12 | Resource-poor AI target with low command power, low XP, and little equipment | Decision AI | AI chooses one affordable high-value response and does not loop on blocked complete packages | Inspect, evaluate, sweep, compare |
| IL-AI-13 | Neutral minor neighbor with claims and low agency, distant major with strong agency but no strategic interest | Named exploiter selection | Neighbor can outrank distant major for land and mobilization files, strong agency alone does not decide relevance | Inspect, evaluate, compare |
| IL-AI-14 | Named exploiter becomes ally during incident | Reliance and future action scores | Aggressive use falls sharply, cooperative or disclosure behavior rises, existing results remain bounded | Inspect, evaluate, compare |
| IL-AI-15 | Target ignores Personnel at Risk until mission is close to failure | AI emergency ordering and severe outcome selection | Recall or shutdown becomes dominant, failure produces one bounded severe result, no cascade across every operative | Inspect, evaluate, compare |
| IL-AI-16 | Four-target Total Compromise with many eligible exploiters | Global caps, report cadence, participant selection | Strategic recipients remain represented, global cap prevents popup explosion, one target does not consume every exploiter slot | Inspect, evaluate, sweep, render |

## Weighted surfaces to inspect

### Baseline target route

The route chooses the source player country or a random valid major.

Required checks:

- both routes are visible to the analyzer when valid
- invalid routes drop out without leaving dead weight
- the player route is not starved in a world with many majors
- the major route still produces variety
- baseline never initializes more than one target

### Major target candidate pool

Required factors include current war relevance, strategic importance, recurrence history, current eligibility, and incident overlap.

A previous target remains eligible. Recurrence memory can affect flavor or small balance factors but must not become immunity.

### Archive domain selection

The domain pool must preserve:

- at least one military or mobilization domain
- at least one nonmilitary domain
- target capability validity
- baseline, Deep Files, and Total Compromise depth differences
- rare-profile requirements

Inspect the complete domain candidate pool under each profile. Do not claim normalized exact odds from a partial list.

### Named exploiter selection

The score should combine relationship, war state, geography, claims, capability, agency strength, active domain, and current foreign plans.

The audit should verify dominance expectations without assuming that `is_major` is always the strongest factor.

### Damage-control AI

Action scoring must consider:

- current Exposure
- active domains
- mission deadlines
- current wars and invasion danger
- agency strength
- available costs
- expected Exposure reduction
- operational sacrifice
- later deception value

Blocked actions must have zero effective weight.

### Foreign exploitation action

The candidate pool should include only actions supported by the recipient, relationship, and active domain.

The audit should verify that a naval action cannot dominate for a country with no meaningful naval use and that a friendly ally does not select hostile exploitation merely because it has a strong agency.

### Poison the Leak

The outcome model should consider:

- target preparation
- selected profile
- recipient Reliance
- archive confidence
- target service quality
- recipient service quality
- consistency of the staged posture
- independent verification

The full candidate pool must include success, partial success, and failure.

### Total Compromise target count

The balance anchor is severe single, two, three, then four targets in descending practical frequency.

The audit should sweep valid-pool sizes from one through at least six and verify graceful fallback. A branch that cannot select its required number of unique targets must not partially initialize.

### Evolution timing

Deep Files and Total Compromise use event-owned MTTH or equivalent paced logic.

Timing scenarios should include:

- threshold crossed before Event 52 ever fires
- threshold crossed during an active incident
- no valid target
- event disabled
- evolution disabled
- active incident near closure
- high-war world with several valid majors

Scheduled state changes must be declared when asking the analyzer for timing results.

## Evidence rules

- Use `hoi4.probability_inspect` first for every surface.
- Use `hoi4.probability_evaluate` for named fixed scenarios.
- Use `hoi4.probability_sweep` for Exposure, agency strength, pool size, war danger, and Reliance thresholds.
- Use `hoi4.probability_compare` after every weighted patch against the same scenario set.
- Use `hoi4.probability_render` for target-count, timing, or sensitivity results when a visual comparison improves review.
- Use `hoi4.probability_simulate` only when the declared candidate pool is complete and seeded sampling answers a question that exact evaluation cannot.
- Use `hoi4.probability_sequence` only after the implementation provides a complete Event 52 sequence manifest covering cadence, cooldowns, removals, target caps, repeatable recovery, and terminal cleanup.
- Label results as exact, bounded, sampled, score-only, or unresolved.
- Do not infer exact normalized probabilities from an incomplete recipient or domain pool.
