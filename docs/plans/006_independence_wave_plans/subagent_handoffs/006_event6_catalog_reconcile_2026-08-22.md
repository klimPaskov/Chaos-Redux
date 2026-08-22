# Event 006 catalog reconciliation — 2026-08-22

- Workbook: `docs/spreadsheets/chaos_redux_events_catalog.xlsx`
- Cell checked: `Events!C7` (Event ID `6`, `Independence Wave`).
- Result: the existing cell already exactly matches the active localisation key `chaosx.events_log.window.event_details.independence_wave` after normalizing the localisation `\n` escapes to workbook line breaks. It begins `New governments have taken control...`; no concurrent workbook content was reverted or rewritten.
- Export command: `python .tools/export_event_catalog_csv.py` completed with `status: success`.
- Refreshed outputs: `docs/spreadsheets/chaos_redux_events_catalog.csv` (183 rows, 14 columns), `docs/spreadsheets/chaos_redux_clusters_catalog.csv` (14 rows, 7 columns), and `docs/spreadsheets/chaos_redux_scenarios_catalog.csv` (12 rows, 6 columns).
- Checks: workbook `Events!A7` is `6`, `Events!B7` is `Independence Wave`, and `Events!C7` matched localisation exactly. No blocked or `needs_user_review` cells identified.
