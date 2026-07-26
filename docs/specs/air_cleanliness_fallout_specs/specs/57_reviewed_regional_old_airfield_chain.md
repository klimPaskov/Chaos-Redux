# Reviewed regional chain 57: The Old Airfield

## Status

This is an accepted Fallout-owned regional chain specification for the Latin America and Caribbean region. The chain remains dormant until the Fallout scheduler release audit authorizes ordinary issuance. It is a single-country domestic transaction and does not create a bilateral compact, aircraft unit, or recurring decision.

## Ownership and identity

The chain lives in `events/fallout_world_end_events.txt` under `add_namespace = chaosx.fallout`. Its candidate id is `586`, its transaction key is `710056`, its scheduler route is `7156`, its route upper bound is `7157`, and its Event Log history is `9162`. The human opening is `chaosx.fallout.586`. Hidden AI uses event `587`. Result events are `588` and `589`. Callback events are `590` and `591`. Cleanup is event `592`. No Zombie Apocalypse id, file, asset, audio, sprite, or path is reused.

## Place and admission

The chain belongs to `fallout_region.latin_america_caribbean` and uses the `regional_and_biome` family. It is a routine incident preferred during the `consolidation` phase with a secondary `rival_orders` phase. The country gate accepts campaign days 730 through 5999, a current Fallout identity and generation, current Fallout resources, no durable Old Airfield completion, no conflicting ordinary transaction, and at least one affordable branch with an eligible state. The admission gate rejects a country that cannot authenticate the current owner and controller.

The target selector scans owned and controlled states and keeps the lowest native state id. A valid state has the current Fallout identity, a produced Air Winter snapshot, current Supply Access, surviving population above 3000, at least one non-damaged air base, an air base total below the vanilla cap of 10, at least one non-damaged infrastructure level, Supply Access at least 18, Reclamation at least 8, Exposure below 75, Disease Pressure below 70, and no exclusive evacuation, natural-disaster, or other state transaction. The selector does not enumerate historical airports and does not fall back to a capital when no state qualifies.

## Meaning and four branches

The event concerns a weathered airfield that can reconnect a highland or tropical interior district to nearby survivor routes. The four choices have authored costs and different institutional memories.

| Branch | Exact opening cost | Intended institution |
| --- | --- | --- |
| Civil air service | Fuel 6, Scrap 5, Power 4, Recognition 2 | Public cargo, medicine, food, and passenger access |
| Military network | Fuel 8, Power 5, Command Power 15 | Air command, reconnaissance, and emergency lift |
| Private couriers | Fuel 4, Scrap 3, Recognition 1 | Cheap trade and intelligence with smuggling pressure |
| International consortium | Fuel 5, Scrap 4, Power 5, Recognition 6 | Standards and capital with external dependency risk |

The ordinary receipt validates the current country, target state, candidate target, selected branch, and affordability immediately before payment. The payment occurs once. If the receipt is stale, the target is lost, or the branch is no longer affordable, the exact ordinary row is cancelled and a cancellation memory is recorded without applying stored state effects.

## Persistent ledgers

The chain initializes and clamps these country ledgers to 0 through 100 without overwriting existing values.

- `fallout_old_airfield_route_reliability_current`, initial 40
- `fallout_old_airfield_flight_safety_current`, initial 40
- `fallout_old_airfield_trade_access_current`, initial 30
- `fallout_old_airfield_intelligence_reach_current`, initial 25
- `fallout_old_airfield_smuggling_pressure_current`, initial 10
- `fallout_old_airfield_external_dependency_current`, initial 0
- `fallout_old_airfield_military_control_current`, initial 0
- `fallout_old_airfield_public_access_current`, initial 35

The chain preserves the selected branch, result and callback grades, target route type, final quality, a terminal institutional flag, and the completion flag. Transient `fallout_event_586_*` values are cleared by authenticated cleanup.

## Deterministic result

The result resolves after 45 days. Its grade is the equal-weight mean of the air-base score, infrastructure score, Supply Access, Reclamation, Fuel, Power, Recognition, Cohesion, inverse Exposure, and inverse Disease Pressure. The grade is clamped to 0 through 100 before the branch threshold is read. There is no random list, MTTH roll, reroll, or post-payment regrade.

The branch thresholds are success and partial values. Civil air service uses 58 and 38. Military network uses 62 and 42. Private couriers uses 55 and 35. International consortium uses 60 and 40. Civil service gains 3 when Cohesion is at least 45. Military network gains 4 when War Support is at least 55. Private couriers gains 3 when Scrap is at least 25 and loses 4 when smuggling pressure is at least 50. International consortium gains 4 when Recognition is at least 40 and loses 4 when Power is below 25.

Every result applies the common state effects. Success adds Supply Access 6, Reclamation 4, lowers Exposure by 3, adds route reliability 10, adds flight safety 8, and instantly adds exactly one air-base level. Partial adds Supply Access 2, Reclamation 1, Exposure 1, route reliability 4, and flight safety 2 without adding a building level. Failure subtracts Supply Access 5 and Reclamation 3, adds Exposure 6, subtracts route reliability 8 and flight safety 10, damages one operational air base, and applies Deaths equal to 0.05 percent of the frozen state population. Failure checks for a non-damaged air base before damage and preserves the minimum population contract.

