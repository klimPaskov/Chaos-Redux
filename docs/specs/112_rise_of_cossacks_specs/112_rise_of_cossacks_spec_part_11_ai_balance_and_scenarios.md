# Part 11. AI, balance targets, scenario design, and acceptance

## Balance intention

The initial rising should create a serious local problem and an interesting small-country campaign.
It should not guarantee the collapse of the country that loses a state.
The host's later power must come from survival, production, training, diplomacy, and actual territorial or federal integration.
The optional national projects can become large because the player has built a large state.

The opening formula in part 03 is authoritative.
The same immutable facts produce the same army and resources for a human or AI host.
The shared player-crisis rule affects the likelihood and timing of supported adverse opportunities.
It does not secretly increase a player host's costs or replenish an AI host's army.

All targets below are proposed design targets for future implementation evaluation.
They are not measured gameplay results.
The planning arithmetic confirms only the stated formulas and bounds.

## AI priorities

The AI first resolves owned reconciliation and already paid work.
It then protects its capital, supplies, a functioning force, and replacement capacity.
It funds A01 Provisional Civil Settlement before discretionary spending and repairs dangerous Cohesion or Legitimacy through feasible specific actions.
A01 may spend below the ordinary 20 Political Power reserve because it is the finite opening administration bridge.
Its current quote must still be affordable, and the AI waits for ordinary accrual if a modifier raises the 35 Political Power base above its present funds.
It obtains a working arms source and a charter.
Only then does it consider optional raids, additional host obligations, and larger projects.

These priorities do not require a new daily all-country controller.
They run through existing host reviews, relevant decisions, and native AI planning.
The controller works on its bounded registered actors and currently due commitments.
Elapsed time, actual resources, and the country's accepted obligations determine behavior.

An AI must be able to decline a larger ambition.
A one-state host with an affordable defense system and civilian settlement is a successful strategic actor.
Its refusal to invade Moscow is not a failure of the content.
A stronger host with a credible national base can choose that campaign.

## Action scoring

Every action is filtered for validity before scoring.
An impossible action has no chance to win through a large desirability score.
The AI uses the same current quote, target recheck, reserve floors, mission capacity, and receipts as the player.

A proposed scoring structure combines urgency, strategic value, feasibility, obligation, and opportunity cost.
Those are internal decision inputs, not additional public country meters.
The exact native AI fields and their mathematical interpretation must be inspected before writing the implementation.

| Situation | Intended priority change | Guard against bad behavior |
| --- | --- | --- |
| Capital or only supply route threatened | Defense, repair, and immediate negotiation dominate | No optional expedition or new distant commitment |
| Cohesion below 40 | Resolve an actual service or command problem | Do not spend nonexistent funds or repeatedly buy a generic unity reward |
| Legitimacy below 35 | Civilian guarantees, local representation, and breach repair dominate | Do not assume another conquest will solve the political problem |
| No military production and no delivery | First workshop bridge, repair, or viable arms contract dominates | A destroyed route or empty donor is not an arms source |
| An accepted installment is due | Honor, renegotiate, or explicitly default before discretionary spending | Do not hide default behind an unrelated focus |
| The army is materially unready | Train, reinforce, or contract commitments | Defense and recovery remain available |
| A raid has low expected value | Prefer normal production or restraint | A prestige reward cannot justify attacking an empty depot |
| A new host asks for support | Compare home defense and actual delivery capacity with the commitment | Refusal or limited volunteers are valid outcomes |
| A great project has no practical geography | Maintain the regional campaign or suspend preparation | Historical claims alone have no feasibility value |
| A member lawfully refuses an unrelated war | Respect the compact or negotiate an amendment | Do not treat valid refusal as automatic treason |
| A patron cannot deliver | Seek an alternative, renegotiate, or withdraw | Do not continue paying forever for a nonexistent supply |
| A migration corridor fails | Protect or redirect the actual cohort | No duplicate destination credit or replacement population |

Ordinary discretionary purchases retain at least 20 Political Power and 10 Command Power after payment, plus the defined manpower and equipment floors.
A direct collapse-prevention action may consume those reserves through an explicit emergency exception.
That exception is visible in the action contract and available to the human under the same conditions.
It is not a hidden AI subsidy.

