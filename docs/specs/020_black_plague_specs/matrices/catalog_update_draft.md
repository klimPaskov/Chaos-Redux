# Catalog Update Draft

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
| Cluster ID | final registered Diseases cluster ID, planning candidate `5` |
| Member Severity | Severe |
| Status | To be changed from To Be Reworked only after full implementation and audit |

## Proposed Diseases cluster row

| Field | Planned value or direction |
| --- | --- |
| Cluster ID | next verified free cluster ID, planning candidate `5` |
| Cluster Name | Diseases |
| Details | Disease incidents create persistent state outbreaks, population loss, containment choices, medical responses, and links to the biological warfare system. Final wording should match in-game cluster detail localisation. |
| Members | `20` initially |
| Type | Minor Fire-Once or the live cluster type that matches one-time severe disease incidents, to be verified against implementation pattern |
| Chaos level | planning unlock tier `2`, subject to live cluster balance |
| Status | In progress during implementation, implemented only after cluster UI and history work |

## Proposed triggerable scenario row

| Field | Planned value or direction |
| --- | --- |
| Scenario ID | next verified free scenario ID, planning candidate `SCN-008` |
| Scenario Name | working label Black Plague Unbound, final wording must be direct and specific |
| Details | Immediately establishes Black Plague in many states across several continents, activates Evolutions I through IV, creates several independent Rat Nations, and creates the Rat King. It does not trigger Evolution V or world end. |
| Type Options | fixed profile, working label Instant Plague Kingdoms |
| Intensity Scaling | Low, Medium, High, and Maximum control continent count, infected-state count and severity, Rat Nation count, Rat King territory and army strength, and the Chaos floor. |
| Status | To Be Implemented, then Needs Testing after scenario registration and launch validation |

## Related catalog notes

- Event 41 Disease in Divisions can become a future Diseases cluster member only after its own rework.
- Event 163 Doctor Wu is a cross-event medical interaction and should not automatically be a cluster member.
- The Black Plague triggerable scenario is a separate catalog row and must be added to the live scenario workbook after final in-game wording exists.
