# Event 025 spreadsheet prompt

Spawn `chaosx_spreadsheet_doc_worker` with `fork_context=false` after final in-game wording and implementation facts are stable.

Edit only:

`docs/spreadsheets/chaos_redux_events_catalog.xlsx`

Update Event 25 fields to match the final player-facing Event Details and evolution wording:

- Event name
- Details
- Evolution I through V
- Type Major
- cluster field according to the accepted standalone runtime design
- status according to final implementation and test state

Do not expose hidden reward keys, exact thresholds, sabotage authors, or future surprises.

Preserve workbook structure, formatting, formulas, filters, and validation.

After saving, run:

`python .tools/export_event_catalog_csv.py`

Do not edit any CSV export directly.

Write the handoff to:

`docs/plans/025_alien_technology_in_antarctica_plans/subagent_handoffs/025_spreadsheet_handoff.md`
