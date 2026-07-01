# Event 014 Cannibalism, evolutions, decisions, and missions

This file continues the Event 014 source design. All names are working labels and not final localisation.

## Evolution philosophy

The event can have up to three evolution stages. It does not need five. Additional stages would add bloat unless the Hannibal event later introduces new mechanics that justify another track.

Each evolution must define active-event evolution and pre-fire evolved opening where relevant.

## Evolution I, ritual and ideology

Working label, not final localisation: `Ritual Hunger`.

### Entry conditions

Evolution I can become available after the baseline event has fired and one or more of these conditions is true:

- cult pressure reached the first threshold in any active country
- a country chose exploitation more than once
- two or more countries have exposure or outbreak variables
- a prisoner transfer, port inspection, or deserter event failed
- chaos is at Gathering Storm or higher and the baseline country did not contain the outbreak fast
- the future Hannibal event sets a cult-interest flag

Pre-fire evolved opening can occur if the event has not fired yet and the world has strong war-horror conditions. It starts the first target with a confirmed cult cell rather than simple rumours.

### Active-event effect

Existing active countries receive new decisions, harsher events, and visible cult-pressure text. Baseline reports begin using language about ritual marks, repeated phrases, unofficial meal rites, and soldiers refusing ordinary rations. Text should still keep uncertainty about organization during the first Evolution I incident.

New behavior:

- cult pressure becomes visible in the decision category
- spread through prisoners, deserters, and field hospitals becomes more likely
- support and medical decisions become less effective unless paired with arrests or route-specific reforms
- exploitation path can create terror units or intimidation missions
- suppression path can create targeted raids and deprogramming missions
- neutral logistics path can still win, but it needs stronger supply proof and prisoner audits

### Pre-fire opening

If Event 014 first fires after Evolution I conditions are already live, it should begin at Baseline Stage 1 or Stage 2 with a cult cell and a first target region. The country should still have a chance to defeat the system before islands or countries appear.

### Player choice split

Evolution I creates a real internal choice.

Suppress the cult:

- costs infantry equipment, support equipment, command power, army XP, manpower, and stability depending on harshness
- lowers cult pressure
- can raise public fear if trials leak or executions become public
- unlocks prison inspections, field kitchens, and chaplain or political officer work depending on ideology
- makes later cannibal country recruitment weaker inside the country

Exploit the cult:

- route-locked by desperation, ideology, low stability, high chaos, or player choice
- gives terror tools and irregular assault bonuses against enemies or resistance
- increases cult pressure and Hannibal resonance
- can create later mutiny, leader scandal, foreign condemnation, and a cannibal officer coup
- makes the country a future recruitment ground even after apparent victory

## Evolution II, organized cult and cannibal islands

Working label, not final localisation: `Silent Islands`.

### Entry conditions

Evolution II can become available after Evolution I and one or more of these conditions is true:

- at least one remote island, colony, cut-off port, or occupied enclave has high island silence
- a country has three or more affected states
- spread reaches multiple countries
- a prison or military hospital chain is infiltrated
- an exploit path country creates terror units and loses control of them
- a front line has repeated disappearances and low supply
- chaos is Rising Chaos or higher

Pre-fire evolved opening can start the event with a remote island case or a cut-off garrison case instead of a normal land-front report.

### Active-event effect

Evolution II unlocks serious state modifiers and organized cult structures.

State modifier families:

- `field_disappearances`, a light military and civilian fear marker
- `night_transfer_zone`, a prison and hospital infiltration marker
- `empty_village_reports`, a civilian disappearance marker
- `silent_garrison`, a remote military collapse marker
- `cannibal_commune`, a pre-country local commune marker
- `hunting_ground`, a cannibal-country controlled state marker that feeds the death system

Remote islands and cut-off territories should receive special flavor. The point is isolation. Ships do not return. Patrol planes see smoke at odd hours. Soldiers refuse transfer orders. Local officials send identical supply requests after the garrison should have been evacuated.

### Cannibal island and commune creation

Evolution II can create an independent cannibal country if a state reaches the commune threshold and the owner fails or ignores containment. The system should prefer remote islands, cut-off ports, isolated colonies, mountain pockets, jungle pockets, and occupied territories with low supply.

The country creation should not be automatic after the first failed decision. It should require a visible failure chain or a scenario launch.

Creation package:

- transfer one to three states depending on severity and local geography
- spawn an irregular cannibal army scaled by population, garrison size, port access, cult pressure, and chaos tier
- add the state modifier `hunting_ground` to controlled states
- set a country flag marking origin, such as island, prison, colony, front, or exploit mutiny
- open the shared cannibal focus tree
- set a special chaos country classification
- classify as actual nonhuman only after Evolution III or a Hannibal transformation explicitly crosses that line

### Pre-fire opening

If the event first fires in an Evolution II world, the opening can begin with a silent island report. The first target country still receives decisions. If it acts fast, it can destroy or evacuate the commune before a country forms.

