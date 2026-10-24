# 120 Widespread Mutiny, Part 2: Responses, losses and recovery

## The response surface

The ordinary decision category shows the two values, the most urgent cohort, its grievance, its actual affected strength and the next deadline. Normal phases expose three to five primary actions. At most three missions can be active. A native target choice or a cohort report changes which case is being viewed. AI evaluation is independent of the human's currently viewed case.

Negotiation, suppression and deliberate inaction remain available when structurally possible. A state with few resources retains a negotiated release or limited stand-down option. A resource shortage cannot force the player to buy political power to escape a crisis whose grievance is lack of supplies.

The category changes with the phase. Starting a relief commitment replaces its start action with the active mission and a cancellation action explaining its actual refund and consequences. Settled actions disappear. An unavailable action explains the precise missing authority, force, transport or payment, rather than presenting a clickable-looking control that silently fails.

## Costs and commitments

The cost anchors below are proposals for ordinary medium-sized cases. The final quote scales with actual affected manpower, distance, route capacity and the chosen ambition. Political power and command power costs use round increments of five. Equipment quantities, native units and formula-derived results retain the precision required by the resource.

Every action has at most four spendable types. Command power never exceeds 60. Formation downtime, a temporarily occupied civilian factory, a route requirement or the presence of loyal troops is displayed separately from immediately consumed resources. Such commitments still have real opportunity costs.

Use a size factor `q = clamp(affected live manpower / 20000, 0.5, 3)`. The price is based on the named cohort at the moment of commitment. A settled smaller cohort cannot be replaced with a larger cohort under the same paid receipt. A material scope change requires a fresh disclosed agreement or a proportional refund and cancellation.

| Working action | Ordinary quote and commitment | Why the cost matters |
| --- | --- | --- |
| Negotiate a service compact | Political power `r5(30q)`, Army XP `r5(10q)`, then the selected practical promise | Gives delegates authority and requires a change in military practice |
| Execute leave and rotation | Command power `r5(15q)`, 1 to 5 trains or the verified local road equivalent, 500 to 3000 fuel when transport actually consumes it, 20 to 40 days of formation downtime | Preserves experienced soldiers by taking them out of current service |
| Repair the relief route | Support equipment `ceil(50q)`, trucks `ceil(25q)` when the road route uses them, one to three civilian factories committed for 30 to 60 days | Fixes the material grievance and competes with construction or other supply needs |
| Agree a discharge schedule | Political power `r5(25q)`, a verified transport slot for remote units, 30 to 90 days to execute the schedule, then the agreed 90 or 180 days of personnel protection | Ends the contested obligation at the cost of field strength |
| Immediate local discharge | Zero spendable resources, actual release of the selected formation, 180 days of protected personnel unavailability | Gives a poor country a genuine exit by sacrificing the field formation and accepting local equipment-recovery limits |
| Prepare loyal-force containment | Command power `min(60, r5(20q))`, Army XP `r5(10q)`, fuel only for motorized deployment, 10 to 20 days of named loyal-force commitment | Pulls reliable troops away from other duties and risks their cohesion |
| Offer a return amnesty | Political power `r5(20q)`, 30 days of a credible receiving and review process | Can recover recorded surviving deserters without inventing recruits |

The transport alternatives are exclusive ways to fulfill the same route. The player pays the selected real method, not trains, trucks and fuel merely because all can be listed. A foot movement on a short secure route can use time and readiness instead of a fictitious fuel bill. A supply repair only charges the equipment it actually consumes.

Factory commitments use a verified native reservation or a complete owner contract. They cannot be described as part of the shared discount framework until that adapter exists. Ordinary payable resources use the exact shared quote, payment and receipt contract where supported. Physical formation release and time are not discounted quantities.

The inline cost row shows at most three icon-backed values and at most four ordinary words. The full tooltip includes every payment, commitment, duration, target and refund rule. Eligibility, displayed affordability and actual deduction use one authoritative current quote. A quote is recalculated before a click takes effect. Once paid, later installments, completion and refund refer to the actual paid receipt.

## Negotiation: promise, delivery, assessment

The first negotiation acknowledges a specific demand and offers one feasible commitment. The opening promise reduces Disaffection by 10 once and suspends a scheduled spread check for up to 10 days. It does not return lost equipment, restore missing soldiers or permanently end refusal.

Leave requires the named formations to leave the disputed duty and remain relieved for the promised period. The player sees the replacement need and resulting weakness of the front. Moving the same formation back into the prohibited task breaks the promise. Renaming its template, lending it to a subject or changing its commander cannot clear the obligation.

Supply relief requires an actual delivery or repaired capacity, followed by 10 days of sustained improvement. Stockpiling equipment elsewhere does not satisfy the mission. A construction or transport project already completed before the demand arose counts if it demonstrably removes that grievance. The player should not repeat the work solely to obtain an event receipt.

