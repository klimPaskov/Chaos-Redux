# Event 016 native raid integration handoff

Date: 2026-08-03

## Scope

This tranche clarifies and wires Event 016's native raid surface without adding the separate KRG biological stockpile ledger. Existing native raid definitions remain the authority for payload reservation, collection, preparation, cancellation, expiry, outcome selection, and raid history.

## Implemented files

- `common/scripted_triggers/016_brilliant_scientist_raid_triggers.txt`
- `common/scripted_effects/016_brilliant_scientist_raid_effects.txt`
- `common/script_constants/016_brilliant_scientist_constants.txt`
- `common/raids/biological_raids.txt`
- `common/raids/biological_battlefield_raids.txt`
- `common/raids/biological_facility_recovery_raids.txt`
- `common/raids/zombie_weaponized_raids.txt`
- `common/raids/016_brilliant_scientist_portal_raids.txt`
- `common/raids/categories/chaosx_raid_categories.txt`
- `interface/chaosx_raids.gfx`
- `localisation/english/chaosx_raids_l_english.yml`
- `docs/events/016_brilliant_scientist/systems/kruger_state_decisions.md`
- `docs/specs/016_brilliant_scientist_specs/README.md`
- `docs/specs/016_brilliant_scientist_specs/package_manifest.md`
- `docs/plans/016_brilliant_scientist_plans/016_krg_biological_stockpile_delivery_addendum.md`

## Runtime behavior

1. Existing ordinary biological, battlefield, captured-facility recovery, hostile weaponized-zombie, friendly weaponized-zombie, and anti-zombie-cure raids remain manually usable whenever their native authority, policy, target, staging, aircraft or formation, and payload requirements pass.
2. A living active Kruger in the current host or active Kruger State multiplies the native AI willingness for those biological operations. It does not auto-launch, bypass authority, change outcome strength, or create a second payload ledger.
3. `brilliant_scientist_portal_warfare_tech`, granted at the teleportation weaponization stage, exposes the native `brilliant_scientist_portal_facility_raid` in `brilliant_scientist_raids`. It requires the existing teleportation weaponization history, the authenticated network, an owned Event 016 or KRG transit terminal, a Portal Raider battalion, the existing `kruger_portal_equipment` archetype, a supply-node starting point, and a hostile state containing a strategic facility.
4. Portal outcomes use native raid history plus persistent Event 016 actor and state markers. Limited, successful, and critical outcomes damage the highest-value surviving strategic facility; no models or new payload archetypes are introduced.

## Validation and risks

- Static schema review followed the offline raid documentation and vanilla land-infiltration precedents.
- The new land raid reuses `motorized_vehicle_entity`, the existing facility-raid map art, and the existing CBRN instrument equipment icon; no new 3D or 2D production was performed.
- Live game validation, AI frequency sweeps, target selection, and native parser acceptance remain user-owned and were not run.
- The separate KRG production/reservation/consumption/transfer/defeat ledger remains queued until the shared native CBRN callback contract exists. No fallback or parallel ledger was added.
