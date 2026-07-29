# Event 15 Utopia Manifesto, Part 8: Visual Direction, Text Direction, Documentation, and Acceptance

All names in this specification are working labels, not final localisation.

## Presentation principle

The event should look like a country trying to build an inhabitable future with 1930s and 1940s tools. Its visual identity should come from books, houses, stores, workshops, railways, gardens, civic assemblies, measured districts, islands, harbors, fortifications, and public labor.

The presentation should avoid turning the event into a map-and-arrow package. Territory matters, but the actor, institution, settlement, and social promise should remain the visual subject.

## Source-mode rule

Generated art is appropriate for:

- fictional report events
- route flags and emblems
- people-free institutional leader tableaux
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

District role cards and state overlays are presented together on the Ledger's Stores and Settlements page.

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

- 8 separately created warning states
- changing emptiness, cracking measure, or tightening supply symbol
- static fallback
- state-driven visibility

### Choice versus Assignment balance animation

Use:

- only when the balance crosses a route-relevant threshold

Purpose:

- show a real institutional shift

Frame plan direction:

- separate 8-frame source sequence for movement toward Choice
- separate 8-frame source sequence for movement toward Assignment

### Reserve-fill animation

The Stores-page reserve gauge has one additional 8-frame source sequence. It is runtime presentation beyond the five required animation families and does not replace any required sequence.

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

Animated leader portraits are not part of the asset requirement. Institutional identity is communicated through static people-free tableaux and animated mechanic seals. Do not create an animated council portrait containing people as a substitute.

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

### Institutional leader tableaux

Required generated institutions:

- Household Assembly
- Council of Callings
- Board of Measure
- command or stewardship council

Each leader image represents the governing body through an empty chamber, council table, ledger, standards apparatus, stores, seals, tools, empty seats, or route emblems. No people, faces, heads, bodies, hands, crowds, silhouettes, statues, busts, mannequins, framed portraits, photographs, or human shadows are allowed.

### Personal leaders

Event 15 does not create a generated personal route leader. Practical Commonwealth preserves the saved surviving constitutional leader and existing portrait. The other four route identities use the institutional tableaux above.

### Advisors

Each of the sixteen advisors requires its own fictional ImageGen portrait master and regional personal identity. A separate ImageGen dossier-frame overlay and separate ImageGen paper, paperclip, illegible-note, and wax-seal overlay provide the visible card artwork. The processing script may crop, grade, angle, derive alpha shadows, composite generated layers, resize, validate, and export. It must not programmatically draw the card, border, paper, seal, emblem, or visible overlay art. Advisor cards are `65x67`, are not square, and are not resized leader images.

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

Every active route flag must begin as a distinct built-in ImageGen heraldic design. Flags are flat identity designs and assets rather than narrative artwork, but they must not be replaced by simple programmatic shapes. Finishing may aspect-fit, resize, apply restrained colour and contrast adjustment, sharpen mildly, and validate preservation. It must not quantize, collapse to solid fills, trace, redraw, substitute motifs, impose a palette ceiling, or normalize away ImageGen-authored detail. Review source, normal, medium, and small versions together.

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

## Current final presentation record

This section is the current authority for the implemented Event 15 super-event, visual, localisation, and catalog presentation. It is not the final whole-event completion verdict. Earlier placeholder requests, two-image route proposals, and World Tension Subsides replacement language remain historical planning provenance only.

### Super-event package

The route presentation uses five display slots and five distinct 457x328 images:

| Slot | Route presentation | Sprite |
| ---: | --- | --- |
| 96 | Consent of Households | `GFX_super_event_015_consent_of_households` |
| 97 | Common Table | `GFX_super_event_015_common_table` |
| 98 | Guardians of Measure | `GFX_super_event_015_guardians_of_measure` |
| 99 | Closed Island | `GFX_super_event_015_closed_island` |
| 100 | The Joke Understood | `GFX_super_event_015_joke_understood` |

All five use the final title `UTOPIA HAS NEIGHBORS`, route-specific descriptions, Thomas More quotation text, and the response `Nowhere has a timetable.` The route effect selects the matching slot through Event 15 script constants.

Audio ID 57 uses `super_event_57_utopia_has_neighbors`. The source is the Musopen performance of Johannes Brahms, *Symphony No. 3 in F major, Op. 90*, third movement, published through Wikimedia Commons under CC0. The frozen source, license evidence, hashes, edit record, music file, sound file, registries, and uniqueness proof are documented in `docs/super_events/015_utopia_manifesto/audio_research.md` and `docs/super_events/super_event_audio_packages.md`.

### Current visual inventory

