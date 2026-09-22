# Part 6: AI direction and shared systems

## A front the AI can use

The opening should put the Japanese AI in a position to fight immediately.
It must receive legal units, accessible objectives, command capacity, usable unloading points, and a coherent land front together.
A high aggression score cannot compensate for a broken supply network or units that the engine sends back to Asia.
Acceptance therefore depends on observed deployment and movement as well as valid script.

Japanese priorities are to retain the principal access points, connect adjacent concentrations, take an additional port, capture western transport junctions, and exploit a weakened route inland.
The invasion army should normally remain in the American theater during the opening campaign.
Reserve enough infantry to protect access and exposed connections, then concentrate the offensive force on a useful axis.
At higher tiers, coastal groups should aim to meet rather than scatter inland in disconnected columns.

American priorities are to secure the routes out of the landing area, reinforce threatened western cities, preserve rail connections from the interior, prevent another ordinary coastal landing, and counterattack an isolated or undersupplied Japanese concentration.
The American AI can recall forces through ordinary movement and transport.
It does not receive a global army teleport, free instant deployment from Europe, or a command that removes Japan from the map.

## What is intended and what must be proved

The design requests theater priority, sensible objectives, and a usable command structure.
It does not assume that a script effect can assign every division to an exact front or order a particular encirclement.
The implementing agent must inspect the supported AI strategies and current repository patterns before choosing the mechanism.
Unsupported tactical precision must remain an explicit limitation, not a fictional API.

During validation, inspect the first day, day 3, day 7, day 30, and day 90.
The first day should show a coherent deployment with viable access.
By day 3 the AI should have useful orders or demonstrate a defensible reason for holding.
By day 7 it should be fighting or preparing a reachable operation, unless overwhelming local resistance makes an immediate assault unreasonable.
The expected opening retention target is at least 80 percent of the created cohort in the mainland theater through day 90 while a useful front remains.
This is an observational target for ordinary conditions, not an instruction to trap retreating units or a claim that a reliable per-division scripting registry already exists.

A failed offensive can be acceptable.
A stationary army with no usable orders, a forced return to Japan while the beachhead stands, repeated transport suicide, or chronic supply collapse caused by the opening design is not acceptable.
A well-prepared American player can defeat the invasion.
The event must create a meaningful fight, not guarantee a minimum occupation duration through hidden invulnerability.

## Japan's operational choices

When ports are threatened, the AI prioritizes defense and the unloading repair action.
When supply is adequate and an adjacent port is lightly defended, it prioritizes that port and a supported coastal advance.
When two concentrations can be joined, it values the connecting corridor more highly than an unrelated inland city.
When the principal connection is secure, it can prepare an inland offensive against an actual transport objective.

Follow-on deliveries are useful when the front has room for additional formations and the next batch can arrive at a retained access point.
They are undesirable when existing units already exceed supported capacity.
The AI must not spend fuel and Command Power on an offensive preparation while it is about to lose its only port.
Nor should it repeatedly repair a secondary port with no useful route to the army.

Japan's existing theaters remain part of its war.
Event-specific priority applies to preserving and exploiting this newly created force.
It should not require stripping every home-island defender, abandoning an immediate capital defense, or emptying another human-controlled coalition front.
Ordinary strategic retreat remains possible when the mainland position is no longer viable.

## The American response

The AI first evaluates the actual mainland threat and the approach routes it can still defend.
It should concentrate regular forces before buying emergency formations that would compete with an already empty equipment pool.
A paid local batch is valuable when it fills an undefended sector with supplied troops.
It is a poor choice when newly created divisions would arrive under-equipped or consume the equipment needed to restore a stronger existing formation.

Railway priority is attractive when inland transport is the limiting factor.
City preparation is attractive at a connected position that protects a meaningful route.
Port protection is attractive when another coastal entry would expose a new region.
Counterattack preparation is attractive when American forces can cut a connection or attack an isolated access point.
These priorities use the same legal targets, budgets, and costs as the player.

The response must remain urgent at all tiers, including a losing Japanese war.
The AI must inspect the new mainland situation instead of dismissing Japan because its national fleet, home industry, or overall war score is weak.

## AI assistance must leave human command intact

No player order is overwritten to enforce an AI demonstration.
A human Japan receives the force, objectives, warnings, and decisions, then controls its operations.
A human United States controls its own response.
Switching player ownership during an episode must not repeat the army grant, reset a mission, change paid costs, or reroll the campaign factor.

Temporary AI strategies belong to the episode and are removed when their purpose ends.
Removing them must not delete unrelated strategies added by another event or country focus.
An expedition that remains after the end of special support becomes an ordinary army with ordinary strategic behavior.

## Probability and performance review

The proposed active-evolution timing is an eligible MTTH target of about 90 days.
Decision scores, target weights, and any randomized choice among equally suitable landing profiles require the repository's probability workflow.
Relative weights are not percentages, and an MTTH value is not a guarantee of firing by that date.

