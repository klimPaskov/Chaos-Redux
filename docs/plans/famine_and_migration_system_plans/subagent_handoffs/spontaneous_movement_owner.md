# Spontaneous movement owner handoff

> **Superseded historical identifier banner (2026-08-25):** Any `fm_*` or `famine_migration_*` identifier quoted in this historical handoff is source-snapshot terminology only and is superseded; current authorities use separate `famine_*`, `migration_*`, or narrow neutral `civilian_transfer_*`/`humanitarian_*` names; see [source_of_truth_map.md](../source_of_truth_map.md).

Date: 2026-08-24

Owner: `chaosx_scripted_system_architect`

## Changed files

- `common/script_constants/famine_migration_spontaneous_movement_constants.txt`
- `common/scripted_triggers/famine_migration_spontaneous_movement_triggers.txt`
- `common/scripted_effects/famine_migration_spontaneous_movement_effects.txt`
- `common/scripted_effects/famine_migration_spontaneous_movement_effects.md`
- `common/scripted_effects/famine_migration_destination_selection_effects.txt`
- `common/scripted_triggers/famine_migration_destination_selection_triggers.txt`
- `common/scripted_effects/chaosx_famine_migration_effects.txt`
- `common/scripted_effects/chaosx_dynamic_effects.md`

The shared-file changes in this ownership slice are the registered-state owner and cleanup calls, the two stable public wrapper delegates, the destination selector’s chain-local actor binding, and their matching documentation. Concurrent shared-file edits were preserved, including the live displacement-country phase block.

## Helper map and call sites

`famine_migration_process_spontaneous_movement_owner` is called only from `famine_migration_process_registered_displacement_state`. `famine_migration_spontaneous_movement_state_is_ready` gates a valid human state with material flight pressure, live population, active displacement, and an expired persisted cooldown. `famine_migration_spontaneous_movement_calculate_request` derives a dynamic people request. `famine_migration_spontaneous_movement_submit_request` is the pressure-only adapter called by `famine_migration_request_internal_displacement` and `famine_migration_request_cross_border_flight`. `famine_migration_spontaneous_movement_trap_request` adds only a positive missing trapped delta after a zero selector pool. `famine_migration_spontaneous_movement_cleanup_destination_proofs` clears the selector's normal destination food and reception proofs through the current route target on every owner exit. `famine_migration_cleanup_spontaneous_movement_state` is called from the registered-state retirement branch. The destination selector's `famine_migration_destination_selection_bind_actor` refreshes the actor from ROOT for ordinary decision callers while preserving the spontaneous owner's explicit origin-owner target.

## Formula and conservation proof

The owner computes:

```text
live_population = state_population_k * constant:chaos_meter_deaths.people_per_k
protected_floor = round(live_population * protected_origin_share)
movable_population = max(live_population - protected_floor, 0)
requested = round(flight_pressure * request_pressure_share)
requested = clamp(requested, effective_minimum, movable_population)
```

The first clamp applies `maximum_request_people`. `effective_minimum` is the normal minimum request unless the live movable pool is smaller. There are no historical totals or fixed per-state movement amounts.

On a valid route the owner enters the saved origin state scope, sets the route-death request to zero, and invokes `famine_migration_transfer_civilians_exact` exactly once. This preserves the existing resolver’s `PREV` adjacency proof contract. That shared endpoint performs the sole population debit, measures `actual_origin_debit`, credits the destination, and returns `survivor_credit`. The owner records a cohort only after `transfer_result = valid` and positive `survivor_credit`, using exactly that survivor credit. The destination is then bound from the actual route target and the same credit is applied once to state and country reception load. The exact transfer’s conservation condition is:

```text
actual_origin_debit = route_deaths + survivor_credit
```

The spontaneous safe-route request supplies `route_deaths = 0`, so ordinary movement is not a death transaction. Origin flight pressure is reduced by measured debit, not requested amount. If no destination exists, only `max(requested - existing_trapped_population, 0)` is registered and the origin population remains unchanged.

Cause classification compares the selected destination owner with the saved origin owner. Equal owners use `internal_displacement`; foreign owners use `cross_border_flight`. The selector receives the saved origin owner through `famine_migration_destination_selection_actor`, avoiding the global-host ROOT scope used by the sparse registry caller.

## Idempotence and bounded scheduling

The owner runs from the existing active displacement-state array only. It never scans all states or countries; the destination selector’s existing `every_neighbor_state` passes remain the only route enumeration. Before a route draw, the state stores `famine_migration_spontaneous_movement_last_date` and `famine_migration_spontaneous_movement_cooldown_until_date`. Same-date calls and save/reload retries therefore fail the ready trigger. Zero-pool retries do not duplicate trapped population because only the positive delta to the current request is added. A successful route reduces flight pressure by measured debit and can retire the active displacement entry only when both flight and trapped ledgers are empty.

