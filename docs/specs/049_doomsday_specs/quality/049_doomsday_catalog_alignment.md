# Event 049 Catalog Alignment

## Current export snapshot

The supplied event catalog CSV still contains the unreworked row:

| Field | Current export value |
| --- | --- |
| ID | `49` |
| Event name | Mass Panic |
| Details | A mad scientist's warning spreads mass panic through the country. |
| Type | Major |
| Chaos level | `1` |
| Cluster | blank |
| Member severity | blank |
| Status | To Be Reworked |

The supplied cluster export contains no Event 49 membership.

## Required authoritative workbook update

The implementation agent must update only `docs/spreadsheets/chaos_redux_events_catalog.xlsx`, then run `python .tools/export_event_catalog_csv.py`.

The export-only CSV files must not be edited directly.

## Proposed event row

| Field | Proposed value |
| --- | --- |
| ID | `49` |
| Event name | Doomsday |
| Details | Global prophecies converge on a predicted end date, weakening war, government, investment, education, and faith in a normal future while Doomsday Societies organize across the world. |
| Evolution I | The Last Calendar. Predictions converge on one accepted Last Day, accelerating conviction, pacifism, institutional withdrawal, and Last Days policies. |
| Evolution II | Nothing After Tomorrow. Doomsday Societies begin replacing local and national government, opening the path to the Final Assembly. |
| Evolution III | blank |
| Evolution IV | blank |
| Evolution V | blank |
| World-End Scenario | The Final Vigil. Humanity gives up conventional geopolitics and transfers practical authority to Doomsday administrations and the Final Assembly until the predicted end. |
| Type | Major |
| Chaos level | `4` |
| Cluster ID | blank |
| Member severity | blank |
| Status | To Be Reworked until implementation is complete and audited |

## Event Details alignment

Event Details should show:

- Event name: Doomsday
- Event type: Major
- Chaos level: `4`, Chaos Tier
- Two evolution rows, each with its own enable state
- One public world-end row for The Final Vigil with its own persistent toggle
- No cluster membership
