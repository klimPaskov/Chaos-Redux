# Mistresses: decisions, operational missions, and recovery

## Give the response a place in the country

The response should compete with the war effort through equipment, travel, trained staff, production time, and the government's ability to maintain cooperation.
A country can investigate individual cases, but it also has to protect the people who provide evidence and keep its own investigators independent.
Those choices connect the personal screening loop to named locations, supply routes, sensitive institutions, and the existing army.

The decision layer therefore has two rhythms.
Case actions resolve a small number of individuals over weeks.
Operational missions build or defend the conditions that make those actions effective over several months.
A player who pays attention to the wider country can make screening faster and more reliable without acquiring perfect information.
A player who relies on coercion can achieve a short-term interruption, then must deal with lost cooperation and the consequences of mistakes.

All new action and mission terms below are working design labels, not final localisation.
All costs, gains, thresholds, and intervals are launch tuning proposals.
`119_mistresses_spec_part_3_screening.md` remains authoritative for individual truth, evidence, method limits, and purge consequences.

## A changing category with a small action set

Use one host-response category, provisionally identified as `mistresses_response`, with an ordinary entry decision that opens the event-owned screening window.
The category header repeats Public Confidence and Investigative Reach without adding another public meter.
Native missions show their current named objective, remaining time, and success or failure conditions.
The main category should normally expose three to five primary actions and at most three active missions.
Case selection, archive navigation, and opening the window are navigation controls, not additional resource purchases.

| Country situation | Primary action families presented | Why this set belongs here |
| --- | --- | --- |
| First referrals | Open screening, establish a service circuit, protect an endangered source, review temporary household access | The country builds a usable response while ordinary relationships continue |
| Established response | Open screening, improve the current service circuit, protect sources, isolate one exposed route, resolve the most urgent institutional problem | The response acts on known targets and keeps its evidence trustworthy |
| Corruption or wrongful removal | Open screening, independent audit, restitution, one current protective action | Recovery replaces lower-priority expansion actions until the immediate problem is addressed |
| Visible revolt | Open screening where authority survives, maintain a civilian corridor, protect command access, fulfil one coalition or reconquest objective | The response is tied to territorial survival and actual people |
| Mother campaign or aftermath | Present the current finite strategic objective and the relevant rescue, liaison, or restitution action | The operational layer supports the larger campaign defined in the owning chapters |

The interface does not hide a fifth policy page full of equivalent buttons.
The institutional problem slot chooses between audit, restitution, and liaison according to the current route and highest-priority unresolved condition.
The player can inspect the available alternatives before committing, but the display presents one selected target and its relevant action family.
Changing target is free navigation and cannot refresh costs, evidence, or deadlines by creating a new transaction.

Mission admission is capped at three concurrent operational contracts per host.
One slot is reserved for an actual endangered civilian or command-continuity emergency when one exists.
Ordinary work does not occupy that reserved slot permanently.
Queued missions have no running deadline until admitted, except an independently existing world incident whose actual deadline must remain visible.
Closing the category cannot pause a mission.

## Dynamic cost quotation

National size affects the cost of serving an area, not the price of deciding the fate of one person.
An individual case normally uses the same small team cost in a large or small country, with a travel adjustment for the actual location.
A service circuit spanning millions of people and several widely separated sites costs more than one compact local circuit.
The player can choose a smaller valid geographic assignment when national resources cannot support the whole affected area.

For launch tuning, define a hidden service-footprint multiplier as the square root of the ratio between the selected registered population and five million, bounded between one-half and three.
The multiplier is calculated for the named assignment's affected, controlled states, using the authoritative population record.
It is a quotation input and never becomes a public event statistic.
An assignment covering five million people has multiplier one.
A footprint of 1.25 million has multiplier one-half, and 45 million reaches the upper bound of three.

Apply a 25 percent travel surcharge to fuel for a dispersed assignment and a 25 percent supply surcharge to equipment when an active war makes access costly.
The presence of both factors changes the appropriate resources independently.
Good existing rail access can remove the travel surcharge.
A completed mission that establishes a functioning service connection can reduce the relevant quantity by 25 percent while that connection remains usable.
The additive focus routes can instead earn their documented 15 percent operation cost or time improvement.
Apply the single strongest eligible reduction to each affected quantity, without stacking the two reductions or extending the benefit to an unrelated route.
Equipment has a minimum charge of five and fuel a minimum of 500 whenever that resource is genuinely consumed.
Fixed Confidence sacrifices and the final containment mission's 50 Command Power payment are not discountable.

