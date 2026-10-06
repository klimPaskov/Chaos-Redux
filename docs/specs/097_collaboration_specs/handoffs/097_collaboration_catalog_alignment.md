# Event 097 Collaboration: Catalog Alignment

This handoff tells `chaosx_spreadsheet_doc_worker` what to change in the event catalog after implementation. The workbook `docs/spreadsheets/chaos_redux_events_catalog.xlsx` is the only editable source. After every successful workbook update, run `python .tools/export_event_catalog_csv.py` from the mod root. Never edit the exported CSV files.

The worker starts only after implementation facts exist, because the spreadsheet fields must match the final in-game localisation word for word.

## Current row

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
| Cluster ID | The Intelligence cluster id chosen when the cluster is built at runtime |
| Status | Set by the user after live validation |

## Cluster catalog row

The cluster catalog row for Intelligence lists members 39 and 52 with severities Medium and Low. Add 97 with severity Medium, so the members read 39, 52, 97 and the severities read Medium, Low, Medium. The cluster id in this row must match the runtime id. The catalog, the cluster documentation, and the Event 052 package currently disagree on that id, and runtime id 8 belongs to Diseases, so the worker records the final id and the reason for it in its handoff.

## Checks

- The Details and evolution text match the final localisation exactly.
- The cluster row and the event row agree on the cluster id.
- The export tool ran after the workbook change, and the three CSV exports changed only where the workbook changed.
