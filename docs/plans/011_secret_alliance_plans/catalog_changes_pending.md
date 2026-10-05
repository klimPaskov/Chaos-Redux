# Event 011 Catalog Changes Pending

Disposition: accepted and queued.

Acceptance basis: the parent’s explicit release direction for this task prohibits XLSX/CSV edits and directs the owner to leave a Markdown pending record.

The accepted Event 011 catalog entry needs to reflect the final release status and the current decision-cost summary after the cost and localisation audit is complete. During that later authorized workbook pass, check whether any catalog field mirrors the opening report title `chaosx.nr11.3.t` and synchronize it if the field exists.

The catalog workbook remains the source of truth, and no export CSV was edited in this task.

Queued work: update the Event 011 row in `docs/spreadsheets/chaos_redux_events_catalog.xlsx` and run `.tools/export_event_catalog_csv.py` in a later authorized spreadsheet task.

Pending wording should describe the paid Event 011 decisions as four-resource maximum bundles, with up to three costs in the inline row and the complete bundle on hover.
