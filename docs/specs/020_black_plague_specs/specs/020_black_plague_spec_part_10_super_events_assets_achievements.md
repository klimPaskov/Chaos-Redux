# 020 Black Plague spec Part 10 - Super-events, assets, and achievements

This part expands the presentation layer for Black Plague. It defines super-event roles, asset families, animation needs, achievement design, and research handoffs. It does not provide final super-event titles, quotes, cultural remarks, button text, audio selections, event text, focus text, decision text, or achievement titles.

All labels are working labels only and are not final localisation.

## Presentation rule

Black Plague has several layers. Each layer should use the right level of presentation.

| Moment | Presentation direction |
| --- | --- |
| first infected state | report or ordinary event, not a super-event unless extreme scenario launch needs it |
| severe local outbreak | report event or disease board update |
| Evolution I stronger strain | evolution log and report direction |
| Evolution II overseas spread | evolution log and possible news report if islands or ports are hit |
| first rat nation | news or report event, super-event only if the outbreak is already regional and public |
| King of Rats | required super-event because the threat changes into organized nonhuman statehood |
| King controls a continent or reaches terminal path | escalation super-event candidate if it does not overlap with world-end |
| rat world-end | required world-end super-event |
| defeat of major King threat | defeat aftermath super-event candidate if the war was global or near-global |

The implementation should avoid super-event inflation. Use super-events for thresholds that change the campaign, not for every infection stage.

## Super-event role map

### Package A: King reveal

Working role label: `king_reveal`.

Trigger direction:

- Evolution IV creates the King of Rats
- the King is a separate country and not only a renamed base rat nation
- all rat-held states and units are transferred or unified under the King
- human countries can see that scattered warrens have become organized

Purpose:

- marks the shift from uncontrolled disease and scattered nonhuman nests to a sentient rat state
- opens deeper King focus tree and global threat logic
- should make players understand that the crisis has changed type

Text direction:

- title direction: short and specific to organized rat sovereignty, research-gated
- description direction: public understanding of a new nonhuman ruler or organized warren realm, without dumping mechanics
- quote direction: real sourced quote about plague, sovereignty, vermin, judgement, hunger, or creatures inheriting ruined spaces
- cultural remark direction: short researched allusion that fits rat sovereignty or plague without cheap comedy

Image direction:

- generated super-event image
- strong central nonhuman sovereign or symbolic rat court
- 1936 to 1945 inspired documentary or painted HOI4 super-event tone if appropriate
- no readable generated text
- avoid a generic map table or abstract skull icon

Audio direction:

- real public domain or clearly licensed musical track
- solemn, strange, court-like, plague procession, or choral dread direction
- no generated tones, drones, or placeholder audio

### Package B: rat world-end

Working role label: `rat_world_end`.

Trigger direction:

- King of Rats completes the world-end path
- required continent or state-set control is met
- death and rat-held territory pressure is high enough
- existing world-end rules are satisfied

Purpose:

- terminal scenario where the King of Rats has taken over the world
- campaign state becomes resolved into rat sovereignty and Black Death ecology

Text direction:

- title direction: finality and rat world direction, research-gated
- description direction: human order has collapsed and the world is governed by rat ecology, without generic apocalypse wording
- quote direction: real sourced quote about endings, inheritance, judgement, beasts, silence, plague, or the fall of human pride
- cultural remark direction: short researched allusion that fits finality, no unsourced lyric or meme reference

Image direction:

- generated super-event image
- vast rat-held capital, ruined human symbols, black fog, crown or warren geometry
- strong central composition that reads at super-event size
- no readable text

Audio direction:

- unique real track with finality
- public domain or clearly licensed
- choral, funeral, processional, or dark orchestral direction

### Package C: continental rat threat escalation candidate

Working role label: `continental_rat_threat`.

Use only if implementation wants a middle threshold between King reveal and world-end.

Trigger direction:

- King controls a large share of a continent or event-defined continent group
- world-end path not yet completed
- human powers still have a chance to stop it

Purpose:

- marks a regional order collapse and opens emergency cooperation
- should not duplicate the world-end super-event

Presentation direction:

- super-event candidate if the threshold feels campaign-defining
- otherwise use a major news event and disease board escalation

Research gates:

- title, quote, button, and audio remain unresearched until a super-event pass accepts this package

### Package D: defeat aftermath candidate

Working role label: `rat_defeat_aftermath`.

Use only if the King was a global or near-global threat.

Trigger direction:

- King of Rats is defeated after controlling a large region, causing massive deaths, or nearing the world-end path
- major warren remnants are cleaned or contained enough to declare the war over

Purpose:

