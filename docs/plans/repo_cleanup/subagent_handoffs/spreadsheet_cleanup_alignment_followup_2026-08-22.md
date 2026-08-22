# Spreadsheet Event Details Alignment Follow-up, 2026-08-22

## Scope

Updated only the Event Details field on the `Events` sheet for Event 012 and Event 019.

The existing Event 016 workbook content was preserved except for verification of its Unicode spelling.

No localisation, gameplay, GUI, interface, asset, status, cluster, or direct CSV edits were made.

## Cells and exact localisation keys

| Event ID | Event | Cell and field | Exact current in-game localisation key | Result |
| ---: | --- | --- | --- | --- |
| 12 | Africa Is One | `Events!C13` — Details | `chaosx.events_log.window.event_details.africa` in `localisation/english/012_african_union_l_english.yml` | Replaced implementation/process prose with the exact current premise text. |
| 19 | Soldiers from Nowhere | `Events!C20` — Details | `chaosx.events_log.window.event_details.infantry_spawn` in `localisation/english/019_infrantry_spawn_l_english.yml` | Replaced implementation/process prose with the exact current premise text. |
| 16 | Brilliant Scientist | `Events!C17` — Details | `chaosx.events_log.window.event_details.brilliant_scientist` plus `GetDhrondanEventDetailClause` resolving `dhrondan_event_detail_clause` | Checked only; the stored character was already Unicode `D’Rhondan`, so no cell edit was made. |

The Event 016 Details value remains otherwise unchanged, preserving its concurrent workbook and CSV content.

`Events!M19` and `Clusters!G10` were not changed.

## Files

- `docs/spreadsheets/chaos_redux_events_catalog.xlsx`
- `docs/spreadsheets/chaos_redux_events_catalog.csv` (export output)
- `docs/plans/repo_cleanup/subagent_handoffs/spreadsheet_cleanup_alignment_followup_2026-08-22.md`

The required exporter also regenerated `docs/spreadsheets/chaos_redux_clusters_catalog.csv` and `docs/spreadsheets/chaos_redux_scenarios_catalog.csv`.

## Validation

Ran from the mod root:

```text
python .tools/export_event_catalog_csv.py
```

Exporter result: `status: success` with 183 Event rows and 14 columns, 14 Cluster rows and 7 columns, and 12 Scenario rows and 6 columns.

The workbook re-opened with the existing five sheets, `Events!A1:N928`, `Clusters!A1:G14`, and `Scenarios!A1:F12` dimensions, existing tables, data-validation counts, conditional-formatting counts, and no formulas.

The exported Event rows for IDs 12, 16, and 19 match their workbook Details cells exactly.

The checked Event 016 cell contains `D’Rhondan` and no replacement character.

## Risks and ambiguity

No wording ambiguity remains for Events 012 or 019 because both Details cells now exactly match their current in-game premise keys.

The earlier `D�Rhondan` appearance was terminal encoding mojibake, not a workbook replacement character; the workbook already contained U+2019 and was intentionally left unchanged.

No blocked or `needs_user_review` cells were introduced.
