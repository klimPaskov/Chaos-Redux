# Event 006 catalog OOXML repair handoff

Date: 2026-08-28

## Scope

Repaired the authoritative event catalog workbook so standard XLSX readers resolve its existing shared-string values. No player-facing wording, workbook rows, columns, or catalog content was invented or rewritten.

## Files changed

- `docs/spreadsheets/chaos_redux_events_catalog.xlsx` — repaired shared-string cell XML in place.
- `docs/spreadsheets/chaos_redux_events_catalog.csv` — refreshed by the required exporter.
- `docs/spreadsheets/chaos_redux_clusters_catalog.csv` — refreshed by the required exporter.
- `docs/spreadsheets/chaos_redux_scenarios_catalog.csv` — refreshed by the required exporter.
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_catalog_xlsx_repair_2026-08-28.md` — this handoff.

## OOXML repair

The worksheet parts stored shared-string indices directly as `<c ... t="s">index</c>`, which made standard readers return blank text. The repair changed only the four worksheet parts as follows, preserving each original index:

- `xl/worksheets/sheet1.xml` (`Events`): 714 cells repaired.
- `xl/worksheets/sheet2.xml` (`Clusters`): 60 cells repaired.
- `xl/worksheets/sheet3.xml` (`Scenarios`): 78 cells repaired.
- `xl/worksheets/sheet4.xml` (`Legend`): 81 cells repaired.

Each malformed cell is now `<c ... t="s"><v>index</v></c>`. The shared-string table, workbook relationships, styles, tables, filters, freeze panes, and other workbook parts were not content-edited.

Event 006 is `Events!A7:N7`. After repair, `openpyxl` resolves the existing Event Name (`Independence Wave`), details, evolution wording, type, chaos level, cluster, severity, and status instead of blanks.

## Export

Ran from the mod root:

```text
python .tools/export_event_catalog_csv.py
```

Exporter result: success. It wrote 166 rows x 14 columns for Events, 14 rows x 7 columns for Clusters, and 13 rows x 6 columns for Scenarios. The Event 006 CSV row is populated with its existing wording; the other two CSV snapshots are also populated rather than blank.

## Remaining risks

- The exporter emitted openpyxl's existing warning that the Data Validation extension is unsupported; it only read the workbook and did not save it. The repaired workbook still contains its original data-validation XML.
- No gameplay, localisation, documentation/specification source, or other unrelated files were edited.
