# Subagent prompt: Event 043 catalog workbook update

You are `chaosx_spreadsheet_doc_worker`.

Update only the authoritative Chaos Redux event catalog workbook for Event 043 with no inherited context.

Read:

- spreadsheet skill
- `docs/spreadsheets/chaos_redux_events_catalog.xlsx`
- `matrices/043_catalog_replacement.md`
- final implemented Event 043 Event Details, evolution details, scenario details, and world-end localisation
- named source files supplied by the parent

Do not read broad wiki or vanilla material.

## Required workbook changes

- replace old Massive Flood Event 43 row
- set Major type
- set Chaos level 3
- leave cluster and member severity empty
- mirror final player-facing Event Details premise
- add two evolution fields
- add one Cthulhu world-end field
- add the verified free manual scenario row
- record Warring Titans and Pact of the Deep
- record Low, Medium, High, and Maximum impact text
- set status from implementation evidence only

Preserve workbook formatting, formulas, filters, validation, and structure.

After save, run:

```text
python .tools/export_event_catalog_csv.py
```

Never edit the CSV files directly.

## Deliverable

Report workbook path, changed sheets and rows, mirrored localisation keys, exporter result, and blockers. If export fails, report it and do not manually patch CSVs.
