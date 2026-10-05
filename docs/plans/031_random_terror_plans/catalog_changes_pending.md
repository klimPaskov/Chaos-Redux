# Event 31 catalog changes pending

Disposition: accepted and queued.
Acceptance basis: lead decision D13 in `agent_decisions_20261004.md` (in-world text drops the meta word "fictional"; the scenario premise keeps its framing), within the user's grant of full design authority.
Reason queued: the implementation round may not edit `docs/spreadsheets/chaos_redux_events_catalog.xlsx`; the workbook owner applies these rows and then runs `python .tools/export_event_catalog_csv.py` from the mod root.

The catalog must match the in-game localisation wording exactly.

| Workbook sheet | Row | Field | Current text | Replace with | In-game source |
| --- | --- | --- | --- | --- | --- |
| Events | Event 31 (Random Terror) | Evo IV | "A fictional jihadist current forms an international command opposed by Muslim governments and communities as well as other states." | "An extremist jihadist current forms an international command opposed by Muslim governments and communities as well as other states." | `random_terror_evolution_jihadist_international_desc` in `localisation/english/031_terrorist_attack_l_english.yml` |

| Events | Event 31 (Random Terror) | Status | "To Be Reworked" | "Needs Testing" | Event 31 is enabled by default in `event_log_event_is_reworked_default_enabled` (`common/scripted_triggers/chaosx_settings_triggers.txt`), decision R41 in `agent_decisions_20261004.md` |

Unchanged on purpose: the Scenarios sheet row SCN-016 Global Jihad keeps "Launch a worldwide crisis led by a wholly fictional jihadist movement...", because it mirrors the Triggerable Scenarios premise (`chaosx.scenarios.global_jihad.desc`), which keeps its framing sentence under D13.
