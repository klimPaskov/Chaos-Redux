# Final Event-Free Spreadsheet Alignment

> **Superseded historical identifier banner (2026-08-25):** Any `famine_incident.1`, `migration_incident.1`, or incident-option identifier quoted in this historical handoff is source-snapshot terminology only and is superseded; current authorities document accounting/presentation seams only and the deliberate deletion of the incident event files and constants.

Status: complete, 25 August 2026.

## Workbook change

- Workbook: `docs/spreadsheets/chaos_redux_events_catalog.xlsx`.
- Sheet: `Events`.
- Workbook row: `150`.
- Catalog event ID: `149`.
- Changed cell: `Events!C150` (`Details`).
- Previous wording: `Retired and absorbed into the migration system. It is unavailable as a random event, and famine-driven movement enters migration only through exact causal adapters.`
- Final wording: `Retired and absorbed into the shared dynamic famine and migration system. Unavailable as a random event.`
- Preserved `Events!A150` as `149`, `Events!B150` as `Immigrations`, and `Events!N150` as `Unavailable`.
- No `Clusters` or `Scenarios` rows or cells were changed.

## Event-free boundary evidence

- The workbook contains no `famine_incident.1`, `migration_incident.1`, `state-pulse`, or `state pulse` cell value.
- No replacement event row was added.
- No famine or migration system event-pool row was added.
- No famine or migration pacing row was added.
- Event 149 remains retired and unavailable; it is not repurposed as a system event.
- Event 118 (`Plague of locust`), Event 120 (`Massive Volcano Eruption`), and Event 131 (`Widespread Mutiny`) remain catalog rows with `Unavailable` status and their existing wording; they remain unavailable source blockers and were not repurposed.
- The workbook retains the existing four sheets, table ranges, three Events validations, two Clusters validations, one Scenarios validation, and zero formulas.

## Export result

Ran `python .tools/export_event_catalog_csv.py` from the mod root after the workbook save.

- Events export: `docs/spreadsheets/chaos_redux_events_catalog.csv`, 177 rows, 14 columns, SHA-256 `9e27472ac8b9599c7fc80cf6f28580199ef0cf00f1e29272144186129e10beb4`.
- Clusters export: `docs/spreadsheets/chaos_redux_clusters_catalog.csv`, 14 rows, 7 columns, SHA-256 `647c9206de61a70d7a0d7adf0740dc97c81c8e63d01fefac6549b430b666425b`.
- Scenarios export: `docs/spreadsheets/chaos_redux_scenarios_catalog.csv`, 12 rows, 6 columns, SHA-256 `52a80f59912841d0b046f889a40bdec66b452d5cc92c3f486245de56f08559cd`.
- Workbook SHA-256 after save: `cf152e972e661c8f05c354aed29b34db5aaac88f6671d874ce60cdb5cdd9c9ca`.
- The exported Event 149 row contains the final retirement wording and `Unavailable` status.

## Blockers

- No spreadsheet alignment blocker remains.
- The unavailable source status for Events 118, 120, and 131 remains a parent-owned gameplay/source blocker; this workbook task did not invent callbacks, replacement IDs, or proxy events.
