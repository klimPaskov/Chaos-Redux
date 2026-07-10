# Event 15 Utopia Manifesto, Part 8: Visual Direction, Text Direction, Documentation, and Acceptance

All names in this specification are working labels, not final localisation.

## Presentation principle

The event should look like a country trying to build an inhabitable future with 1930s and 1940s tools. Its visual identity should come from books, houses, stores, workshops, railways, gardens, civic assemblies, measured districts, islands, harbors, fortifications, and public labor.

The presentation should avoid turning the event into a map-and-arrow package. Territory matters, but the actor, institution, settlement, and social promise should remain the visual subject.

## Source-mode rule

Generated art is appropriate for:

- fictional report events
- route flags and emblems
- institutional council portraits
- focus icons
- idea icons
- decision icons
- achievement icons
- scripted GUI panels and animated seals
- final fictional super-event image

Sourced art is appropriate when implementation chooses to depict:

- Thomas More himself
- a real historical edition or page of *Utopia*
- a real historical leader
- a real historical flag or symbol
- a real archival planning or cooperative photograph

The opening report image can use a sourced historical edition or a generated period scene. If it uses a real edition or person, source documentation is required. If it uses a generated scene, it should depict a fictional recipient and avoid readable generated text.

## Event picture family

### Opening report image

Target:

- report event image, 210 by 176

Subject direction:

- an old volume or manuscript being examined in a modest public library, municipal room, school, monastery collection, or port archive
- several local readers or officials
- physical circulation and curiosity

Source mode:

- generated period-documentary scene by default
- sourced archival material only if a real edition is selected and documented

Avoid:

- glowing supernatural book
- readable generated text
- modern archive equipment
- a map as the main subject
- generic cabinet table composition without people or public stakes

### First common store report image

Target:

- report event image, 210 by 176

Subject direction:

- shelves, sacks, tools, ration counters, families, and civic workers
- practical provision rather than propaganda spectacle

Variants:

- orderly opening
- scarcity and crowd pressure
- council-managed store
- technical inventory
- guarded closed store

### Garden settlement report image

Target:

- report event image, 210 by 176

Subject direction:

- 1930s planned settlement under construction
- houses, gardens, rail or road, workshop, and civic hall
- route variant in architecture and crowd behavior

### Necessary Ground news image

Target:

- news event image, 397 by 153, black and white

Use only when:

- first major international case becomes public
- ultimatum or joint administration has regional significance

Subject direction:

- harbor, border settlement, local assembly, migration convoy, or treaty scene
- the people and institution behind the case

### Final proclamation super-event image

Target:

- 457 by 328

Source mode:

- generated alternate-history art

Variant family:

- voluntary commonwealth assembly
- council union and common stores
- planned city network
- fortified closed island
- practical plural commonwealth

## Scripted GUI visual family

### Commonwealth Ledger panel

The panel should resemble a civic ledger, planning board, or public account system without using readable decorative text inside the art.

Needed states:

- normal
- selected tab
- locked tab
- warning
- crisis
- formation-ready

The UI should keep values legible and avoid excessive parchment decoration.

### Value icons

#### Need

Motif direction:

- empty measure, broken supply line, unfilled bowl, or missing segment

#### Plenty

Motif direction:

- full store, grain and tools, stocked shelves, or connected houses

#### Concord

Motif direction:

- linked hands, meeting circle, charter seal, or assembled households

#### Choice versus Assignment

Motif direction:

- open path and measured grid
- two balanced tools
- hand choosing among callings and hand assigning a place

The icon must avoid presenting one side as a universal moral binary.

### Calling icons

- Provisioning and Agriculture
- Workshops and Arsenal
- Civic Works and Transport
- Learning and Care
- Maritime and Settlement
- Defense and Watches

Each icon should be designed for its actual GUI size and should not be a resized focus icon.

### Target and case cards

Needed states:

- no target selected
- target eligible
- target selected
- offer pending
- counteroffer
- refusal
- ultimatum available
- case expired
- stewardship active
- associate established

### District cards

Needed roles:

- market garden
- industrial housing
- rail junction
- port town
- research town
- refugee municipality
- Inland Island ring

Needed states:

- surveyed
- planned
- building
- blocked
- complete
- disputed

## Animation plan

The major mechanic receives an animation planning pass. Animation is used where it communicates state, not on every icon.

