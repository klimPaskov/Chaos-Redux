# Event 006 catalog audit — 2026-09-12

## Disposition

Implemented as a bounded audit with no safe workbook cell changes required. The current shared workbook already matches the current player-facing localisation and preserves the newer catalog row and sheet structure.

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

- `docs/spreadsheets/chaos_redux_events_catalog.csv`: 166 rows, 14 columns, SHA-256 `2513570a9dcba604101d6258549882ba33740e56d7dba005cfbf424da83261b4`.
- `docs/spreadsheets/chaos_redux_clusters_catalog.csv`: 20 rows, 7 columns, SHA-256 `a5b37060ddcd4063f10eb326c21ca8b4b3f557b2be2be48dc2c3c0cbe60ff28e`.
- `docs/spreadsheets/chaos_redux_scenarios_catalog.csv`: 16 rows, 6 columns, SHA-256 `8b944de19817b3887eac22e3d12437e62990273c8b0db1c6f27928f349d4b2e7`.

Each export contains its target row for Event ID `6`, Cluster ID `2`, and Scenario ID `SCN-008`. The workbook contains zero formulas and zero Excel error cells. Current tables are `Events!A1:M1014`, `Clusters!A1:H20`, `Cluster Memberships!A1:G76`, and `Scenarios!A1:F16`.

## Remaining review item

The exporter currently emits a trailing blank Events CSV column and omits the workbook-only Clusters status column because its fixed export widths are 14 and 7 respectively. This is an exporter-contract issue outside the workbook-only audit; no exporter or workbook structure change was made.

