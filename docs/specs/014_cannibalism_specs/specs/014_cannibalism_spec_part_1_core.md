# Event 014 Cannibalism, core specification

This is the source design for Event 014 Cannibalism.

The event begins as a war horror incident inside one country at war. It can be contained if the first country acts early and keeps the reports inside the armed forces. If the first response fails, the incident becomes a cultic military infection that spreads through prisoners, deserters, island garrisons, and occupied territories. At high chaos it can produce isolated cannibal countries, a global hunger network, and a hidden-leader world-end route.

The planning package uses working labels for routes, assets, countries, and super-event roles. These labels are not final localisation. Implementation must write final player-facing text from the tone directions and must research any source-dependent super-event title, quote, cultural remark, or audio.

## Source of truth for classification

The user-provided catalog entry is the source of truth for this spec. Event 014 is a Minor Fire-Once event and begins disabled until implementation reworks it. The uploaded workbook row currently records the event as Minor Repeatable and To Be Reworked. The implementation pass should update the workbook only after in-game event details and evolution wording exist.

The event does not belong to any cluster. It should stay outside event clusters unless a later accepted cluster design explicitly adds war-horror incidents as a cluster family.

## Design promise

The first player-facing incident should feel like a military discipline failure caused by hunger, exhaustion, ruined logistics, poor command, and prolonged war. The player should first see reports that are incomplete, disputed, and hard to verify. Commanders deny the worst claims. Field hospitals whisper about missing wounded. Prisoner transfers become hard to audit. Supply clerks report sacks that were never requisitioned.

The system then turns that first horror into a playable containment crisis. The country can respond through investigation, ration reinforcement, unit rotation, military police, courts-martial, prison oversight, field kitchens, evacuation corridors, island inspections, and propaganda suppression. These actions should cost concrete resources such as infantry equipment, support equipment, trains, convoys, fuel, command power, army XP, manpower, stability, war support, supply control, and divisions committed to named regions.

The event has three identities that should remain separated across its progression.

1. Baseline war horror. The issue is discipline collapse and survival panic inside exhausted units.
2. Cult formation. The issue becomes ritual, recruitment, and a hunger ideology that spreads between countries.
3. Cannibal statehood and hidden-leader integration. The issue becomes a military actor, a world threat, and a possible terminal route.

Baseline progression is not the same as evolution. The ordinary crisis can rise from report to outbreak to containment or local failure. Evolutions are mutation tracks that add new rules, new actors, and new presentation.

## First firing target selection

The first country should be chosen from countries at war. The target weight should rise from conditions that make the report believable and dangerous.

Strong positive target factors:

- long war duration
- low national stability
- low war support
- high recent military casualties
- low manpower reserve
- low supply in active combat states
- divisions in cut-off pockets
- fighting in mountains, jungle, desert, arctic, swamp, or islands
- occupied territory with high resistance
- prison camps, field hospitals, or remote garrisons under pressure
- active famine, plague, disaster, mass panic, or chemical and biological contamination from other Chaos Redux systems
- existing death-system pressure in the country
- high chaos tier

Negative target factors:

- high stability
- high supply and strong logistics
- short war duration
- strong field hospital and supply technology
- no divisions near enemy lines
- no active combat or fronts
- already contained cannibalism in the same country without spread
- being a special nonhuman country where human military discipline does not apply

The event should never pick a country that is not at war for the first baseline firing unless a triggerable scenario deliberately bypasses normal selection. It should avoid dead tags, subjects without their own army, tags marked as actual nonhuman countries, and countries whose state ownership makes follow-up decisions impossible.

## Opening incident structure

The entry event, working id `chaosx.nr14.1`, should be a hidden bootstrap that selects or receives the target country and prepares variables.

The first visible country event should use a serious report style and should not state that a global cult is starting. It should describe the public record of the first incident and the command dispute. The player should understand that something has gone wrong in the army, that discipline and manpower are at risk, and that ignoring the report will make later containment harder.

The first country receives the baseline national spirit, working label `cannibalism_in_the_ranks`. The spirit should be staged and should change as the country responds.

Opening mechanical direction:

- moderate stability loss
- small war support loss if the public report leaks
- weekly manpower drain that scales with exposed divisions and severity
- lower division organization recovery or supply grace in affected fronts
- a small military experience or command power disruption penalty
- hidden variables for hunger pressure, discipline collapse, cult pressure, spread pressure, containment, and public fear
- a decision category opens for containment actions
- the Event Details entry records the incident as a war horror and discipline crisis, not as an immediate world threat

The first option set should define response posture. Final option text belongs to localisation, not this spec.

Response posture directions:

- Official discipline response. Serious military command tone. Reduces discipline collapse through courts, rotations, and field policing. Raises fear if too harsh.
- Logistics response. Practical supply tone. Costs trains, convoys, fuel, support equipment, and civilian factory burden. Slower, safer, better for democracies and stable states.
- Secrecy response. Bureaucratic denial tone. Short-term stability protection, higher hidden spread pressure, worse leak later.
- Exploit response. Cruel high-risk tone for desperate or extremist governments. Unlocks terror use and cult infiltration risks. It should be route-locked, chaos-weighted, and dangerous.

## Core mechanic values

Use dynamic values and central constants. The implementation can choose exact names, but the mechanic needs these conceptual values.

| Value | Meaning | Visible to player | Main sources | Main sinks |
| --- | --- | --- | --- | --- |
| Hunger pressure | How much battlefield scarcity and supply collapse push soldiers toward the first taboo | yes | low supply, long war, casualties, pocketed units, famine, disasters | ration decisions, supply corridors, rotating divisions |
| Discipline collapse | How far normal command authority has failed | yes | low stability, low war support, failed missions, secrecy leaks, exploited terror | military police, courts, officer inspections, successful missions |
| Cult pressure | How far acts have become ritual and ideology | yes after Evolution I | repeated incidents, prison infiltration, exploit choices, hidden-leader reveals, island isolation | arrests, deradicalisation, chaplain and medical work, exposure missions |
| Public fear | Civilian and military panic from rumours, missing persons, and state modifiers | yes | leaks, state disappearances, island silence, failed trials, nearby cannibal country | truthful briefings, relief work, restored order, defeat of cannibal states |
| Spread pressure | Chance the event crosses borders or jumps to a new country | partly visible | POW transfers, fronts, refugees, ports, remote garrisons, high chaos | prisoner audits, border quarantine, convoy inspection, allied warning |
| Containment | Country progress toward defeating the active outbreak | yes | successful decisions and missions | failed missions, new incidents, cult sabotage |
| Island silence | Remote territory risk used for islands, colonies, and cut-off coastal enclaves | visible after first island case | cut-off ports, island garrisons, low convoys, failed inspections | convoy escorts, naval patrols, evacuation missions |
| hidden-leader resonance | Sealed-leader buildup for Event 014 | hidden until Evolution II seeds the hidden leader | cult pressure, ritual ideology, cannibal countries, global spread | none until the reveal route is active |

No single value should decide everything. The event should feel alive because the values interact. For example, low hunger pressure with high cult pressure means ideology has survived after the original scarcity ended. High hunger pressure with low cult pressure means a conventional military and logistics response can still solve the crisis.

## Baseline stages

Baseline stages are ordinary crisis progression and should not be logged as evolutions.

### Baseline Stage 0, rumours and missing wounded

This is the first visible stage. It has one affected country and no infected state modifier yet unless the opening target state is already severe.

Playable behavior:

- opens the containment category
- applies the first national spirit
- starts a low weekly manpower drain
- creates a first target region from the active war front or from a high-risk garrison
- allows early containment victory if the player uses several successful responses before cult pressure rises

### Baseline Stage 1, confirmed military outbreak

This begins if hunger pressure or discipline collapse reaches the first threshold, if a first mission fails, or if the player ignores the category.

Playable behavior:

- adds the first affected state modifier, working label `field_disappearances`
- increases weekly manpower drain and local resistance risk
- unlocks missions to secure kitchens, field hospitals, prisons, or depot routes
- adds a chance for a minor news event if public fear is high
- gives nearby enemies, allies, or faction leaders a hidden diplomatic awareness flag

### Baseline Stage 2, containment race

This begins when the country has more than one affected state, when public fear spreads, or when spread pressure becomes meaningful.

Playable behavior:

- creates a time-limited containment mission
- forces the player to choose between military, medical, logistics, and secrecy postures
- adds target state groups by front, prison region, supply corridor, or island chain
- creates a chance of cross-border exposure after prisoner exchanges, encirclement breaks, evacuation convoys, or port transfers

### Baseline Stage 3, local victory or local failure

The country reaches a local outcome.

Victory requires containment above threshold, cult pressure below threshold, no active cannibal state modifier, and no recent spread jump. Victory removes the national spirit or replaces it with a temporary aftermath spirit about military trauma and inspections. If no other country has an active outbreak, the global system goes dormant and Event 014 is considered defeated for the campaign unless a triggerable scenario or hidden-leader branch deliberately reopens it.

Failure occurs if cult pressure and spread pressure remain high, if affected states persist too long, if an island silence case matures, or if the player chooses exploitation repeatedly. Failure does not automatically create a cannibal country. It prepares Evolution I and Evolution II entry paths and makes cross-border spread possible.

