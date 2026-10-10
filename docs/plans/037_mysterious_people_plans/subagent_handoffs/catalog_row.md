# Event 37 catalog row handoff

Workbook: `docs/spreadsheets/chaos_redux_events_catalog.xlsx`, sheet `Events`, row 38 (key `ID` = 37).

## Cell delta

| Cell | Header | Before | After |
| --- | --- | --- | --- |
| C38 | Details | A major country receives millions of unexplained new recruits. | People with homes, families and histories appear overnight in every inhabited land, and their neighbours cannot remember a time without them. The arrivals repeat, and each wave needs houses, work and food before the next one comes. Nobody knows where they come from. |
| D38 | Evo I | (empty) | Population Surge: Each manifestation brings far more people, enough to fill new streets in every town. |
| E38 | Evo II | (empty) | Overpopulation Crisis: Manifestations outgrow the housing and food of crowded regions. |
| F38 | Evo III | (empty) | Humanity Multiplies: Manifestations large enough to swamp whole countries, and governments that begin counting origins. |
| M38 | Status | To Be Reworked (fill FFF4B183) | Needs Testing (fill FFD9D2E9, Legend colour) |

Unchanged: B38 Event Name (Mysterious People), G38 to I38 (Evo IV, Evo V, World-End Scenario, empty), J38 Type (Minor Repeatable), K38 Chaos level (1), L38 Cluster ID (15).

## Hashes

- Before: `6aeab76b7cb5e094286ec6cfa9abdb5e1aa102937f84f14a1a0c91b588927334`
- After: `d300319b751d3de3ae376eaba3b64fd32a5aef1e419f15f65065f5ee9bef2ce9`

The before-copy was kept outside the tracked tree in the session scratchpad. The hash was rechecked immediately before replacement.

## Write route

Narrow OOXML candidate edit of `xl/worksheets/sheet1.xml` only, changing the row 38 cell nodes. Every other ZIP member payload is byte-identical to the before-copy, and sheet1.xml is identical outside row 38. The style index for M38 changed from 72 to 70, which differs only in fill (same font, border and alignment).

Reopened comparison with openpyxl across all five sheets: only C38, D38, E38, F38 and M38 changed in value or style. Tables, data validations, conditional formatting, column widths, row heights, freeze panes, auto-filter, comments and tab colours match the before-copy. The workbook has no formulas, so no recalculation applies.

## Wording sources

Localisation file `localisation/english/037_mysterious_population_l_english.yml`:

- Details matches `mysterious_people.event_details.description`.
- Evo I to III bodies match `mysterious_people.evolution.stage_1.body`, `stage_2.body` and `stage_3.body`.
- Evo I to III titles match `mysterious_people.evolution.stage_1.title`, `stage_2.title` and `stage_3.title`.

## Status basis

Needs Testing is set as instructed by the parent, which records user approval of Needs Testing for completed reworks awaiting validation (matching rows 29 and 42). No playability approval is implied.

## Exporter

`python .tools/export_event_catalog_csv.py` from the mod root exited 0 and rewrote the three exports:

- `docs/spreadsheets/chaos_redux_events_catalog.csv` (166 rows, 13 columns)
- `docs/spreadsheets/chaos_redux_clusters_catalog.csv` (20 rows, 8 columns)
- `docs/spreadsheets/chaos_redux_scenarios_catalog.csv` (17 rows, 6 columns)

A CSV-parser check against the workbook found equal headers and zero mismatched records for all three sheets. The ID 37 CSV record shows status Needs Testing, the three Evo texts, empty Evo IV, Evo V and World-End cells, Minor Repeatable, Chaos level 1 and cluster 15.

## Gaps and review notes

- The parent-specified Evo I to III cells carry the stage title as a lead-in (`Title: body`). Other event rows hold body text without a title. The localisation keeps titles separate. Kept as instructed; `needs_user_review` if the lead-in format should be aligned with other rows.
- Row height stays at the existing fixed 22.5. The longer Details and Evo texts may not fully show in a fixed-height row. This follows the existing row pattern and was not changed.
- Visual inspection of the workbook was not performed.
- Cluster 15 membership was not touched, so no cluster comparison was needed.
