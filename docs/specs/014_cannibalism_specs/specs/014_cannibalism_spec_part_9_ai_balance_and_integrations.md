# Event 014 Cannibalism, Part 9: AI, Balance, and System Integrations

## AI design goal

Every important actor must understand the event as a strategic system. AI should not click whichever decision is available, choose a route through flat focus weights, or ignore terminal anchors.

AI behavior depends on:

- war state
- supply
- casualties
- stability
- ideology
- manpower and equipment
- naval access
- local state control
- Field Hunger
- Command Integrity
- Cult Cohesion
- Network Reach
- Larder
- Frenzy
- Network Alignment
- player proximity
- world threat
- Hannibal reveal
- Wendigo existence
- world-end risk

## Ordinary-country AI profiles

### Liberal and democratic governments

Default behavior:

- open emergency response
- protect witnesses and prisoners
- restore supply
- public court-martial with evidence
- request international aid
- avoid terror exploitation

Escalation behavior:

- form joint suppression operations
- support liberation of communes
- target transformation anchors

Failure risk:

- may delay decisive military action if evidence remains uncertain

### Conservative authoritarian governments

Default behavior:

- quiet investigation
- officer replacement
- targeted military police
- concealment when public panic would destabilize the regime

Escalation behavior:

- hard purge with mapped targets
- blockade and prison control

Failure risk:

- destroys evidence and drives cells underground

### Fascist or extreme militarist governments

Default behavior:

- discipline crackdown
- high willingness to conceal
- possible terror exploitation under military pressure

Escalation behavior:

- prison and occupation use
- aggressive collective punishment

Failure risk:

- creates organized cult cadres and warlord officers

The AI should exploit only when defeat risk, ideology, and expected short-term military value outweigh the modeled future danger.

### Communist one-party governments

Default behavior:

- ration and logistics campaigns
- political-officer investigation
- purge of organizers
- controlled public explanation

Failure risk:

- prison and deportation networks become Evolution II nodes if secrecy and coercion are high

### Resource-poor minor countries

Default behavior:

- ask for aid
- evacuate isolated units
- use amnesty and rehabilitation
- prioritize one critical state

Failure risk:

- cannot sustain multiple active missions
- vulnerable to foreign seeding and warlord conquest

### Colonies, subjects, and occupied governments

Behavior:

- request overlord relief
- protect transfer and convoy routes
- react strongly to abandoned garrisons
- can become independent commune locations when overlord support fails

The overlord must not absorb all agency. The affected country or controller gets its own containment requirements.

## Foreign AI reactions

### Allies

- offer equipment, convoys, trains, and military police support
- share intelligence
- screen returning volunteers
- avoid transferring prisoners into infected routes

### Rivals

Possible actions:

- propaganda exposure
- border screening
- opportunistic attack
- covert support to a commune when cynical and high-chaos

Ordinary AI should rarely support cannibal actors directly. Such support belongs to extreme chaos, desperation, or deliberate proxy policy and carries major consequences.

### Major powers

- prioritize network hubs near strategic theaters
- create naval blockades against Island Hosts
- support locally cured countries
- form temporary anti-cannibal coordination when world threat is active
- attack Wendigo anchors before ordinary secondary fronts

## Warlord AI archetypes

### Island Reaver AI

- protects port and Larder
- raids convoys
- chooses nearby islands and weak coasts
- invests in naval access before distant conquest
- aligns with the network under blockade pressure

### Siege Butcher AI

- fortifies city and feeding districts
- attacks relief routes
- uses night sorties
- avoids leaving the capital without a secure corridor

### March Predator AI

- targets depots, rail hubs, and weak fronts
- keeps Frenzy high
- abandons exhausted states
- avoids long sieges without Larder

### Hoarder personality

- saves Larder
- avoids expensive recruitment
- resists tribute
- likely to manipulate network alignment

### Feast Captain personality

- spends Larder on units and raids
- keeps Frenzy high
- aligns when it improves offensive tempo

### Charismatic Initiator personality

- seeds cells
- recruits followers
- supports Evolution I and II content

### Suspicious Tyrant personality

- purges captains
- personal tyranny route
- likely to resist Hannibal unless weak

### Network Disciple personality