A command compact defines accepted officers, access to delegates and a review of the disputed practice. It can reduce the immediacy of disobedience without guaranteeing agreement on every future order. If the government removes an existing commander, it changes or transfers the actual character and role with ownership checked. It does not create a fictional duplicate of a real person.

At delivery, the practical promise is assessed before the political reward. A completed compact reduces Disaffection by 20 and raises Agreement confidence by 20 once. If confidence is at least 70, every surviving eligible formation that accepted the compact can return after its actual rest period. At confidence 40 to 69, a disclosed dissenting group can choose continued leave or agreed discharge. Below 40, an external guarantee, further verifiable delivery or a smaller negotiated obligation is required for a reliable return. Those cases keep an exit path and do not consume a second compact fee merely to reveal that the first was insufficient.

The degree of dissent is chosen from the actual cohort and its recorded history. It cannot fabricate a fixed percentage of new soldiers. Exact partial-personnel operations need the proof described in the implementation handoff. If only whole formations can be addressed, that limitation must be resolved before implementation is declared faithful.

## Demobilization as a deliberate sacrifice

Immediate local discharge is the zero-spend fallback. The government accepts the cohort's release where it is, gives up its active service and honors 180 days of protected personnel unavailability. It does not purchase a journey, promise remote repatriation or grant a confidence reward. Disaffection falls by 20 once after actual discharge, and ordinary recovery follows. Only equipment actually secured by its entitled owner returns to usable stock. Equipment outside that owner's custody remains in a recorded recovery claim.

The action is available to a valid consenting cohort even at zero political power, command power and equipment. A human confirmation discloses the loss of the last formation when relevant. If a native operation cannot lawfully complete during active combat, the action can register the accepted discharge without charging anything and execute at the first valid disengagement. It cannot report successful removal, stop counting real casualties or grant recovered equipment before that happens. A pending acceptance has one 10-day pause in administrative escalation, with no repeated extensions from clicking again. Combat and actual loss remain possible.

The agreement identifies which formations or personnel are released, where their equipment goes, the earliest lawful return to service, and the front or garrison gap left behind. The confirmation shows the actual projected army reduction. A country can choose a larger release to end an otherwise unaffordable crisis, provided the soldiers and their legal owner accept it.

An orderly discharge returns serviceable recorded equipment to its actual entitled owner. Damaged, lost or stolen equipment is kept in the separate outcome record. Personnel move from deployed service to a protected discharge status. They are unavailable for immediate redeployment for 90 days, extended to 180 when the agreement promises final wartime release. The event does not erase civilian population or register deaths.

A native disband may already refund manpower and equipment. The implementation must account for that actual refund before reserving unavailable personnel or recording recovered equipment. It must never add another manual refund from the desired amount. The outstanding protected-personnel ledger, rather than a countrywide negative manpower payment, prevents immediate re-recruitment from becoming a free loop.

A later return to voluntary service uses only outstanding, surviving, eligible recorded personnel and honors the original terms. It cannot create a second copy of a demobilized formation, restore its full old equipment for free, or return soldiers who have since been transferred to a warlord or another country.

## Suppression by loyal troops

Containment starts with a real force selection. Eligible loyal formations must be owned or expressly authorized, available for the duty, sufficiently supplied, outside every mutiny or conflicting commitment, and capable of reaching the target. An unstaffed template, stockpile, remote ally or nominal army-size number cannot satisfy this requirement.

Define `R` as the effective deployable manpower of the committed loyal force divided by that of the resistant cohort. Current strength and organization contribute to effective manpower, using a verified calculation. Routine containment requires `R >= 1.5`. A ratio of at least 2 gives the government a materially safer option, while reducing coverage on its other fronts.

The player sees the selected force, its downtime, known risks and the estimated outcome range. It can cancel before movement with only incurred costs retained. An irreversible confirmation puts cancellation first for an unattended popup. Any later click rechecks the exact proposal, authority and live units.

The initial balance model uses the following probabilities, expressed as authored design estimates:

`Success = clamp(r5(40 + 20(R - 1) + 10U + 10Q - 15V - 15T), 10, 85)`

`Fracture = min(100 - Success, r5(clamp(40 - Success / 2 + 15V + 10T, 5, 50)))`

`Partial = 100 - Success - Fracture`

Here `U` is one when the loyal force has a verified supply advantage, `Q` when Disaffection is below 60, `V` when Disaffection is at least 80, and `T` when Agreement confidence is below 20. The fracture result cannot consume more than the probability remaining after success. The score is frozen only when the physical confrontation commits. Preparation gives a preview, which updates if conditions change. Part 6 checks representative cases and the nonnegative remainder.