## Containment victory and re-entry rules

A country that defeats its own outbreak receives a country flag marking local containment. This should prevent ordinary Event 014 decisions and spirits from returning to that country through routine spread for a long cooldown. It does not make the country immune to cannibal countries, military invasion, sealed-unifier world-end mechanics, or triggerable scenarios.

If the event never spread beyond the original country, local victory also clears global active flags. If it spread to other countries, each country must defeat its own outbreak. One country winning does not solve the world.

A contained country can re-enter only through strong conditions:

- cannibal country controls a border state or nearby island
- hidden-leader mechanics explicitly target the country
- the country chooses to exploit captured cannibal networks
- a triggerable scenario forces it
- world-end route is active and no normal immunity applies

## Spread model

Spread should be rare at baseline and more common after Evolution I.

Spread channels:

- shared front lines after prolonged battles
- prisoner transfers and prison camps
- deserters entering an allied or neutral state
- evacuation convoys and refugee routes
- cut-off island garrisons
- military hospital transfer chains
- black-market food networks
- occupation zones with high resistance
- cult envoys unlocked by Evolution I
- hidden-leader-linked recruitment after the reveal route is active

Spread should target countries that are at war or directly connected to a war zone. A peaceful country can receive an exposure event only through refugees, ports, occupied territory, or a cannibal country bordering it. Peaceful exposure should begin as public fear, port inspections, or prison rumours, not as immediate unit cannibalism.

Spread should respect country size and target validity. The system should not spam tiny countries with impossible containment categories. Small countries can receive a compact response package and can call for foreign help.

## Relationship with Chaos Meter systems

Event 014 should interact with Chaos Redux systems without hijacking them.

Chaos Meter:

- first firing adds a small chaos increase
- successful containment can reduce chaos slightly if no spread occurred
- exploit choices, state disappearances, cannibal country formation, and hidden-leader integration add larger chaos
- chaos tier changes evolution chance, opening severity, and AI risk tolerance

Deaths system:

- baseline military cannibalism causes a small military death log over time
- state disappearances cause civilian deaths only when state modifiers become active
- cannibal countries cause serious civilian deaths in controlled states through weekly consumption and displacement
- world-end route can create fast death-system pressure

Condemnation:

- ordinary containment does not add condemnation
- secrecy can create diplomatic penalties when exposed
- exploit choices add condemnation or hidden atrocity visibility when the government knowingly uses cannibal terror
- cannibal countries are treated as world threats rather than normal condemned regimes once they begin open rampage

Air cleanliness:

- no direct air contamination interaction is needed
- contaminated or outbreak states from chemical and biological warfare can raise hunger pressure and public fear through local chaos

World threat framework:

- Evolution III or a large cannibal country should add a cannibalism source to the shared world threat state
- this source should be cleared after the global cult is defeated and no cannibal country or high-level cult network remains

## Connections with other events

Event 014 should connect where the link improves play.

Useful links:

- Natural Disasters can raise hunger pressure after famine, drought, flood, ash, crater, or refugee aftermath
- Black Plague can increase public fear and make quarantine costs cheaper or more accepted
- Disease in Divisions can create false positives and make the first reports harder to identify
- Mass Panic can amplify fear, leaks, and decision category urgency
- Zombie Outbreak should be classified differently from cannibalism, but high chaos can make observers confuse the two in report direction
- Fury can increase long war and atrocities pressure, which makes cannibalism target weight higher
- Independence Wave and civil wars can make breakaway prisons, depots, and garrisons harder to inspect
- the hidden leader should become the later ideological recruiter, leader, or unifier when that event is implemented

Avoid artificial links:

- Event 014 should not become a chemical or biological warfare system
- Event 014 should not become a generic disease, zombie, or vampire system
- Event 014 should not create the terminal route until the hidden-leader reveal and a large global cult network justify it

## Player-facing tone direction

Early event tone should be restrained and investigative. The country is trying to determine whether the report is a slander, a starvation crime, a military breakdown, or something worse. Player-facing text should avoid revealing the cult path early.

Mid-stage tone should show institutions buckling. Field kitchens, prisons, hospitals, and transport offices matter more than borders or maps.

High-chaos tone can become overtly monstrous. It should imply that people are choosing or becoming something inhuman, especially near hidden-leader mechanics, while still treating the baseline as human collapse.

Option tone should vary by response posture. Logistics options should sound practical. Military justice options should sound severe. Denial options should sound bureaucratic and self-protective. Exploit options should sound self-damning and cruel, not funny.

No final localisation belongs in this spec. The implementation should write final event text later.
