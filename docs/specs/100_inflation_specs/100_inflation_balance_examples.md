# Inflation: executed authored-model balance examples

## Evidence and assumptions

These recorded examples use integer arithmetic under the proposed parameters in Parts 2–4.
They establish that particular declared sequences produce the stated index values and timing conditions.
They do not establish HOI4 execution, AI choice, affordability, actual payment, native timer behavior, country eligibility, political probabilities or achievement completion.
The original author named `100_authored_arithmetic.py` and `100_authored_arithmetic_trace.json` as separately retained planning evidence.
Neither file was supplied with this import or is present at the named `docs/plans/100_inflation_plans/` destination.
The tables can be recalculated from their declared inputs, but they do not establish that the original script or trace was independently reproduced here.
No gameplay source was implemented or executed.

The external contribution includes the unresolved-crisis baseline of +5 and is already capped between −10 and +20.
The baseline is never added again.
Each ten-day review applies the effective old stance and current programme, resolves due milestones, reconciles continuity and objectives, then promotes the selected stance.
A selection made after a review affects promotion at the following review and index movement at the review after that.
The examples apply the accepted −100 to +150 index bounds, although the principal recovery sequences do not need clipping.

External pressure is held constant within each example.
This is a declared arithmetic input, not a finding about any particular country's economy.
Supply, political institutions, costs and enabled evolutions remain explicit scenario assumptions.
The examples do not prove all six planned achievements.

## 1. Currency recovery through the full taper

Start on day 0 at +150 with external pressure +20, effective and selected emergency restriction −20, and the maintained D11 programme −15.
The maintained commitment pauses Evolution IV runaway.
Both the strong-effective-stance and unrepaired-supply conditions are declared true at the day-30 milestone, so exactly one extra −20 shock applies.

The review dates are aligned to programme acceptance.
Select −10 after the day-30 settlement and select −20 after the day-70 review.
Those are valid single-step ordinary changes from −20 and −10 respectively, separated by more than the ten-day cooldown.
The final twenty-day taper occurs after the corresponding review, so day 70 still uses −15, day 80 uses −10 and day 90 uses −5.

| Day | Effective stance used | Programme used | Review movement | After review | Due milestone | Final index | Selection or promotion |
| --- | ---: | ---: | ---: | ---: | --- | ---: | --- |
| 0 | −20 | −15 | No review | +150 | Programme starts | +150 | Selected −20 |
| 10 | −20 | −15 | −15 | +135 | None | +135 | No change |
| 20 | −20 | −15 | −15 | +120 | None | +120 | No change |
| 30 | −20 | −15 | −15 | +105 | −45, then one −20 shock | +40 | Select −10 afterward |
| 40 | −20 | −15 | −15 | +25 | None | +25 | Promote selected −10 |
| 50 | −10 | −15 | −5 | +20 | None | +20 | Political reprieve can resolve |
| 60 | −10 | −15 | −5 | +15 | None | +15 | No change |
| 70 | −10 | −15 | −5 | +10 | Taper becomes −10 | +10 | Select −20 afterward |
| 80 | −10 | −10 | 0 | +10 | Taper becomes −5 | +10 | Promote selected −20 |
| 90 | −20 | −5 | −5 | +5 | Programme expires | +5 | Keep −20 |
| 100–160 | −20 | 0 | 0 each review | +5 | No fixed liability declared | +5 | Keep −20 through recovery |

The index is extreme throughout day 0 to day 30, giving 30 actual extreme days.
At day 30 the warning can issue with its complete chosen deadline, while the final index +40 begins nonsevere continuity.
Day 50 completes twenty nonsevere days.
The next committed movement reaches +15 on day 60, which remains nonsevere and avoids an immediate extreme return.
Reprieve can therefore resolve on day 50, including at a tied twenty-day warning expiry.

Stable continuity begins on day 70 at +10.
Day 80 remains +10 and day 90 reaches +5 without leaving the stable band.
After expiry, +20 external and −20 effective stance cancel exactly.
The index stays +5 through day 160, completing ninety continuous stable days.
The episode's hyperinflation and conditional-shock history justify that ninety-day requirement.
If other fixed liabilities exist, section 6's closing rule must still be applied before success.

