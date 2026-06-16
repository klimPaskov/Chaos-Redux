# Event 013 Spreadsheet Handoff

Workbook:
- `docs/spreadsheets/chaos_redux_events_catalog.xlsx`

Rows touched:
- Event 013 Natural Disasters catalogue row.
- Natural Disasters event-log/detail/evolution/cluster fields.
- Event 046 catalogue row, reduced to an unknown placeholder.

Result:
- The spreadsheet worker updated the Event 013 catalogue/detail/evolution/cluster data from the implemented files and marked Event 046 as an inactive unknown placeholder.
- The worker found a duplicate Natural Disasters cluster surface on row 11 and marked it for review.
- The main implementation cleared the duplicate row 11 cluster columns so the Natural Disasters cluster remains represented by Event 013 only.

Follow-up status:
- Workbook dimensions, freeze panes, and formula count were preserved after the worker pass.
- The main implementation should re-read the workbook after the final Event 013 wording updates and keep the row text aligned with in-game localisation and docs.
