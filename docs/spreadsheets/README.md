# Spreadsheet sources and exports

This directory contains the editable event catalog workbook, its generated catalog snapshots, and the separate doctrine workbook.

## Source and export rules

- [`chaos_redux_events_catalog.xlsx`](chaos_redux_events_catalog.xlsx) is the only editable source for the event catalog.
- [`chaos_redux_events_catalog.csv`](chaos_redux_events_catalog.csv), [`chaos_redux_clusters_catalog.csv`](chaos_redux_clusters_catalog.csv), and [`chaos_redux_scenarios_catalog.csv`](chaos_redux_scenarios_catalog.csv) are generated exports and must not be edited directly.
- [`doctrines.xlsx`](doctrines.xlsx) is a separate doctrine workbook and is not an event-catalog export.
- Run `python .tools/export_event_catalog_csv.py` from the mod root after an accepted event-catalog workbook update.

The workbook remains the catalog authority for event, cluster, and scenario rows, while player-facing wording must stay aligned with the current localisation and event-log documentation.

## Event description and status contract

- `Evo I` through `Evo V` store the complete player-facing description for each implemented evolution stage. Evolution titles remain separate in the in-game Event Details selectors and must not replace these descriptions.
- When an event exposes more than five distinct evolution-detail rows, preserve every complete overflow entry in `Evo V` with its title as a separator until an explicit workbook-schema migration is approved. Do not add a column or discard the extra description during routine alignment work.
- `World-End Scenario` stores the complete player-facing description for every public terminal branch owned by the event. When one event owns several branches, the cell may retain each scenario title as a separator, but every title must be followed by its full description.
- The only valid status labels are `Playable`, `Partially Available`, `To Be Reworked`, `Unavailable`, and `Needs Testing`.
- `Playable` requires explicit approval and is never assigned as a default.
- `Partially Available` records a usable catalog row with material unavailable, blocked, or incomplete content; it is not a playable approval.
- Events 1 through 20 use `Needs Testing` until their current implementation has been approved as playable.
- Events above Event 20 with an actual `chaosx.nr<ID>.1` root definition use `To Be Reworked` until their replacement implementation is approved.
- Event IDs without an actual `chaosx.nr<ID>.1` root definition use `Unavailable`.
- The `Legend` sheet is the source for valid dropdown values and the fill colors assigned to Type, Status, Member Severity, evolution, and World-End cells. Data validation, conditional formatting, and populated-cell fills must remain synchronized with it.
- Catalog status does not change runtime registration or default enablement.