Round equipment quotes upward to multiples of five and fuel quotes upward to multiples of 500.
Round an eligible discounted operation duration upward to five whole days, with a floor of 90 days for ordinary native missions.
The explicitly justified 30-day final containment and shorter individual case actions retain their own timing rules.
Show the exact amount that will be charged.
Command Power stays conservative and is never above 60 for any action.
The selected assignment, route, duration, and all resources belong to one coherent quote.
If the live quote changes before the player commits, update the display and require a fresh deliberate selection instead of charging a different price from the one confirmed.

### Cost palette and action budget

The table describes the normal supplied path.
Multiplier F means the selected service-footprint multiplier.
Resource names are written here for design clarity.
The actual interface uses each resource's correct texticon, with at most three inline resource entries and every committed resource explained in the full cost view.

| Action family, working label | Normal consumed or committed resources | Number of resource types | Retained requirements |
| --- | --- | ---: | --- |
| Supplied case verification | 5 support equipment and 500 fuel, with travel adjustment | 2 | An unused method, one staff slot, accessible person and source |
| Protected contact trace | 5 Command Power, 5 support equipment, 1,000 fuel | 3 | A recorded contact, one staff slot, named observation area |
| Individual purge | 5 Command Power, 5 support equipment, 5 Public Confidence, and one coercive-handling slot committed for five days | 4 including the temporary handling commitment | Same person and authority at confirmation, no prior removal receipt |
| Service circuit | 25 × F support equipment, 5 Army XP, 2,500 × F fuel | 3 | Reachable named service sites and an available mission slot |
| Witness protection operation | 25 × F support equipment, 1,000 × F fuel | 2 | A real endangered source and a named route or protected site |
| Independent institutional audit | 10 Army XP and one civilian factory committed for the audit interval | 2 | A bounded set of source groups and an institution outside their collection chain |
| Isolation of an exposed route | 25 × F support equipment, 5 Command Power, 2,500 × F fuel | 3 | A discovered existing edge, authority at the named choke point, continuing access |
| Restitution programme | 25 Political Power and one civilian factory committed for the programme interval | 2 | A documented wrongful action and a valid surviving household or community |
| Foreign source exchange by sea | 25 × F support equipment, 10 convoys, 2,500 fuel | 3 | A consenting eligible partner, functioning ports, and an accessible sea route |
| Temporary coercive patrol | 15 Command Power, 100 × F infantry equipment, 5,000 × F fuel, 5 Public Confidence | 4 | A named accessible district and actual locally assigned security units |
| Temporary household access agreement | 25 Political Power | 1 | A specific public institution and the compatible policy route |

The universal Confidence loss from purge and coercive patrol counts toward the cost budget because it is a guaranteed sacrifice at selection.
It cannot be hidden in an outcome tooltip as a fifth cost.
Its actual amount is bounded by the current nonnegative Confidence reserve and previewed with the other sacrifices.
An empty Confidence meter does not itself prohibit a valid purge or patrol, and does not suppress their unrest, cooperation, or later accountability consequences.
Later evidence-dependent unrest is a consequence, not an additional entry fee.
No action adds an undisclosed manpower debit, stability debit, fuel fee, or equipment subtype behind the published quote.

An existing trained formation required at a location is a retained condition when it remains under normal player control.
Moving it away can interrupt mission progress.
If a later implementation actually locks that formation or reserves manpower as payment, the commitment becomes a consumed resource type and must be counted and displayed.
The same distinction applies to a civilian factory that is unavailable for normal construction while the project uses it.

## Every host has a viable response

Small countries must make difficult decisions without being locked out by a resource type they cannot obtain.
The slower local history visit in the screening chapter has no equipment payment and uses a staff slot for 30 to 45 days.
It still reads an ordinary saved evidence packet with the same dependence and corruption risks.
It is useful for a poor country and costly in time for an overstretched major power.

For a service circuit without fuel or a motorised supply chain, offer a local civilian circuit using 25 × F support equipment and 10 Army XP over 150 to 180 days.
If even that equipment is unavailable, the country can organise a walking circuit with no stockpile payment, a 180-day deadline, one occupied investigation slot, and named local visits.
Its completion raises Reach by 10 instead of 15.
This path consumes time and response capacity, has genuine geographic objectives, and cannot be repeated on the same already functioning circuit for more rewards.

A country without an available civilian factory can conduct an outside-observer audit over 180 to 210 days.
It pays 25 × F support equipment and requires a real consenting partner with an independent collection chain.
A country without either production capacity or a partner can use a local separation audit over 210 days, occupying one investigation slot and temporarily closing the selected source group to new evidence collection.
This retains the basic integrity remedy without creating an imaginary foreign institution.

