# Event 008: Event Log, Localisation, and Text Direction

This file describes the player-facing wording surfaces for Event 008. It does not contain final localisation YAML. It defines the intended text so the implementation and localisation pass can keep events, logs, details, evolutions, follow-up incidents, and the catalog aligned.

## Naming

Canonical event name: **Tensions Rising**

Avoid alternatives that sound like a war has already begun. The event is pressure before the break.

## Baseline popup

### Title

**Tensions Rising**

### Description direction

The description should be short and report-like. It should mention diplomatic accusations, military communiqués, leaks, denials, and public unease. It should not reveal future hidden mechanics.

Suggested draft:

> A chain of public accusations, military communiqués, unattributed leaks, and official denials has unsettled diplomatic circles. Border offices, newspapers, and staff rooms have begun behaving as if a crisis is near.

### Option text

**Another file on the desk.**

### Visible effect text

- Calm/baseline: `World tension increases by 100.`
- Evolved stages: show both chaos and world tension. Do not show exact hidden relation-pair math in the option.

## Evolved popup text variants

The same event can use stage-aware descriptions. The implementation may use scripted localisation or separate subevents.

### Stage I: Cable Traffic Flood

> The cables are moving faster than the diplomats. Every denial is copied, every correction is reprinted, and every quiet military note seems to reach a foreign desk before dawn.

Option: **The wires hum all night.**

### Stage II: The Accusation Market

> Rumour has become a commodity. Newspapers sell it, ministries launder it, border officers fear it, and foreign rivals repeat it with just enough distance to deny authorship.

Option: **Everyone has a source.**

### Stage III: General Staffs Stop Sleeping

> Staff offices remain lit long after the public briefings end. Maps are checked, train schedules copied, and commanders receive quiet orders to prepare for an unnamed crisis.

Option: **No one sleeps through this.**

### Stage IV: The Permanent Alert

> The latest warnings spread across foreign offices. Capitals compare denials, watch railway notices, and prepare contingency files as the pressure becomes part of daily government.

Option: **Log the latest alerts.**

## Event details window

### Main detail text

> This repeatable pressure incident follows public accusations, leaks, and military communiqués as diplomatic distrust spreads. Later stages bring broader panic through embassies, markets, staff rooms, and border offices. Even when tension is already high, the same headline can return with new diplomatic aftershocks.

### Mechanics summary text

> Later stages quicken the exchange of reports and sour relations between plausible rivals. Panic spreads through embassies, markets, staff rooms, and border offices, and safe border incidents can become clashes at high chaos.

### World-end line

> This event never becomes a world-end scenario. It can push the campaign toward collapse through rising pressure, but it does not end the world by itself.

## Evolution detail entries

Evolution track name: **Diplomatic Fever**

### Stage I event detail preview

**Cable Traffic Flood**  -  Diplomatic cables begin outpacing official denials, and rumours start to shape later incidents.

### Stage II event detail preview

**The Accusation Market**  -  Rumours and accusations become useful political tools, damaging relations and spreading temporary panic.

### Stage III event detail preview

**General Staffs Stop Sleeping**  -  Military staffs react immediately, and several rivalries move at once.

### Stage IV event detail preview

**The Permanent Alert**  -  The alert has become permanent. Diplomatic shocks, follow-up incidents, and rare border clashes spread through the remaining channels without ending the campaign.

## Evolution log titles

| Stage | Evolution log title | Short row direction |
| --- | --- | --- |
| I | Cable Traffic Flood | Diplomatic traffic begins outpacing official denials. |
| II | The Accusation Market | Rumours and accusations shape ministries, newspapers, and border commands. |
| III | General Staffs Stop Sleeping | Military staffs react immediately as diplomatic exchanges continue. |
| IV | The Permanent Alert | The alert has become part of daily government. |

The stage title should appear in evolution catalogue, evolution history, and selected-event detail surfaces wherever the current event-log implementation supports stage text.

## Follow-up incident text directions

