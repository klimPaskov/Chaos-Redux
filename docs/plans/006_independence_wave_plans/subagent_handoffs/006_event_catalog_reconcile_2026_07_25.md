# Event 006 catalog reconciliation handoff

- Updated authoritative workbook: `docs/spreadsheets/chaos_redux_events_catalog.xlsx`.
- `Events` row 7 (`ID` 6, Independence Wave): refreshed `Event Name`, `Details`, `Evo I`–`Evo V`, `Type`, `Cluster ID`, `Member Severity`, and `Status` from current in-game localisation. Status remains `In progress`.
- `Clusters` row 3 (`Cluster ID` 2, Liberations): refreshed `Details`, member list, type, chaos level, and status from the Events Log surface. Status remains `In progress`.
- `Scenarios` row 9 (`SCN-008`, Every Banner Rises): refreshed name, sovereign-scatter detail, type options, intensity scaling, and status from current scenario localisation. Status remains `Needs Testing` pending completion evidence.
- Exporter: `python .tools/export_event_catalog_csv.py` completed successfully and refreshed all three export-only CSV snapshots (Events: 241 rows/13 columns; Clusters: 13 rows/7 columns; Scenarios: 12 rows/6 columns).

Remaining blocker: no in-game completion evidence was available, so Event 006 and SCN-008 were not promoted to completion statuses.