Foreign exchange uses an overland variant where a functioning land corridor exists.
That variant pays 50 × F support equipment and 5,000 fuel, consumes no convoys, and depends on the actual corridor remaining usable.
A landlocked country cannot pay a sea-route price for a journey that never occurs.
The geographic choice is a mutually exclusive route for the same contract, not two ways to collect the same reward.

## Service and protection missions

### Service circuit

The country selects up to five named affected service sites from its registered participant states.
The sites must include an actual unresolved access or collection problem.
The objective requires completing a staffed visit at each selected site and maintaining the connecting service arrangement for 30 elapsed days after the final visit.
An assignment that was already fully served at activation is not eligible as a new success.

The supplied mission normally lasts 120 days, extending to 150 or 180 for dispersed terrain, interrupted access, or the slower path.
The interface names the current sites and marks visited locations without adding a national progress meter.
These are finite objective checkmarks.
Staffed visits use the assignment's prepaid service commitment and do not require a second fee at each site.

Full success raises Investigative Reach by 15 and unlocks the relevant permanent local service connection.
A walking circuit raises it by 10.
This family can build Reach to 75.
Further progress comes from the focus route and coalition or scientific institutions specified in `119_mistresses_spec_part_7_focus_routes_ai.md`.
Partial success retains visited-site service but grants only 5 Reach when the minimum useful connection was actually established.
Failure preserves honest records of completed visits, grants no Reach, and can reduce Confidence by 5 if a public commitment to an endangered community was broken.

The same healthy circuit cannot be rebuilt repeatedly.
A damaged service can be restored, but restoration recovers only the capacity actually lost.
Newly affected areas can justify a new assignment with its own finite site receipts.
This makes a large country's breadth of work meaningful without allowing a tiny safe district to generate limitless national capacity.

### Witness protection operation

Select an existing endangered source and its actual location.
The mission lasts 90 to 150 days depending on distance, access, and urgency.
It requires an accessible protected site plus a maintained corridor or a supplied formation in the named district for 30 elapsed days.
A country using the civilian alternative establishes successive local safe visits instead of fielding a military formation.
That alternative takes 150 days and occupies an investigation slot while it operates.

The objective is to preserve access to a person who can provide evidence.
Success keeps the source available, raises Confidence by 10 once, and permits an independently sourced investigation if the relevant material exists.
It never guarantees adverse testimony or invents a new guilty candidate.
Partial success can preserve the source but lose the travel route, which retains the witness and delays later collection.
Failure can make that real source inaccessible if the existing network or war situation can actually reach it.
There is no automatic death or free enemy recruitment merely because a mission timed out.

Protection records its actual service interval.
An operation that begins and ends between two network updates still receives its promised protection for the elapsed period.
Overlapping operations cannot claim the same protected days twice.
The interval handling belongs to `119_mistresses_spec_part_10_integration_transactions.md`.

## Integrity and network operations

### Independent institutional audit

An audit selects up to five existing source groups in one institution or a connected collection chain.
The country commits an independent team and completes two separate comparisons, one of source provenance and one of the original collection material.
Both must occur after activation.
Merely having high Reach, a factory, or Army XP does not complete the objective.

The usual deadline is 150 days, extending to 180 or 210 for the supported low-capacity variants.
Success publishes the saved integrity findings, identifies shared provenance where the evidence supports it, and enables one replacement investigation for a packet implicated by the recorded finding.
An erroneous concern about a clean source permits that same workflow when the required independent collection path exists.
Neither the button nor AI eligibility checks the unobserved true integrity bit.
It also protects newly established source groups within the audited institution for 180 days, using the 5 percent launch corruption chance from the screening chapter.
This protection applies to the actual institution and cannot transfer to every source in the country.

Partial success can identify the shared chain while leaving the material comparison inconclusive.
The reports are then visibly dependent, but no person is declared innocent or alien.
Failure leaves the source record unresolved and returns the committed factory at closure.
The team cannot start the same audit repeatedly to draw another result.
New corruption must come from a genuinely new source generation or observed change.

### Isolation of an exposed route

This mission acts on an existing network edge that screening or another concrete incident exposed.
The player selects its named transit or institutional choke point and sustains the required local presence for 45 elapsed days within a 150 to 240-day mission.
The longer interval applies to contested or remote locations.
A civilian service route can replace a military cordon when the target is an institution and the route allows independent supervision.

Successful isolation makes that exact edge unusable for 180 days.
Any network operation requiring it must find another existing valid path or fail through the normal network rules.
The mission does not kill either endpoint, alter their truth, or award the individual-removal score again.
Completion can raise Reach by 5 once because the country has established a usable connection between its own services.
Any larger cell-disruption objective checks the actual surviving network under the core chapter's rules.

