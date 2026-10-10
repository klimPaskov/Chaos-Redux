# Event 033 Acid Rain catalog and cluster alignment

Status: `implemented`.
The workbook row, cluster row and generated exports were updated in parent commit `02cf2601e` under agent decision D21; the cell-level record is [the catalog change record](../../../plans/033_acid_rain_plans/catalog_changes_pending.md).
`docs/spreadsheets/chaos_redux_events_catalog.xlsx` stays the only editable source, and `python .tools/export_event_catalog_csv.py` regenerates the CSV exports after every workbook change.

## Event-catalog row

| Column | Current value |
| --- | --- |
| ID | `33` |
| Event Name | Acid Rain |
| Details | The in-game `acid_rain.event_details.description` text |
| Evo I | Severe Storm Cells, from `acid_rain.evolution.stage_1.title` and `.body` |
| Evo II | Multiple Weather Fronts, from `acid_rain.evolution.stage_2.title` and `.body` |
| Evo III | Global Acid Rain, from `acid_rain.evolution.stage_3.title` and `.body` |
| Type | Major |
| Chaos level | `2` |
| Cluster ID | `5` |
| Status | Needs Testing |

Catalog Details and evolution cells must keep matching the in-game localisation wording.
The Events sheet does not store member severity; Acid Rain's Severe value belongs to its Cluster Memberships row and the Natural Disasters cluster row.

## Cluster row

Cluster 5, Natural Disasters, lists members `13, 13, 13, 13, 13, 33, 51`: five logical Event 13 season slots, the optional Severe Acid Rain member and the optional High Heat Wave member.
Its root type stays Minor Repeatable, and its Details describe the mixed Major pacing in player terms.
The five Event 13 entries are logical slots with their own tier and chance behavior, not placeholders.

## Member registry

| Field | Value |
| --- | --- |
| Event ID | `33` |
| Danger | Severe |
| Order | After all five Event 13 slots |
| Required when it is the trigger | Yes |
| Optional participation | Part 7 tier table (see README open question 4 on the Severe floor) |
| One-time validity | Not fired, not active, not reserved |
| Pacing contribution | Major when queued, committed once at launch |
| History owner | Event 33 owns its event row; the cluster owns the sequence row |

## Event Details and evolution registry

Event Details shows the Major type, Chaos level 2, the Natural Disasters cluster, the live status block, the stored outcome after closure and the viewing country's achievements (D34).
The three evolutions are cumulative, global, persist after Chaos falls and add no Chaos on activation.

## Re-check after any change

1. Regenerate the CSV exports from the workbook.
2. Verify exactly one Event 33 row with Type, Chaos level, Cluster ID and Status as above.
3. Verify that cluster 5 keeps Event 13 in slots 1 to 5, Acid Rain in slot 6 and Heat Wave in slot 7 with aligned severity lists.
