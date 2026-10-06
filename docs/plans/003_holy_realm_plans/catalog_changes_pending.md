# Event003 Catalog Changes Pending

The event catalog workbook and export CSV files were not edited in this QA pass, as requested.

The Event003 game Event Details string in `localisation/english/003_the_holy_realm_l_english.yml` was revised to describe the Holy Realm's Himalayan refuge, the Bodhisattva's governing vows, and the pressure on the Mandala. The existing authoritative workbook row `Events!A4:M4` has different wording in `C4` and remains status `Needs Testing` in `M4`.

After the parent accepts the final Event Details wording, the workbook owner should update only the Event003 row in `docs/spreadsheets/chaos_redux_events_catalog.xlsx`, then run `python .tools/export_event_catalog_csv.py` from the mod root. The three export-only CSV files must not be edited directly.

No spreadsheet export was run because there was no workbook update.

## Release-QA queue, 2026-10-06

Disposition: accepted and queued under the user's explicit prohibition of workbook and CSV edits in this release pass.
Current evidence is `release_qa_completion_20261006.md`; any copied action wording must reflect the five removed flat manpower grants and one-time Open Roads, preserving the actual peacekeeping resource return.
The 47-action filters, installed 12 portraits and position-only layout commit do not authorize Playable status; final D584 native layout is cleared but probability/native-gameplay and broader design acceptance remain open; the parent-approved seven shortcuts, above 600 High Passes authorization and installed filter icons may be described as source-applied, while the explicit 6+3 presentation simplification and cleared layout evidence and remaining matrix/AI/native-gameplay limits remain visible.
Any Storehouses wording must describe the current national supply-hub/CP/Reach/conditional-Cohesion reward and omit the removed free compact-member infrastructure promise.
Older row observations remain historical until the catalog owner verifies the workbook.
Keep status `Needs Testing` until explicit user approval authorizes another status.
Copy current in-game Event Details and evolution/scenario wording; super-event quotation/button text and debug rejection prose are not event details.
Any eventual workbook save requires `python .tools/export_event_catalog_csv.py`; export-only CSV files remain unedited directly.

The final focus implementation is `08a32875eb5e693d52903b0cd88fb35a0d809b1e`: 111 preserved focuses, seven navigation shortcuts, visible milestone requirements and High Pass force authorization above Chaos 600.
Storehouses wording must describe the national hub/Command Power/Reach/conditional Cohesion reward without promising foreign infrastructure.
Catalog status remains Needs Testing; no workbook or exported CSV was edited.
