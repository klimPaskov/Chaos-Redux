# Event 006 catalog wording alignment — 2026-08-03

## Scope

Updated only the editable event catalog workbook and refreshed its three export-only CSV snapshots. The alignment is limited to player-facing wording for Event 006 / SCN-008; it does not promote implementation status or assert the 14/20 admission-capacity target.

## Workbook changes

Workbook: `docs/spreadsheets/chaos_redux_events_catalog.xlsx`

- `Events!C7` — replaced the stale event-detail text and scripted-localisation suffix with the current static event-detail wording from `localisation/english/chaosx_gui_l_english.yml`, key `chaosx.events_log.window.event_details.independence_wave`.
- `Events!F7` — aligned Evolution III title/body with `localisation/english/006_independence_wave_evolutions_l_english.yml`, keys `independence_wave.evolution.3.title` and `.body`.
- `Events!G7` — aligned Evolution IV title/body with the same source, keys `independence_wave.evolution.4.title` and `.body`.
- `Scenarios!C9` — aligned SCN-008 Sovereign Scatter details with `localisation/english/006_independence_wave_scenario_l_english.yml`, key `chaosx.scenarios.independence_wave.desc.sovereign_scatter`.
- `Scenarios!E9` — replaced the condensed intensity summary with the four source impact strings (`low`, `medium`, `high`, `maximum`) from the same scenario localisation file, labelled by intensity and separated into readable paragraphs.

No other workbook cells were changed. `Clusters!C3` and the already-current Event 006 titles/bodies were left unchanged.

## Status and capacity boundary

`Events!M7` remains `Partially Available`, `Clusters!G3` remains `Partially Available`, and `Scenarios!F9` remains `Playable`. These values were not changed because the current workbook validation/legend schema permits only `Playable`, `Partially Available`, and `Unavailable`, while the latest conservative completion evidence uses `In progress` / `Needs Testing` terminology. Resolving that schema contradiction is outside this wording-only spreadsheet scope. This handoff makes no claim that Event 006 is fully playable and makes no claim that 14/20 bands are admitted; fail-closed capacity behavior remains an implementation concern.

## Export

Ran from the mod root after saving the workbook:

```text
python .tools/export_event_catalog_csv.py
```

Exporter result: success.

- `docs/spreadsheets/chaos_redux_events_catalog.csv` — 183 rows, 13 columns, SHA-256 `0b3d3b9ba9e3c5c83f19f18e546a390495720a24aa402c84c230286403e972fd`.
- `docs/spreadsheets/chaos_redux_clusters_catalog.csv` — 14 rows, 7 columns, SHA-256 `ebe0348e9773f2f1affee0d6067503e1be40f3297fe5fac404ceccdae4d4cb2e`.
- `docs/spreadsheets/chaos_redux_scenarios_catalog.csv` — 13 rows, 6 columns, SHA-256 `1ab7ee1189ba99a8167f2cb98f8e61b698b6adda8b3c648a8b49cc0d67a87708`.

## Validation

- Compared the saved workbook against `HEAD` outside the five intended cells: zero unexpected value differences and zero unexpected style differences.
- Preserved sheet names, table references (`Events!A1:M1015`, `Clusters!A1:G15`, `Scenarios!A1:F12`), and all existing data-validation ranges/formulas.
- Workbook contains zero formulas and zero Excel error cells.
- Export rows for Event ID `6`, Cluster ID `2`, and Scenario ID `SCN-008` match the updated workbook values.

