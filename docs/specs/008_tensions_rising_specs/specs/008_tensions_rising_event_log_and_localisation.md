# Event 008: Event Log, Localisation, and Text Direction

This file describes the player-facing wording surfaces for Event 008. It does not contain final localisation YAML. It defines the intended text so the implementation and localisation pass can keep events, logs, details, evolutions, delayed reports, and the catalog aligned.

## Naming

Canonical event name: **Tensions Rising**

Avoid alternatives that sound like a war has already begun. The event is pressure before the break.

## Baseline popup

### Title

**Tensions Rising**

### Description direction

The description should be short and report-like. It should mention diplomatic accusations, military communiqués, leaks, denials, and public unease. It should not reveal future hidden mechanics.

Suggested draft:

> A chain of public accusations, military communiqués, and unattributed leaks has unsettled diplomatic circles. No capital admits there is a crisis, yet border offices, newspapers, and staff rooms have all begun behaving as if one is near.

### Option text

**Another file on the desk.**

### Visible effect text

- Calm/baseline: `World tension increases by 10.`
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

> Staff offices remain lit long after the public briefings end. Maps are checked, train schedules copied, and commanders told that nothing is happening while being ordered to prepare for it.

Option: **No one sleeps through this.**

### Stage IV: The Permanent Alert

> The world no longer waits for tension to rise. It lives inside it. Every capital has learned to deny the same thing at once, and every denial now sounds like an order.

Option: **The line is gone.**

## Event details window

### Main detail text

> A repeatable global pressure incident. In calm conditions it raises world tension while there is still room for tension to rise. Once the world has entered higher chaos tiers, the same headline can keep firing even at maximum world tension, adding chaos directly and leaving diplomatic aftershocks behind it.

### Mechanics summary text

> Higher stages can briefly quicken the rhythm of later incidents, sour relations between plausible rivals, and produce delayed reports about the panic spreading through embassies, markets, staff rooms, and border offices.

### World-end line

> No world-end scenario. This event can help push the world toward collapse through chaos and pacing pressure, but it never becomes a terminal branch by itself.

## Evolution detail entries

Evolution track name: **Diplomatic Fever**

### Stage I event detail preview

**Cable Traffic Flood**  -  The event begins to add chaos directly and can fire even when world tension is already full. Diplomatic cables, denials, and rumours can briefly quicken later incidents.

### Stage II event detail preview

**The Accusation Market**  -  The event adds stronger chaos and tension packets. Rumours become useful political tools, damaging relations and sometimes creating temporary national panic.

### Stage III event detail preview

**General Staffs Stop Sleeping**  -  The event can push several rivalries at once. Countries become more willing to react through existing war-preparation and diplomatic systems.

### Stage IV event detail preview

**The Permanent Alert**  -  The event reaches its final non-terminal form. It applies severe pressure, large diplomatic shocks, and can trigger a one-time super-event when first reached.

## Evolution log titles

| Stage | Evolution log title | Short row direction |
| --- | --- | --- |
| I | Cable Traffic Flood | Diplomatic traffic begins outpacing official denials. |
| II | The Accusation Market | Rumours and accusations become a political economy. |
| III | General Staffs Stop Sleeping | Military staffs react before diplomats finish speaking. |
| IV | The Permanent Alert | The world no longer needs room for tension to rise. |

The stage title should appear in evolution catalogue, evolution history, and selected-event detail surfaces wherever the current event-log implementation supports stage text.

## Delayed report text directions

### The Telegram Nobody Signed

Tone: muted, bureaucratic, suspicious.

> A message circulated through several foreign ministries today. Every government named in the document denied writing it. Several denied receiving it. None denied reading it.

### Embassy Side Doors

Tone: quiet public unease.

> Reporters have noticed embassy staff abandoning front entrances in several capitals. Officials insist the change is procedural. The guards at the front gates have been doubled.

### The Calm Map Says Nothing

Tone: tension beyond measurement.

> The public measures say the world can grow no more tense. The offices disagree. Clerks still copy new warnings, commanders still ask for clearer orders, newspapers still find darker words.

### Insurance Rates Jump in Neutral Ports

Tone: markets smell panic.

> Neutral shipping firms have begun rewriting their rates before any government admits danger. It is often said that merchants hear war before diplomats name it.

### The Rumour That Arrived Twice

Tone: impossible coincidence.

> Two capitals received the same rumour through different channels, with the same phrasing, the same missing signature, and the same urgent warning. Both deny being the source.

### Staff Cars After Midnight

Tone: military fatigue.

> Staff cars were seen outside several ministries long after midnight. Official spokesmen said the meetings were routine. No one asked why routine now requires blackout curtains.

### Fleets Keep Radio Silence

Tone: naval near-miss.

> A naval movement passed without public explanation today. Harbour offices confirmed nothing, denied nothing, and asked newspapers not to print ship names.

### Border Lamps

Tone: frontier unease.

> Lamps stayed lit along a quiet border through the night. Local commanders blamed weather, then training, then paperwork. None of the explanations satisfied anyone nearby.

### One Denial Too Many

Tone: denial as proof.

> The third denial came faster than the first accusation. By the time it reached the morning papers, several foreign editors had decided speed was evidence enough.

### The Last Normal Briefing

Tone: pre-super-event dread.

> The briefing began with ordinary phrasing. It ended with no questions, no jokes, and no one willing to call the day ordinary again.

## Super-event text direction

Working title: **The Red Line Disappears**

Alternative title: **The Whole Map Holds Its Breath**

Description should emphasize lights, offices, sealed cables, nervous staff, and the collapse of believable deniability. It should not claim that the world has ended.

Button direction: short, grim, specific. Examples to research or refine:

- **No one admits it first.**
- **Every line moves now.**
- **The lamps stay on.**

Quote direction: real sourced quote about fear, war before declaration, peace as fragile, public denial, or the psychology of crisis. Do not invent a quote.

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
| super-event | `super_event.<slot>.t`, `.d`, `.a`, `.q` after slot assignment |

## Spreadsheet/catalog note

The uploaded workbook row inspected during planning still described Event 8 as `Increase world tension by 5.` The rework source of truth is the user prompt in this task. After implementation and final localisation, route the spreadsheet update through the spreadsheet worker so event detail, evolution detail, cluster detail, and catalog wording match the in-game strings.
