# State Selection and Spread Model

## Initial mainland origin scoring

| Scoring component | Relative importance | Notes |
| --- | --- | --- |
| Population size | very high | use tiers or normalized population rather than a flat bonus |
| Low development or state category | high | favors neglected regions |
| Poor infrastructure | high | increases isolation and weak response |
| Weak national preparedness | high | rewards prevention before the event |
| Weak local medical access | high | can be derived from hospitals, supply, and control |
| Occupation and resistance | medium | represents broken administration |
| Frontline or troop concentration | medium | creates early movement routes |
| Refugee or migration pressure | medium | uses shared route data when available |
| Port or rail hub | low to medium | improves later escape but should not dominate the origin roll |
| Capital status | negative | capital remains possible when genuinely vulnerable |
| Strong prevention law | strong negative | never creates full immunity |
| Recent disease cleanup memory | strong negative or temporary exclusion | prevents immediate unfair recurrence |

## Origin validation

- one valid human owner or controller
- one meaningful mainland connection
- no island fallback
- sufficient population
- not wasteland
- not nonhuman-controlled
- not already Black Plague infected
- event log actor can be assigned

## Route scoring

| Route | Base availability | Main positive factors | Main negative factors | Evolution gate |
| --- | --- | --- | --- | --- |
| land adjacency | adjacent states | source load, open border, high target population, war | border closure, target preparedness, natural barrier | baseline |
| internal rail and supply | same controller or valid internal route | rail hub, strategic redeployment, troop movement | route restriction, inspection, damaged connection | baseline |
| cross-border military | warfront, occupation, volunteers, expeditionaries | troop density, captured state, hospital collapse | decontamination, command restriction, protected route | baseline |
| refugee or migration | real movement route | displacement, resistance, state collapse | reception screening, safe corridor, surveillance | baseline when compatible route exists |
| port local exposure | infected coastal state | port size, cargo, troop return | inspection, closure, strong surveillance | baseline local only |
| overseas port jump | source and destination port link | convoy, trade, access, port size, rat stowaways | inspections, closures, isolation, countermeasure | Evolution II |
| biological strike | existing delivery system | payload, delivery success, weak target defense | interception, partial failure, strong countermeasure | project completion |
| rat occupation | rat unit captures state | rat strength, duration, disease dominion | rapid human liberation and clearance | Evolution III |
| Rat King sea campaign | royal port and campaign route | Sea Broods, Dominion, captured ports | naval and air control, closed relief ports | Rat King late branch |

## Target outcomes

| Exposure result | Use case |
| --- | --- |
| no status change | protection exceeds route score |
| Threatened | credible exposure without established infection |
| Incubating | ordinary successful spread |
| Infected | severe source, weak target, rat occupation, or strong weapon deployment |
| high-load Infected | catastrophic rat occupation, doomsday release, or special late route |

## Spread pacing targets

- first month should normally threaten nearby states without creating a continental epidemic
- an untreated origin should often create one to three new infected states by the end of the first three months
- a weak regional response should create several new states per month by the middle phase
- Evolution I increases pace by a noticeable but containable amount
- Evolution II port jumps should be uncommon per route and important when they occur
- Rat-Controlled states should infect newly occupied territory reliably

## Movement restriction tradeoffs

| Restriction | Spread reduction | Strategic cost |
| --- | --- | --- |
| targeted border corridor closure | high cross-border civilian reduction | trade, supply, relations |
| full border closure | very high civilian reduction | severe trade, diplomacy, movement cost |
| port inspection | medium to high sea-route reduction | convoy and port throughput |
| port closure | very high sea-route reduction | overseas supply and trade loss |
| troop route restriction | high military-route reduction | reinforcement and planning loss |
| civilian travel suspension | high domestic movement reduction | factory, construction, stability loss |
| sealed state transport | maximum combined reduction | extreme supply and humanitarian risk |

## Triggerable scenario distribution model

The manual scenario uses the normal vulnerability score but adds geographic spread and actor-package requirements.

| Scenario component | Selection rule |
| --- | --- |
| Continents | choose distinct eligible inhabited continents before adding extra anchors to one continent |
| Anchor basins | high population, low development, weak capacity, dense cities, ports, rail hubs, occupation, movement, and connected states |
| Established states | allocate the global intensity target among selected continents by population, vulnerability, and valid connected basins |
| Threatened ring | add adjacent and transport-linked states around each anchor |
| Rat Nation basins | connected severe plague clusters with safe capital and transfer state |
| Royal Basin | strongest remaining cluster with defensible capital, high Rat Infestation, and enough separation to preserve independent broods |
| Existing actors | count existing infected states, Rat Nations, and Rat King toward targets instead of duplicating them |
| Small or altered maps | scale optional counts down after the minimum valid two-continent, two-brood, one-King setup |

The scenario performs one full mapmode rebuild after all seed states and actors are registered. Ordinary live play returns to affected-state refreshes.

## Performance model

- maintain an array or registry of active Black Plague source states
- maintain threatened targets only while exposure exists
- batch ordinary spread on a weekly cadence
- use immediate targeted updates for occupation, deployment, and major route changes
- avoid scanning every world state on an unrestricted daily country on-action
- clean stale state references after cure, annexation, tag destruction, scenario bootstrap, and world end
