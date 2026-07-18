
# Living World Event Ecosystem

Working labels in this file are not final localisation.

## Design promise

The Fallout scenario must feel inhabited from the first day after the blackout through at least ten years of continued play. States, governments, armed groups, families, institutions, trade routes, ruins, ecosystems, and memories must keep changing. The event layer is responsible for making those changes visible and playable.

The event system must do more than report suffering. It must create choices, relationships, rivalries, local institutions, recurring characters, partial recoveries, unexpected competence, political disputes, cultural change, and new reasons for war or cooperation.

## Catalogue scale

The full implementation target is roughly 660 to 910 unique Fallout event blocks.

A practical content distribution is:

| Layer | Target event blocks | Role |
| --- | ---: | --- |
| Transition and orientation | 20 to 30 | Blackout sequencing, rewrite handoff, player continuation, first country briefing |
| Global survival and society | 70 to 90 | Food, water, shelter, health, salvage, power, crime, culture, family, law |
| Regional and biome | 90 to 120 | Region-specific climate, infrastructure, food systems, transport, memory, ecology |
| Government archetype | 120 to 160 | Twelve archetypes with distinct internal politics and recurring crises |
| Successor country memory | 190 to 260 | At least two unique chains for each selected candidate, with 99-candidate coverage |
| Character and leader | 50 to 70 | Recurring people, councils, officers, doctors, engineers, organizers, children |
| Diplomacy, trade, war, and settlement | 45 to 65 | Contact, recognition, compacts, raids, corridors, wars, peace, integration |
| Cause memory, mutant fiction, and altered ecology | 35 to 55 | Cause-specific aftermath, fictional altered societies, nonhuman ecology |
| Recovery, generation change, and late world order | 40 to 60 | Thaw, rebuilding, constitutions, successor generations, blocs, long ambitions |

The target is not a quota for filler. Every event block must change a value, state, relationship, character, decision, mission, idea lifecycle, focus route, military package, or future event weight.

## Per-campaign event volume

A human country should normally see roughly 90 to 180 meaningful visible events during ten years of Fallout play.

The exact number depends on:

- player speed and pause behavior
- country size
- number of active arcs
- government archetype
- regional danger
- wars
- contact network
- survival pressure
- route choices
- climate phase
- cause memory
- use of optional incident notifications

The event system must not display several unrelated popups on one day. A dense library should create variety between campaigns.

## Event file and namespace

All Fallout events belong in:

`events/fallout_world_end_events.txt`

The file uses:

`add_namespace = chaosx.fallout`

The file is organized into internal sections:

1. request and transition
2. player continuation and orientation
3. global survival
4. regional pools
5. archetype pools
6. successor memory pools
7. character arcs
8. diplomacy and war
9. cause memory and fictional altered content
10. recovery and late-game world order
11. hidden AI resolution and cleanup

Future event work normally scans the dedicated file and assigns the next free suffixes in stable sections. The accepted Ash-week orientation contract is the documented exception and reserves `chaosx.fallout.62` through `chaosx.fallout.84` for its five components, result events, closure, and cleanup identities.

## Event identity model

Every event records several context fields.

Required context dimensions:

- Fallout phase
- country or state owner
- region
- biome or state class
- government archetype
- country-memory package
- cause memory
- current winter phase
- current survival-resource crisis
- active route
- neighboring archetypes
- recurring character or institution
- prior event memory
- visible severity
- whether the event is local, national, bilateral, regional, or global

An event may belong to more than one family, but it has one primary family for fatigue and cadence.

## Event classes

### Orientation events

Orientation events explain what survived and what is failing. They open decisions, reveal starting values, introduce the first recurring characters, and identify the country's immediate crisis.

Every materialized playable successor receives the accepted five-component Ash-week orientation chain during the reveal grace period. The chain covers national orientation, capital or main-state condition, immediate resource crisis, government-archetype introduction, and the first character or institution. Its distinct visible and hidden roots, delayed results, closure, and cleanup use reserved suffixes `chaosx.fallout.62` through `chaosx.fallout.84`. The exact sequence, timing, identity, parity, recovery, asset, and non-activation contract is authoritative in `03_fallout_timeline_and_campaign_pacing.md`.

### Arc events

Arc events are ordered chains with persistent memory. They change politics, characters, institutions, borders, or route access. A country should have one to three active major arcs at a time.

### Crisis incidents

Crisis incidents react to current mechanics, such as food collapse, filter failure, a broken rail corridor, a refugee surge, or a reactor emergency. They often open a timed mission.

### Routine incidents

Routine incidents show daily survival and social change. They still have effects. They should be shorter, less frequent, and more varied than crisis incidents.

### Relationship events

Relationship events involve another country, neighbor, enclave, convoy, faction, character, or social group. They create memory on both sides.

### Broadcast events

Broadcast events inform many countries about major regional changes, first contacts, new compacts, large wars, restored power grids, or extraordinary recoveries. They are not ordinary super-events.

### Hidden AI resolution

AI countries receive the same mechanical choices. When a player-facing popup would create noise, the AI resolves through hidden events that use the same choice weights and effects.

## Scheduling model

The Fallout event scheduler is separate from the ordinary Chaos Redux random-event picker.

The scheduler maintains:

- country event readiness
- active arc count
- last visible Fallout event date
- family fatigue
- regional broadcast cooldown
- bilateral event reservation
- character arc reservation
- crisis priority
- player relevance
- no-popup quiet period after the blackout

A country becomes eligible for a visible Fallout event when its local cooldown expires and at least one candidate family has a positive score.

## Candidate scoring

A candidate score should include:

- base family weight
- phase suitability
- severity
- unresolved mechanic pressure
- player relevance
- state value
- region match
- archetype match
- cause-memory match
- relationship opportunity
- recurring character availability
- route match
- previous choice memory
- family fatigue penalty
- recent event penalty
- active arc cap
- repeated-state penalty
- recent war or crisis priority

The scheduler selects one event from the highest relevant pool, then applies a family cooldown.

## Anti-spam rules

- One human country normally receives no more than one ordinary Fallout popup in fourteen days.
- A major crisis may break the limit once, then impose a longer recovery cooldown.
- A global broadcast cannot be followed by another global broadcast for at least thirty days unless the world rewrite is still in progress.
- The same event family cannot appear twice in a row.
- The same state cannot be the focus of three visible incidents in a short period unless it is the capital or an active siege.
- A recurring character cannot trigger two separate arcs at once.
- A country cannot hold more than three major unresolved event arcs.
- AI-only outcomes do not consume the human player's visible event budget.
- A decision or mission should carry ongoing pressure when repeated popups would add little.

## Event memory

Event memory is essential for a ten-year scenario.

Memory categories:

- choice memory
- institution memory
- character loyalty
- character injury or death
- relationship trust
- atrocity or betrayal
- relief received
- trade debt
- refugee treatment
- mutant recognition policy
- old-world restoration policy
- salvage law
- ration law
- constitutional direction
- war settlement
- climate adaptation
- cause-memory interpretation

Memory should alter later event text direction, options, AI weights, focus availability, diplomatic reactions, and achievements.

## Real effects standard

Every visible event must have at least one material effect.

Accepted material effects include:

- change food, water, medicine, salvage, power, shelter, radiation burden, cohesion, memory, or reclamation
- change state population through the shared Deaths system
- damage or repair a building
- change winter exposure, climate adaptation, or state category damage
- start, advance, cancel, or fail a mission
- add, modify, replace, or remove an idea
- add or remove an advisor, commander, leader, or character trait
- change a government archetype route
- alter a focus branch or decision family
- move refugees or skilled population
- create or change bilateral trust, recognition, debt, embargo, access, or compact membership
- create claims, border pressure, war preparation, peace terms, or integration work
- reveal a salvage zone, refuge, water source, seed vault, reactor, station, or forbidden zone
- create a military formation with a clear source and cost
- change future event weights or unlock a follow-up chain

A temporary minor modifier can support an event. It cannot be the whole outcome of an important choice.

## Choice design

Most important events should provide two to four choices.

Choices should represent real differences such as:

- consume reserves or accept deaths
- save infrastructure or move people
- centralize authority or empower local councils
- admit refugees or preserve shelter space
- share technology or keep a monopoly
- recognize altered people or enforce quarantine
- trade food for fuel or remain independent
- preserve an old institution or build a new one
- punish raiders or negotiate transit
- restore a city or abandon it
- accept short-term production loss to reduce long-term climate damage
- use coercion and gain output while damaging cohesion and future legitimacy

AI weights depend on archetype, resources, war state, route, character influence, and previous memory.

## Positive and mixed events

At least one third of routine and society incidents should offer competence, adaptation, humor, affection, celebration, discovery, or partial recovery.

Examples of positive event roles:

- a repaired radio connects two settlements
- children develop a new school calendar
- a greenhouse produces the first surplus
- a river convoy arrives
- an old engineer teaches apprentices
- a mutant and human medical team solves a local problem
- a recovered song or sport becomes a civic ritual
- an abandoned machine shop becomes a public workshop
- a marriage or adoption links rival communities
- a successful thaw repair saves a rail line
- a local election removes a ration thief
- a militia turns into a fire and rescue brigade

Positive events still change mechanics. They should not become reward giveaways without cost or prior preparation.

## Tone distribution

The event library should contain:

- urgent crises
- political disputes
- hard moral choices
- technical problems
- domestic life
- local humor
- cultural memory
- military conflict
- exploration
- diplomacy
- discovery
- recovery
- strange high-chaos content
- quiet generational change

The scenario should not read as one continuous funeral. Repetition of the same bleak tone will make a large event library feel smaller.

## Event art use

Not every event needs unique art.

Use unique report art for:

- major orientation chains
- recurring character introductions
- major regional crises
- first diplomatic contacts
- landmark recoveries
- first mutant recognition events
- major war settlements
- late world-order events

Routine incidents can share carefully grouped Fallout-owned report images when the subject, region, and cause memory match. No zombie-owned image or path may be used.

## Event log and documentation

Fallout events should have a dedicated event-history filter or a clear Fallout source marker in the existing log system.

The log records:

- working family or final event identity
- date
- actor
- target or state where relevant
- phase
- major choice
- relationship partner
- arc stage
- outcome

Routine incidents may use compact log entries. Major arcs and broadcasts require full entries.

## Save and multiplayer behavior

- The host owns event selection and effects.
- A bilateral event reserves both countries before firing.
- A character arc stores its actor and country.
- Save-load preserves active arcs, cooldowns, fatigue, reservations, and event memory.
- If a reserved target disappears, the event cancels cleanly or selects a valid successor.
- Human countries receive their own choices.
- A global event cannot force one human player's choice onto another human country without a separate response event.

## Completion standard

The event ecosystem is not complete when only the transition, opening orientation, and a few survival incidents exist.

Completion requires:

- all event layers represented
- every government archetype has a real internal event pool
- every region has a real regional pool
- every selected successor has unique country-memory chains
- recurring characters exist
- bilateral and multilateral relationships create memory
- war has causes and aftermath
- recovery creates new problems and opportunities
- the second generation changes politics
- AI resolves the same systems
- the visible event budget prevents spam
- event effects connect to the survival, climate, focus, decision, state, population, building, and diplomatic systems
