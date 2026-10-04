# Event 029 catalog changes pending

Disposition: accepted and queued.
Acceptance basis: the lead's round-one decision to fix catalog text by changing the game rather than the workbook, recorded as D2 and D16 in `agent_decisions_2026-10-04.md`.
Reason queued: agents may not edit `docs/spreadsheets/chaos_redux_events_catalog.xlsx` or its exported CSV files in this round; the workbook owner applies the row change and runs `python .tools/export_event_catalog_csv.py`.

## Row 29, Riches Found

| Column | Requested change |
| --- | --- |
| Details | Drop the final sentence "When no valid country and state pair exists, Event Details shows N/A." It describes interface behaviour rather than the event. The remaining Details text already matches the in-game `riches_found.event_details.description` word for word. |
| Evo I | No change. The in-game `riches_found.evolution.stage_1.body` uses the workbook text. |
| Evo II | No change. The in-game `riches_found.evolution.stage_2.body` uses the workbook text. |
| Evo III | No change. The in-game `riches_found.evolution.stage_3.body` uses the workbook text. |
| Type | No change: Minor Repeatable. |
| Chaos level | No change: 1. |
| Cluster ID | No change: 7, 15 (D2). |
| Status | No change: Needs Testing. |

The source for this comparison was the exported `docs/spreadsheets/chaos_redux_events_catalog.csv` as it stood on 2026-10-04; it was read, not edited.
