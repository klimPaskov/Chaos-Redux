# Event 018 Resources Found, Part 4 Assets, Achievements, Localisation Direction, and Completion Standard

All names in this file are working labels only. They are not final localisation.

## Visual identity

The ordinary event should look like a period resource discovery. The high-chaos branch should look like the earth itself has become hostile. The visual progression should move from survey crews, mine equipment, oil derricks, assay tables, rail spurs, and workers, toward corroded galleries, empty camps, evacuation lines, armored cordons, and finally nonhuman bodies emerging from the resource state.

The main visual subject should not default to maps or staff tables. The event is about a place becoming valuable and then dangerous. Asset prompts should focus on people, equipment, caves, resource seams, worker settlements, monsters, evacuation routes, and the Cave Host.

## Asset coverage overview

Required asset families:

| Asset family | Need |
| --- | --- |
| Report event images | discovery, boom, sickness, public attack, closure, Cave Host aftermath |
| News event images | border crisis, Cave Host emergence if implemented as news, world reaction |
| Super-event images | Cave Host reveal, world-end, optional defeat aftermath |
| Decision category icon | resource field category |
| Decision icons | survey, extraction, concessions, security, safety, evacuation, hunts, closure |
| Idea and national spirit icons | boom, concession influence, unsafe extraction, public panic, sealed depths, anti-monster lessons |
| Cave Host leader portrait | generated fictional nonhuman portrait |
| Cave Host flags | fictional flag family, normal, medium, and small sizes |
| Cave Host focus icons | icon motifs for hunger, stone hide, tunnels, brood hierarchy, surface terror, continental maw |
| Cave Host country UI | possible country selection portrait and event-log actor icon if repo pattern supports it |
| Custom UI assets | ledger background, stage seals, meters, warning frames, animated closure seal, animated breach warning |
| Achievement icons | one 64x64 completed icon per achievement, with variants produced by achievement workflow |

Historical source mode is not central here because the Cave Host is fictional. Ordinary report images can be generated period-documentary scenes unless implementation chooses sourced real mining or oilfield photographs. Generated content is appropriate for monsters, fictional cave state, supernatural resource seams, Cave Host portrait, fictional flags, and high-chaos super-event images.

## Animated presentation plan

The event benefits from animated state visuals because the field is a living pressure system.

Animated assets should be planned for:

| Animated asset | Gameplay state | Target surface | Frame direction |
| --- | --- | --- | --- |
| Resource field category seal | field active and stage changes | decision category or scripted GUI | cracks and glow become more visible across stage states |
| Extraction pressure warning | high extraction pressure | ledger meter frame | warning border pulse from real source frames |
| Public panic warning | public attacks active | panic card | trembling or flicker as a frame-sheet animation |
| Closure seal | closure available, last chance, sealed | closure button or card | seal tightens or fractures across state variants |
| Cave breach warning | breach countdown | emergency card | fissure widening and shadow movement |
| Cave Host leader portrait | Cave Host country active | leader portrait or scripted GUI overlay | nonhuman breathing, eye glow, or stone dust, generated as real source frames |
| World-end super-event image variants | not necessarily animated in final HOI4 super-event unless repo supports it | super-event asset handoff | static image is acceptable unless current super-event UI supports animation cleanly |

Every animated asset needs source frames, processed frames, sheet PNG, sheet DDS, static fallback, preview GIF for review only, manifest, and `.gfx` handoff. No final animation may be created by shifting or recoloring one still image.

## Cave Host country package

Working public country label: Cave Host. This is a working label, not final localisation. The final public map name should remain short and direct. It should not use office or administrative naming.

Country package direction:

| Surface | Direction |
| --- | --- |
| Tag | New custom tag, final tag must avoid conflicts. |
| Country type | Special chaos country and actual nonhuman country. |
| Spawn state | Origin resource state. |
| Government | Nonhuman hostile host, ordinary ideology only as engine container. |
| Leader | Literal cave monster, generated fictional portrait, nonhuman metadata where supported. |
| Ruling party | Working label should describe the host or brood, not a normal party. |
| Names | Direct map name, ideology variants can stay close because ordinary politics do not matter. |
| Flag | Fictional mineral, claw, cave-mouth, or black seam motif. No text. |
| Starting ideas | Nonhuman host rules, slow armored bodies, resource-bound broods, surface confusion. |
| Starting army | 8 to 30 unique cave monster divisions based on origin exploitation. |
| Reinforcement | Automatic divisions from controlled non-origin resource states. |
| Production | No normal manpower or equipment recruitment. |
| Diplomacy | Immediate wars on neighbours, no ordinary factions, no normal peace unless defeat logic says so. |
| AI | Resource-seeking, slow, aggressive, prioritizes rich states and continental threshold. |
| Focus tree | Fixed-purpose nonhuman tree with method branches. |
| Assets | Leader portrait, flags, focus icons, idea icons, super-event image, decision icons. |
| Docs | Country package must be documented and classified in shared nonhuman triggers. |

