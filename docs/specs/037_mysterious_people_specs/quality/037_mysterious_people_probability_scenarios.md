# Event 037 probability and weighted-logic scenarios

## Purpose

These named scenarios define the expected ordering for every weighted Event 037 surface.
They assign no final percentages, because exact values need the implemented candidate pool.
The audit cycle, tool use, retry limits, and before-and-after comparison rule are owned by `CLAUDE.md` and the `chaosx_ai_probability_auditor` definition, and this file only supplies the scenarios.

## Weighted surfaces

- evolution timing
- stance choice
- action and project choice, including target hotspot
- flavour pool selection
- flavour option `ai_chance`

## Evolution timing

| ID | Scenario | Expected result |
| --- | --- | --- |
| `EV37-EVO-001` | Chaos `200`, one firing, no country above Strained | Evolution I near its base timing, slowed |
| `EV37-EVO-002` | Chaos `200`, one country at Emergency | Evolution I faster than `EV37-EVO-001` |
| `EV37-EVO-003` | Chaos `400`, newcomers above `5%` of the world, one country at Emergency | Evolution II at its fastest legitimate pace |
| `EV37-EVO-004` | Eligible evolution disabled | Zero activation and no recorded flag |
| `EV37-EVO-005` | Evolution I disabled, Evolution II enabled at `400` | Evolution II activates without logging Evolution I |
| `EV37-EVO-006` | First firing at `650` Chaos, all stages enabled | Highest stage used once, evolutions recorded in order |

## Stance

| ID | Country | Expected order |
| --- | --- | --- |
| `EV37-POL-001` | Stable democracy at Absorbing | Open Integration clearly first |
| `EV37-POL-002` | Fascist government at Strained | Restricted Registration first |
| `EV37-POL-003` | Non-aligned country with stability `30%` at Emergency | Restricted Registration first |
| `EV37-POL-004` | Communist country with stability `70%` | Open Integration first |
| `EV37-POL-005` | Country that does not use normal civilian systems | No candidate |

No stance should win for every valid country.

## Actions

| ID | Situation | Expected order |
| --- | --- | --- |
| `EV37-ACT-001` | Strained, hotspot with infrastructure `2`, free factories | Roads and Water leads |
| `EV37-ACT-002` | Strained, hotspot with infrastructure `6`, free factories | Emergency Housing leads |
| `EV37-ACT-003` | Emergency at war, fewer than `10` free civilian factories | Registration Drive and Requisition lead, projects suppressed |
| `EV37-ACT-004` | Capital hotspot at Emergency and a small hotspot at Breakdown | The capital is targeted first |
| `EV37-ACT-005` | Evolution III, `30` civilian factories, hotspot over `1,000,000` people | Build a New City becomes viable |
| `EV37-ACT-006` | Hotspot changes controller during evaluation | Zero weight and the selection clears |
| `EV37-ACT-007` | Stability above `50%` at Overcrowded | Requisition suppressed |
| `EV37-ACT-008` | Three state projects already running | No new project candidate |

## Flavour pool

| ID | Context | Expected behaviour |
| --- | --- | --- |
| `EV37-FLV-001` | First baseline firing, rural states | Village, school, relative, road, and factory events dominate |
| `EV37-FLV-002` | Evolution I urban hotspot | New districts and work without homes become likely |
| `EV37-FLV-003` | Evolution II hotspot at Emergency with supply strain | Grain, station, and entry-limits events become possible |
| `EV37-FLV-004` | Evolution III newcomer majority | Majority, origin register, and second capital events become possible |
| `EV37-FLV-005` | An event fired for this country within its last four flavour events | That event is excluded |
| `EV37-FLV-006` | No valid state for any event | No flavour fires |

## Flavour option AI

| ID | Event and country | Expected choice |
| --- | --- | --- |
| `EV37-OPT-001` | `.24` origin register, democracy (ineligible) | Event does not fire |
| `EV37-OPT-002` | `.24` origin register, fascist country at Emergency | Adopt is likely but not certain |
| `EV37-OPT-003` | `.24` origin register, non-aligned country with high stability | Reject leads |
| `EV37-OPT-004` | `.21` station at Breakdown, neighbours at war | Close the station leads |

## Acceptance

Weighted logic passes when Open Integration leads for stable inclusive countries, projects follow the real bottleneck, invalid targets have zero weight, evolution timing respects enablement, flavour stays varied, and the origin register is never automatic.
