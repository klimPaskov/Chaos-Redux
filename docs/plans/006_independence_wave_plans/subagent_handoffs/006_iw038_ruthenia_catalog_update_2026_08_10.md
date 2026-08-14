# IW-038 Ruthenia catalog update

Status: complete for the requested spreadsheet scope; no live or in-game evidence claimed.

## Source authority

- `docs/events/006_independence_wave/ruthenia_package.md`
- Parent direction: align Event 006's player-facing summary with the admitted Ruthenian mountain compact, four government paths, shared Independence Wave framework, and the package's current partially available status.

## Workbook change

- Editable source: `docs/spreadsheets/chaos_redux_events_catalog.xlsx`
- Sheet: `Events`
- Row: `7` (`ID` `6`, `Independence Wave`)
- Field: `Details` (`Events!C7`)
- The summary keeps the existing Independence Wave premise and Join the Independence Wave condition, then adds the player-facing Ruthenian package description: a mountain compact secures civic concord and mountain security before choosing among civic, agrarian, socialist, or emergency governments through the shared Independence Wave framework.
- `Events!M7` remains `Partially Available`.
- No implementation identifiers, tuning values, project costs, force masks, or asset paths were added to the player-facing field.
- No other workbook rows, sheets, formulas, formatting, tables, filters, data validation, freeze panes, or workbook structure were changed.

## Export

Ran from the mod root after the workbook save:

```text
python .tools/export_event_catalog_csv.py
```

Exporter completed successfully and refreshed all three export-only snapshots:

- `docs/spreadsheets/chaos_redux_events_catalog.csv` - 183 rows, 13 columns, SHA-256 `a735e77aef55c124f566aa19ad54df2abd9f6bc58bccb52bd16edfe808b3e6bb`
- `docs/spreadsheets/chaos_redux_clusters_catalog.csv` - 14 rows, 7 columns, SHA-256 `0bdd2e73f4c556af5fbdb028a2bbae258ef4d3402450d4bb112a63644047d299`
- `docs/spreadsheets/chaos_redux_scenarios_catalog.csv` - 12 rows, 6 columns, SHA-256 `66ea4a5802862c1c72f0f3e8ead04cb4f1bfde5e62f88411e3b29f64cb5cf760`

## Blockers and review

- No spreadsheet cells are blocked or marked `needs_user_review` for this update.
- The Ruthenian package's historical portraits remain source placeholders and Event 006 remains `Partially Available`; that package status is recorded here rather than exposed as implementation wording in the player-facing summary.
- Runtime/live validation is outside this handoff and was not claimed.
