# Black Plague Asset Production Prompt

Create the complete visual asset package for Chaos Redux Event 20 Black Plague. Read the accepted Event 20 spec pack, `AGENTS.md`, `chaos-redux-event-assets`, and `chaos-redux-frame-animation` before production. Inspect the matching Chaos Redux reference folders before creating any asset.

## Event identity

- Event ID: `020`
- Slug: `black_plague`
- Source mode: generated for all fictional plague, rat, Rat King, UI, flag, portrait, report, news, and super-event art unless a later accepted handoff identifies a real historical source requirement
- Final working package: `docs/assets/020_black_plague/`
- Final gameplay assets must live in event-scoped folders under their normal asset categories
- No placeholder, primitive-shape, recolor-only, resized-cross-type, or transform-only animation output is acceptable

## Required reference inspection

Inspect these folders before work:

- idea and national spirit icons: `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/ideas`
- focus icons: `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/national_focus`
- decision and decision category icons: `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/decisions`
- report event images: `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/event_art/report`
- news event images: `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/event_art/news`
- super-event images: `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/event_art/super_event`
- achievements: `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/achievements`
- flags: `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/flags/normal`

## Disease and crisis-board package

Create separate source art for:

- one 64 by 64 Black Plague disease or idea icon
- one Black Plague disease selector icon using the exact live disease-selector size, with no dedicated Black Plague category icon
- state-status UI icons for Threatened, known Incubating, Infected, Severe Crisis, Collapsed, Contained, Recovery, Cured, known Weaponized, and Rat-Controlled
- value icons for Disease Load, Mortality Pressure, Spread Pressure, Containment, Treatment Coverage, and Relapse Risk
- six countermeasure milestone states designed for the live progress surface
- one shared crisis-board background or decorative panel only when the live UI needs new art

Use one clear central subject, high contrast, no text, and exact final-size readability. Status icons must remain distinguishable without relying only on color. The existing mapmode uses a black base fill for established Black Plague states, so outlines and status icons must stay readable over black.

## Animated crisis seal

Create an animated Black Plague crisis seal for the shared disease board.

- target size: determine from the live GUI before production
- frame count: 8 real source frames
- loop: slow, continuous, settings-aware
- motion: subtle black vapor, small pulse in the plague mark, controlled intensity
- states: normal active, Severe Crisis, and Collapsed can use separate source-frame families when the live UI supports state switching
- static fallback required
- horizontal sheet PNG and DDS required
- preview GIF for review only
- no animation made by opacity, scale, rotation, blur, recolor, or offset of one still

## Black fog feasibility prototype

Prototype a state-attached animated black fog only after the implementation owner identifies a verified map or GUI surface that can anchor it dynamically.

Desired art:

- 8 to 12 real source frames
- low dark particulate fog
- transparent background
- slow drift with no flashing
- distinct density families for Infected, Severe Crisis, Collapsed, and Rat-Controlled when technically practical
- no obstruction of borders, units, labels, or state selection

Required outcome:

- complete final asset and wiring handoff when the engine surface works
- or a reproducible `blocked by engine surface` report naming the tested file, sprite pattern, and limitation

Do not substitute a generic screen tint and call it black fog. The disease mapmode remains a separate implementation surface.

## Human decision icons

Create separate 32 by 32 decision icon art for the decision families listed in `matrices/asset_inventory.md`. At minimum cover:

- surveillance
- medical reserve
- transport inspection
- border closure
- port inspection
- troop route restriction
- field hospitals
- civilian travel restriction
- quarantine
- army cordon
- emergency hospitals
- relief corridor
- burial and sanitation crews
- vector control
- city rat clearing
- sealed granaries, markets, and warehouses
- sewer and burrow-shaft clearance
- flea, shelter, and bedding treatment
- rail-yard and dock vermin purge
- demolition of infested blocks
- treatment distribution
- sealed transport
- evacuation
- controlled reopening
- residual tracing
- recovery support
- foreign medical mission
- cure research and knowledge sharing
- intelligence theft
- weapon project safety and acceleration
- stockpile destruction
- anti-rat fortification
- purge warrens and burrow clearance
- armored clearance
- air reconnaissance
- royal node strike

Each icon needs its own decision-sized composition. Do not resize focus or idea icons.

The triggerable scenario reuses the disease, Rat Nation, Rat King, report, and coronation assets from this package. Do not create a separate scenario icon or custom scenario window art unless the live scenario UI has a verified technical requirement.

## Report, news, and super-event images

### Report images, 210 by 176

Generate period-authentic documentary source scenes, then use `tools/process_report_event_image.py` for the final report-card treatment.

1. origin outbreak in a neglected crowded mainland district
2. Severe Crisis with overwhelmed care and blocked streets
3. first Rat Nation emergence with organized rat movement in ruins or a sewer opening

Requirements:

- 1936 to 1945 photographic technology and composition
- period clothing, vehicles, streets, and architecture
- no generated text
- no modern props
- black-and-white with sepia through the project processor
- transparent report-card corners and soft shadow

### News images, 397 by 153 black and white

1. first confirmed overseas port outbreak
2. first recognized Rat Nation military front

Use fictional period-news source art, high contrast, no text, and no modern imagery.

### Super-event images, 457 by 328