- marks costly survival and the long cleanup after a rat war
- should not fire for a tiny base warren defeated quickly

Text direction:

- recovery, missing population, ruined infrastructure, and vigilance
- reflective rather than triumphant
- no final quotes or remarks in this planning file

Image direction:

- generated or sourced depending on whether the final scene must be fictional or archival-like
- likely generated documentary-style aftermath scene, black fog residue, cleanup lines, troops and doctors in ruined districts

Audio direction:

- reflective music, not victory fanfare

## Super-event research handoff

The super-event research prompt must ask the researcher to:

- compare several real quote candidates for each accepted package
- verify exact wording and attribution from reliable sources
- keep direct quotes short enough for UI and copyright limits
- research cultural remark candidates separately from main quotes
- find unique real audio for each completed super-event
- verify license and recording rights
- document source URL, author, performer, license, duration, and use case
- coordinate generated or sourced image needs with asset subagents

Unresearched titles, quotes, remarks, slogans, lyric fragments, allusions, and audio choices are blockers for implementation. They must not be converted into final localisation.

## Visual asset family map

### Disease and state visuals

| Asset | Type | Source mode | Size direction | Use |
| --- | --- | --- | --- | --- |
| Black Death disease icon | disease UI or decision icon | generated | existing shared disease UI size | identifies Black Death in shared disease board |
| black fog map overlay | mapmode or GUI state | generated or scripted visual | engine-dependent | shows infected states dynamically |
| infected state card overlay | scripted GUI | generated | UI-specific | disease board selected state card |
| contained state marker | mapmode or UI | generated | UI-specific | marks contained but not cured state |
| recovery residue marker | mapmode or UI | generated | UI-specific | cured or recovering state with relapse risk |
| weaponized-hit marker | mapmode or UI | generated | UI-specific | marks recent Black Death weapon deployment |
| port-risk marker | UI or mapmode | generated | UI-specific | marks overseas risk after Evolution II |

### Disease board UI assets

| Asset | Type | Animation need | Use |
| --- | --- | --- | --- |
| shared disease board header | UI panel | optional static | category identity within shared disease system |
| Black Death seal | decision category or GUI seal | animated recommended | changes from calm to infected to severe to rat threat |
| disease load meter | GUI meter | static variants or animation | selected state disease load |
| cure progress meter | GUI meter | static variants or animation | cure thresholds and cleanup unlocks |
| spread route panel icons | UI icons | static | border, port, troop, refugee, weapon, rat routes |
| active mission warning frame | UI frame | animated if useful | severe outbreak and rat threat missions |
| rat warning mark | UI warning | animated recommended after Evolution III public reveal | warren pressure and rat border state |

### Decision and mission icons

| Family | Required icons |
| --- | --- |
| preparedness | surveillance, stockpile, emergency health law |
| threatened state | border controls, port inspections, troop restrictions, refugee corridor |
| infected state | quarantine, lockdown, hospitals, field medicine, cleanup crews |
| cure research | national cure, sample sharing, treatment deployment |
| weaponization | sample study, safety program, payload project, accident response |
| anti-rat | cordon, field operation, border fortification, evacuation, burnout operation |
| international coordination | medical aid, containment coalition, research sharing |

Decision icons must be designed for 32x32 and cannot be resized focus icons.

### Focus icon families

Base rat focus icons:

| Lane | Motifs |
| --- | --- |
| Awakening warren | nest, tunnel mouth, first swarm, broken floorboards |
| Swarm growth | brood chamber, mass rats, corpse-fed movement, hidden reserves |
| Plague ecology | black fog, grain stores, port vermin, sick roads |
| Human war | wire line, night attack, supply sabotage, tunnel breach |
| Warren defense | burrow fort, ruins, hidden litters, plague moat |
| Absorption | two nests merging, tooth right, inherited brood |
| King preparation | crown instinct, black court below, all warrens answering |

King focus icons:

| Lane | Motifs |
| --- | --- |
| Coronation and sentience | rat crown, throne below, first law, speech of teeth |
| Royal command | crown command, elite guard, command tunnels |
| Brood council | council nest, many eyes, patient warren |
| Hunger mind | single appetite, devour roads, endless gnawing |
| Swarm command | tunnel signal, King guard, continental swarm |
| Warren economy | scavenged surface, gnawed factories, corpse fields |
| Plague mastery | black fog nests, cure resistance, harbor warrens |
| Human terror | empty village, broken hospital, roads run black |
| Rat unity | no lesser crowns, one underground realm |
| Continental conquest | plague belt, ports of swarm, continent below |
| World-end path | every road a tunnel, crown below continent, rat world threshold |

Focus icons use 94x86 and require asset-specific generation. They must not be derived from decision icons.

