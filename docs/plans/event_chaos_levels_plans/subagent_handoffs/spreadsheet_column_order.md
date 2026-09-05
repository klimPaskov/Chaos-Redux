# Spreadsheet Column Order Handoff

## Documentation review, 2026-09-05

Disposition: unresolved.
Historical workbook-edit record. Its scalar Member Severity column and 14-column Events export conflict with the later schema-alignment handoff and the reviewed workbook evidence linked below. Retain the original row counts, field mapping, and inspection results as revision-specific evidence. Do not reproduce this migration from the old handoff or treat its headers as the current schema.
See the [shared-plan review](../../repo_cleanup/subagent_handoffs/2026-09-05_shared_plan_dispositions.md) for the source ledger, cross-document conflicts, and evidence limits.

## Retained record

Updated `docs/spreadsheets/chaos_redux_events_catalog.xlsx` on the `Events` sheet.

- Changed row 1 and the full table field mapping for columns K:N from `Cluster ID, Member Severity, Status, Chaos level` to `Chaos level, Cluster ID, Member Severity, Status`.
- Preserved the table reference `A1:N1015`, moved each field's existing cell styles and column widths with its data, and moved field-specific data validation ranges to `M2:M1015` and `N2:N1015`.
- Representative event IDs validated: 1 has chaos level 1; 9 has chaos level 2; 20 has chaos level 1; 98 has chaos level 1; 99 remains blank; 163 has chaos level 1.
- Workbook header and exported Events CSV header both equal `ID, Event Name, Details, Evo I, Evo II, Evo III, Evo IV, Evo V, World-End Scenario, Type, Chaos level, Cluster ID, Member Severity, Status`.
- Table metadata order is `ID, Event Name, Details, Evo I, Evo II, Evo III, Evo IV, Evo V, World-End Scenario, Type, Chaos level, Cluster ID, Member Severity, Status` with table column IDs retained with their fields.
- Exported snapshots refreshed with `python .tools/export_event_catalog_csv.py`: Events 183 rows / 14 columns, Clusters 14 rows / 7 columns, Scenarios 12 rows / 6 columns.

Changed files are the workbook, the three exporter-generated CSV snapshots, and this handoff.

Remaining risk: no live Excel UI round-trip was performed; the OOXML package, openpyxl-loaded structure, table metadata, validations, widths, and exported headers were inspected after the edit.