Starting ideas should have lifecycles:

| Idea role | Starting form | Upgrade path | Removal |
| --- | --- | --- | --- |
| Resource-bound host | Explains automatic resource-capacity divisions. | Hunger lane improves spawn timing or state cap handling. | Removed only if Cave Host defeated. |
| Slow armored bodies | Huge armor and low speed. | Stone hide lane strengthens armor at speed cost. | Removed only on defeat. |
| Surface confusion | Early enemy panic and Cave Host disorganization. | Tunnel or terror lane changes it into targeted surface warfare. | Can be replaced by late-game continental maw idea. |
| Origin nest | Origin state special support. | Brood hierarchy lane modifies initial host behavior. | Cleared if origin is lost or sealed. |

## Cave Host focus tree asset direction

Focus icons should form a coherent family, but each icon should be designed as a focus icon at 94x86 and not resized from other icon types.

Focus motif families:

| Lane | Icon motifs |
| --- | --- |
| Opening trunk | cave mouth, mineral crown, first brood, origin nest |
| Hunger lane | resource vein, claw over ore, glowing seam, divided resources |
| Stone hide lane | armored hide, broken bullets, anti-tank silhouette, stone plates |
| Tunnel lane | underground road, roots through rock, mine rail into darkness |
| Brood hierarchy lane | queen or alpha silhouette, brood clusters, larger monster shape, many small shapes |
| Surface terror lane | abandoned street, cave shadow in city, evacuation lanterns, broken barricade |
| Continental maw lane | continent cracked by seams, resource nodes connected underground, multiple cave mouths |

The tree should avoid ordinary national development icons. The Host does not build schools, parliaments, normal factories, or diplomatic corps.

## Achievement design overview

Achievements are required because the event has a deep route, hidden failure, player-controlled prevention, and a playable nonhuman crisis actor.

Achievement design should cover:

- ordinary economic mastery
- diplomatic risk
- safe closure
- overexploitation
- defeating the Cave Host
- playing as or enabling the Cave Host
- preventing world-end
- causing world-end
- resource denial against the Host
- protecting population during public attacks

Achievement titles below are working labels only. Final title and description localisation must be written during implementation.

High-value achievement spread:

| Working label | Route | Difficulty | Why it is not trivial |
| --- | --- | --- | --- |
| Boom Without Blood | Owner containment | Medium | Requires high field richness with low worker deaths and no public danger. |
| Resource Curse | Owner or rival | Medium | Requires losing or seizing the discovery state through border crisis. |
| Close the Mouth | Owner prevention | Hard | Requires closing an Evolution III public danger site before Cave Host emergence. |
| Surveyors Came Back Wrong | Overexploitation | Hard | Requires reaching sickness stage and then containing it without Cave Host emergence. |
| Hard Attack Solves Geology | Anti-Host war | Hard | Requires defeating Cave Host using anti-armor preparation or holding it below a resource threshold. |
| Starve the Deep | Anti-Host war | Very hard | Requires denying Cave Host resource states until its non-origin capacity collapses. |
| The Mine Owns the Map | Cave Host route | Very hard | Requires playing as or switching to Cave Host and controlling a defined number of resource states. |
| Continental Maw | World-end | Secret or very hard | Requires Cave Host world-end scenario conditions. |
| All That Glitters | Ordinary repeatable mastery | Medium | Requires several ordinary discoveries across different resource types without triggering public danger. |
| Paid in Concessions | Diplomacy | Medium | Requires using multiple foreign concessions without losing the state or becoming a puppet. |
| The Last Shift Came Home | Humanitarian | Hard | Requires completing evacuation and safety missions with low deaths during public attacks. |
| Sealed Riches | Sacrifice | Hard | Requires closing an every-resource Evolution III site before breach. |

Achievement icons should use direct visual motifs, not text. Completed icons should be generated separately from focus or idea icons.

## Localisation direction

The planning spec does not provide final localisation. Implementation must write final text from these directions.

### Discovery text direction

The discovery popup should focus on local discovery work, the state, the resource type, and the sudden economic importance. It should avoid direct effect listings. It can use confident or lightly ironic tone because the baseline is a positive minor event.

Dynamic references:

- owner country name
- state name
- resource type
- possibly a generic survey actor, such as miners, geologists, oil crews, or local authorities, based on resource type

Avoid:

- final cave monster spoilers
- exact hidden variables
- generic map-change framing
- staff-table crisis cliches
- effect-list descriptions

### Trade and diplomacy text direction

Diplomatic text should make the field feel useful and contested. It should show foreign companies, importers, smugglers, consulates, military survey teams, and resource-hungry governments. It should not use bland diplomatic panic templates. Foreign reactions should vary by relation, ideology, resource need, border status, and war state.

### Sickness text direction

Sickness text should describe worker harm, corroded equipment, strange fatigue, missing shifts, and medical uncertainty. It should not directly state that this is a warning of monsters. It should not announce hidden mechanics. The player should see the cost of continued extraction through observed effects and decision pressure.

### Public danger text direction

Public danger text can become sharper and more frightening. It should describe monsters seen in settlements, evacuations, public attacks, rail closures, and people fleeing cities. It should avoid cheap comedy. It should still keep final monster taxonomy vague unless the Cave Host has emerged.

### Cave Host text direction

After Evolution IV, the country is public. Text can name the nonhuman threat, but final names remain implementation-owned. Tone should be severe, strange, and physical. The leader is literally a cave monster. The country should not sound like a normal cabinet.

### Cave Host focus text direction

Focus text should not read like normal national development. It should describe instincts, tunnel systems, brood organization, stone bodies, hunger for resource-rich states, and surface war. It should avoid humanoid political slogans unless used as foreign interpretation.

### Event detail direction

Event Details should describe the event premise and visible stages. It should not list resource numbers, modifiers, or hidden risk formulas. It can mention that excessive exploitation can make the state unstable once the relevant evolution exists, but it should not spoil the final Cave Host in the baseline details.

### Spreadsheet direction

Spreadsheet fields should mirror final in-game event detail and evolution detail wording after implementation. The spreadsheet worker should update the workbook only after final localisation exists.

## Super-event direction

Super-event research gates:

| Super-event | Title | Button remark | Quote | Audio |
| --- | --- | --- | --- | --- |
| Cave Host reveal | research required | research required | research required | licensed or public domain track required |
| World-end | research required | research required | research required | licensed or public domain track required |
| Defeat aftermath | research required if implemented | research required if implemented | research required if implemented | licensed or public domain track required |

The image direction can be planned now, but final text and audio cannot be accepted until researched and documented.

## Implementation acceptance standard

The implementation should not be marked complete unless these surfaces are finished or explicitly reported as blocked:

- random event registration and Minor Repeatable classification
- valid state and resource selection
- baseline resource deposit around 100 of one random resource
- repeatable ordinary fields and one primary deep site rule
- owner popup and event log entry
- event details and spreadsheet-aligned wording after final localisation
- decision category with values, staged decisions, costs, AI, and cleanup
- diplomacy and trade reactions
- border crisis and possible state transfer if valid
- demilitarized field pressure in Evolution I
- worker sickness and deaths system integration in Evolution II
- public monsters, evacuation, hunts, closure, and population loss in Evolution III
- Cave Host country package in Evolution IV
- Cave Host nonhuman classification
- Cave Host leader, flags, focus tree, starting ideas, unique divisions, and AI
- automatic resource-based Cave Host division capacity
- cave monster units with high armor, slow speed, and hard attack counterplay
- Cave Host wars against neighbouring countries
- world threat integration
- world-end trigger and super-event
- super-event image, quote, remark, audio, localisation, and documentation
- assets, manifests, and sprite handoffs
- achievements and icon directions
- meaningful validation and completion audit
- mandatory improvement loop pass and resolved addendum or closure handoff
- event catalog workbook update after implementation

## Known implementation risks

| Risk | Required handling |
| --- | --- |
| HOI4 resource fields may need static resource type effects | Use meta effects or scripted helper patterns after checking local docs. |
| Random state resource addition can become hard to reverse | Store event-added resource amounts per state where possible or use stage-specific cleanup helpers. |
| Multiple repeat fields can create cleanup complexity | Keep one primary deep site and ordinary field records. |
| Border state transfer can break maps | Use validated transfer logic and report any fallback if needed. |
| Cave Host capacity can be expensive if checked too often | Use event-driven refresh on state capture, loss, monthly pulse, or targeted on actions, not uncontrolled daily world loops. |
| Cave Host no-equipment divisions may need special templates | Use vanilla and repo precedent before implementing. |
| Nonhuman classification affects other events | Register in shared special chaos and actual nonhuman triggers. |
| Super-event audio licensing can block completion | Treat unclear audio as blocker, not placeholder. |
| Asset production can become large | Split icons, non-icon generated art, and audio into narrow subagent prompts. |
| Final text can accidentally spoil hidden branch | Run localisation audit before completion. |
