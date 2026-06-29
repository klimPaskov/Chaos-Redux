
# Event 013 localisation, event detail, docs, and catalog alignment

This file defines text direction and catalog alignment for Event 13 Natural Disasters. It does not provide final localisation. All names are working labels unless they are existing fixed event names such as Natural Disasters.

## General text direction

Natural Disasters text should read like reports from observatories, railway bureaus, port authorities, local governors, field hospitals, and foreign relief desks. It should identify the affected area clearly. It should not sound like a generic map change.

Use dynamic text for:

- affected state,
- affected country,
- named region where available,
- disaster family,
- warning state,
- recovery state,
- refugee or aftermath state,
- first abnormal disaster family when the Evolution III super-event fires.

Do not expose hidden weights, exact variable names, raw building damage formulas, or achievement conditions in ordinary event text.

## Event popup direction

| Popup family | When shown | Direction |
| --- | --- | --- |
| Sequence opener | First report in an Event 13 sequence. | Name the affected area and the public report. Explain what kind of disaster began and whether warnings are uncertain or already late. |
| Warning popup | Warning exists before impact. | Give the country a short response window. Make the warning specific to family, such as coastal wave, fire weather, seismic tremor, flood stage, blizzard, dust wall, or skywatch report. |
| Impact popup | Player or major directly hit, or newsworthy threshold passed. | State what happened to the area and what local authorities can confirm. Mention visible damage and local suffering without listing numeric effects. |
| Aftermath popup | Recovery chain begins. | Show the concrete aftermath, such as broken rail, blocked port, displaced people, contaminated wells, ash cleanup, crater fields, or aftershock inspections. |
| Recovery success popup | Mission or major recovery closes. | Show that transport, shelters, water, port, or inspections stabilized the area. Avoid triumphal tone when deaths were high. |
| Recovery failure popup | Mission failure creates follow-up. | Show what collapsed, spread, or was left unresolved. The text should make failure readable without mocking the affected people. |
| Regional system news | Evolution II threshold. | Present the disaster as a regional response problem, with multiple local boards and border effects. Do not list every affected state if many are hit. |
| Abnormal disaster news | Evolution III threshold. | Present conflicting reports and observations. The public should understand the disaster is outside normal categories, but the text should not claim a world end. |

## Option tone direction

- Ordinary disaster options can use sober administrative wording, terse official orders, or grim understatement.
- Cheap comedy is not appropriate when the popup includes mass death, famine, refugees, or severe urban destruction.
- Sarcasm can appear in minor low-loss-rate incidents, especially when bureaucrats understate obvious chaos.
- Route-specific national jokes should be avoided unless sourced or culturally grounded by implementation research.
- Options that spend resources should clearly communicate action direction, such as evacuate, repair, ration, close, shelter, inspect, or accept relief.

## Decision and mission text direction

Decision text should describe the public action and the missing requirement. It should not describe internal implementation.

Examples of text direction, not final text:

- Evacuation decisions should name transport, shelter, and exposed districts.
- Engineer decisions should name roads, bridges, rail, ports, or airfields.
- Foreign relief decisions should name the route type and diplomatic condition.
- Drought decisions should name water, rationing, relief corridors, or field kitchens.
- Ash and dust cleanup should name airfields, rail, masks, engines, and visibility.
- Aftershock missions should name bridge inspections, cracked housing, and unstable tunnels.
- Corridor tracking should name observatories, radio stations, coastal watch, or storm path reports.

Do not use raw trigger text for state requirements. Use named regions or dynamic state lists where possible.

## GUI text direction

The Disaster Operations Map should use clear short labels. It can show technical operations language, but it should not show raw variables.

Required dynamic summaries:

- active warnings,
- impacts this sequence,
- active aftermaths,
- recovery progress,
- worst state,
- next visible follow-up risk,
- selected state or region,
- foreign relief availability,
- current abnormal corridor state when applicable.

The GUI should use consistent color direction for values.

