
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

Orientation reads Survival Cohesion and State Supply Access only from committed schema-3 ledgers. Country Cohesion opens from Food, Shelter capacity, and already-adjusted Recognition. State Supply Access opens from surviving post-rewrite infrastructure and drives a native local-supply penalty. State results mutate only the authenticated assigned capital through the live Air Winter and Supply Access helpers. Caller-supplied mirrors are forbidden. A stale or missing row blocks the result without a partial state write.

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

The scheduler maintains country readiness, frozen pacing size, active arc count, last visible Fallout event day, family fatigue, repeated event and state history, crisis-break history, bilateral reservations, character reservations, delayed results, visible-budget reservations, phase, player relevance, and the seven-day no-popup interval after reveal.

The stable post-allocation scheduler registry is the only country pool. A country with no frozen successor assignment row cannot enter the scheduler. Later conquest, state transfer, annexation, and fragmentation do not rewrite its pacing size.

| Frozen pacing size | States in committed successor assignment |
| --- | ---: |
| Small | 1 through 3 |
| Medium | 4 through 9 |
| Large | 10 or more |

The host-owned coordinator performs transaction reconciliation first. It then reviews every current human successor in the frozen player-continuation array once and reviews a bounded nonhuman registry batch from the stable cursor. Human countries are skipped when encountered by the AI cursor.

| Frozen scheduler registry count | AI countries reviewed per engine date |
| --- | ---: |
| 1 through 30 | 1 |
| 31 through 60 | 2 |
| 61 through 90 | 3 |
| 91 or more | 4 |

A country may commit at most one newly selected envelope on one engine date. Due results, callbacks, cancellations, and cleanup take priority. The scheduler does not create a second world-country iterator or a new all-country daily or monthly action.

## Cadence and visible budget

Ash week has no ordinary cadence. The orientation chain and the seven-day quiet interval own that period.

| Fallout phase | Small | Medium | Large |
| --- | ---: | ---: | ---: |
| First season, days 8 through 90 | 24 | 18 | 14 |
| First winter year, days 91 through 365 | 28 | 24 | 20 |
| Consolidation, days 366 through 730 | 32 | 28 | 24 |
| Rival orders, days 731 through 1460 | 34 | 30 | 26 |
| New states, days 1461 through 2190 | 36 | 32 | 28 |
| Soot retreat, days 2191 through 2920 | 38 | 34 | 30 |
| Second world, days 2921 through 3650 | 40 | 36 | 32 |
| Open continuation, day 3651 onward | 46 | 42 | 38 |

Every candidate declares an immutable integer visible-budget cost from 1 through 4. The cost includes its visible opening and every visible result or callback already promised by the same envelope. The opening reserves the phase and size cooldown multiplied by that cost. Later visible results may extend the due day by one current base cooldown. They cannot shorten the opening reservation. Hidden AI results, mechanical callbacks, and cleanup have zero visible-budget cost. An AI opening reserves the same narrative envelope against its own local cadence.

A crisis incident may break ordinary cadence only when normalized unresolved pressure is at least 80, the exact crisis target and resource remain current, no crisis break was committed for that country in the previous 180 days, and at least seven days have elapsed since its last visible Fallout popup. The break reserves 42 days multiplied by visible-budget cost. It cannot bypass an issued receipt, due result, or unresolved same-crisis transaction.

Global broadcasts keep a thirty-day global minimum. A visible broadcast consumes cost 1 for every human recipient and cannot clear or shorten a local cooldown. The blackout and world-rewrite presentation are outside this class.

## Candidate scoring

Every manually reviewed candidate names its phase and identity pool. It names the exact durable or live receipt behind every nonzero input. Working labels and prose are not evidence. A required dimension mismatch makes the row ineligible. A neutral dimension contributes zero.

Primary-family base weights are:

| Primary family | Base weight |
| --- | ---: |
| Global survival and society | 40 |
| Regional and biome | 42 |
| Government archetype | 42 |
| Successor country memory | 48 |
| Character and leader | 44 |
| Diplomacy, trade, war, and settlement | 40 |
| Cause memory and altered fiction | 38 |
| Recovery and late world order | 42 |

An authored adjustment may range from minus 10 through plus 10. A value outside that band invalidates the candidate.

All normalized values are clamped to 0 through 100. Fixed-point contributions accumulate without intermediate rounding. The scheduler rounds once after all additions and deductions.

```text
score = primary_family_base
      + authored_adjustment
      + phase_suitability
      + 0.30 * severity
      + 0.25 * unresolved_mechanic_pressure
      + 0.10 * player_relevance
      + 0.10 * state_value
      + region_match
      + government_match
      + country_memory_match
      + cause_memory_match
      + winter_match
      + crisis_resource_match
      + character_match
      + bilateral_opportunity
      + route_match
      + previous_choice_match
      + recent_war_or_crisis
      + arc_capacity_adjustment
      - family_fatigue
      - repeated_state_penalty
      - repeatable_event_penalty
```

| Exact input | Contribution |
| --- | ---: |
| Preferred phase | 30 |
| Supported secondary phase | 15 |
| Exact region match | 20 |
| Exact government-archetype match | 20 |
| Exact country-memory match | 20 |
| Exact terminal-cause memory match | 15 |
| Exact Air Winter condition match | 15 |
| Exact survival-resource crisis match | 25 |
| Required recurring character available | 15 |
| Valid bilateral partner and relationship opportunity | 15 |
| Exact focus, decision, or government route match | 15 |
| Supporting previous choice memory | 12 |
| Recent war or crisis explicitly relevant | 20 |

