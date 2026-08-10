# Event 005 spreadsheet parity resolution

Date: 2026-08-09

## Scope

This pass reconciled the editable Event 005 workbook row with the live event-detail and evolution-detail localisation.

## Result

- `docs/spreadsheets/chaos_redux_events_catalog.xlsx` remains the only editable catalog source.
- `Events!C6` now exactly matches `chaosx.events_log.window.event_details.soviet_collapse`, including its dynamic scripted-localisation tokens.
- `Events!D6:H6` already matched the five live Event 005 evolution-detail strings and required no wording changes.
- The Event 005 row remains ID `5`, cluster `2`, severity `Severe`, and status `Playable`.
- Existing workbook styles were preserved. The workbook contains no formulas or comments.

## Export parity

After the workbook correction, `.tools/export_event_catalog_csv.py` regenerated the export-only files:

- `docs/spreadsheets/chaos_redux_events_catalog.csv`
- `docs/spreadsheets/chaos_redux_clusters_catalog.csv`
- `docs/spreadsheets/chaos_redux_scenarios_catalog.csv`

The CSV files were not edited directly.

## Completion statement

The Event 005 workbook, event-detail text, evolution-detail text, and generated catalog exports are in exact wording parity. No fallback wording or simplified summary was used.
