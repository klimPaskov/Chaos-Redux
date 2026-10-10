# 16. Visual Presentation and Assets

## A world that changes from plague to plague

The visuals begin with an unsettling environmental change and end with recognizable mass civilian loss.
Each plague needs its own scene and silhouette; ten interchangeable disaster photos or one red tint over everything would lose the sequence.

Scenes are original generated period images of the interwar and wartime world, never presented as archival evidence.
Egypt gets an additional Nile scene; the rest is global: cities and farms, different climates, small countries and industrial powers, occupied areas and reception points.
Suffering is shown through damaged services, interrupted work, shelters, empty places and mourning.
No invented photograph shows a real person dying, and tenth-plague imagery never implies that all victims were children.

## Inventory

| Consumer | Count | Final size |
| --- | ---: | --- |
| Country report pictures | 16 | 210 × 176, report-card processing |
| News pictures | 6 | 397 × 153, black and white |
| Super-event pictures | 4 | 457 × 328 |
| Category pictures | 12 | Verify the actual category consumer; 114 × 101 is the planning reference |
| National spirit icons | 3 | 64 × 64 |
| Decision icons | 14 | 32 × 32 |
| Achievement states | 36 | Twelve subjects × colored, grey, not eligible, 64 × 64 |

The static inventory is 91 outputs.
The global Darkness presentation (Part 7) is separate and may add runtime assets once its consumer is chosen.
Production follows the `chaos-redux-event-assets` skill: full-quality sources first, report-card processing for reports, the black-and-white news treatment, genuine alpha for icons, the skill's DDS converter, and the achievement processor for triplets.
Every output gets a manifest row linking source, processing, size, destination, sprite and consumer.

## Report pictures

The suffixes are local identifiers under the Event 085 prefix.

| Suffix | Scene | Consumer |
| --- | --- | --- |
| `report_blood_world` | A municipal water point suddenly unusable, red water beside ordinary period equipment | Blood outside Egypt |
| `report_blood_nile` | A recognizable Nile bank with period river life disrupted by the red river | Blood for Egyptian territory |
| `report_frogs` | Frogs blocking a tram, workshop or civic doorway as cleanup begins | Frogs |
| `report_lice_gnats` | Crowded relief work and interrupted rest, insects shown without microscopic imagery | Lice and Gnats |
| `report_flies` | Food protection and sanitation work under dense flies | Flies |
| `report_livestock` | An emptied livestock enclosure and anxious farm workers | Livestock |
| `report_boils` | Period care, covered patients and strained staff, without graphic detail | Boils |
| `report_hail_fire` | Shelter activity beside hail-damaged buildings and a fire in the same landscape | Hail and Fire |
| `report_locusts` | A swarm edge approaching the last intact crop beside damaged land | Locusts |
| `report_darkness` | A midday civic space lit only by lamps under unnatural darkness | Darkness |
| `report_passover` | Neighbors organizing a protected doorway and practical supplies | Passover |
| `report_firstborn` | Empty adult and child places in a household or workplace, mourning rather than spectacle | Tenth plague |
| `report_exodus` | Civilians with belongings approaching a reception or transit point | Exodus |
| `report_mourning` | A community memorial with ongoing relief in a damaged town | Mourning |
| `report_blood_returns` | A repaired water point turning red again, newly composed | First renewed cycle |
| `report_cycle_broken` | Ordinary daylight and repair work returning to a battered town | Escape |

Each is its own composition, not a crop of a master picture.

## News, super-events and category pictures

The six news subjects are global Blood, public recognition of the pattern, storm destruction, global Darkness, the firstborn night and the Exodus; each is composed for the news frame.
News is sent once per episode milestone, never per country or state.
The four super-event pictures are described in [Part 17](085_ten_plagues_of_egypt_spec_part_17_super_event_directions.md) and composed at 457 × 328.

The twelve category pictures cover the ten phases, mourning and reconstruction, with mutually exclusive conditions so exactly one shows.
An intermission before a restart uses the mourning picture with the return date in text.

No focus inlay, formable puzzle, country selection window or 3D plague unit is part of this event.

## Icons

Spirit icons: the crisis, the Harden Our Hearts policy and mourning or reconstruction, each with a distinct silhouette.
The crisis spirit's tooltip changes with the active consequences; there are no per-plague spirit icons.

Decision icons follow the fourteen actions in [Part 14](085_ten_plagues_of_egypt_spec_part_14_decisions_and_missions.md): hardened heart, safe water, frog clearance, infestation control, military stand-down, food and sanitation, rural continuity, civilian care, storm shelter, harvest preservation, essential service, Passover, foreign relief and reconstruction.
Use clear objects and actions, no tiny text or miniature scenes.
Shared Famine, Migration and Natural Disasters actions keep their owners' icons.

## Achievement art

The twelve subjects are in [Part 18](085_ten_plagues_of_egypt_spec_part_18_achievements.md).
Each gets one original transparent subject; the grey and not-eligible states are deterministic derivatives with the unchanged overlay.
Names and meaning stay in localisation, not inside the picture.

## Animation

No 3D animals, skeletal animation or animated portraits are needed.
If motion is later chosen for a 2D consumer, it follows the frame-animation skill with real authored frames and a static accessibility state.
