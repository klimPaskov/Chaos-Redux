# Event 26 catalog changes pending

Disposition: implemented in catalog commit `bddbd9f8f` on 2026-10-11 (workbook plus regenerated export); the rows below are retained as the instruction that was applied. Evo I carries the rendered values 600 and 75.
The acceptance basis is the lead's Round 1 agent decisions for Event 26 (2026-10-04), recorded in [agent_decisions_2026-10-04.md](agent_decisions_2026-10-04.md).
Implementation stays queued because the Event 26 engineer does not edit `docs/spreadsheets/chaos_redux_events_catalog.xlsx` or its CSV exports in the shared tree; the workbook owner applies these rows and then runs `python .tools/export_event_catalog_csv.py` from the mod root.

## Event 26 row (`docs/spreadsheets/chaos_redux_events_catalog.xlsx`, sheet with the `ID` column)

| Field | Current workbook value | Required value | Source of truth | Decision |
| --- | --- | --- | --- | --- |
| Details | A Friday clearance sale draws crowds into shops across the world. Quartermasters, intelligence officers, and ministry clerks join the rush, bringing government orders to counters already piled with civilian purchases. | A Friday clearance sale draws crowds into shops across the world. Quartermasters, staff officers, and ministry clerks join the rush, bringing government orders to counters already piled with civilian purchases. Base-game national decisions, guarantees, intelligence operations, license purchases, military-industrial organizations, equipment upgrades, leader promotions, leader traits, preferred tactics, and special projects keep their normal price. | `black_friday.event_detail.premise` in `localisation/english/026_black_friday_l_english.yml` (the in-game text separates the last sentence from the premise with a blank line) | D7, D24, D36 |
| Status | Needs Testing | Needs Testing (unchanged) | Live verification of the sale, the price table, and the achievement is still pending | D8 |
| Evo I | If this evolution is enabled and chaos is at least [?constant:black_friday_event.evolution_chaos\|0] when the sale begins, eligible purchases receive [?constant:black_friday_event.evolution_discount_percent\|0]% off. That rate lasts until the next daily tick, even if chaos falls. | If this evolution is enabled and chaos is at least [?constant:black_friday_event.evolution_chaos\|0] when the sale begins, eligible purchases receive [?constant:black_friday_event.evolution_discount_percent\|0]% off. That rate lasts for the rest of the day, even if chaos falls. | `black_friday.evolution.1.body` in `localisation/english/026_black_friday_l_english.yml` | D23 |