- high alignment
- coordinated offensives
- early submission

### Defiant Mouth personality

- anti-absorption route
- executes couriers
- seeks ordinary-country aid only when facing Hannibal

## Hannibal AI

### Unification priorities

1. preserve and strengthen the host
2. absorb aligned warlords
3. isolate resistant warlords
4. centralize Larder routes
5. integrate origin specialist units
6. attack coalition hubs
7. protect network capitals and ports

### Expansion target scoring

Positive factors:

- high population
- weak supply
- existing cells
- prisons and ports
- low stability
- neighboring territory
- strategic rail and naval routes
- coalition leadership

Negative factors:

- wasteland
- zombie or actual-nonhuman territory that yields no usable Larder
- severe chemical or biological contamination
- impossible naval reach
- overextended fronts before mature logistics

### Decision behavior

- spends Larder on units only when there is equipment and territory to sustain them
- uses cells before major invasion
- preserves powerful warlords as commanders when loyalty is adequate
- purges dangerous rivals when central authority can survive the rebellion
- enters ordinary terminal route only after strategic conditions

### Player-adjacent behavior

Hannibal can prioritize a strong player who blocks network routes, but should not ignore every other front to suicide into the player. Threat and path scoring remain strategic.

## Wendigo Hannibal AI

Before terminal lock:

- protects anchors
- accelerates transformation when safe
- trains Wendigo units
- attacks cold and high-population routes
- avoids losing all anchors for a temporary tactical gain

After lock:

- complete world conquest
- no peace normalization
- prioritize remaining major population centers and coalition capitals
- use strongest available units and global war tools

## Route validity

AI must never choose:

- Evolution I route when Evolution I is disabled
- network route when Evolution II is disabled
- Hannibal route when Evolution III is disabled
- Wendigo route without a valid existing Wendigo country
- island route without port or naval access
- a focus that requires a dead target
- a decision against an invalid state or annexed country
- world-end progression below chaos 1000
- terminal progression when another world-end exists

## Balance philosophy

### Early ordinary crisis

The baseline should be dangerous but fair.

- serious stability and manpower pressure
- concrete supply and unit costs
- several viable containment philosophies
- enough time to react when the player acts promptly
- mission failure creates escalation, not instant unavoidable collapse

### Evolution I

The system becomes harder because ideology survives improved supply.

- suppression requires intelligence and legitimacy
- exploitation creates strong short-term power
- cell survival becomes the main risk

### Evolution II

The system becomes regional and military.

- ordinary countries need joint action, naval operations, and territorial liberation
- warlord countries are dangerous at birth
- network spread remains route-based and counterable

### Evolution III

The system becomes a major chaos-country war.

- Hannibal has strong unification advantages
- the world has a final pre-terminal counterplay window
- completed routes become deliberately overpowered

### Terminal routes

Balance no longer means parity with ordinary countries. It means the player and AI had credible earlier opportunities to stop the route.

## Effect-strength bands

Exact numbers belong to implementation tuning. The design target uses outcome bands.

### Significant ordinary action

A successful major containment decision should move a visible value enough to change the next choice. It should not produce a one or two percent effect that the player cannot notice.

### Major focus reward

A branch anchor should unlock units, decisions, state changes, leaders, map effects, or a substantial mechanic transformation.

### Warlord starting package

A new country should threaten its origin state immediately while remaining vulnerable to coordinated counterattack.

### Mature Hannibal package

A completed nonterminal Hannibal route should defeat a conventionally stronger country through combined military, cell, and population mechanics.

### Terminal ordinary route

The country should be capable of global conquest without normal supply and reinforcement limits dominating play.

### Terminal Wendigo route

The country should be effectively impossible to defeat after lock.

## Population-consumption balance

Population consumption must be powerful and finite.

Rules:

- remove real state population
- log civilian deaths through the Deaths system when enabled
- do not create population from nothing
- do not count the same deaths twice
- reduce future Larder yield as a state empties
- contaminated or wasteland states yield little or nothing
- liberated states stop continuing loss but do not restore dead population
- recruitment from consumption has caps and equipment requirements

### Consumption stages

#### Hunting ground

- limited disappearances
- local fear
- small Larder
- recoverable with rapid liberation

