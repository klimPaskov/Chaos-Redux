# SCN-008 scenario-detail localisation fit audit (2026-08-15)

## Disposition

The eight SCN-008 selected-mode descriptions were shortened to fit the existing `chaosx_scenarios_window` detail body without changing the scenario mechanics, mode cardinality, intensity rules, catalog status, or admission gates. The scenario remains source-registered but catalog `Unavailable` and fail-closed.

## Source change

Only `localisation/english/006_independence_wave_scenario_l_english.yml` was changed. The eight keys under `chaosx.scenarios.independence_wave.desc.*` now use concise player-facing text that retains the required mechanics: every viable movement is attempted, protected host remnants and unique anchors, pre-formed-league and release-created-faction separation, congress setup, former-host and bounded-target war rules, patron reach and influence, and Great Partition protected remnant states with non-overlapping territory.

The previous localisation lines were 296–457 characters including their keys. The replacement player-facing texts are 169–239 characters across the eight modes, while the existing detail body remains `maxWidth = 388` and `maxHeight = 104` in `interface/chaosx.gui`. The four intensity impact descriptions and summary-event text were not changed.

The localisation file retains its UTF-8 BOM. No scripted-localisation keys, scenario IDs, mode IDs, trigger logic, event effects, or GUI geometry were changed.

## Catalog mirror

Because the player-facing scenario detail changed, the editable workbook cell `Scenarios!C8` was updated to mirror `chaosx.scenarios.independence_wave.desc.sovereign_scatter`. Its style ID remains 44 and wrapping remains enabled. The workbook was exported with `.tools/export_event_catalog_csv.py`.

The export-only Scenarios CSV now has SHA-256 `489dc1772284bda64b8903a87b23b0d9f841335e866319b17b90d75570dd5af8`. Events and Clusters exports remain unchanged at SHA-256 `c5c29bc03092fe12d0a44381d59c5865f085c0bc3759240b6d2f151cd21fc6db` and `0bdd2e73f4c556af5fbdb028a2bbae258ef4d3402450d4bb112a63644047d299` respectively. The workbook status remains `Scenarios!F8 = Unavailable` and `Events!M7 = Partially Available`.

## MCP evidence

Post-change `hoi4.gui_inspect` for `chaosx_scenarios_window` with `scenario:{id:"independence_wave"}` returned `GUI_INSPECTED`, complete model extraction, 36 inspected elements, and no `GUI_VISIBLE_OVERLAP` failure. The shared graph remains aggregate-invalid because 2,000 global diagnostics were retained or truncated, including unrelated symbol, texture, unsupported, unresolved, and fidelity issues. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b37c2bfff4d8cd1d6934f2447f9da05279036e2165a8e7b997a7d7169fd9fc20/f284739081d1e1dc36f6d19a77eba8dad75d16e0cdfd7a457d8e9efc69a84c0b/gui-inspect.f268f149615e2e36.json`.

Post-change `hoi4.gui_render` returned `GUI_RENDERED` for normal, hover, selected, disabled, long-text, and full-list states at 1920×1080 and 2560×1440. The linked SVG artifact is available at `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ec5e0c0895fb42ae0b8d229c19e98de887e0909ccbaa016e2033308a3bb55a7b/d8c52ccaf5d586de51392030349b15aa16121d68ca9689745005f68ca044c626/chaosx_scenarios_window-full.svg`. The renderer is an offline approximation and the response was wire-truncated, so wrapping and clipping are not certified and the render is evidence rather than a full GUI acceptance claim.

## Scope record

No gameplay, event, scripted-localisation, GUI, central adapter, attestation, preflight, Join, portrait, flag, or asset source changed. SCN-008 remains unavailable until the existing package-attestation, typed scenario, event projection, and family-isolated GUI acceptance gates are satisfied.
