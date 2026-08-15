# Event 006 catalog update: Join the Independence Wave

Status: complete for the requested spreadsheet scope; no live or in-game evidence claimed.

## Changed workbook

- Editable source: `docs/spreadsheets/chaos_redux_events_catalog.xlsx`
- Sheet: `Events`
- Row: `7` (`ID` `6`, `Independence Wave`)
- Field: `Details` (`Events!C7`)
- The existing Event 006 summary now uses concise in-world wording for the Join the Independence Wave path: a greatly reduced country whose entire remaining territory matches a prepared homeland may dissolve its old government and continue as that country, while refusal retains the existing government.
- No unrelated rows, sheets, formulas, formatting, filters, validation, freeze panes, or workbook structure were changed.
- Event 006 status remains `Partially Available`; no live evidence was asserted.

## Export

Ran from the mod root:

```text
python .tools/export_event_catalog_csv.py
```

Exporter completed successfully and refreshed all three export-only snapshots after the wording revision:

- `docs/spreadsheets/chaos_redux_events_catalog.csv` — 183 rows, 13 columns, SHA-256 `e1be032673ad694dd4cc2b932979b7659818c946c9cea59327614135ebcefe54`
- `docs/spreadsheets/chaos_redux_clusters_catalog.csv` — 14 rows, 7 columns, SHA-256 `0bdd2e73f4c556af5fbdb028a2bbae258ef4d3402450d4bb112a63644047d299`
- `docs/spreadsheets/chaos_redux_scenarios_catalog.csv` — 12 rows, 6 columns, SHA-256 `66ea4a5802862c1c72f0f3e8ead04cb4f1bfde5e62f88411e3b29f64cb5cf760`

## Blockers / review

No spreadsheet cells are blocked or marked `needs_user_review` for this requested update. Runtime/live validation remains outside this handoff and was not claimed.
