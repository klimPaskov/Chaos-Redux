# Event 097 Collaboration: Catalog Alignment

This handoff tells `chaosx_spreadsheet_doc_worker` what to change in the event catalog after implementation. The workbook `docs/spreadsheets/chaos_redux_events_catalog.xlsx` is the only editable source. After every successful workbook update, run `python .tools/export_event_catalog_csv.py` from the mod root. Never edit the exported CSV files.

The worker starts only after implementation facts exist, because the spreadsheet fields must match the final in-game localisation word for word.

## Historical planning row

The CSV export at planning time shows row 97 as: name Collaboration, Details "Countries establish collaboration networks against one another.", empty evolution fields, empty world-end field, type Minor Repeatable, Chaos level 1, empty cluster id, status To Be Reworked. The workbook itself is stored through Git LFS in this checkout and could not be opened during planning, so the worker must read the real workbook row before writing.

## Fields to update

| Field | New content |
| --- | --- |
| Event Name | Collaboration, unchanged |
| Details | The final Event Details premise text, exactly as written in localisation |
| Evo I | The final Event Details evolution catalog text for Deep Networks |
| Evo II | The final text for Administrations in Waiting |
| Evo III | The final text for The Fifth Column |
| Evo IV | The final text for Collaboration Governments |
| Evo V | Empty |
| World-End Scenario | Empty |
| Type | Minor Repeatable |
| Chaos level | 1 |
| Cluster ID | 20, the current Intelligence identifier, matching `constant:event_cluster_id.intelligence` |
| Status | Set by the user after live validation |

## Cluster catalog row

The nested design proposes members 39, 52 and 97 with severities Medium, Low and Medium.
Inspect current workbook membership and accepted integration requirements before changing a row.
Intelligence uses ID **20**, confirmed by the parent's [current identifier audit](../../../plans/repo_cleanup/specification_package_audit_2026-10-07/handoffs/identifier_overlaps.md) in both runtime constants and the canonical XLSX `Clusters` sheet.
ID 9 belongs to National Breakthroughs, and ID 8 belongs to Diseases.
Preserve identifier 20 in both the event and cluster rows, and record any authorized membership change separately from this resolved identity.
The Event 039 type question and the Event 097 variant conflict remain separate decisions.

## Checks

- The Details and evolution text match the final localisation exactly.
- The cluster row and the event row agree on the cluster id.
- The export tool ran after the workbook change, and the three CSV exports changed only where the workbook changed.
