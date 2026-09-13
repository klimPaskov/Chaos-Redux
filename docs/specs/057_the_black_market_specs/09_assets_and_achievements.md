# Assets and Achievements

## Visual direction

Event 57 should look like a period clandestine logistics system.

The visual identity should use:

- railway sidings
- guarded warehouses
- merchant holds
- false crate markings
- fuel drums
- mixed military equipment
- shipping papers without readable generated text
- customs lamps and inspections
- neutral ports
- folded route notes
- anonymous brokers shown from a distance or without identifiable portrait framing

The palette can use aged paper, dark wood, steel, canvas, oil, muted military paint, and low industrial light.

Avoid modern containers, computers, neon crime imagery, online-market symbolism, skull emblems, gangster caricatures, national stereotypes, readable generated labels, and generic money piles as the main subject.

## Asset source mode

The event is fictional and international. Its report art and category pictures should use generated period-authentic documentary scenes.

Gameplay icons and achievement icons should use generated transparent icon art through the correct icon workflow.

The asset package does not need a grounded person or institutional portrait.

## Reference inspection

Before production, asset workers must inspect the exact matching reference families under:

`C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\.agents\skills\chaos-redux-event-assets\assets\vanilla_reference`

Required families:

- `event_art/report/`
- `icons/decision_categories/`
- `icons/decision_categories/pictures/`
- `icons/decisions/`
- `icons/achievements/`

The decision-category-picture folder must contain its own labeled `contact_sheet.png`. When missing, the asset worker must create it and update the reference README and catalog before generating Event 57 pictures.

## Report event pictures

### First Contact

| Field | Requirement |
| --- | --- |
| Working basename | `black_market_first_contact` |
| Type | report event picture |
| Size | `210x176` |
| Source mode | generated period documentary scene |
| Runtime folder | `gfx/event_pictures/057_the_black_market/` |
| Proposed sprite | `GFX_report_event_057_black_market_first_contact` |

Composition direction:

- a dim wartime depot or railway warehouse
- several crates from different military origins
- one guarded exchange between officials and anonymous intermediaries
- no clear national insignia that identifies founders
- documentary framing from outside the conversation
- 1936 to 1945 clothing, transport, lighting, and materials
- no readable generated text

### Seized Shipment

| Field | Requirement |
| --- | --- |
| Working basename | `black_market_seized_shipment` |
| Type | report event picture |
| Size | `210x176` |
| Source mode | generated period documentary scene |
| Runtime folder | `gfx/event_pictures/057_the_black_market/` |
| Proposed sprite | `GFX_report_event_057_black_market_seized_shipment` |

Composition direction:

- customs or military personnel opening a concealed cargo compartment
- mismatched weapons, fuel drums, or technical cases
- route evidence visible through objects, not readable documents
- tense but non-cinematic lighting
- no gore
- no modern equipment

### Grand Auction

| Field | Requirement |
| --- | --- |
| Working basename | `black_market_grand_auction` |
| Type | report event picture |
| Size | `210x176` |
| Source mode | generated period documentary scene |
| Runtime folder | `gfx/event_pictures/057_the_black_market/` |
| Proposed sprite | `GFX_report_event_057_black_market_grand_auction` |

Composition direction:

- a large hidden depot with one exceptional military or technical lot
- masked national identity through plain coats, crates, shadows, and intermediaries
- period telephones, paper ledgers, and transport equipment
- no modern auction room
- no readable generated bids or signs

## Decision category icon

| Field | Requirement |
| --- | --- |
| Basename | `black_market_category` |
| Type | decision category icon |
| Target | inspect active consumer, expected compact category icon |
| Source mode | generated transparent icon |
| Proposed sprite | `GFX_decision_category_057_black_market` |

Icon direction:

- one sealed crate crossed by a folded route line or key
- clear silhouette
- transparent unused canvas
- dark outline and subtle shadow
- readable at the final size
- no text, coins, skull, or modern padlock

## Evolution category pictures

The same category changes its static picture after each evolution. Each picture is separate source art designed for the category-picture consumer.

The current reference family uses `114x101`, but final size must be confirmed from the active sprite and GUI consumer.

### Baseline picture

Working basename: `black_market_category_local_circuit`

Direction:

- one compact rail or warehouse exchange
- small mixed cargo
- local shadows and limited scale
- one clear visual route

### Evolution I picture

Working basename: `black_market_category_international_network`