1. Rat King coronation
   - sentient one-person rat sovereign
   - organized brood court
   - ruined civic interior or captured hall
   - regalia made from period materials
   - no comedy crown, map table, or readable text

2. Rat King world end
   - sovereign above or within a conquered human capital
   - organized global rat dominion
   - emptied streets and human remnants
   - strong central composition and finality
   - no abstract diagram or title card

3. Rat King defeat aftermath, only if the implementation retains the eligibility-gated super-event
   - broken throne or abandoned royal nest
   - relief and reconstruction at great cost
   - reflective rather than triumphal

## Base Rat Nation portraits

Create four institutional collective leader portraits at 156 by 210.

- Urban Warren
- Field Brood
- Dock Brood
- War Brood

These are collective or brood identities, not single humanlike characters. Record them as institutional leaders. Make each portrait distinct in subject, framing, lighting, and setting. Do not create one portrait and recolor it.

Optional proto-sentience variants may be created only when the final focus-tree implementation uses visible portrait changes.

## Rat King portrait package

Create one sentient individual Rat King portrait and animation package.

### Static portrait

- 156 by 210
- upper-torso HOI4 framing
- sentient rat sovereign
- subdued painterly treatment
- captured period regalia
- no text, cartoon styling, or modern props

### Animation

- 10 to 12 separately generated or edited source frames
- same identity, camera, framing, and palette
- subtle breathing, whisker motion, eye focus, cloak movement, and background fog
- static fallback
- processed frames at 156 by 210
- horizontal sheet at 1560 to 1872 by 210
- final sheet DDS
- preview GIF and contact sheet
- animation brief and frame plan

Record the portrait's apparent presentation and require a matching nonhuman name pool and leader metadata. Do not permit opposite-presentation name assignment.

Create route portrait variants only when the government route changes the public leader identity enough to justify them.

## Flags

### Reusable RTA carrier flag family

Create one complete RTA base flag family for the reusable carrier. Internal brood markers are represented through state markers, basin variables, and UI accents rather than additional country flags or tags.

Each design needs:

- normal 82 by 52 TGA
- medium 41 by 26 TGA
- small 10 by 7 TGA
- correct vanilla TGA origin
- contact-sheet orientation validation

Design the RTA family with a distinct motif such as tails, teeth, burrow spirals, grain, harbor hooks, broken rails, trenches, or plague marks. Do not create palette swaps, flipped copies, or copied emblems for unregistered brood tags.

### Rat King

Create:

- base Rat King flag set
- Absolute Crown route flag set when the live cosmetic identity uses it
- Council of Burrows route flag set when used
- Black Breath Hierophancy route flag set when used
- world-end cosmetic flag set

## Focus icon families

Create focus-specific 94 by 86 assets for every implemented focus. Use the route-family inventory as a prompt map.

Base Rat Nation families:

- awakening and survival
- four origin archetypes
- hierarchy
- mutation
- territorial plague economy
- military method
- rival absorption
- proto-sentience

Rat King families:

- coronation
- three government routes
- administration and supply
- military castes
- plague mastery
- captured knowledge
- population policy
- continental campaign
- world-end path

Related icons can share motifs and palette. Separate branches must not be recolored copies of one composition. Every final focus needs a deliberate assigned icon.

## Idea and spirit icons

Create separate 64 by 64 art for:

- Uncounted Brood
- Born of Pestilence
- Fractured Instinct
- Crowned Brood
- Plague Dominion
- Stolen Mind
- route or failure forms only when their meaning changes materially

Do not derive them from focus icons.

## Rat and Rat King decision icons

Create separate 32 by 32 art for:

- Brood Mass
- Hunger
- Coherence
- burrow node
- pulse timer
- concentrate and scatter
- rival challenge and resistance
- absorption
- Dominion
- Sentience
- Brood Cohesion
- royal pulse doctrines
- population policies
- intelligence operations
- continent target
- capital objective
- Crown the Continent
- world-end readiness

## Animated Rat King seal

Create a settings-aware animated scripted-GUI seal for world-end readiness.

- target size from live GUI
- 8 real source frames
- static fallback
- slow crown and entwined-tail motion with controlled fog
- available, critical, and complete states can use separate sheets if the interface supports them
- no transform-only motion

## Achievement icons

Create the 14 completed 64 by 64 icons described in `matrices/achievement_matrix.md`, then produce:

- grey variant through black-and-white conversion
- not-eligible variant by compositing the approved achievement overlay

Final achievement DDS files stay directly under `gfx/achievements/` and use exact registered achievement IDs.

## Required package outputs

For every asset:

- source PNG
- processed PNG at exact target size
- final DDS or TGA
- manifest entry
- proposed or preserved sprite name
- final path
- target GFX file
- related event, focus, idea, decision, leader, flag, achievement, or UI key
- status and uncertainty

For animation:

- brief
- frame plan
- source frames
- processed frames
- static fallback PNG and DDS
- horizontal sheet PNG and DDS
- preview GIF
- contact sheet
- frame count, FPS, loop, anchor, play-on-show expectation
- verified local wiring precedent

Create `docs/assets/020_black_plague/gfx_handoff.md` with ready-to-review sprite snippets. Do not edit GFX or gameplay files unless the parent explicitly expands scope.
