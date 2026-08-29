# Event 31 Random Terror specification

## Part 5: Territorial insurgency and country packages

## Country-package purpose

A territorial Event 31 actor must be a real playable country package.

It needs viable territory, a capital, a political identity, a fictional leader or council, starting forces, equipment, technology, economy, decisions, focus routes, reinforcement, diplomacy, AI, defeat behavior, and visible assets.

A flag and a handful of militia divisions are not enough.

The package should still be reusable because several countries can appear in one campaign.

It should adapt to the organization's profile, region, origin, evolution, and current territory.

## Territorial actor profiles

### Local Cell State

A small actor formed from one isolated or border state.

It has limited administration, improvised units, weak supply, and a narrow survival goal.

It normally seeks a sponsor, a corridor, more territory from the parent, or a negotiated enclave.

### Regional Insurgent State

A stronger actor formed from several connected states or a large civil-war share.

It has a functioning command, captured industry, a recruitment system, and a route toward regional domination or settlement.

### Transnational Network State

A territorial safe haven that directs cells across borders.

It values ports, border corridors, training areas, intelligence, foreign sponsorship, and Network Reach.

Its domestic administration can remain weak while its external network is strong.

### Jihadist International State

A territorial actor that enters the Evolution IV fictional jihadist route.

It combines forced rule, foreign fighters, international coordination, rivalry over religious authority, and conflict with Muslim governments and other enemies.

### Final Revelation State

The world-end actor led by the ambiguous entity.

It is a terminal transformation of existing jihadist power, not an ordinary baseline country spawn.

Its abilities and presentation are defined in Part 8.

## Organization identity generation

Each actor receives a stable fictional package identity when its parent organization becomes durable.

The identity draws from:

- broad region
- leadership form
- strategic profile
- ideology family
- current evolution
- territorial origin
- sponsor or rivalry history
- takeover or secession origin

Possible leadership forms include:

- clandestine directorate
- war council
- ideological secretariat
- military command
- revolutionary committee
- territorial emirate for the fictional jihadist branch
- divided coalition
- charismatic fictional leader
- institutional council

Names should sound plausible inside the alternate-history campaign without copying real organizations.

No name should combine a real community, religion, ethnicity, or nationality with terrorism as a generic label.

The final identity must remain stable through state gains, losses, save reload, and ordinary focus progression.

Route transformations can add a cosmetic name and flag while preserving the actor's event lineage.

## Territory-seizure requirements

A normal territorial seizure requires:

- at least one Armed Insurgency or Lost Local Control state
- sufficient Terror Pressure
- an organization with an active local base
- evidence of local armed strength, defection, captured equipment, or collapsed government control
- a viable country carrier
- a valid capital state
- a parent country that can retain viable territory or undergo a full takeover

The first territorial package should prefer a contiguous enclave.

A noncontiguous package is allowed only when the movement has separate established strongholds and the actor can maintain them through ports, corridors, or an existing war.

Wastelands, invalid empty states, isolated meaningless regions, and occupied enemy territory outside the crisis cannot be transferred simply to enlarge the actor.

## Parent-country survival

A secession should leave the parent with at least one owned and controlled core state, a capital or valid replacement, and a viable path to continue the conflict.

When that is impossible, the event chooses between:

- a government takeover
- a capital crisis with a smaller rebel enclave
- a civil war division that preserves both sides
- a negotiated autonomous actor
- postponing territorial creation until a valid map exists

The engine should not create a one-state parent with no capital, no supply, and no army merely to preserve a formal split.

## Capital selection

The actor's capital should normally be:

- a controlled state inside its founding territory
- populated
- connected to its main territory
- defensible enough to serve as a command center
- supported by infrastructure or local administration
- distinct from a frontline tile when a safer valid alternative exists

A captured national capital can become the actor's capital only when the takeover branch supports it.

A local or regional actor can rename a fictional administrative center through scripted localisation when the route and state identity support it.

No invented city name should overwrite a well-known real city without a route-specific reason and player-facing event.

## Carrier and identity transaction

The implementation must use the shared country-carrier registry and release transaction patterns.

Before assigning a carrier, the implementation needs a collision audit across:

- vanilla countries
- active Chaos Redux countries
- protected Event 006 and Soviet Collapse carriers
- installed Workshop references
- other local mods included in the project audit scope
- active Event 31 actors