Civil success adds Trade Access 8, Public Access 12, Recognition 4, Cohesion 4, and Food 3. Partial adds 3, 5, 1, and 1 to the first four values. Failure subtracts Trade Access 4, Public Access 10, Recognition 4, and Cohesion 4. Military success adds Intelligence Reach 10, Military Control 12, War Support 0.03, and Supply Access 2. Partial adds Intelligence Reach 4, Military Control 5, War Support 0.01, and Cohesion minus 2. Failure subtracts Intelligence Reach 5, Military Control 8, War Support 0.02, and Cohesion 6. Courier success adds Trade Access 12, Intelligence Reach 6, Scrap 4, Recognition 2, and Smuggling Pressure 5. Partial adds Trade Access 5, Intelligence Reach 2, and Smuggling Pressure 10. Failure subtracts Trade Access 6, Intelligence Reach 3, Recognition 4, and adds Smuggling Pressure 18. Consortium success adds Trade Access 8, Intelligence Reach 8, Recognition 6, Power 2, and External Dependency 4. Partial adds Trade Access 4, Intelligence Reach 3, Recognition 2, and External Dependency 10. Failure subtracts Trade Access 5, Intelligence Reach 4, Recognition 5, adds External Dependency 18, and adds Smuggling Pressure 6.

Each branch applies one checked state modifier for its corridor identity. The modifier affects only documented air, supply, infrastructure, or control surfaces and is removed by its result or callback cleanup path.

## Callback and memory

The callback resolves after 270 days. It reauthenticates the current country, target, branch, result receipt, and Fallout generation. Its equal-weight score uses route reliability, flight safety, current Supply Access, Reclamation, Recognition, Trade Access or Military Control for the military branch, Intelligence Reach, inverse Exposure, inverse Smuggling Pressure, and inverse External Dependency. Success is at least 65. Partial is at least 42. Lower values fail.

Civil success ends with `fallout_old_airfield_aviation_compact`, partial with `fallout_old_airfield_local_air_service`, and failure with `fallout_old_airfield_grounded_public_route`. Military success ends with `fallout_old_airfield_air_command`, partial with `fallout_old_airfield_contested_air_command`, and failure with `fallout_old_airfield_garrison_route_failed`. Courier success ends with `fallout_old_airfield_licensed_courier_network`, partial with `fallout_old_airfield_courier_network`, and failure with `fallout_old_airfield_smuggling_network`. Consortium success ends with `fallout_old_airfield_aviation_compact`, partial with `fallout_old_airfield_dependent_consortium`, and failure with `fallout_old_airfield_consortium_collapse`.

Callback failure subtracts route reliability 5, flight safety 5, and Supply Access 3, adds Exposure 4, applies Deaths equal to 0.02 percent of the frozen state population, and may damage one operational air base after checking that one exists. Callback text and applied outcome use one authenticated outcome value. Target loss records a cancellation payload and never applies frozen state effects.

## AI and cleanup

Hidden AI uses the same four branches and affordability checks. Base priorities are civil 44, military 40, courier 34, and consortium 36. Unauthenticated or unaffordable choices receive minus 1000. Civil gains 14 for continuity, food, or religious governments, 10 when Cohesion is at least 50, and 8 when Food is below 30. Military gains 16 for warlord governments, 12 while at war, 8 when War Support is at least 55, and loses 12 when Cohesion is below 30. Courier gains 14 for scavenger or nomad governments, 8 when Fuel is below 25, and loses 16 when Smuggling Pressure is at least 60. Consortium gains 14 for technate or machine governments, 10 when Recognition is at least 40, 8 when Power is at least 35, and loses 14 when External Dependency is at least 50. Ties resolve in civil, consortium, military, courier order.

Cleanup releases result and callback rows exactly once, clears all transient variables and reservations, removes temporary branch modifiers, preserves the selected terminal memory, and clears the pending flags. It does not assign a new country, transfer territory, or create a partner relation.

## Presentation and proof boundary

The dedicated report card is `GFX_report_event_fallout_old_airfield_chain`. Its source and processed preview belong under `docs/assets/586_old_airfield_chain/`. The runtime DDS is `gfx/event_pictures/fallout_world_end/report_event_fallout_old_airfield_chain.dds` at the event report-card dimensions `210x176`. The image shows a repaired remote runway in a Latin American highland or tropical interior, an improvised radio mast, mechanics around a weathered transport aircraft, and mixed civilian and uniformed workers without modern markings or readable signage.

The chain is a reviewed ordinary candidate tranche, not release-floor credit while the scheduler is dormant. Static proof must cover event id uniqueness, candidate and route collisions, branch cost references, state target selection, delayed-row ownership, cleanup order, Event Log history 9162, localisation coverage, dynamic modifier fields, and the report-card dimensions. Runtime proof of delayed delivery, save recovery, multiplayer presentation, and AI frequency remains outside this no-HOI4 run.
