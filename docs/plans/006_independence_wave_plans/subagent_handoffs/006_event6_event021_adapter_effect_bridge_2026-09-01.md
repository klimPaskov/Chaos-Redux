# Event 006/Event 021 adapter effect bridge

Date: 2026-09-01.

## Scope and disposition

This tranche lets the validated Event 021 adapter consume Event 006 package-side effects without making the adapter an active Event 006 origin.

The shared `is_independence_wave_package_content_active` predicate already separates strict Event 006 lifecycle state from bounded Event 021 setup and proven origin-neutral receipts. The effect gates below now use that package-content contract where package state is intentionally consumed. Evolution feedback and achievement refresh remain explicitly restricted to a real Event 006 active origin.

## Changed source

- `common/scripted_effects/006_independence_wave_effects.txt` uses the package-content gate for package refresh, value mutation, route selection, host-ledger, idea-lifecycle, and network APIs. `independence_wave_prepare_country_origin` keeps Event 021 on its own generation counter and avoids recording an Event 006 origin or resetting Event 006 achievement trackers during adapter preparation. Evolution failure feedback and achievement refresh run only under the strict Event 006 active-origin proof.
- `common/scripted_effects/006_independence_wave_focus_effects.txt` allows validated adapter package setup to apply the shared focus value, transport, economy, and military-archetype bundles.
- `common/scripted_effects/006_independence_wave_form03_effects.txt` and `common/scripted_effects/006_independence_wave_form48_effects.txt` use the package-content gate for member-corridor and dissolution effects.
- `common/scripted_effects/006_independence_wave_formable_registry_effects.txt` uses the package-content gate for invitation/member ledgers and routes absorbed Event 021 adapters through `event021_cleanup_absorbed_event6_adapter` instead of ending an Event 006 origin.
- `common/scripted_effects/006_independence_wave_iw043_iw058_package_effects.txt` uses the package-content gate for the institutional surfaces of the two shared-focus carriers.

No package id, weight, cost, automatic count, origin flag, pre-event UI, category, mission, queue, or country admission was added or widened here.

## Contract and safety

The only non-strict paths are the bounded transient setup branch and the proven receipt branch of `is_independence_wave_package_content_active`. The strict `is_independence_wave_active_country` predicate remains the sole gate for Event 006 lifecycle, evolution, network, league, achievement, and visibility surfaces that require a committed origin. Event 005/Soviet-collapse origin separation remains unchanged.

The adapter generation path uses the Event 021 generation variable and does not advance `global.independence_wave_next_generation_id`, record an Event 006 origin, or run Event 006 achievement-reset logic. Adapter absorption invokes the existing Event 021 cleanup owner and leaves the normal Event 006 origin-end path intact for ordinary packages.

## Validation and limits

The parent ran the focused Event 006 allocator, country API, strict flag, FORM-16, SCN-008 scenario-matrix, and GUI-matrix validators successfully after the source bridge was present.

The available Event MCP inspect/render route remains partial and defers workspace-wide helper/lifecycle projections; no live game or save/load proof is claimed. Event 021 allowlisted `iw_070`–`iw_072` retain their explicit Event 006-origin predicates and remain fail-closed for the origin-neutral adapter. The broader Event 006 package boundary remains HOLD / PARTIAL pending complete country packages, rights/identity evidence, typed probability comparisons, and runtime receipts.
