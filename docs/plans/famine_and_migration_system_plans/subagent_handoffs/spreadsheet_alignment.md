# Famine and Migration Spreadsheet Alignment

## Changed workbook

- Workbook: `docs/spreadsheets/chaos_redux_events_catalog.xlsx`
- Sheet: `Events`
- Row: 150, catalog ID `149`
- Changed column: `C` (`Details`)
- Previous details: `A migration crisis drains people from a random major country or the player toward neighboring states. Stability and living conditions shape the severity of the loss.`
- Final details: `Retired and absorbed into the shared dynamic famine and migration system. Unavailable as a random event.`
- Preserved `Event Name` as `Immigrations` and `Status` as `Unavailable`.

No system event row or replacement event ID was added. No cluster or scenario row was changed. The implementation owns exactly `famine_state_map_mode` and `migration_state_map_mode`; no mapmode or random-event catalog row was added.

## Export result

Ran `python .tools/export_event_catalog_csv.py` from the mod root successfully.

- `docs/spreadsheets/chaos_redux_events_catalog.csv`: 183 rows, 14 columns, SHA-256 `25e79832048b3ffbf2ee2a0746a3e1717e5db248be188ce8d2f081a2e71fbe29`
- `docs/spreadsheets/chaos_redux_clusters_catalog.csv`: 14 rows, 7 columns, SHA-256 `0bdd2e73f4c556af5fbdb028a2bbae258ef4d3402450d4bb112a63644047d299`
- `docs/spreadsheets/chaos_redux_scenarios_catalog.csv`: 12 rows, 6 columns, SHA-256 `8d31d120dd81adb3ef48bae2afed8cf539bb4f23a60b04771c1eacc57875a398`

The exported Event149 row is line 311 and contains the retirement wording above with `Unavailable` status.

## Validation and blockers

Workbook validation confirmed all five sheets, existing table ranges, data validations, cell styles, and zero formulas remain intact. There are no spreadsheet blockers for this alignment. Broader runtime probability and mapmode-render evidence remains parent-owned and was not changed by this workbook-only task.
