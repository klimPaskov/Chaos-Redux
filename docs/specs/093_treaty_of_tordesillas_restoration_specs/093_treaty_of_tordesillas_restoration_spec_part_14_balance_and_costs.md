# Treaty of Tordesillas Restoration: balance and cost register


## Status of these numbers

This is the canonical proposed tuning register.
Values are design choices for implementation and testing, not measurements from a running game.
Earlier parts explain behavior.
If a later balance change is approved, update this register and the relevant acceptance tests together rather than leaving conflicting prices in multiple files.

Most player-facing costs, durations, and changes use multiples of five.
The geographic meridians, percentage formulas, fixed-point accounting, one-time identities, and quarter-package installments are structural exceptions.
No action needs more than four spendable resource types.
This design does not require a command-power payment above the project's conservative 60-point limit and currently specifies no mandatory command-power cost.

## Diplomatic scale

| Item | Proposed value | Meaning |
| --- | --- | --- |
| Formal public Galicia demand | 25 political power from Portugal | One valid opening demand, not a monthly purchase |
| Final diplomatic pressure | 50 political power from Portugal | One escalation after a live refusal |
| Compensated cession administration | 50 political power per signing crown | Charged only when the agreement is valid |
| Standard compensation material | 1000 infantry equipment and 50 support equipment | Delivered to the legal owner, with recipient-approved scaling |
| Civil-war contract administration | 25 political power from Portugal | Once on a signed contract |
| Restoration conference | 50 political power per participating crown | No debit for an invalid or declined preflight |
| Reconciliation conference after serious breach | 50 political power per participating crown | Restitution material negotiated separately |
| Conference cooldown | 180 days | A material new circumstance is also needed after rejection |
| Ordinary diplomatic answer window | 30 days | Not an active performance mission |
| Civil-war final delivery after early victory | 30 days | Only remaining signed obligations |
| Non-revision recovery after serious breach | 90 days | No aggression or prohibited enemy support |

The material compensation can be negotiated at one, two, or three standard packages according to the legal owner's size and the value of the settlement.
Both players see the concrete price.
An AI must reject an unaffordable package rather than accepting a promise that bypasses payment.

A peaceful Galician cession can apply a one-time 5-point war-support loss to Spain and a 5-point gain to Portugal.
These are political consequences, not discounted resource costs.
Recognizing an existing border without transfer does not repeat the prestige change.

## Civil-war package

One standard aid package contains 1000 infantry equipment, 50 support equipment, and one logistical component chosen at signing: 5 trains, 250 motorized equipment, or 5000 fuel.
These are alternative signed logistical components, not freely interchangeable deliveries after the recipient has agreed.

Use one package for a recipient with up to 10 owned military factories at signing, two for 11 through 25, and three above 25.
The scale is frozen for that contract.
The result is a useful starting proposal rather than an assertion that factory count perfectly measures wartime need.
A mutually approved amendment can change the contract without retroactive credit farming.

Infantry equipment contributes 50 percent of Aid Fulfillment, support equipment 30 percent, and the chosen logistics component 20 percent.
Each contribution is capped at its promised amount.
Portuguese volunteers that serve the recipient for at least 90 days of the contract add 10 percentage points once; they cannot cover any component's own 50 percent minimum, and total fulfillment is capped at 100.
The earned-transfer threshold is 75 percent total, with at least 50 percent of each required component delivered.
Full fulfillment is 100 percent.

A standard delivery period is 180 days.
Each installment ships one quarter of every signed component, or the remainder when less is outstanding, so four installments complete the contract.
When Portugal lacks part of a component, the installment ships what is in stock and the shortfall stays outstanding.
Installments have a 30-day cooldown and no separate diplomatic reward.

The Portuguese AI retains at least the larger of its current verified critical equipment deficit or a 25-percent strategic reserve for the relevant component.
This is an AI planning rule, not a restriction on a human who knowingly accepts the risk.
The exact deficit and reserve calculation needs installed-source inspection.
If it cannot be measured honestly, do not claim the AI reserve test has passed.

## Confidence register

| First settled origin | Starting Confidence |
| --- | --- |
| Fully fulfilled aid bargain honored | 70 |
| Earned bargain honored below full fulfillment | 65 |
| Peaceful compensated cession | 60 |
| Agreed renunciation or recognition of the existing border | 55 |
| Dispute merely postponed | 35 |
| Refusal without a final settlement | 30 |
| Coercive Galician settlement | 25 |
| Portugal backed the defeated Spanish side | 20 |
| Earned bargain repudiated | 15 |

Before the first outcome, the provisional value is 40.
Apply the first settled origin once.
Later amendments use changes to the existing value, not a reset to whichever origin yields the best number.

When an origin has already been established, a later final border agreement adds 15 once instead of resetting the origin value.
A later honored aid contract adds 20 once if earned or 25 once if fully fulfilled, and cannot also initialize a second origin.
These gains require distinct completed obligations and do not repeat for re-signing the same settlement.
A completed material restitution can add 15 once for that breach.
A genuine agreed mutual-support objective can add 5, at most once in 180 days and at most 15 from this general support family across the campaign.
An actual major breach subtracts 20 once.
Deliberate aggression against the partner suspends the treaty regardless of the remaining numeric value.

