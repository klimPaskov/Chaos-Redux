# Event 26 catalog update brief

## Current catalog conflict

The supplied event catalog contains two conflicting rows:

- ID `26` is still `Desert question`.
- A separate no-ID backlog row is named `Black Friday`.

The authoritative workbook must contain one Event 26 row after implementation. Do not edit the CSV export directly.

## Target Events sheet row

| Column | Target value |
| --- | --- |
| ID | `26` |
| Event Name | Black Friday |
| Details | When selected at Gathering Storm or higher, Black Friday waits for an eligible Friday. For that day, registered government, military, intelligence, equipment, and project purchase costs are reduced by 50 percent. The sale ends on the next daily tick, preserves ordinary requirements and modifiers, and uses minimum nonzero rounding. |
| Evo I | Chaos Tier: the active Friday discount rises to 75 percent. The stronger rate is chosen when the sale begins and remains fixed for that day. |
| Evo II | blank |
| Evo III | blank |
| Evo IV | blank |
| Evo V | blank |
| World-End Scenario | blank |
| Type | Minor Fire-Once |
| Cluster ID | blank |
| Member Severity | blank |
| Status after implementation | Needs Testing |

The final workbook wording must match the implemented Event Details and Evolution I text. The spreadsheet worker should copy exact in-game mirror wording where the field is a mirror field.

## Duplicate resolution

Remove the no-ID Black Friday backlog row or convert it into the ID 26 row without leaving a duplicate. Preserve workbook formatting, filters, formulas, validation, and row structure.

## Export

After saving `docs/spreadsheets/chaos_redux_events_catalog.xlsx`, run:

```text
python .tools/export_event_catalog_csv.py
```

Confirm that the Events, Clusters, and Scenarios CSV snapshots were regenerated from the workbook. Do not hand-edit any of those CSV files.
