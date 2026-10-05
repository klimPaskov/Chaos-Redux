# Event 002 catalog update pending

The parent task forbids XLSX and CSV writes in this QA pass, so `docs/spreadsheets/chaos_redux_events_catalog.xlsx` and its generated CSV exports were not edited.

The existing catalog source needs a parent-owned review for any event-facing text fields that mirror the Event 002 news surface. The outbreak event's primary display title remains “Zombie Outbreak”; the revised `chaosx.news.3` world-report title is “Zombie Outbreak Spreads” and its description includes the count of successful new zombie-held states available when the once-only report opens. The main super-event title is “The Dead Have Risen”; its quote and button are not event-detail copy.

If the workbook needs a corresponding event-detail or scenario-field change, the parent should update the workbook and then run `python .tools/export_event_catalog_csv.py` from the mod root. Do not edit the export-only CSVs directly.