A settled, breach-free compact can recover 5 after each 90-day period, but passive recovery stops at 60.
Unresolved grievances stop passive recovery.
This permits a limited alliance to heal while requiring a real cooperative achievement for the 65-point world-end gate.

Restoration needs 50 Confidence.
Evolution IV needs 60.
World-end entry needs 65.
Each also requires the specific political conditions described in its part.
Confidence is clamped between 0 and 100 and is not paid as a currency.

## Regional tiers

Determine the tier from the originally enrolled states' frozen activation population and state count, taking the higher tier from either criterion.
Small is at most 5 million people and at most 3 states.
Medium is at most 20 million people and at most 8 states.
Larger enrollments use the large tier, with the normal coherent-region ceiling of 12 states.
A registered exceptional region above that ceiling needs an explicit design review, not a silent discount.

| Requirement | Small | Medium | Large |
| --- | --- | --- | --- |
| Minimum continuous ownership and control | 60 days | 90 days | 120 days |
| Minimum compliance in every enrolled state | 30 percent | 40 percent | 50 percent |
| Maximum resistance in every enrolled state | 20 percent | 15 percent | 10 percent |
| Base project duration | 90 days | 150 days | 240 days |
| Political power | 50 | 75 | 100 |
| Support equipment | 50 | 100 | 200 |
| Trains | 0 | 5 | 10 |

Every threshold applies to each enrolled state; there is no regional average.
A coercive settlement lowers the compliance floor by 10 points (20, 30 and 40 percent).
A recently conquered enrollment, defined as any enrolled state held for fewer than 180 days, adds 60 days to the base project.
A coercive local settlement uses that same additional preparation period, without stacking a second identical 60-day surcharge.

Two project slots are available at Evolution III.
The capacity focus changes this to three.
The mutually exclusive acceleration focus multiplies duration by 0.80.
The concentrated pace multiplies support-equipment cost by 1.50 and duration by 0.85.
Where both speed factors apply, compose them before rounding upward to the next five days.
No project is shorter than 60 days.

Any project pauses while an enrolled state breaks its compliance floor or resistance ceiling, loses supply, or is at famine or catastrophic famine Food Security.
A concentrated project that pauses for any reason continues at the ordinary duration from that point, and the extra support equipment is not refunded.
This creates exposure to actual deterioration without inventing a random disruption roll.

Loss of control or required legal authority for 60 consecutive days forces cancellation or a valid reduced original enrollment.
A temporary supply failure pauses progress.
Recovery does not enroll newly conquered states.

## Cancellation accounting

Before a successful start, a failed preflight costs nothing.
After a project begins, political power is non-refundable.
Equipment refunds equal half of the actual paid equipment associated with the uncompleted fraction of work, rounded down to whole five-unit quantities and capped at the actual unrefunded receipt.
The final remainder may be zero.

For example, a project that actually paid 100 support equipment and is half complete can refund at most 25 support equipment on ordinary cancellation.
A later discount does not change that receipt.
A second cancellation or reload cannot issue the refund again.
An implementation error before any project effect requires an explicit compensating transaction rather than pretending the engine rolled back automatically.

Delivered aid or compensation is different.
The recipient already has the goods.
Refund cannot duplicate those goods.
Any agreed return must be an actual reverse transfer from available stock, and combat losses or equipment already deployed are not recreated.

## Global pacing

| Item | Proposed value |
| --- | --- |
| Evolution thresholds | 200, 400, 600, 800 Chaos |
| Baseline eligible evolution opportunity mean | Approximately 90 days, subject to verified MTTH modifiers |
| World-end threshold | Strictly greater than 1000 Chaos |
| Entry reach per crown | At least 70 percent of weighted sphere |
| Entry direct integration per crown | At least 40 percent of weighted sphere |
| Entry stability period | 90 consecutive days |
| Final integration per crown | At least 60 percent of weighted sphere |
| Final partition stability period | 90 consecutive days |
| Standard final-campaign ultimatum | 120 days |
| Major theater objective | At least 180 days, adjusted for genuine difficulty |
| Sustained territorial-collapse test | Reach below 40 percent or integrated controlled share below 20 percent for 180 days |
| Loss of independent treaty-power status | Failure review after 90 days |

## Balance acceptance

Test Portugal at several economic scales, victorious and defeated Spanish intervention, a peaceful strong Spain, and both late-game empires.
A material contract should be useful without requiring Portugal to disarm itself.
Regional coring should be materially faster and less repetitive than the installed Anarchist Spain benchmark while retaining meaningful preparation.

The two halves need not have identical difficulty.
Neither crown should be consistently unable to reach the final requirements under competent play.
Adjust logistics, focus-path usefulness, project capacity, or diplomatic opportunities before resorting to free armies or weakening the two-sided world-end requirement.
