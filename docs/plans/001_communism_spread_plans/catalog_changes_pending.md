# Catalog changes pending for Event 001

Disposition: pending parent review and eventual workbook update by the catalog owner.

- Event 001 overview wording should match `chaosx.nr1.1.d`: “Communist organizers are building networks among workers and soldiers. Strikes and party meetings now challenge governments across the world.”
- The first root choice should match `chaosx.nr1.1.a`: “The government will defend the country against communist revolt.”
- Do not add the forced-event ineligible fallback to the catalog. It explains an administrative test case and is not the event's normal player path.

The workbook was not edited. This note does not replace the catalog source workbook or its required CSV export.
- Other reviewed Event 001 report, evolution, result-option, and Black Friday cost wording changed in localisation. Reconcile any workbook cells that mirror these strings during the final spreadsheet pass; the workbook remains the authoritative catalog source.

## Release-QA queue, 2026-10-06

Disposition: accepted and queued under the user's explicit prohibition of workbook and CSV edits in this release pass.
Current evidence is `release_qa_completion_20261006.md`; older row observations remain historical until the catalog owner verifies the workbook.
Keep status `Needs Testing` until explicit user approval authorizes another status.
Copy current in-game Event Details and evolution/scenario wording; super-event quotation/button text and debug rejection prose are not event details.
Any eventual workbook save requires `python .tools/export_event_catalog_csv.py`; export-only CSV files remain unedited directly.
