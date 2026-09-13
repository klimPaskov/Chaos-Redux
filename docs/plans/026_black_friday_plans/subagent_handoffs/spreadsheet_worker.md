# Event 26 spreadsheet worker handoff

Audit date: 2026-08-30.

The authoritative workbook `docs/spreadsheets/chaos_redux_events_catalog.xlsx` was updated directly. The Events sheet row for ID 26 now describes Black Friday, the Friday reservation and one-day sale, and Evolution I's 75-percent snapshot. The duplicate no-ID Black Friday backlog row was removed. The row retains Minor Fire-Once classification, no cluster assignment, and `Needs Testing` status.

The exported files `docs/spreadsheets/chaos_redux_events_catalog.csv`, `docs/spreadsheets/chaos_redux_clusters_catalog.csv`, and `docs/spreadsheets/chaos_redux_scenarios_catalog.csv` were regenerated with `python .tools/export_event_catalog_csv.py`. No CSV was edited directly.

The workbook details and Evolution I wording were checked against the current Event 26 localisation. The row remains pending live validation because the cost-family registry and Part 8 owner/payment evidence are incomplete.