#### Feeding state

- strong population loss
- recruitment and Larder
- major resistance and economic collapse

#### Silent Larder

- severe depopulation
- heavy building and infrastructure damage
- high short-term output and low future value
- long recovery after liberation

The state remains reclaimable. Event 14 should not copy Event 10 Death's instant island wasteland behavior.

## Deaths system integration

- civilian population consumption logs as civilian deaths
- consumed or murdered military personnel log as military deaths where scope exists
- Deaths system toggle controls shared logging and presentation according to existing rules
- gameplay population loss and Larder accounting must remain coherent when the display system is disabled
- total consumed population supports reveal, achievements, AI, and world-end thresholds

## Chaos Meter integration

Chaos rises through:

- first public incident
- cross-border spread
- commune and warlord creation
- major population-consumption milestones
- Hannibal reveal
- terminal progression

Chaos can fall through:

- clean local containment
- network node destruction
- global victory
- reconstruction milestones

The event should not create chaos every day from passive existence. Use milestone and scaled consequence changes.

## World-threat integration

Event 14 should add a dedicated source to the shared `world_in_threat` framework when the crisis becomes existential.

Suggested activation:

- several cannibal-controlled states
- more than one warlord country
- Hannibal unification
- active Wendigo Hannibal

Suggested deactivation:

- no viable military or network threat remains

Do not create a parallel one-off cooperation flag.

## Event 10 Death interaction

- Death wastelands yield no Larder
- cannibal states remain reclaimable and do not automatically become Event 10 wastelands
- population consumption is gradual and actor-driven
- Death and cannibal actors can fight over islands
- no direct merge or shared leader

## Event 2 Zombie and Wendigo interaction

- zombie-controlled population is not usable Larder unless existing zombie mechanics explicitly allow it
- actual-nonhuman zombies are excluded from baseline infection
- contamination and destroyed population reduce Larder value
- the Wendigo crossover uses the existing Wendigo country only at Hannibal unification

## Event 7 Fury and general war interaction

- additional wars and casualties can improve Event 14 eligibility
- Fury countries can become targets only if they remain ordinary human countries and meet shared classifications
- Event 14 does not join the Random War or Fury cluster
- cannibal expansion uses its own state and country system

## Famine, migration, locust, plague, and disaster interactions

Actual shortages and isolation can raise Field Hunger and make containment logistics harder.
A disaster family appearing elsewhere, or a disaster warning without local consequences, supplies no shortage evidence.
Famine alone creates no ritual cell or cult.

### Current shortage inputs

