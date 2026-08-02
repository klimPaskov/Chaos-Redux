# Independence Wave, Part 7: AI, balance, assets, achievements, and acceptance

All names in this file are working labels, not final localisation.

## Accepted implementation scope (2026-08-02)

AI, balance, asset, achievement, and acceptance checks apply to the single shared `independence_wave_focus_tree` generic framework used by every admitted Event 006 release. Package and regional variation is gated shared content and scripted adapters inside that tree. A reviewed additive carrier may preserve a meaningful existing tree, currently IW-012 ICE. Bespoke country focus-tree definitions and live/in-game testing are outside the current implementation scope. This scope decision does not waive package, formable, asset, AI, balance, rights, or runtime gates.

## AI design promise

Every Event 6 country must behave like a new state trying to survive. AI behavior changes with package type, government route, former-host threat, patron access, league state, geography, force strength, and chaos.

A single generic AI weight table is not enough.

## AI actor groups

### Fragile released state

Priorities:

- secure capital
- reduce instability
- gain nearby recognition
- avoid immediate war
- accept limited aid without surrendering all autonomy
- build basic forces

Avoids:

- distant formables
- aggressive border demands
- expensive patron balancing before a second patron exists
- league leadership bids

### Viable released state

Priorities:

- complete government settlement
- professionalize army
- seek host treaty or guarantee
- join network and league
- pursue compact regional claims

### Armed released state

Priorities:

- secure depots and borders
- convert defecting units
- evaluate host weakness
- seek military allies
- choose civilian control or military route

Risks:

- premature war
- coup
- equipment collapse
- radical league politics

### Highly legitimate but weak state

Priorities:

- recognition
- guarantees
- volunteer and equipment support
- defensive league
- careful military growth

### Strong but unrecognized state

Priorities:

- practical trade and de facto recognition
- demonstrate territorial control
- pressure host
- avoid diplomatic isolation

### Patron-dependent state

Priorities:

- satisfy patron demands if client route is chosen
- balance or buy out influence if autonomy route remains open
- avoid joining hostile league charters

### League-oriented state

Priorities:

- recognize other members
- contribute to shared goals
- answer rescue calls when affordable
- support compatible charter
- avoid member wars

### Radical high-chaos state

Priorities:

- expansion
- breakaway sponsorship
- armed league
- hidden formables
- coordinated host pressure

Limits:

- still checks supply, strength, allies, and route validity
- can take dangerous risks, but should not declare impossible wars at random

### Former host

The host chooses among acceptance, negotiation, client settlement, containment, and reconquest.

Factors:

- share of territory lost
- military strength
- stability
- current wars
- ideology
- claims
- great-power support
- league intervention risk
- recognition of the new state
- previous failed reconquests

A democratic or exhausted host may negotiate. A revanchist, authoritarian, strong, or humiliated host may prepare reconquest. A near-remnant host prioritizes its own survival.

### Neighbor and regional power

Factors:

- border
- claims
- ideology
- trade route
- threat from host
- fear of precedent
- patron rivalry
- league growth

Actions:

- recognize
- guarantee
- mediate
- arm
- invest
- infiltrate
- contain
- support host
- sponsor a rival claimant

### Great-power patron

Factors:

- strategic access
- ideology
- resources
- naval and land reach
- rivalry with the host
- existing commitments
- league charter
- expected influence return

Actions use separate channels rather than one generic aid button.

## AI route validity

AI route selection must verify:

- required states exist and are reachable
- former host exists when a host route needs it
- sponsor exists and can reach the country
- league has viable members
- formable requirements can still be met
- required ideology or leader is active
- evolution is enabled
- country has Event 6 origin
- route is not already invalidated by reunion, annexation, or another formable
- target country exists
- border or access conditions are real

Invalid routes are hidden, bypassed, or weighted to zero.

### IW-012 two-stage route evaluation