| Value | Color direction |
| --- | --- |
| Recovery progress | Green or positive color. |
| Population pressure | Red or danger color. |
| Transport damage | Orange or warning color. |
| Water and food stress | Yellow or dry color. |
| Coastal danger | Blue or wave color. |
| Ash and dust | Grey or dark color. |
| Fire spread | Red-orange color. |
| Refugee pressure | Purple or humanitarian color. |
| Abnormal tracker | High-chaos accent, used sparingly. |

## Event details window direction

Event Details for Event 13 should explain this in player-facing terms:

- Natural Disasters records local and regional disaster sequences.
- Each firing chooses a valid affected area and can schedule delayed related reports.
- Disasters damage local industry, infrastructure, transport, supply, and population.
- Population losses feed the shared deaths system through per-state dynamic percentages, not fixed death amounts.
- Higher evolution stages expand disaster families, regional spread, and chained aftermaths.
- Recovery decisions and missions can reduce damage and prevent follow-ups.
- Evolution III introduces abnormal disasters such as meteor showers, massive quake-wave events, huge volcanic crises, delayed tsunami chains, and moving storm corridors.
- No Event 13 world-end branch exists.

It should not list raw effects or exact mortality percentages.

## Evolution detail direction

| Evolution | Detail direction |
| --- | --- |
| Evolution I | Explain that disaster reports become more varied, with more local families and warning windows. |
| Evolution II | Explain that disasters can become regional systems, hit neighboring states, strain supply, create refugee and aftermath ledgers, and open recovery mechanics. |
| Evolution III | Explain that high-chaos abnormal variants appear, with meteor showers, massive seismic and volcanic events, tsunami chains, and moving storm corridors, but no world-end branch. |

## Cluster detail direction

The Natural Disasters cluster detail should explain that this cluster contains Event 13 as repeated member slots rather than several different disaster event IDs. It should say that higher chaos unlocks stronger Event 13 member slots and that each true Event 13 member sequence logs once. It should also say that subdisaster reports inside a sequence do not create extra random-event history rows.

## Scenario detail direction

The Disaster Barrage scenario detail should explain:

- the scenario starts a manual disaster season immediately,
- type chooses the family emphasis,
- intensity chooses incident count, delay compression, and abnormal access,
- warnings and impacts arrive over a short period,
- the scenario does not start a world-end branch,
- the scenario bypasses normal chaos and evolution prerequisites only for setup.

## Spreadsheet alignment fields

After implementation and final localisation, `chaosx_spreadsheet_doc_worker` should update the catalog workbook using exact in-game wording where fields mirror UI text.

Recommended fields to align:

| Sheet area | Field | Source of truth after implementation |
| --- | --- | --- |
| Main event row | Details | Event Details localisation direction implemented in-game. |
| Main event row | Evo I | Evolution I detail localisation. |
| Main event row | Evo II | Evolution II detail localisation. |
| Main event row | Evo III | Evolution III detail localisation. |
| Main event row | World-End Scenario | Plainly state that Event 13 has no world-end scenario. |
| Main event row | Type | Minor Repeatable. |
| Main event row | Cluster ID | Natural Disasters cluster ID, expected 5 if current registry keeps it. |
| Main event row | Member Severity | Low baseline, with cluster details showing higher member entries. |
| Cluster table | Natural Disasters details | Cluster detail localisation after implementation. |
| Cluster table | Members | Event 13 only, even if listed through multiple member slots in script. |
| Manual scenario table | Scenario ID | Next free scenario id, expected SCN-007 if still free. |
| Manual scenario table | Scenario Name | Final in-game scenario name. |
| Manual scenario table | Details | Final scenario detail text. |
| Manual scenario table | Type Options | Final type labels. |
| Manual scenario table | Intensity Scaling | Final intensity impact text. |

## Documentation direction

Create or update `docs/events/013_natural_disasters.md` during implementation. It should include:

- event summary,
- event map and hidden subevents,
- target selection,
- disaster family catalogue,
- warning and impact flow,
- deaths system integration with per-state percentage death calculations,
- recovery decisions and missions,
- evolution stages,
- cluster behavior,
- manual scenario behavior,
- GUI and animated asset notes,
- placeholder migration for Sandstorm and Event 46,
- AI behavior,
- limitations and tuning notes.

Do not leave docs describing old one-off disaster behavior after implementation.
