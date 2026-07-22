# Fallout workbook ownership correction

## Workbook change

- Workbook: `docs/spreadsheets/chaos_redux_events_catalog.xlsx`
- Sheet: `Events`
- Row: 3, Event ID 2, `Zombie Outbreak`
- Cell: `I3`, `World-End Scenario`
- Before: the valid `Zombie Apocalypse` block was followed by an appended `Fallout` section beginning `War and contamination have poisoned the air beyond recovery.`
- After: the `Zombie Apocalypse` block is retained exactly and the appended `Fallout` section is removed.
- No Fallout event row was added.

## Scenario check

The `Scenarios` sheet still contains `SCN-001` through `SCN-010` and `SCN-013` only. The highest live scenario ID remains 13. `SCN-014` was not added because the exact manual province sweep remains unproven.

## Export

Ran `python .tools/export_event_catalog_csv.py` from the mod root successfully. The exporter refreshed all three export-only snapshots:

- `chaos_redux_events_catalog.csv`, 1015 rows, 13 columns
- `chaos_redux_clusters_catalog.csv`, 13 rows, 7 columns
- `chaos_redux_scenarios_catalog.csv`, 12 rows, 6 columns

## Remaining blocker

The exact manual province sweep for a Fallout scenario remains unproven, so no `SCN-014` catalog row was created.