Regular event targets `famine_migration_transfer_origin`, `famine_migration_spontaneous_origin_owner`, `famine_migration_destination_selection_actor`, and `famine_migration_route_destination` are chain-local. The destination selector refreshes the actor from ROOT whenever the temporary override guard is absent, preventing stale actor reuse across registry iterations. The owner clears `famine_migration_destination_food_safe_proven` and `famine_migration_destination_reception_proven` on the route destination after every terminal path, including valid reception, no-selection/trapped, invalid destination, and failed exact-transfer paths. No global event target was introduced.

## Required probability evidence

The first mandatory `hoi4.probability_inspect` was run before helper design against `common/scripted_effects/famine_migration_destination_selection_effects.txt` for `internal_safe_route`, `foreign_safe_evacuation`, `foreign_transit`, and `third_country_resettlement`. The MCP result was `PROBABILITY_SOURCE_INSPECTED` with `poolComplete=false`, zero extracted candidates, four unresolved identifiers, source revision `47e9cc152877ad553d909cd7c697f4c51ad5549696e858c88c2ff4fac740c091`, source hash `95d51b3eb64a3c55856b7fbcb6b1a1738abeca238a5ecf8dd29ab12a908a9659`, and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/69571e697b325d2a61c47efacb885a8513a0052b0a1484d104db25164c372b1c/773a4c86decd3db29f68498d200aa2491b7f29f6dacbd75ed7d5945d11622d7d/probability-inspect-95d51b3eb64a3c55856b7fbcb6b1a1738abeca238a5ecf8dd29ab12a908a9659`.

The named `chaosx_ai_probability_auditor` is not available in the current tool registry. Consequently, baseline, owner-patch, compare, sweep, sequence, and rendered evidence for `prob_disaster_flight`, `prob_bombing_exodus`, `prob_destination_selection_internal`, `prob_destination_selection_persecution`, and `prob_cleanup` remain blocked. The direct MCP inspection is recorded as source evidence only and is not substituted for the auditor route.

A narrow `hoi4.map_inspect` query for state adjacency returned `MAP_INSPECTED` with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f84ceb339145a7a8cfe45159b92efbee38e2e0a7aaee1480abfc22af84d662c6/6c2aff44a910117f6421f440c4cf66d49261b72cc3879d2b642d2c3320f05fbf/map-inspect.bbb909a0a4fdd2d4.json`. It matched no static state because the owner consumes a dynamic registry entry; adjacency/network checks passed. The artifact reports existing map-position/port diagnostics and truncated broad diagnostics, so it is route-system evidence rather than a clean repository-wide map validation.

After the actor-override patch, the current SHA-256 hashes are `FD62688AEDF546986851FFC2ED955C41D594C0D2626A09C4930EDB7A66EFC55C` for the destination-selection effects and `14FCBD0B2C607D5EB50B2912E65680331B7139A2E55EA7E1B750571583A001E5` for the destination-selection triggers. The probability artifact above reflects the pre-override effects hash and is not post-patch engine evidence.

## Bounded proof-cleanup follow-up

The selector's destination candidate branch persists `famine_migration_destination_food_safe_proven` and `famine_migration_destination_reception_proven` on the destination state as normal variables. Existing decision and corridor owners clear them, but the spontaneous owner previously had no terminal cleanup after a selector attempt. The local cleanup helper now runs unconditionally after the spontaneous owner body and clears both variables through `event_target:famine_migration_route_destination` when that target exists. It performs no population, movement, death, pressure, reception, or AI arithmetic and does not add a scan or recurring hook. Because the helper is idempotent and missing targets are a no-op, it covers valid success, trapped/closed route, no selection, invalid destination, failed transfer, and early retry exits without changing the existing transaction contract.

The proof census found selector production at `common/scripted_effects/famine_migration_destination_selection_effects.txt:338-339`, exact-validation consumption through `famine_migration_destination_is_valid`, and existing ordinary-owner cleanup in decisions/corridors. This patch adds the spontaneous owner consumer cleanup without touching those shared producers or other owners.

The normal proof variables do not carry a durable destination-state id, so an old save cannot be repaired safely by guessing or by scanning states. The existing registered-state processor already reaches the owner; each later selector binding overwrites the current destination proofs and the terminal cleanup clears them. No extra recurring hook or whole-world cleanup is necessary or permitted.

## Validation and follow-up

Read-only checks confirmed balanced braces after adding the local cleanup helper, exactly one owner cleanup call, and two clear operations inside the helper. Source inspection retained one `famine_migration_transfer_civilians_exact` call in the spontaneous owner and no pre-transfer `famine_migration_record_displaced_cohort` call in the internal or cross-border public wrappers. No weighted candidate or AI formula changed, so no new probability MCP evaluation was applicable; the earlier required probability artifact remains source evidence only and the unavailable auditor blocker remains unchanged. No decision, localisation, event, asset, mapmode, or GUI files were changed by this follow-up.
