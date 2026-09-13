# Event 006 catalog audit — 2026-09-12

## Disposition

Implemented as a bounded audit with no workbook cell changes required. The current shared workbook already matches the current player-facing localisation and preserves the newer catalog row and sheet structure. A mechanical exporter-width defect was repaired separately in `.tools/export_event_catalog_csv.py` so the read-only snapshots now match the workbook schemas.

## Audited workbook scope

Authoritative workbook: `docs/spreadsheets/chaos_redux_events_catalog.xlsx`.

- `Events!A7:M7` (Event ID `6`, Independence Wave) matches the current event-detail localisation at `chaosx.events_log.window.event_details.independence_wave`; `D7:H7` match the five current evolution body strings at `independence_wave.evolution.1.body` through `.5.body`.
- `Clusters!A3:H3` (Cluster ID `2`, Liberations) matches the current cluster detail at `chaosx.events_log.window.cluster_details.description.liberations`.
- `Scenarios!A8:F8` (Scenario ID `SCN-008`, Every Banner Rises) matches the current scenario name, Sovereign Scatter detail, type options, and Low/Medium/High/Maximum impact strings in `localisation/english/006_independence_wave_scenario_l_english.yml`.

All 11 source-to-workbook wording checks matched exactly. Evolution columns intentionally contain the current detail body strings without the separately localised evolution titles, consistent with the current workbook convention.

## Status and capacity boundary

The audit left `Events!M7` as `Needs Testing`, `Clusters!H3` as `Partially Available`, and `Scenarios!F8` as `Needs Testing`. No status was promoted and no 14/20 capacity claim was added.

## Export and validation

Ran `python .tools/export_event_catalog_csv.py` from the mod root successfully after the audit.

- `docs/spreadsheets/chaos_redux_events_catalog.csv`: 166 rows, 13 columns, SHA-256 `e2e457ba96ae89b316aa01248eebe41d9aacbafc590f4940b56a55133fcd35c6`.
- `docs/spreadsheets/chaos_redux_clusters_catalog.csv`: 20 rows, 8 columns, SHA-256 `689fe07883da14abe2ceb7c29c151db50808cf97a366e60808281b16e37c76a2`.
- `docs/spreadsheets/chaos_redux_scenarios_catalog.csv`: 16 rows, 6 columns, SHA-256 `8b944de19817b3887eac22e3d12437e62990273c8b0db1c6f27928f349d4b2e7`.

Each export contains its target row for Event ID `6`, Cluster ID `2`, and Scenario ID `SCN-008`. The workbook contains zero formulas and zero Excel error cells. Current tables are `Events!A1:M1014`, `Clusters!A1:H20`, `Cluster Memberships!A1:G76`, and `Scenarios!A1:F16`.

## Exporter repair

The exporter width map now uses 13 columns for Events and 8 for Clusters, matching the authoritative workbook headers. The regenerated snapshots have uniform row widths of 13, 8, and 6 respectively, with no trailing blank field and with `Clusters!Status` preserved. No workbook cell, player-facing wording, or catalog status changed.