### Ledger seal animation

Use:

- category header or full-window emblem

Purpose:

- show that the national system is active
- subtle page, instrument, hand, or seal movement

Frame plan direction:

- 8 real source frames
- stable camera and central emblem
- rest, opening movement, active measure, closing movement, rest
- horizontal frame sheet
- static fallback
- restrained loop rate

Avoid:

- moving one still image by transform
- fake glow-only pulse
- readable text

### Need warning animation

Use:

- critical Need state

Purpose:

- draw attention to a material emergency

Frame plan direction:

- 6 to 8 separately created warning states
- changing emptiness, cracking measure, or tightening supply symbol
- static fallback
- state-driven visibility

### Choice versus Assignment balance animation

Use:

- only when the balance crosses a route-relevant threshold

Purpose:

- show a real institutional shift

Frame plan direction:

- separate frame sequence for movement toward Choice
- separate frame sequence for movement toward Assignment, or one reversible state set if the engine pattern supports it
- 8 real source frames per sequence or a verified lower count with a documented reason

### Formation-ready seal

Use:

- formation decision and final route state

Purpose:

- signal that all public proof conditions are met

Frame plan direction:

- 10 real source frames
- incomplete ring or island seal becomes whole
- route-specific center emblem
- static fallback
- play on show where supported

### Animation restraint

Do not animate:

- every focus icon
- ordinary decision icons
- every calling icon
- every advisor portrait

Animated leader portraits are not part of the baseline asset requirement. The institutional identity can be communicated through static portraits and animated mechanic seals. A later improvement pass can add a route-specific animated council portrait only if it has a clear state and does not create asset bloat.

## Focus icon families

Every focus or focus group needs a real icon assignment. The implementation can reuse icons within a coherent family when the visual meaning remains accurate.

### Opening family

Motifs:

- recovered volume
- public edition
- household census
- first store
- agricultural instruction
- congress
- interim charter

### Consent family

Motifs:

- household assembly
- open doors
- municipal charter
- cooperative land
- constitutional provision
- voluntary league

### Common Table family

Motifs:

- shared table
- calling councils
- worker workshop
- congress of communes
- pooled reserves
- international council

### Guardians family

Motifs:

- survey instruments
- measured housing
- tables and charts without readable text
- planned city
- technical board
- flexible versus exact measure

### Closed Island family

Motifs:

- sealed ring
- service register
- guarded store
- penal works
- auxiliary contract
- fortified channel
- assigned colony

### Hidden humanist family

Motifs:

- mirror and book
- open lamp
- sunset clause
- mixed institutions
- public criticism
- incomplete ring

### Shared support families

- callings and education
- common stores
- Garden City and public works
- island project
- defense and engineers
- foreign commonwealth
- Necessary Ground
- stewardship and integration
- final formation

## Idea icon families

Each idea should have its own 64 by 64 spirit design.

Required ideas:

- Found Manifesto
- Unmeasured Country
- Inherited Order
- Charter of Households stages
- Common Table stages
- Perfect Measure stages
- Closed Island stages
- Practical Commonwealth stages
- reserve institution
- district network
- auxiliary dependency or contract strain if represented as an idea
- stewardship burden if represented as an idea

Do not satisfy these by shrinking focus icons.

## Decision icon families

Each decision icon should be composed for 32 by 32 readability.

Priority icons:

- survey
- publish accounts
- build store
- fill reserve
- release stores
- open call
- guaranteed placement
- assignment quota
- learn second trade
- register land
- district survey
- district build roles
- select island
- build harbor or Inland Island terminal
- draft Need case
- purchase
- lease
- joint administration
- ultimatum
- renounce case
- emergency provision
- local charter
- status vote
- league invitation
- reserve compact
- citizen watch
- auxiliary contract
- formation decision

Decision category icons:

- Commonwealth Ledger
- Necessary Ground selected-target category if separate
- League and Associates if separate

## Portrait family

### Institutional portraits

Potential generated portraits:

- Household Assembly
- Council of Callings
- Board of Measure
- command or stewardship council

Each portrait should show a clear governing body rather than a cluttered crowd.

### Fictional personal leaders

Only required when implementation creates a personal route leader.

Rules:

- period-appropriate clothing
- regional visual identity
- apparent gender recorded
- matching name pool
- no generic office-title name for a one-person portrait

### Advisors

