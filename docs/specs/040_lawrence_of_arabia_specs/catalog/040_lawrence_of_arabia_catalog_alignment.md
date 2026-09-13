# Event 40 Catalog Alignment

## Current exported row

The supplied event catalog export currently records:

- ID: `40`
- Event name: Lawrence of Arabia
- Details: a random Arabian country falls under British control through a Lawrence intervention
- Type: Minor Repeatable
- Chaos level: `1`
- Cluster: blank
- Status: To Be Reworked

The type and description do not match the accepted design.

## Required future workbook update

Edit only the authoritative workbook at:

`docs/spreadsheets/chaos_redux_events_catalog.xlsx`

After saving the workbook, run:

`python .tools/export_event_catalog_csv.py`

Do not edit any of the three CSV snapshots directly.

## Proposed catalog fields

The wording below is a working catalog draft. The spreadsheet worker must align the final row with implemented Event Details and evolution wording.

| Field | Required value or direction |
| --- | --- |
| ID | `40` |
| Event Name | Lawrence of Arabia |
| Details | Britain secretly recalls T. E. Lawrence and sends him into one Arabian government. The target can accept aid, limit British access, expose the network, or redirect it toward an independent Arab project. Later internal stages can move the campaign to other valid Arabian governments without returning Event 40 to the random pool. |
| Evolution I | The Arab Revolt Network allows British-backed cells, smugglers, officers, and rebels to create sabotage, defections, local uprisings, and viable government-replacement attempts. |
| Evolution II | The British Arabian System links existing clients and allies through arms, intelligence, ports, railways, air routes, oil agreements, and joint political pressure while members retain autonomy routes. |
| Evolution III | Lawrence's Arabia allows a proven regional network or independent congress to form British Arabia, an Independent Arab Federation, or the rare Lawrence's Kingdom. |
| Evolution IV | blank |
| Evolution V | blank |
| World-End Scenario | blank |
| Type | Minor Fire-Once |
| Chaos level | `1` |
| Cluster ID | blank |
| Member Severity | blank |
| Status | To Be Reworked until implementation and validation justify a later state |

## Event Details direction

Event Details should explain:

- the concealed survival of a man believed dead
- the first target and the possibility of later regional stages
- the contest over aid, sovereignty, officers, routes, and political promises
- the possibility of clients, allies, resistance, defection, and federation

It should not expose:

- exact rare-route predicates
- hidden federation readiness
- AI scores
- internal cell calculations
- tuning constants

## Event log classification

- Event 40 belongs in the Fire-Once array.
- Its default weight begins at the Fire-Once default.
- The initial firing permanently removes it from future random selection.
- Regional stages are follow-up event-chain work.
- The initial firing applies one minor-event pacing transaction.
- Later regional stages do not apply further pacing transactions.

## Cluster alignment

Event 40 remains outside every event cluster.

It has intelligence, diplomacy, formable, and regional-war connections, but assigning it to a cluster would change the intended Fire-Once entry and could make the regional campaign fire through unrelated cluster selection.

## Scenario alignment

No triggerable scenario row is planned. Manual testing should use the ordinary Event 40 force-trigger route and event-specific debug or setup controls created during implementation.
