# Event 006 collision-gate specification reconciliation

Date: 2026-08-14.

## Scope

This documentation-only reconciliation updates the core specification's dated collision paragraph. It does not change gameplay, package admission, reservation groups, map ownership, assets, localisation, or Join order.

## Source evidence

The live region-06 planner contract in `common/scripted_triggers/006_independence_wave_packages_region_06_triggers.txt` rejects the state-354 Trabzon mutex when the competing Lazistan or Pontus package is already reserved. The live region-12 planner contract in `common/scripted_triggers/006_independence_wave_packages_region_12_triggers.txt` applies the equivalent state-441 Kashmir/Himalayan mutex. The package groups remain distinct and both contracts fail closed.

## Documentation change

`docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_1_core.md` now labels its older “two cross-group findings remain unresolved implementation gates” sentence as a dated design snapshot and points current readers to the implemented state-354 and state-441 mutexes. The paragraph explicitly preserves the no-merge and no-broader-map-grant constraints.

## Authority and disposition

Current Event 006 authority is unchanged at 40 runtime adapters, 32 content-attested packages, 29 compatible reservation groups, and 161 unattested selectable rows. The whole event remains HOLD / PARTIAL. This reconciliation does not authorize central admission, a new package, a map rewrite, or a compatibility-adapter promotion.

## Validation

The edited paragraph was checked against the two named trigger files, and `git diff --check` was run on the spec and this handoff. Existing concurrent count edits in the core spec were preserved and are intentionally not included in this handoff's scope.
