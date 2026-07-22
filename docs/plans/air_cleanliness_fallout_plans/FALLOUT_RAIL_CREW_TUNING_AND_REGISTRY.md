# Fallout Rail Crew Twenty-Seven Tuning and Registry Contract

## Scope

This document records the dormant Rail Crew Twenty-Seven survival pilot. It is a global-survival event family under `add_namespace = chaosx.fallout`. The pilot is not an activation approval and it is not included in the release-floor event-block count.

The opening uses one exact ordinary Fallout receipt. Its target must be a state owned by the receiving country. The state must retain a current Fallout survival identity row, a durable resource row, a produced Air Winter snapshot, and a native railway surface. The state must be in Air Winter phase 3 or later and must not already carry the rail registry flag.

## Registry contract

The opening copies the state target into the country registry and records `fallout_event_114_corridor_state_id`, `fallout_event_114_rail_registry_generation`, and `fallout_event_114_rail_registry_owner`. The state stores `fallout_event_114_registry_generation`, `fallout_event_114_registry_owner`, and `fallout_event_114_rail_registry_committed`.

Every delayed result and cleanup trigger rechecks the generation, owner, state flag, state identity row, durable resource row, state owner, water-independent Air Winter snapshot, and produced source kind. The result and callback effects run only after their exact delayed receipt has been terminalized. The result cleanup receipt releases its own row and keeps the corridor registry alive until the callback is resolved. Final cleanup clears the registry after both rows are released, or after callback scheduling fails. Durable rail memories remain after cleanup.

The rail value is read from the native state `rail_way` field. A state without a live railway level is rejected by the opening contract, so the pilot never substitutes a supply node, infrastructure value, or variable-only corridor.

## Tuning tables

The contract is centralized in `common/script_constants/fallout_world_end_event_constants.txt`.

- Result delay is 3 days.
- Callback delay is 7 days.
- Corridor modifiers last 120 days.
- Heroic crew memory lasts 240 days.
- Atrocity memory lasts 180 days.
- Fragmented route memory lasts 300 days.
- The four branches are send protected crews, use forced labor, abandon the line, and request neighbor access.
- Protected-crew success requires fuel 40, scrap 35, and rail 3. Its partial band requires fuel 20 and rail 1.
- Forced-labor success requires fuel 40, scrap 18, and rail 1. Its partial band requires fuel 20 and rail 1.
- Abandonment succeeds when rail is at least 1 and either fuel or scrap is below its partial threshold. A rail 1 state without that shortage is partial.
- Neighbor access succeeds with power 35, recognition 35, and rail 1. A rail 1 state without those diplomatic and grid inputs is partial.
- Failure mortality requests the branch-specific share of current state population through `apply_exact_state_civilian_population_loss` with the Fallout aftermath Deaths reason. The minimum remaining population guard is 100 people.
- Result and callback values change fuel, scrap, power, recognition, stability, cohesion, war support, state reclamation, trains, support equipment, infantry equipment, and native rail damage. The shared resource clamp runs after every result and callback.

The branch token upper bound is 5. Hidden AI result tokens use event IDs 1014 through 1017. The hidden AI callback uses event ID 1018. These IDs do not collide with the NZL package, food pilot, or water pilot.

## Branch effects

Protected crews spend fuel and scrap to restore rail capacity, trains, and repair equipment. A success adds a protected-corridor modifier and durable crew memory. A partial result restores a narrower route. A failure damages the native rail surface, records deaths, and adds route fragmentation.

Forced labor produces the largest immediate transport return when its resource floor is met. It also reduces cohesion and war support, and its callback retains a durable atrocity memory. Failure damages the line and uses the Deaths system.

Abandonment spends fewer stores and clears the corridor control variable. A successful withdrawal preserves a smaller reclamation reserve. A partial withdrawal leaves the line out of service. A failed withdrawal damages the native transport surface and records deaths.

Neighbor access is intentionally a country and state pilot. It records shared or local access, recognition, trains, support equipment, and a neighbor-access modifier. It does not yet select a live bilateral partner country, validate a partner-owned target, or write a diplomatic relation. That missing bilateral registry is a known simplification and keeps this branch uncounted.

The callback turns a successful result into a named crew institution, a forced-labor result into an atrocity memory, or any failed continuation into a fragmented route. The event log records all twelve branch outcomes and three callback outcomes through history `9107`.

## Files and wiring

- `common/scripted_triggers/fallout_world_end_rail_event_triggers.txt` owns target and registry authentication.
- `common/scripted_effects/fallout_world_end_rail_event_effects.txt` owns scoring, result effects, Deaths calls, native rail damage, history payloads, callback scheduling, and cleanup.
- `common/dynamic_modifiers/fallout_world_end_rail_security_dynamic_modifiers.txt` owns state and country consequence modifiers.
- `events/fallout_world_end_events.txt` owns human, hidden AI, delayed result, callback, and cleanup event blocks.
- `localisation/english/fallout_world_end_l_english.yml` owns concrete text for the four choices, three outcome bands for each branch, callback outcomes, modifiers, and event-log payloads.
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt` maps history `9107` and its fifteen payloads.
- `FALLOUT_EVENT_ID_LEDGER.md` records IDs `114` through `120`, `122`, and hidden AI IDs `1014` through `1018`.

The dedicated event image `GFX_report_event_fallout_rail_crew_twenty_seven` is bound to the opening and all human result and callback surfaces. No zombie asset, file, path, audio, or sprite is used.

## Static proof completed

- The rail effect, trigger, event, modifier, event-log, and localisation blocks are brace-balanced after implementation.
- The Fallout event namespace has no duplicate event IDs after allocating hidden rail companions at 1014 through 1018.
- The localisation file retains UTF-8 with BOM.
- All new event, modifier, history, payload, and scripted-localisation keys are present in the touched localisation surfaces.
- The rail chain contains no scheduler activation flag, active scheduler flag, or caller.
- The rail chain contains no zombie reference.
- Human and hidden AI result rows share one result and callback effect path.
- The neighbor-access branch is explicitly documented as a country and state pilot rather than a complete bilateral diplomacy chain.

## Runtime proof still required

HOI4 was not launched by request. Static inspection cannot prove that the numeric state value in `var:` scope remains a live state target at every delayed boundary. It cannot prove native `rail_way` reads, native `damage_building` placement, delayed receipt retention across save and reload, multiplayer owner checks, event ordering, dynamic modifier placement, Deaths callback accounting, event-log rendering, or scheduler performance.

The event caller and exact Fallout-owned scheduler activation are absent. Until those are reviewed and wired, this chain must remain dormant. Activation review must also replace the country and state neighbor-access pilot with a live bilateral partner registry or reject the branch as a local access result.

## Release accounting

This pilot adds no release-floor blocks. It is a typed implementation tranche for the global-survival library. The release floor remains 660 manually reviewed event blocks. Expansion toward 910 remains gated on review depth, scheduler activation proof, and the unresolved engine-sensitive surfaces above.
