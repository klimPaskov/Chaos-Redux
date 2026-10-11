# Event 021 native release footprint prototype (parked)

Disposition: unresolved, parked outside the loaded mod paths on 2026-10-11.
This folder holds the query and snapshot layer drafted for `event021_native_release_footprint_gap_2026-10-07.md` and the registered footprint addendum.
It is not loaded by the game, because it has no producer or consumer in the shipped Event 021 flow.

## What exists

- `script/006_independence_wave_event021_footprint_effects.txt` and `.md`: read-only carrier blueprint, native footprint and living-carrier lookup queries on the exact donor.
- `script/006_independence_wave_event021_footprint_constants.txt`: query status enums.
- `script/021_random_civil_war_registered_release_effects.txt`: the territory snapshot builder, the donor-remnant measurement and the territory validation.
- `tests/`: 18 fixture tests that execute those script bodies against declared maps. Run them from this folder with `python -m unittest test_event021_native_footprint_query test_event021_registered_release_snapshot`.

## Why it is parked

The snapshot builder reads inputs that nothing in the shipped flow publishes: `random_civil_war_release_authorized_states`, `random_civil_war_release_source_scope`, `random_civil_war_release_mutation_active` and `release_territory_contract_ready`.
No journal owns the frozen set through ownership change, rollback, actor registration and cleanup, and the front ledger arrays in `021_random_civil_war_dynamic_front_candidate_effects.txt` still record the anchor only.
Wiring it into the opening, active-review and frozen Maximum paths means changing the ledger contract and proving native `release`, living-carrier reuse and rollback in the engine, which the fixtures cannot do.

## To resume

Move `script/` files back to `common/scripted_effects/` and `common/script_constants/`, move `tests/` back to `.tools/` with the path constants restored, publish the authorized-state and source inputs from the Event 006 package publisher, and replace the anchor-only append in `event021_parent_append_dynamic_event6_front_candidate` with the complete transfer set.
The probability baseline for the intended change is in `../event021_registered_footprint_probability_2026-10-07/` and `../probability_snapshots/registered_footprint_before_2026-10-07/`.

## Player impact of the open gap

A native Event 006 release moves every source-owned core state of the registered carrier, while the Event 021 front ledger records the anchor.
The territory itself changes hands correctly.
The ledger undercounts the transferred region, so the donor remnant check and the front cleanup can disagree with the map for multi-state packages.
