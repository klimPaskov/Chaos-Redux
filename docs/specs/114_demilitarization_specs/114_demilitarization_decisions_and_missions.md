# Demilitarization: military responses and missions

The response category contains four decision families. Each addresses a different military problem: living conditions, experienced cadres, an army that is too fragmented to sustain, or attendance that has broken down.

All labels are working labels, not final localisation. Decision titles, button text, descriptions, and mission prose must be written during implementation from the direction here.

## A small, usable category

Show the category when the country has an Event 114 territorial obligation, active service system, unresolved formation notice, or outstanding service programme. Before Desertion Crisis, its short description explains the actual territorial rule and war transition.

When service management is active, show Army Cohesion, its band, the main current pressure, the next review date, and any endangered formation. Describe the number and names of usable states as native geographic facts.

Show at most four actionable decision rows plus one urgent muster mission. Put the endangered formation first. Use a short target list within the relevant decision family, ordered by urgency and legitimate eligibility. Never list every world state or every division at once.

When recovery is pending, show at most one recovery-objective row below the urgent muster. It summarises the highest outstanding target and current clean-review progress. Several loss receipts remain internal and do not create a list of duplicate mission rows.

A player should be able to read a decision's current cost, duration, eligibility failure, likely benefit, and cancellation rule before committing. The first confirmation option for an irreversible consolidation is a harmless cancel action. Revalidate the exact unit and resource cost when the player confirms.

## Shared programme rules

Service conditions, cadre retention, and attendance enforcement share one active programme slot. Consolidation is a separate instant action with its own cooldown. All response activation cooldowns count calendar days. Review, muster, and protection intervals count accumulated peacetime days where explicitly stated.

Costs are real start costs. A programme does not reserve a future discount or create a resource grant. It must revalidate available political power, command power, army experience, industrial commitment, selected target, and current peace before charging.

One country can receive one completion receipt for one programme. An invalid target at completion does not convert into a free country-wide benefit.

Durations below run during an uninterrupted peacetime programme. War entry cancels the programme, releases remaining civilian-factory commitments, and preserves sunk political, command, and experience costs. It grants no completion benefit. Programme cooldowns start on activation and survive cancellation.

A suspended muster notice is different from a cancelled response programme. The notice retains its remaining peacetime interval. The player must choose a new valid response after peace if the notice remains unresolved.

### Work due on the same date

Resolve the country's current war and ownership state first. Then settle already-due personnel returns and legitimate programme completions. Apply the ordinary cohesion review and its partial incident next, then resolve due muster notices from the resulting current state. Publish reports and achievement checks after the physical transactions settle.

Snapshot whether a programme legitimately covered the instant immediately before its due completion. A service-conditions programme completing on an ordinary review boundary still earns that review's +4 benefit once. A cancelled programme earns no benefit for time after cancellation. Thus an uninterrupted 28-day programme spanning two reviews earns both review benefits and its completion result.

A cadre programme that was validly started early enough to finish on the muster deadline therefore completes before the notice is judged. An action started after the due instant cannot claim retroactive completion. Each due item is consumed once under this ordering.

## D114-01: improve service conditions

**Purpose.** Keep soldiers supplied and housed while their normal garrisons and expectations of service have been disrupted.

**Visibility.** Desertion Crisis is active locally and an eligible fielded army exists. Keep the row visible with a reason when another programme occupies the slot or industrial capacity is unavailable.

**Availability.** The country is at peace, cohesion is below 90, no programme is active, and the 56-day activation cooldown has expired.

**Cost and duration.** Spend 25 political power and commit civilian factories for 28 days. The intended commitment is one factory below 50,000 eligible fielded manpower, two from 50,000 to 249,999, and four at 250,000 or more. Determine the bracket at activation and keep it fixed for that programme. Require the full chosen commitment.

**Effects.** While the programme is active, add 4 cohesion at each ordinary review. Completion adds 12 cohesion, provided an eligible army still exists and the industrial obligation was actually served. Clamp at 100. This programme can reverse a deteriorating trend but does not grant immunity from partial desertion.

**Failure and cancellation.** War cancels as described above. Loss of the required industrial commitment cancels the programme immediately without a completion reward. Release remaining commitments and retain sunk costs. Record the actual served period and preserve the activation cooldown.

**AI.** Prefer when cohesion is 45–74, industrial resources are available, and no formation faces a nearer deadline. Avoid spending the last available civilian capacity during a genuine reconstruction emergency when another valid response is available.

**Writing direction.** Focus on accommodation, rations, predictable leave expectations, and the practical work of running inland barracks. Use restrained administrative irony in the completion acknowledgement. Do not imply that soldiers are being purchased.

**Asset.** A ration tin with a folded blanket, A114-D01.

## D114-02: retain experienced cadres

**Purpose.** Preserve the organisation and expertise of a real formation that could otherwise unravel.

