# Event 33 catalog changes pending

Disposition: accepted and queued.
The acceptance basis is agent decision D21 in [agent_decisions_2026-10-04.md](agent_decisions_2026-10-04.md), taken on 2026-10-04 under the full design authority the user granted for Event 033.
Implementation stays queued because the Event 033 engineer does not edit `docs/spreadsheets/chaos_redux_events_catalog.xlsx` or its CSV exports in the shared tree; the workbook owner applies these values and then runs `python .tools/export_event_catalog_csv.py` from the mod root.

## Event 33 row (`docs/spreadsheets/chaos_redux_events_catalog.xlsx`, sheet with the `ID` column)

| Field | Current workbook value | Required value | Source of truth |
| --- | --- | --- | --- |
| Details | A lethal atmospheric system moves through a frozen registry of valid states, touching each state exactly once while prepared countries spend resources to limit deaths, damage, contamination, and supply loss before the ordinary cloud dissipates. | A lethal acid-rain system moves between regions, exposing the inhabited states registered at formation to corrosion, poisoned runoff, infrastructure damage, and direct civilian loss. Countries can build shelters, protect water and food, expand emergency medicine, harden transport, evacuate states ahead of storm forecasts, and repair the aftermath. The rain ordinarily disperses only after it has crossed every eligible state. | `acid_rain.event_details.description` in `localisation/english/033_acid_rain_l_english.yml` |
| Evo I | Severe Storm Cells: localized high-intensity cells add stronger human, infrastructure, supply, and military pressure while the regional system continues moving. | Severe Storm Cells: Concentrated cells form inside the moving front, giving threatened states nine days to prepare for heavier corrosion and lethal exposure. | `acid_rain.evolution.stage_1.title` and `acid_rain.evolution.stage_1.body` |
| Evo II | Multiple Weather Fronts: two independent fronts can operate at once, with a conditional third front, separate warnings, timers, intensity, and severe cells. | Multiple Weather Fronts: The atmospheric mass divides into independent fronts with separate routes, warnings, intensity, and severe cells. | `acid_rain.evolution.stage_2.title` and `acid_rain.evolution.stage_2.body` |
| Evo III | Global Acid Rain: simultaneous worldwide exposure closes the regional phase, applies the same exact population-loss contract everywhere, and retains a guaranteed dissipation path. | Global Acid Rain: The fronts merge into a worldwide layer that exposes every valid inhabited state and produces regional superstorms with nine-day forecasts. | `acid_rain.evolution.stage_3.title` and `acid_rain.evolution.stage_3.body` |
| Status | To Be Reworked | Needs Testing | The rework is implemented in source; live-game verification is the remaining gate |

Evo IV, Evo V and World-End Scenario stay empty, and Type (Major), Chaos level (2) and Cluster ID (5) are unchanged.
The current Details cell says the rain touches each state exactly once, which does not match play: a front visits a region twice, and severe cells, superstorms and the global layer expose states again.
