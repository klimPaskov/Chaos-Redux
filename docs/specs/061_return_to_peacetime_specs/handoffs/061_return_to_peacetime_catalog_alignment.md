# Event 061 catalog alignment handoff

## Authority rule

Edit the authoritative XLSX workbook only.

After the workbook change, run:

`python .tools/export_event_catalog_csv.py`

Review the generated CSV diff.

Do not edit the three CSV exports directly.

## Current stale Event 61 export

| Field | Current exported value |
| --- | --- |
| ID | 61 |
| Event Name | Half mils into civs |
| Details | Half of each country's military factories become civilian factories. |
| Type | Minor Repeatable |
| Chaos level | 1 |
| Cluster ID | empty |
| Member Severity | empty |
| Status | To Be Reworked |
| Evolutions | empty |

The source specification supersedes this placeholder.

## Required Event 61 fields

| Field | Required value or direction |
| --- | --- |
| ID | `61` |
| Event Name | `Return to Peacetime` |
| Type | `Minor Repeatable` |
| Chaos level | `1` |
| Cluster ID | `4` |
| Member Severity | `High` |
| Status | Match verified implementation state. Keep `To Be Reworked` until implementation. Use `Needs Testing` only after the complete rework exists and validation has begun. |

## Details field direction

The revised details must explain these public facts in compact catalog form:

- every ordinary country begins dismantling wartime economic and military structures
- half of eligible military factories convert into civilian factories
- half of War Support transfers into Stability
- economy and conscription laws move one step toward peacetime floors
- military production suffers a temporary reconversion penalty
- Return to Rearmament allows a costly recovery

Do not include:

- internal state-ledger variables
- raw Readiness formula
- hidden AI logic
- exact anti-exploit checks
- implementation file names
- developer or testing language

## Evolution I field direction

Fixed name:

`Swords into Ploughshares`

Required public content:

- a portion of eligible military surplus is dismantled, sold, or redirected
- protected reserves can reduce losses
- recovered value supports civilian reconstruction

## Evolution II field direction

Fixed name:

`The Great Demobilization`

Required public content:

- a portion of eligible standing divisions is mustered out
- manpower and equipment return through demobilization
- countries that rebuilt cadres and preparedness can reduce the loss

## Evolution III field direction

Fixed name:

`Permanent Peace`

Required public content:

- Peacetime Economy and No Army become available
- countries that failed to rearm can be pushed into them
- prepared countries can avoid forced adoption
- difficult recovery remains possible

## Current stale Peace cluster export

| Field | Current exported value |
| --- | --- |
| Cluster ID | 4 |
| Cluster Name | Peace |
| Members | `9, 9` |
| Type | Minor Repeatable |
| Chaos level | 1 |
| Status | Partially Available |

The duplicate member entry is wrong.

## Required Peace cluster alignment

| Field | Required value or direction |
| --- | --- |
| Cluster ID | `4` |
| Cluster Name | `Peace` |
| Members | `9, 61` |
| Member order | White Peace first, Return to Peacetime second |
| Event 9 role | Low |
| Event 61 role | High |
| Type | Minor Repeatable |
| Chaos level | 1 |
| Status | Reflect member implementation. Keep a partial state while one member remains incomplete. |

## Cluster details direction

Explain that the cluster de-escalates the world in two stages:

- eligible wars can end through settlement
- countries then unwind wartime industry, public mobilisation, and standing-force structures

Do not imply that White Peace always finds a valid war.

Do not imply that Event 61 requires White Peace to fire successfully.

## Cluster execution requirements

- member 9 evaluates first
- member 61 evaluates second
- an Event 9 skip does not block Event 61
- the cluster consumes one pacing event
- each fired member keeps its own history, repeatable state, and weight cap
- each member's minimum Chaos rules remain valid

## Related event rows

Do not silently rewrite these rows as part of Event 61 implementation, but review their future integration notes:

| Event | Current relation |
| --- | --- |
| 59, The Offensive | AI rearmament pressure |
| 82, Law Upgrade | inverse law movement and shared law helper |
| 94, Half Gone | stockpile recalculation before Evolution I resolution |
| 103, Conscription | future shared conscription-law helper |
| 124, Demilitarization | overlapping countrywide concept that needs later differentiation |
| 131, Widespread Mutiny | special-unit exclusion |
| 148, Pacifism | future AI preference input |

## Export verification

After regeneration confirm:

- Event 61 name is updated
- all three evolution cells are populated
- Cluster ID is 4
- Member Severity is High
- Peace cluster members are exactly `9, 61`
- no duplicate `9, 9` remains
- Status matches implementation truth
- generated CSVs contain no manual-only divergence from the workbook
