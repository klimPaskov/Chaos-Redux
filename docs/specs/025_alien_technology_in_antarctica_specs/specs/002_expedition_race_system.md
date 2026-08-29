# Expedition race system

## Core loop

Each participant manages one expedition through a country-scoped ledger.

The player reads three visible values, chooses one of the currently relevant actions, completes phase missions, reacts to hazards or rivals, and decides when to attempt the next major step.

The runtime advances through bounded event-owned pulses over the stored participant roster. It does not scan every country.

## Visible values

### Expedition Progress

Expedition Progress is the primary value and uses a range from 0 to 100.

It represents the verified movement toward locating and securing the recovery core. Progress is phase-aware. A country cannot skip the outpost, survey, and final recovery gates by reaching a numeric threshold early.

Progress rises from:

- completed phase missions
- strong logistics
- successful surveys
- signal tracking
- recovered rival data
- intact outposts
- suitable research and electronics capabilities
- route-specific preparation
- controlled risk-taking

Progress falls or becomes temporarily blocked from:

- loss of the staging route
- outpost destruction or capture
- false coordinates
- severe weather setbacks
- prolonged supply failure
- high exposure incidents
- failed recovery attempts
- withdrawal

### Logistics Readiness

Logistics Readiness uses a range from 0 to 100.

It represents the current ability to move people, fuel, equipment, and recovered material through the expedition route. It is affected by committed convoys, fuel, support equipment, civilian capacity, route burden, outpost condition, convoy interference, and emergency resupply.

Readiness determines whether a mission can begin, how quickly it advances, and whether a setback becomes manageable or severe.

A high stockpile does not keep readiness permanently high. Supplies must be committed through phase actions and can be damaged or intercepted.

### Exposure Risk

Exposure Risk uses a range from 0 to 100.

It represents combined exposure to Antarctic hazards, active signals, unknown biological or mechanical contact, damaged containment, reckless recovery, and prolonged work around alien material.

It is not the Event 016 Exposure value. Internal identifiers must remain event-scoped and distinct.

Exposure Risk affects:

- accident chance
- personnel losses
- equipment damage
- signal incidents
- survivor encounters
- Evolution V aftermath severity
- which containment and concealment actions become available

After the winner is declared, the same meter may change its visible label to Alien Dependence for countries that retain material under Evolution V. The underlying event-owned ledger may continue, while the player sees one coherent support value and no fourth meter.

## Hidden participant values

The following values support the mechanic but do not appear as equal-status meters:

| Internal value | Purpose | Player presentation |
| --- | --- | --- |
| Survey certainty | Accuracy of the current crash-zone model | Site markers and concise tooltip |
| Outpost integrity | Physical condition and security of the base | Outpost frame and status label |
| Crew condition | Health and cohesion of personnel | Status icon and incident tooltip |
| Expedition intelligence | Knowledge of rivals and routes | Rival-card detail level |
| Route burden | Distance, access, sea pressure, and staging difficulty | Route band and cost breakdown |
| Current commitment | Active material and civilian capacity | Readiness tooltip |
| Sabotage exposure | Vulnerability to hostile actions | Counterintelligence state |
| Hostility | Rival-specific escalation state | Rival-card stance icon |
| Fragment score | Verified recovered material | Recovery inventory |
| Recovery priority | Tie resolution for simultaneous operations | Hidden, explained only when needed |

These values exist to support decisions. They should not become another wall of numbers.

## Global event values

| Global value | Role |
| --- | --- |
| Event phase | Current global race phase |
| Recovery core secured | Ends primary winner competition |
| Wreck integrity | Used by Evolution IV |
| Signal intensity | Used by Evolution I |
| Survivor pressure | Used by Evolution II |
| Militarisation | Used by Evolution III |
| Fragment sites remaining | Used by Evolution IV |
| Entry window remaining | Controls participation |
| Active participant count | Bounded roster status |
| Winner identity | Stored country scope |
| Event 036 arbitration tier | Shared alien-recovery result state |

## Participant roster

The event creates a stored participant roster at initialization.

The roster includes:

- every human country that accepts during the entry window
- the selected AI major countries
- the narrow valid Kruger State exception when applicable

AI selection occurs after the human invitation state is known or through reserved slots that are safely reduced when humans enter.

The preferred ordinary size is four to eight participants. The mechanic must remain valid with one participant, many human participants, or no valid AI majors.

The GUI uses a scrollable rival list or a five-card priority view plus an Other Expeditions row. It must not discard participants only because they do not fit on one static panel.

## Participant identity and persistence

Each participant needs a stable participant identifier that survives save and reload.

The implementation should use the repository's proven country-array and event-target patterns. It must not rely on temporary event targets for the full event lifetime.

Every participant row stores or can derive:

- country scope
- participant identifier
- route band
- selected gateway
- current phase
- progress
- readiness
- exposure
- survey certainty
- outpost integrity
- crew condition
- fragment score
- action cooldowns
- rival hostility records
- withdrawal or elimination state
- reward tier
- winner state

Parallel arrays must stay aligned. A dedicated rebuild or audit helper should verify array lengths before every major roster rebuild.

## Bounded pulse model

The race advances through one scheduled hidden event or event-owned pulse chain.

Recommended behavior:

