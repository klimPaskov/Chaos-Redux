# Sandstorm balance scenarios and mathematical checks

## What was checked

This file records planning arithmetic and the scenarios required for later implementation evidence.
The accompanying [calculation data](099_sandstorm_balance_calculations.json) contains the inputs and results.
The arithmetic assumes that each requested whole-person debit applies exactly and rereads the remaining modeled population every six hours.
That assumption is useful for testing the design's numbers but does not establish the native population helper's behavior.
No engine, gameplay, statistical health model or HOI4 probability tool was run.

The six-hour interval is the proposed consequence integration cadence.
Rendering may refresh more often, while geographic work can process several swept cells within an interval.
Cadence changes must preserve equivalent elapsed exposure, actual state population and one committed dose per interval.
Repeated display refresh is not another dose.

## Civilian arithmetic

| Case | Starting residents | Covered share | Conditions | Modeled direct deaths |
| --- | --- | --- | --- | --- |
| B01 | 20,000 | 20% | Five severe days, unprotected | 15 |
| B02 | 2,000,000 | 75% | Five severe days, unprotected | 5,991 |
| B03 | 2,000,000 | 75% | Five severe days, household retreat | 2,848 |
| B04 | 2,000,000 | 75% | Five severe days, retreat and full basic-quality mask input | 2,173 |
| B05 | 2,000,000 | 75% | B04 with an operated corridor over the modeled exposed area | 2,412 |
| B06 | 2,000,000 | 75% | B04 with the maximum combined heat and Acid Rain amplification | 2,933 |
| B07 | 2,000,000 | 100% | Twelve extreme days, unprotected | 59,127 |
| B08 | 2,000,000 | 100% | Twelve extreme days, retreat and full basic-quality mask input | 21,627 |
| B09 | 200,000 | 100% | Six severe hours, unprotected | 40 |
| B10 | 900 | 100% | Twelve extreme days, unprotected, already below protected minimum | 0 |
| B11 | 1,001 | 100% | Twelve extreme days, unprotected | 1 |

The examples are separate counterfactual arithmetic runs used to compare balance choices.
They are not an in-game saved-lives statistic and cannot be used as an achievement receipt.
The exposed fraction remains constant within each illustrative case, while actual game movement would vary it.
The dense and sparse cases show that losses follow actual resident scale and geographic coverage.
The long extreme case intentionally represents a catastrophic regional disaster.
If native review finds that outcome unsuitable for the intended campaign, tune the rates or profile distribution openly while preserving exposure-based danger and the moving wall.

The household-retreat factor is 0.7×0.45 + 0.2×0.40 + 0.1×0.80 = 0.475.
Full basic-quality mask input gives a breathing-channel multiplier of 1 − 0.65×0.55 = 0.6425.
Combining the two yields 0.7×0.45×0.6425 + 0.2×0.40 + 0.1×0.80 = 0.3623875 of unprotected direct risk.
An operated corridor raises the movement term, producing 0.4023875.
The maximum proven triple-overlap factor applies once, giving 0.489223125 for the protected case.
All these coefficients are design proposals.

## Union and current population

For two fronts each covering forty percent of a state's modeled residents, with ten percent common coverage, the union is seventy percent.
With two million current residents, the public estimate is approximately 1.4 million, not 1.6 million.
The dose uses the capped combined local intensity in the shared portion.
It does not debit each front's residents independently.

If 50,000 residents have actually left through migration before the next interval, the remaining state population is read before exposure is computed.
The event does not subtract those departures again.
Route deaths belong to the cohort transaction, and survivors credited to a destination appear in that destination's later current population.
Issued masks and household retreat do not remove residents from the public geographic estimate.

## Motion and local residence

| Profile | Travel depth | Minimum moving speed | Permitted stall | Maximum straight-passage residence |
| --- | --- | --- | --- | --- |
| P01 | 600 km | 120 km/day | 2 days | 7 days |
| P02 | 840 km | 120 km/day | 0 days | 7 days |
| P03 | 1,440 km | 120 km/day | 2 days | 14 days |

The calculation is travel depth divided by the minimum moving speed, plus permitted stall.
Crosswind width determines the breadth of the affected region and is not used in this residence calculation.
Curvature and rotational sweeps can extend real exposure and therefore require the same residence check against the actual path.
Overlapping independent fronts and later returns can produce longer total exposure, with the visible union and history making the reason clear.

At a nominal 150 kilometers per day, a forty-five to ninety-day journey covers 6,750–13,500 kilometers of path.
That supports continental and oceanic travel.
It does not guarantee that every baseline storm circumnavigates the map.

## Material and season duration

As an illustrative mathematical model, material retaining fractions 0.950, 0.967, 0.974, 0.980 and 0.984 each day reaches five percent of a fixed initial reference in approximately 58.40, 89.27, 113.72, 148.28 and 185.73 days respectively.
This checks that the proposed typical stage durations can be produced by bounded attenuation.
It is not the mandatory final storm equation or a scientific atmospheric prediction.
Additional finite source draws, larger evolved openings and different local concentration profiles change the result.