Partial success interrupts the edge only during the actual maintained interval.
Failure ends the attempted isolation and lets the surviving network use its own resources to act again.
An edge that ceases to exist through a genuine removal resolves the mission as superseded, with no duplicate disruption reward.
A different mission cannot extend the same 180-day interval by overlapping its last day.
Renewal requires a new paid contract after the previous isolation expires and a still existing edge.

When accurate removals and maintained isolation leave a verified cell fully disconnected, the completed local assignment can publish one macro-containment receipt for its identified surviving cohort.
This requires zero usable institutional access, no surviving usable external link, and the actual local supervision needed to prevent the cohort from operating, under `119_mistresses_spec_part_2_networks_population.md`.
The receipt removes that finite cohort's contribution to territorial seizure and assistance to other cells while the isolation holds.
It does not kill, absorb, or individually identify every resident alien, and it removes no human population.
An actual escape, rebuilt connection, or loss of supervision can reopen the operational danger through a new recorded world outcome.
The UI describes the observed containment objective and its continuing obligations without exposing an unobserved person's truth through action availability.

### Temporary coercive patrol

The coercive route can establish a 45-day patrol after its quoted resources and Confidence sacrifice are paid.
This is a temporary policy action rather than a 45-day timed objective.
It slows exposed route activity in the selected district and protects actual sensitive access while security units remain present.
It creates no automatic guilty verdict and cannot purge a set of portraits in one click.

The policy also reduces voluntary witness cooperation during its actual service interval.
The player may obtain a short breathing space while making subsequent independent evidence harder to gather.
Repeated patrols require a 90-day cooldown and cannot stack their protection.
The route's institutional and recruitment consequences remain with the host focus and network chapters.
Any observed wrongful intervention feeds restitution and confidence recovery through the same individual history.

## Restitution and reversible accommodation

### Restitution programme

Restitution begins from a documented wrongful action or a proven contaminated investigation.
It identifies the actual surviving household or affected community and the responsible case records.
The mission lasts 120 to 180 days and requires a completed review, a funded public service or compensation delivery, and withdrawal of the specific improper restrictions.
Its factory or slower service commitment represents work performed, not a fictional reversal of death.
A host without a free civilian factory can use a 180 to 210-day local redress contract that consumes 25 Political Power and occupies one investigation slot while delivering the same documented repair.
This slower alternative requires no additional stockpile and releases its staff capacity at closure.

Full success restores 15 Confidence and removes the eligible residual unrest condition after its minimum consequence interval.
It cannot erase the death record, restore an executed person, remove a valid achievement disqualifier, or refund the purge's operational resources.
Partial success restores 5 Confidence when a real delivery occurred but the institutional correction remains incomplete.
Failure leaves the unmet obligations and associated case history visible.
The same wrong cannot finance repeated confidence rewards, and the reward is bounded by the Confidence actually lost from the qualifying wrongs.

The player can initiate restitution without waiting for national collapse.
The AI should prefer it when continuing loss of cooperation would make its current response ineffective.
The mission offers a way back from mistakes while preserving their cost.

### Temporary household access agreement

The accommodation route can grant a specific household or social introduction network access to a defined public institution for 90 days.
Its public rationale concerns ordinary family support and social continuity.
The resulting recruitment, stability, and access changes use the existing ordinary-crisis rules in `119_mistresses_spec_part_2_networks_population.md`.
The decision neither declares the people alien nor promises that the agreement is safe.

The player can revoke the permission before expiry through a consequence preview that ends its remaining benefit and access.
Revocation returns no already consumed Political Power and does not reroll any case.
A 120-day access-review mission becomes available if concrete incidents challenge the arrangement.
It consumes 10 Army XP and 10 support equipment, with one named institution and an independent reviewing team as retained requirements.
The team compares the original access record against an independently obtained visit or delivery record after activation, then maintains the revised access separation for 30 elapsed days.
Full success ends that specific sensitive-access permission while preserving an otherwise valid household-support benefit.
It can raise Reach by five once for the institution when it establishes a new usable service relationship.
Partial success preserves the independently established record but grants no access removal or Reach reward.
Failure leaves the documented access and its consequences in place and does not fabricate guilt.
A host lacking either resource can use a 180-day review that occupies one investigation slot and temporarily suspends the chosen institutional permission while it collects the same two records.
The slower path can restore a justified permission or confirm the separation without a stockpile payment.
No healthy, already reviewed permission generates a second reward, and a new review requires genuinely new conduct or a different permission generation.
This provides tactical accommodation and a recovery path without granting permanent immunity from investigation.