### Ideas and national spirits

| Idea family | Icon direction |
| --- | --- |
| Black Death state modifier | black fog over city or field, compact and readable |
| Contained infection | black fog held behind cordon or medical mark |
| Recovery residue | pale residue and cleanup mark |
| Weaponized exposure | sealed plague mark, not technical lab imagery |
| Base warren | nest or swarm silhouette |
| Nonhuman swarm | rat mass and tooth shape |
| Plague ecology | black fog and tunnel roots |
| Burrowed state | underground nest under ruins |
| Crowned warren | rat crown and warren geometry |
| Royal command | crown and command tunnel motif |
| Brood council | council nest motif |
| Hunger mind | single hunger mark, high-chaos and readable |
| Broken crown | cracked rat crown or broken warren symbol |

Idea icons use 64x64 and should be separate from focus icons.

### Country assets

Base rat nations need:

- base flag for each rat tag in normal, medium, and small sizes
- optional dominant warren cosmetic flag
- institutional or creature leader portrait
- country name, adjective, party, and ideology localisation direction
- focus tree icons and idea icons

King of Rats needs:

- base King flag in all sizes
- Royal Command flag variant in all sizes if route uses flag change
- Brood Council flag variant in all sizes if route uses flag change
- Hunger Mind flag variant in all sizes if route uses flag change
- King leader portrait
- route portrait overlays or variants
- animated portrait package if produced
- super-event image for reveal and world-end

### Unit and warfare assets

| Asset | Use |
| --- | --- |
| warren swarm unit icon | baseline rat division family |
| sewer rush unit icon | fast urban attack family |
| plague gnawer unit icon | plague attack family |
| burrow guard unit icon | defensive family |
| brood mass unit icon | late mass family |
| King guard unit icon | elite King route unit |
| anti-rat doctrine icon | human counterplay research or idea |
| cordon operation icon | anti-rat decision |
| nest assault icon | operation decision |
| burnout cleanup icon | recovery decision |

### Report and news images

Report event image candidates:

| Moment | Source mode | Direction |
| --- | --- | --- |
| first outbreak state | generated period-documentary | crowded neglected district, sickness, black fog implication, no readable text |
| first severe collapse | generated period-documentary | overwhelmed streets, improvised hospitals, abandoned markets |
| first rat warren | generated fictional documentary | ruined district with nonhuman sign, no clear King reveal |
| retaken warren cleanup | generated period-documentary | soldiers and medical crews clearing ruins |

News image candidates:

| Moment | Source mode | Direction |
| --- | --- | --- |
| Evolution II overseas spread | generated or sourced-like period news | port quarantine and ships, black and white |
| first rat nation public | generated period news | panicked border or ruined town, no final text |
| King military breakthrough | generated period news | rat war front, black fog, troops retreating or holding line |
| King defeated after major war | generated period news | cleanup and survivors, reflective tone |

All report images need report-card processing. News images must be black and white.

## Animation planning pass

Animation is useful for Black Plague because the disease is stateful and visual. The asset prompt should require actual frame plans, source frames, static fallbacks, and frame-sheet DDS files where animation is accepted.

Recommended animated assets:

| Animated asset | Surface | State logic | Frame direction |
| --- | --- | --- | --- |
| black fog state card | disease UI | exposed, infected, severe, collapse | 6 to 10 source frames, fog shifts without readable text |
| disease board seal | decision category or GUI | calm, threatened, infected, rat threat | separate source frames for each state or static variants if animation is too noisy |
| rat warren warning | UI warning | normal, high pressure, critical | 6 to 8 frames, subtle pulse from source frames |
| King portrait overlay | leader portrait or super-event adjacent | route and high-chaos state | generated frame set with clear static fallback |
| world-end progress frame | King UI or focus route card | late terminal path active | 8 to 12 frames, black fog and crown geometry |

Animation should not be created from a shifted or recolored still image. If real frame production is blocked, the asset should remain static and the blocker should be reported.

## Achievement suite expansion

Achievements are working designs. Final titles and descriptions are localisation work. Every achievement needs an icon direction and tracking plan.