Resource pressure is twice the distance below 50, with both the distance and result clamped to their accepted bounds. Air Winter phases 0 through 6 normalize to 0, 15, 30, 45, 65, 85, and 100. Severity and state value use event-owned formulas tied to exact receipts. Player relevance is 100 for a human recipient, 50 when an AI recipient's exact bilateral partner is human, 25 when the candidate names a current human-owned war or mission target, and 0 otherwise. Only the highest applicable player-relevance value is used.

A new major arc receives a capacity adjustment of plus 10 with zero active arcs, zero with one, minus 20 with two, and becomes ineligible with three. An authenticated continuation does not use that adjustment. The final rounded score must be greater than zero. The scheduler has no minimum-score fallback.

## Fatigue, repetition, and caps

Every country stores twenty fatigue entries. Index 0 remains zero. Entries 1 through 19 stay in the 0 through 100 range. Before scoring, each entry loses one point for every elapsed day since the last fatigue update. All entries commit before the update day. Repeating the decay on the same engine day changes nothing.

An issued opening adds 60 fatigue to its cooldown family once and clamps at 100. Results, callbacks, cleanup, cancellation before issue, and failed issue attempts do not add fatigue. The last cooldown family is a hard veto for the next independent opening. If every otherwise valid row belongs to that family, nothing is selected.

Each country stores its two most recent visible state targets and issue days. Repeating a state once within 90 days applies a 35-point penalty. A third visible incident about the same state within 120 days is ineligible. A current capital or active siege may bypass that third-incident veto but retains the penalty.

A completed nonrepeatable event is permanently ineligible for that country. A repeatable event is ineligible for 90 days after its last opening, takes a 50-point penalty through day 365, and has no event-recency penalty later.

| Transaction surface | Cap per country |
| --- | ---: |
| Outstanding ordinary opening | 1 fixed receipt |
| Active major arcs | 3 |
| Delayed and callback rows | 8 |
| Bilateral rows including cleanup-pending rows | 6 |
| Independent arcs for one character or institution | 1 |
| Newly selected envelope per engine date | 1 |

Cleanup-pending and issued tombstones count against their cap until exact release. A delayed or callback reservation must be due from 1 through 730 days after its parent transaction. Longer stories advance through reviewed arc stages and reserve another bounded row only after the earlier stage terminalizes.

## Determinism, relationships, and AI parity

A recurring character or institution reserved by an unresolved arc, delayed row, or bilateral row cannot open another independent arc. A bilateral candidate requires current scheduler and survival rows for both countries, distinct participants, valid gates in both directions, no conflicting issued reciprocal receipt, no opening of the same pair and family in the previous 90 days, and available row capacity on both sides. Exact partner-score ties use the lower frozen partner registry index. Both reciprocal rows commit before either event may issue.

The implemented relationship reservation substrate records this contract in `2026-07-26_relationship_candidate_reservation_addendum.md`. The candidate eligibility trigger remains fail-closed unless both rows carry the exact reciprocal candidate id, transaction key, event-token pair, visible cost, bilateral opportunity, and source-index back-reference. The selected relationship branch calls the existing bilateral reservation API and does not use the ordinary receipt or dispatch path. Current relationship rows retain the no-partner sentinel, so no relationship event is active or release-floor countable.

The implemented major-arc reservation substrate records its top-level payload contract in `2026-07-26_major_arc_candidate_reservation_addendum.md`. Major rows may reserve only through the exact arc identity, parent-ticket, actor-shape, and current-scope proof, then enter the existing capped arc ledger at the opening stage. The Year Zero pilot has a separate major-stage consumer that authenticates its existing human and hidden-AI events, advances the ticket through its authored stages, and releases the row after cleanup. The other major rows still skip ordinary dispatch and remain dormant and outside release-floor credit.

The scheduler selects the higher final score. Exact score ties prefer crisis incidents, then major-arc openings, relationships, routine incidents, and broadcasts. Remaining ties use the lower stable candidate identity, lower stable target identity, then lower bilateral partner registry index. Due results and cleanup never compete with new candidates. Random rolls and MTTH do not resolve ties.

The selected payload freezes generation, registry index, phase, control mode, candidate identity, event tokens, primary family, cooldown family, visible-budget cost, final score, target, partner, parent arc, character, issue day, due day, and every branch token before its pending marker. An exact retry must match that payload.

Human and hidden AI routes use the same eligibility, score, costs, arc and queue reservations, result partitions, fatigue, memory, and cleanup. The frozen control mode does not change if control changes while a transaction is pending. Human-only player relevance is the sole intended scoring difference. Hidden AI receives no reduced cost, guaranteed success, free branch, or invisible reward loop.

Save recovery retries one frozen unissued selection without rescoring. An issued selection remains a blocking tombstone and cannot emit a second command. A stale generation cancels an unissued selection with a typed reason. An issued selection remains owned by its exact event terminalizer.

The numerical scheduler remains dormant until the release gates pass. Both activation flags must remain unset. No unreviewed candidate row, event caller, or suffix from `100` through `126` receives release-floor credit from the numerical substrate.

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
