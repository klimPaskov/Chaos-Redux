# Spreadsheet sources and exports

This directory contains the editable event catalog workbook, its generated catalog snapshots, and the separate doctrine workbook.

## Source and export rules

- [`chaos_redux_events_catalog.xlsx`](chaos_redux_events_catalog.xlsx) is the only editable source for the event catalog.
- [`chaos_redux_events_catalog.csv`](chaos_redux_events_catalog.csv), [`chaos_redux_clusters_catalog.csv`](chaos_redux_clusters_catalog.csv), and [`chaos_redux_scenarios_catalog.csv`](chaos_redux_scenarios_catalog.csv) are generated exports and must not be edited directly.
- [`doctrines.xlsx`](doctrines.xlsx) is a separate doctrine workbook and is not an event-catalog export.
- Run `python .tools/export_event_catalog_csv.py` from the mod root after an accepted event-catalog workbook update.

The workbook remains the catalog authority for event, cluster, and scenario rows, while player-facing wording must stay aligned with the current localisation and event-log documentation.
