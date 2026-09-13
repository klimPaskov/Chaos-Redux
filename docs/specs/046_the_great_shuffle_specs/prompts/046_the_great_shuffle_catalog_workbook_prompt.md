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

Add or update the Randomizations cluster as Minor Repeatable, Chaos level 1.

Describe deliberate permanent randomization of existing gameplay state.

Add Event 46 as a Medium member.

Do not assume a numeric cluster ID from the missing value in the current export.

Use the authoritative runtime and workbook allocation supplied by the parent.

## Domestic Unrest cluster

Add or update Domestic Unrest as Minor Repeatable, Chaos level 1.

Add:

- Event 1, Communist Insurgency, Medium
- Event 21, Random Civil War, Low
- Event 31, Random Terror, Medium

Keep Event 21 in Wars as well.

Do not overwrite one membership with another.

When the workbook still has one Cluster ID and one Member Severity field per event, use the parent-approved multi-membership representation and preserve formatting, validation, filters, exporter compatibility, and in-game mapping.

Record any structural workbook change explicitly.

## Existing assignments

Verify Event 2 remains a Severe Diseases member without creating a duplicate.

For Alien Invasions and Event 43, use only the parent-provided resolved runtime facts.

The supplied export conflict names Event 43 Massive flood while the accepted assignment names Monsters from the Deep.

Do not guess.

When final source confirms Monsters from the Deep, align Event 43 as a Severe Alien Invasions member.

Otherwise report the conflict and leave the unresolved row unchanged.

## Save and export

Preserve workbook structure, formatting, formulas, filters, validation, and unrelated rows.

After a successful workbook save, run `python .tools/export_event_catalog_csv.py` from the mod root.

Verify that the Events, Clusters, and Scenarios CSV exports are regenerated and structurally valid.

The CSVs are export-only.

In the handoff list exact rows and fields changed, any multi-membership structure change, exporter result, and unresolved catalog conflict.
