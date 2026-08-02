# Event 016 event-catalog alignment handoff

Status: complete for the requested workbook alignment pass.

## Changed files

- `docs/spreadsheets/chaos_redux_events_catalog.xlsx`
- Export-only snapshots refreshed by the mandated exporter:
  - `docs/spreadsheets/chaos_redux_events_catalog.csv`
  - `docs/spreadsheets/chaos_redux_clusters_catalog.csv`
  - `docs/spreadsheets/chaos_redux_scenarios_catalog.csv`

## Exact workbook changes

- Sheet `Events`, row 17, Event ID `16` (`Brilliant Scientist`), cell `C17` (`Details`) now mirrors the current `chaosx.events_log.window.event_details.brilliant_scientist` localisation exactly, including the two-paragraph line break.
- Cells `D17:G17` (`Evo I` through `Evo IV`) were audited against the four current `brilliant_scientist.evolution.*.title` and `.desc` localisation pairs and already matched exactly.
- `H17` (`Evo V`) remains blank.
- `I17` (`World-End Scenario`) was audited against the current `Laboratory World` and `The Strategic Singularity` Event Details title/details strings and already matched exactly.
- `J17` remains `Minor Fire-Once`.
- `K17` (cluster) and `L17` (member severity) remain blank.
- `M17` remains `Partially Available`, which is an allowed catalog status and matches the current bounded package status.
- Row 177 remains `Crazy Scientist (absorbed into Event 016)` with `Unavailable` status. No standalone event row was recreated.

## Export evidence

Ran from the mod root:

```text
python .tools/export_event_catalog_csv.py
```

Exporter returned `status: success` and refreshed 183 Events rows, 14 Clusters rows, and 13 Scenarios rows. The Events export contains the updated Event 016 details and the absorbed Crazy Scientist row.

## Remaining risks

- No gameplay, localisation, or event-source files were modified.
- The catalog continues to mark Event 016 as `Partially Available`; broader content, live acceptance, and Event 016-specific 3D packages remain outside this workbook-only pass.