A carrier must preserve origin, parent, organization, region, route, and package identity.

A carrier is cleared only after its actor is fully defeated, annexed, merged, or transformed and every reference has been cleaned.

Two active organizations cannot silently share one carrier.

## Political identity

Ordinary Event 31 territorial actors use an event-owned extremist political identity.

The political package should distinguish leadership and route without treating a vanilla ideology as a direct synonym for terrorism.

The ruling identity can be represented through a dedicated subideology, event-owned politics, party names, cosmetic names, and route-specific AI.

Possible route families include authoritarian military command, revolutionary absolutism, criminal-political rule, millenarian cult government, fictional ultranationalist restoration, and the later jihadist current.

The exact political presentation should fit current Chaos Redux ideology infrastructure and avoid a new ideology family unless the live repository proves it is necessary.

## Leaders and portraits

Every visible Event 31 leader is fictional or institutional.

The portrait source classification is therefore `fictional_high_chaos` for one-person leaders and fictional institutional for councils.

Portraits are produced through `chaosx_portrait_creator` with native ImageGen.

Requirements:

- full `156x210` country-leader framing
- period-appropriate clothing and photographic treatment
- one memorable invented motif tied to the actor's route
- no real-person resemblance target
- no ethnic caricature
- no real extremist insignia
- no modern tactical equipment
- no readable generated text
- matching gender and name metadata
- stable runtime identity

Institutional councils can use a staged group only when the accepted portrait brief authorizes it. A symbolic empty-chair, masked council chamber, or seal portrait can be used when it reads clearly at leader size and does not become a generic placeholder.

Leadership succession must be planned.

A territorial actor should not become leaderless when a fictional commander dies, defects, loses a power struggle, or merges into another actor.

## Flags and emblems

Every flag uses ImageGen under the flat flag-design workflow.

The design must be:

- fictional
- flat
- readable at normal, medium, and small sizes
- free of fabric folds, scenery, gradients, perspective, and fake lettering
- free of real extremist symbols
- free of sacred calligraphy used as hostile branding
- distinct between base, route, jihadist, merger, and final identities

A coordinated family can share geometry or a color relationship.

Ideology and route variants must remain genuinely distinct designs, not simple recolors.

The same symbol can appear on a faction emblem, focus icon family, and country flag only when each asset is independently designed for its surface.

## Starting ideas

A new actor should begin with no more than three deep ideas.

### Improvised Command

Starting role:

- weak coordination
- limited planning
- militia fragmentation
- unreliable officer structure

Mitigation paths:

- Shadow Council route improves concealment and coordination
- War Directorate centralizes field command
- Ideological Secretariat improves obedience and recruitment

Failure forms:

- rival commanders
- purges
- splinter warfare

Final forms vary by route.

### Captured Economy

Starting role:

- disrupted factories
- stolen or improvised supply
- dependence on captured stockpiles
- poor repair capacity

Mitigation paths:

- controlled extraction
- criminal and smuggling economy
- foreign sponsorship
- civil administration and taxation
- captured industrial reconstruction

Failure forms:

- looting spiral
- famine and collapse
- sponsor dependency

### Contested Legitimacy

Starting role:

- population resistance
- weak recognition
- parent-government claims
- unstable local compliance

Mitigation paths:

- coercive rule
- service provision
- ideological mobilization
- foreign recognition
- merger into a larger Event 31 structure

Failure forms:

- local revolt
- defections
- negotiated surrender
- leadership split

The focus tree and decisions should replace or transform these ideas.

The actor must not finish the campaign with the starting negative stack unchanged.

## Country values

Territorial actors manage three visible values.

### Territorial Control

Measures administration, garrison reach, local compliance, and secure control of held states.

Low control raises resistance, defection, sabotage, and collapse risk.

High control unlocks taxation, recruitment, construction, and integration.

### Network Authority

Measures the actor's influence over cells, foreign fighters, splinters, and other territorial organizations.

High authority improves overseas support and merger leadership.

Low authority creates rivalry and limits external operations.

### External Supply

Measures sponsors, captured depots, smuggling corridors, ports, foreign assistance, and protected transport.

It affects equipment replacement, fuel, force growth, and foreign operations.

These values should be shown in a normal decision category with clear stages and concise tooltips.

No dedicated country mechanic window is required.

## Starting research and technology

A local cell state begins with `2` research slots.

A regional insurgent state begins with `3` research slots.

