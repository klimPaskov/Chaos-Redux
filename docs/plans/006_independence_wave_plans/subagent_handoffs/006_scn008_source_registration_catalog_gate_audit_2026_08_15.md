# SCN-008 source-registration and catalog-gate audit (2026-08-15)

## Disposition

SCN-008 (`Every Banner Rises`) is source-registered and generic-UI wired, but its catalog status remains `Unavailable` and must remain fail-closed. This audit makes no gameplay, localisation, GUI, workbook, adapter, attestation, preflight, or Join change.

The runtime source exposes the scenario entry and summary events, six numeric type families, four intensity bands, eight visible modes, transaction barriers, candidate ranking, blocked/unavailable ledger output, and the shared release helpers. Those surfaces establish source coverage, not playable acceptance.

## Source crosswalk

- `events/006_independence_wave_scenario.txt` defines the hidden launch barrier `chaosx.triggerable_scenarios.8` and the summary event `chaosx.triggerable_scenarios.80`.
- `common/decisions/006_independence_wave_scenario_decisions.txt` defines the read-only scenario-ledger navigation decisions and zero-cost AI settings.
- `common/decisions/categories/006_independence_wave_scenario_categories.txt` owns the scenario-ledger decision category.
- `common/scripted_triggers/006_independence_wave_scenario_triggers.txt` validates the six numeric type families, three Universal Belligerence rules, four intensity values, transaction barrier, and launch eligibility.
- `common/scripted_effects/006_independence_wave_scenario_effects.txt` initializes settings, applies intensity tuning, ranks and iterates the 138 bound-package registry, records blocked or unavailable entries, and invokes shared release helpers.
- `common/script_constants/006_independence_wave_scenario_constants.txt` records the scenario families, `bound_package_count = 138`, `disabled_unbound_package_count = 55`, total registry size 206, and country/intensity values.
- `localisation/english/006_independence_wave_scenario_l_english.yml` is UTF-8 BOM encoded and supplies the final player-facing name `Every Banner Rises`, eight mode labels, four intensity descriptions, launch states, and summary text. Each impact description states that all viable candidates are still attempted.
- `common/scripted_effects/chaosx_triggerable_scenarios_effects.txt`, `common/scripted_triggers/chaosx_triggerable_scenarios_triggers.txt`, and `common/scripted_localisation/chaosx_scripted_localisation_scenarios.txt` register scenario ID 8, sort value 3.5, selection eligibility, names, IDs, type labels, impact labels, and launch-status text in the shared settings surface.
- `common/scripted_guis/chaosx_scripted_gui_settings.txt` and `interface/chaosx.gui` provide the generic scenario list, sort controls, intensity slider, type controls, launch confirmation, and scenario detail body.

## MCP evidence

The mandatory event scan for `events/006_independence_wave_scenario.txt` returned `EVENT_INSPECTED_PARTIAL` at revision `741883f50501db1f866db675ee6ad6cb4009a90ad539eb84b08ce5e82602f65b`, graph hash `37eb00185cb12c74f97438ecee7380780cf4eec14d3693f7930e97a91ce4b720`, and zero selected blocking diagnostics. The workspace projection remains partial because helper and lifecycle analysis is deferred. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cf1b47c879d6b17d76f89e35bbf308a3b4aa5c8c9e4bdcb363fe37f3ed6a087a/01f0403587d42802366df9f39cadb90449db3d8b39e4a7b71bdf3e6392172c79/event-scan-741883f50501.json`.

The focused state-flow inspection for `chaosx.triggerable_scenarios.8` returned the same partial revision and zero selected blocking diagnostics. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9bf78c5d299f335343dedf7970d1e6246aa70039c59e2189160e88ce29e8ed4b/f32036825107f86e73f315853fc85012792188e160e738774f565e9439560223/event-state_flow-741883f50501.json`.

The generic `chaosx_scenarios_window` GUI inspection with `scenario:{id:"independence_wave"}` returned `GUI_INSPECTED`, complete model extraction, 36 inspected elements, and no detected visible-overlap failure. Aggregate validation is false because the shared workspace retained truncated global diagnostics, including 1999 retained graph diagnostics, 1999 retained validation diagnostics, 8 unresolved elements, and unrelated symbol, texture, unsupported, and fidelity issues. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/12e4045a27b28baca5f9983bc25f4370613f3dd750bc676156c1376c75d0834d/a7170028bd9fb4ee1527ad323a39167d25e2c8d302880185e293e01576ca5c2f/gui-inspect.6f7eed155ac66534e.json`.

The corresponding render produced a full scenario-window SVG artifact, but the response was truncated and did not provide clean validation evidence. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ec5e0c0895fb42ae0b8d229c19e98de887e0909ccbaa016e2033308a3bb55a7b/7c31424202d045c202f127a4cc844a1073f385b4d607a67bdc2cd2b6a5a84399/chaosx_scenarios_window-full.svg`.

## Catalog boundary

The editable workbook remains the catalog source of truth. `Scenarios!F9` for `SCN-008` remains `Unavailable`, while `Events!M7` remains `Partially Available`. This matches the current catalog reconciliation and the accepted whole-event boundary of 40 runtime adapters, 32 content-attested packages, 29 compatible groups, and 161 unattested selectable rows.

Changing SCN-008 to `Playable`, `Needs Testing`, or `Partially Available` would overstate acceptance because the scenario's 138 bound-package target is not fully attested, typed probability fixtures remain incomplete, event MCP analysis is partial, GUI validation is aggregate and truncated, and no clean runtime scenario acceptance receipt exists. The source registry and generic UI therefore remain documented as implemented source surfaces, while catalog availability remains intentionally fail-closed.

## Required follow-up before catalog promotion

1. Complete typed scenario fixtures covering the eight visible modes, four intensities, and three Universal Belligerence rules, then obtain same-scenario probability evidence without claiming balance from empty or incomplete pools.
2. Re-run focused event inspection after the workspace helper and lifecycle projection is available and preserve a current revision receipt.
3. Obtain family-isolated GUI inspection and render evidence for long text, full-list state, intensity controls, launch confirmation, and scenario summary at the supported resolutions.
4. Reconcile the 138 bound-package target against current content attestations and scenario preflight without widening central admission or deterministic Join by registry count alone.
5. Only after those gates pass, update the workbook from its source and run `.tools/export_event_catalog_csv.py`.

## Scope record

No gameplay, localisation, GUI, workbook, CSV, central adapter, attestation, preflight, Join, portrait, flag, or asset file was changed by this audit.
