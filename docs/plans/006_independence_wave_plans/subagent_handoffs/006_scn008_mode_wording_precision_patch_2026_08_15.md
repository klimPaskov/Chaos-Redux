# SCN-008 mode wording precision patch (2026-08-15)

## Disposition

Applied a narrow player-facing localisation correction for two SCN-008 mode descriptions. The patch clarifies the existing scenario contract without changing scenario IDs, mode selection, allocation, type effects, intensity rules, or admission status.

## Source changes

`localisation/english/006_independence_wave_scenario_l_english.yml`

- `chaosx.scenarios.independence_wave.desc.sovereign_scatter` now states that releases remain outside pre-formed leagues and retain no release-created faction ties.
- `chaosx.scenarios.independence_wave.desc.great_partition` now states that the host keeps one protected remnant, preferring a controlled capital, then a safe core or owned state.

The wording follows the accepted scenario type contract and the core host-protection order. No semicolons, scripted-localisation keys, dynamic tokens, or mechanics were introduced.

## Catalog mirror

`docs/spreadsheets/chaos_redux_events_catalog.xlsx` cell `Scenarios!C8` was updated to mirror the revised Sovereign Scatter description. Existing style ID `44` and wrapping were preserved. The workbook exporter was run from the mod root.

Current export hashes:

- Events CSV: `c5c29bc03092fe12d0a44381d59c5865f085c0bc3759240b6d2f151cd21fc6db`
- Clusters CSV: `0bdd2e73f4c556af5fbdb028a2bbae258ef4d3402450d4bb112a63644047d299`
- Scenarios CSV: `8d31d120dd81adb3ef48bae2afed8cf539bb4f23a60b04771c1eacc57875a398`

## Validation and limits

- The localisation file retains its UTF-8 BOM.
- The two owned keys remain unique and the catalog text mirrors the revised Sovereign Scatter key.
- This is a text/catalog correction only. No gameplay, GUI, central adapter, attestation, preflight, Join, asset, or workbook surface beyond `Scenarios!C8` changed.
- SCN-008 remains unavailable and fail-closed pending its existing typed scenario, package-attestation, event-projection, and family-isolated GUI acceptance gates.

## Post-change GUI evidence

The required post-change `hoi4.gui_inspect` for `chaosx_scenarios_window` with scenario `independence_wave` returned `GUI_INSPECTED` with a complete model extraction and no `GUI_VISIBLE_OVERLAP` failure. The workspace-wide graph remains aggregate-invalid because the server retained or truncated unrelated global diagnostics. Artifact:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/06d28e9174ee47d096b51b858dd0ea99deb795a308c674704badf93a383311e9/9bc3ee22e13903264c4e69bf7b0642f5b39a1c3bd067460bc5a4d792e0489d9a/gui-inspect.57021b835ecdacd3.json`

The required `hoi4.gui_render` completed for normal, long-text, full-list, and missing-localisation states at 1920×1080 and 2560×1440. The render is offline approximation evidence and wire-truncated, so it does not certify live wrapping or clipping. Artifact:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ec5e0c0895fb42ae0b8d229c19e98de887e0909ccbaa016e2033308a3bb55a7b/f51a6d4c0a86501d94df206efa04fcc28a7e2b2b23e2286139b7a8d68e2145ca/chaosx_scenarios_window-full.svg`
