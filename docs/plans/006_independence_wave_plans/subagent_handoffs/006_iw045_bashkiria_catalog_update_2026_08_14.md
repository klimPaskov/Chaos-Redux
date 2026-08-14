# IW-045 Bashkiria catalog update — 2026-08-14

## Scope

Updated only the editable event catalog workbook field `Events!C7` for Event ID `6` (`Independence Wave`). The existing static Independence Wave Event Details mirror remains byte-for-byte intact as the first paragraph; the second paragraph is the accepted additive player-facing Bashkiria package summary.

## Workbook change

- Source workbook: `docs/spreadsheets/chaos_redux_events_catalog.xlsx`
- Sheet/row/field: `Events!C7` / Excel row 7 / `Details`
- Event ID: `6` (`Independence Wave`)
- Preserved: `Events!A7:B7`, `Events!D7:M7`, all other sheets, workbook formatting, formulas, filters, validation, freeze panes, and structure.
- Added summary: Bashkiria's Frontier Congress, Congress Cohesion and Frontier Readiness ledgers, constitutional/agrarian/socialist/emergency routes, oilfield and railway administration, mounted frontier security, community registration, former-host ledgers, and the Volga–Ural corridor.
- Deliberately omitted: numeric authority/ladder values and state identifiers from the player-facing catalog summary.

## Export

After each workbook save, ran from the mod root:

```text
python .tools/export_event_catalog_csv.py
```

Final exporter result: success.

- `docs/spreadsheets/chaos_redux_events_catalog.csv` — 183 rows, 13 columns, SHA-256 `d486dffcb1208a4c97ed147629379e520084f822c1e4f3bd4ddb564f5bcab170`
- `docs/spreadsheets/chaos_redux_clusters_catalog.csv` — 14 rows, 7 columns, SHA-256 `0bdd2e73f4c556af5fbdb028a2bbae258ef4d3402450d4bb112a63644047d299`
- `docs/spreadsheets/chaos_redux_scenarios_catalog.csv` — 12 rows, 6 columns, SHA-256 `66ea4a5802862c1c72f0f3e8ead04cb4f1bfde5e62f88411e3b29f64cb5cf760`

The exported Event ID `6` row mirrors the saved `Events!C7` text, including the Unicode Volga–Ural corridor name. No CSV was edited directly.

## Blockers / review

No blocked or `needs_user_review` cells were introduced. Runtime admission, whole-event status, and live validation remain outside this spreadsheet-only handoff.