## Foreign exchange, revolt, and the survival war

Foreign source exchange begins with a specific partner and a specific independent question.
The partner must exist, have continuing authority, consent to the service, and be able to reach the agreed route.
Its 180 to 270-day mission requires delivery of original material and a genuinely independent collection or assessment.
Copying a domestic report through another country's office does not satisfy it.

Success makes the new evidence available to the agreed participants and can add 10 Reach to a host that lacks the relevant connection.
That gain is one-time for a functioning partner connection.
Repeated exchanges provide their actual evidence or operational service, not another flat Reach reward.
Partial delivery preserves the material that arrived without publishing a completed independent finding.
Failure spends no second fee and does not create automatic hostility or a dead partner.

After The Unveiling, the same operational system supports the human survival routes in `119_mistresses_spec_part_6_countries_forces.md` and `119_mistresses_spec_part_7_focus_routes_ai.md`.
Evacuation objectives select real surviving people and named open routes from the population ledger.
Their ordinary deadlines are 90 to 150 days, with a shorter emergency interval only when an already visible front creates a genuine immediate deadline.
The shared population receipt determines how many people actually reach safety.
No reward can use a planned evacuation amount when the measured transfer was smaller.

The normal land-corridor contract consumes 25 × F support equipment, 2,500 × F fuel, and five Command Power.
Select at most five actual origin states, a reachable receiving state with consenting authority, and a finite civilian cohort that has not already been assigned elsewhere.
Part 2 fixes the launch throughput and reception-capacity rules, while this mission owns the prepaid service and the observed transfers. A supplied land route moves at most 500 × F people per service day, the ten-convoy sea route at most 250 × F, and the walking alternative at most 50. The actual eligible cohort and remaining reception capacity can lower every transfer.
After activation, establish the route and maintain access for 30 elapsed days while measured arrivals move people from their origins to the destination.
Full success delivers the entire saved assignment and raises Confidence by ten once for that assignment.
Partial success preserves the actual delivered population and grants five Confidence if at least half arrived.
Failure leaves people at their real surviving locations or in the recorded interrupted transit state, with no automatic mass death and no second copy of a refugee cohort.
Actual combat or absorption losses use the population owner's separate measured outcome.
The route closes when its assignment ends, and a follow-up selects remaining unassigned people rather than reusing the same completed arrival receipt.

A sea corridor substitutes ten committed convoys for the five Command Power cost, keeping support equipment and fuel as its other two resource types.
The convoys are unavailable for ordinary use during the operation and return at closure unless the inspected transport system reports an actual loss.
A stockpile-poor host can organise a 150-day local walking corridor with no equipment payment and one occupied investigation slot, only between accessible neighbouring controlled states.
Its capacity is lower and its achievable assignment must be quoted from the real route before activation.
Neither alternative grants distant passage without a functioning corridor or doubles the existing refugee transfer.

Reconquest assignments name an actual occupied target, the required continuing control, and the local service restored after capture.
Their ordinary deadlines are 180 to 270 days, and success is based on post-activation control and restoration work.
The normal restoration contract consumes 50 × F support equipment, 2,500 × F fuel, and ten Army XP.
The army's actual military operation remains under ordinary war and supply rules, with no payment that conjures a formation or transfers the target for free.
After genuine recapture, hold the selected state for 30 consecutive days and re-establish one named civilian service and its connection to a controlled receiving institution.
Full success restores that service and can raise Reach by ten once for a newly recovered service region.
Partial success retains the time actually protected and the delivered restoration work, but pays no national Reach reward while control or the service remains incomplete.
Failure records the real territorial outcome, releases temporary commitments, and leaves the military campaign running.
Already restored regions cannot be repeatedly abandoned and retaken for the reward.
A poor reconquering host may use a 270-day civilian restoration contract with one investigation slot occupied and no stockpile payment, requiring the same genuine recapture, 30-day hold, and completed local service.
Its completion raises Reach by five instead of ten and cannot restore an institution that the country never regained authority to operate.
The exact Mother objectives and regional contest remain authoritative in `119_mistresses_spec_part_8_mother_aftermath.md`.
These adapters use that chapter's finite objectives and do not introduce another public command, readiness, or coalition meter.

### Nonterritorial local-insurrection response

Part 5 owns the finite revealed pockets that cannot form a viable territorial country. One host mission covers the saved pockets that the host can actually reach. A 45-day emergency response consumes 30 Command Power and 50, 100 or 150 support equipment under the small, medium and large operating-capacity bands defined below. It retains a real local security assignment or protected civil authority for the final 30 consecutive days. No target, force or authority is conjured by paying.