A transnational or jihadist state can reach `4` through administration and captured institutions.

The final world-end state can reach `5` as part of its terminal package.

The actor receives a safe union of compatible technologies from its parent and actual donors.

Technology grants should reflect:

- the parent's researched equipment
- captured military units and stockpiles
- controlled industry
- defecting officers and scientists
- current date
- sponsor support

The actor does not receive every parent technology automatically.

Mutually exclusive industry and doctrine branches must remain valid.

No advanced custom technology is granted merely because the actor formed.

An actor that captures a real research center or receives a sponsor project can gain a bounded research bonus or later technology through play.

## Starting forces

Starting force size depends on territory, population, captured units, state activity, defection, and evolution.

The following values are balance anchors.

| Actor profile | Typical starting formations |
| --- | --- |
| Local Cell State | `4` to `8` militia or irregular infantry divisions |
| Regional Insurgent State | `8` to `16` mixed infantry and mobile formations |
| Transnational Network State | `12` to `24` formations with stronger support and reserves |
| Jihadist International State | `15` to `30` formations, scaled by real territory and foreign-fighter routes |
| Final Revelation State | merged surviving formations plus pressure-scaled uprisings |

The actor uses existing combat battalions and support companies.

Suggested templates can include:

- light militia infantry
- captured regular infantry
- mobile raiding infantry using available trucks
- defensive urban infantry
- border and mountain infantry when the territory supports it

No new Event 31 battalion is required.

No template receives equipment that the actor cannot obtain.

Formations should spawn in controlled states with supply and avoid immediate encirclement when a safer valid state exists.

## Equipment and manpower

The starting package draws from:

- a bounded share of captured parent stockpile
- equipment held by defecting units
- local arms and support equipment created by the event's abstract buildup
- sponsor transfers already established in the chain
- controlled factories and production lines

The actor receives enough basic equipment to make its starting divisions functional.

It should not receive years of reserve stockpile or top-tier equipment without a source.

Manpower comes from controlled population, existing armed cells, defectors, foreign fighters, and recruitment decisions.

Deaths do not convert directly into manpower.

Force growth must remain connected to population, equipment, supply, and Territorial Control.

## Reinforcement pathways

A fighting actor needs several future force paths.

- recruit local militia from controlled population
- absorb armed cells after a state seizure
- integrate defecting police or military units
- capture depots and production lines
- receive sponsor equipment
- attract foreign fighters after Evolution II or IV
- convert militia into regular formations through the military route
- raise emergency defenders during a parent offensive
- inherit bounded forces during an actor merger

Every pathway has a cost, cooldown, resource source, or control requirement.

No repeatable free-unit loop is allowed.

## Industry and construction

The actor inherits the real buildings in controlled states, including damage.

The starting economy should reflect disruption.

A local actor can have weak construction and production penalties until it stabilizes administration.

The economy routes can:

- repair captured factories
- protect depots
- rebuild railways and infrastructure
- expand controlled extraction
- establish coerced requisition
- create a criminal trade network
- accept sponsor construction
- build a civil tax administration
- fortify border corridors
- improve ports or airbases when they exist

Rewards should be state-based when possible.

A landlocked actor should not receive a token naval branch or free dockyards.

## Air force

No actor receives a free air force by default.

An air capability can arise through:

- captured aircraft at a controlled airbase
- defecting pilots
- sponsor transfers
- repaired local production
- later focus and decision investment

The actor should begin with no aircraft when no source exists.

A developed territorial actor can use reconnaissance, interception, transport support, or ground support according to equipment.

No unique Event 31 aircraft model is required.

## Navy

No actor receives a free navy by default.

A coastal actor can begin with convoys needed for supply and can later acquire limited patrol or escort capacity through captured ports, defections, purchases, or sponsors.

Capital ships require a real defection or capture event and should remain rare.

A landlocked actor has no naval branch.

## Intelligence agency

A formal intelligence agency is optional.

It should be created only for a durable transnational, jihadist, or final actor that can use operations meaningfully.

Local actors use decisions and hidden network values instead of receiving an agency for flavor.

## Advisors and commanders

Durable actors can receive fictional advisors and commanders tied to route identity.

Useful roles include:

- field commander
- quartermaster
- captured-industry administrator
- foreign liaison
- internal security chief
- ideological organizer
- civil administrator
- smuggling coordinator
- faction negotiator