| Working key | Eligible country | Difficulty | Hidden | Unlock direction | Disqualifier direction | Icon motif |
| --- | --- | --- | --- | --- | --- | --- |
| `020_black_plague_clean_room` | any country with first infected state or outbreak owner | hard | visible | contain and cure the first outbreak state before it spreads to another state | weaponize Black Death or let state reach collapse | clean cordon around dark state |
| `020_black_plague_no_graves_left_open` | any country | hard | visible | suffer severe Black Death deaths, reach mature cure progress, clean all owned infected states, never weaponize | use Black Death payload or lose a state to rats | hospital and black fog fading |
| `020_black_plague_firebreak_continent` | any country on threatened continent | very hard | visible | after Evolution II, prevent any overseas infection from establishing on the player's home continent for a long period | own an infected port on home continent | port cordon and continent mark |
| `020_black_plague_black_doctor` | bio-capable country | hard | hidden | study Black Death defensively and reach high cure contribution without causing a home accident | weaponized deployment or major lab accident | mask and sealed sample, abstract |
| `020_black_plague_bad_idea_survived` | bio-capable country | very hard | hidden | weaponize Black Death, deploy it, then avoid domestic outbreak and survive diplomatic backlash | domestic collapse or world-end from rats | cracked payload and shield |
| `020_black_plague_last_quarantine` | country bordering rats | hard | visible | hold a rat border cordon long enough to stop a rat country from entering core states | lose core state to rats | wire line and rat shadow |
| `020_black_plague_first_warren_burned` | any human country | medium hard | visible | destroy the first rat nation before any second rat nation appears | a second rat nation appears first | burning warren mark |
| `020_black_plague_no_crown` | any human country | very hard | hidden | prevent the King of Rats from appearing after Evolution III becomes possible | King appears | broken crown before completion |
| `020_black_plague_crown_hunter` | any human country | very hard | visible | defeat the King after it controls a large region but before world-end path completes | world-end path succeeds | spear or cordon through rat crown |
| `020_black_plague_clean_continent` | any human country | very hard | visible | clear all Black Death, rat-held, and warren-remnant states from a continent after the King existed | leave relapse pressure or warren remnant | continent and cleanup flame |
| `020_black_plague_play_the_warren` | base rat nation | hard | hidden | as a base rat nation, absorb another rat nation and become the dominant warren | become King too early if achievement requires base form | two nests merging |
| `020_black_plague_crowned_below` | King of Rats | hard | visible | form the King and complete the coronation trunk while holding all inherited warrens | lose capital nest before trunk complete | rat crown below tunnel |
| `020_black_plague_three_minds` | King of Rats | hard | hidden | complete one government route and its matching capstone in separate campaign tracking or route-specific variant | switch route or fail route lock | crown, council, hunger triptych |
| `020_black_plague_continent_under_earth` | King of Rats | very hard | visible | control the required continent group as King without triggering world-end yet | terminal scenario fires before condition tracking | continent tunnel motif |
| `020_black_plague_rat_world` | King of Rats | extreme | hidden | trigger the rat world-end scenario | none beyond normal world-end conditions | world under rat crown |
| `020_black_plague_humanity_returns` | human coalition leader or major | extreme | hidden | defeat a near-terminal King and clean enough states to stop relapse | world-end succeeds or major warren remnants remain | broken crown and sunrise cleanup motif |

Achievement implementation should avoid automatic unlocks. It should track route, evolution, disease, rat country, King, and cleanup state over time.

## Achievement tracking notes

Important tracking flags or values:

- first outbreak state id and whether it spread
- whether player ever weaponized or deployed Black Death
- cure contribution by country
- domestic accident caused by Black Death study
- first rat nation id and whether second appeared
- King formation and King source country
- King maximum controlled states or continent progress
- world-end path started and completed
- rat-held state maximum count
- continent cleanup completion
- warren-remnant cleanup completion
- player country route if playing rats or King

Disqualifiers should be explicit. For example, a clean containment achievement should fail if the disease spreads, if weaponization is used, or if the first state reaches collapse.

## Asset prompt expansion requirements

The asset prompt should be updated to include:

- every focus icon family from Part 7
- every decision icon family from Part 8
- every unit icon family from Part 9
- flags for base rats and King route variants
- portraits for base rat leaders and King route variants
- animated UI assets for disease board state changes
- super-event images for required packages
- achievement icons for the full suite
- report and news image candidates
- source mode and reference folder for each asset type
- exact target sizes from the asset skill
- manifest and DDS handoff requirements

## Super-event prompt expansion requirements

The super-event prompt should include the required packages A and B and optional packages C and D with clear acceptance rules. It must keep all final wording and audio choices research-gated.

The prompt should instruct the text researcher to compare candidates, not choose a generic apocalypse quote. It should instruct the audio researcher to reject unclear licensing and to avoid generated test tones, sound-effect beds, and placeholder tracks.

## Localisation direction

Final text should handle the plague and rat routes with restraint. The disease should be scary because states lose people, roads empty, and governments must choose between damage and control. Rat content can become strange and high-chaos after it becomes public. Early disease text should not reveal rat nations or the King.

No final localisation is provided in this file.
