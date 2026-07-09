# Event 16 Brilliant Scientist, scripted GUI design

All GUI labels in this file are working labels and not final localisation. This section decides how the Kruger mechanic should be presented if the full system is implemented.

## Recommendation

Use a hybrid design.

The baseline can be handled by a normal decision category because early Kruger management has only a few choices. From Evolution I onward, the system benefits from a custom scripted GUI opened from the decision category. The GUI is justified because the player must track multiple living values, project memories, field selections, security incidents, foreign attention, and final confrontation state.

The GUI should not replace the decision system. It should be a management window for the human player. AI should use equivalent decisions or scripted effects and should never depend on human-only GUI clicks.

## Window purpose

Working window label: Kruger Institute Dossier. This is not final localisation.

The window should help the player answer five questions:

- how much research value Kruger is producing
- how much authority the state still has over him
- which project field is active
- which dangers are visible now
- what action family is currently relevant

The window should not reveal exact hidden rebellion formulas, exact rebel unit spawn totals, or the final-device path before the campaign has exposed the needed conditions.

## Entry surface

| Surface | Behavior |
| --- | --- |
| decision category | always remains the required action surface and AI action owner |
| open window decision | visible to human host after Kruger is accepted |
| close window button | closes the custom panel without changing gameplay |
| alert state | category icon or header changes when an incident, project completion, foreign theft, or confrontation state is active |
| normal decision presentation | decision category header must show the same values through scripted localisation so the mechanic remains readable without opening the custom window |

## Core layout

| Panel | Content | Gameplay purpose | Hidden data policy |
| --- | --- | --- | --- |
| portrait panel | Kruger portrait stage, status, host country | shows relationship state and portrait evolution | does not reveal alien truth until route exposes it |
| meter row | Research Momentum, Laboratory Autonomy, Security Integrity, Public Fame, Government Leverage, Strangeness summary | core mechanic clarity | Strangeness can use public summary bands rather than raw value early |
| field selector | current field and available field cards | controls project reveal and clutter | locked fields show public requirement direction only |
| project cards | one safe, one ambitious, one dangerous candidate for current field | keeps choice readable | memory outputs shown as facility summaries |
| security board | foreign incidents, staff risk, guard loyalty, theft pressure | gives active response choices | does not list future revolt strengths |
| final confrontation panel | appears only during rogue or sovereign phases | arrest, siege, evacuation, bargain, coalition, sabotage | no final-device details until race starts |
| aftermath panel | appears after containment or defeat | archive, publish, destroy, share, weaponize | future event hooks stay implicit |

## Meter design

| Meter | Display direction | Interaction | Warning state |
| --- | --- | --- | --- |
| Research Momentum | strong positive value with field contribution breakdown | projects and focuses raise it, restraint can slow it | none unless project overload is active |
| Laboratory Autonomy | state control loss value | exemptions, private guards, sealed projects raise it | warning when government action begins to fail |
| Security Integrity | protection and chain-of-custody value | guards, counterintelligence, audits raise it | warning when theft or assassination risk rises |
| Public Fame | public and foreign attention value | public science raises it, secrecy lowers it | warning when foreign attention and panic events are likely |
| Government Leverage | ability to impose limits | peer review, audits, loyal guards raise it | warning when arrest and audit actions become unreliable |
| Strangeness | anomaly summary | dangerous projects and alien or temporal memories raise it | warning through observed incidents, not spoiler language |

## Project card states

| State | Visual direction | Meaning |
| --- | --- | --- |
| locked | dim card and concise requirement tooltip | field or evolution not ready |
| available | normal card with cost summary | player can start it |
| active | highlighted card and timer | project in progress |
| completed safe | calm facility stamp | memory exists with low danger |
| completed dangerous | severe facility stamp | memory exists with stronger risk |
| incident | warning frame | event or mission is active |
| suppressed | darkened card | project family destroyed, archived, or blocked by route |

