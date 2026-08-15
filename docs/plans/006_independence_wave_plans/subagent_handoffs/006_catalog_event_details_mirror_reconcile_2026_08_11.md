# Event 006 catalog Event Details mirror reconciliation

Status: complete for the requested spreadsheet scope. This handoff supersedes the same-day ladder-appending handoff; the numeric ladder remains in current authority documentation and is intentionally excluded from the catalog Event Details mirror.

## Workbook change

- Editable source: `docs/spreadsheets/chaos_redux_events_catalog.xlsx`
- Sheet and row: `Events!7` (`ID` `6`, `Independence Wave`)
- Changed field: `Details` (`Events!C7`)
- `Events!C7` now exactly matches the static player-facing text from `localisation/english/chaosx_gui_l_english.yml:948`, preserving the Independence Wave premise and Join eligibility sentence while excluding the runtime-only rival-bloc scripted-localisation suffix.
- Removed the Ruthenian/package spotlight and automatic-wave numeric ladder from `Events!C7` so the catalog field mirrors in-game Event Details.
- Preserved `Events!M7 = Partially Available`, all other Event 006 fields, workbook sheets, formatting, tables, validation, and structure.

## Export

After saving the workbook, ran from the mod root:

```text
python .tools/export_event_catalog_csv.py
```

Exporter completed successfully and refreshed all three export-only snapshots:

- `docs/spreadsheets/chaos_redux_events_catalog.csv` — 183 rows, 13 columns, SHA-256 `c5c29bc03092fe12d0a44381d59c5865f085c0bc3759240b6d2f151cd21fc6db`
- `docs/spreadsheets/chaos_redux_clusters_catalog.csv` — 14 rows, 7 columns, SHA-256 `0bdd2e73f4c556af5fbdb028a2bbae258ef4d3402450d4bb112a63644047d299`
- `docs/spreadsheets/chaos_redux_scenarios_catalog.csv` — 12 rows, 6 columns, SHA-256 `66ea4a5802862c1c72f0f3e8ead04cb4f1bfde5e62f88411e3b29f64cb5cf760`

## Validation and blockers

- Saved `Events!C7` matches the static source text exactly; no Ruthenian/package or ladder text remains in the cell.
- Exported Event ID `6` row matches the saved workbook, including `Partially Available` status.
- Workbook retains all existing sheets, tables, validation, and zero formulas.
- No blocked or `needs_user_review` cells were introduced. Runtime admission and live validation remain outside this spreadsheet handoff.