### The Telegram Nobody Signed

Tone: muted, bureaucratic, suspicious.

> A message circulated through several foreign ministries today. Every government named in the document denies writing or receiving it, and officials across those capitals have already read it.

Effect direction: small world-tension, chaos, and opinion aftershock.

### Embassy Side Doors

Tone: quiet public unease.

> Reporters have noticed embassy staff abandoning front entrances in several capitals. Guards now stand in doubled numbers at the front gates, and the staff give no public reason for the change.

Effect direction: small world-tension, chaos, opinion, and AI posture aftershock.

### The Calm Map Says Nothing

Tone: tension beyond measurement.

> The public measures say the world can grow no more tense. Clerks continue copying new warnings, commanders ask for clearer orders, and newspapers find darker words.

Effect direction: small world-tension, chaos, and opinion aftershock.

### Insurance Rates Jump in Neutral Ports

Tone: markets smell panic.

> Neutral shipping firms have begun rewriting their rates. Every voyage now carries a surcharge for a war that no capital will name.

Effect direction: small world-tension, chaos, opinion aftershock, and Insurance Market achievement hook.

### The Rumour That Arrived Twice

Tone: impossible coincidence.

> Two capitals received the same rumour through different channels, with identical phrasing, a missing signature, and the same urgent warning. Neither government can identify where the message began.

Effect direction: world-tension, chaos, and multiple opinion aftershocks.

### Staff Cars After Midnight

Tone: military fatigue.

> Staff cars were seen outside several ministries long after midnight. Spokesmen called the meetings routine, and blackout curtains covered the windows.

Effect direction: world-tension, chaos, opinion, and AI posture pressure.

### Fleets Keep Radio Silence

Tone: naval near-miss.

> A naval movement passed without public explanation today. Harbour offices offered no details and asked newspapers not to print ship names.

Effect direction: world-tension, chaos, opinion, and AI posture pressure.

### Border Lamps

Tone: frontier unease.

> Lamps stayed lit along a quiet border through the night. Local commanders attributed the display to weather, training, and paperwork. No explanation satisfied anyone nearby.

Effect direction: heavier opinion pressure and possible high-stage safe non-transfer border war.

### One Denial Too Many

Tone: denial as proof.

> The third denial came faster than the first accusation. By the time it reached the morning papers, several foreign editors had decided speed was evidence enough.

Effect direction: heavier opinion pressure and possible high-stage safe non-transfer border war.

### The Last Normal Briefing

Tone: the last ordinary briefing before extended alert routine.

> The briefing began with ordinary phrasing and ended with no questions or jokes. No one was willing to call the day ordinary again.

Effect direction: strongest follow-up bundle and the highest high-stage safe border-war chance.

## Localisation key plan

Suggested keys only, final naming should match repo patterns.

| Surface | Suggested key |
| --- | --- |
| event name | `chaosx_event_8_name` |
| main popup title | `chaosx.nr8.1.t` |
| main popup description | `chaosx.nr8.1.d` |
| main popup option | `chaosx.nr8.1.a` |
| stage I description | `chaosx_tensions_rising_stage_1_desc` |
| stage II description | `chaosx_tensions_rising_stage_2_desc` |
| stage III description | `chaosx_tensions_rising_stage_3_desc` |
| stage IV description | `chaosx_tensions_rising_stage_4_desc` |
| event detail | `events_log_event_detail_8_desc` or repo equivalent |
| evolution track name | `events_log_evolution_8_diplomatic_fever` |
| follow-up titles | `chaosx.nr8.followup_telegram.t`, etc. |
| opinion modifiers | `tensions_rising_leaked_cables`, etc. |

## Spreadsheet/catalog note

The uploaded workbook row inspected during planning still described Event 8 as `Increase world tension by 5.` The rework source of truth is the user prompt in this task. After implementation and final localisation, route the spreadsheet update through the spreadsheet worker so event detail, evolution detail, cluster detail, and catalog wording match the in-game strings.
