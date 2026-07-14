# Event 006 package registry handoff: Regions 12–14

## Scope and ownership

This tranche implements the accepted current-map allocator package registry for `IW-133` through `IW-206`, limited to Regions 12–14. It adds package readiness triggers, metadata loaders, automatic weight publishers, reservation publishers, and regional selectors. It does not edit the shared allocator, planner, execution, constants, tag, country, asset, or localisation files.

The offline wiki core pages, official vanilla script documentation, the vanilla `POL_remove_danzig_effect` event-target precedent, the vanilla `BUL_get_random_bulgarian_destination_royal_visit` weighted-list precedent, the accepted Event 006 specs, the current installed-map binding audit, and the existing Region 01–11 package registries were consulted before implementation.

## Files added

- `common/scripted_triggers/006_independence_wave_packages_region_12_triggers.txt`
- `common/scripted_effects/006_independence_wave_packages_region_12_effects.txt`
- `common/scripted_triggers/006_independence_wave_packages_region_13_triggers.txt`
- `common/scripted_effects/006_independence_wave_packages_region_13_effects.txt`
- `common/scripted_triggers/006_independence_wave_packages_region_14_triggers.txt`
- `common/scripted_effects/006_independence_wave_packages_region_14_effects.txt`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_packages_regions_12_14_handoff.md`

## Exact package coverage

| Region | Bound rows | Automatic rows | High-chaos subset | Explicit-only rows | Omitted rows |
|---|---|---|---|---|---|
| 12 — South Asia and Himalaya | `133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 147, 148, 149` | `134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 145, 147, 148` | `135` | Routes `133, 144, 149` | `146` |
| 13 — Southeast Asia, East Asia, and Oceania | `150, 151, 152, 154, 155, 156, 158, 159, 161, 162, 164, 166, 167, 169, 170, 171, 172, 173, 175, 177, 179` | `150, 151, 152, 154, 155, 156, 158, 159, 161, 162, 164, 166, 167, 169, 170, 171, 173, 175, 177, 179` | `150, 151, 156, 161, 166, 167, 169, 171` | Specific community `172` | `153, 157, 160, 163, 165, 168, 174, 176, 178` |
| 14 — Americas and Caribbean | `180, 182, 183, 184, 185, 192, 193, 196, 197, 198, 200, 201, 203, 204` | `180, 182, 184, 185, 192, 197, 198, 200, 201, 203, 204` | `197, 198, 200, 201, 203, 204` | Routes `183, 196`; specific community `193` | `181, 186, 187, 188, 189, 190, 191, 194, 195, 199, 202, 205, 206` |

Totals: 51 bound rows, 44 automatic rows, 15 high-chaos rows, seven explicit-only rows, and 23 omitted rows. Omitted rows have no trigger, loader, weight, reservation, or selector reference. No substitute package or fallback anchor was introduced.

## Identifier contract

Every bound row has all three callable package identifiers:

- `can_plan_independence_wave_package_iw_NNN`
- `independence_wave_load_package_iw_NNN`
- `independence_wave_reserve_package_iw_NNN`

Every automatic row, and only an automatic row, additionally has `independence_wave_prepare_weight_iw_NNN` and appears in its region's automatic aggregate and `random_list` selector. The explicit route/specific-community rows have no weight or selector entry.

Regional entry points are:

- `independence_wave_prepare_region_12_automatic_weights`
- `independence_wave_select_region_12_automatic_package`
- `independence_wave_prepare_region_13_automatic_weights`
- `independence_wave_select_region_13_automatic_package`
- `independence_wave_prepare_region_14_automatic_weights`
- `independence_wave_select_region_14_automatic_package`

The implementation consumes only existing shared helpers: plan-open and slot predicates, tag and anchor availability, the high-chaos predicate, allocation-weight calculation, reservation begin/finish, anchor reservation, and compact/extended state attempts. It uses regular event targets `liberation_candidate_country`, `liberation_candidate_anchor`, and `liberation_candidate_primary_host`.

## Binding and reservation behavior

- Fixed multi-state bindings use the first accepted state as the unique coordinator anchor. Remaining compact states are published through `independence_wave_try_candidate_compact_state`; extended states use `independence_wave_try_candidate_extended_state`.
- Ordered alternative anchors are implemented for `IW-134` (`440`, then `986`), `IW-200` (`301`, then `688`), and `IW-203` (`512`, then `507`). Readiness accepts either currently safe alternative, the loader selects the first available alternative in accepted order, and reservation uses `event_target:liberation_candidate_anchor`.
- Host survival, protected-capital rejection, state reservation collisions, tag living/provenance collisions, and optional-state trimming remain centralized in the existing shared predicates and reservation lifecycle.
- Reservation groups exactly match the accepted installed-map binding CSV. Packages sharing a group cannot be selected together in one plan.

Manual archetype assignment was derived from each accepted opening archetype, force profile, and geographic binding, using only the existing archetype constants:

- `urban_administrative`: `140`
- `industrial_breakaway`: `180, 183, 184`
- `agrarian_regional`: `134, 135, 141, 143, 144, 185, 192, 200`
- `port_or_island`: `142, 150, 152, 154, 155, 156, 158, 164, 167, 171, 173, 175, 177, 179, 182, 196`
- `mountain_or_frontier`: `137, 138, 139, 147, 148, 149, 151, 159, 162, 169, 193, 197, 198, 201, 203, 204`
- `river_or_corridor`: `133, 136, 145, 161, 166`
- `nomadic_or_dispersed`: `170, 172`

## Tag registration handoff

All 19 reused tags were found in the installed vanilla/mod country-tag registries:

`BLC, FIJ, FSM, GAR, HAW, HYD, KAS, KHL, LAO, MEN, MPU, MYS, PSH, QUE, RAS, SAM, SIN, SKK, YUC`.

The following 32 accepted new tags were collision-free when this bounded tranche was produced, all end in `X`, and were subsequently registered by the parent integration:

- Region 12: `FCX, FDX, FLX, FNX, FOX, FSX`
- Region 13: `FTX, FUX, FVX, FXX, FYX, FZX, GBX, GCX, GEX, GFX, GHX, GKX, GMX, GOX, GPX`
- Region 14: `GZX, HAX, HBX, HCX, HKX, HNX, HOX, HPX, HSX, HUX, HVX`

The shared candidate-tag predicate was verified to reject living tags, already reserved tags, Soviet-collapse active/origin tags, and Independence Wave active-origin tags.

## Validation evidence

- Cross-checked the three registries against all `IW-133`–`IW-206` rows in `006_current_installed_map_package_bindings.csv`: 51/51 accepted bindings have readiness/load/reservation identifiers; the automatic set is exactly 44/44; the high-chaos gates are exactly 15/15; the seven explicit-only bindings are absent from automatic weights/selectors; all 23 unbound rows have zero references.
- Cross-checked reservation groups, tag tokens, tag-registration metadata, dispositions, depths, regions, ordered anchors, unique anchor roles, compact roles, and extended roles package by package against the accepted binding and candidate CSVs.
- Verified all 75 referenced state IDs exist in the installed vanilla plus mod state history.
- Verified all 19 reused tags were registered and all 32 new tags were collision-free before their parent-owned registration.
- Verified all 11 shared helper identifiers resolve to existing definitions and the package identifiers introduced here are unique.
- Verified selector membership equals weight membership in each region, all six files have balanced blocks, and no unsupported comparison operators or space-indented script lines were introduced.

## Risks and integration notes

- The 32 new tags are registered. Full researched country content, leaders, assets, and package-content readiness flags remain required before their packages can enter a live Event 006 pool.
- `IW-139` and route-only `IW-149` overlap state `441` across different reservation groups. The shared state reservation predicate prevents simultaneous planning; any later route caller must continue to invoke the package readiness trigger before reservation.
- `IW-169` state `617`, `IW-198` state `302`, and `IW-201` state `306` are rejected while they are protected host capitals. This is intentional accepted behavior, not a missing fallback.
- On the installed 1936 map, `IW-200` normally skips protected-capital state `301` and uses state `688`; if world state later makes `301` safe, the accepted ordered selection permits it.
- Same-state collisions (`425`, `427`, `982`, `986`, and `950`) are contained by accepted reservation groups and the shared reserved-state predicate.

## Simplifications, omissions, and blockers

No simplifications or fallback bindings were used. The only omitted packages are the 23 rows explicitly marked unbound or disabled by the accepted installed-map audit. Registration is resolved; full country-package integration remains parent-owned work, not a substitution in this tranche.

No commit was created, as requested by the parent task.