Conservative splits and merges do not extend material lifetime by themselves.
A child must not receive a new relative retirement rule that accidentally makes many tiny children live longer than the unsplit wall.
All material and intensity are subject to the original season's taper and stop.
The proposed taper envelope is full through day 330 and then declines linearly to zero at day 360.
The same envelope influences actual intensity, all consequences and the displayed wall.
The day-300 creation cutoff takes precedence over later apparent spare capacity.

## Capacity and receipt traces

| Trace | Required result |
| --- | --- |
| Baseline starts once | One active front, one spent birth and one global fired receipt |
| Stage II splits one into two | Parent retires, two children spend two births, material is conserved and active count rises by one |
| Stage II has seven births spent and attempts two more children | Reject or leave the parent intact under its valid pending policy because nine would exceed eight |
| Two fronts merge | Active count falls, replacement identity inherits history and spent births do not fall or rise |
| Three fronts contact the same desert | Each contact may be recorded, but all compete for the same finite family source and two-reseed allowance |
| A merged front revisits a used source | Previous source receipts remain spent despite the changed front ID |
| Day 300 creation request | Rejected even if scheduled earlier or if active slots are free |
| Day 330 surviving wall | Compulsory attenuation applies to every lineage and geographic consumer |
| Day 360 late callback | No new population, organization, building or railway mutation, with owned acute cleanup and missed-work diagnostic |

A capacity rejection is not a reason to erase an already admitted evolution.
The defining stage opening requires capacity before promotion.
Ordinary later creation opportunities can fail visibly and naturally within the remaining budgets.

## Physical-damage boundaries

Normal hours contribute one, severe hours two and extreme hours four toward the forty-eight-equivalent-hour grace.
Weakening contributes zero.
For example, twelve normal hours followed by twelve severe hours gives thirty-six equivalent hours and has not yet begun physical damage.
Three additional extreme hours reach forty-eight exactly.
Only further exposure qualifies for the current band's physical damage rate.
Changing intensity or front identity cannot restart the grace or replay its accumulated time.

The implementation must translate proposed damaged-capacity percentages into actual native building and railway units with observed before and after values.
The passage cap uses real working capacity at entry, with existing damage excluded from further eligible damage until repaired.
Same-passage repair does not reset the receipt or its cap.
Actual repair can make capacity physically damageable again, but cumulative damage under that passage still cannot exceed its remaining cap.

## Payment boundaries

Use a D2 fixture with eight working factories, infrastructure level three and airbase level two.
The proposed Support Equipment quote is the ceiling of 64 + 15 + 10, which is 89, plus 15 Political Power and two real civilian factories committed for forty-eight hours.
The factory commitment is a capacity requirement and time sacrifice, not an unlisted stockpile debit.

For a six-hundred-kilometer D3 route, the proposed full quote is 10 Political Power, 80 Support Equipment, 40 trucks and 2,000 fuel.
Its effective seven-day interval starts after twelve hours of successful preparation.
At every price boundary, the complete cost must be either successfully paid once or fail without a granted benefit and with exact actual-paid refund behavior.
The four resource components must remain visible in full tooltip detail even when the compact row shows only three icons.

## Future probability scenarios

The probability owner must inspect source before evaluating these named fixtures.
Willingness scores are not asserted click probabilities, and dynamic MTTH cumulative timing needs the actual game-version adapter.

| Fixture | Inputs and intended ordering |
| --- | --- |
| Q01 Eligible origins | Complete current family pool, equal family weights, source geometry and scenario exclusions. Political subdivision alone must not increase a family's share |
| Q02 Ordinary steering | Complete turn, speed and width profile pool. Persistent courses should dominate modest changes, with sharp reversals reserved for the appropriate evolved behavior |
| Q03 Evolution boundary | Chaos 199/200, 399/400, 599/600 and 799/800, enabled/disabled settings, stage age and remaining viable time |
| Q04 Late evolution | Near day 270 and at day 300, with free and full capacities. Impossible defining openings must not advance a stage |
| Q05 Branch survival | Same parent material with small and dominant allocations, desert and ocean paths, exact birth caps and deterministic seeds |
| Q06 Poor civilian response | Dense severe threat, low stocks and low PP. Free household retreat must remain a credible first response |
| Q07 Wartime scarcity | Essential route versus threatened industry, fuel reserve, occupied target and exact quote boundaries |
| Q08 Air preservation | Exposed concentrated wings versus wholly distant wings, strong and weak warning, known operating policy |
| Q09 Queue fairness | Highest-ranked target unaffordable, several lower-ranked targets useful and affordable. The queue must continue within its work bound |
| Q10 Repeated branches | Complete custom pool, declared cadence, scheduled control changes and material transitions. No unlimited creation or permanent candidate starvation |

Preserve immutable before-source bytes, hashes and the same scenario fixture for an audit, patch and compare cycle.
Use sampled simulation only for explicitly declared uncertain inputs.
No current-file self-comparison can replace missing before evidence.

## Remaining native evidence

Military symmetry, real air effects over land and sea, exact map projection, source-family completeness, actual population mutation, railway damage, factory commitments, response-locality and cleanup remain required implementation proof.
The native scenarios also need save and reload, host loss, control transfer, duplicate wakes, stale revisions, available DLC combinations and simultaneous owner activity.
The planning arithmetic resolves numerical relationships and exposes edge cases.
It does not close those engine gates.
