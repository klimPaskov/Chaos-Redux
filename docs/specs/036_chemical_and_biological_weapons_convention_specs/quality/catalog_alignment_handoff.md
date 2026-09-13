# Catalog alignment handoff

## Supplied export state

The supplied Events CSV contains this Event 036 row:

| Field | Exported value |
| --- | --- |
| ID | `36` |
| Event Name | Alien Spacecraft |
| Details | A country recovers an alien spacecraft and receives a fleet of jet fighters plus the means to produce more. |
| Type | Minor Repeatable |
| Chaos level | `1` |
| Cluster ID | Empty |
| Member Severity | Empty |
| Status | To Be Reworked |

The supplied Clusters CSV contains 13 rows.

It contains Diplomatic Panic at cluster ID `3` and no row named Diplomacy.

The supplied Scenarios CSV contains no Event 036 entry.

## Required workbook update

After implementation and final localisation, update the authoritative XLSX event row to:

| Field | Required value |
| --- | --- |
| ID | `36` |
| Event Name | Chemical and Biological Weapons Convention |
| Details | Final player-facing premise aligned with Event Details |
| Evo I | First Use Becomes Acceptable summary |
| Evo II | Strategic WMD Doctrine summary |
| Evo III | The Arsenal Without Limits and international program summary |
| Type | Minor Fire-Once |
| Chaos level | `1` |
| Cluster | Diplomacy |
| Member Severity | High |
| Status | Final status supported by implementation evidence |

## Cluster decision

The approved design uses a Diplomacy cluster.

Do not map Event 036 to Diplomatic Panic solely because it has a current numerical ID.

Inspect the authoritative workbook and runtime cluster registry.

Create or reconcile a Diplomacy cluster row and assign a stable ID through the normal project process.

Add Event 036 as a High-severity member only after the cluster identity and runtime registration agree.

## Export rule

Edit only `docs/spreadsheets/chaos_redux_events_catalog.xlsx`.

Run `python .tools/export_event_catalog_csv.py` after the workbook saves successfully.

Verify that all three export snapshots were regenerated.

Do not edit the CSV files directly.