## Political route preferences

| Host condition | Plausible preference | Conditions that can reverse it |
| --- | --- | --- |
| Secure Don or Kuban base with towns and time to govern | Civilian or federal settlement | Severe invasion, officer opposition, or an unacceptable federation offer |
| Immediate military danger with a coherent officer core | Professional ataman mandate | Unsustainable equipment, a successful peace, or a strong civilian compact |
| Real Soviet partner with accessible deliveries and compatible guarantees | Socialist service | Leadership removal demands, coercive recruitment, broken support, or incompatible wars |
| Threatened Terek frontier with a feasible sponsor | Defined service autonomy | A distant offensive demand or a stronger reciprocal local settlement |
| Viable Ural economy and willing neighbors | River commons or regional coalition | Closed access, overmobilization, or conflicting coalition promises |
| Actual refugee or exile contact with receiving capacity | Bounded return or sanctuary | No safe passage, insufficient housing, or an unacceptable patron |
| Strong Russian bridgehead and defensible route to the heartland | Cossack Russia | Unready army, inability to govern acquired states, or an affordable regional peace |
| Lower Volga base and distinct willing steppe counterparts | Negotiated Golden Horde commonwealth | A failed congress, a contested capital, or incompatible partner demands |
| Strong military control but weak voluntary support | A contested imperial or military claim can be considered | The AI must still survive the resistance, diplomacy, and supply consequences |

The AI must not reduce every ideology to one unavoidable route.
A fascist or authoritarian counterpart can offer an attractive arsenal and dangerous terms.
A democratic counterpart can refuse an unwanted military alliance.
A socialist counterpart can value service without accepting independence.
The response follows actual interests and institutional commitments.

The popular service crown, Horde regency, and Ukrainian hetman routes use an authentic institutional solution when no verified named candidate is available.
AI must not become stuck waiting for a person who died, is already owned elsewhere, or has no valid return route.

## Target selection and player weighting

Initial selection uses a country draw followed by a state draw.
That prevents a country's number of map subdivisions from determining its entire crisis exposure.
State selection then favors actual frontier opportunity and a documented host connection while keeping every otherwise valid state possible.

The 1.25 player-target factor is a multiplier within the full candidate calculation.
It is not an added 25 percentage points.
For two otherwise equal eligible authorities, one human and one AI, the proposed conditional country probabilities would be 1.25 divided by 2.25 and 1 divided by 2.25.
Those are approximately 55.56 percent and 44.44 percent in that deliberately simplified pool.
Real pools include instability, war, crisis load, near-capitulation, state composition, and the shared scheduler.
Their final probabilities require the full source-backed model.

Mixed legal-owner and controller cases need candidate-level treatment of both affected countries.
Their player and crisis-load factors must be applied once.
The occupied-state adapter must prove its complete-pool calculation before that variant is enabled.
Neither a player factor nor a low crisis count bypasses physical validity or the three-crisis cap.

The Hosts Answer has one selected source and at most one new answer roll per 30-day observation.
Its source-selection and answer-probability stages must not apply the human factor twice.
Source cooldown is 120 days for an AI-only authority and 90 days for a player authority after a committed answer.
Changing control cannot shorten an already committed cooldown.

## Military AI

The AI uses native templates and normal reinforcement.
It does not receive replacement units to compensate for poor deployment.
Its force plan retains a viable capital defender and a real reserve before an optional raid or expedition.

Cavalry is used for screening, suitable mobile operations, defense in depth, and pursuit.
The AI should not send a small mounted force into repeated unsupported frontal attacks against a prepared modern army.
Infantry and artillery provide the staying power for harder combat.
Motorized formations are considered only when fuel and truck replacement are sustainable.

The native raid model requires a predicted success value of at least 0.55 for ordinary AI use.
A target also needs actual military value and a legal route.
The AI compares the risk to its committed formation with the bounded disruption or capture benefit.
A peacetime store raid needs a real border dispute and must include its Legitimacy and diplomatic costs in that comparison.

An AI can stop raiding after modernization makes ordinary production more useful.
It can continue reconnaissance and defensive operations under native military systems.
The design does not require a raid every time its cooldown expires.