The poor-country alternative lasts 90 days. It has no stockpile charge, consumes the smaller of five war-support points and the current available war support, and applies a 10% local production burden in the affected states for 90 days. It uses the same real authority and final 30-day protected-presence requirement. The remaining burden still applies at zero war support. These are alternatives for the same assignment and cannot both be paid for one pocket.

Success isolates the actual surviving alien cohort, removes its usable institutional access and external links, and closes its revolt contribution without killing the recorded people. Until genuine resolution, each affected state retains Part 5's 10% local production burden and the host retains one five-point stability penalty regardless of the number of pockets. Failure or cancellation after commitment loses ten Confidence once, clamped at zero, and applies one additional 90-day 10% local production penalty. Replace an existing civil-protection burden instead of stacking both temporary penalties. Neither outcome grants containment or cancels the baseline burden, including at zero Confidence and war support.

Retreat is a separate once-per-pocket opportunity after at least 45 real unresolved days or an actual military breakthrough. It can move at most 25% of the originally revealed surviving adults, rounded down and bounded by current survivors, to an existing brood along a real usable controlled route. Its measured origin debit and destination credit cannot be repeated through cancellation. Remaining active pockets retain their disruption, with no passive growth, extra human deaths or fresh territorial roll. A retry requires 30 days after closure. Actual completed screening or macro-containment can settle the same cohort earlier, and its receipt closes the mission without a second reward.

Access is a preflight condition. If occupation makes a pocket inaccessible, retain it for liberation instead of offering a paid impossible response. This shorter emergency mission is justified by an already revealed local crisis. It does not change the ordinary long-duration investigation and recovery missions.

### Mother relay disruption

At Mother emergence, save the actual set of up to five eligible relays outside the lair.
The required disabled count is the ceiling of 60 percent of that actual set.
A verified target appears as a named map objective, while an unidentified site initially appears only through its supported regional evidence.
The human player can disable a relay by holding its state for 30 consecutive days, or use the paid operation when a real access route exists.
Military disablement lasts while human control continues, subject to the alien repair rules in the Mother chapter.

The paid operation lasts 90 days and uses three resources.
Its launch price is 10 Army XP, support equipment of 25, 50, or 75, and fuel of 2,500, 5,000, or 7,500.
The three capacity bands use the acting country's operating controlled civilian factories, military factories, and dockyards, with small at ten or fewer, medium above ten through 30, and large above 30.
Freeze the selected band with the quote.
Allied delivery can support a small responder without changing the actual donor or inventing stockpiles.
The no-DLC operation remains authoritative, with any native raid route invoking the same single outcome receipt rather than creating a second opportunity.

Require an identified relay, a real supplied staging location, and continuing access through friendly adjacent territory, a valid coalition corridor, or an independently established event-owned approach.
The operation must complete two distinct preparations, delivery of its reserved material and establishment of an independent observation source, then sustain its usable approach for 30 elapsed days.
These are finite tasks on the selected operation.
No current stockpile threshold auto-completes them at activation.

The launch full-success chance is 65 percent, increased by 15 points for verified independent preparation supported by Reach at least 50, and by ten points for 45 days of uninterrupted supplied access.
An actual defender counter-operation reduces it by 20 points.
Clamp the resulting full-success chance between 25 and 85 percent.
Assign the next 15 percent of outcomes to partial success, with the remainder as failure.
Show the observable preparation and access contributions to risk, without revealing an unobserved defender operation through an exact live probability.
Draw and save the operation's random rank once at commitment, then resolve it against the final threshold derived from actual service and defender response.
Changing a panel cannot redraw it.

Full success disables that relay for 60 days.
Partial success retains one genuine preparation result for a later attempt but does not disable the relay or fabricate a new source.
Failure delivers no disablement.
Loss of the actual approach at resolution cancels the operation through its authority and access terms, without a consolation roll.
Only one coalition operation may target a relay at a time, with a 180-day interval between starts on the same relay.
Repeated attempts remain possible at their full real cost and elapsed time.

### Alien relay repair

One living brood controlling a militarily disabled relay may commit a 60-day repair when the real site is supplied. Consume 25 Command Power, 250 Line equipment and 50 support equipment once. Retain actual alien control and supply for the full interval. A loss fails the paid attempt, leaves the relay disabled and preserves already spent resources. A new attempt requires renewed eligibility and a 30-day interval after the failure. Only one repair can own a relay. Merger rebinds its owner without resetting time or payment.

