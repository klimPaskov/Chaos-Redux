# Murder Mystery Specification Part 14: Visual Asset and Presentation Package

## Asset strategy

Event 39 is dynamic, fictional, and high-chaos. Most finished art should use native ImageGen through the correct project worker after period-source research. Dynamic host identity makes a photograph of one real assassination unsuitable as the universal opening image. Historical material should be used as reference evidence for clothing, offices, transport, intelligence work, military kit, and period visual language, not as a claim that the fictional movement is a real organization.

Every final asset needs source evidence, processed PNG preview, final DDS where the consumer uses DDS, stable final path, sprite handoff, manifest row, and acceptance review. No runtime file may remain under temporary `docs/assets/039_murder_mystery/` after full completion.

## Source-mode rules

- fictional event, news, report, country, faction, and super-event art uses `chaosx_generated_event_art`
- every fictional character portrait uses `chaosx_portrait_creator` and native ImageGen
- focus, idea, decision, achievement, technology, agency, operation, unit, equipment, trait, faction, and other icons use `chaosx_icon_artist`
- period reference research and any real archival non-portrait source use `chaosx_asset_source_researcher`
- animated assets follow `chaos-redux-frame-animation` through the owning asset worker
- 3D source art, model jobs, animation, audio, and counters follow the Event 39 3D prompt and `chaosx_3d_model_pipeline`

No generated text, fake newspaper headline, copied insignia, borrowed real extremist symbol, religious stereotype, or generic ninja costume is allowed.

## Visual identity

The core symbol family should communicate removed authority and hidden coordination. Accepted motifs include:

- an empty chair or empty dais
- a cut command knot
- a broken seal with one intact hidden thread
- a masked hand holding a severed ceremonial cord
- a closed eye formed from map routes
- a keyhole with no visible key holder
- a grid of cells whose center is absent

The visual system should avoid literal gore. Threat can be communicated through absence, interrupted ceremony, abandoned offices, files, broken communications, shadows, and controlled military preparation.

Suggested palette direction:

- charcoal, aged paper, muted black, dull silver, dark burgundy, and cold institutional green
- host-country color may appear as a secondary accent in dynamic or route-aware presentation
- terminal art can broaden toward drained grey and pale institutional light

Color cannot be the only state cue. Icons and meters need shape, frame, label, texture, or silhouette differences.

## Event and report picture family

All target dimensions and crop behavior must follow the exact installed Chaos Redux and vanilla reference surface. The following is the minimum narrative picture set.

| Working asset | Consumer | Source mode | Visual direction |
| --- | --- | --- | --- |
| Opening assassination | original-host event and international news | generated | disrupted state office, empty leader position, security and evidence, no identifiable real person |
| Emergency succession | host report | generated | acting government taking control amid secured doors and files |
| First failed attempt | local report | generated | protected convoy, ceremony, or office after an intercepted attack |
| Evidence preserved | investigation report | generated | period evidence room, sealed files, map routes, controlled documentary tone |
| Witness lost | investigation report | generated | abandoned safe transfer point, no body close-up |
| Cell exposed | investigation report | generated | raided safe house with communications, equipment, and records |
| Final capture success | national and international report | generated | restrained arrest aftermath, uncertain face, evidence and escort |
| Final capture failure | host report | generated | empty room, open route, burned or removed records without fantasy effects |
| Murder Cult revealed | Evolution I event | generated | followers around copied symbols and files, no real religious imagery |
| Foreign cell discovered | secondary-country event | generated | local intelligence office connects foreign route evidence |
| Major foreign assassination | international news | generated | state ceremony or command office disrupted, dynamic-country neutral |
| Assassin State split | Evolution III event | generated | barricaded administrative district, organized cadres, new flag, visible territorial control |
| Foreign revolt | Evolution IV event | generated | local cell movement seizing rail, radio, or government district |
| Movement inheritance | report | generated | surviving regional command receives sealed network records |
| Assassin State defeat | defeat report | generated | captured capital, abandoned symbol, surviving files under guard |
| Remnant cleanup | aftermath report | generated | investigators dismantling hidden compartments and archives |

Do not reuse one image for several materially different events. Coordinated art direction is allowed. Source artwork must match the actual moment.

## Decision category pictures

### Murder Mystery Investigation

Use a generated category picture with a period case room, protected-office map, photographs or files without readable generated text, and a central missing identity. It must leave enough visual space for the native category layout.

Required public progression variants:

- baseline investigation
- Murder Cult
- international network
- counterinsurgency after the Assassin State appears
- resolved or aftermath state when the category briefly closes

Variants should show different operational scale and institutional condition. They must not be simple recolors.

### Foreign Cell Investigation

Use a related but distinct country-facing picture that emphasizes imported evidence, local target protection, and an external route. Do not resize the original-host picture.

### Brotherhood Operations

Use a command room assembled from clandestine communications, territorial maps, unit dispatches, and foreign cell links. The central seat can remain visually empty or obscured to reinforce the contradiction.

Progression variants:

- territorial survival
- foreign network support
- Veiled Compact and subjects
- Evolution V terminal preparation

### World Without Leaders

Use a terminal category picture that shows campaign sectors, dismantled state symbols, and the movement's hidden command structure. It should remain readable and avoid a world map covered in fake text.

## Animated category warning

One animated asset family is authorized because it clarifies immediate risk.

Working asset: `murder_mystery_imminent_incident_warning`.

Consumer: an animated warning strip or icon in the decision category when a murder, escape, or revolt preparation enters its final public warning state.

Brief direction:

- native transparent source frames
- real per-frame source artwork
- a sealed dossier or command cord shifting from secure to visibly breached
- eight to twelve frames at a restrained rate
- one horizontal frame sheet DDS
- static fallback DDS
- GIF preview for review only
- no text, primitive geometry, glow-only frames, transform-only motion, or GIF runtime path

The exact consumer and frame size must be verified against a local category or GUI precedent. If the ordinary decision category cannot consume the animation safely, use state-specific static variants and record the consumer blocker. Do not add a custom window merely to display it.

## Focus icon families

Every final focus needs an icon designed for its own role at the established focus canvas, normally 94 by 86 when the current reference confirms it. Icons should be organized into coordinated families without resizing other asset types.

Required families:

- founding and capital survival
- captured archives and inventory
- state contradiction and command settlement
- Hidden Hand route
- Cells Without Masters route
- Necessary Mask route
- clandestine workshops
- seized industry and rail control
- pragmatic contracts and trade
- Assassin doctrine
- Shadow Companies
- Silent Guard
- conventional adaptation
- Master Assassins
- Mechanized Assassins
- foreign cells and secure communications
- route interdiction and intelligence theft
- revolt preparation
- Veiled Compact and subjects
- original host conquest and administration
- Evolution V terminal preparation
- World of Anarchy activation
- nonterminal late-game settlement

The icon artist should create one distinct icon per final focus. This family list sets the visual language and required reference shelves.

## Idea and national-spirit icons

At minimum, create distinct 64 by 64 spirit art for:

- Underground Becomes Government
- Cells Under Arms
- Leadership Is a Crime
- every route-specific mature replacement of those three starting spirits
- succession crisis
- institutional memory after capture
- compromised ministry
- protected leadership system
- mature international network
- foreign derivative administration
- terminal campaign command
- terminal defeat or postwar protection compact

A staged spirit can reuse one coordinated subject only when each stage receives asset-type-specific art that visibly changes its state. Do not make a focus icon and crop it into an idea icon.

## Decision and mission icons

Create distinct 32 by 32 decision art or exact current reference size for the actions that remain visible in the final design.

Families include:

- succession security
- evidence preservation
- witness protection
- office-group protection
- agency or case-team commitment
- communications audit
- route tracing
- safe-house raid
- final capture plans
- evidence sharing
- border, port, rail, and convoy interdiction
- cell support
- foreign revolt preparation
- subject reinforcement
- Cohesion settlement
- terminal sector selection
- government administration outcome

Mission icons should distinguish protection, route control, evidence transport, cell raid, revolt prevention, capital survival, and terminal sector mandate.

## Intelligence assets

When La Résistance consumers exist, create or adapt event-owned art for:

- Event 39 investigation operation
- foreign cell infiltration operation
- coordinated arrest operation
- protected-person protocol
- movement route operation
- government command disruption operation

Each intelligence-operation icon follows its own canonical reference. It cannot be a generic decision icon resized into the agency UI.

## Unit and technology art

Required asset families are defined in Part 9:

- Assassin Cadre sub-unit and division art
- Shadow Company
- Silent Guard
- Master Assassin
- Mechanized Assassin
- Saboteur Cell support company
- operations-kit equipment
- compact Event 39 technology line
- bespoke large counters, map counters, and template emblems
- 3D model materials and source art

Every unit surface uses its exact reference family and current consumer dimensions.