**Visibility.** Desertion Crisis is active and at least one legitimate formation is available. Prioritise the unit named by an endangered-formation notice.

**Availability.** The country is at peace, no programme is active, the formation has existed for at least 28 days under a verifiable service identity, and the 42-day activation cooldown has expired. The formation must be eligible for the country's military accounting and contain at least 500 soldiers.

**Cost and duration.** Spend 10 army experience and 15 command power. Run a 7-day programme tied to the selected formation. The formation must remain under the same legitimate personnel owner and remain outside combat. This leaves a real response window inside a newly issued 14-day muster notice.

**Completion.** Add 15 cohesion. Resolve that formation's open muster notice, if present. Protect the formation from selection for a new full-dissolution notice for the next 28 peacetime days. Partial desertion remains possible.

**Place requirement.** Where legal domestic space exists, the formation must be in a legal same-controller cantonment at completion. For a country with zero legal space, accept only the verified native preservation state required by the core specification. Do not invent a free capital exemption.

**Failure.** If the formation disbands, transfers owner, merges away, or enters an unresolved native operation, close the programme without a reward. War cancellation does not preserve a completed protection that was never earned.

**AI.** Highest priority when the programme can finish before a current muster deadline and the target is valid. Otherwise favour a substantial experienced formation over a newly raised token unit.

**Writing direction.** Present the decision as recovering attendance, clarifying service obligations, and keeping command knowledge inside the formation. Success acknowledges the specific formation and its continued existence.

**Asset.** A secured service badge and paybook, A114-D02.

## D114-03: consolidate a weakened formation

**Purpose.** Deliberately reduce organisational fragmentation before uncontrolled desertion removes a unit on worse terms.

**Visibility.** A valid weakened formation exists and at least one other eligible domestic formation will remain after the action.

**Availability.** The country is at peace, cohesion is below 70, the 90-day activation cooldown has expired, and the selected formation has less than 75% of its highest verified actual manpower during the previous 90 calendar days. It must also have a committed Event 114 personnel-loss receipt within the previous 56 calendar days. Enlarging a template without losing actual soldiers does not qualify. It must have at least 500 actual soldiers and have existed under the current legitimate owner for at least 60 days. It must represent at least 1% of eligible fielded manpower.

A formation created by splitting or renaming a recently created unit does not inherit fictitious age. The formation must not be fighting, encircled, expeditionary, in an unresolved transfer, or needed as the last remaining eligible formation.

**Cost.** Spend 5 army experience and deliberately disband that exact formation. The sacrifice is its independent organisation and accumulated experience.

**Effect.** Return only its actual manpower and equipment through verified native voluntary disband semantics. Add 12 cohesion, capped at 70 for this action. If it was the endangered formation, close that notice as voluntary consolidation.

The action does not enter soldiers into the delayed-return system, qualify as spontaneous dissolution, trigger a recovery achievement, or create a direct Chaos reduction.

**Confirmation.** Show the selected formation, current soldiers, actual equipment-return basis, and the loss of formation identity. Place harmless cancellation first. At confirmation, verify the same unit identity and current conditions. If it has vanished, cancel without charging or selecting a replacement.

**AI.** Consider when the army has several depleted formations, cohesion is low, and preserving all units is unrealistic. Avoid consolidating the only substantial trained formation or a unit whose lawful disband would fail another event's independent condition. Never disband merely because a division-count target would be easier.

**Writing direction.** Explain the deliberate choice to preserve people and equipment while losing a formation. The acknowledgement should be sober and practical, without claiming a painless reform.

**Asset.** Two infantry collar patches joined by a leather strap, A114-D03.

## D114-04: enforce attendance

**Purpose.** Restore short-term obedience when the command structure is close to losing control.

**Visibility.** Desertion Crisis is active, an eligible fielded army exists, and cohesion is below 45.

**Availability.** The country is at peace, no programme is active, stability is at least 15%, and the 84-day activation cooldown has expired.

**Cost.** Spend 30 political power and 10 command power. Reduce stability by 8 percentage points immediately. The action cannot create a negative resource balance.

**Effect.** Add 20 cohesion immediately. For 28 days, halve the country's ordinary review incident chance after its current cohesion band is determined. The national loss ceiling and per-formation loss percentages stay unchanged.

**Aftereffect.** At the end of the enforcement period, subtract 10 cohesion once. Any early cancellation of an activated enforcement programme, including war, an empty eligible army, or an invalid continuing actor, settles this aftereffect once through the legitimate owner or succession transaction. Retain the separately committed backlash receipt and its remaining peacetime interval unless it was already consumed. Cancellation cannot retain the initial gain without its corresponding consequence.

**Backlash.** Commit one backlash roll at activation. Its chance is 35% when pre-action stability is below 35%, otherwise 15%. Resolve it after seven peacetime days, or retain its remaining interval through war. A backlash subtracts 10 cohesion and 5 stability points once and creates a country report.

