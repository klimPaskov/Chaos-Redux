# Event 60 catalog alignment handoff

## Authority

The editable source is `docs/spreadsheets/chaos_redux_events_catalog.xlsx`.
The three CSV catalogs are generated exports and must not be edited directly.
Run `python .tools/export_event_catalog_csv.py` after the workbook is saved.

## Current snapshot findings

The supplied Event 60 row already identifies Research Failure as Minor Repeatable, Chaos level 1, and To Be Reworked.
Its snapshot summary mentions the two-slot collapse and a Kruger Directorate preserving capacity at a political and institutional cost.
The cluster, member role, and evolution fields are blank.

The supplied Scientific Research cluster row is marked Unavailable and has no stable cluster ID in the snapshot.
The implementation agent must inspect the authoritative workbook and current runtime registry before assigning or activating that cluster.

Nearby scientific catalog rows contain stale or mismatched summaries.
Event 60 integration should use accepted event specs and implemented owner systems, not infer behavior from those stale neighboring rows.

## Required Event 60 row after implementation

| Field | Required content |
| --- | --- |
| Event ID | `60` |
| Event name | Research Failure |
| Type | Minor Repeatable |
| Chaos level | `1` |
| Cluster | Scientific Research |
| Cluster role or member severity | High |
| Baseline details | One valid major or player-controlled country suffers a collapse of scientific capacity, loses active work and a verified safe set of established technologies, falls to two operational research slots, and gains a national reconstruction system. A valid Kruger Directorate may preserve its slot count by accepting a severe authority transfer while remaining vulnerable to all other damage. |
| Evolution I | Lost Archives, available at 200+ Chaos. More branches and generations can be lost, archives begin in worse condition, and reconstruction becomes slower and more expensive. |
| Evolution II | Scientific Dark Age, available at 400+ Chaos. Core industrial, electronics, military, and advanced-engineering branches face wider regression, while selected accumulated research advantages can also be damaged under verified owner policies. |
| Evolution III | Knowledge Collapse, available at 600+ Chaos. The country falls to one operational research slot and faces the deepest safe regression and longest reconstruction. |
| Status | Match the final implementation and validation state. Do not mark Implemented until the technology transaction, AI, decisions, assets, Event Logs, docs, and required audits are complete. |

## Player-facing text alignment

The workbook detail must match the final Event Details premise and evolution descriptions.
It should explain the public situation and recovery structure.
It should not list internal node counts, flags, variables, exact modifier values, transaction receipts, test names, or implementation history.

The Event Log name, Event Details title, workbook event name, and debug selector should all resolve to Research Failure.
Evolution names must match exactly across the workbook, Event Details preview, evolution history, and event documentation.

## Scientific Research cluster handoff

Before activating the cluster:

1. Resolve its stable ID from the authoritative workbook and current registry.
2. Confirm its type, Chaos unlock tier, participation chance, cooldown, and danger summary.
3. Register Event 60 as a High member with any member-specific tier rule required by the accepted cluster design.
4. Verify ordering when a cluster episode contains Event 60 and a positive research event. Event 60 regression resolves first, then a compatible positive event can recover one bounded part of the loss.
5. Confirm the cluster counts as one pacing event while each member keeps its own event history and repeatable state.
6. Align cluster detail text with the final implemented member set.

## Spreadsheet worker brief

The spreadsheet worker should receive:

- the final implemented Event 60 Event Details localisation
- final evolution localisation
- the resolved Scientific Research cluster registry entry
- the final status and validation report
- this handoff

It should preserve workbook layout, formulas, filters, and validation, update only the relevant rows and linked fields, save the workbook, run the exporter, and report the workbook and generated CSV changes.