Advisors should unlock through focuses or events and change play.

They should not be added as decorative portrait workload.

Each authorized visible character needs its own portrait requirement.

## Diplomacy

A territorial actor can:

- seek recognition
- seek a sponsor
- join an Event 31 coordination structure
- merge with a compatible actor
- support cells abroad
- negotiate with the parent
- accept a ceasefire
- exchange prisoners
- enter a proxy relationship
- fight rival Event 31 actors
- fight Event 14 cannibals
- enter the fictional jihadist faction after meeting its route conditions

It cannot join the cannibal faction or treat cannibal actors as natural allies.

Normal factions should use strict acceptance based on ideology, sponsor interest, war, and international cost.

A major power can exploit an actor without granting full faction membership.

## Actor mergers

A merger requires:

- compatible route or a successful leadership contest
- connected or supportable territory
- clear carrier ownership
- valid capital and army transfer
- safe handling of wars, subjects, factions, leaders, ideas, and equipment
- player consent when a player-controlled actor would be absorbed

The merger preserves history and records which organization became dominant.

A weaker actor can become a regional command, subject, faction member, or annexed territory according to the route.

A merger should not duplicate units, equipment, technology, or country ideas.

## Actor splits

A split can follow:

- leadership death
- low Network Authority
- failed merger
- unequal sponsor support
- doctrinal conflict
- military defeat
- resistance in a distant enclave
- jihadist leadership rivalry

The split uses valid territory and carrier availability.

It should not fire when no second viable actor can exist.

## Takeover of the parent

A victorious actor can replace the parent government.

The takeover should:

- preserve valid country ownership and capital
- replace or transform the country identity
- integrate surviving actor forces once
- reconcile technologies and stockpiles safely
- remove obsolete parent response decisions
- create resistance and legitimacy consequences
- open the Event 31 focus route suited to the takeover
- preserve foreign wars and diplomatic consequences where valid

The actor does not gain instant full cores or loyalty over every parent state.

Large or culturally divided states require staged consolidation.

## Defeat and cleanup

A defeated actor enters one of these outcomes.

### Military destruction

Territory returns to the parent or valid controller.

Surviving cells can remain dormant according to pressure and legitimacy.

### Negotiated surrender

The actor disarms under terms and the parent begins reintegration.

Hardliners can reject the settlement and remain as a smaller cell.

### Leadership decapitation and fragmentation

The actor loses central authority and splits into local cells or rival remnants.

### Foreign evacuation

Leaders and selected units escape to a sponsor or another Event 31 actor.

### Merger under pressure

The actor is absorbed by a stronger organization before defeat.

Cleanup must remove:

- country-specific decisions and missions
- active actor values
- invalid cell links
- temporary occupation and supply modifiers
- obsolete focus access
- world-threat source contribution when no qualifying actor remains
- carrier ownership after every consumer is cleared

It preserves Deaths, Condemnation, event history, lasting state damage, and surviving dormant cells.

## Special-country classification

Every territorial Event 31 actor and takeover identity is a special Chaos country.

It should be added to the shared `is_special_chaos_country` classification through a generic Event 31 actor marker.

It is not an actual nonhuman country.

The Final Revelation state remains a human-populated extremist country led by an ambiguous entity, so it also stays outside `is_actual_nonhuman_country` unless a later accepted design explicitly transforms the population.

## Asset and model boundary

The actor package requires flags, portraits, focus icons, idea icons, decision icons, a category picture, faction emblems, report art, and super-event art where relevant.

It does not require:

- a custom combat battalion
- a custom equipment archetype
- a 3D unit model
- a custom building model
- custom unit audio
- a bespoke unit counter

Existing HOI4 units and equipment are sufficient for the design.

This is an accepted scope decision, not a temporary fallback.

## Completion standard

A territorial country package is complete only when:

- the territory and capital are valid
- the parent remains viable or undergoes a valid takeover
- the carrier is collision-safe and origin-aware
- the actor has a stable fictional identity
- leader, flag, parties, ideas, and localisation agree
- the actor has functioning starting forces and equipment
- research slots and technology fit the actor profile
- economy, supply, air, and navy setup follow real territory and sources
- force growth requires resources and control
- the focus tree and decisions are playable
- AI can survive, expand, negotiate, split, merge, and lose
- defeat and annexation clean every active surface
- the actor is special Chaos but not nonhuman
