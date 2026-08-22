# Event 006 catalog alignment handoff

Updated `docs/spreadsheets/chaos_redux_events_catalog.xlsx` on the `Events` sheet, row 7, event ID 6 (`Independence Wave`), field `C7` (`Details`).

Replaced the stale pre-release wording about provisional states rising and unsettled pressure with the current post-release event-detail wording from `chaosx.events_log.window.event_details.independence_wave`, including the dynamic rival-bloc placeholders.

Ran `python .tools/export_event_catalog_csv.py` successfully after saving the workbook.

Refreshed export snapshots: `docs/spreadsheets/chaos_redux_events_catalog.csv`, `docs/spreadsheets/chaos_redux_clusters_catalog.csv`, and `docs/spreadsheets/chaos_redux_scenarios_catalog.csv`.

Validation: exported Events row ID 6 is `Independence Wave`, and its `Details` value exactly matches the updated `Events!C7` text.

Blocked or needs_user_review cells: none.