The registered ICE adapter uses two separate AI layers. Its six paid projects establish a founding posture from the five Iceland ledgers, war state, severe former-host threat, host survival, Compact readiness, Network Standing, and League membership. The four mutually exclusive government focuses then perform the formal route evaluation; no project may silently lock a government route.

The intended all-routes-valid checks are:

| Situation | Constitutional | Traditional | Emergency | Patron | Preferred route |
| --- | ---: | ---: | ---: | ---: | --- |
| Stable civic peace and settled charter | 80 | 10 | 1 | 10 | Constitutional Republic |
| Stable port and shipping administration with settled charter | 10 | 80 | 1 | 10 | Traditional Authority |
| War, severe host threat, and mature Coastwatch | 0.625 | 2.5 | 320 | 2.5 | Emergency Military |
| Treaty-backed Compact and peaceful severe host pressure | 2.5 | 2.5 | 40 | 80 | Patron-Client |
| No distinguishing route signal | 10 | 10 | 10 | 10 | Controlled replayable tie |

These are source-level design weights before engine normalization, not runtime completion evidence. Invalid routes must receive zero selectable probability through their existing availability gates. Armed Neutrality has zero AI willingness in stable peace without war or severe host threat, while the formal Emergency Military focus remains available when its Coastwatch or commitment gate is satisfied. Costs, durations, project caps, focus costs, route rewards, and the harbour survival deadline remain unchanged.

## AI resource safety

AI should not spend the last usable equipment, trains, convoys, fuel, manpower, or civilian capacity on a prestige decision while the capital is threatened.

Decision willingness considers:

- stockpile reserve
- front need
- supply
- production recovery
- mission urgency
- host threat
- league obligations
- expected recognition or legitimacy gain
- patron dependency

## AI league behavior

AI evaluates each charter pillar separately.

### Joining

Positive factors:

- host threat
- low recognition
- high network standing
- compatible government
- nearby members
- need for aid
- anti-patron strategy

Negative factors:

- strong independent security
- patron opposition
- border conflict with member
- incompatible radical charter
- fear of automatic wars
- low cohesion

### Contributions

AI contributes when it has reserve resources and when the shared goal protects a real interest.

It should not donate equipment while losing its capital or starving its own divisions.

### Rescue calls

AI response tiers:

- diplomatic protest
- equipment aid
- volunteers
- guarantee
- expeditionary force
- war entry

The response depends on charter, confidence, capacity, and threat.

### Leadership

AI challenges leadership when it has strong standing, contributions, recognition, and a different charter agenda. It avoids futile challenges that would collapse the league during an emergency.

## Balance model

Balance comes from pressure, costs, tradeoffs, and counterplay. It does not come from making every effect too small to matter.

## Opening balance goals

### Fragile opening

The country should be able to survive with careful play, outside aid, or favorable geography. It should not be guaranteed to survive an immediate major-host attack without preparation.

### Viable opening

The country can hold its capital and border against limited pressure. It still needs recognition, government capacity, and army reform.

### Armed opening

The country can threaten the host locally. It starts with higher instability and military political danger.

### High-chaos opening

The country can become a regional problem quickly. Its power carries severe diplomatic, internal, or supply risks.

## Host balance goals

- the host always remains playable
- losing several regions creates a real crisis
- the host can negotiate rather than being forced into endless reconquest
- reconquest is possible but not free
- a capital remnant receives survival tools
- repeated waves cannot strip the same remnant below one valid state
- the host cannot farm annexation rewards by repeatedly killing and re-releasing the same tag

## Mechanic balance

### Legitimacy

Should move meaningfully through government and public actions. It should not be solved by one focus.

### Recognition

Should require several diplomatic relationships or a major treaty. One patron can accelerate it, but dependency grows.

### Government Capacity

Should be slower for large, dispersed, and underdeveloped packages. Strong local institutions can offset size.

### Security

Can grow quickly through mobilization and aid. Overmobilization raises instability and costs equipment.

### Instability

Should create early pressure and later route identity. It should not become an unavoidable death spiral. Successful actions must produce visible recovery.

