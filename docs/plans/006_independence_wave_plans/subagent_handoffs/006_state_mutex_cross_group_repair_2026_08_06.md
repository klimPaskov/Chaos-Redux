# Event 006 cross-group state mutex repair

Date: `2026-08-06`.

Scope: close the two accepted cross-reservation collisions without merging their reservation groups or broadening package dispositions.

## Source change

`common/scripted_triggers/006_independence_wave_packages_region_12_triggers.txt` now defines `is_independence_wave_region_12_state_441_mutex_open`. The helper requires state 441 to be absent from the current release reservation and rejects a plan that already contains IW-139 or IW-149. Both `can_plan_independence_wave_package_iw_139` and `can_plan_independence_wave_package_iw_149` call the helper before checking their country and anchor predicates.

The existing region-06 source already provides the equivalent `is_independence_wave_region_06_state_354_mutex_open` guard for IW-067 Lazistan and IW-068 Pontus. The two packages retain separate reservation groups and both use the state-level mutex before reservation.

This is a readiness gate only. It does not promote the Kashmir, Himalayan, Lazistan, or Pontus package, alter the accepted map, or change any formable identity.

## Evidence

- `hoi4.map_inspect` inspected states 354 and 441 in workspace `mod_chaos_redux_ea3b2d67c2c0`; artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/22350e865bda174a74f9629eaf14362e5be54202adf252190dbb55be9d6e647f/433a63038017441b6c2fa6515d823ebb7002d369bfacb55ad32e8e574ee9833f/map-inspect.cbfe0f707948ce8e.json`.
- `python -B .tools/audit_event6_allocator.py` passes the 23-attested / 22-group boundary, the doubled 6/8/10/14/20 ladder, the twenty-package static witness, and the joint reservation order.
- `python -B .tools/audit_event6_scenario_matrix.py` passes all 32 SCN-008 cells and eight edge cases.
- The source file has balanced braces and no whitespace errors in the scoped diff.

## Remaining boundary

The map inspection still reports unrelated global `map/buildings.txt` position and floating-harbor diagnostics. No map rewrite is justified by this trigger-only repair. Live release, save/load, and runtime reservation observation remain outside this handoff.