- normal pulse every 10 to 15 days
- longer delays when no participant has an active mission
- immediate bounded refresh after a player action that changes visible state
- no `on_daily`, `on_weekly`, or `on_monthly` whole-world iteration
- no recurring random-country scan
- no continuous target recalculation outside the stored roster

Each pulse processes only active participants and the rival records needed for their current actions.

The pulse performs these steps:

1. validate each stored participant
2. clean invalid targets and expired cooldowns
3. resolve active missions
4. apply supply consumption and route pressure
5. update readiness and exposure
6. apply bounded weather or anomaly incidents
7. update progress where phase conditions permit
8. check evolution incidents
9. check final recovery completion
10. rebuild visible board state when needed
11. schedule the next pulse

## Progress calculation direction

Progress gain should use a dynamic factor model.

A conceptual model is:

`phase base + readiness contribution + survey contribution + outpost contribution + active mission contribution + technology contribution + intelligence contribution - route burden - weather pressure - exposure pressure - sabotage effects`

The implementation must centralize each factor in script constants or a documented tuning file.

Progress gains should be bounded per pulse. A country cannot jump through a phase from one event option.

## Readiness calculation direction

Readiness changes from actual commitments and current conditions.

Positive factors include:

- successful resupply
- direct southern gateway
- intact ports and staging rights
- strong convoy and fuel reserves
- outpost repairs
- escort protection
- prepared aviation support
- spare equipment caches

Negative factors include:

- long or chartered routes
- wartime convoy pressure
- hostile interception
- severe weather
- damaged outpost
- repeated rush actions
- fuel shortage
- lost gateway access
- failed evacuation

Readiness must have a protected minimum only during brief setup transitions. A participant that cannot sustain the route should be forced into emergency recovery or withdrawal.

## Exposure calculation direction

Exposure should rise from choices and incidents, not from passive time alone.

Major sources include:

- tracking an active signal without shielding
- entering opened compartments
- attempting survivor capture
- handling unstable fragments
- rushing the primary wreck
- concealing accidents
- continuing study after Evolution V

Mitigation includes:

- shielding and isolation equipment
- remote study
- medical quarantine
- controlled recovery
- destroying contaminated material
- transferring material to a prepared partner
- withdrawing exposed personnel

Exposure may drift down slowly only when the expedition has safe containment and no active high-risk operation.

## Route burden

Route burden is derived from the best valid staging route the country can actually use.

The route system recognizes four broad bands:

1. direct southern gateway
2. established long-ocean route
3. chartered or allied gateway
4. improvised distant route

A route is based on controlled ports, access agreements, staging rights, convoy ability, and current war conditions. Capital distance alone is insufficient.

A country may improve its route by securing access to a better gateway. Losing access can worsen the route during the race.

## Gateway groups

The implementation should map named gateway groups to actual live states after repository and map inspection.

The design groups are:

- southern South America and the Falklands route
- southern Africa and Cape route
- Tasmania and the Australian southern route
- New Zealand and South Island route
- other verified sub-Antarctic staging possessions present in the live map

The player-facing interface should show the selected gateway or route family. It should not expose raw state IDs.

## Weather and seasonal pressure

Weather is a bounded expedition hazard, not a global climate system.

The event may generate:

- pack ice delay
- whiteout
- crevasse loss
- radio blackout
- fuel freezing or engine damage
- katabatic wind damage
- sea-ice route closure
- short clear-weather window

Weather incidents use the participant route, phase, preparation, and readiness. They do not require a whole-world weather scan.

The system may use broad austral-season bands if the live date and engine support make this reliable. Seasonal logic must never make the event impossible outside a narrow calendar window.

## Rival knowledge

Rival cards show only information the participant has earned.

Default visible information:

- country name and flag
- active or withdrawn state
- broad phase
- public posture

Additional intelligence may reveal:

- approximate progress band
- readiness band
- current route
- recent incident
- suspected target site
- exposure warning

The board must distinguish confirmed information, estimate, and unknown state.

## Anti-runaway rules

The event should reward preparation without becoming automatic for the largest major.

Use these controls:

- phase gates
- bounded progress per pulse
- diminishing returns from repeated identical actions
- material consumption over time
- route and war pressure
- rival counterplay
- final mission duration
- exposure from reckless acceleration
- a requirement to maintain readiness during final recovery

Do not use hidden rubber-band bonuses that make the leader lose for no stated reason. Catch-up comes from available actions, rival choices, fragment routes, and the leader's higher exposure to sabotage.

## Tie resolution

When two final recovery missions complete in the same pulse, resolve the winner by:

1. earlier recorded mission start or completion timestamp according to the live mission pattern
2. higher verified survey certainty
3. higher logistics readiness
4. lower exposure risk
5. higher outpost integrity
6. one seeded bounded random roll only if every prior factor is equal

The result should be recorded in the event log detail data so a human player can understand a close loss.

## Participant invalidation

A participant is invalid when it no longer exists, enters a terminal state, loses every valid staging route for a prolonged period, or cannot maintain the minimum expedition commitment.

Invalidation triggers a cleanup event that:

- cancels missions
- clears rival target records
- converts recoverable progress into the correct fragment or withdrawal state
- releases temporary civilian commitment
- records casualties or equipment loss already incurred
- removes the country from active processing
- preserves historical event details

Capitulation alone does not instantly delete the expedition. A short evacuation or seizure window may allow an ally, occupier, or rival to recover exposed personnel and data.