### Patron Influence

Aid must feel powerful. Dependency must also matter. The player should face real choices between speed and sovereignty.

## Formable balance

- negotiated formations are slower but more stable
- military formations are faster but receive claims, resistance, and integration costs
- large unions require sustained administration
- hidden high-chaos formables can be powerful, but they need rare conditions and severe consequences
- no formable can be repeated for free rewards
- AI does not pursue impossible or suicidal formations

## League balance

- the league cannot form from one country
- mutual defense obligations reflect the charter
- strong members cannot drain weaker members without confidence loss
- shared reserves require real contributions
- patron capture is a strategic danger
- cohesion rises from successes and falls from broken promises
- aggressive charters create containment and war risks

## Replayability plan

Variation comes from:

- different candidate packages
- different hosts
- different territorial levels
- different government archetypes
- different opening forces
- regional overlays
- country ambition modules
- patron availability
- host reactions
- league charter
- formable discovery
- evolution state
- chaos
- prior wave survival

The system should not force the same constitutional, military, or league outcome in every campaign.

## Achievement set

The event needs a difficult achievement set covering survival, diplomacy, league leadership, formables, anti-patron play, host settlement, rare countries, and the triggerable scenario.

The authoritative achievement matrix is `matrices/006_achievement_matrix.csv`.

Priority achievement themes:

- survive from an anchor-state opening to entrenched recognition
- remain free of dominant patron influence
- secure peaceful host recognition
- defeat a reconquest without becoming a client
- form and lead the league
- keep a cross-regional league together
- rescue another member
- form a region-specific larger country
- complete a signature country ambition
- turn a one-state country into a major power
- complete a radical high-chaos bloc
- survive the all-countries scenario

Achievements must not unlock merely because Event 6 fired.

## Visual identity plan

Every visible surface needs an asset family or explicit reuse plan.

### Event images

- wave summary report image
- concentrated regional wave report variants
- host crisis report image
- first recognition report image
- first league congress news image
- major formable news images for selected signature routes

### Super-event images

- league formation image
- dangerous coordinated revisionism image

Both are alternate-history moments and should normally use generated period-authentic scenes. Historical people or specific real events cannot be fabricated.

### Core mechanic UI

- category icon
- panel background
- five value icons
- former-host status frame
- patron card family
- league card and charter seal
- formable seal
- warning frames
- progress bars and state variants

### Animated assets

Recommended state-driven animation:

- recognition seal progression
- dependency warning pulse
- league charter activation
- formable eligibility seal

Each animation requires:

- real source frames
- static fallback
- horizontal frame sheet
- preview GIF for review only
- manifest
- sprite handoff

Animation is not needed for every country flag, focus icon, or leader.

### Focus icons

The framework needs coordinated icon families for:

- founding and administration
- constitutional government
- popular councils
- traditional restoration
- military government
- patron client route
- recognition and diplomacy
- army and security
- economy and infrastructure
- former host and border settlement
- league and congress
- formables
- high-chaos sovereignty

Country ambition modules receive unique icons.

### Idea icons

Distinct 64x64 icon art for:

- Improvised Government stages
- Unrecognized State stages
- Fragmented Command stages
- Unsettled Borders stages
- Patron Pressure stages
- league membership and leadership spirits
- route-specific institutions

Idea icons cannot be resized focus icons.

### Decision icons

Distinct 32x32 icons for major action families:

- recognition
- government construction
- army integration
- depot security
- host settlement
- patron aid
- patron balancing
- network aid
- league vote
- border arbitration
- formable proclamation
- integration mission

### Flags

Every country needs normal, medium, and small flags.

Source rules:

- historically attested flags and symbols are sourced and documented
- real community and traditional symbols require source review
- fictional or alternate route flags use generated art
- ideology and route variants are distinct designs, not recolors
- base flags of existing countries are preserved unless a deliberate transformation is part of the route
- formable and cosmetic flags follow the `X` tag and identity plan