## Economic and diplomatic AI

An arms purchase needs a supplier that can actually deliver.
The AI reads the exact equipment model, quantity, price, route, deadline, and existing obligations.
It avoids immediate reversed trades and the reuse of reserved stock.
A discount changes the price the parties actually pay and receive rather than creating the difference as free Political Power.

An AI needs real reception capacity before encouraging civilian return.
It should prefer a smaller safe cohort to an ambitious movement with no destination.
When a corridor closes, it protects the existing receipt and seeks a valid redirect or return.
It cannot abandon an actual cohort to start a more profitable new one.

A confederal AI treats member autonomy as part of the bargain that creates its strength.
It can request more central power.
It must face the response and pay the political cost if it breaks the charter.
Voluntary merger is assessed separately from alliance.

## Proposed balance targets for controlled future comparisons

| Area | Proposed target | What the target does not claim |
| --- | --- | --- |
| Small valid opening | A genuinely playable force with replacements and no more than eight initial divisions | Guaranteed victory against its former owner |
| Strong-source opening | Formula and equipment caps still hold under very large source manpower | A fixed ratio to every major power's total army |
| Civil survival in a protected fixture | Most eligible AI hosts pursue an arsenal and charter within the first year when war and supply do not prevent it | A measured percentage in live campaigns |
| War survival | A severe source crisis creates credible local survival and negotiation opportunities | An arbitrary universal survival rate across maps and wars |
| Great-project pacing | A national transformation normally takes several years of actual development and campaigning | A fixed historical date or forced player timetable |
| Host proliferation | At most four simultaneous Event 112-created independent hosts and twelve active country participants | Four guaranteed new countries |
| Material assistance | Donor floors and actual route capacity constrain every delivery | Automatic success after a diplomatic yes |
| Meter recovery | A settled host can recover toward 60, while higher values require actual institutions and outcomes | Passive maximum values or recurring war drain |
| Raiding | Bounded disruption or measured capture with meaningful risk and persistent cooldowns | A renewable replacement for industry |
| Regional endpoint | A viable one-state or limited host can complete a durable settlement | A requirement to conquer an empire to finish the event's content |

These targets should be evaluated across named fixtures and compared before and after any weighted change.
If a target fails, the owner changes the relevant design parameter or source implementation.
The auditor must not silently redefine success to match the result.

## Scenario families

The complete numbered F-series founding and transaction cases are in part 03.
The evolution and lifecycle cases are in part 07.
The implementation usage map adds 54 named cross-domain cases with specific evidence requirements.
Those are planned cases, not executed tests.

The following integrated campaign fixtures connect those unit-level contracts into meaningful play.

| Fixture | Setup | Questions to resolve |
| --- | --- | --- |
| V01 Small peaceful frontier | Case A-style source, one valid industrially poor state, no evolution | Can the host complete A01 from the lowest clamped meters, honor the day 30, 60 and 90 checkpoints, and ratify a civilian charter after its 30-day hold without a second state or offensive-readiness gate? |
| V02 Occupied collapse | Distinct legal owner and controller, major war, competing claims | Does the enabled occupied-state adapter preserve wars, units, requester identity, and the correct source snapshot? |
| V03 Soviet Collapse overlap | DHC dormant, KHC already alive, concurrent 005/006 reservations | Does exactly one release win while the living Kuban country keeps its content? |
| V04 Maximum pressure | Case D-style source, two existing local crises, human displaced authority | Do force caps, crisis admission, player weighting, and counterpart responses remain correct? |
| V05 One-state civic recovery | Low C and J, poor army readiness, one affordable local council path | Can the country recover without conquest, a second state, or a repeated grant? |
| V06 Professional modernization | Real cavalry force, limited arsenal, later truck and fuel access | Do training and conversion consume actual resources and preserve unit identity? |
| V07 Confederation disagreement | Three distinct willing hosts, one refuses an unrelated offensive | Does the agreed charter distinguish lawful refusal from breach and preserve partner agency? |
| V08 Russian national bid | Home host, real heartland bridgehead, existing rival national government | Does the route require Moscow, civilian settlements, viable access, and a genuine constitutional outcome? |
| V09 Golden Horde congress | Lower Volga base, distinct steppe counterparts, an existing Mongolia | Do mandates, sovereignty, religion, rival claims, and later tribute or commonwealth terms produce different play? |
| V10 Failed refuge corridor | Real civilians debited, route changes, receiving authority annexed | Does every person remain on one measured disposition with no duplicate destination credit? |
| V11 Evolution before firing | Shared tier and world gates satisfied, no principal host yet | Does activation remain inert until the root rising, then use one day-14 bootstrap without a second new country? |
| V12 Saturated resurgence | Four created hosts, twelve participants, pending deliveries and exile actors | Does the system reject new discretionary work without deleting identities or obligations? |
| V13 Defeat and restoration | Principal loses all states while a partner and a real evacuated cohort survive | Does coordinator succession preserve physical assets, Fire-Once history, and the original used grants? |
| V14 Complete presentation | Long country names, missing optional contact, invalidated selected territory, mature route | Do the two meters, filtered actions, state puzzle, flags, reports, and focus tree remain truthful? |

