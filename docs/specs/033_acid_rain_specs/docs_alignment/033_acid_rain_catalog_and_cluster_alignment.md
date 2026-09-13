# Event 033 Acid Rain catalog and cluster alignment

## Authority

The accepted Event 33 brief and this package supersede the current CSV export, which still lists Acid Rain as Minor Repeatable, Chaos level 1, without cluster membership or evolutions.

The workbook source remains authoritative for actual catalog editing. Update the workbook first, then regenerate CSV exports. Do not hand-edit the exported CSV as the only change.

## Accepted event-catalog row

| Column | Accepted value |
| --- | --- |
| ID | `33` |
| Event Name | Acid Rain |
| Details | Direction only: summarize the moving lethal acid-rain system, worldwide preparation, direct state-population deaths, damage, exact state coverage, and ordinary dissipation gate. Final spreadsheet wording belongs in implementation. |
| Evo I | Working label `Severe Storm Cells`. Direction only: summarize localized high-intensity cells and their stronger human, infrastructure, supply, and military effects. |
| Evo II | Working label `Multiple Weather Fronts`. Direction only: summarize two independent fronts, the conditional third front, separate warnings, timers, intensity, and severe cells. |
| Evo III | Working label `Global Acid Rain`. Direction only: summarize simultaneous worldwide exposure, regional superstorms, and the guaranteed later dissipation path. |
| Type | Major |
| Chaos level | `2` |
| Cluster ID | `5` |
| Status | To Be Reworked until implementation acceptance |

The Events sheet does not store member severity. Acid Rain's Severe value belongs to its logical row in Cluster Memberships and the aggregate Natural Disasters row in Clusters.

## Cluster-catalog row

Keep Cluster ID 5 and its existing root identity. Update members from:

`13, 13, 13, 13, 13`

to:

`13, 13, 13, 13, 13, 33, 51`

Cluster Details direction:

- identify five logical Event 13 season slots, one optional Severe Acid Rain member, and one optional High Heat Wave member
- explain that Event 33 and Event 51 are separate logical rows after the Event 13 sequence
- explain mixed Major pacing without exposing internal queue jargon in final player-facing text
- write final spreadsheet wording during implementation and localisation review

Other cluster fields:

| Column | Accepted value |
| --- | --- |
| Cluster ID | `5` |
| Cluster Name | Natural Disasters |
| Members | `13, 13, 13, 13, 13, 33, 51` |
| Type | Minor Repeatable root with documented mixed Major pacing |
| Chaos level | `1` |
| Status | Partially Available until Event 33 and mixed pacing are implemented |

If the workbook Type column only accepts existing simple enums, retain `Minor Repeatable` and document mixed effective pacing in Details and system docs. Do not invent an unsupported enum only for the export.

## Member registry

Add one Event 33 member row or equivalent structured record:

| Field | Value |
| --- | --- |
| Event ID | `33` |
| Danger | Severe |
| Base order | After all five Event 13 slots |
| Required when trigger | Yes |
| Optional participation | Tier table from Part 7 |
| Earliest tier | Gathering Storm |
| One-time validity | Not fired, not active, not reserved |
| Pacing contribution | Major when queued |
| History owner | Event 33 owns its event row, cluster owns sequence row |

Do not relabel the five Event 13 entries as placeholders. They are logical season slots with separate tier and chance behavior.

## Event Details alignment

Event 33 Event Details should show:

- Major event
- Chaos level 2
- Natural Disasters cluster
- Severe member
- ordinary independent and cluster firing sources
- formation date
- current phase
- world coverage
- national Preparedness link
- lifetime actual state population removed by Event 33 and contamination contribution
- enabled evolution records
- achievements
- final outcome and duration after closure

## Evolution registry alignment

Add cumulative records. The names below are working labels until localisation review:

| Evolution | Threshold | Scope | Persists after Chaos falls | Adds Chaos on activation |
| --- | --- | --- | --- | --- |
| Severe Storm Cells | Rising Chaos | Global Event 33 runtime | Yes | No |
| Multiple Weather Fronts | Chaos Tier | Global Event 33 runtime | Yes | No |
| Global Acid Rain | Totalen Chaos | Global Event 33 runtime | Yes | No |

## Major-event registry alignment

- remove Event 33 from repeatable list
- add Event 33 to Major list
- start ordinary Major weight at the framework default of zero
- include validity gate for Chaos 200 or higher
- preserve one-time fired state
- add Natural Disasters cluster reservation gate

## Documentation alignment

Update repository statements that currently describe:

- Event 33 as repeatable
- Event 33 as Chaos level 1
- continent completion as the event endpoint
- Acid Rain as one prototype map image per continent
- Event 13 as the only possible Natural Disasters cluster event

Archive old prototype notes only when useful for migration history. Current system docs should describe the accepted runtime.

## Export validation

After workbook update:

1. regenerate events and clusters CSV files
2. parse them with the repository spreadsheet validation workflow
3. verify exactly one Event 33 row
4. verify Event 33 Type, Chaos, Cluster ID, Severity, and Status
5. verify Cluster 5 member list has six entries in accepted order
