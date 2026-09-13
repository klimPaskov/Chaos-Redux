# Catalog and Documentation Alignment

## Current exported row problem

The supplied event catalog CSV identifies Event 51 as Minor Fire-Once. The accepted brief and this package define Minor Repeatable with a complete active, recovery, cleanup, and later-firing loop.

The authoritative workbook must be updated after implementation facts are stable.

## Event workbook row

Required player-facing fields:

| Field | Required value or direction |
| --- | --- |
| Event ID | `51` or workbook-standard numeric form |
| Event name | Heat Wave |
| Description | Persistent global heat crisis with uneven state effects, changing intensity, mitigation choices, and possible lasting environmental damage |
| Event type | Minor Repeatable |
| Chaos level | 1 |
| Status | Implemented or Needs Testing only after actual implementation evidence |
| Cluster | Natural Disasters |
| Member severity | High |
| Evolutions | Three stages with accepted names and thresholds |
| Event Details | Match in-game premise wording |
| Super-event field | Evolution III escalation super-event when implemented |

Do not mark the row Implemented because this specification exists.

## Evolution detail rows

The workbook should contain player-facing detail aligned with the in-game evolution previews.

### The Killing Heat

Direction:

- heat becomes systematically lethal
- civilian and military deaths depend on local conditions and mitigation
- prolonged heat raises wildfire and drought pressure

Do not list death formulas or hidden thresholds.

### The Drying Earth

Direction:

- long extreme exposure can permanently damage land and water systems
- famine and movement can grow from failed regions
- degradation is gradual and conditional

### The Scorched World

Direction:

- some regions can become temporarily close to uninhabitable
- water, agriculture, armies, and settlement can collapse together
- rare final degradation can create wasteland

The detail should not say the campaign ends.

## Cluster workbook row

Update the Natural Disasters cluster member list to include Event 51 once as a High-severity member.

Required checks:

- no duplicate Event 51 member row
- role and minimum tier match live registry
- member severity matches Event Details
- cluster description includes persistent heat only when wording remains concise
- optional or mandatory role matches actual behavior

The current CSV snapshot has repeated Event 13 entries. The spreadsheet worker should inspect the authoritative workbook structure before deciding whether these are intentional role rows or stale duplication.

## In-game documentation

Create or update:

- event overview
- lifecycle
- public values
- decisions and missions
- integrations
- environmental degradation
- presentation and assets
- super-event research
- completion report

Documentation should distinguish:

- accepted design
- implemented runtime
- blocked map or asset work
- validation evidence

## Event Details alignment

Workbook Event Details wording should match in-game Event Details in premise and scope. It should not become a mechanical effect list.

The row should convey:

- global persistent heat
- uneven state vulnerability
- water, army, food, industry, and transport pressure
- dynamic duration and surges
- recovery and repeatability
- lasting damage at higher evolution

## Event log name alignment

The name `Heat Wave` and Event ID 51 must resolve identically in:

- event popup
- event history
- Event Details
- evolution logs
- cluster member detail
- debug name mapping
- workbook
- docs

## Super-event alignment

After research and implementation, align:

- super-event slot
- title
- description
- button reaction
- quote and attribution
- image
- audio ID
- final recording and rights
- Event Details reference
- event docs
- workbook field
- canonical music track list

## Export workflow

Only the XLSX is editable.

After a successful update, run from the mod root:

`python .tools/export_event_catalog_csv.py`

Then verify that the generated Events, Clusters, and Scenarios CSV snapshots match the workbook.

## Spreadsheet worker prompt inputs

The parent should provide:

- final implemented status
- final Event Details wording keys
- final evolution detail wording keys
- final cluster role and severity
- final super-event status
- exact workbook path

The spreadsheet worker should not infer implementation completion from specs.

## Documentation acceptance

- workbook type says Minor Repeatable
- cluster lists Event 51 once
- thresholds match `200+`, `600+`, and `1000+`
- in-game and workbook premise wording agree
- no stale Fire-Once wording remains
- super-event field matches actual implementation
- exports are regenerated, not hand edited
