
# Spreadsheet worker prompt for Event 013 Natural Disasters

Use `chaosx_spreadsheet_doc_worker` only after the Event 13 implementation has final in-game localisation for event details, evolution details, cluster details, and scenario details.

Primary workbook:

`docs/spreadsheets/chaos_redux_events_catalog.xlsx`

## Task

Update the Event 13 Natural Disasters row and related Natural Disasters cluster and Disaster Barrage scenario fields so they match final in-game wording.

## Source of truth

Use final in-game localisation and scripted localisation. Do not paraphrase mirror fields.

## Fields to update

- Event ID 13 Details.
- Event ID 13 Evo I.
- Event ID 13 Evo II.
- Event ID 13 Evo III.
- Event ID 13 World-End Scenario.
- Event ID 13 Type.
- Event ID 13 Cluster ID.
- Event ID 13 Member Severity.
- Event ID 13 Status after implementation status is known.
- Natural Disasters cluster details and members.
- Disaster Barrage manual scenario row, using the scenario id implemented by the main agent.

## Required care

- Preserve workbook structure, formatting, formulas, filters, freeze panes, and validation.
- If a final in-game string does not exist yet, mark the cell as blocked or needs user review rather than guessing.
- Report changed sheet, row, column, event id, cluster id, scenario id, and blocked fields.