When an existing mutiny or unrest system has an applicable acceptance hook, pass a single external pressure receipt to that owner. Do not create a second copy of the same incident or a guaranteed civil war. If the hook is absent, the defined domestic cohesion and stability consequence remains the complete Event 114 outcome.

**AI.** Prefer only when a severe formation crisis is imminent and constructive responses cannot finish or cannot be afforded. Weight it strongly downward below 35% stability unless the alternative is a near-term loss of a major formation.

**Writing direction.** Use the language of registers, attendance, and command authority. The report may show the distance between a formally complete roster and the men actually present. Avoid celebratory repression or invented quotations.

**Asset.** A whistle and closed duty roster, A114-D04.

## M114-01: muster an endangered formation

This automatic mission is created only by the severe-state conditions in the desertion specification. It is tied to one exact formation and lasts 14 accumulated peacetime days.

The player can succeed by completing D114-02 for that target, or by having cohesion at least 35 and a valid surviving target at the due check. D114-03 deliberately settles the matter through consolidation, recorded as a different disposition.

Classify the due outcome before applying the failed-muster penalty. With a valid unresolved target and cohesion from 25 to 34, apply the failed-muster cost of 5 cohesion once and perform no dissolution roll. Below 25, when the other severe-state conditions remain valid, perform one 25% dissolution roll and then apply the same cost once. The cost is separate from the ordinary review's 12-point negative cap and cannot retroactively create a dissolution roll.

Every failed notice that leaves the formation intact receives a 28-peacetime-day notice cooldown. A vanished target, invalid ownership, active combat, or lost authority instead closes with its true cancellation disposition and no invented failed-muster cost. A valid target at cohesion at least 35 succeeds as described above.

Display the true remaining interval, the target, and the available response. Changes of location, controller, or presentation must not create a new deadline. A stale notification cannot delete a newly selected unit.

Use the mission-specific A114-M01 source and output. It coordinates with the cadre motif but has its own consumer, brief, and original artwork. The threatened formation is a dynamic native text value, not generated lettering.

## M114-02: restore dependable service

This is a recovery objective attached to a charged personnel milestone or verified spontaneous dissolution. It does not add a second meter.

The objective becomes visible after a charged personnel milestone or a verified spontaneous dissolution. At the incident's committed result, store the actual post-incident eligible fielded manpower and the newly acknowledged, unrecovered personnel loss covered by its receipt. The recovery target is that post-incident army plus 75% of the acknowledged loss, with the added amount rounded up to whole soldiers. This always requires actual rebuilding above the post-loss state.

Reach that target, then maintain it and cohesion at least 70 through two subsequent clean reviews. A clean review has no Event 114 personnel debit, spontaneous dissolution, or unresolved endangered-formation notice. The delayed personnel return contributes only after it actually arrives and the soldiers are fielded through normal reinforcement or recruitment.

Completion creates one containment receipt. It can qualify for the mapped Chaos reduction if the original loss had an unreversed Event 114 charge. If a personnel milestone and a full dissolution cover any of the same persons, they cannot create two recovery entitlements for those persons. Longer achievement requirements remain separate.

There is no countdown failure penalty. War pauses the clean-review requirement but does not turn an unfinished recovery into success. A further qualifying loss resets the clean-review streak and creates its own immutable recovery target. Keep the older unrecovered targets. The applicable target is the highest outstanding target, so a new loss cannot lower the army level needed for recovery. Settle overlapping personnel coverage once and consume only the legitimate original charge entitlement.

Use mission-specific A114-M02 with its own original source and output. Coordinate its recovery motif with the broader family without reusing a decision or achievement subject.

## Failure and scarcity remain playable

A poor country can lack industrial capacity for D114-01. It can still choose cadres, consolidation, or enforcement when those costs and targets are valid. An army with no suitable depleted formation cannot invent a consolidation target. A country with no command resources may have to accept partial losses while rebuilding the resources for a response.

Scarcity changes the choice. AI and player eligibility are identical. Under Total, a country without industrial capacity, useful army experience, or sufficient command resources may remain in severe service conditions. That harsh outcome is intentional at this stage. It can preserve the remaining real forces, use resources when they become available through normal play, or enter a legitimate war, which releases Event 114's peacetime pressure. The design does not promise that shrinking an army alone removes geographic crowding or guarantees peacetime recovery.

The category should explain a genuine absence of an affordable action in ordinary language. It should not present disabled actions as clickable or imply that a technical accounting failure is a gameplay requirement.

## Event 096 boundary

A response never unlocks templates or grants an army allowance. D114-03 can change actual army size and D114-02 can work with an existing template, but Event 096 alone evaluates its own conditions.

Any interoperation refresh must be read-only with respect to Event 096 restrictions. Its own owner may subsequently settle a condition from the actual changed army. Entering war is not an Event 114 shortcut to that settlement.

