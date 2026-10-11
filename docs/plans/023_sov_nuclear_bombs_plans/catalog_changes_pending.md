# Event 23 catalog changes pending

Disposition: implemented in catalog commit `bddbd9f8f` on 2026-10-11 (workbook plus regenerated export); the rows below are retained as the instruction that was applied.
The acceptance basis is the lead's Round 1 decision D9 for Event 23 (2026-10-04), recorded in [agent_decisions_2026-10-04.md](agent_decisions_2026-10-04.md), applied after the priority 1 and 2 gameplay commits.
Implementation stays queued because the Event 23 engineer does not edit `docs/spreadsheets/chaos_redux_events_catalog.xlsx` or its CSV exports in the shared tree; the workbook owner applies this row and then runs `python .tools/export_event_catalog_csv.py` from the mod root.

## Event 23 row (`docs/spreadsheets/chaos_redux_events_catalog.xlsx`, sheet with the `ID` column)

| Field | Current workbook value | Required value | Source of truth | Decision |
| --- | --- | --- | --- | --- |
| Status | To Be Reworked | Needs Testing | Event 23 is reworked and enabled by default through `event_log_event_is_reworked_default_enabled` in `common/scripted_triggers/chaosx_settings_triggers.txt`; live verification is still pending | D9 |
| Cluster ID | (blank) | (blank, unchanged) | Event 23 belongs to no cluster | D9 |
| World-End Scenario | (blank) | (blank, unchanged) | Event 23 has no world-end row; its major exchange is a nonterminal super-event | D9 |

The Details cell already matches `sov_nuclear_bombs.event_details.description`.
The Evo I to Evo IV cells already match `sov_nuclear_bombs.evolution.i.body` to `sov_nuclear_bombs.evolution.iv.body` in `localisation/english/023_soviet_nukes_l_english.yml`, and Evo V stays blank.
Event Name, Type and Chaos level need no change.
