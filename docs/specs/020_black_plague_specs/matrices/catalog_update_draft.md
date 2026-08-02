# Catalog Update Draft

> Runtime reconciliation, 2026-08-02: the editable workbook already carries Event 020, the Diseases cluster row (`8`), and `SCN-012`. The values below remain the wording contract for the workbook and exported CSVs. Status is `Needs Testing` until the user performs live validation. Do not treat the rows as an instruction to add another cluster, scenario, or Rat tag.

This file defines the catalog fields that must be replaced after implementation. The text below is planning copy, not guaranteed final player-facing wording. The spreadsheet worker must mirror final in-game localisation.

## Event row 20

| Field | Planned value or direction |
| --- | --- |
| ID | `20` |
| Event Name | Black Plague |
| Details | A severe Black Death strain begins in one vulnerable mainland state, kills population over time, spreads through state and transport routes, and becomes part of the shared disease containment and biological warfare system. Final wording should remain premise-focused and omit effect lists. |
| Evo I | The strain becomes more lethal, spreads somewhat faster, relapses more easily, and requires countries to adapt their countermeasures. |
| Evo II | The disease can cross seas through ports, convoys, military movement, and other valid maritime connections. |
| Evo III | Connected uncontrolled plague basins can break away into hostile Rat Nations with strong self-growing armies that use no human manpower or equipment. |
| Evo IV | The strongest brood can become a separate sentient Rat King country that unifies the Rat Nations and receives a deeper government and focus tree. |
| Evo V | A successful Rat King can unlock a world-end focus path after enough conquest and deaths. |
| World-End Scenario | The Rat King completes the world-end path, controls a continent, and takes over the world. |
| Type | Minor Fire-Once |
| Cluster ID | `8` (live Diseases cluster) |
| Member Severity | Severe |
| Status | `Needs Testing` while live consumer validation remains user-owned |

## Proposed Diseases cluster row

| Field | Planned value or direction |
| --- | --- |
| Cluster ID | `8` (live registered cluster) |
| Cluster Name | Diseases |
| Details | Disease incidents create persistent state outbreaks, population loss, containment choices, medical responses, and links to the biological warfare system. Final wording should match in-game cluster detail localisation. |
| Members | `20` initially |
| Type | Minor Fire-Once or the live cluster type that matches one-time severe disease incidents, to be verified against implementation pattern |
| Chaos level | planning unlock tier `2`, subject to live cluster balance |
| Status | Registered and wired; live consumer validation remains user-owned |

## Proposed triggerable scenario row

| Field | Planned value or direction |
| --- | --- |
| Scenario ID | `SCN-012` (live registered scenario) |
| Scenario Name | working label Black Plague Unbound, final wording must be direct and specific |
| Details | Immediately establishes Black Plague in many states across several continents, activates Evolutions I through IV, seeds internal brood basins in the reusable `RTA` Rat Nation carrier, and creates the separate `RTX` Rat King. It does not trigger Evolution V or world end. |
| Type Options | fixed profile, working label Instant Plague Kingdoms |
| Intensity Scaling | Low, Medium, High, and Maximum control continent count, infected-state count and severity, internal `RTA` brood coverage, Rat King territory and army strength, and the Chaos floor; the number of rat country tags never scales above `RTA` and `RTX`. |
| Status | Registered and wired; live launch and balance validation remain user-owned |

## Related catalog notes

- Event 41 Disease in Divisions can become a future Diseases cluster member only after its own rework.
- Event 163 Doctor Wu is a cross-event medical interaction and should not automatically be a cluster member.
- The Black Plague triggerable scenario is already a separate `SCN-012` row in the live scenario workbook. Keep its four intensity descriptions aligned with the shared scenario UI and launch report.
