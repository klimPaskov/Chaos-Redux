# Event 013 Spreadsheet Alignment Check

Workbook:
- `docs/spreadsheets/chaos_redux_events_catalog.xlsx`

Changed sheet and cell:
- `Main Sheet`
- Row `8`
- Cell `Y8`
- Scenario `SCN-007`

Change made:
- Replaced stale `SCN-007` detail text with the current in-game wording from `localisation/english/chaosx_gui_l_english.yml`:
  - `The Natural Disasters barrage has begun under the selected type and intensity. Warnings, impact reports, aftermath markers, and recovery tasks will arrive as the sequence moves across eligible regions.`

Readback evidence:
- Event 13 row `14`:
  - `C14` matches `chaosx.events_log.window.event_details.natural_disasters`.
- Natural Disasters cluster row `10`:
  - `Q10` matches `chaosx.events_log.window.cluster_details.description.natural_disasters`.
- Event 46 row `47`:
  - `C47` matches the combined placeholder wording from `localisation/english/046_great_earthquake_l_english.yml` for the dormant catalogue state.
- Scenario `SCN-007` row `8`:
  - `Y8` now matches `chaosx.triggerable_scenarios.7.d`.

Verification:
- Workbook structure remained `1015` rows by `28` columns on `Main Sheet`.
- Freeze panes remained `A3`.
- No other workbook cells were edited in this pass.

Blocked or needs review:
- None in this pass.
