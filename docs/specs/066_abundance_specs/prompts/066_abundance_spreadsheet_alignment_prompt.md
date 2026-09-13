# Event 066 Abundance Spreadsheet Alignment Prompt

Use `chaosx_spreadsheet_doc_worker` with `fork_context=false` only after the Event 66 implementation and final player-facing localisation are available.

## Required reading

Read:

- the spreadsheet skill
- `docs/spreadsheets/chaos_redux_events_catalog.xlsx`
- final Event 66 event name, Event Details, evolution details, and cluster details localisation
- `docs/specs/066_abundance_specs/research/066_abundance_catalog_crosswalk.md`
- the exact source files named by the parent

Do not read or edit unrelated gameplay files.
Do not edit documentation or localisation.

## Events sheet

Update the row with ID `66`.
Replace the old `CIC` identity and random-major international-market description.

Required fields:

- Event Name: match final in-game name, `Abundance`
- Details: match final Event Details premise wording
- Evolution I: match final Strange Abundance detail wording
- Evolution II: match final Abundance Comes in Pairs detail wording
- Evolution III: match final Everything in Excess detail wording
- Evolution IV and V: blank
- Type: `Minor Repeatable`
- Chaos level: `1`
- Cluster ID: verified Sudden Abundance ID
- Member Severity: preserve Low, Medium, and High without collapsing the three logical roles
- Status: use the implementation status supplied by the parent and supported by evidence

Keep player-facing cells free of implementation terms, raw weights, provider IDs, debug state, and source-history notes.

## Clusters sheet

Create or update Sudden Abundance using the verified cluster ID.
ID `9` is only a provisional planning value until the runtime registry and workbook prove it is free.

The member list must contain three ordered Event 66 entries for Low, Medium, and High.
It must also include Event 64 Border Fortifications and every other accepted member supplied by the parent.
Do not guess the complete cluster membership from the Event 66 spec alone.

Cluster details should explain the shared abundance theme and the role of severity without exposing coalescing variables or internal probability formulas.
Set Type, Chaos level, and Status from verified implementation facts.

## Workbook integrity

Preserve workbook structure, formatting, formulas, filters, validation, conditional formatting, and Legend-driven colors.
Use the established multi-value representation for cluster and severity cells.
Do not create a second workbook.

## Export

After saving the authoritative workbook, run:

```text
python .tools/export_event_catalog_csv.py
```

The exporter must regenerate:

- `chaos_redux_events_catalog.csv`
- `chaos_redux_clusters_catalog.csv`
- `chaos_redux_scenarios_catalog.csv`

Never edit those CSV files directly.
If export fails, report the failure and do not claim catalog alignment is complete.

## Handoff

Report the workbook path, sheets and cells changed, final Event 66 row values, final Sudden Abundance row values, preserved formatting and validation, exporter result, generated CSV paths, and any unresolved cluster ID or membership issue.
