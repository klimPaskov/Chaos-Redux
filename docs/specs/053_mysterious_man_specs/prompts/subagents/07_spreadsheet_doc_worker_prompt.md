# Prompt for `chaosx_spreadsheet_doc_worker`

Spawn with `fork_context=false` only after final Event 53 in-game Event Details and evolution wording exists.

Read the spreadsheet skill, the authoritative workbook, the final Event 53 localisation and scripted localisation needed for mirror fields, and:

`docs/specs/053_mysterious_man_specs/catalog/event_053_catalog_alignment.md`

Update only Event ID 53 in:

`docs/spreadsheets/chaos_redux_events_catalog.xlsx`

Preserve workbook structure, formulas, filters, validation, formatting, and freeze panes.

Required row state:

- ID `53`
- Event Name `Mysterious Man`
- Type `Minor Fire-Once`
- Chaos level `1`
- blank Cluster ID
- blank Member Severity
- Details and Evolution I to III mirror final in-game wording
- Evolution IV and V blank
- World-End Scenario blank
- Status `Needs Testing` when complete source implementation evidence exists

Remove the stale scientific-breakthrough Details text.

After saving the workbook, run:

`python .tools/export_event_catalog_csv.py`

Never edit a CSV export directly.

Report workbook path, sheet, row, fields changed, exporter result, and any blocked mirror field.
