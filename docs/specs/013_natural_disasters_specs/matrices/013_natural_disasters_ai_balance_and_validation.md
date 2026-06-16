# Event 013 — AI, Balance, Helper, and Validation Matrix

## AI behavior goals

AI countries should respond to disasters in a way that preserves campaign plausibility without spending themselves into collapse. The AI should prioritise capital states, factory states, supply hubs, ports, and active war fronts. It should not burn scarce convoys or trains on low-impact states while losing a war, but it should not ignore repeated disasters entirely.

## AI disaster response priorities

| Actor type | High priority | Medium priority | Low priority / avoid |
| --- | --- | --- | --- |
| Player country AI equivalent | n/a | should receive clear player decisions | n/a |
| Major powers | factories, capital, ports, supply hubs, allies | refugee aid, foreign relief | repeated aid to distant enemies |
| Minor countries | capital and only-factory states | simple relief decisions | expensive regional aid abroad |
| Island nations | ports, convoys, coastal storms, tsunami | food imports | landlocked relief logic |
| Landlocked countries | rail, infrastructure, drought, earthquake | refugee hosting | port/convoy recovery |
| Countries at war | front supply, capital, factories, military industry | relief if stable | costly evacuation that ruins war effort |
| Low stability countries | actions that reduce panic | harsh order if authoritarian | stability-costly public policies |
| Authoritarian regimes | military engineers, coercive evacuation, propaganda | foreign aid if desperate | open refugee generosity unless ideology supports it |
| Democratic regimes | relief, shelters, international aid | rationing | harsh sealing decisions unless overwhelmed |
| Communist regimes | labour brigades, public works, grain offices | foreign aid to ideological allies | private-market disaster exploitation |
| Fascist regimes | militarised relief, forced labour, propaganda | evacuation if industry valuable | refugee acceptance except for subjects/allies |

## AI response weights by disaster family

| Family | AI priorities |
| --- | --- |
| Earthquake | engineer repair, rescue, rail repair, capital/factory states first |
| Flood | flood barriers before impact, railway repair after, refugee decisions if evolved |
| Storm surge | port closure before impact if safe, shoreline rescue after, convoy aid if overseas |
| Drought | feed dry belt, rationing, import food if convoys/trains available |
| Wildfire | firebreak mobilisation, shelter program, factory shutdown in rich states |
| Landslide | guard passes, rail repair, supply reconnection |
| Volcano | evacuation, ash cleanup, airbase closure/recovery |
| Tsunami | shoreline rescue, port recovery, refugee shelter |
| Meteor | crater survey, emergency shelters, panic control, engineer repair |

## Balance tuning principles

1. Baseline damage is local and recoverable.
2. Repeatability pressure comes from recurrence, not one giant early hit.
3. Evolutions increase affected area, chains, and burst count before they increase raw damage.
4. Resource costs should scale by country size and disaster severity.
5. Strong countries recover faster because they have resources, but repeated disasters can still strain them.
6. Weak countries should not be hard-locked out of recovery; they should receive cheaper partial relief options with weaker outcomes.
7. War state increases both vulnerability and opportunity cost.
8. High chaos permits spectacular events but must still name targets and produce playable aftermath.

## Suggested severity bands

These are design bands, not final constants.

| Severity | Use | Impact direction |
| --- | --- | --- |
| Local | baseline one-state disasters | small building damage, small population loss, short modifier |
| Serious | Evolution I burst or high-value state hit | noticeable buildings/supply/population, recovery recommended |
| Regional | Evolution II footprints | anchor heavy, secondary lighter, regional recovery decisions |
| Cascading | Evolution III chains | two-step aftermath with famine/refugee/supply/stability pressure |
| Abnormal | Evolution IV variants | several states or regions, stronger damage, super-event candidate |
| Scenario Maximum | manual scenario only | many disasters in short period, explicit test/challenge behavior |

## Helper architecture plan

The implementation should avoid copying damage and target logic in every disaster event. Use a small helper map.

| Helper concept | Scope | Inputs | Outputs / side effects |
| --- | --- | --- | --- |
| `select_natural_disaster_target_state` | root/global or controller | family, severity, avoid_recent, region mode | saves target state/event target and controller |
| `score_natural_disaster_target_state` | state | family, current chaos, vulnerability factors | target weight variable |
| `apply_natural_disaster_impact` | state | family, severity, warning_prepared, scenario flag | building/population damage, modifier, log variables |
| `queue_natural_disaster_burst` | global | evolution stage, intensity, scenario type | delayed events with family/target context |
| `record_natural_disaster_history` | global/country | family, severity, affected name, chain flag | event-log row variables and detail text |
| `open_natural_disaster_recovery` | country/state | family, severity, active aftermath | activates/hides relevant decisions |
| `clear_natural_disaster_state_context` | state/country | family/context id | removes flags, temporary variables, stale decisions |
| `natural_disaster_can_affect_country` | country trigger | none or family | validity and special-country exclusions |
| `natural_disaster_can_affect_state` | state trigger | family, severity | validity and vulnerability gating |
| `natural_disaster_update_recovery_pressure` | country | active aftermath count | category header values and national pressure |

