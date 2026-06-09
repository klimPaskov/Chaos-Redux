# Event005 evolution spreadsheet parity tranche

## Scope

Parent-side cleanup for Soviet Collapse evolution-detail wording parity.

## Changed files

- `docs/spreadsheets/chaos_redux_events_catalog.xlsx`

## Implementation

Updated the Event005 row evolution-detail cells so the spreadsheet uses the same player-facing milestone names and descriptions as the in-game localisation:

- `First Durable Secession`
- `Regional Cascade`
- `Union Unmade`
- `Maximum Rupture`
- `Parallel successor authorities` / `Fringe successor authorities`

The spreadsheet no longer labels the Event005 secession stages as `Gathering Storm`, `Rising Chaos`, `Chaos Tier`, or `Terminal Rupture`.

## Validation

- Read `docs/spreadsheets/chaos_redux_events_catalog.xlsx` as XLSX XML and verified `zip_test None`.
- Compared the updated workbook shared strings against:
  - `chaosx.events_log.window.evolution_details.soviet_collapse_secession.body.stage_1`
  - `chaosx.events_log.window.evolution_details.soviet_collapse_secession.body.stage_2`
  - `chaosx.events_log.window.evolution_details.soviet_collapse_secession.body.stage_3`
  - `chaosx.events_log.window.evolution_details.soviet_collapse_secession.body.stage_4`
  - `chaosx.events_log.window.evolution_details.soviet_collapse_high_chaos.body.event_detail`

## Remaining risks

- This tranche does not change event-log registration logic or scripted-localisation routing. It only aligns the spreadsheet descriptions with the existing in-game wording.
