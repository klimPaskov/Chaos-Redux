# Event 24 catalog handoff

## Scope

The spreadsheet role aligned the authoritative Event 24 workbook row with the final Event Details and evolution wording after implementation was complete.

## Runtime surfaces

`docs/spreadsheets/chaos_redux_events_catalog.xlsx` is the editable source, with Event 24 on the `Events` sheet row 25.

The Event Details field now matches the final in-game wording, and the Evo I, Evo II, and Evo III fields use the final titles and concrete body text for all three named evolutions.

## Validation

The required exporter was run after the workbook update and regenerated `chaos_redux_events_catalog.csv`, `chaos_redux_clusters_catalog.csv`, and `chaos_redux_scenarios_catalog.csv` from the workbook.

## Remaining risks

The CSV files remain export-only and were not edited directly. Workbook and export staging still requires a final dirty-worktree comparison so unrelated existing catalog changes are not included in the Event 24 commit.