Advisor portraits can reuse existing country people when appropriate. Fictional new advisors need separate portrait direction and regional names.

## Flag family

Required final sizes:

- 82 by 52
- 41 by 26
- 10 by 7

Required route states:

- Consent cosmetic identity
- Common Table cosmetic identity
- Guardians cosmetic identity
- Closed Island cosmetic identity
- hidden humanist cosmetic identity

Additional ideology variants are required only when the route can retain more than one ideology after formation. They must use distinct designs.

The event should not overwrite the original base flag before route transformation.

## Faction and league emblems

Possible emblem families:

- Household Congress
- Congress of Common Tables
- Network Directorate
- Island Hierarchy
- Plural Compact

Use generated fictional emblems. Keep them readable at small scale and distinct from national flags.

## Achievement icon family

The achievement matrix defines the achievement set. Each achievement needs:

- completed 64 by 64 icon
- grey variant
- not-eligible variant using the repository overlay workflow
- exact achievement ID filename
- direct connection to route or conduct

The icon set should cover:

- peaceful formation
- genuine Need restraint
- high Choice and Plenty
- two-year reserve
- league building
- Inland Island
- coercive Perfect Island
- hidden humanist route
- consensual integration
- crisis recovery
- mercenary or penal-labor challenge where appropriate

## Localisation direction

The planning package does not provide final copy. Implementation writes final localisation after repository inspection and key registration.

### Event title direction

Identify a recovered utopian manifesto and a country deciding whether to make it public policy. Avoid generic titles such as The Perfect Society or A New Dawn.

### Opening description direction

Viewpoint:

- recipient government and public

Visible information:

- old text recovered or revived
- passages circulate quickly
- several groups see practical relevance
- the country is weak enough that the proposal cannot remain a drawing-room argument

Keep uncertain:

- final interpretation
- hidden route
- coercive consequences
- formation

### Accept option direction

Tone varies by ideology and leader. It should communicate commitment to a national experiment and show the tree-replacement warning through a clear tooltip.

### Reject option direction

Tone can be skeptical, cautious, amused, or hostile. It should not imply cowardice or impose a large penalty.

### Ledger text direction

Use concrete public language.

- Need describes what is missing and why.
- Plenty describes stores, homes, transport, tools, and capacity.
- Concord describes cooperation, trust, and local acceptance.
- Choice versus Assignment describes how work and service are allocated.

Avoid abstract philosophical exposition inside tooltips.

### Focus text direction

Each route should sound distinct.

- Consent uses civic, local, voluntary, and constitutional language.
- Common Table uses worker, council, common provision, and class language.
- Guardians uses survey, design, standards, capacity, and public engineering language.
- Closed Island uses service, unity, rationing, fortification, and necessity language.
- Hidden humanist uses criticism, limits, revision, and plural institutions.

Descriptions should explain the public action and visible direction. They should not list hidden thresholds or future surprises.

### Decision text direction

Each decision should name the action, target, cost, and public result. Nonstandard costs need icon-first requirement text and detailed tooltips.

### Occupation and integration text direction

The text must distinguish:

- emergency stewardship
- partnership
- municipality
- settlement
- assigned colony
- integration

Do not describe every form as liberation or every local population as passive.

### Super-event text direction

Research gate applies.

- final title requires research and writing
- main quote requires verified wording and attribution
- cultural remark requires source and copyright review
- audio requires source and license verification

The route variants should share a recognizable event identity while reflecting different institutions and moral outcomes.

## Event Details direction

The Event Details text should explain the premise and player experience without listing effects.

It should cover:

- a weak country revives an old utopian political program
- common stores, chosen work, planned settlements, and land justified by need become national questions
- the experiment can become voluntary, council-based, technocratic, coercive, or critically reformist

It should not expose:

- exact route names if hidden
- evolution thresholds
- final cosmetic identities
- achievement routes
- super-event conditions
- numeric values

## Evolution detail direction

- Glosses in the Margin describes rival interpretations becoming organized.
- Necessary Shores describes material pressure pushing the experiment beyond its existing borders.
- Cities of One Measure describes linked settlement models and associated municipalities.
- Nowhere Made Law describes the manifesto becoming a regional legal identity.
- The Perfect Island describes extreme separation and refuge under world collapse.

These summaries should remain situational rather than mechanical.

## Documentation requirements

The implementation should create or update one canonical event document under the Event 15 path.

