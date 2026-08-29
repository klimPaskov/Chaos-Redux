# Event 006 Event Details and catalog premise repair

Date: 2026-08-29 (Europe/Kyiv).

## Scope

This bounded tranche keeps the Event 006 Event Details window and the gameplay-facing catalog aligned with the premise-only wording contract. It removes exact Join thresholds and rival-compact ledger interpolation from the public event summary while preserving the underlying Join, rival-compact, decision, and status-window mechanics in their owning systems.

## Changed files

- `localisation/english/chaosx_gui_l_english.yml`: rewrote `chaosx.events_log.window.event_details.independence_wave` as a situation-and-premise summary with no thresholds, dynamic counters, reward values, or ledger selectors.
- `docs/spreadsheets/chaos_redux_events_catalog.xlsx`: updated `Events!C7` to the same premise text and corrected `Clusters!D3` from the duplicated `5, 6, 6, 6` member list to `5, 6`.
- `docs/spreadsheets/chaos_redux_events_catalog.csv`: regenerated from the workbook.
- `docs/spreadsheets/chaos_redux_clusters_catalog.csv`: regenerated from the workbook.
- `docs/spreadsheets/chaos_redux_scenarios_catalog.csv`: regenerated from the workbook.

## Validation and limits

`python .tools/export_event_catalog_csv.py` completed successfully and reported the three regenerated exports. The workbook's existing openpyxl data-validation warning remains a tooling limitation; no formula-bearing cells were changed. No gameplay, event timing, category visibility, decision cost, AI weight, admission, or asset file changed. Current HOI4 Event Details MCP inspect/render/compare routes remain unavailable, so this handoff records source and catalog alignment only and makes no engine or live-runtime claim.

## Simplifications and blockers

No fallback or design simplification was introduced. Full Event 006 completion remains HOLD / PARTIAL under the current completion audit because package breadth, typed probability evidence, GUI acceptance, portrait/identity gates, and super-event 23 rights/audio remain unresolved.