V01 and V05 are especially important.
A complex national tree cannot compensate for an opening economy or charter path that is impossible to complete.
V01 also uses a quote above the initial 40 Political Power, an interrupted founding mission, a single viable under-equipped formation and a delayed assembly start.
It verifies ordinary funding, preserved finite receipts and eventual lawful recovery without a grant reset.
A generic H12 host with no external contact must be able to reach GP08 regional consolidation from Cohesion 60 and Legitimacy 60 after completing its real civilian, economic and service work.
V08 and V09 must be run for each accepted institutional ending rather than testing only the easiest variant.

## Probability evidence

Every weighted surface needs an inventory.
This includes initial country and state selection, source and outcome selection in the evolution, counterpart responses, focus scores, decisions, raids, and any research behavior that the event changes.

Before editing a weighted implementation, preserve actual immutable source bytes and the exact scenario fixture bytes.
Record their hashes.
The owner then applies the chosen change.
The read-only probability auditor uses the same fixture set for the required before and after comparison.

A probability result must say whether it is exact, bounded, sampled, score-only, or unresolved.
A model that lacks the native engine's external factors cannot claim an exact final game percentage.
A seeded simulation needs its actual seed, sample count, uncertainty interval, and assumptions.
A static MTTH or a partial event pool does not establish cumulative campaign timing.

Focus choice, native raid interpolation, and generic weighted random selection can have different engine semantics.
The implementation must use the appropriate verified adapter for each.
It cannot normalize all of them with the same spreadsheet formula and call the result validated.

## What planning has actually verified

The source-reading gate is complete for all supplied project text variants.
The repository inspection established particular carrier, catalog, and shared-helper facts at the pinned revision.
The architect evaluated the seven proposed opening examples and their arithmetic invariants.
The package review checks design consistency, required coverage, and the integrity of the delivered files.

No game was launched.
No installed map or mod-stack collision scan was completed.
No HOI4 MCP inspection, render, probability comparison, native raid, save-state test, or live campaign result is claimed.
Those are implementation and release evidence requirements.

The specification is complete as a planning deliverable when every intended route, system, dependency, and review disposition is present.
The gameplay is complete only after its actual implementation and the relevant source, visual, mathematical, and runtime evidence agree.


## Additional closure scenarios from planning review

The no-industry variant of V01 fills every factory slot and removes any repairable military factory.
It must be excluded unless the exact installed native civilian-to-military conversion route is verified and actually available.
A future arms invitation alone cannot pass that check.
M02 and M05 must expose their provisional native templates at funded start, without granting a unit or technology, so the required trained formation can exist before completion.
For each great-project constitution, record the ordinary meter baseline, all actual political and physical work, the one finite endorsement receipt and the unchanged final formation checks.
Repeat the constitutional branch switch after endorsement and confirm that it cannot collect a second variant's budget.
For GP05, GP06 and GP07, complete the treaty form first and confirm all member flags remain unchanged.
Then test the optional principal-only constitutional identity act with owned anchors and an accepted mandate, and repeat it with one partner refusing or an anchor controlled by someone else.
