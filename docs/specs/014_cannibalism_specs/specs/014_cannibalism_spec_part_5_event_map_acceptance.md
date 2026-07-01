# Event 014 Cannibalism, event map, integration, and completion gates

This file continues the Event 014 source design. All names are working labels and not final localisation.

## Event chain map

The implementation should keep Event 014 in one namespace, with the root entry following the usual `chaosx.nr14.1` pattern.

Suggested event family:

| Working event | Role | Visibility | Notes |
| --- | --- | --- | --- |
| chaosx.nr14.1 | root bootstrap and target preparation | hidden | selects target or receives scenario target |
| chaosx.nr14.2 | first country report | visible to target | baseline opening and response posture |
| chaosx.nr14.3 | first command investigation | visible to target | confirms or deepens first report |
| chaosx.nr14.4 | public leak minor news | news | only if public fear or secrecy leak triggers |
| chaosx.nr14.5 | failed containment follow-up | visible to target | moves to confirmed outbreak |
| chaosx.nr14.6 | successful local containment | visible to target | closes active category if no spread remains |
| chaosx.nr14.7 | spread exposure event | visible to new country | country-specific opening after spread |
| chaosx.nr14.8 | Evolution I reveal | visible to affected country or global depending on state | ritual and ideology become visible |
| chaosx.nr14.9 | Evolution II island or commune reveal | visible and possible news | organized cult and island silence |
| chaosx.nr14.10 | cannibal country declaration | news or country event | fired only when country forms |
| chaosx.nr14.11 | Evolution III global network reveal | super-event or news gateway | prepares world threat source |
| chaosx.nr14.12 | Hannibal connection reveal | super-event gateway | blocked until Hannibal exists |
| chaosx.nr14.13 | world-end terminal gateway | hidden plus super-event | sets world-end flags and scenario-specific state |
| chaosx.nr14.14 | defeat aftermath gateway | hidden plus visible aftermath | only after a global threat is beaten |

The exact count can change during implementation, but these roles must be covered. Do not collapse the entire event into one popup and one idea.

## Event Details direction

Event Details should describe the premise and current known situation, not raw effects.

Baseline Event Details direction:

- a country at war has reports of cannibalism inside military units
- authorities are unsure whether this is starvation, atrocity, slander, or discipline collapse
- the affected country can investigate, feed, rotate, police, suppress, or hide the issue
- early containment can end the crisis locally

Evolution details direction:

- Evolution I describes ritual and ideological cells among soldiers, prisoners, and supply routes
- Evolution II describes organized cults, state disappearances, silent islands, and possible independent communes
- Evolution III describes global network behavior, coordinated cannibal countries, and Hannibal hooks
- World-end detail describes Hannibal or another accepted unifier turning the cult into a terminal threat

Event Details must not list stability penalties, weekly manpower drain, or other raw effects.

## Event log and evolution log

The event log should record the first firing as Event 014 with the affected country as actor.

Evolution log records should include:

- event id 14
- evolution type for the cult mutation track
- stage I, II, or III
- tier display matching the existing evolution system
- actor country when the milestone belongs to a country
- no actor when the milestone is global

Do not record Baseline Stage 0 to Stage 3 as evolutions.

Evolution I actor handling:

- actor is the first country where cult pressure becomes visible
- if multiple countries cross the threshold at once, pick the country with the highest cult pressure and mention global spread through details

Evolution II actor handling:

- actor is the country owning or losing the silent island, commune, or organized cult state
- if a cannibal country forms, the new country can be saved as the actor for later rows

Evolution III actor handling:

- actor can be the strongest cannibal country or Hannibal if Hannibal exists
- no actor is acceptable if the network reveal is deliberately global

## Spreadsheet alignment after implementation

After final in-game localisation exists, the spreadsheet row should be updated to match.

Expected player-facing fields:

- Details should describe war reports, military breakdown, containment, spread, cult escalation, and cannibal countries in narrative terms
- Evo I should describe ritual ideology
- Evo II should describe organized cults, silent islands, state modifiers, and commune formation
- Evo III should describe global network and Hannibal hooks
- World-End Scenario should describe the Hannibal-linked terminal route and make clear it is not default
- Type should match the implemented source classification, Minor Fire-Once
- Status should change only after implementation and audits

## Scripted GUI integration

A custom GUI is recommended after Evolution I. If implementation cannot safely add the GUI in the first pass, the decision category must still expose all visible values through scripted localisation. This would be an explicit queued task, not a silent simplification.

GUI state flow:

1. hidden during first ordinary baseline report unless category header is enough
2. available after confirmed outbreak or Evolution I
3. warning visual state when cult pressure or public fear reaches high range
4. island visual state when island silence is active
5. global network state during Evolution III
6. Hannibal state only after Hannibal exists
7. closed or converted to aftermath view after local containment
8. closed during world-end if a terminal GUI replaces it

## Documentation output

Implementation should create or update the event doc:

- docs/events/014_cannibalism.md

The doc should cover:

- what the event is
- trigger and target logic
- baseline stages
- evolutions
- decisions and missions
- cannibal country package
- AI behavior
- Hannibal hooks
- world-end route
- super-event package
- assets and animation
- achievements
- spreadsheet alignment
- known limitations

## Completion audit gates

The event is not complete until these checks are true.

Event system:

- Event 014 is registered in the correct fire-once array
- disabled and enabled event settings work
- target validity returns unavailable or N/A when no country at war can host it
- the first target is prepared before history logging when actor data is needed

Mechanics:

- hunger, discipline, cult, fear, spread, containment, island silence, and Hannibal resonance are initialized and cleaned
- country containment does not clear other countries
- global dormancy occurs only when no active spread remains
- triggerable scenario bypass flags are scoped and cleaned

Decisions and missions:

- no decision family is a flat political power store
- every mission has success and failure logic
- every map requirement has readable tooltip direction
- active mission cap or phase filter prevents clutter
- AI has equivalents for important actions

Cannibal country:

- tag is registered and documented
- country origin flags are set
- start forces and templates are dynamic
- focus tree is assigned only to event-created cannibal tags
- shared special chaos country classification is updated
- actual nonhuman classification is applied only after a designed transformation

Assets:

- every required asset has source PNG, processed PNG, DDS, manifest entry, and handoff
- animated assets have source frames, sheet DDS, static fallback, and preview GIF
- gore requirement is met through generated fictional art

Super-events:

- no unresearched quote, button remark, title, or audio is implemented as final
- every final super-event has image, audio, localisation, slot, helper wiring, docs, and spreadsheet alignment

Audits:

- run or request decision and mission audit
- run or request localisation audit
- run or request country package audit if a cannibal country exists
- run or request focus tree audit if the cannibal tree exists
- run or request event completion audit before claiming done
