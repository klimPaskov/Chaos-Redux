# Event 33 catalog changes pending

Disposition: implemented in the authoritative workbook and generated exports on 2026-10-07, pending parent isolated commit integration.
The acceptance basis is agent decision D21 in [agent_decisions_2026-10-04.md](agent_decisions_2026-10-04.md), taken on 2026-10-04 under the full design authority the user granted for Event 033.
The catalog worker applied the six approved cells and ran `python .tools/export_event_catalog_csv.py` after the workbook save.
The current [handoff](subagent_handoffs/catalog_current_review_2026_10_07.md) and [preservation evidence](catalog_current_2026_10_07/resume_verification.json) identify the exact cell changes, current source/export hashes, unchanged native workbook features and protected other-owner edits.
An isolated HEAD-plus-six-cells workbook and matching exports keep those other edits out of this plan's commit.
`Needs Testing` follows D21 and does not claim that the outstanding Event 33 source repairs or native-game gates are complete.

## Event 33 row (`docs/spreadsheets/chaos_redux_events_catalog.xlsx`, sheet with the `ID` column)

| Field | Prior workbook value | Accepted implemented value | Source of truth |
| --- | --- | --- | --- |
| Details | A lethal atmospheric system moves through a frozen registry of valid states, touching each state exactly once while prepared countries spend resources to limit deaths, damage, contamination, and supply loss before the ordinary cloud dissipates. | A lethal acid-rain system moves between regions, exposing the inhabited states in its path to corrosion, poisoned runoff, infrastructure damage, and direct civilian loss. Countries can build shelters, protect water and food, expand emergency medicine, harden transport, evacuate states ahead of storm forecasts, and repair the aftermath. The rain ordinarily disperses only after it has crossed every state in its path. | `acid_rain.event_details.description` in `localisation/english/033_acid_rain_l_english.yml` |
| Evo I | Severe Storm Cells: localized high-intensity cells add stronger human, infrastructure, supply, and military pressure while the regional system continues moving. | Severe Storm Cells: Concentrated cells form inside the moving front, giving threatened states nine days to prepare for heavier corrosion and lethal exposure. | `acid_rain.evolution.stage_1.title` and `acid_rain.evolution.stage_1.body` |
| Evo II | Multiple Weather Fronts: two independent fronts can operate at once, with a conditional third front, separate warnings, timers, intensity, and severe cells. | Multiple Weather Fronts: The atmospheric mass divides into independent fronts with separate routes, warnings, intensity, and severe cells. | `acid_rain.evolution.stage_2.title` and `acid_rain.evolution.stage_2.body` |
| Evo III | Global Acid Rain: simultaneous worldwide exposure closes the regional phase, applies the same exact population-loss contract everywhere, and retains a guaranteed dissipation path. | Global Acid Rain: The fronts merge into a worldwide layer that exposes every inhabited state in its path and produces regional superstorms with nine-day forecasts. | `acid_rain.evolution.stage_3.title` and `acid_rain.evolution.stage_3.body` |
| Status | To Be Reworked | Needs Testing | Accepted D21 classification, not a claim that remaining source repairs and validation gates are complete |

Evo IV, Evo V and World-End Scenario stay empty, and Type (Major), Chaos level (2) and Cluster ID (5) are unchanged.
The prior Details cell's exactly-once claim is superseded by the accepted premise above: fronts revisit regions, and severe cells, superstorms and the global layer can expose states again.
Clusters!C6 also matches the current Natural Disasters description, and slot 7's existing optional High Heat Wave remains unchanged after Acid Rain's sixth optional Severe slot.
