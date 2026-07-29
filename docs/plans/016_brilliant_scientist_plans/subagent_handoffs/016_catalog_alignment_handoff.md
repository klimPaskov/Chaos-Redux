# Event 016 catalog alignment handoff

Scope: `docs/spreadsheets/chaos_redux_events_catalog.xlsx`, Events sheet only, with the unnumbered `Crazy Scientist` concept row explicitly absorbed as requested.

## Workbook changes

- Event ID `16`, row `17` (`Brilliant Scientist`): set `C` (Details) to exactly match the current in-game localisation key `chaosx.events_log.window.event_details.brilliant_scientist` from `localisation/english/016_brilliant_scientist_evolutions_l_english.yml`.
- Event ID `16`, row `17`: updated `D:G` with the exact four logged evolution title/body pairs from `016_brilliant_scientist_evolutions_l_english.yml`:
  - National Scientific Ascendancy
  - The International Scientific Contest
  - Forbidden and Autonomous Science
  - Sovereign Science
- Event ID `16`, row `17`: kept `H` (`Evo V`) blank because exactly four evolutions are logged.
- Event ID `16`, row `17`: updated `I` with the in-game Event Log world-end detail wording for `Laboratory World` and `The Strategic Singularity`, including the shared Fallout pipeline.
- Event ID `16`, row `17`: preserved `J = Minor Fire-Once`, left `K` (cluster) and `L` (severity) blank, and set `M = In progress` to reflect a core-ready package without claiming every planned scenario/flavor/3D surface is complete.
- Former blank concept row `177`: renamed `Crazy Scientist (absorbed into Event 016)` and recorded that its standalone concept is absorbed/superseded by the Kruger Directorate package; no other rows were changed.

## Export

After saving the XLSX, ran `python .tools/export_event_catalog_csv.py` from the mod root successfully. The exporter refreshed all three snapshots:

- `docs/spreadsheets/chaos_redux_events_catalog.csv` - 259 rows, 13 columns (SHA-256 `49a949263132245c02997962ee95667d334d20718a3bb64deef9848b1c2a7080`)
- `docs/spreadsheets/chaos_redux_clusters_catalog.csv` - 13 rows, 7 columns
- `docs/spreadsheets/chaos_redux_scenarios_catalog.csv` - 12 rows, 6 columns

## Remaining risks

- The catalog status remains `In progress`; this alignment does not claim completion of any broader Event 016 scenario, flavor, asset, or live-game QA work outside the catalog.
- No Event 016 cluster exists, so the cluster field remains intentionally blank.