### Portraits

- every country leader, route leader, commander, and named officeholder for a
  real, historical, restored, regional, indigenous, dynastic, separatist, or
  otherwise plausibly historical country uses a sourced real portrait
- a historical collective authority uses sourced archival material for its
  real institution or a sourced real period representative
- fictional one-person leaders use generated portraits only when the country
  is truly fictional and high-chaos
- a country that existed in whole or in part, claims continuity from a real
  polity or institution, represents a real community, or remains plausibly
  historical is grounded and cannot receive a generated person
- generated high-chaos leaders use distinctive invented ceremonial dress,
  regalia, body adornment, ritual objects, altered uniforms, or other coherent
  fictional cultural motifs instead of generic portrait design
- generated high-chaos leaders must look intentionally extraordinary; reject
  ordinary, conventionally dressed, or interchangeable fictional officeholders
- strange details must belong to the fictional polity's designed culture and
  must not borrow or exaggerate sacred objects or traits of a real people
- generated portraits do not use modern props, meme treatment, gore, or
  stereotypes or caricatures of real cultures
- signature country routes receive priority portrait depth
- ordinary framework countries can begin with a sourced historical council or
  sourced period representative and later select a sourced leader

Accepted user direction dated 2026-07-16 narrows the Event 6 portrait roster:

- every Event 6 personal, command, and collective portrait depicts men only;
- no Event 6 character carries female gender metadata;
- every fictional portrait master is generated against the canonical vanilla
  leader or commander references and finished in the recognisable HOI4
  painterly-realistic style;
- sourced real portraits are cropped to head and shoulders and receive an
  identity-preserving HOI4 treatment;
- a newly defined Event 6 character may not duplicate a person already defined
  and recruited, or otherwise owned by a live vanilla or Chaos Redux character
  roster. Reuse of an existing registered character requires an explicit guarded
  transfer/availability contract that prevents simultaneous ownership; creating a
  second token with the same person and a new portrait is not reuse;
- incidental text such as a ship, production line, street, or equipment name is
  not character ownership by itself; ownership requires an actual character,
  portrait, leader, commander, operative, or named officeholder consumer;
- a historical or plausibly historical package with no defensible sourced
  candidate and usable portrait remains blocked instead of receiving a
  generated officeholder;
- `portrait_BAY_rupprecht_of_bavaria.dds` and
  `portrait_RHI_josef_friedrich_matthes.dds` are approved and remain untouched;
  every other current Event 6 leader or commander portrait must be replaced
  through its compliant source mode; grounded packages use sourced real people
  or real archival institutional material, never generated substitutes;
- Event 6 gameplay advisor offices use no custom advisor portrait icons or
  `GFX_portrait_advisor_*` registrations.

The absence of custom advisor icons is a selected presentation rule, not
permission to omit advisor mechanics, traits, costs, availability, or AI.

## IW-043/IW-058 reviewed asset tranche

The bounded package asset authorities are:

- `docs/assets/006_independence_wave/iw043_iw058_generated_visuals_2026_07_18/manifest.md`
  for eight all-male institutional portraits, ten flat flags, and two report
  images;
- `docs/assets/006_independence_wave/iw043_iw058_static_icons_2026_07_18/manifest.md`
  for two decision categories, sixteen decisions, six idea families, and the
  three-state Assyria survival achievement triplet.

The final files are reviewed and runtime-installed for the bounded base package.
The later sourced-leader rule supersedes the source-mode acceptance of the eight
generated IW-043/IW-058 institutional portraits. Those portraits cannot satisfy
package visual readiness and require sourced real replacements before the
packages can retain final portrait attestation.
The Assyria triplet's provenance record explicitly excludes the post-1968/1973
modern Assyrian flag from the 1936 baseline. The exact CHU/ASY setup now writes
the FORM-12/13/18 adapter and signature-achievement-writer attestations only
after package identity, politics, institutional leader, force, and visual
receipts pass. Art completion and attestation do not bypass the hidden
achievement trigger contracts. The two IW-043/IW-058 signature achievements
remain hidden until their exact route and survival proof conditions are met.
No custom Event 006 advisor, adviser, dossier, or portrait asset is permitted;
all eight institutional characters remain male.

