# Fallout Living World Event Asset Prompt

Create the visual asset packages for the Fallout living-world event library after the implementation batches define final event ids, country selections, route identities, and sprite names.

Use the accepted successor asset matrix together with the living-world event matrices. This prompt expands event and society coverage. It does not replace the existing flag, focus, idea, decision, portrait, GUI, or country-package obligations.

## Ownership

Use dedicated Fallout folders and manifests.

Required roots include:

- `docs/assets/fallout_world_end/`
- `gfx/event_pictures/fallout/`
- `gfx/interface/fallout_world_end/`
- `gfx/interface/goals/fallout_world_end/`
- `gfx/interface/ideas/fallout_world_end/`
- `gfx/interface/decisions/fallout_world_end/`
- `gfx/leaders/fallout_world_end/`

Flags remain in the engine-required flag roots with Fallout successor or cosmetic-tag filenames.

Do not reuse zombie event images, zombie portraits, zombie flags, zombie icons, zombie GUI textures, zombie sounds, zombie music, zombie sprite names, or zombie asset paths.

Fallout is not a normal super-event. Do not create or wire a Fallout super-event image.

## Asset strategy

The event library is large. It needs a deep image library, not one image for every event.

A report image can support a tightly related event family when:

- the physical subject is the same
- the region and institution fit
- the image does not depict a specific unique result
- repeated use will be uncommon in one campaign

A unique image is required when:

- a recurring character is introduced or transformed
- a successor identity is revealed
- a major city, institution, altered society, or regional compact is established
- a major war, peace, famine, thaw, migration, constitutional settlement, or Year 10 order changes the campaign
- the event's central subject cannot be represented by an existing family image

Do not use one generic ruins image across unrelated regions and systems.

## Report and news image families

Plan a release library of roughly 90 to 140 report images and 20 to 35 news or broadcast images.

Priority report families:

- shelter entry, filter room, sealed ward, ventilation failure, late arrivals
- ration hall, seed vault, ash field, greenhouse, fungal food, livestock slaughter, fishing fleet
- water court, pump repair, contaminated reservoir, ice well, desalination plant
- field hospital, decontamination line, maternity ward, medicine exchange, epidemic checkpoint
- rail repair, convoy, port clearance, frozen road, bridge failure, tunnel refuge
- power station, generator hall, hydro facility, mine, salvage yard, radio relay
- refugee column, reception camp, family reunification, citizenship hearing, resettlement
- market, ration fraud, smuggling, labor dispute, local court, election, council, mutiny
- school, archive, funeral, festival, marriage, new settlement, first harvest
- first contact, technical exchange, trade convoy, compact meeting, border post, armistice
- raider siege, corridor war, water war, salvage conflict, city reclamation
- altered ecology and fictional mutant society scenes
- thaw flood, ice breakup, ultraviolet warning, recovered vegetation, second-generation politics

Regional versions must reflect architecture, clothing, terrain, transport, food systems, and institutions. Do not create a modern post-apocalypse costume style that erases 1930s and 1940s material culture.

News or broadcast images should cover only events that deserve wide recognition, such as:

- public confirmation of the world rewrite
- first interregional contact
- creation of a major compact
- a severe famine or migration crisis
- a major successor war
- a recognized altered polity
- first reliable interregional transport
- climate thaw milestone
- Year 10 world-order settlement

News images must follow the established black-and-white format.

## Recurring character portraits

The recurring character matrix requires portraits or institutional images for roles that become visible gameplay actors.

Priority roles include:

- quartermaster
- shelter engineer
- physician
- radio operator
- seed keeper
- railway dispatcher
- water judge
- militia commander
- refugee organizer
- archivist
- teacher
- market inspector
- salvage captain
- reactor or power engineer
- religious relief leader
- altered-community representative
- first post-collapse generation leader

Real historical people require sourced portraits. Fictional people use generated portraits. Record apparent gender presentation and require matching name pools and metadata. Councils, committees, and offices use institutional names and collective portraits.

Produce route variants only when the character's role, allegiance, injury, altered condition, or leadership status changes visibly.

## Successor identity assets

Every selected playable successor needs:

- normal, medium, and small flag
- ideology or route variants where required
- leader or council portrait
- country-selection or detail portrait where used
- founding event image
- at least one domestic-memory event image
- one external or regional image family
- late identity or route-capstone image
- focus, idea, and decision icon coverage from the existing matrices

All 99 candidates need an asset disposition before the candidate pool is called complete:

- complete
- selected for current implementation batch
- historically sourced work pending
- generated work pending
- blocked with reason
- not selected for the current build

Do not silently omit assets for candidates that remain eligible to spawn.

## Icons

Create separate source art for each icon type.

Needed families include:

- survival resources
- shelter conditions
- winter and climate phases
- state reclamation
- government archetypes
- citizenship and legitimacy
- trade and corridor types
- character loyalty and institution status
- war causes and settlement paths
- generation change
- altered society and ecology
- Year 10 world-order goals

Do not resize a focus icon to satisfy an idea or decision icon. Use coordinated icon families with separate art designed for each target size.

## GUI and event presentation

The existing blackout GUI package remains separate from normal event art.

Living-world UI may require:

- event-family status markers
- active major-arc indicator
- recurring character portrait frame
- contact and recognition status
- compact or treaty seal
- regional hazard markers
- Year 10 world-order status
- static fallbacks for any animation

Animation should be limited to meaningful state changes, such as an urgent arc warning, contact established, compact crisis, severe winter, or late thaw. Follow the frame-animation skill.

## Source mode

Use sourced material for:

- real leaders
- historical flags
- attested symbols
- real archival photographs
- identifiable historical buildings, documents, or institutions when the event requires them

Use generated material for:

- fictional successors
- fictional councils
- alternate-history scenes
- altered societies
- fictional flags and emblems
- symbolic event art
- unique period-documentary scenes that have no real archival equivalent
- interface and icon art

Generated World War II-era scenes must use period clothing, vehicles, tools, architecture, photographic technology, and composition. Avoid modern tactical equipment, modern survival clothing, modern roads, modern vehicles, readable generated text, film stills, and cinematic color grading.

## Required processing

Report images use the established report-card treatment and final 210 by 176 format.

News images use the established 397 by 153 black-and-white format.

Leader portraits normally use 156 by 210.

Use exact established sizes for icons and flags from the asset skill.

For every asset, preserve:

- source
- processed PNG
- final DDS or TGA
- source URL and license where sourced
- prompt and source-mode rationale where generated
- target event family, country, route, idea, focus, decision, or character
- sprite name
- final path
- status
- uncertainty

## Contact sheets

Create contact sheets by:

- event family
- region
- government archetype
- successor batch
- recurring character role
- climate and recovery phase
- icon type

Contact sheets must show final crop, dimensions, transparency, naming, and intended use.

## Review failures

The asset pass fails when:

- one generic ruins image represents most events
- regions look interchangeable
- fictional societies lack ordinary civilian life
- every image is bleak and no competence, affection, ritual, recovery, or celebration appears
- a real person or flag was generated
- a fictional altered society is presented as a scientific prediction
- icon types are satisfied by resizing one master image
- a candidate successor remains spawnable with missing visible identity assets
- an asset points into another feature folder
- a Fallout super-event image is created
