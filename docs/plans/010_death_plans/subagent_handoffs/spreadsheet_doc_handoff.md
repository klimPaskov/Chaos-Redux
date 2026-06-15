# Spreadsheet Doc Handoff - Event 010 Death

Workbook updated in place:
`docs/spreadsheets/chaos_redux_events_catalog.xlsx`

## Scope

- Audited Event `010` (`Death`) in the main catalog row.
- Audited triggerable scenario `SCN-006` in the manual scenario table.
- Used in-game player-facing localisation as the source of truth for event-detail and evolution-detail wording.

## Result

- Row ID `10` remains `Death`.
- Type remains `Minor Fire-Once`.
- Cluster ID remains blank.
- Member Severity remains blank.
- Status remains `Implemented`.
- `SCN-006 Death` already existed and already included:
  - Type Options: `Quiet Origin, Island Pattern, Mainland Reveal, Last Shores`
  - Intensity Scaling: `Low/Medium/High/Maximum ...`
- No scenario-table edits were needed.

## Changed Cells

Sheet: `Main Sheet`
Row: `11`
Event ID: `10`

- `C11` `Details`
- `D11` `Evo I`
- `E11` `Evo II`
- `F11` `Evo III`
- `G11` `Evo IV`
- `H11` `Evo V`
- `I11` `World-End Scenario`

## Cell Update Summary

- `C11` changed from a compressed paraphrase to the exact current event-detail body from `chaosx.events_log.window.event_details.death`.
- `D11` through `H11` changed from shorter paraphrases to title-plus-body wording aligned with the current in-game evolution-detail text:
  - `First Silence`
  - `Missing Island Reports`
  - `His Name Was Death`
  - `No More Sea`
  - `There Was No Man`
- `I11` changed to world-end wording aligned with the in-game `No More Sea` and final `There Was No Man` evolution-detail text.

## Implementation Evidence For Status

`Implemented` is supported by local implementation evidence:

- Entry event exists: `events/010_death.txt` contains `id = chaosx.nr10.1`.
- Death pulse event exists: `events/010_death.txt` contains `id = chaosx.nr10.10`.
- Triggerable scenario support exists:
  - `localisation/english/chaosx_gui_l_english.yml` contains `chaosx.triggerable_scenarios.6.d`
  - `localisation/english/chaosx_gui_l_english.yml` contains the Death scenario type labels and intensity text
- Event-log detail and evolution-detail localisation exists for Death in `localisation/english/chaosx_gui_l_english.yml`.

## Validation

- Re-opened the workbook after save and confirmed row `11` now contains the updated Event `010` wording.
- Confirmed `SCN-006` still exists in the manual scenario table and still lists the required type options and intensity scaling.
- Confirmed worksheet structure remained intact on save:
  - Freeze pane still `A3`
  - Data validation entries still present: `5`
- No other sheets were edited.

## Risks

- `I11` is aligned to the in-game world-end/final-consumption evolution wording, but the workbook has only one `World-End Scenario` cell for both the Last Shores phase and the terminal consumed-world end state. The current value combines both to avoid inventing new wording or dropping either implemented state.