The pending `chaosx_ai_probability_auditor` must begin with `hoi4.probability_inspect`.
It then evaluates named scenarios, sweeps relevant thresholds, simulates only declared uncertain inputs, compares revisions, and renders evidence where useful.
An unavailable game-version timing adapter leaves timing conclusions unresolved.
No such tool run has been performed for this package.
The scenario contract is in `reference/074_capability_and_probability_gates.md`.

Recurring event work is confined to Japan, the United States, and a bounded registry of selected coastal and objective states.
Do not introduce a daily world scan or poll every country for this one invasion.
Reuse the existing periodic framework where possible.
The chosen cadence must support the stated continuous-hold and access-loss timers accurately.

## Chaos impact map

The catalog Chaos level remains 1 and the Wars membership remains Medium.
These classifications do not require every consequence to add exactly one point.
Use the shared Chaos provider and its bounds for the following proposed event-specific consequences.
All numbers below are tuning anchors that require a review alongside the existing common sources.

| Material consequence | Proposed Chaos change | Receipt and reversal |
| --- | ---: | --- |
| A real new Japanese mainland front is established at baseline, I, II, or III | +10, +15, +20, or +30 | Once at successful initial commitment, proportional to the starting tier only |
| A new major Pacific access point outside the initial footprint is captured and held for 15 continuous days | +5 | Once for the episode, not once per port |
| A Pacific state containing territory outside the initial footprint is secured through subsequent combat and held for 30 continuous days | +5 | Once for the episode, only after a real territorial gain |
| Two useful inland victory-point objectives outside the initial footprint are held with a coastal connection for 30 continuous days | +10 | Once for the episode |
| An active evolution becomes enabled or is selected | 0 | A stage flag is not itself a world consequence |
| A decision is clicked, an army is paid for, or a report is acknowledged | 0 | No repeated administrative Chaos income |
| A credited territorial milestone is durably reversed by American or allied recovery | Reverse its outstanding event-specific credit | One reversal per credited milestone, no payment without a matching prior credit |
| The initial front is contained and the original territory is restored to the United States or its legitimate wartime allies for 30 days | Reverse the outstanding initial-front credit | Do not also reverse the same credit through another terminal callback |

Maximum distinct positive event-specific credit is 30 at baseline and 50 at an initial tier III opening.
Active upgrades do not pay the difference between those initial-shock values.
The larger army can enable real territorial milestones, but no second landing shock is credited.
This prevents a stage upgrade and the same territorial change from being counted as separate new invasions.

If Japan already has a major operating mainland front before the event, grant the requested reinforcement but do not award the initial new-front credit again.
An existing isolated coastal province without an operating army does not automatically constitute a major front.
The capability review must define a measurable existing-front predicate before coding this distinction.
It must not turn that predicate into an eligibility restriction.

Shared war declarations, peace, capitulation or annexation, army buildup thresholds, and deaths keep their normal owners.
Event 074 does not duplicate their payments.
The initial-front credit describes the new theater, not the creation of a specific number of divisions.
The balancing review must examine a case in which the opening crosses a shared army-buildup threshold and reduce overlapping event pressure if that combination is excessive.

Negative recovery payments cannot exceed the outstanding positive credits of this episode.
A Japanese recapture after a reversal does not recreate the same credit.
Neutral conquest, a separate world event, or a peace settlement that leaves Japan's occupation intact does not qualify as American recovery.
Terminal cleanup must retain the permanent receipts needed to prevent duplicate payments.

## Interaction with other Chaos Redux systems

The shared war and occupation systems own ordinary combat and territorial consequences.
The deaths system owns actual losses through its established providers.
Event flavor about evacuation, abandoned factories, or damaged housing does not itself remove population, add recorded deaths, or justify a second casualty counter.
No additional famine, migration, contamination, condemnation, or global-threat subsystem is introduced here.

If a different event already affects the selected territory, retain its state data and combine effects through the existing APIs.
A Japanese landing must not cure a famine, erase chemical contamination, remove fortifications from Event 064, or reset another event's state modifier merely because it prepares a port.
Only Event 074's own temporary support is removed during its cleanup.

Shared force-provider concepts may be reused only where their documented budget and country-neutral contract fit ordinary Japanese units.
The portal-raid implementation is a useful reference for transactional controller changes and creation receipts.
It is not permission to add teleportation equipment, portal troops, or Event 016 flags to this invasion.
See the source register for the exact inspected repository material.

## News and history records

The initial landing consumes one fire-once history entry and one shared timer selection.
Its reports, missions, deliveries, and later battlefield news do not count as additional random-event selections.
Active evolutions use the established evolution-history pathway and its actor fields.
A skipped disabled stage does not create a fictional history record for that stage.

History must distinguish the initial footprint from later conquest and should retain the highest realized tier, whether special support ended, and the broad outcome.
It must not claim an American victory merely because the supply timer expired.
Nor should it claim Japan conquered the United States merely because tier III was selected.
