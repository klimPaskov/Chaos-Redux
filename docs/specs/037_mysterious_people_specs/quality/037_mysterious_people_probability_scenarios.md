# Event 037 probability and weighted-logic scenarios

## Purpose

This matrix defines the scenario contract for every weighted Event 037 surface. It does not assign final percentages before implementation exposes the complete pool and external factors.

The probability auditor must begin with `hoi4.probability_inspect`. It should classify each result as exact, bounded, sampled, score-only, or unresolved. Any patch to weights requires a baseline audit, an owner-applied patch, and `hoi4.probability_compare` over the same scenario IDs.

## Surface inventory

Weighted surfaces expected during implementation:

- evolution MTTH and modifiers
- policy AI choice
- national response decision AI
- selected-state priority
- settlement destination selection
- foreign donor selection
- foreign reception response
- extreme-policy choice
- flavour-event pool
- local event-option AI
- project complication or success variation when random behavior is retained
- cluster participation only if Various Anomalies receives a live cluster contract

## Evolution timing scenarios

| ID | Scenario | Expected result | Required evidence |
| --- | --- | --- | --- |
| `EV37-EVO-001` | Chaos `200`, one prior firing, low world share, no country above Strained | Evolution I becomes possible near its base timing without immediate certainty | inspect, evaluate, timing render |
| `EV37-EVO-002` | Chaos `200`, recent firing, several Strained countries | Evolution I is faster than `EV37-EVO-001` | compare and sensitivity |
| `EV37-EVO-003` | Chaos `400`, world share above `5%`, several Overcrowded countries | Evolution II is materially faster than low-pressure eligibility | evaluate and compare |
| `EV37-EVO-004` | Chaos `600`, world share above `10%`, one Breakdown country, recent firing | Evolution III has the strongest legitimate acceleration | evaluate and sweep |
| `EV37-EVO-005` | Eligible evolution disabled | Disabled stage has zero activation and no recorded flag | inspect and exact trigger proof |
| `EV37-EVO-006` | Evolution I disabled, Evolution II enabled at `400` | Evolution II can activate and receives required lower mechanics without logging Evolution I | inspect chain and compare |
| `EV37-EVO-007` | First event firing at `650` Chaos with all stages enabled | Highest eligible pre-fire stage is used once, with clean evolution ordering | event chain inspect and sequence proof |

## Policy AI scenarios

| ID | Country state | Expected policy order |
| --- | --- | --- |
| `EV37-POL-001` | Stable democracy, strong food, strong industry, Absorbing | Open Integration first, Managed Settlement second, Restricted Registration distant |
| `EV37-POL-002` | Large authoritarian state, strong transport, Strained | Managed Settlement first, Restricted Registration second, Open Integration lower |
| `EV37-POL-003` | Weak authoritarian state, Emergency, poor services | Restricted Registration can lead, but relief and support decisions remain available |
| `EV37-POL-004` | Stable communist planned economy, large rural capacity | Managed Settlement leads, Open Integration remains viable |
| `EV37-POL-005` | Actual nonhuman country | no ordinary Event 037 policy candidate |
| `EV37-POL-006` | Country with no living mysterious population | no policy candidate |

No single policy should dominate every valid country.

## National response scenarios

| ID | Situation | Expected action order |
| --- | --- | --- |
| `EV37-ACT-001` | Strained, housing bottleneck, strong construction | Emergency Housing leads |
| `EV37-ACT-002` | Strained, transport bottleneck, many trains and fuel | Water and Transport leads |
| `EV37-ACT-003` | Overcrowded, acute food projection | Famine-owned food response dominates unrelated Event 037 projects |
| `EV37-ACT-004` | Emergency during major war, military logistics spare | Military Logistics becomes viable but does not always dominate |
| `EV37-ACT-005` | Emergency during major war, fronts undersupplied | Military Logistics is suppressed to protect the front |
| `EV37-ACT-006` | High pressure, no domestic capacity, friendly donors | Foreign Relief leads over an impossible new-city program |
| `EV37-ACT-007` | Absorbing, high integration, spare industry | Employ New Workforce leads over emergency actions |
| `EV37-ACT-008` | Breakdown, safe destination available | Migration redistribution leads over closed zones for ordinary regimes |
| `EV37-ACT-009` | Breakdown, no safe destination, food route available | Famine relief leads over invalid movement |

## Selected-state priority scenarios

| ID | State set | Expected ordering |
| --- | --- | --- |
| `EV37-STA-001` | one tiny Breakdown state and one major Overcrowded capital | capital can lead due to population-weighted impact |
| `EV37-STA-002` | similar population, one active Famine and one housing strain | Famine state leads |
| `EV37-STA-003` | one trapped border cohort and several Strained states | trapped cohort receives urgent priority |
| `EV37-STA-004` | one invalid state after control change | invalid state receives zero weight and selection clears |
| `EV37-STA-005` | one state already has active project | duplicate incompatible project is excluded |
| `EV37-STA-006` | planned destination with strong capacity | destination can be selected for preparation even with low current pressure |

The auditor should verify that state weighting is not normalized against missing or invalid candidates.

## Settlement destination scenarios

