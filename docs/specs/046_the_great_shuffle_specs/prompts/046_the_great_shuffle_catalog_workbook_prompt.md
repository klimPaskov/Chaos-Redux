# Event 046 catalog workbook prompt

Use `chaosx_spreadsheet_doc_worker` only after implementation and final player-facing localisation are available.

Read the spreadsheet skill, `docs/spreadsheets/chaos_redux_events_catalog.xlsx`, final Event 046 localisation, Event Details text, evolution text, cluster text, and the Event 46 catalog section in Part 6.

Do not read broad wiki or vanilla files for this bounded workbook task.

Do not edit gameplay, localisation, docs, assets, or any CSV directly.

## Event 46 row

Update ID `46` from **Seismic Archive** to **The Great Shuffle**.

Set:

- Type: Minor Repeatable
- Chaos level: `1`
- Cluster relationship: Randomizations
- Member severity for Randomizations: Medium
- Status: Needs Testing only after source implementation and required non-live validation, otherwise To Be Reworked

Mirror the final Event Details premise and each of the five evolution descriptions.

Do not list raw ranges, family weights, protected registries, source file names, or implementation history.

Leave the world-end field empty.

Never assign Playable without explicit user approval.

## Randomizations cluster

Randomizations is already cluster 14 in the workbook with Event 46 as its Medium member; keep that row and update its details only if the final wording changes.

## Other rows

Leave Domestic Unrest, multi-cluster rows, Event 2, and Event 43 to their owners; this package changes none of them.

## Save and export

Preserve workbook structure, formatting, formulas, filters, validation, and unrelated rows.

After a successful workbook save, run `python .tools/export_event_catalog_csv.py` from the mod root.

Verify that the Events, Clusters, and Scenarios CSV exports are regenerated and structurally valid.

The CSVs are export-only.

In the handoff list exact rows and fields changed, any multi-membership structure change, exporter result, and unresolved catalog conflict.
