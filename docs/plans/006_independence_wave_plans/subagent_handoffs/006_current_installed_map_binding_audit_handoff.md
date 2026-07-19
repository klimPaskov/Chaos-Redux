# Event 006 current-installed-map binding audit handoff

> **Historical all-row ledger note.** The `149` bound / `57` unbound figures in
> this handoff are the original 2026-07-14 all-row map result, retained for
> traceability. Current selection uses the binding CSV's `138` bound / `55`
> unbound selectable rows plus `13` overlay rows. Use
> `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv`
> for identity and
> `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv`
> for current package bindings.

## Scope completed

Audited all 206 accepted Event 006 candidate packages against the currently installed 1–1081 Hearts of Iron IV state map. Resolved authoritative anchor, compact, and extended bindings where the accepted package definition and current map support them; left packages unbound where a unique current state or required named package does not exist.

This tranche is documentation-only. No gameplay, specification, localisation, workbook, or asset file was edited.

## Files produced

- `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv`
  - 206 package rows;
  - exact IDs and names by anchor/compact/extended level;
  - binding mode and readiness verdict;
  - public-baseline comparison and rebind status;
  - initial owner/capital evidence;
  - host-survival implication, binding reason, and source evidence.
- `docs/plans/006_independence_wave_plans/package_bindings/006_current_map_state_collisions.csv`
  - all 14 state overlaps;
  - same-group versus cross-group classification;
  - automatic claimants and required resolution.
- `docs/plans/006_independence_wave_plans/package_bindings/006_current_map_reservation_groups.csv`
  - all 111 reservation groups;
  - all 206 packages covered exactly once;
  - bound/unbound membership, current claims, and cross-group collision IDs.
- `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_binding_audit.md`
  - method, map authority, direct rebindings, disables, collisions, host-survival findings, and implementation gates.

## Historical principal findings (original all-row ledger)

- Bound: 149 packages.
- Unbound: 57 packages.
- Automatic/high-chaos packages disabled for no unique current state: 29.
- Specific-community packages deliberately unbound: 26.
- Scenario packages unbound: 2.
- Distinct installed states referenced: 205.
- Direct public-baseline-to-current rebindings: 26.
- New exact bindings for packages with no public-baseline state: 22.

The accepted nonautomatic restrictions were preserved. The four exact specific-community bindings are IW-055 on 825, IW-091 on 775, IW-172 on 536, and IW-193 on 476; none was promoted into the automatic pool.

## Collision gates and resolution

1. **State 354 Trabzon:** IW-067 Lazistan and IW-068 Pontus use different reservation groups but the same anchor. The implemented Region 06 readiness layer adds an explicit state-354 mutex in addition to shared state reservation.
2. **State 441 Kashmir:** automatic IW-139 Kashmir and route-only IW-149 Himalayan confederation cross reservation-group boundaries. Both implemented readiness triggers reject a state already reserved by the shared transaction.

The other 12 collision rows are within accepted reservation groups and are safe only if the maximum-one rule is enforced. Extended claims must trim before compact or anchor claims.

## Host-survival gates

The installed-history snapshot identifies protected-capital or host-erasure concerns for IW-005, IW-012, IW-059, IW-074, IW-081, IW-082, IW-114, IW-169, IW-198, IW-200, and IW-201. The CSV contains the owner/capital evidence and per-package implication.

Initial history is diagnostic only. Implementation must recalculate current owner, current capital, and remaining owned states at selection time, reserve the protected state first, trim extended then compact territory, and reject any anchor that would eliminate its host.

## Simplifications, omissions, and blockers

- No fallback or generic state binding was used.
- The 57 unbound packages are intentional blockers, not approximations. They must remain unavailable until an accepted design update or a future current-map state supplies exact geography.
- The optional HOI4 map inspection tool could not build its model: `MAP_MODEL_BUDGET_BLOCKED` reported 500,208 records against a 500,000 ceiling. No conclusion relies on that tool. Installed vanilla state histories, state-name localisation, country histories, tag cores, and victory-point locations are the audit authority.
- The audit originally recorded two cross-group conflicts. The runtime package registry resolves both without changing the accepted binding data.

## Validation evidence

- 206 unique IDs, exactly IW-001 through IW-206.
- 149 bound and 57 unbound rows.
- All 205 referenced state IDs exist in the installed 1,081 state files.
- No bound row lacks an anchor or compact set.
- Every anchor is included in its compact set.
- No compact/extended overlap.
- 111 reservation groups cover all 206 packages exactly once.
- The 14 collision rows were independently recomputed from the package CSV with no differences.
- No empty readiness verdict or binding reason.

## Parent actions

1. Treat `006_current_installed_map_package_bindings.csv` as the installed-map implementation input.
2. Preserve the implemented Trabzon mutex and require every Kashmir route caller to use its package readiness trigger before reservation.
3. Carry the accepted audit into the source specification if these bindings are approved; this plan folder remains working documentation.
4. Keep all unbound rows out of automatic, high-chaos, scenario, and specific-community selectors according to their verdict.
5. Implement runtime host-survival checks rather than copying the static 1936 outcome as an allow-list.

## Skills used

- `chaos-redux-events`
- `chaos-redux-subagents`

No skill was created or updated.
