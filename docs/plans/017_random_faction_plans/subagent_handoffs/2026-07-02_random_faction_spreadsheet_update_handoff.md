# Event 017 Random Faction Spreadsheet Update Handoff

## Scope

Updated `docs/spreadsheets/chaos_redux_events_catalog.xlsx` after the localisation audit changed the in-game Event Details and Evolution III wording.

## Changed Workbook Surface

- Workbook: `docs/spreadsheets/chaos_redux_events_catalog.xlsx`
- Sheet: `Events`
- Excel row: `18`
- Event ID: `17`

## Changed Cells

- `Details`: refreshed to mirror `chaosx.events_log.window.event_details.random_faction`.
- `Evo III`: refreshed to mirror `chaosx.events_log.window.evolution_details.random_faction.body.stage_3`, keeping the catalog's `Neutrality Collapse:` title-prefix style.

## Checked and Left Unchanged

- `Event Name`: `Random faction`
- `Type`: `Minor Repeatable`
- `Cluster ID`: `3`
- `Member Severity`: `Low`
- `Status`: `Implemented`
- `Evo I`
- `Evo II`

## Validation

- Re-read Event ID `17` from the saved workbook and confirmed the updated `Details` and `Evo III` values.
- Confirmed workbook sheets remained `Events`, `Clusters`, `Scenarios`, `Info`, and `Legend`.

Blocked cells: none.