This path relies on real maintenance and timely policy decisions.
Emergency access on day 0, the stability reserve, productive capacity and actual commitment execution were not engine tested.
D11 carries its initial stability loss up to five points and its programme opportunity cost.
The conditional milestone shock adds another actual stability loss up to five points and ninety days of 10% construction and 10% factory-output burden from day 30, lasting through day 120.
The combined adjustment slot observes the 40% construction and 30% output ceiling, while each obligation retains its own expiry.
The crisis spirit remains separate.
These costs are consequences to implement and verify, not material payments proven by the index calculation.

## 2. Lagged restriction can miss recovery

Consider a damaged episode at +20 with a frozen ninety-day recovery requirement, external +5, effective stance −20 and selected stance −10.
Without further changes, the executed values are:

| Day | Effective stance used | Final index |
| --- | ---: | ---: |
| 10 | −20 | +5 |
| 20 | −10 | 0 |
| 30 | −10 | −5 |
| 40 | −10 | −10 |
| 50 | −10 | −15 |
| 60 | −10 | −20 |

Stability begins on day 10 but breaks on day 50 after only forty days.
Touching the stable band has not completed the damaged episode.
Selecting −10 never removes the old −20 movement at day 10.

A timely alternative is to select −5 after day 30.
Day 40 still uses −10 and reaches −10, then promotes −5.
The following reviews apply external +5 and stance −5, holding −10.
That sequence preserves the stable attempt, subject to other declared liabilities and costs.
It illustrates a valid lagged intervention, not proof that AI will select it.

## 3. Prompt major fiscal containment with Currency Crisis disabled

With D11 disabled, emergency consolidation remains available under the accepted D03B entry conditions.
Assume +150, external +20 and already effective −20 restriction.
Acceptance applies −30 once, then maintained −15 programme pressure with runaway paused.

| Time | Applied movement | Final index | Current band |
| --- | ---: | ---: | --- |
| Acceptance | −30 | +120 | Extreme |
| Day 10 | −15 | +105 | Extreme |
| Day 20 | −15 | +90 | Severe, below extreme |
| Day 30 | −15 | +75 | Severe |
| Day 40 | −15 | +60 | Severe boundary |
| Day 50 | −15 | +45 | Nonsevere |

If the extreme interval starts at acceptance, it lasts twenty days and cannot alone meet the thirty-day warning requirement.
Prior exposure remains retained. Prompt containment does not itself cancel a warning already earned from that history.
The programme's combined 40% construction and 30% factory-output profile, actual stability loss up to ten points and ninety-day obligation make the correction costly.
Abrupt cancellation preserves the original obligation, applies the accepted +10 release once and does not replay the opening −30.
The shared 120-day major-programme reuse interval prevents switching to settlement for another immediate correction.
Actual eligibility, reserves and cost execution remain untested.

## 4. Severe deflation needs an exit plan for stimulus

Start at −90 with external −10 and emergency support +20.
For this example D13 has already passed its first ten-day startup and has fifty days remaining, so its +10 contribution is valid at the first shown review.
The final review precedes its expiry on day 50.
The episode has a qualifying ninety-day contraction-shock history.

| Day | Keep emergency support: final index | Select +10 after day 30: final index |
| --- | ---: | ---: |
| 0 | −90 | −90 |
| 10 | −70 | −70 |
| 20 | −50 | −50 |
| 30 | −30 | −30 |
| 40 | −10 | −10 |
| 50 | +10 | 0 |
| 60 | +20 | 0 |
| 70 | +30 | 0 |

The untreated support combination raises the index by twenty points per review until programme expiry.
Stable continuity starts on day 40, but continued emergency support raises prices to +20 on day 60 even after D13 ends.
The stable attempt therefore breaks after twenty days.

In the managed column, selecting +10 after day 30 leaves +20 effective for day 40, then promotes +10.
Day 50 has external −10, stance +10 and D13 +10, reaching 0.
After expiry, external −10 and stance +10 cancel.
The index can remain 0 to day 130, completing ninety continuous stable days from day 40 under these declared inputs.
No free programme startup, lasting building award or economic-history reset is assumed.