Direction:

- linked rail, port, and distant freight cues in one coherent period scene
- larger cargo and wider origin variety
- no painted world map as the main subject

### Evolution II picture

Working basename: `black_market_category_underground_economy`

Direction:

- embargoed cargo moving through layered neutral paperwork and hidden depots
- technical cases and industrial material
- state officials present indirectly

### Evolution III picture

Working basename: `black_market_category_anything_has_a_price`

Direction:

- exceptional guarded stock, technical dossiers, unusual equipment cases, and large clearing activity
- broad scale without fantasy spectacle
- the market feels powerful but remains period-authentic

Proposed sprites:

- `GFX_057_black_market_category_local_circuit`
- `GFX_057_black_market_category_international_network`
- `GFX_057_black_market_category_underground_economy`
- `GFX_057_black_market_category_anything_has_a_price`

## Decision icon family

All decision icons are independent `32x32` assets. They can share motifs and palette, but none should be a resized copy of another asset type.

| Basename | Use | Visual direction |
| --- | --- | --- |
| `black_market_buy_lot` | purchase current offer | open crate with one clear military silhouette |
| `black_market_sell_surplus` | list member surplus | outbound crate and inventory tag without text |
| `black_market_commission` | request offer class | sealed request case and broker key |
| `black_market_open_route` | create or repair route | rail, road, or port route symbol |
| `black_market_safer_route` | reroute delivery | split route with guarded branch |
| `black_market_intelligence` | buy or sell intelligence | closed dossier and lens motif |
| `black_market_compartmentalize` | reduce Exposure | separated ledger pages or locked compartments |
| `black_market_burn_route` | destroy compromised route | broken rail or burned manifest motif without flames dominating |
| `black_market_penetration` | counterintelligence posture | marked cargo and surveillance symbol |
| `black_market_suppression` | close local cell | customs seal over route symbol |
| `black_market_grand_auction` | exceptional auction | large sealed case with bid marker, no text |
| `black_market_underwrite` | convert industrial burden into credit | factory silhouette and sealed account book |

Every icon should have native transparency, stable centering, readable silhouette, and no opaque square background.

## Texticons

Market Credit requires a dedicated texticon with a stable token before any decision uses it as a visible cost.

Working asset:

- basename: `black_market_credit_texticon`
- motif: small stamped account chit, ledger mark, or trade token
- transparent unused canvas
- no readable generated text

The exact dimensions and sprite registration must follow an inspected existing custom texticon precedent.

## Achievement set

The seven achievements below use working titles. Final player-facing wording should be written during implementation and localisation audit.

Each achievement needs:

- exact achievement ID
- tracking flags or variables
- current-player eligibility
- disqualifiers
- completed icon
- grey icon
- not-eligible icon
- documentation
- catalog or achievement list alignment when the project exposes one

### 1. No Questions Asked

- Proposed ID: `57_the_black_market_no_questions_asked`
- Visibility: visible
- Eligible country: any ordinary player country that becomes a member
- Goal: complete purchases from every baseline cargo family during one campaign while Exposure never reaches `50`
- Baseline families: small arms, support or artillery, transport, fuel or convoys, and intelligence
- Disqualifiers: Force Trigger debug state, full network dismantling before completion, any player Exposure record of `50+`
- Why it is difficult: the player must use several offer classes without relying on high-risk bulk trade
- Tracking: one receipt flag per cargo family plus highest Exposure reached
- Icon direction: several different sealed crates arranged behind one intact customs seal

### 2. Enemy of My Enemy's Quartermaster

- Proposed ID: `57_the_black_market_enemy_quartermaster`
- Visibility: visible
- Eligible country: active member
- Goal: receive a settled equipment delivery whose proven source country is currently at war with the buyer at both dispatch and settlement
- Additional requirement: source identity never becomes public through that transaction
- Disqualifiers: self-created civil-war copy, source and buyer become allies before settlement, duplicated provider receipt
- Why it is difficult: the route must survive active hostility and the source must be real
- Tracking: buyer, source, hostility proof at dispatch and settlement, secrecy outcome
- Icon direction: two opposing helmets divided by one anonymous supply crate

### 3. The Embargo Has Holes

