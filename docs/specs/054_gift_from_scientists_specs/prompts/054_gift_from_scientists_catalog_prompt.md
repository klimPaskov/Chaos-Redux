# Event 54 Catalog Prompt

Use `chaosx_spreadsheet_doc_worker` only after Event 54 implementation, final localization, and completion findings are available.

Read the spreadsheet skill, the authoritative workbook at `docs/spreadsheets/chaos_redux_events_catalog.xlsx`, the Event 54 catalog handoff, and only the final Event 54 and Scientific Research localization needed to mirror player-facing text.

## Event 54 row

Update ID 54 with:

- final name from in-game localization
- Minor Repeatable type
- Chaos level 1
- Scientific Research membership with Medium severity
- final Event Details premise text
- final evolution premise text for Multiple Breakthroughs, Accelerated Discovery, and Scientific Deluge
- implementation-derived status

Remove the stale infrastructure-boom description.

## Scientific Research cluster row

Use the stable runtime ID confirmed by implementation. Do not assign proposed ID 9 when the repository already reserves another identity.

Set:

- name Scientific Research
- Minor Repeatable type
- Chaos level 2
- final cluster premise text
- members 16, 24, 27, 54, and 60
- implementation-derived status

Preserve member-specific severities in the workbook's normalized membership source when the workbook structure supports it. Preserve Event 27's second Medium membership in Military Preparation. Do not collapse many-to-many membership into one Event 27 cluster cell when the normalized source exists.

## Save and export

Preserve workbook sheets, formulas, formatting, filters, validation, and unrelated rows.

Save the workbook, then run `python .tools/export_event_catalog_csv.py` from the mod root. Do not edit the generated CSVs directly.

Report the workbook path, changed rows and fields, exporter result, generated files, and any mismatch between runtime localization and workbook structure.