## Asset source modes

The authoritative asset matrix is `matrices/006_asset_family_registry.csv`.

Every asset entry states:

- asset type
- target size
- source mode
- visual role
- final folder direction
- static or animated status
- reference folder
- manifest requirement

## Text and localisation direction

The planning package does not provide final localisation.

Implementation must write final text for:

- wave entry event
- country opening events
- host crisis events
- foreign reaction events
- evolution milestones
- mechanic values and breakdowns
- decisions and missions
- focus names and descriptions
- league charter and votes
- formable decisions and integration
- achievements
- Event Details
- event log
- cluster details
- triggerable scenario UI
- super-events after research

### Tone by surface

#### Wave summary

Concrete public scenes from several regions. Emphasize governments, crowds, armed units, local institutions, and confusion. Avoid a dry map summary.

#### Released country opening

Local viewpoint and urgent practical problem. Mention the institution that took power and the source of the first forces.

#### Host crisis

Focus on loss of command, divided institutions, soldiers, refugees, debt, property, and political pressure. Avoid generic humiliation language.

#### Recognition

Diplomatic and legal tone with visible consequences. Avoid implementation language and reward lists.

#### League

Institutional, political, and strategic. Tone changes by charter.

#### High chaos

Confident, strange, revisionist, or frightening according to route. Avoid generic apocalypse wording.

### Completed research handoff

The two final super-event text packages and musical selections are approved in `research/006_super_event_text_research.md` and `research/006_super_event_audio_research.md`. The corrected descriptions preserve the accepted triggers and tone. The `6002` United States Marine Band source is verified and preserved for production. The accepted `6001` London Brass Players recording is blocked for United States redistribution and must not be processed or wired without permission or a waiver. A replacement quote or recording requires explicit user approval and a new verified source note.

## Event log and catalog direction

Event 6 remains:

- ID 6
- Minor Repeatable
- Liberations cluster member
- current status To Be Reworked until implementation is complete

The Event Details entry should describe sudden waves of new states and their struggle for survival. It should not list mechanic values, modifiers, wave algorithms, or hidden formables.

Evolution details should describe public changes in the pattern of new states. They should not describe ordinary wave counts as evolutions.

The spreadsheet row must be updated only after final in-game wording exists. The spreadsheet worker should mirror final Event Details, evolution, cluster, and scenario text rather than paraphrasing this spec.

## Documentation plan

Implementation should create or update:

- canonical event doc under `docs/events/006_independence_wave/overview.md`
- country package registry documentation
- regional overlay documentation
- focus tree and overlay documentation
- decision and mechanic documentation
- formable registry documentation
- league system documentation
- triggerable scenario documentation
- asset manifest and GFX handoff
- super-event research note
- achievement documentation
- Event 6 plan disposition and subagent handoffs
- catalog workbook after localisation is final

## Implementation staging

The event can be implemented in tranches, but no tranche is a fallback completion.

### Tranche 1

- origin system
- wave planner
- host safety
- doubled 6, 8, 10, 14, 20 automatic ladder, including 20 at World Collapse
- registered candidate pool
- core country values
- basic survival decisions
- starting forces
- event log and docs

### Tranche 2

- full common focus framework
- regional overlays
- patron system
- former-host system
- AI route behavior
- expanded candidate registry

### Tranche 3

- league network and faction mechanics
- formable framework
- signature country modules
- achievements
- advanced assets

### Tranche 4

- high-chaos candidate pool
- hidden routes and formables
- super-events
- triggerable scenario
- final catalog and completion audits

If implementation is staged, unresolved tranches remain explicitly queued. The event cannot be called fully reworked until the accepted specification is complete or deviations are approved and documented.

## Acceptance criteria

