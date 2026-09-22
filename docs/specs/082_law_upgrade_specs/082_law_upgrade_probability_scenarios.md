# Law Upgrade: probability and AI evidence contract

## Current evidence status

No HOI4 probability inspection, scenario evaluation, sweep, simulation, or engine-calibrated MTTH conversion was executed during this planning session. The supplied probability-auditor definition was read, but that specialist and its required tools were not callable here.

Numbers in the numbered specification are proposed inputs and relative priorities. They are not claimed cumulative probabilities.

## Required specialist sequence

The `chaosx_ai_probability_auditor` must begin with `hoi4.probability_inspect` against the actual implemented sources and loaded game version. The inspector must identify all relevant MTTH entries, modifiers, scripted helpers, candidate actions, ordinary AI spending alternatives, eligibility gates, and state inputs.

Only after inspection should it use `hoi4.probability_evaluate` for named fixtures, `hoi4.probability_sweep` around boundaries, `hoi4.probability_simulate` for explicitly declared uncertain inputs, and `hoi4.probability_compare` for before-and-after evidence. Use `hoi4.probability_render` where a timing or sensitivity plot makes the evidence clearer.

Keep exact, bounded, sampled, and unresolved results separate. Use the verified game-version MTTH adapter for cumulative timing. The auditor supplies evidence and does not decide the intended balance.

## Starting operational thresholds for AI fixtures

These thresholds are author proposals for evaluation, not previously implemented project facts.

| Input | Proposed fixture meaning |
| --- | --- |
| Serious equipment shortage | Weighted deployed-land-force equipment fulfillment below 80% |
| Ample equipment | Weighted fulfillment at least 95%, with nonnegative reinforcement stock outlook |
| Critical manpower shortage | Available deployable manpower below 25% of current reinforcement requirement, with a positive requirement |
| No manpower shortage | Available manpower covers reinforcement requirement plus 90 days of observed losses |
| Serious reconstruction need | At least 20% of relevant owned factory capacity is damaged or under repair |
| Low War Support | Below 50% |
| Very low War Support | Below 25% |
| Voluntary extreme entry support gate | At least 80% |
| Stronger defensive enemy | Verified hostile war-strength estimate at least 150% of the country and its participating allies' estimate |

Use actual owner-supported measures. A zero denominator does not create a fabricated shortage or an infinite strength ratio. Keep unavailable strength and projected-loss inputs explicitly unresolved instead of making up a number.

Weighted equipment fulfillment must use a documented cost or equivalent system-level weight. It cannot sum every item as if a rifle and an aircraft carried the same need.

## Evolution fixtures

| Case | State | Expected qualitative result |
| --- | --- | --- |
| P01 | Chaos 199, no active evolution | Evolution I ineligible |
| P02 | Chaos 200, fewer than half of civilian countries at war | Evolution I nominal base 90 days |
| P03 | Chaos 400, at least half at war | Evolution I nominal input 33.75 days before the adapter |
| P04 | Chaos 599, Evolution I active | Evolution II ineligible |
| P05 | Chaos 600, Evolution I active, both II modifiers true | Evolution II nominal input 50.625 days |
| P06 | Chaos 799, Evolution II active | Evolution III ineligible |
| P07 | Chaos 800, Evolution II active, both III modifiers true | Evolution III nominal input 33.75 days |
| P08 | Chaos crosses above a threshold, then below it before activation | Eligibility suspends, no law or War Support grant |
| P09 | First Event 82 firing at Chaos 850, all evolutions enabled | Highest eligible opening profile, one step only |
| P10 | Evolution I disabled, Chaos 850 | Higher dependent profiles unavailable |
| P11 | Activated evolution, later Chaos decline | Historical activation retained |
| P12 | No qualifying civilian-country denominator | Population-share timing modifier inapplicable |

For P07, define the second share as at least half of all relevant civilian countries holding both Total Mobilization-or-higher and Scraping-the-Barrel-or-higher. It is not a changing half-of-a-half denominator.

Evaluate fixed-state horizons at 30, 90, 180, and 365 days only with the verified adapter. Also evaluate scheduled changes at days 30 and 90 for war entry, support collapse, settings changes, and a threshold recrossing.

## Reversal and spending fixtures

| Case | Country state | Required qualitative comparison |
| --- | --- | --- |
| A01 | Peace, both laws, support 20%, sufficient PP | Both reversals outrank routine voluntary extreme entry |
| A02 | War, both laws, support 100%, equipment fulfillment 60%, manpower ample | Conscription exit receives strong priority |
| A03 | War, both laws, support 90%, critical reinforcement manpower shortage | No automatic conscription exit solely because the law is extreme |
| A04 | War, economy extreme only, shortages caused by unavailable resources | Do not value the full theoretical output as usable production |
| A05 | Peace after victory, economy extreme | Recognize that war-only bonuses are inactive |
| A06 | One point below reversal affordability | No payment or law change, saving priority can remain |
| A07 | Two exits initially affordable, first purchase changes affordability | Requote the second, no overdraft |
| A08 | Ordinary price 113 PP after normal rounding | Reversal requires 226 PP |
| A09 | Discount expires before confirmation | Current accepted quote and debit agree |
| A10 | Newly forced extreme with unchanged desperate-war conditions | No unconditional forced immediate reversal |
| A11 | AI voluntarily enters an extreme law | No immediate contradictory paid exit under unchanged inputs |
| A12 | Relevant category unavailable or unrecognized | No fictional action joins the candidate pool |
| A13 | Human and AI with identical country state | Same mechanics and current price |
| A14 | PP spending alternatives compete with a strategically necessary exit | Candidate-pool and reserve policy prevent endless avoidable starvation |

## Sensitivity sweeps

Sweep support through 0, 24.99, 25, 49.99, 50, 79.99, 80, and 100. Sweep equipment fulfillment around 80% and 95%, manpower coverage around the critical threshold, damaged capacity around 20%, and current PP around each full quoted reversal price.

For each supported law owner, sweep one position below the normal cap, at the cap, and at the extreme. Include both-law and single-law states and peaceful as well as wartime conditions.

Do not report a relative score of 100 as a 100% chance. Inspect the complete action pool and the actual game choice mechanism.

## Completion evidence

The specialist handoff must include source revision, game build, inspector output, exact fixture inputs, scenario results, uncertainty disposition, unresolved engine access, and any recommended balance concern.

A sampled favorable result is not a proof that the AI cannot enter a purchase loop. Include deterministic same-state entry/exit consistency checks and long enough live observation to expose recurring spending failures.