## 5. One OR shock and exact boundaries

The conditional settlement shock is one −20 movement when either condition holds.
Starting from +105 immediately before the fixed correction gives:

| Effective restriction at most −10 | Supply unrepaired | Fixed correction | Extra shock | Final index |
| --- | --- | ---: | ---: | ---: |
| No | No | −45 | 0 | +60 |
| Yes | No | −45 | −20 | +40 |
| No | Yes | −45 | −20 | +40 |
| Yes | Yes | −45 | −20 | +40 |

Both true conditions do not produce −40 or two shock costs.
The no-shock result +60 is still severe, so it does not begin nonsevere reprieve.

| Index | Stable | Severe | Extreme |
| --- | --- | --- | --- |
| −85 or −80 | No | Yes | Yes |
| −75 or −60 | No | Yes | No |
| −55 or −15 | No | No | No |
| −10, 0 or +10 | Yes | No | No |
| +15 or +55 | No | No | No |
| +60 or +95 | No | Yes | No |
| +100 or +150 | No | Yes | Yes |

Severe boundaries belong to severe state.
Stable boundaries belong to stable state.
A same-time crossing adds no fictitious elapsed exposure, although every actually applied movement can interrupt continuity.

## 6. Fixed closing liabilities can deny success despite a stable final value

Suppose a completed ninety-day attempt reaches its closing check at +5.
Its remaining recorded fixed liabilities, settled in their due order, are +10 followed by −10.
The executed sequence is +5 → +15 → +5.

The first applied movement leaves the stable band and resets continuity immediately.
The second returns prices to +5, beginning a new attempt at that timestamp.
Recovery is denied even though the final number equals its starting value.
It would be incorrect to net the two liabilities to zero before applying them, or retire the index while the first liability remained unpaid.
The consumed installment receipts prevent later callbacks from applying them again.
This arithmetic does not establish actual receipt consumption or native callback idempotence.

## 7. Warning ties and the limit of late rescue

| State at expiry after all due economic movements | Result under the accepted rule |
| --- | --- |
| Twenty continuous nonsevere days, with next committed index +20 | Reprieve resolves before tied failure. |
| Twenty continuous nonsevere days, with next committed index +60 | Reprieve still resolves, since +60 is severe but not extreme. |
| Twenty continuous nonsevere days, with next committed index +100 | No reprieve, since the commitment returns directly to an extreme. |
| Ten continuous nonsevere days and next review remains nonsevere | One ten-day extension can complete the twenty-day requirement. |
| Fifteen continuous nonsevere days and next review remains nonsevere | One five-day extension can complete the requirement. |
| Nine continuous nonsevere days | No earned extension. |
| Ten nonsevere days but next review reaches +60 | No extension, since the forecast is severe. |
| A prior extension was already consumed and the streak breaks | No second extension. |

Completed reprieve requires the known next movement to avoid an extreme.
The earned extension has the stricter requirement that the next review remain nonsevere.
The executed +60 fixtures distinguish these gates, while the +100 fixture blocks completed reprieve.

A due same-time movement that breaks the streak is processed before this table's success check.
The rule does not preserve an obsolete twenty-day streak after a real excursion.

Starting currency settlement at +150 on the first day of an already issued twenty-day warning reaches +120 on expiry day 20 and +40 only on day 30.
It cannot earn the necessary ten nonsevere days by that deadline.
Prompt fiscal containment also cannot guarantee rescue from that already issued warning, since it remains severe through day 40.
Earlier intervention matters.

If the currency programme instead receives a twenty-day warning on programme day 20, expiry is day 40.
Use section 1's policy sequence, selecting -10 after day 30 and promoting it after the day-40 review.
Its day-30 move to +40 gives ten continuous nonsevere days by expiry.
The next committed review reaches +20, so a single extension to day 50 is earned and twenty nonsevere days then permit reprieve.
These examples demonstrate coherent early and late timing under fixed inputs.
They do not validate political branch selection, actual warning timers or a guarantee against unforeseen external changes.
