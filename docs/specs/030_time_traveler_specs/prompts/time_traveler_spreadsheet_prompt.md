# Event 030 Spreadsheet Prompt

You are `chaosx_spreadsheet_doc_worker`. Update only `docs/spreadsheets/chaos_redux_events_catalog.xlsx` after implementation facts and final in-game wording exist.

Read the spreadsheet skill, the workbook, Event 030 final localisation and scripted localisation, the final Event 030 docs, and the implemented triggerable scenario wording. Do not read unrelated repo systems and do not edit gameplay, localisation, docs, assets, or CSV files.

Replace the legacy Event 30 row with final player-facing fields for:

- baseline premise
- Evolutions I through V
- Machine Extinction War
- Major classification
- Chaos level `1`
- no cluster
- final implementation status

Add or update the final All Times at Once scenario row under the collision-checked scenario ID with its one type, four intensity descriptions, and final status.

Match Event Details, evolution detail, world-end detail, scenario detail, and in-game wording. Do not paste mechanics tables, hidden thresholds, raw effects, working labels, or implementation notes into the workbook.

Preserve workbook structure, formulas, formatting, filters, and validation. After saving, run `python .tools/export_event_catalog_csv.py`. Report exporter failure and do not edit the three CSV exports manually.
