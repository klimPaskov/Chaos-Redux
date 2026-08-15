# Event 006 catalog wave-ladder update

Status: complete for the requested spreadsheet scope. No gameplay, localisation, or live-runtime changes were made.

## Workbook change

- Editable source: `docs/spreadsheets/chaos_redux_events_catalog.xlsx`
- Sheet and row: `Events!7` (`ID` `6`, `Independence Wave`)
- Changed field: `Details` (`Events!C7`)
- Preserved the existing Event Details/summary and Ruthenian package wording, then added the player-facing automatic wave ladder: Calm World 3, Gathering Storm 4, Rising Chaos 5, Chaos Tier 7, and Totalen Chaos 10 countries. World Collapse remains 10 countries with stronger forces, greater instability, increased rarity pressure, and greater ambition.
- Preserved `Events!M7 = Partially Available`, all other Event 006 fields, workbook sheets, formatting, tables, validation, and structure.

## Export

After saving the workbook, ran from the mod root:

```text
python .tools/export_event_catalog_csv.py
```

Exporter completed successfully and refreshed all three export-only snapshots:

- `docs/spreadsheets/chaos_redux_events_catalog.csv` — 183 rows, 13 columns, SHA-256 `b0bca5948cfa100d4a2b8a35b99649d985a111a1894039e23c4bc42962f264d9`
- `docs/spreadsheets/chaos_redux_clusters_catalog.csv` — 14 rows, 7 columns, SHA-256 `0bdd2e73f4c556af5fbdb028a2bbae258ef4d3402450d4bb112a63644047d299`
- `docs/spreadsheets/chaos_redux_scenarios_catalog.csv` — 12 rows, 6 columns, SHA-256 `66ea4a5802862c1c72f0f3e8ead04cb4f1bfde5e62f88411e3b29f64cb5cf760`

## Validation and blockers

- Workbook retains the `Events`, `Clusters`, `Scenarios`, `Info`, and `Legend` sheets and contains zero formulas.
- Exported Event ID `6` row matches the saved workbook, including the ladder wording and `Partially Available` status.
- No blocked or `needs_user_review` cells were introduced. Runtime admission and live validation remain outside this spreadsheet handoff.
