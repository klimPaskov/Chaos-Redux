# Country-package implementation prompt for Event 044 Yakub Returns

Use `chaos-redux-events`, `chaos-redux-focus-trees`, `chaos-redux-decisions-missions`, `chaos-redux-event-assets`, `chaos-redux-subagents`, and `AGENTS.md`.

Read spec parts 2 through 4, the country package matrix, focus architecture, AI strategy matrix, acceptance criteria, asset prompt, and focus-tree prompt.

## Tag and identity audit

Before assigning any tag, audit:

- installed vanilla country tags and identities
- all Chaos Redux tags and protected carrier collections
- every installed Workshop mod
- sibling local mods
- existing event-created carrier registries

If the intended identity already exists in vanilla, reuse it safely and preserve meaningful existing content. If a protected Chaos Redux carrier fits, use the matching collection and record provenance. Do not create a duplicate identity.

Lock the tag before flags, country files, character ownership, or runtime names are finalized. Record audited roots, conflicts, no-match evidence, and final disposition.

## American anchor state

Implement one full playable American Event 44 state package.

Formation paths:

- negotiated sovereignty
- unilateral secession
- federal collapse
- autonomous compact

Territorial packages:

- Great Lakes industrial compact, Detroit preferred
- Atlantic urban compact
- Southern congress
- negotiated district

Territory depends on chapter institutions, political control, local defections, negotiated cession, municipal authority, and actual campaign control. Race or assumed racial demographics cannot select territory.

Prefer contiguous territory. Handle enclaves only through explicit compact, port, corridor, or campaign-state proof.

## Country classification

The state is human.

It may receive a stable special Chaos country marker only when shared routing needs one. It must remain outside `is_actual_nonhuman_country` and must use normal civilian systems.

Audit and document:

- famine
- migration
- occupation
- population loss
- Deaths
- diplomacy
- peace conferences
- subjects
- normal civilian events

Any shared classifier change must update `chaosx_dynamic_triggers` source and documentation. Event-specific lifecycle checks stay in Event 44 files.

## Starting government and identity

Implement:

- public and cosmetic country names
- adjective
- map color
- capital and fallback capital
- ruling party and party names
- starting laws
- leader or institutional leadership
- route-specific leader changes
- normal, medium, and small flags
- route-specific flags and cosmetic identities
- International identity where required

Yakub may lead directly, appoint a council, or remain supreme ideological founder. Founder state must change leader availability.

Use fictional one-person leaders or institutional councils for new route leaders. Do not assign real historical figures invented allegiance.

## Starting ideas

The accepted starting idea set is:

- Disputed Revelation
- Parallel Institutions
- Improvised National Defense

Each idea needs negative or mixed starting effects and route-specific mitigation, replacement, upgrade, corruption, or removal.

Do not add a large stack of generic positive ideas. Document the complete lifecycle table.

## Economy and production

Scale starting capacity from received territory and formation path.

Include:

- inherited factories and infrastructure
- damage from civil war or peaceful transfer
- captured or transferred stockpiles
- supply hubs, railways, ports, and convoys
- fuel and train needs
- consumer economy and emergency administration
- route-specific cooperative, state-directed, or regulated enterprise development

A negotiated one-state compact must remain viable through supply, trade, transit, guarantee, or economic support. It must not receive a major-power industrial package for free.

## Technology

Use a bounded technology inheritance and compatibility approach based on formation source, defectors, captured institutions, and route.

Do not grant every American technology automatically. Preserve mutually exclusive industry branches and other incompatible technologies through the established union helper where relevant.

Any new technology or doctrine content requires `hoi4.tech_inspect`, `hoi4.tech_render`, and `hoi4.tech_compare`. The accepted design does not require a new technology tree.

## Starting armed forces

Use ordinary period units and equipment. No custom sub-unit, custom equipment family, custom 3D model, custom counter, or custom voice package is required.

Dynamic force factors:

- controlled population
- state count
- captured depots
- military and police defections
- chapter defense institutions
- formation path
- United States weakness
- current war
- foreign support
- Chaos and evolution state

Accepted templates:

- community defense brigade
- national guard brigade
- mobile reserve
- artillery group

Templates may use vanilla battalions because the movement's military identity comes from recruitment, organization, supply, route, and progression rather than a biologically or technologically distinct unit family.

Starting forces must be usable and limited. A small compact receives militia and a defensive core. A large federal-collapse state may receive more defectors and equipment. No flat division count applies to every package.

## Reinforcement and growth

Implement growth through:

- organize community defense
- integrate defectors
- secure depots
- invite volunteer cadres
- build the national arsenal
- mobilization and training
- foreign aid corridors
- focus rewards
- International support
- captured equipment
- demobilization after emergency

Prevent free-unit loops. Tie unit creation to manpower, equipment, training, state institutions, depots, or foreign routes.

## Navy and air force

A landlocked or small state may begin without a meaningful navy or air force. Coastal territory, defecting bases, captured aircraft, and route development can create them.

Do not spawn large fleets or air forces without territorial and source proof. Provide later acquisition, production, volunteer, and training paths.

## Focus and decisions

Load the full American focus tree only for the valid Event 44 state and origin. Preserve origin proof when a carrier tag can be reused by another event.

Wire the state-building decision category, route decisions, recognition, integration, formables, International relations, and terminal readiness.

Implement the two regional formation paths:

### North American New Nation

Requirements:

- stable Event 44 state
- substantial contiguous region
- local institutions
- constitutional or route-specific integration
- staged cores or federal membership

### Diaspora Federation

Requirements:

- Evolution III
- several independent member states
- at least two world regions
- high International Cohesion
- member approval or successful federation conflict
- valid anchor
- no active succession crisis

Member territory does not become instant cores of the anchor.

## United States aftermath

A peaceful partition needs:

- treaty relations
- trade and transit
- border security
- reconciliation, containment, rivalry, or coexistence policy
- future reunification or permanent separation handling

A civil war needs:

- valid war participants
- army and equipment division
- settlement choices
- postwar occupation or recognition
- no zero-state or duplicate-country outcome

The United States must remain playable and retain coherent vanilla or mod content outside the exact event changes.

## Foreign regional state packages

Implement bounded valid packages for regional breakaways from:

- Caribbean
- Brazil
- Britain
- France
- West Africa
- South Africa
- Ethiopia
- Liberia

Each package needs:

- local identity
- valid territory
- capital
- leader or institution
- parties
- flags
- starting ideas
- forces
- economy
- shared regional tree module
- local decisions
- International stance
- AI
- annexation and cleanup

Do not force every region to create a state. Legal movements, autonomous zones, parties, and allied governments are valid outcomes.

## AI

Implement route and survival AI using territory, industry, supply, recognition, founder state, faction strength, relations, war, International status, and Chaos.

The AI must not:

- select invalid route content
- create impossible formables
- abandon an exposed one-state country without defense
- raise units without equipment
- accept subject status through every aid offer
- join a supremacist International when local politics reject it
- pursue terminal commitment from a hopeless position

Complex route or target weights require the probability audit workflow.

## Assets and documentation

Coordinate all portraits, flags, focus icons, idea icons, report images, and emblems through the asset prompt. No placeholder flag or portrait can support a completion claim.

Document:

- tag audit
- origin and carrier proof
- territory packages
- capitals and fallbacks
- leader ownership
- party and identity states
- ideas and lifecycles
- forces and scaling
- economy and technology
- focus loading
- decisions
- AI
- formables
- cleanup
- asset crosswalk

Run the country-package auditor after implementation. Resolve every tag, history, state, leader, flag, party, focus, idea, force, technology, supply, AI, formable, and cleanup finding before completion.