| ID | Candidate set | Expected result |
| --- | --- | --- |
| `EV37-DST-001` | nearby low-pressure state with food and transport | preferred destination |
| `EV37-DST-002` | empty-looking remote state without water or route | strongly suppressed or invalid |
| `EV37-DST-003` | foreign destination with strong reception and access | viable under agreement |
| `EV37-DST-004` | destination at Emergency | invalid or near-zero |
| `EV37-DST-005` | destination changes controller during request | fails closed and no credit applies |
| `EV37-DST-006` | two valid destinations, one closer and one much safer | safety can outweigh distance when crisis is severe |

Exact transfer probability requires complete Migration candidate facts.

## Donor and reception scenarios

| ID | Country state | Expected response |
| --- | --- | --- |
| `EV37-DON-001` | food-secure ally with convoys and low pressure | aid likely |
| `EV37-DON-002` | food-insecure ally at Emergency | aid strongly suppressed |
| `EV37-DON-003` | distant rival seeking influence | conditional aid can be viable |
| `EV37-DON-004` | no route or required stockpile | zero aid candidate |
| `EV37-DON-005` | reception country has spare capacity and open policy | acceptance likely |
| `EV37-DON-006` | reception country near Breakdown | refusal or limited intake dominates |
| `EV37-DON-007` | persecuting requester under high Condemnation | donors can condition or refuse aid |

## Extreme-policy scenarios

| ID | Regime and crisis | Expected ordering |
| --- | --- | --- |
| `EV37-EXT-001` | democracy, Breakdown, relief and settlement valid | support actions dominate, atrocity effectively zero |
| `EV37-EXT-002` | authoritarian, Breakdown, relief valid | coercive control may appear, extermination remains strongly suppressed |
| `EV37-EXT-003` | exterminatory regime, Evolution III, sustained Breakdown, no safe response, existing camp capacity | forced labor or killing can become possible |
| `EV37-EXT-004` | same as `EV37-EXT-003`, but high alliance dependence and monitoring | atrocity materially suppressed |
| `EV37-EXT-005` | prior atrocity exposed, severe sanctions active | further atrocity score reflects regime character and consequences, not automatic escalation |
| `EV37-EXT-006` | pressure below Emergency | extermination and forced labor unavailable regardless of ideology |
| `EV37-EXT-007` | no living mysterious population in target | every targeted extreme action invalid |

The audit must show that systematic killing does not become a general AI pressure optimization.

## Flavour-event pool scenarios

| ID | Context | Expected pool behavior |
| --- | --- | --- |
| `EV37-FLV-001` | first baseline firing, rural state | village, roads, schools, records, and family events dominate |
| `EV37-FLV-002` | Evolution I urban state, housing bottleneck | districts, factory shift, work without homes, and municipal conflict dominate |
| `EV37-FLV-003` | Evolution II active Famine | grain, hospitals, relief, station, and border events dominate |
| `EV37-FLV-004` | Evolution III mysterious majority | majority, maps, second capital, origin classification, and new cities dominate |
| `EV37-FLV-005` | closed zone active | closed-zone and evidence events become possible |
| `EV37-FLV-006` | same country saw one flavour family recently | recent family is suppressed until diversity memory clears |
| `EV37-FLV-007` | no valid target state | no flavour event fires |
| `EV37-FLV-008` | multiplayer with several human countries | each country receives local pool independently without duplicating global effects |

No flavour family should permanently starve when its valid conditions persist.

## Project outcome scenarios

Random complication should be used only where it improves play. Most missions should resolve from visible conditions.

When randomness remains:

| ID | Project state | Expected result |
| --- | --- | --- |
| `EV37-PRJ-001` | fully funded, stable, strong route | success strongly dominates |
| `EV37-PRJ-002` | under occupation, damaged, weak route | complication or partial success rises |
| `EV37-PRJ-003` | requirement became invalid | project fails closed through defined outcome |
| `EV37-PRJ-004` | repeated prior failure | cost or difficulty rises, but success remains possible |
| `EV37-PRJ-005` | hidden random pool incomplete in audit | result marked unresolved, not presented as an exact probability |

## Cluster scenario

Use only after Various Anomalies has a registered cluster and complete member pool.

`EV37-CLU-001` should verify that selecting Event 037 and firing the cluster applies Event 037 exactly once, preserves member skip logic, creates one pacing transaction, and does not normalize against absent cluster members as if they were valid.

## Required audit sequence

1. Inspect the exact weighted surface and complete candidate pool.
2. Record scenario inputs and external state.
3. Evaluate baseline.
4. Render timing, matrix, sensitivity, or comparison view when useful.
5. Apply any bounded patch through the owner.
6. Compare the same scenario IDs.
7. Report dominance, starvation, invalid candidates, uncertainty, and unresolved external factors.
8. Keep the probability auditor read-only.

## Probability acceptance

The weighted system passes when inclusive support dominates viable ordinary cases, coercive and atrocity choices require the mapped conditions, invalid targets have zero participation, evolution timing respects stage and enable state, flavour remains diverse, donors and destinations use real capacity, and no exact percentage is claimed from an incomplete pool.