- Proposed ID: `57_the_black_market_embargo_has_holes`
- Visibility: visible
- Eligible country: current target of Event 50 or a shared major strategic embargo
- Goal: while the embargo remains active, complete one fuel delivery, one military-equipment delivery, and one industrial-procurement delivery
- Disqualifiers: embargo removed before any required delivery settles, packages with no route proof
- Why it is difficult: three cargo classes need surviving routes under active restriction
- Tracking: active embargo proof and three settled package receipts
- Icon direction: blocked trade gate with three concealed cargo paths passing beneath it

### 4. Liquid Assets

- Proposed ID: `57_the_black_market_liquid_assets`
- Visibility: visible
- Eligible country: active member that never adopts State Patronage
- Goal: win and receive a Grand Auction lot after earning at least the winning bid's Market Credit value through verified sales
- Disqualifiers: State Patronage, debug credit, duplicated sale receipts, winning cargo not delivered
- Why it is difficult: the player must build a real seller economy and preserve enough route capacity for the auction
- Tracking: sale-earned credit total, non-sale credit sources, posture history, bid, auction settlement
- Icon direction: stacked sealed crates transforming into one large locked case, without literal liquid imagery

### 5. Invisible Empire

- Proposed ID: `57_the_black_market_invisible_empire`
- Visibility: hidden until Event 57 fires
- Eligible country: founding member
- Goal: remain a member until Evolution III activates while the country's Exposure stays below `25`, with no route ever reaching Compromised
- Disqualifiers: withdrawal, expulsion, Exposure `25+`, compromised route, player joining after founding
- Why it is difficult: growth must come through careful small trade, brokerage, and route management
- Tracking: founder receipt, maximum Exposure, route-compromise history, Evolution III activation
- Icon direction: broad network of crates and routes hidden behind one plain closed warehouse door

### 6. Customs Seizure

- Proposed ID: `57_the_black_market_customs_seizure`
- Visibility: visible
- Eligible country: a player country that has never been a member
- Goal: dismantle every active Black Market route that passes through owned or controlled territory and cause the connected regional cell to become dormant
- Disqualifiers: any membership acceptance, route created by player infiltration without eventual dismantling, incomplete cell dormancy proof
- Why it is difficult: the player needs evidence, local control, several successful actions, and a live target cell
- Tracking: never-member flag, route IDs touching player territory, dismantled receipts, cell dormancy receipt
- Icon direction: customs officer seal over an opened false cargo compartment, without a character portrait

### 7. Prototype Without a Project

- Proposed ID: `57_the_black_market_prototype_without_a_project`
- Visibility: hidden until Evolution II or the first approved experimental offer
- Eligible country: active member
- Goal: receive and field or validly use one owner-approved experimental package while the owning source project remains incomplete
- Disqualifiers: generic unapproved token, source project completed before delivery, package not fielded or used, debug grant
- Why it is difficult: it depends on a rare owner package, route handling, and project-state isolation
- Tracking: provider ID, package ID, source project state at dispatch and settlement, recipient use proof
- Icon direction: unusual covered machine or weapon crate with an unfinished technical drawing motif, no readable text

## Achievement asset paths

Achievement files follow the root-only achievement convention in `gfx/achievements/`.

For each exact ID, create:

- `<achievement_id>.dds`
- `<achievement_id>_grey.dds`
- `<achievement_id>_not_eligible.dds`

Completed source art is generated first. Grey and not-eligible variants follow the established achievement workflow and overlay reference.

## Asset manifest

The temporary event workspace should contain:

- source art
- processed PNGs
- final review contact sheets
- prompt records
- source-mode records
- DDS outputs before runtime placement
- dimensions
- alpha validation
- sprite handoff
- achievement triplet coverage

Recommended temporary path:

`docs/assets/057_the_black_market/`

Before full event completion, durable provenance, prompt, review, and runtime crosswalk facts must move into permanent event or plan documentation. Final assets move to runtime folders. No runtime path may reference `docs/assets/`. The completed temporary event workspace should then be deleted according to the asset workflow.

## Asset acceptance

The asset package is not complete until:

- every required source exists
- all event pictures are `210x176`
- category pictures match the inspected consumer
- all decision icons are independent `32x32` designs
- the Market Credit texticon is wired and readable
- every achievement has three final states
- transparent assets retain real alpha
- no white matte, checkerboard, halo, or opaque square remains
- all sprites and runtime paths are registered
- category pictures switch with evolution state
- the first-contact, seizure, and auction events use the correct art
- contact sheets show final assets at native size
- manifests and permanent evidence are aligned
