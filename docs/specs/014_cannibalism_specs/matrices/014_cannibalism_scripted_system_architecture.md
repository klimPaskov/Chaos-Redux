# Event 014 Cannibalism scripted-system architecture handoff

This is a planning handoff for the scripted-system architect. It is not implementation code.

## Helper map

| Helper concept | Scope | Inputs | Outputs | Side effects | Call sites |
| --- | --- | --- | --- | --- | --- |
| initialize cannibal country state | country | target country, target state, scenario flags | variables for hunger, discipline, fear, containment | sets outbreak flags and opens category | root event, scenario launch |
| calculate cannibal target weight | country | war duration, supply, casualties, stability, terrain, chaos | target weight value | none | random event selection helper |
| refresh cannibal pressure | country | active states, ideas, choices, chaos, supply | updates hunger, discipline, cult, fear, spread | may unlock stage events | event options, decisions, missions |
| add cannibal state pressure | state | pressure type, intensity, responsible country | state modifier or variables | records deaths if needed | incidents, failures, cannibal country control |
| resolve containment success | country | containment, cult, state pressure, spread | success flag or failure flag | closes category if clean | containment mission, cleanup pulse |
| attempt spread jump | country or state | spread channel, source, target pool | new target country or no target | fires exposure event if valid | failed missions, high spread pressure |
| create cannibal commune | state | origin type, severity, owner | new cannibal country or local commune | transfers state, spawns units | Evolution II failure, scenario |
| spawn cannibal forces | country | origin, severity, state population, garrison, chaos | unit and equipment package | consumes or records source pressure | country creation, focus rewards |
| mark cannibal world threat | global | active countries, cult nodes, territory, hidden leader, Wendigo fusion | world threat source state | updates shared world threat | Evolution III refresh, fusion branch |
| cleanup cannibal country state | country | reason | removes flags, decisions, targets | clears variables and targets | containment, annexation, route close |
| cleanup cannibal global state | global | no active actors check | dormant global state | clears world threat if valid | local victories, threat defeat |

## Script constants and tuning groups

Use script constants for:

- opening target weights
- chaos-tier multipliers
- baseline pressure thresholds
- evolution thresholds
- decision cost multipliers
- mission duration bands
- spread channel weights
- state modifier intensity bands
- death-system scaling bands
- cannibal country starting force bands
- AI route weights
- triggerable scenario intensity bands

Use local at-file constants only where the engine rejects script constants in duration fields. Mirror those values in the tuning docs.

## Core variables and flags

Country variables:

- cannibal_hunger_pressure
- cannibal_discipline_collapse
- cannibal_cult_pressure
- cannibal_public_fear
- cannibal_spread_pressure
- cannibal_containment
- cannibal_island_silence
- cannibal_hidden_leader_resonance
- cannibal_active_stage
- cannibal_response_posture

Global variables:

- global.cannibalism_active_countries
- global.cannibalism_spread_count
- global.cannibalism_commune_count
- global.cannibalism_global_cult_pressure
- global.cannibalism_hidden_leader_network_power
- global.cannibalism_wendigo_fusion_readiness

Flags:

- cannibalism_active
- cannibalism_locally_contained
- cannibalism_exploited_cult
- cannibalism_spread_source
- cannibalism_has_silent_island
- cannibalism_country_origin_island
- cannibalism_country_origin_front
- cannibalism_country_origin_prison
- cannibalism_country_origin_colony
- cannibalism_country_origin_exploit_mutiny
- cannibalism_hidden_leader_seeded
- cannibalism_hidden_leader_revealed
- cannibalism_wendigo_fusion_active
- cannibalism_world_threat_active

State flags or variables:

- cannibal_state_pressure
- cannibal_state_pressure_type
- cannibal_state_responsible_country
- cannibal_state_hunting_ground
- cannibal_state_silent_island

## Event targets

Use short-lived event targets for immediate chains:

- cannibal_target_country
- cannibal_target_state
- cannibal_source_country
- cannibal_exposure_country
- cannibal_commune_state

Use global event targets only for persistent world-threat or hidden-leader-linked references that cannot be represented by flags or variables. If global event targets are used, every cleanup path must clear them.

Potential global targets:

- cannibal_primary_country
- cannibal_hidden_leader_actor, only after Evolution III reveal
- cannibal_wendigo_fusion_actor, only during alternate terminal branch

## Cleanup plan

Cleanup must run when:

- country contains outbreak
- country is annexed
- cannibal country is defeated
- target state changes owner
- selected island is evacuated or lost
- triggerable scenario setup finishes
- world-end branch starts
- event is disabled before an evolution records a milestone

Cleanup must remove:

- visible decisions and missions
- selected target flags
- temporary event targets
- stale state variables when state pressure is cleared
- response posture flags if the category closes
- AI strategy flags tied to invalid routes

Cleanup must not remove:

- global spread history while another country remains active
- achievement tracking flags
- hidden-leader resonance, seed strength, reveal flags, and Wendigo fusion flags when those values still affect later escalation or achievements
- aftermath flags needed for later leak or tribunal content

## Validation recommendations

- grep for duplicate Event 014 ids
- grep for remaining working labels in localisation after final text is written
- check every decision id has localisation
- check every focus id has icon and localisation
- check every scripted value has cleanup
- check every cannibal country formation path sets origin flag
- check no ordinary country receives the cannibal tree unless event-created
- check no final super-event quote or audio remains marked research required
- check no animated sprite points to a GIF path

## Hidden leader and Wendigo fusion helper needs

The scripted architecture should treat the hidden leader as part of Event 014. Evolution II seeds the hidden-leader values, Evolution III reveals and unifies when network strength is sufficient, and the Wendigo fusion branch checks whether the Wendigo country exists before terminal routing. Do not create a future-event dependency for this route.

Suggested helper concepts:

- seed hidden leader pressure from Evolution II commune, island, and exploitation outcomes
- calculate hidden-leader reveal readiness from cult nodes, cannibal countries, deaths, hunting grounds, and chaos
- unify cannibal actors into one country with absorbed armies and origin memory
- check Wendigo fusion eligibility
- apply Wendigo fusion package with portrait state, unit access, unit training unlock, inherited cannibal buffs, and terminal flagging

These helpers should use strong values for mature cannibal routes and terminal fusion. Do not tune the final route as a normal country.
