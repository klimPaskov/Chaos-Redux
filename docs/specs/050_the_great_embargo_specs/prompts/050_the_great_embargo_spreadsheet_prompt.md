# Event 050 spreadsheet prompt

Update the authoritative Chaos Redux event catalog workbook after Event 50 implementation and final localisation are complete.

Read only the spreadsheet skill, `docs/spreadsheets/chaos_redux_events_catalog.xlsx`, final Event 50 localisation and Event Details wording, final evolution wording, final cluster registry facts, and the Event 50 source-conflict ledger.

## Required Event 50 row

Preserve:

- ID `50`
- The Great Embargo
- Minor Repeatable
- Chaos level 1
- Negative Economy cluster
- Medium member severity

Replace the one-line rough detail with the final player-facing Event Details premise. Add final Evolution I and Evolution II detail fields that match in-game wording.

## Cluster reconciliation

The supplied CSV has an incomplete Negative Economy row with no ID and conflicting type, Chaos level, and availability. Do not guess.

Read the final authoritative cluster implementation and update the workbook only from verified facts. If the cluster remains unimplemented, preserve Event 50's accepted design relationship in the event row only where the workbook schema permits it and report the unresolved cluster fields.

## Workbook rules

Preserve formatting, validation, filters, formulas, and sheet structure. Do not edit the three CSV exports directly.

After saving the XLSX, run:

`python .tools/export_event_catalog_csv.py`

Confirm that the Events, Clusters, and Scenarios CSV snapshots were regenerated. If export fails, report the failure and do not hand-edit a CSV.

## Handoff

List workbook path, sheets and cells changed, final copied localisation sources, export result, and unresolved cluster facts.
