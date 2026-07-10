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

### Prison Breaker AI

- targets prisons and rear areas
- uses cells and transfer routes
- manages internal factions
- prefers infiltration over direct major-front assault

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

## Famine, locust, plague, and disaster interactions

Where other events create real shortages or isolation:

- Field Hunger rises
- containment logistics become harder
- relief decisions can solve more than one problem

The events remain separate. A famine does not automatically create a cult.

## Camps and genocide-system interaction

The exploitation route can connect to prison, detention, evidence, condemnation, and Deaths systems.

Rules:

- do not treat camps as automatic cannibal nodes
- only active Event 14 policy and cell conditions create the connection
- foreign discovery of feeding programs can increase condemnation and evidence pressure
- ordinary containment protects prisoners and removes the connection

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