## Script constants and tuning table plan

Use script constants for shared values where supported. Use local `@` constants only for duration fields that reject `constant:` tokens.

Recommended categories:

- `natural_disaster_weight`: family baseline weights and terrain multipliers;
- `natural_disaster_severity`: damage scale, population loss scale, modifier duration bands;
- `natural_disaster_burst`: min/max incidents by evolution and scenario intensity;
- `natural_disaster_recovery`: cost scaling, mission durations, recovery reductions;
- `natural_disaster_ai`: response weight multipliers;
- `natural_disaster_warning`: warning chances and mitigation scale;
- `natural_disaster_scenario`: manual scenario IDs, intensity stops, type IDs.

## Event target and cleanup plan

Use event targets for short chains. Global event targets should be avoided unless necessary for a multi-day delayed chain. If a global target is used, the helper must clear it.

Context to store for delayed chains:

- target state;
- target controller;
- disaster family;
- severity;
- source warning flag;
- scenario flag, if manual;
- chain parent id;
- affected region label id.

Cleanup should happen when:

- recovery mission succeeds or fails;
- state owner/controller changes and old decisions become invalid;
- disaster aftermath expires;
- country is annexed or no longer exists;
- manual scenario sequence completes;
- world-end state begins and normal random incidents are frozen.

## Exploit checks

| Risk | Prevention |
| --- | --- |
| Player farms recovery rewards | recovery should reduce penalties, not give repeatable net-positive factories/resources |
| AI spends all equipment on small disasters | AI thresholds and severity gating |
| Same state repeatedly destroyed | state/family cooldown and anti-repeat memory |
| Manual scenario permanently loosens caps | scenario flags scoped and cleared |
| Disaster aid used to farm relations infinitely | target/cooldown caps and no aid if no active disaster |
| Recovery decisions bypass occupation realities | require control/supply/port/route access where relevant |
| Instant full recovery trivialises high chaos | partial success and duration shortening instead of full removal for severe variants |
| Event 46 still fires separately | disable/placeholder Event 46 and update registration/catalog |

## Validation plan for implementation

Task-specific checks after implementation should include:

- Event 13 remains Minor Repeatable and logs Natural Disasters history rows.
- Cluster Natural Disasters contains only Event 13 unless user later expands the cluster.
- Baseline event can fire and identifies affected state/area in text.
- Each implemented disaster family has at least one impact event, aftermath modifier, and recovery path or documented reason it does not need one.
- Evolution I queues multiple delayed local incidents without multiplying event-system pacing count for each member if using cluster/burst wrappers.
- Evolution II can produce a regional footprint with anchor and secondary damage.
- Evolution III can produce at least one delayed aftermath chain.
- Evolution IV can produce meteor shower and abnormal earthquake wave variants.
- Event 46 Earth Earthquake is not still an active duplicate disaster event and is marked placeholder/unknown.
- Manual triggerable scenario launches at each intensity without requiring chaos tier or prior event history.
- Decision category hides when no active warning/aftermath/scenario context exists.
- Recovery decisions show clear missing resource text for trains, convoys, support equipment, fuel, supply, or unit presence.
- AI response has family-aware weights and avoids impossible targets.
- Event Details and spreadsheet details do not display raw mechanical effects.
- Super-event research gates are respected; no unresearched quote/audio/button text is pasted as final localisation.
- Asset manifest covers static and animated UI pieces, report/news/super-event images, icons, and achievement icons.

## Surfaces to audit with subagents

- `chaosx_scripted_system_architect`: helper map, constants, event targets, cleanup.
- `chaosx_decision_mission_auditor`: recovery category, costs, missions, AI, clutter.
- `chaosx_localisation_auditor`: event/detail text, dynamic state/region names, warning text, cost text.
- `chaosx_icon_artist`: decision/category/idea/achievement icons and animated warning icons.
- `chaosx_generated_event_art`: generated report/news/super-event fictional disaster art.
- `chaosx_asset_source_researcher`: historical/archival disaster images if sourced art is chosen.
- `chaosx_super_event_text_researcher`: final quote and cultural remark for Evolution IV super-event.
- `chaosx_super_event_audio_researcher`: licensed/public-domain audio for Evolution IV super-event.
- `chaosx_spreadsheet_doc_worker`: catalog row update after localisation is implemented.
- `chaosx_event_completion_auditor`: final spec-versus-implementation audit.