Project cards should show facility summaries and visible costs. They should not show text such as rebel clone value, final device prerequisite, or hidden world-end trigger.

## Button families

| Button family | Cost direction | Effect direction | AI equivalent |
| --- | --- | --- | --- |
| start safe project | factories, time, sometimes stability | safe memory and research gain | AI decision with same field weight |
| start ambitious project | factories, XP, equipment, security burden | stronger memory and risk | AI decision if route supports it |
| approve sealed project | factories, support equipment, security staff, stability or war support | large reward, Autonomy, Arsenal Weight | AI rare unless high chaos or war pressure |
| audit facility | intelligence, time, slower momentum | Leverage and possible hidden-stockpile reveal | AI uses when Leverage low and Security available |
| strengthen guard chain | equipment, manpower, command capacity | Security and arrest preparation | AI uses under theft or confrontation pressure |
| evacuate staff | trains, convoys, civilian factories | reduces rebel assets and casualties | AI uses if confrontation likely |
| destroy prototype | state control, units, equipment, air or special forces | removes project asset family | AI uses only with high Leverage or crisis |
| negotiate concession | stability, legitimacy, Autonomy | keeps Kruger working temporarily | AI uses when arrest is unsafe |
| call coalition | diplomacy, relations, threat state | foreign containment and sabotage options | AI uses when Kruger sovereign |

## Scripted GUI tab set

| Tab | Opens when | Purpose | Animated assets |
| --- | --- | --- | --- |
| Institute | baseline | overview and meter row | portrait stage and optional danger seal |
| Projects | after first field choice | field cards and project actions | selected card glow if asset budget allows |
| Security | after first foreign or staff incident | staff, guards, theft, foreign heat | warning pulse when active incident exists |
| Foreign attention | Evolution II | observers, rivals, theft, defection | usually static, flag cards enough |
| Confrontation | Evolution III crisis or Evolution IV | arrest, siege, bargain, evacuation, coalition | danger seal and critical warning frame |
| Final device | Kruger sovereign and device race active | component progress, sabotage, arming risk | required final-device progress frame |
| Aftermath | contained, defeated, or treaty route | captured knowledge choices | static treatment preferred |

## Animated presentation pass

Animation should clarify state changes. It should not be used as decoration on every card.

| Animated asset | Use | Frame plan direction | Static non-animated counterpart |
| --- | --- | --- | --- |
| Kruger stage 4 portrait overlay | leader portrait or GUI portrait when route becomes openly alien, machine, temporal, or terminal | 8 to 12 real source frames, instrument light, eye light, or temporal shimmer drawn per frame | severe static portrait |
| danger seal | category header or confrontation tab | 6 to 8 frames, slow warning pulse from real source frames | static warning seal |
| final-device progress frame | final-device tab | 8 to 12 frames, state-driven glow for arming progress | static reactor or equation frame |
| selected project card glow | optional project tab | 6 frames if needed, drawn card highlight states | selected static card |
| foreign theft alert | security tab | 6 frames, subtle dossier stamp or signal flicker | static alert icon |

Every animated asset must follow the frame-animation workflow with source frames, processed frames, frame sheet, final DDS, static non-animated counterpart, manifest, and `.gfx` handoff.

## GUI cleanup

The scripted GUI should hide itself or change state cleanly when:

- Kruger is sent away
- Kruger defects to another country
- Kruger is imprisoned or killed
- Kruger becomes sovereign
- the host is annexed
- the host loses the laboratory state
- the final device terminal branch fires
- postwar aftermath choices finish

The window should not show stale project targets, dead country targets, old lab states, or invalid foreign rivals.

## Decision versus GUI closure

The custom GUI is recommended for the full rework. A normal decision category is acceptable only for an early implementation tranche or a reduced baseline. If the full project, foreign attention, and confrontation systems are implemented, a GUI should be added or the decision category will likely become cluttered.
