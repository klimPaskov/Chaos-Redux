# Event-catalog spreadsheet prompt for Event 016 Brilliant Scientist

Use `chaosx_spreadsheet_doc_worker` only after final in-game Event Details, evolution details, event-log wording, and world-end wording exist. Spawn with `fork_context=false`.

Read:

- The parent prompt with exact Event 16 fields to update.
- The spreadsheet skill.
- `docs/spreadsheets/chaos_redux_events_catalog.xlsx`.
- Only the final Event 16 localisation and scripted localisation needed to mirror player-facing text.

Update the Event 16 row while preserving workbook structure, formatting, formulas, filters, validation, and freeze panes.

Required alignment:

- Name: Brilliant Scientist.
- Type: Minor Fire-Once.
- Details: exact final Event Details wording, with no mechanical effects.
- Four evolution entries that match the in-game evolution details.
- Conditional world-end wording that matches the implemented Laboratory World and Strategic Singularity routes.
- Cluster field remains blank.
- Status becomes Reworked only after implementation and completion audit.
- Any separate unnumbered `Crazy Scientist` row or note is marked according to the accepted absorption or redesign disposition.

Do not guess missing wording. Mark cells blocked or needing review when final in-game text is absent. Do not edit gameplay, localisation, documentation, assets, or other spreadsheets.

Report workbook path, sheet, row, columns, Event 16 fields, and blocked cells.