## Country flags and faction emblem

### Central Assassin State

Produce normal, medium, and small flags for the reserved carrier and any actual ideology or route variants that the implementation wires. Flag work begins after tag and cosmetic identities are stable.

Design direction:

- flat invented emblem
- strong readability at small size
- no text
- no historical religious, national, or extremist symbol
- no direct copy of anarchist black flag conventions as the only identity
- base form should support route variants through changed emblem structure, not simple recolor

### Foreign derivatives

Use a bounded flag system that combines the central movement symbol with local geometric or color identity. Every live carrier and cosmetic variant needs all three flag sizes. Do not create one identical flag for every derivative.

### Veiled Compact

Create a distinct faction emblem for the Compact. It should show coordinated cells around an absent center or a divided seal. It should not be identical to the central state flag.

## Portrait package

All Event 39 named people are fictional high-chaos identities and may use native ImageGen through the portrait creator.

Minimum authorized portraits:

- the revealed First Knife or final selected leader identity
- one centralized successor or directorate leader when the route needs it
- one decentralized council or symbolic collective presentation when supported
- one pragmatic administrator or institutional leader when the route needs it
- one or two army commanders
- one intelligence or foreign-cell organizer

The final roster should remain compact. Do not create portraits for every advisor direction unless the final focus tree explicitly adds the character.

Portrait direction:

- 1930s to 1940s clothing and photographic language
- distinct individual identity
- no real-person resemblance as a design goal
- no generic ninja mask
- no fantasy glow or modern tactical gear
- route and country role visible through clothing, posture, setting, and insignia

The portrait worker owns processing, DDS, portrait-specific GFX, and existing character portrait references.

## Achievement art

Every achievement in Part 16 needs three root-level DDS variants whose filenames match the final achievement ID:

- eligible or normal
- grey
- not eligible

Achievement icons need distinct small compositions that communicate the challenge. Use the standard project overlay workflow for the not-eligible state. Do not create grey or not-eligible variants by guessing the engine treatment.

## Super-event images

The three authorized super-event roles are:

- Assassin State public reveal
- World of Anarchy activation
- Brotherhood defeat aftermath when its gate passes

Each needs a distinct full scene, not a flat symbol or title card. Source and role direction are in Part 15 and the super-event prompt.

## News and report hierarchy

Use:

- report events for evidence, witnesses, local cells, minor casualties, route discoveries, and normal investigations
- normal country events for major phase decisions and host outcomes
- news events for opening leader murder, major foreign assassination, public Assassin State revolt, major foreign derivative creation, and complete capture
- super-events only for the Assassin State reveal, World of Anarchy, and a sufficiently large defeat aftermath

This hierarchy prevents presentation inflation.

## Reference inspection

Before every asset family, inspect:

- exact matching `assets/vanilla_reference/` shelf and contact sheet
- source path and owning vanilla or Chaos Redux definition
- native size, frame count, alpha, crop, and consumer
- at least one installed vanilla or Chaos Redux runtime precedent

Missing exact references block the asset. They do not authorize a close visual substitute.

## File placement direction

Final event-owned assets should use event-scoped folders under the correct category, for example:

- `gfx/event_pictures/039_murder_mystery/`
- `gfx/report_event_pictures/039_murder_mystery/` when that surface uses a distinct root
- `gfx/super_events/039_murder_mystery/`
- `gfx/interface/ideas/039_murder_mystery/`
- `gfx/interface/goals/039_murder_mystery/`
- `gfx/interface/decisions/039_murder_mystery/`
- `gfx/interface/technologies/039_murder_mystery/` or exact live tech root
- `gfx/leaders/<reserved_tag>/`

Flags and achievements stay in engine-required root structures. Exact paths must be confirmed from the live repo and references.

## Asset manifest

The permanent manifest should record:

- asset ID and event owner
- asset type and runtime consumer
- source mode
- source path, prompt, or provenance
- target dimensions and background mode
- processed PNG and final DDS path
- sprite name and target GFX file
- route, evolution, country, or state consumer
- reference folder and local precedent
- frame plan and fallback for animation
- portrait classification where relevant
- status and blocker

## Acceptance standard

The asset package is accepted only when every authorized consumer has a correct final asset, every source mode is valid, every generated asset has source evidence, every alpha-backed asset passes transparency review, icons remain readable at native size, flags and achievements have all required variants, animation has real source frames and a static fallback, portraits are correctly classified, model and counter assets are complete, and no placeholder or unrelated reused art remains.