The 60-day disablement earned by a successful human disruption operation cannot be shortened by repair or an emergency override. If military damage and timed disruption both apply, both must have ended before the relay returns. Human control prevents repair completion. The Mother's defeat closes all repair operations. These are three-resource actions using an existing site, with no new relay or guardian granted as a completion reward.

### Adult-captive assimilation during Mother command

Part 8 defines this finite alien war policy. Its 90-day commitment targets at most 250 already registered, physically held human adult civilian partners or adult case subjects. It cannot target unknown residents, minors, service cohorts or previously lost people. Consume 50 Command Power, 100 Political Power and 250 Line equipment, and reserve 50 real uncommitted alien adults as noncombat staff. This is four commitments. The target people are a saved population cohort whose actual outcome is measured, not a fifth purchase currency.

One brood can have one active commitment and must leave at least 180 days between starts. Its owned-and-controlled supplied site must remain valid throughout. Rescue, recapture, supply loss or the Mother's defeat interrupts unfinished absorption. Rescue is allowed to preempt the population reservation through the shared cohort owner, which closes this mission before any subsequent debit. Actual surviving people and staff remain at their real locations. Already spent inputs are not duplicated by refund.

Completion consumes only the measured eligible adult human loss through the shared nonhuman-occupation adapter and records those deaths once. Pending new alien adults equal the floor of half that measured result, capped by the maximum 250-person target. Their release shares Part 6's monthly adult ceiling. Paid donor missions survive a merger with their original sites and elapsed time, but no new start is admitted while any remains, and the latest inherited start date controls the cooldown. The Mother cannot create an unlimited combat-kill or occupation conversion economy.

### Final containment of the Mother

One coalition-owned final mission becomes available when the required relay count is currently disabled, a human force controls the lair with a valid supplied or supported expeditionary route, and the actual guardian condition has been resolved.
At commitment, enough relays must be under continuing human-held disablement or have at least 30 days left on their saved timed disablement. Reject a known impossible attempt without payment. At a shared completion and timed-expiry instant, credit the fully maintained 30-day interval before expiring that timed disablement. An actual control loss or other disqualification committed before completion still fails the mission.
It lasts 30 days because the final containment is a live military emergency.
It consumes 50 Command Power and 50, 100, or 150 support equipment using the same responder capacity bands.
This is a two-resource action with one shared coalition payment receipt.
Any allied contribution reserves and transfers real resources into that receipt, with no duplicate mission or outcome.

During the 30 days, the required relay disablement and lair control must remain valid.
Loss of either fails the current attempt, releases any temporary reservation, and preserves the actual spent resources.
A rejected preflight or cancellation before commitment spends nothing.
The moment of successful commitment is also the irreversible deployment boundary, so a later voluntary cancellation cannot recover supplies that are already in use.
Success invokes the unique Mother-defeat result from the owning chapter.
Total military destruction remains a separate valid route to that same one-time defeat result.

## One payment and one outcome

Every paid action has a pure quote and eligibility check shared by the visible price, enabled state, AI, and final action.
All simultaneous requirements are checked together.
At commitment, validate the exact actor, person or location, target generation, current authority, unused method or mission slot, and complete resource quote.
Only then publish the active payment receipt and debit every consumed resource once.
After payment, completion reads that paid receipt instead of attempting to buy the action again.

An unavailable choice never drains a partial fee.
A duplicate click cannot create a second investigation, take another factory, or extend a protection interval.
An expired confirmation cannot charge the newly selected case.
An equipment token must identify the same eligible stockpile in preview, affordability, and debit.
Current engine resources may change while the game is paused, so the interface must refresh its quote and availability immediately after the responsible mutation.

Upfront consumables represent work committed at launch and normally remain spent when the player voluntarily abandons a valid mission.
Factories and other explicitly temporary reservations return at closure.
A rejected commitment returns every accidentally debited resource and grants no reward or success receipt.
Exceptional cancellation caused by loss of authority releases reservations, preserves completed service history, and follows the recorded contract's refundable portion.
It must never run both normal failure and exceptional cancellation.

A mission's successful result, partial result, timeout, cancellation, and supersession share one final resolution guard.
The timer displayed to the player matches the operative deadline, including a legitimate extension.
Partial payments, when a later implementation truly needs them, cannot remove and reactivate the mission to obtain more time.
The detailed receipt and native-timer requirements are consolidated in `119_mistresses_spec_part_10_integration_transactions.md`.

## AI priorities and resource envelopes

The AI first preserves a viable response, then protects time-sensitive people, resolves dangerous evidence, and invests in capacity where its workload justifies it.
It does not spend resources simply because a category is available.
It uses the same target requirements and route alternatives as the player.
Its production planning may identify a useful future service before the equipment exists, while actual execution still requires the complete quote.