| Result | Immediate consequence | Continuing cost and recovery |
| --- | --- | --- |
| Contained | Resistant command is broken, surviving formations are secured or enter a supervised settlement, Disaffection falls by 25 once | Loyal-force readiness is reduced by 20% of its current organization, the force remains committed for at least 10 days, and confidence falls by 10 |
| Costly partial | Some units comply, others desert or remain organized | Only actual outcomes are booked, the remaining cohort receives a new 20-day choice, and coercive aftermath lasts 90 days |
| Fracture | The confrontation fails and some committed troops can join the refusal | The exact defectors leave loyal authority, existing mutineers remain, and a warned warlord or territorial revolt branch becomes available |

The outcome does not script arbitrary executions to manufacture a difficulty cost. Combat losses are whatever the verified confrontation actually causes. Arrests, service restrictions, desertion and deaths have distinct records. A containment result can restore operational authority without making the soldiers trust the government.

A failed crackdown does not automatically launch a nationwide civil war. It first asks whether the resistant force can hold a coherent local footprint, whether a viable Event 116 warlord can receive it, and whether a negotiated withdrawal remains possible. The country package gate in Part 4 determines whether an armed territorial actor can actually exist.

## Choosing to wait

Inaction is a deliberate posture with a visible next review. It reserves no resources and confers no agreement. A government can wait for an imminent peace, a route repair already in progress or replacement forces that will make a better settlement possible. The UI distinguishes such live facts from mere hope.

After the deadline, unresolved Disaffection of 60 to 79 permits a desertion loss of up to 5% of the cohort's current recorded manpower per 10-day review, with a cumulative ceiling of 15% of its opening strength. At 80 or above, the proposed rate is up to 10%, with a ceiling of 30% before a separately warned organized outcome. The cumulative ceiling counts gross lifetime personnel debits for this cohort, including people later returned through amnesty. A return never reopens the loss budget. These are loss ceilings, not minimum guaranteed removals. Actual loss cannot exceed surviving uncommitted personnel.

Deserters reduce real deployed capacity. A corresponding, explicitly recorded portion of personal equipment can leave with them. Heavy equipment remains with the formation unless an observed seizure or defection transfers it. The initial personal-equipment departure ceiling is 25% of the equipment proportion attributable to the deserters. Any recovered cache is credited once against the missing equipment record.

Desertion is not a death and does not reduce civilian population. Amnesty can return at most 25% of the outstanding surviving deserters in a single 30-day program when confidence is at least 70 and the original grievance is remedied. Further return requires a new actual choice by the remaining soldiers and cannot exceed the outstanding ledger. The program is unavailable for people who already joined a recognized armed recipient.

## Missions and cancellation

| Mission | Duration anchor | Success | Partial or failure | Authority-loss cancellation |
| --- | --- | --- | --- | --- |
| Respond to the refusal | 20, 30 or 45 days as disclosed | A valid commitment or completed immediate settlement | Organic progression follows actual Disaffection | Clears the response obligation without inventing success |
| Deliver the compact | 30 to 60 days, extended before commitment for a verified remote route | Promised rest, supply, representation or discharge actually delivered | Delivered portions count, undelivered obligations remain, confidence responds once | Refunds only unused refundable components and releases remaining commitments |
| Restore reliable service | 90 days | No fresh breach and every cohort has a lawful disposition | A new material breach reopens only the affected obligation | Preserves historical outcomes and hands surviving duties to the lawful successor |
| Reintegration and return | 90 to 180 days | Protected discharge and voluntary return terms honored | Missed transport or unlawful remobilization damages confidence | Outstanding people and equipment remain in the exact succession ledger |

The short opening windows are justified by an immediate military refusal. Institutional recovery uses the longer mission pacing required for substantial work. A mission follows one authoritative deadline. Partial payments, UI refreshes, save loading and duplicate callbacks cannot restart it. A replacement deadline requires a disclosed extension agreed before expiry.

Cancellation distinguishes a vanished target from government bad faith. If the actor loses authority through annexation or a settlement owned by another system, obsolete tasks stop without failure rewards. If the actor voluntarily breaks its own promise, the appropriate confidence and disaffection consequences apply. A refunded stale click never grants a success receipt or a scripted cooldown.

## Lasting outcomes

The country holds one event-owned military relationship spirit at a time. Its forms follow the actual outcome: an active divided command, a delivered service compact, a coerced settlement or unresolved distrust. Later decisions transform or remove that spirit. It does not stack a separate badge for every cohort.

A delivered compact can grant 10% organization recovery to the affected conventional service package for 90 days, justified by rest and reliable supply. It does not permanently improve every unit in the country. A coerced settlement gives immediate availability with a 90-day confidence liability and no compensating free manpower. Complete demobilization produces a smaller army and restored political reliability. A successful revolt creates the real country consequences in Part 4.

Country recovery closes when Disaffection is at most 25, every cohort has a final lawful disposition, and the last promised recovery period is complete. Confidence and durable history remain available for recurrence. Cleanup removes temporary penalties, missions, reservations, AI strategies and stale front agreements without destroying historical proof.
