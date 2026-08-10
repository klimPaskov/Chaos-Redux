# Event 016 native raid integration handoff

> Historical implementation note superseded by the 2026-08-09 documentation reconciliation: native Event 016 raids are the current architecture and are not blocked by the optional native CBRN callback. Portal Facility Raid now uses seven-day preparation, ten Command Power, sixty Teleportation Equipment, hostile-province seizure, fully supplied unit spawn, and eligible building transfer; the separate KRG stockpile and delivery ledger remains queued. See `docs/events/016_brilliant_scientist/systems/portal_raider_api.md` and `docs/plans/016_brilliant_scientist_plans/016_portal_plague_documentation_reconciliation_2026-08-09.md` for current status.

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

1. Existing ordinary biological, battlefield, captured-facility recovery, hostile weaponized-zombie, friendly weaponized-zombie, and anti-zombie-cure raids remain manually usable whenever their native policy, target, staging, aircraft or formation, and payload requirements pass.
2. A living active Kruger in the current host or active Kruger State bypasses the separate Event 016 authority board and multiplies native AI willingness for those biological operations. It does not auto-launch, change outcome strength, or create a second payload ledger.
3. `brilliant_scientist_portal_warfare_weaponization_tech` exposes the native `brilliant_scientist_portal_facility_raid` in `brilliant_scientist_raids`. Active Kruger, the existing locked `Quantum Transit Raiders` template, one `kruger_portal_equipment` charge, a supply-node starting point, and a hostile state containing a factory or strategic facility are enough; the former separate network, terminal, and authority steps are not required.
4. Limited outcomes damage the target facility. Successful outcomes additionally set the target province controller to the raider country, create a `Portal Breach Cadre` with the existing `Quantum Transit Raiders` template in that province, and extract one factory level into the raider country's off-map industry. Critical outcomes call extraction twice, so up to two factory levels can be removed when the target has enough factories. No models or new payload archetypes are introduced.

## Validation and risks

- Static schema review followed the offline raid documentation and vanilla land-infiltration precedents.
- The new land raid reuses `motorized_vehicle_entity`, the existing facility-raid map art, and the existing CBRN instrument equipment icon; no new 3D or 2D production was performed.
- Live game validation, AI frequency sweeps, target selection, and native parser acceptance remain user-owned and were not run.
- The separate KRG production/reservation/consumption/transfer/defeat ledger remains queued until the shared native CBRN callback contract exists. No fallback or parallel ledger was added.
