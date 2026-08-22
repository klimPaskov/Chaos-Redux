# Spreadsheet Event Details Alignment Handoff, 2026-08-22

## Scope

Updated only the Event Details field on the `Events` sheet for catalog Events 1, 2, 7, 9, and 10.

The workbook remains the editable catalog source at `docs/spreadsheets/chaos_redux_events_catalog.xlsx`.

## Changed cells and source keys

| Event ID | Event | Cell and field | Player-facing source key |
| ---: | --- | --- | --- |
| 1 | Communist Insurgency | `Events!C2` — Details | `chaosx.events_log.window.event_details.communism_spread` |
| 2 | Zombie Outbreak | `Events!C3` — Details | `chaosx.events_log.window.event_details.zombie_outbreak` |
| 7 | Fury | `Events!C8` — Details | `chaosx.events_log.window.event_details.fury` |
| 9 | White Peace | `Events!C10` — Details | `chaosx.events_log.window.event_details.white_peace` |
| 10 | Death | `Events!C11` — Details | `chaosx.events_log.window.event_details.death` |

The five cells now use the current concise premise wording from `localisation/english/chaosx_gui_l_english.yml`, with paragraph breaks preserved as in-game detail text.

No evolution, world-end, cluster, scenario, status, identifier, or other catalog fields were changed.

## Files

Changed by this handoff:

- `docs/spreadsheets/chaos_redux_events_catalog.xlsx`
- `docs/spreadsheets/chaos_redux_events_catalog.csv` (export output)
- `docs/plans/repo_cleanup/subagent_handoffs/spreadsheet_cleanup_alignment_2026-08-22.md`

The exporter also regenerated the export-only cluster and scenario snapshots; no worktree diff was reported for those two outputs:

- `docs/spreadsheets/chaos_redux_clusters_catalog.csv`
- `docs/spreadsheets/chaos_redux_scenarios_catalog.csv`

## Validation

Ran from the mod root:

```text
python .tools/export_event_catalog_csv.py
```

Exporter result: `status: success`.

The exporter reported 183 Event rows and 14 columns, 14 Cluster rows and 7 columns, and 12 Scenario rows and 6 columns.

The saved workbook re-opened with the existing five sheets, `Events!A1:N928`, `Clusters!A1:G14`, and `Scenarios!A1:F12` dimensions, existing tables, data-validation counts, conditional-formatting counts, and no formulas.

The five target CSV rows match the five workbook Details cells exactly after export.

## Risks and review notes

The workbook and Event CSV already had unrelated worktree modifications before this bounded update, so they were preserved and not reverted.

The workbook was saved in place with openpyxl while retaining existing workbook structure and target-cell styles; no GUI layout, gameplay, localisation, or Event 21+ content was touched.

No blocked or `needs_user_review` spreadsheet cells were introduced.
