# Event 006 catalog audit — 2026-09-13

Date: 2026-09-13 (Europe/Kyiv).

Owner: bounded Chaos Redux spreadsheet/catalog worker.

## Disposition

No workbook cell change was justified. The existing Event 006 workbook rows and generated CSV snapshots match the current player-facing localisation and the current catalog/status authority. This audit did not promote Event 006, SCN-008, or Cluster 2 availability.

The workbook and export files already had unrelated working-tree changes when this audit began. They were preserved. No gameplay, localisation, scripted-localisation, or source-of-truth files were edited.

## Files reviewed

- `docs/spreadsheets/chaos_redux_events_catalog.xlsx` as the editable catalog source.
- `docs/spreadsheets/chaos_redux_events_catalog.csv`, `docs/spreadsheets/chaos_redux_clusters_catalog.csv`, and `docs/spreadsheets/chaos_redux_scenarios_catalog.csv` as read-only generated snapshots.
- `localisation/english/chaosx_gui_l_english.yml` for Event Details, Cluster 2 name/detail, and the Liberations cluster wording.
- `localisation/english/006_independence_wave_evolution_l_english.yml` for the five evolution bodies.
- `localisation/english/006_independence_wave_scenario_l_english.yml` for SCN-008 name, Sovereign Scatter detail, eight type names, and four intensity strings.
- `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md` for current catalog authority and status boundaries.
- `docs/specs/006_independence_wave_specs/quality/catalog_alignment_handoff.md` for the accepted premise-only catalog contract.
- `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_2_event_flow_and_evolutions.md` and `specs/006_independence_wave_spec_part_6_formables_league_and_scenario.md` for the accepted five-evolution and eight-mode SCN-008 structure.
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_completion_audit_2026-09-12.md` for current completion disposition and catalog status gates.
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_asset_audit_completion_update_2026-09-12.md` for current visual-asset blockers.
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_catalog_audit_2026-09-12.md` for the preceding catalog/export audit and exporter-width repair receipt.

## Workbook and wording evidence

The authoritative workbook currently has `Events!A1:M1014`, `Clusters!A1:H20`, `Cluster Memberships!A1:G76`, and `Scenarios!A1:F16`. The selected rows are `Events!A7:M7` for Event ID `6`, `Clusters!A3:H3` for Cluster ID `2`, and `Scenarios!A8:F8` for `SCN-008`.

The workbook has zero formulas and zero Excel error cells. Existing table references and styles were preserved; no row, column, filter, validation, freeze-pane, or workbook-structure edit was made.

The exact mirror audit produced 12/12 matches:

- `Events!C7` matches `chaosx.events_log.window.event_details.independence_wave`.
- `Events!D7:H7` match `independence_wave.evolution.1.body` through `.5.body`.
- `Clusters!B3` matches `chaosx.event_cluster.liberations.name`.
- `Clusters!C3` matches `chaosx.events_log.window.cluster_details.description.liberations`.
- `Scenarios!B8` matches `chaosx.scenarios.independence_wave.name`.
- `Scenarios!C8` matches `chaosx.scenarios.independence_wave.desc.sovereign_scatter`.
- `Scenarios!D8` matches all eight current SCN-008 type localisation keys joined in the existing catalog convention.
- `Scenarios!E8` matches all four current SCN-008 intensity localisation keys in the existing labelled-paragraph convention.

Event 006 retains the empty terminal/world-end field required by the accepted catalog contract, type `Minor Repeatable`, chaos level `1`, cluster IDs `2, 16`, and status `Needs Testing`. Cluster 2 retains its current five-member list and severity list, type `Minor Repeatable`, chaos level `1`, and status `Partially Available`. SCN-008 retains its current eight player-facing modes, four intensity paragraphs, and status `Needs Testing`.

## Export validation

The generated snapshots were refreshed from the existing workbook with `python .tools/export_event_catalog_csv.py`. The exporter returned `status: success`.

- `docs/spreadsheets/chaos_redux_events_catalog.csv`: 165 data rows, 13 columns, SHA-256 `e2e457ba96ae89b316aa01248eebe41d9aacbafc590f4940b56a55133fcd35c6`.
- `docs/spreadsheets/chaos_redux_clusters_catalog.csv`: 19 data rows, 8 columns, SHA-256 `689fe07883da14abe2ceb7c29c151db50808cf97a366e60808281b16e37c76a2`.
- `docs/spreadsheets/chaos_redux_scenarios_catalog.csv`: 15 data rows, 6 columns, SHA-256 `8b944de19817b3887eac22e3d12437e62990273c8b0db1c6f27928f349d4b2e7`.

The selected Event ID `6`, Cluster ID `2`, and `SCN-008` rows are present in their corresponding snapshots with uniform row widths. No CSV was edited directly.

## Change report

No workbook sheets, rows, columns, event IDs, fields, statuses, or formatting were changed by this worker. The only write performed during this audit was the required exporter refresh of the three generated CSV snapshots from the unchanged workbook.

## Remaining blockers

The current Event 006 completion receipt remains **HOLD / PARTIAL**. The completion handoff records 161 selectable rows without central content attestation, incomplete League transition callers and typed probability evidence, partial broader SCN-008 evidence, and a blocked super-event 23 path. These are not safe reasons to alter catalog wording or promote statuses.

The current asset handoff keeps ASSET-005, ASSET-006, ASSET-039, and ASSET-044 at `needs_user_review`, and ASSET-045 and ASSET-046 at `blocked`. It also records unresolved portrait consumer/rights gates, generated-flag provenance gaps, and incomplete dynamic GUI playback evidence. No catalog status was changed to represent these blockers beyond the existing non-final status values.