Required content:

- event identity and classification
- recipient selection
- opening choice
- Ledger values and presentation
- focus route architecture
- decisions and missions
- idea lifecycle
- country identity
- league and associates
- Necessary Ground
- occupation and integration
- evolutions
- AI
- super-event
- assets
- catalog alignment
- known limitations

The documentation must distinguish accepted source specs from later working plans.

## Catalog replacement

The event catalog row should be replaced with:

- ID 15
- new event name from final localisation
- player-facing Details text matching Event Details
- five evolution entries matching final in-game evolution detail wording
- no world-end entry
- type Minor Fire-Once
- no cluster ID
- no member severity
- final implementation status after testing

The spreadsheet worker should update the actual workbook only after the in-game localisation exists. This package contains a CSV-oriented plan, not the workbook edit.

## Subagent and audit expectations

Before implementation completion, the parent agent should run:

- repo explorer for exact file and precedent map
- scripted-system architect for helper and tuning plan
- focus-tree auditor after the tree exists
- decision and mission auditor after the decision system exists
- country-package auditor after cosmetic identity and leadership exist
- localisation auditor after all visible text exists
- asset subagents for generated and sourced art
- super-event text and audio researchers
- documentation curator after long integration
- spreadsheet worker after final player-facing text
- improvement-loop planner for mandatory near-completion depth review
- event completion auditor before any completion claim

Ready-to-use prompts are provided in `prompts/subagents/`.

## Specification acceptance criteria

### Core event

- Event 15 is Minor Fire-Once.
- It has no cluster.
- The old World Tension Subsides content is fully replaced.
- AI accepts.
- Eligible human player can accept or reject.
- Reject leaves the tree unchanged and clears all temporary Event 15 state.

### Recipient safety

- Major and strong-industry countries are excluded.
- Protected unique trees are excluded.
- other event-created packages are excluded.
- focus replacement warning is visible to a selected player.
- manual and debug selection can explain unavailability.

### Focus tree

- comprehensive replacement tree exists.
- five interpretations exist, including hidden humanist route.
- economy, callings, defense, diplomacy, settlement, external policy, crisis, and late-game branches exist.
- support branches change with political route.
- final identity has post-formation play.
- AI route behavior exists.
- focus icons and localisation exist.

### Ledger

- four values are visible.
- causes and effects are readable.
- values alter gameplay.
- AI can operate the system.
- cleanup exists.

### Decisions and missions

- common stores, callings, districts, island project, Necessary Ground, stewardship, league, defense, and governance families exist.
- costs use varied resources.
- important missions have success, partial success, and failure.
- active mission clutter is controlled.
- target selection is safe.
- exploit loops are blocked.

### Territory and integration

- claims require a real case.
- peaceful steps exist.
- claims can expire.
- post-acquisition stewardship exists.
- local charters and status outcomes exist.
- Assigned Colony has strong costs.
- instant core spam is prevented.

### Country package

- original tag and base flag are preserved before transformation.
- route cosmetic identities exist.
- route party and institution directions are implemented.
- advisors and portraits are covered.
- military growth is institutional and paid.
- league rules and associate statuses exist.

### Evolutions

- five evolution stages exist.
- active-event and pre-fire paths are implemented where mapped.
- evolution disable rules are respected.
- evolution log actor and detail coverage exist.

### Super-event

- regional threshold justifies it.
- route variants are aligned.
- final image exists.
- final quote and cultural remark are sourced.
- unique final licensed audio exists.
- image, text, audio, slot, trigger, docs, and catalog agree.

### Assets

- event images, focus icons, idea icons, decision icons, flags, portraits, league emblems, achievement icons, GUI assets, and animation packages are complete or explicitly blocked.
- every animated asset has real source frames, sheet, static fallback, preview, manifest, and handoff.
- no placeholder art is called final.

### Text and documentation

- final localisation is written from the direction in this package.
- no prompt fragments remain in player-facing text.
- Event Details and catalog Details do not list effects.
- docs match implementation.
- plan dispositions are recorded.

### Completion proof

- focus route coverage audit passes.
- decision and mission audit passes.
- country package audit passes.
- localisation audit passes.
- mandatory improvement-loop pass is resolved.
- event completion audit finds no undisclosed simplifications, fallbacks, missing assets, missing AI, stale docs, or unresolved accepted plans.