### Controlling acceptance authority (2026-07-29)

Completion is evaluated from source and static evidence. Repository source inspection, MCP inspections, transaction and source audits, asset audits, documentation reconciliation, and catalog alignment remain required. Live or in-game execution, save/load behavior, runtime consumer observation, and player-owned evidence are optional future QA and are not completion blockers. This decision does not waive static package-capacity, incomplete-package, formable, asset, focus-diagnostic, rights, route, AI, or wiring requirements.

### Release planner

- exact wave counts by chaos band
- synchronized release
- unique anchors
- host retains at least one state
- capital preference works
- overlap and living-tag checks work
- repeat memory works
- Event 5 origin collision is safe

### Country content

- every released country has an origin marker
- every country receives values, decisions, ideas, forces, and AI
- every country receives the shared generic tree or a reviewed additive carrier assignment
- existing meaningful trees are preserved
- no serious fighting country spawns empty
- all new tags and route tags end in `X`

### Mechanics

- all values are visible and dynamic
- focuses, decisions, missions, events, wars, patrons, and league actions change them
- blocked requirements are readable
- cleanup works after annexation, reunion, formable, and host death

### Focus trees

- survival, government, economy, military, diplomacy, former host, expansion, league, and ambition content exists
- routes have real depth and payoffs
- regional overlays change play
- signature countries have gated package modules inside the shared generic tree; no separate bespoke focus-tree definition is required in the current scope
- AI route behavior exists
- negative ideas have lifecycles
- icons and localisation are complete

### Decisions and missions

- action-based objectives
- varied dynamic costs
- success, failure, and partial outcomes
- active mission caps and clutter control
- AI equivalents
- exploit protection

### League

- network exists before faction
- formation has membership and charter rules
- cohesion, cause, patron capture, reserve, and confidence matter
- shared goals and failure states exist
- AI can join, contribute, refuse, rescue, challenge, and leave
- faction war logic matches charter

### Formables

- regional registry works across candidates
- formation uses decisions and map checks
- integration is staged where needed
- hidden routes have reveal logic
- flags, names, leaders, AI, and post-formation play exist

### Scenario

- scenario ID registered
- all viable candidates are attempted at every intensity
- intensity changes territory and forces
- type selector changes diplomacy and war setup
- six numeric scenario families expose eight player-facing modes because Universal Belligerence has three independently selectable rules
- source and MCP acceptance coverage maps all eight modes at Low, Medium, High, and Maximum for 32 mode/intensity cells; live cell execution is optional future QA
- Universal Belligerence rules have separate target-selection and result evidence rows
- blocked candidates are reported
- host and overlap safety remains active

### Super-events

- league formation super-event fires only at a durable league threshold
- danger super-event fires only at a globally important aggressive threshold
- text, quotes, images, audio, and wiring are complete and sourced
- normal waves do not receive super-events

### Assets and localisation

- no placeholder visible assets remain
- historical flags and real portraits are sourced
- generated fictional assets have manifests
- animations use real source frames and static fallbacks
- all visible keys exist
- Event Details and catalog wording align

### Audits

Before completion:

- focus tree audit
- decision and mission audit
- country package audit
- localisation audit
- completion audit
- documentation cleanup
- spreadsheet update
- final improvement-loop closure or resolved addendum

## Completion proof

A completion report should include:

- route coverage table
- candidate package coverage count by region and depth level
- formable family coverage
- mechanics value and action map
- AI source and weight inspections with declared scenario inputs
- host survival tests
- Event 5 and Event 6 collision tests
- triggerable-scenario source and MCP inspections for all 32 selectable mode/intensity cells and the bounded collision, selector, rollback, and persistence sweeps; live execution and save/load are optional future QA
- asset manifest status
- super-event research and wiring status
- achievement tracking status
- docs and catalog alignment
- all simplifications, omissions, and blockers

No simplification is implied by this specification. Any reduced implementation must be reported and approved rather than presented as full completion.