The implemented classifier is `cannibalism_country_has_external_hunger_pressure` with its state and severe variants in `common/scripted_triggers/014_cannibalism_triggers.txt`.
It reads the Event 013 disaster flags (`natural_disaster_famine_pressure`, `natural_disaster_supply_collapse`, `natural_disaster_disease_pressure` and the aftermath flags), the Soviet camp famine pressure (`genocide_soviet_famine_pressure_site`, `camp_rework_soviet_famine_pressure`, `sov_famine_pressure_state`, the owner's `famine_pressure` and `sov_famine_crisis_active`), biological contamination, and the locust ingress flags, which no current system sets.
Under shortage an active host gains `cannibalism_integration.weekly_shortage_hunger` (4) Field Hunger per pulse and a further `weekly_severe_shortage_hunger` (3) under severe shortage, its primary-theater logistics objective must hold `logistics_shortage_add_days` (14) longer, and first-host and theater selection add `host_shortage_score` (25) and `state_shortage_score` (16).
The classifier does not read the shared famine system's state stage (`famine_food_stage`, constants `famine_food_stage.*`).
A famine committed by the famine and migration system, including the famine the Hunger Lines scenario commits on Event 014 node states, therefore adds no Field Hunger today.
Proposal P-014-A in the package README closes this gap without a new value or a second relief payment.

### Ownership boundary with the famine and migration system

The famine and migration system (`docs/systems/famine_system.md`, `docs/systems/migration_system.md`, package `docs/specs/famine_and_migration_system_specs/`) owns food stages, food reserves, relief, refugee cohorts and their deaths.
Event 014 owns cells, nodes, Field Hunger, consumption and the Larder.
Event 014 countries are special Chaos countries, so `humanitarian_country_is_valid` fails for them and a state they own or control leaves both humanitarian mechanics; consumption there is recorded only through the Event 014 Deaths transaction.
Since the 10 October 2026 famine and migration rework, a capture by any Event 014 country at war with the owner sends front flight from the owner's neighbouring states through `humanitarian_handle_special_front_capture` (`humanitarian_capture_pressure.special_front_fraction`, 0.02, or `nonhuman_front_fraction`, 0.04, for transformed Wendigo Hannibal).
Event 014 adds no refugee request of its own, and its survivor spread route (`cannibalism_spread_route.survivor`) still picks a neighbouring state independently of those cohorts; proposal P-014-B links the two.

When an Event 014 relief action reaches a state with active Event 013 aftermath, the existing shared-relief bridge credits that state's current rescue, stabilization, or reconstruction phase.
The Event 014 action owns its payment and containment result, and Event 013 owns recovery completion, later disaster losses, and its history.
Medical protection additionally requires that state's active disaster-disease pressure.
The relief can remove the matching hunger, supply, or disease pressure without finishing every recovery phase, repairing every damaged building, erasing accrued deaths, or curing an established ritual cell or network node.
A supply restoration therefore changes the next containment choice while investigation and cell suppression can remain necessary.

One completed shipment or medical action receives one bridge application to its actual destination, including when both systems acknowledge it.
A different independently paid delivery can still help through the existing action limits.
A closed aftermath card receives no delayed credit, and loss of access leaves the existing relief action's own failure or cancellation outcome authoritative.
Without Event 013 aftermath, ordinary Event 014 relief retains its containment result.
AI should judge relief against the local shortage and its remaining containment work, with the same destination, affordability, and completion checks as a human.

The implemented bridge is `cannibalism_apply_shared_relief_to_current_state`, called once by `cannibalism_complete_logistics_mission` at the primary theater state.
It credits the current Event 013 phase score (`shared_relief_score`, 2), clears that state's disaster famine and supply-collapse flags, lowers a Soviet camp-famine owner's `famine_pressure` by `shared_relief_famine_reduction` (12), and marks the state as relieved for `shared_relief_days` (90).
It does not deliver food to the shared famine system: food relief in a state with an active `famine_food_stage` belongs to the famine decisions (Release Food Stores, Import Food, Escort Relief, Airlift Relief), which own their payment and delivery.

### Hunger Lines scenario link

On a successful `SCN-010` launch the triggerable-scenario dispatcher calls the famine-owned `famine_apply_hunger_lines_scenario_pressure` after `trigger_cannibalism_scenario` reports success.
That hook reads `global.cannibalism_node_states`, the `cannibalism_active_node` state flag and `global.cannibalism_scenario_last_intensity`, seizes the food stores of each valid node state and commits acute shortage at Low and famine at Medium and above.
Event 014 must keep those three identifiers stable; it never writes famine stages itself.
Part 11 records the scenario side of this contract.

## Camps and genocide-system interaction

The exploitation route can connect to prison, detention, evidence, condemnation, and Deaths systems.

Rules:

- do not treat camps as automatic cannibal nodes
- only active Event 14 policy and cell conditions create the connection
- foreign discovery of feeding programs can increase condemnation and evidence pressure
- ordinary containment protects prisoners and removes the connection

Current source: `cannibalism_expose_detention_exploitation_in_current_country` raises evidence, disqualifies the clean route and sets `cannibalism_feeding_program_exposed` and the global `cannibalism_feeding_program_exposed_abroad`, but no rule reads those two flags and Event 014 calls no Condemnation source.
The only shared Condemnation now attached to Event 014 countries comes from Event 031's cannibal clash (see Event 031 below).
Proposal P-014-C turns the exposure into one real Condemnation source.

## Event 031 Random Terror interaction

Event 031 owns an implemented rivalry with Event 014 countries.
Its incident draw includes a cannibal clash only when a terror state borders a state controlled by an Event 014 country (`is_cannibalism_country`), and `random_terror_resolve_cannibal_clash` applies the clash deaths and building damage there and adds public major atrocity Condemnation to that cannibal controller through `random_terror_add_cannibal_clash_condemnation`.
Event 031 actors and Event 014 countries both count as special Chaos countries; neither event recruits from or merges with the other.
Event 014 keeps `is_cannibalism_country` stable for this consumer.

## Chemical and biological warfare interaction

- contamination lowers usable population and Larder yield
- chemical and biological attacks can kill cells and civilians but create severe condemnation and state damage
- cannibal countries can exploit chaos but cannot eat contamination as a free resource
- gas or outbreak systems should exclude actual nonhuman Wendigo Hannibal where shared triggers require it

## Nuclear and air-cleanliness interaction

- nuclear wasteland and severe contamination reduce or eliminate Larder yield
- cannibal AI should avoid empty irradiated territory unless it provides strategic transit
- world-end branches remain distinct from fallout world-end

## Multiplayer

- Event 14 has one global entry event and shared Network Reach
- each infected country owns its own containment decisions
- player-controlled warlords preserve control during unification
- simultaneous joint missions should not duplicate rewards
- Hannibal host selection must be deterministic and multiplayer-safe
- scenario setup must record selected type and intensity before launch

## Exploit prevention

Check for:

- repeated consumption of one population loss
- free unit loops
- equipment duplication on tag transfer
- repeated warlord absorption rewards
- Larder farming from the same battle
- surrender and re-release loops
- player-control loss during host selection
- decision targets that remain after annexation
- terminal route below chaos threshold
- ordinary countries accessing cannibal recruitment
- Wendigo units available without the crossover

## Accepted scorer and MTTH implementation

The implemented target model uses two reusable country scorers:

- `cannibalism_unified_target_scorer`
- `cannibalism_wendigo_target_scorer`

Targeted decisions use two matching MTTH weights:

- `cannibalism_unified_target_decision_weight`
- `cannibalism_wendigo_target_decision_weight`

Exactly six unified targeted decisions consume the unified weight: foreign army seeding, global campaign preparation, terror ultimata, border incidents, coalition-hub destruction, and enemy-front collapse. Their narrower adjacency, current-enemy, affordability, route, and cooldown gates remain hard conditions.

Hard-invalid candidates are absent rather than weakly scored. The model rejects self, allies and subjects, dead or capitulated countries, Event 014 cannibal countries, actual nonhumans, unusable population, locked targets, and targets without a proved war, adjacency, inherited cell, rail, naval, or post-lock route. Valid factors include population, weak supply, cells, prisons, ports, low stability, adjacency, physical corridors, coalition command, current war, cold-front evidence, contamination, distance, and actor overextension.

### Resolved pre-lock first-band strategy behavior

The pre-lock Wendigo strategy package intentionally uses fixed first assignment. A valid target receives one low, medium, or high package, and later focus calls can add newly valid targets. The effects database exposes `add_ai_strategy` but no corresponding scripted removal effect, so an already recorded pre-lock target is not dynamically removed or re-banded if its score later changes. The transformation lock runs a separate post-lock scorer and applies a separate one-time 1000/2000/3000 escalation package. This is the implemented design contract, not an open finding. Documentation and player-facing text must not describe the pre-lock package as continuously re-scored.

AI Pack training, receipt muster, inherited winter cells, hunt launch, and hunt pressure also preserve the existing 800-Larder countdown floor after payment. Duplicate Pack-contract and pre-lock target-priority writes are guarded.

## Balance validation scenarios

1. Strong major power, short well-supplied war, low event chance.
2. Long overseas war with convoy losses, severe baseline opening.
3. Poor minor country, humane containment through aid and evacuation.
4. Authoritarian country conceals and later faces exposure.
5. Exploitation route wins a battle and creates Evolution I pressure.
6. Two-country spread resolved independently.
7. Island commune blockaded and recovered.
8. Warlord country survives and expands.
9. Several warlords converge, reveal stopped during warning phase.
10. Hannibal unifies and is defeated before terminal lock.
11. Ordinary world-end qualifies only above chaos 1000.
12. Existing Wendigo country triggers alternate merge.
13. Wendigo transformation anchors destroyed before lock.
14. Terminal Wendigo route becomes effectively undefeatable.
15. Event 10 wasteland yields no Larder.
16. Deaths display disabled without breaking population accounting.
