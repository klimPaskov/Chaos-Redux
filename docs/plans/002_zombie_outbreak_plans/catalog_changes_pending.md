# Event 002 catalog update pending

The parent task forbids XLSX and CSV writes in this QA pass, so `docs/spreadsheets/chaos_redux_events_catalog.xlsx` and its generated CSV exports were not edited.

The existing catalog source needs a parent-owned review for any event-facing text fields that mirror the Event 002 news surface. The outbreak event's primary display title remains “Zombie Outbreak”; the revised `chaosx.news.3` world-report title is “Zombie Outbreak Spreads” and its description includes the count of successful new zombie-held states available when the once-only report opens. The main super-event title is “The Dead Have Risen”; its quote and button are not event-detail copy.

If the workbook needs a corresponding event-detail or scenario-field change, the parent should update the workbook and then run `python .tools/export_event_catalog_csv.py` from the mod root. Do not edit the export-only CSVs directly.
## Release-QA queue, 2026-10-06

Disposition: accepted and queued under the user's explicit prohibition of workbook and CSV edits in this release pass.
Current evidence is `release_qa_completion_20261006.md`; the installed 12 portraits/seven category crops do not authorize a Playable status, and the corrected cure-panel source/evidence commit 275fa0e9 does not clear remaining model/Hannibal and multi-slot tooltip gates or authorize Playable status.
Older row observations remain historical until the catalog owner verifies the workbook.
Keep status `Needs Testing` until explicit user approval authorizes another status.
Copy current in-game Event Details and evolution/scenario wording; super-event quotation/button text and debug rejection prose are not event details.
Any catalog field that actually mirrors cure timing or martial-law scope must follow the corrected current source: League membership/investment can shorten research, and martial law prevents new rear-area outbreaks rather than halting established fronts.
The six shared description corrections are implemented in `978c7b5d5745cc00058e136a88b8c068ebe00b94`; this queued workbook alignment does not reopen that source wording issue or establish mechanical/GUI validation.
Any eventual workbook save requires `python .tools/export_event_catalog_csv.py`; export-only CSV files remain unedited directly.

## Release pass 2026-10-11
The world-report text of `chaosx.news.3` changed: its description now reads "The horde now holds [one state name, or N new states, among them the first]. Infected travelers can carry the disease farther along roads and through ports."
The title "Zombie Outbreak Spreads" is unchanged.
The Anti-Zombie League invitation `chaosx.nr2.7` now names the League leader's adjective, and the `chaosx.nr2.14` and `chaosx.nr2.15` descriptions are shorter.
None of these are Event Details text, so no workbook field depends on them unless the catalog mirrors the news surface.
