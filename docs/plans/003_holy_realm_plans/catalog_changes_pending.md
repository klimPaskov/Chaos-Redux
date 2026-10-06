# Event003 Catalog Changes Pending

The event catalog workbook and export CSV files were not edited in this QA pass, as requested.

The Event003 game Event Details string in `localisation/english/003_the_holy_realm_l_english.yml` was revised to describe the Holy Realm's Himalayan refuge, the Bodhisattva's governing vows, and the pressure on the Mandala. The existing authoritative workbook row `Events!A4:M4` has different wording in `C4` and remains status `Needs Testing` in `M4`.

After the parent accepts the final Event Details wording, the workbook owner should update only the Event003 row in `docs/spreadsheets/chaos_redux_events_catalog.xlsx`, then run `python .tools/export_event_catalog_csv.py` from the mod root. The three export-only CSV files must not be edited directly.

No spreadsheet export was run because there was no workbook update.

## Release-QA queue, 2026-10-06

Disposition: accepted and queued under the user's explicit prohibition of workbook and CSV edits in this release pass.
Current evidence is `release_qa_completion_20261006.md`; older row observations remain historical until the catalog owner verifies the workbook.
Keep status `Needs Testing` until explicit user approval authorizes another status.
Copy current in-game Event Details and evolution/scenario wording; super-event quotation/button text and debug rejection prose are not event details.
Any eventual workbook save requires `python .tools/export_event_catalog_csv.py`; export-only CSV files remain unedited directly.
