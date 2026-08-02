# Catalog Update Draft

> Runtime reconciliation, 2026-08-02: the editable workbook already carries Event 020, the Diseases cluster row (`8`), and `SCN-012`. The values below remain the wording contract for the workbook and exported CSVs. Status is `Needs Testing` until the user performs live validation. Do not treat the rows as an instruction to add another cluster, scenario, or Rat tag.

This file records the catalog wording contract for the live Event 020 rows. The spreadsheet worker must mirror final in-game localisation, while the status below remains `Needs Testing` until the user completes live validation.

## Event row 20

| Field | Planned value or direction |
| --- | --- |
| ID | `20` |
| Event Name | Black Plague |
| Details | A severe Black Death strain begins in one vulnerable mainland state. It kills population over time, spreads along state and transport routes, and draws countries into a shared struggle over containment and biological warfare. |
| Evo I | The strain grows more lethal and spreads faster, with relapses that force countries to adapt their countermeasures. |
| Evo II | The disease crosses seas through ports, convoys, military movement, and other maritime routes. |
| Evo III | An uncontrolled plague basin gives rise to the first Rat Nation, whose broods grow armies without human supplies. |
| Evo IV | The strongest brood becomes a sentient Rat King with a government and ambitions of its own. |
| Evo V | The Rat King opens a path toward world conquest after enough land and lives have been taken. |
| World-End Scenario | The Rat King completes its final path, controls a continent, and carries the plague kingdom across the world. |
| Type | Minor Fire-Once |
| Cluster ID | `8` (live Diseases cluster) |
| Member Severity | Severe |
| Status | `Needs Testing` while live consumer validation remains user-owned |

## Live Diseases cluster row

| Field | Planned value or direction |
| --- | --- |
| Cluster ID | `8` (live registered cluster) |
| Cluster Name | Diseases |
| Details | Disease incidents leave persistent outbreaks and population loss, and they force choices over containment, medicine, and biological warfare. |
| Members | `20` initially |
| Type | Minor Repeatable |
| Chaos level | planning unlock tier `2`, subject to live cluster balance |
| Status | Registered and wired; live consumer validation remains user-owned |

## Live triggerable scenario row

| Field | Planned value or direction |
| --- | --- |
| Scenario ID | `SCN-012` (live registered scenario) |
| Scenario Name | Black Plague Unbound |
| Details | A sudden Black Plague crisis spreads across several continents. New outbreaks appear, internal rat basins grow, and a Rat King emerges. The final world-end path remains closed. |
| Type Options | Instant Plague Kingdoms |
| Intensity Scaling | Low, Medium, High, and Maximum spread the crisis across more continents, states, brood basins, and Rat King territory as severity rises. The scenario creates only the two established rat countries. |
| Status | Playable |

## Related catalog notes

- Event 41 Disease in Divisions can become a future Diseases cluster member only after its own rework.
- Event 163 Doctor Wu is a cross-event medical interaction and should not automatically be a cluster member.
- The Black Plague triggerable scenario is already a separate `SCN-012` row in the live scenario workbook. Keep its four intensity descriptions aligned with the shared scenario UI and launch report.