- 14 report-event images and 3 news-event images are registered.
- Five route super-event images are registered in `interface/015_utopia_manifesto_super_event.gfx`.
- 124 focus usages resolve to 74 unique focus sprites.
- The decision map contains 174 rows, covering 9 categories, 121 decisions, and 44 missions.
- There are 165 gameplay decision and mission icon assignments.
- Fifty ideas resolve to 12 unique idea sprites.
- Fourteen achievements have 42 active, complete, and failed variants.
- Forty-six unique scripted-GUI sprite references resolve.
- The static Ledger family contains 4 value icons, 6 Calling icons, 10 case cards, 7 district-role cards, and 6 district-state overlays. District role and state art is paired on Stores and Settlements.
- The five required animation families contain 8 Ledger-seal frames, 8 Need frames, 8 Choice frames, 8 Assignment frames, and 10 formation frames. The reserve-fill presentation contributes one additional 8-frame runtime family outside the required-family count.
- The base Event 15 registry contains 459 sprite definitions and the route-super-event registry contains 5, for 464 total registrations with no duplicate names.

The July 16 requirement-first asset report passes all `24/24` accepted rows. Its SHA-256 is `a05d4c53f2ff775754ecdc00f9ee26789da16a13a05c0146044b095ff6891f33`, and the requirement crosswalk SHA-256 is `8cf869a2f6f53ee9119a2bf2148c6eff4efae8c70ceae6c6d0e052f7dcae19bd`. Current final asset authority is `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/advisor_asset_final_audit_2026_07_18.md`, SHA-256 `d2f659ac4e968a9d48ae3f346c1a7d9d5e1cb6b09b67f3be16a789662b583693`. It independently passes the advisor dossiers, active flag and institutional portrait packages, and the Choice and Assignment frame-by-frame packages. The current mapping CSV records 174 rows and 165 gameplay assignments. The older decision-mapping subsection of `final_icon_frame_audit.json` is superseded for those counts only.

### Flags and portraits

Every active route flag has a genuine built-in ImageGen source and a flat heraldic flag design in the runtime package. Twenty-one independent designs plus four intentional engine-lookup aliases produce 75 runtime TGAs. These are ImageGen-authored designs, not simple-shape substitutes. The finishing pipeline preserves generated geometry and tonal detail without quantization, tracing, primitive redraw, motif substitution, or a palette ceiling.

Four people-free built-in ImageGen, vanilla-HOI4-style institutional tableaux are 156x210. Eight founder and successor institutional entries share those four images by durable institution. Sixteen advisors use distinct 65x67 dossier cards built from independent fictional ImageGen portrait masters plus separate generated frame and paper/seal overlays. Processor v5.0 only crops, grades, angles, derives alpha shadows, composites the generated layers, validates, and exports. It does not draw the advisor card. Advisor cards are not square portraits or resized institutional leaders.

### Localisation and audit state

The final English-localisation gate passes at the static-source level. Its nine Event 15-owned files contain 2,480 quoted definitions, 2,480 exact unique keys, and 2,480 case-folded unique keys. No duplicate, missing, or unaccounted orphan key remains across the audited event, focus, decision, mission, category, idea, character, achievement, identity, Ledger, scripted-localisation, super-event, and formation-name surfaces. The audit renamed two founding idea IDs to explicit `_idea` suffixes to remove case-only collisions with stable cosmetic identity keys. It also normalized six player-facing definitions without changing their requirements, costs, or outcomes. The report is `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/localisation_final_audit_2026_07_18.md`, SHA-256 `8d6e12652670782aef40259c263e18d306989d9134e7059b4e732dc4bc4a0e17`.

The live Ledger vocabulary is Need, Plenty, Concord, and Choice versus Assignment. `Surplus` remains only in historical working labels or stable engine-facing identifiers. Player-visible implementation-language families are absent from the final scan. The current workbook SHA-256 is `ed52b1f3ee3f0e602b3cc6a4b5fd7bc0d340445a3c085c6c8531fbcd2c0430f4`. Fresh read-only proof in `spreadsheet_current_hash_followup_2026_07_18.md`, SHA-256 `e0ba36c5805e0aca01b6bf74fec4f6dc29a24aecf4a3ec36382c334e5c741bd1`, confirms 13/13 parity for `Events!A16:M16` and normalized row SHA-256 `e330489603bd739e64fc356b8bb79498c4a34d54433f28cda4c2ba459dadab1e`. The older spreadsheet and localisation audit workbook snapshot `729e48a3135094d210b70e74ce3694ff0b66dbd5d2bc448051db931a41f4bd80` is pre-drift but Event 15-row-equivalent. Localisation `\\n` is decoded to workbook LF characters for the details comparison. The current focus, country, decision, localisation, asset, catalog, improvement-loop, and independent documentation evidence passes. The fresh whole-event completion audit also passes in `docs/plans/015_utopia_manifesto_plans/completion_audit.md`, SHA-256 `5a90b637478872d6f960c7e67630e0efd0fda3e17869bad2c094473596a12183`, with 53-file runtime-text manifest SHA-256 `395873f4821fdf159cfb2f6edb9eecc0790a724f151cb0df62f89b969649d4b2`. It closes the final acceptance gate with no open P0 through P3 finding, fallback, simplification, omission, blocker, or queued accepted plan.