## Evolution III, global hunger network and Hannibal hook

Working label, not final localisation: `Global Table`.

### Entry conditions

Evolution III can become available when the cult is no longer a local military crisis.

Possible conditions:

- cannibal countries control enough states or population
- several countries have unresolved cult pressure
- at least two remote islands become silent and one mainland state copies the pattern
- total death-system impact from cannibalism reaches a high threshold
- chaos is Chaos Tier or higher
- the future Hannibal event has created Hannibal, a Hannibal tag, or a Hannibal cult variable

### Active-event effect

Evolution III changes the cult from war horror into a world threat.

New behavior:

- cannibal countries can coordinate raids and pacts
- ordinary countries can discover cross-border symbols, courier routes, or shared ritual calendars
- cult pressure can survive after hunger pressure is solved
- exploited terror units can defect or become recruitment pipelines
- state modifiers become more lethal
- the shared world-threat framework can mark cannibalism as an active source
- a super-event can fire when the network becomes publicly undeniable

### Hannibal integration

The Hannibal connection should be future-proof.

If Hannibal exists:

- Hannibal can take command of one cannibal country, become a global event target, or inspire a network without direct control
- Hannibal can use cannibalism outbreaks as recruitment grounds
- countries that exploited cult terror should receive extra Hannibal resonance
- Hannibal-aligned cannibal countries get a hidden or visible focus branch
- a Hannibal takeover super-event can fire once the connection becomes public
- the world-end route requires Hannibal power plus global cult strength, unless a later accepted Hannibal spec changes this rule

If Hannibal does not exist:

- Evolution III still works as a global cult network
- world-end preparation can be recorded but should not trigger the Hannibal world-end route
- the spec should leave a clean hook for the future Hannibal event to read existing cult variables, cannibal countries, and spread history

### Pre-fire opening

A pre-fire Evolution III opening should be rare. If Event 014 first fires in a world already at high chaos with large war-horror pressure, it can start with multiple exposure countries or one remote commune already near formation. It should not jump directly to world-end.

## Decision category design

Working label, not final localisation: `Frontline Hunger Office`.

The category should open for countries with active outbreak, exposure, local containment aftermath, or nearby cannibal country pressure. It should stay curated. Do not show every possible action at once.

### Header presentation

The category header should show:

- current stage or posture
- hunger pressure
- discipline collapse
- cult pressure when revealed
- public fear
- containment progress
- current high-risk region or selected state
- whether spread risk exists
- whether the country is pursuing suppression, logistics, secrecy, or exploitation

A custom scripted GUI is recommended once Evolution I is active. The early baseline can use decision category text alone.

### Basic containment decisions

| Working label | Phase | What it represents | Costs and requirements | Result direction | Failure risk |
| --- | --- | --- | --- | --- | --- |
| Secure field kitchens | baseline | guards rations, kitchens, and ration ledgers | support equipment, infantry equipment, command power, division presence in target region | lowers hunger pressure and discipline collapse | sabotage can raise fear |
| Rotate compromised units | baseline | pulls suspect formations away from front | trains, fuel, manpower, temporary combat penalty, unit presence | lowers discipline collapse | front weakness if used during heavy enemy pressure |
| Ration convoy to the front | baseline | emergency food and medical convoy | trains or convoys, fuel, support equipment, civilian factory burden | lowers hunger pressure and public fear | convoy loss raises spread if port or rail unsafe |
| Field hospital audit | baseline | checks wounded lists and missing personnel | support equipment, army XP, medical tech improves success | finds first cult cell or lowers fear | failure raises public fear |
| Military police sweep | baseline and Evolution I | raids barracks, prisons, and kitchens | infantry equipment, command power, stability hit if harsh | lowers discipline collapse and cult pressure | harshness raises fear and resistance |
| Prison transfer freeze | Evolution I | stops POW and prisoner route spread | command power, convoy or train reduction, relations hit if allies affected | lowers spread pressure | overcrowding raises hunger pressure |
| Chaplain or political officer work | Evolution I | ideological and moral counter-pressure | army XP, stability, ideology-specific advisor or law support | lowers cult pressure without mass arrests | slow and weak during high hunger |
| Public truth commission | Evolution I or aftermath | admits the crisis and rebuilds trust | stability, war support, political power, local support | lowers public fear and future leak damage | can reveal exploit choices and add condemnation |
| Island inspection squadron | Evolution II | sends ships, aircraft, and inspectors to remote territories | convoys, fuel, naval or air access, command power | lowers island silence or reveals commune | missing ships raise fear and can trigger event |
| Emergency evacuation | Evolution II | removes garrison or civilians from a silent region | convoys, trains, fuel, manpower, state control | removes local pressure if early | failure spreads exposure to port country |

### Suppression path decisions

Suppression should be effective but costly. It can create temporary stability damage and military disruption. It should not become a simple good button.

Decision families:

- targeted military trials
- prison kitchen seizure
- officer purge of compromised commands
- guarded burial and evidence recovery
- interdiction of black-market ration routes
- allied alert and prisoner-transfer treaty
- kill or capture cult officer missions

Suppression success should raise containment and lower cult pressure. Suppression failure should create named incidents, not silent variable changes.

### Logistics path decisions

The logistics path is the safest long-term response. It should be expensive and hard during active war.

Decision families:

- emergency ration rail mission
- port convoy inspection
- field bakery repair
- supply hub reinforcement
- winter or jungle ration adaptation
- medical triage program
- prisoner camp food audit
- foreign relief request for small countries

These decisions should use real map requirements. The player may need to hold a rail hub, keep a port open, place supplied divisions in a region, or spend trains and fuel.

### Secrecy path decisions

Secrecy is a tempting delay tool. It lowers immediate public fear but raises hidden spread and leak severity.

Decision families:

- censor battlefield letters
- move the court files
- pressure reporters
- transfer suspects without trial
- seal hospital ledgers
- deny allied inspectors

The UI should warn that secrecy prevents panic but makes later discovery worse. It should not reveal exact hidden outcomes.

### Exploitation path decisions

Exploitation is the dark route. It should be available only when the country meets one of these conditions:

- fascist or extremist route
- low stability and severe desperation
- high chaos
- exploit choice taken in opening event
- country already uses terror systems or has active genocide or atrocity mechanics
- Hannibal influence exists

Exploitation actions:

- weaponize terror rumours against enemy units
- recruit compromised assault detachments
- use prisoner fear as counter-resistance policy
- stage false surrender larders
- send cultic infiltrators behind the line
- bargain with a cannibal country for temporary military aid

Costs and risks:

- stability and war support damage
- increased cult pressure and Hannibal resonance
- condemnation when exposed
- death-system impact
- chance of cannibal unit defection
- civil conflict or leader scandal after repeated use

Exploitation should never be a safe power path.

## Timed missions and objectives

Missions should make the player act on the map or commit resources. Avoid passive stockpile checks.

| Mission | Trigger | Objective | Duration band | Success | Failure |
| --- | --- | --- | --- | --- | --- |
| Guard the ration rail | low supply front | hold rail hub or route and keep supplied divisions in target states | 100 to 140 days | lower hunger pressure and unlock safer convoy decisions | raise hunger and create field disappearance state |
| Audit the field hospitals | missing wounded report | spend support equipment and keep target state supplied | 90 to 120 days | reveal or remove first cell | public fear and cult pressure rise |
| Seal the prison kitchens | POW or prison spread risk | control target state, spend infantry equipment and command power | 90 to 130 days | lower spread pressure | prisoner riot or cult courier event |
| Inspect the silent island | island silence threshold | keep naval access, spend convoys and fuel, optionally station ships or planes nearby | 120 to 180 days | remove island silence or reveal commune early | ships vanish and Evolution II chance rises |
| Evacuate the garrison | remote severe case | move garrison by convoy or rail before the timer ends | 90 to 160 days | clears state pressure at high cost | exposure reaches evacuation port |
| Break the ritual cell | Evolution I cell found | raid named state with divisions and equipment | 90 to 130 days | lowers cult pressure and containment rises | cult becomes organized in that state |
| Retake the island commune | before country formation | control nearby port and land divisions or naval forces | 120 to 180 days | prevents cannibal country formation | commune declares itself or joins another cannibal actor |
| Stop the mainland copying | after first island case | inspect ports, hospitals, and prison transfers in mainland state group | 120 to 180 days | delays Evolution III | mainland hunting ground appears |

## Aftermath decisions

Countries that contained the outbreak should receive a smaller category or a temporary aftermath subsection.

Aftermath actions:

- veteran screening
- memorial and record sealing choices
- ration audit reform
- allied evidence handover
- captured cult archive review
- dismantle terror units if exploitation path was used
- hunt escaped cult officers

Aftermath should matter. A clean containment country can resist future spread better. A secrecy containment country can suffer a later leak. An exploitation country can become a Hannibal recruitment node.

## Scripted GUI recommendation

The mechanic benefits from a small custom window after Evolution I. It should be opened from the decision category and should not replace normal decisions.

Window concept:

- left side shows four meters, Hunger, Discipline, Cult, Fear
- center shows a selected risk region card with state names or a named region
- right side shows response posture and active missions
- bottom shows spread channels as locked, suspected, active, or sealed
- Hannibal resonance remains hidden until the future Hannibal event or a high-chaos reveal

Clickable GUI buttons should call the same scripted effect families as decisions. The AI must use equivalent decisions or scripted pulses. No human-only exploit button should exist.

Animated GUI states:

- static baseline seal for first report
- warning pulse when cult pressure is revealed
- animated ration ledger with blood seep effect at high public fear
- animated island signal card when island silence is active
- animated Hannibal hook state only after Hannibal exists

All animations require real frame source art, frame sheets, static fallbacks, and manifest entries.
