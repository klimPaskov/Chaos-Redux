# Catalog Workbook Update Prompt

Act as `chaosx_spreadsheet_doc_worker` only after Event 051 implementation facts and final player-facing wording exist.

Read:

- spreadsheet skill
- `docs/spreadsheets/chaos_redux_events_catalog.xlsx`
- final Event 051 Event Details, evolution, cluster, and super-event localisation
- `docs/specs/051_heat_wave_specs/23_catalog_and_documentation_alignment.md`

## Required updates

- Event 51 type becomes Minor Repeatable
- Chaos level remains 1
- cluster becomes Natural Disasters
- member severity becomes High
- event premise matches in-game Event Details
- three evolution rows or fields use accepted names and thresholds
- super-event field matches actual implementation
- status reflects implementation evidence, not the existence of specs
- Natural Disasters cluster includes Event 51 once with the live role and minimum tier


Preserve workbook structure, formulas, filters, validation, and formatting.

After saving, run:

`python .tools/export_event_catalog_csv.py`

Do not edit CSV exports directly. Report any exporter failure and leave the workbook as the only attempted source change.
