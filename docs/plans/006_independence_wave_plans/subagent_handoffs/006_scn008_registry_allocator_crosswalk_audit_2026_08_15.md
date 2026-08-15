# SCN-008 registry and allocator crosswalk audit (2026-08-15)

This is a bounded source and evidence audit of the Event 006 SCN-008 ranked allocator. It does not claim a live-game transaction or promote any package.

## Disposition

No safe source patch was justified. The allocator and current registry agree on the accepted 138 bound rows, the 55 current-map-unbound rows, and the 13 vanilla-route overlay rows that remain outside the standalone release pool.

## Crosswalk evidence

- `common/scripted_effects/006_independence_wave_scenario_effects.txt` contains 138 unique `independence_wave_scenario_ranked_package_ids` entries.
- The same file contains 55 unique `independence_wave_scenario_blocked_package_ids` entries in `independence_wave_scenario_append_unbound_registry_rows`.
- The ranked and unbound sets are disjoint, and together contain 193 package IDs.
- All 138 ranked IDs and all 55 unbound IDs exist in both `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv` and `docs/specs/006_independence_wave_specs/research/006_package_research_resolution.csv`.
- The 13 registry rows excluded from those two sets are exactly the rows marked `vanilla_route_overlay_only`: IW-005, IW-022, IW-025, IW-035, IW-059, IW-085, IW-101, IW-102, IW-105, IW-156, IW-196, IW-197, and IW-204.
- Every unbound package ID is paired with exactly one country entry, and each entry matches the current installed binding in `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv`.
- The ranked rows resolve to the current binding ledger without missing package IDs. Their disposition mix remains intentional: automatic, not-living, unique-state, high-chaos, route-only, specific-variant, and scenario-only rows are attempted through the shared preflight and reservation path rather than silently promoted.
- `common/script_constants/006_independence_wave_scenario_constants.txt` retains the matching registry constants: `bound_package_count = 138`, `disabled_unbound_package_count = 55`, and `total_registry_package_count = 206`.

## Ledger ordering witness

`independence_wave_scenario_freeze_summary` clears the presentation arrays before rebuilding them. On a committed plan it copies selected IDs to the released ledger and rejected IDs/reasons to the blocked ledger. On a failed plan it copies rejected rows and selected rows to the blocked ledger with the failure reason. Only after that bounded-plan branch does `independence_wave_scenario_append_unbound_registry_rows` append the 55 quarantined IDs, matching country entries, and `unbound_current_map` reasons. The final blocked count is therefore computed after the unbound rows are appended, while `bound_blocked_count` remains the count of rejected bound rows. No array-order defect was found in this review.

## MCP evidence boundary

The required file-targeted `hoi4.event_inspect` scan of `events/006_independence_wave_scenario.txt` completed as `EVENT_INSPECTED_PARTIAL` with zero selected blocking diagnostics. The source-linked artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9c500ddf43b7989e95dd47e9413b6de97f79b2c7d795867598b604cb2a7ce497/1e9c391c2493c6bdee93c54ea6fb812272d52840dfcdf379fc2b47cff127de4b/event-scan-741883f50501.json` at revision `741883f50501db1f866db675ee6ad6cb4009a90ad539eb84b08ce5e82602f65b`.

The bounded `hoi4.event_render` overview completed as `EVENT_RENDERED_PARTIAL` with source-linked JSON, SVG, and PNG artifacts. The overview artifact root is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b6bc760071f2f76ab4b5cd0b7f867146e91ee99b05c8ed623473fab975bfc43c/26a235014d151fc06ced1f24e1f9c40e7549d21ae71451023765099c37533cf9/event-overview-741883f50501-manifest.json`. Validation remains partial because the large workspace defers helper and lifecycle projections; this is not treated as a full event pass.

## Remaining boundary

The 13 overlay rows remain outside the standalone allocator by design. The 161 unattested selectable rows, adapter-only packages, package identity and asset holds, typed probability limitations, and central admission/Join gates remain governed by the current whole-event authority. This audit does not widen any adapter, attestation, preflight, scenario, or Join list.
