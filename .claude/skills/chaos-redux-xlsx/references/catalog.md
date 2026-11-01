# Event catalog

Read the current [spreadsheet README](../../../../docs/spreadsheets/README.md#event-description-and-status-contract) for classification, description, and Legend rules.
The [exporter](../../../../.tools/export_event_catalog_csv.py) owns exported sheets, widths, and serialization; inspect its `SHEET_EXPORTS`, `SHEET_WIDTHS`, and cache check rather than copying a schema into this skill.
`docs/spreadsheets/chaos_redux_events_catalog.xlsx` is authoritative; its three CSV exports are never editable inputs.

## Locate and edit

Discover actual headers and Excel table ranges; worksheet dimensions alone do not define the data extent, and a filter can belong to a table.
Keep legitimate unavailable rows even when descriptions are blank.
Events, Clusters, and Scenarios use their respective ID headers as keys; Cluster Memberships uses `(Cluster ID, Slot)`, allowing repeated Event IDs.
Legend may have a title row above its headers.

Use exact current Event Details, evolution-detail, and cluster-detail localisation from the parent's named sources.
Preserve paragraphs and dynamic meaning when resolving display markup; missing dynamic inputs remain a reported gap.
Use `chaos-redux-events` prose guidance when authoring wording.

- `Details` contains the full description, not an effect list or implementation notes.
- `Evo I` through `Evo V` hold complete implemented evolution descriptions, not selector titles or ordinary baseline stages.
  Overflow stays complete in `Evo V` with titles as separators until an approved schema migration.
- `World-End Scenario` retains every public terminal branch's complete description, separated by titles where needed; preserve the meaning of cross-event links.
- `Scenarios` holds separate manual setup records, not those public terminal branches.

Apply current README status rules only to scoped rows using accepted implementation facts.
Record explicit approval before assigning `Playable`; source checks alone do not establish it.
For Type, Status, Severity, evolution, or World-End presentation, read Legend labels and actual fills and keep dropdown coverage, conditional formatting, and populated-cell fills aligned.

## Membership comparison

For each touched cluster, compare membership rows in Slot order with `Clusters.Members (ID)` and `Clusters.Member Severities`.
Both aggregate sequences must match slot lengths, order, and duplicates exactly; never deduplicate repeated slots or severity entries.
Compare each touched event's distinct cluster set with its comma-separated `Events.Cluster ID` list.
Check names against source wording, including membership display names after a rename, and severity labels against Legend.

## Export verification

Run the exporter after the authoritative save; disposable checks can use `--workbook <candidate>` and `--output-dir <temporary directory>`.
Compare parsed CSV headers, ordered records, full multiline fields, and widths to the corresponding workbook sheets, allowing only the exporter's empty trailing-row trimming and value serialization.
Cluster Memberships and Legend remain workbook-only.
The exporter rejects formula caches exposed as `None`, but cannot prove nonempty caches are fresh or error-free; use [preservation.md](preservation.md#formulas-and-caches) if formulas are present.