The following ordinary and emergency envelopes govern human response work. At the start of each 30-day budget window, assign ordinary event work at most 10 percent of the country's currently uncommitted support equipment and fuel after the normal military reserve.
Allow up to 25 percent during a visible local survival emergency when the existing front and protected population justify it.
Use a 20 Command Power ordinary monthly envelope and a 40 Command Power emergency envelope.
These are action-budget ceilings, separate from the 60 maximum on any single decision.
The receipt saves the budget window so opening the GUI, changing a target, or triggering a new minor incident cannot reset it.
An expensive institution or relay project can accumulate an internal allocation from up to three consecutive budget windows before commitment.
That allocation earmarks existing resources rather than charging them early, and every purchase still rechecks the live stockpile.
The unique final Mother mission has an explicit strategic reserve of 50 Command Power outside the ordinary 40-point emergency envelope.
The AI must accumulate that real reserve and the exact support-equipment quote, rather than remain permanently unable to take the final action or receive a waived payment.

Alien wartime operations use their own finite military budget. Reserve the real 25 Command Power and equipment for a threatened relay repair before discretionary expansion. Assimilation requires a separate actual 50 Command Power strategic reserve, its full Political Power and equipment quote, 50 uncommitted adult staff and the 180-day start interval. It receives lower priority than preserving a viable army, supply and an endangered relay. Neither the human 20/40-point envelope nor an AI-only free grant applies to these alien actions. The reserve is an earmark of existing resources that is rechecked at commitment, not a second pool of Command Power.

Keep at least 25 percent of uncommitted event capacity available for a newly endangered source while a credible crisis is active.
If resources are exhausted, use a slower legal alternative, finish current work, or spare a weak case.
Do not waive the cost for AI, reveal truth to make it more efficient, or send it through an unavailable target.
An AI coalition member evaluates source exchange against the partner's survival and actual route, rather than treating every friendly country as a valid delivery destination.

| Representative situation | Required priority ordering | Action to avoid |
| --- | --- | --- |
| Small poor host with first weak referrals | Slow local investigation before an unaffordable national programme | Spending its last military equipment on a broad patrol |
| Strong host with dependent adverse reports | Independent audit or genuinely independent method before purge | Counting copies as corroboration |
| Host with endangered witness and open route | Protect the source before expanding the service circuit | Letting a routine programme consume the emergency slot |
| Host suffering proven wrongful removals | Restitution and clean collection before another weak coercive action | Repeating purges to conceal the first mistake |
| Host at war with an exposed sensitive route | Affordable finite isolation and command continuity before distant liaison | Using an impossible overseas route |
| Successor after state loss | Revalidate current sites and continue surviving paid services | Charging the inherited mission again |

These orderings require a bounded probability audit of the implemented scores and actual candidate pools.
Decision willingness scores are not click probabilities.
The audit must examine resource starvation, rare-case starvation, route invalidity, and the effect of the 30-day budget boundary.
`119_mistresses_spec_part_12_chaos_balance.md` owns the combined scenario matrix.

## Meaningful results and player information

Every operational mission needs a visible result connected to what the country did.
A protected witness remains available.
A restored service opens a usable investigation route.
A severed edge prevents a real network operation.
A restitution programme ends an improper restriction and restores cooperation while leaving the death record intact.
The player should not receive only a small generic modifier after months of work.

Descriptions use the perspective of the responsible institution and the affected people.
Costs, dates, current destinations, missing requirements, and visible consequences belong near the action.
The writer should use sober language for coercion and suffering, and reserve irony for the actor's hypocrisy or self-justification.
Cultural references require separate research.
The final text must not reveal hidden alien truth, advertise achievement routes, or announce future evolutions.

## Source notes

The action and mission design applies `.claude/skills/chaos-redux-decisions-missions/SKILL.md`, especially Core design rule, Cost and sacrifice design, Mission quality, Mission duration, Progressive decision categories, AI behavior, and Category cleanup and lifecycle.
The atomic cost and timed-payment contracts follow its complete `references/cost-payment-and-localisation.md` and `references/validation-addenda-and-handoffs.md`.
The exact two-value budget follows [Part 1](119_mistresses_spec_part_1_core.md) and the mechanic-wide budget in `.claude/skills/chaos-redux-event-planning/references/advanced-focus-tree-design.md`.
The explicit interval accounting and authority-loss requirements are grounded in `.claude/skills/chaos-redux-events/references/scripted-systems-and-country-integration.md`, Country activation and ROOT.
The UI's automatic paused updates and content budget follow `.claude/skills/chaos-redux-scripted-gui/SKILL.md`.
