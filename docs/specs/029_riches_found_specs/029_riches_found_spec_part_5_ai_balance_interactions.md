# Event 029: AI, balance, multiplayer, and system interactions

## AI design purpose

Every ordinary country can receive Riches Found, so the AI must understand the mine as a strategic asset with a local crisis attached.

The AI should not use one ideology-only route table.

It should evaluate the mine's value, the country's capacity, war state, stability, government type, local conditions, foreign access, and active evolution.

The AI must be able to manage the system without a human-only scripted GUI.

All AI actions should call the same cost, trigger, effect, transfer, logging, and cleanup helpers used by player decisions.

## AI state inputs

Important AI inputs include:

- current war state
- enemy proximity to the mine
- state control and core status
- mine operating state
- mine contribution before diminishing returns
- total controlled mine count
- Extraction Pressure
- Mine Development
- Local Order
- Revenue Legitimacy
- hidden concession exposure
- hidden illicit capture
- hidden deep excavation
- active Resource Curse state
- active Gold Disease state
- active supernatural state
- stability
- war support
- political power
- industry
- construction capacity
- manpower
- equipment
- fuel
- trains
- convoys
- supply in the mine state
- supplied divisions in the state and access route
- faction membership
- nearby rivals
- foreign contract offers
- controller dependence on mine receipts
- expected time before loss of control
- expected cost of closure or sealing

The AI should not use an action whose required state, target, route, contract, evolution, equipment, or access no longer exists.

## AI policy profiles

AI policy is a weighted profile, not a permanent route lock.

A country can change policy after war, conquest, corruption exposure, government change, or a severe mine crisis.

### Public Development

This profile favors:

- local claims
- camp administration
- public health
- worker housing
- local labor
- local revenue share
- citizens' dividend
- stabilization fund
- transparent auction
- public contracts
- mine police
- moderate pressure
- repair and controlled closure

It accepts lower immediate output for reliable long-term value.

### State Extraction

This profile favors:

- state reserve
- nationalized operation
- central treasury receipts
- rail and processing development
- state security
- deep mining after reinforcement
- limited foreign technical contracts

It produces strong national value and higher dependence risk.

### Concession Economy

This profile favors:

- private claims
- foreign finance
- limited or exclusive concession
- infrastructure-for-access
- private guards
- rapid development
- contract renewal

It works best for weak or capital-poor states and carries foreign leverage and capture risk.

### Militarized Mine

This profile favors:

- army cordon
- state reserve
- emergency extraction
- strategic stock and shipment control
- strict access
- nationalization without compensation when hostile actors are involved
- denial or evacuation before loss

It is common during war, civil war, occupation, and authoritarian emergency.

### Predatory Extraction

This profile favors:

- maximum pressure
- patronage
- forced or coercive labor where existing systems and public consequences support it
- private or military repression
- secret contracts
- rapid deepening
- continued operation during crisis
- supernatural bargain under extreme conditions

It delivers the strongest short-term reward and the highest failure risk.

The AI should choose this profile only under ideology, desperation, war, personalist rule, low legitimacy, or high-chaos conditions.

## Government and ideology tendencies

### Democratic governments

Stable democracies should favor Public Development.

They should prefer open claims with enforceable rules, public services, local sharing, audits, disclosed contracts, mine police, and moderate extraction.

They can choose a concession when capital is weak or foreign relations are strong.

They should strongly avoid mass violence, secret exclusive contracts, permanent military control, and supernatural bargains unless the country is near defeat or has already collapsed politically.

A low-stability democracy can centralize revenue or tolerate patronage under emergency pressure.

The AI should not assume that democracy guarantees good management.

### Communist governments

Communist governments should favor state reserve, nationalization, worker participation, public development, and limits on foreign ownership.

They can choose worker cooperatives, local committees, and armed workers more often.

They can still produce patronage, coercive labor, military control, and hidden theft through party or security structures.

They should avoid an exclusive foreign concession unless survival depends on it or the partner is politically aligned.

### Fascist governments

Fascist governments should favor state extraction, military control, rapid development, central receipts, and strategic offtake agreements.

They are more willing to use private guards, emergency contracts, violent nationalization, and high pressure.

They should still invest in rail, processing, and safety when the mine has long-term strategic value.

They are more willing to keep the mine open during Gold Disease and to use coercive responses.

### Non-aligned, monarchist, and personalist governments

These governments should vary by state capacity and leader style.

A strong monarchy can create a crown or state monopoly and a stabilization fund.

A personalist regime can route revenue through patronage, elite families, officers, or private concessions.

A weak non-aligned minor can accept foreign infrastructure and security in exchange for access.

The profile should respond to stability, dependence, and foreign protection. Do not treat all non-aligned states the same.

### Colonial or occupation governments

A controller in a non-core or occupied state is more likely to choose direct extraction, military security, concession rule, and shipment protection.

It should recognize that low legitimacy and resistance reduce long-term value.

An AI with adequate time and strategic interest can choose local revenue sharing to improve control.

An occupier expecting to lose the state soon can strip equipment, deny the mine, or evacuate valuable personnel.

It should not receive full normal output from a hostile occupied state.

## Capacity and scale tendencies

### Major power

A major power should usually develop the mine domestically or through a controlled limited concession.

It can afford audits, rail, processing, safety, and nationalization.

It should value strategic denial during war.

It should not accept an exclusive foreign concession without a strong diplomatic or emergency reason.

### Industrial minor

An industrial minor can use state extraction, joint venture, or public development.

It should balance the 1,000 political-power windfall against the risk of overcommitting its small construction base.

### Poor or infrastructure-limited minor

A weak minor should find foreign finance, an infrastructure-for-access agreement, or a slow public route attractive.

It should not start several expensive projects at once.

It should protect the mine from becoming a foreign enclave by valuing disclosure, local sharing, and contract limits when its institutions permit.

### Landlocked controller

A landlocked country should value rail, road, and neighboring transit access.

It should not choose convoy or port actions unless the selected state and route make them valid.

### Island or overseas controller

An overseas mine should value ports, convoys, escort, and foreign naval access.

The AI should account for blockade and convoy shortage.

It should not treat an isolated island as an easy full-output asset.

## War-state behavior

### Peace

The AI should favor development, settlement, governance, and long-term contracts.

It can accept slower projects and lower pressure.

### Limited war away from the mine

The AI can centralize some revenue and accelerate transport while preserving long-term value.

It should not automatically militarize the district when no threat exists.

### Front near the mine

The AI should prioritize Hold the Mine During War, supplied divisions, route defense, evacuation planning, and denial risk.

It can suspend dividends and increase emergency extraction for a defined window.

### Civil war

Each side should value the actual controller contribution and the state's transport route.

The AI should not count the mine for both sides.

It should avoid expensive development when control is uncertain.

### Expected loss

When the mine is likely to fall soon, the AI chooses among:

- reinforce and hold
- evacuate workers and records
- move portable equipment
- destroy or deny key infrastructure
- suspend or close the mine
- negotiate with the likely new controller through an existing concession

Denial should carry real economic, population, legitimacy, and reconstruction consequences.

## AI response to low values

### Low Extraction Pressure

The AI may develop or increase output when development and order are adequate.

It should not waste resources on emergency closure.

### High Extraction Pressure

The AI should compare current contribution against collapse, evolution, and order risk.

Cautious profiles reduce shifts, reinforce shafts, seal deep sections, or close temporarily.

Aggressive profiles maintain or increase pressure during war or dependence.

### Low Mine Development

The AI should select one valid development priority based on geography and commodity profile.

It should not queue rail, housing, processing, drainage, and port projects at once.

### Low Local Order

The AI should choose one primary response that fits legitimacy and capacity:

- civil administration
- mine police
- negotiated truce
- pay protection
- army cordon
- private guards
- temporary closure

It should not keep adding security layers without cleanup.

### Low Revenue Legitimacy

The AI should consider audit, local sharing, dividend, public contract, administration replacement, or repression.

The chosen response should reflect ideology, stability, and dependence.

## AI evolution behavior

### The Resource Curse

A reform-capable AI should attempt a sequence of audit, revenue settlement, transparency, and diversification.

A patronage AI should use mine income to stabilize the regime while accepting corruption.

A private-interest AI can accept The Gilded Sovereignty when government capacity is low and output is high.

The AI should not alternate every month between nationalization and concession.

Use route memory, cooldowns, and contract state.

### Gold Disease

The AI should first reduce movement and determine whether the mine can remain open safely.

High-legitimacy AI should prefer revenue sharing, controlled access, workforce support, and temporary closure.

Military AI should prefer cordon, workforce replacement, clearing, and sealed sections.

An aggressive AI can continue extraction when the country depends on the mine or is losing a war.

Permanent sealing should be rare before lesser containment attempts fail.

### Demons Beneath the Mine

Most AI profiles should initially investigate, reduce pressure, seal dangerous sections, evacuate, or seek assistance.

Scientific, religious, occult, and military responses depend on country context and available helpers.

Bargaining should require high chaos plus desperation, authoritarian or personalist tolerance, mine dependence, or prior supernatural commitment.

A stable democracy at peace should almost never accept The Bottomless Account.

A collapsing authoritarian government at war can accept it.

The AI should understand visible obligations and breach risk.

## AI foreign behavior

### Concession seeker

A foreign actor evaluates:

- mine value
- development opportunity
- route access
- controller weakness
- relations
- faction alignment
- rival involvement
- strategic need
- existing contract portfolio
- mine crisis
- expected security cost

It should prefer a limited concession or infrastructure agreement when relations are good.

It can seek an exclusive concession when the controller is weak, desperate, aligned, or corrupt.

### Sponsor after contract

A sponsor should protect its investment through diplomacy, aid, security, repair, or pressure.

It should not automatically declare war after every contract dispute.

Escalation depends on value, ideology, relations, strategic need, and military balance.

### Rival

A rival can expose corruption, back claimants, sabotage transport, support nationalization, or prepare seizure during war.

It should need access, interest, and risk tolerance.

### Neighbor

A neighbor can provide labor, transit, joint security, smuggling access, or armed pressure.

Border status and mine-state adjacency should matter.

## Required probability audit surfaces

Every complex `ai_will_do`, event option weight, foreign-target weight, evolution MTTH factor, raid target weight, and random incident pool needs the specialized probability audit.

The auditor begins with `hoi4.probability_inspect`.

It then uses:

- `hoi4.probability_evaluate` for named campaign states
- `hoi4.probability_sweep` for value thresholds and rank reversals
- `hoi4.probability_compare` after implementation changes
- `hoi4.probability_simulate` only when uncertain inputs are declared
- `hoi4.probability_render` when a matrix, sensitivity chart, timing view, or comparison makes the result easier to review

Willingness scores are not click probabilities.

The audit must include availability, target validity, cost, cooldown, policy memory, and route state.

## Exact 1,000 political-power windfall

The opening grant remains exactly 1,000 political power.

This is an intentionally extreme immediate reward.

The implementation must not silently lower, split, cap, or replace it.

The balance pass must test:

- whether the current HOI4 political-power storage rules waste part of the grant
- whether AI countries immediately buy laws, advisors, command appointments, decisions, or policies in a destabilizing sequence
- whether a player can bank the grant through another project system before the event
- whether repeatable firing can favor one country several times
- whether multiplayer targeting feels arbitrary or decisive
- whether the event's reduced repeatable weight is enough to prevent frequent repeated windfalls
- whether the grant interacts with country-specific political-power caps or scripted systems

If live or probability evidence shows that 1,000 political power breaks the event system, the implementation agent must report the conflict and request a design change.

It cannot substitute a smaller value without approval.

## Ongoing political-power income

The mine's ticking political-power benefit is separate from the opening grant.

It must be modest enough that one managed mine is valuable without replacing normal political-power generation.

It should respond to development, operating state, legitimacy, extraction policy, and diminishing returns.

High-pressure predatory extraction can raise short-term income.

Corruption, theft, closure, occupation, and crisis reduce effective income.

A country controlling several mines cannot stack uncapped political-power gain.

## Construction and production balance

The mine supports:

- construction speed
- civilian construction capacity or consumer-goods relief
- production-efficiency gain or cap
- military-factory output

The exact mix should preserve the user request without inventing unsupported modifier names.

The first mine should have a noticeable effect.

The aggregate cap should keep several mines below the strength of a complete national economic path or major late-game economic system.

Local development projects can create real state buildings only through bounded missions and one-time project completion.

They must not create repeatable factory or infrastructure farming.

## Diminishing returns design bands

Exact constants belong to implementation, but the intended curve is:

- first controlled mine: full marginal contribution
- second controlled mine: roughly one half to two thirds of the first mine's marginal contribution before quality factors
- third controlled mine: small marginal contribution
- fourth and later mines: minimal aggregate contribution while retaining local strategic and denial value

The total country aggregate has a hard cap.

The curve should be implemented through script constants and one reusable aggregation helper.

The tooltip should explain that additional mines have diminishing national returns.

It should not expose a long mathematical formula.

## Mine quality and reward strength

Every mine receives a quality band during survey.

Quality changes the ceiling, not the opening 1,000 political power.

Suggested bands:

- modest vast deposit
- rich deposit
- exceptional deposit
- extraordinary deposit

The wording should be improved during localisation.

Quality should influence development payoff, foreign interest, and pressure from deep extraction.

The highest quality must remain rare.

A low-quality mine should still justify the event's premise and the persistent state modifier.

## Repeatable-event behavior

Event 029 follows the global repeatable-event weight system.

After firing, its weight cap halves and its weight recovers through the shared monthly rule.

The event should not add its own independent timer or recovery system.

A country that already has a mine remains eligible for another firing when it has another suitable state.

Every valid recipient country receives the same country-selection weight. Existing mine count, country size, ideology, major status, and player control must not bias the recipient roll.

Diminishing returns limit the persistent value of several mines, while the exact 1,000 political-power grant remains a possible repeated windfall because the user specified a completely random recipient.

The selected state must be new.

The same event instance must never create two mines.

## Global mine count and performance

The mine registry should be bounded by actual Event 029 firings.

The event system must not scan every state to find mines during every daily or weekly tick.

Recommended maintenance model:

- register a state when a mine is created
- update that entry through bounded state-control and event actions
- rebuild one controller aggregate when a relevant mine changes
- process incidents through scheduled mine jobs or narrow on-actions
- remove or mark terminal entries after permanent sealing, exhaustion, or destruction

The implementation should inspect existing repository registry patterns before creating a new one.

If a shared persistent-site registry exists, Event 029 should use or extend it through a narrow adapter.

## Exploit prevention

### Discovery farming

The player cannot manually choose the recipient through normal play.

Force trigger remains a testing and settings path under the existing contract.

The same firing grants 1,000 political power once.

Reloading or reopening the report must not repeat it.

### Controller-transfer duplication

The previous controller loses the contribution before the new controller gains it.

The state cannot have two saved current controllers.

Annexation, occupation, civil war, and release must call the same reconciliation helper.

### Closure loops

Temporary closure lowers pressure over time and costs output, worker support, and recovery resources.

Closing and reopening immediately must not erase crisis state.

Reopening needs a cooldown or mission completion.

### Development farming

Every permanent building or infrastructure grant has a one-time project identity.

Canceling, losing, and regaining the state does not reset completed projects.

Destroyed buildings can be repaired, not re-granted as another completion reward.

### Concession farming

A mine can have one exclusive concession.

Limited contracts have bounded slots or types.

Signing, revoking, compensating, and re-signing cannot duplicate infrastructure or one-time finance rewards.

### Audit farming

Audits have cooldowns and state.

A clean audit does not repeatedly grant political power or legitimacy.

A later audit requires a new trigger such as contract renewal, corruption evidence, or controller transfer.

### Nationalization farming

Compensation is paid by the nationalizing controller.

Foreign claims cannot be created repeatedly from the same contract.

A revoked concession cannot be restored without a new negotiation.

### Gold Disease farming

Population loss, purges, closures, and workforce replacement cannot produce a positive net reward loop.

The syndrome cannot be moved intentionally to unrelated states for benefits.

### Supernatural payment farming

The Bottomless Account uses defined payment families with caps, cooldowns, and one-time stages.

Unrelated deaths, genocide, strategic bombing, disease, and military casualties cannot satisfy an obligation.

The system cannot convert arbitrary population loss into output.

## Multiplayer behavior

The selected recipient can be a player or AI country under the ordinary event-target rules.

When the event targets a player, only that player receives the decision category and initial event.

Other players can interact through foreign concessions, neighboring pressure, war, occupation, contract disputes, and control transfer.

The mine state remains a shared world object.

A player who captures it gains the bounded controller system after reconciliation.

A previous player loses the positive contribution.

Foreign contract and controller-transfer popups should avoid sending duplicate choices to every player.

The implementation must follow the project's ghost-copy and multiplayer event pattern.

The exact 1,000 political-power grant should be tested for competitive fairness, but it remains random by design.

## Chaos integration

Ordinary discovery does not need a large chaos increase.

Possible chaos changes include:

- small reduction after a durable public settlement
- small increase after claim war, major raid, or corrupt seizure
- stronger increase after massacre, foreign intervention, catastrophic collapse, or demonic bargain
- evolution-log entry under the shared evolution system

The mine's economic bonuses do not directly add chaos simply because they exist.

The event should not create a hidden passive chaos farm.

## Deaths integration

Use exact state population loss and the shared Deaths system for:

- mine collapse
- fire or settlement disaster when lethal
- raid massacre
- claimant war
- guard mutiny
- military clearing
- forced entombment
- Gold Disease violence
- supernatural disappearance or sacrifice when the route defines real deaths

Use distinct Deaths reason IDs for major Event 029 causes.

Population must be removed exactly once.

Military casualties should be classified correctly when the source is an armed force.

## Condemnation integration

Condemnation applies to publicly known responsibility for:

- forced labor
- mass killing
- abusive private or public security
- military purge
- forced entombment
- destroyed records after atrocities
- blocked inspection
- coverups
- exposed foreign sponsorship of abuses

Ordinary corruption, theft, bad contracts, and low legitimacy do not automatically create atrocity condemnation.

Hidden evidence remains hidden until a report, audit, occupation, witness, or exposure route reveals it.

## Air Cleanliness and contamination

Ordinary mining does not alter global Air Cleanliness by default.

Gold Disease is not biological contamination.

Demons Beneath the Mine is not chemical, biological, nuclear, or atmospheric contamination.

A later accepted collapse or industrial accident can use relevant environmental systems only through a documented adapter.

## Event 013 Natural Disasters

A physical earthquake, landslide, flood, or collapse can interact with Event 029.

Event 029 can call the public `call_natural_disaster` effect only when every required exact-state input and proof is available.

The call should preserve Event 013 ownership of disaster targeting, damage, reports, aftermath, and Deaths registration.

Event 029 should not use Event 013 as a generic mine-collapse button.

An ordinary mine collapse can remain Event 029-owned.

## Event 016 Brilliant Scientist

Event 016 can provide bounded assistance when a valid Event 016 host or institution exists.

Possible support includes:

- advanced survey
- drainage or reinforcement analysis
- Gold Disease behavior study
- secure material handling
- measurement of supernatural anomalies
- sealing advice

The adapter must not:

- create Event 016 project history
- create Kruger ownership
- transform the controller into an Event 016 host
- grant a random advanced technology without an accepted reward route
- advance Strategic Singularity
- create free facilities or units

Scientific assistance changes Event 029 outcomes only.

## Event 018 Resources Found

Event 029 and Event 018 must remain mechanically separate.

Rules:

- a state cannot host both persistent site identities
- Event 029 does not add strategic resources by default
- Event 029 does not call deeper deposits, caves, fossils, Oth-Kesh, or The World Opens Below
- Event 018 does not inherit Event 029 corruption, concession, Gold Disease, or demon state
- shared state selection helpers can be reused only when they preserve both events' exclusions
- event logs and catalog entries keep separate names and descriptions

A cross-event report can acknowledge that governments compare the two kinds of discovery.

It must not merge their mechanics.

## Event 019 Infantry Spawn

Event 029 creates no custom combat unit or unit family.

Mine police, guards, army cordons, worker militias, and foreign security are represented through decisions, unit requirements, temporary modifiers, existing units, or event-owned state effects.

Implementation should not create a new Event 019 provider for these ordinary security roles.

If implementation later adds a real custom combat subunit, the full Event 019 integration obligation applies.

## Black Plague and biological systems

Gold Disease must not register as Black Plague, a bioweapon, an outbreak, or contamination.

No cure, vaccination, disease spread, or bio-stockpile logic is used.

A flavor comparison by frightened characters is possible, but mechanics and Event Details must remain clear enough to prevent player confusion.

## Camps and genocide systems

The event does not create a separate camp system.

If a predatory controller uses forced labor or mass killing through an existing shared atrocity route, Event 029 should call the shared population, evidence, Deaths, and Condemnation helpers.

It should not duplicate those systems inside the mine event.

## World threat

Ordinary Resource Curse, Gold Disease, and contained demons do not create a global world-threat source.

A world-threat source becomes appropriate only if a later branch proves that the supernatural force has escaped the mine and now affects the wider world as an existential threat.

This specification does not require that escalation.

## Event logs and Event Details

The entry event records one normal Event 029 history row with the recipient as actor.

The selected mine state must be available to Event 029 detail and history text through the event's own stored state data.

Controller transfer does not create another Event 029 random-event history row.

It can create a report or consequence entry inside the mine system.

The three registered evolutions record through the shared evolution pipeline.

Event Details needs:

- event premise
- repeatable classification
- current live weight or `N/A`
- fired count
- actor mapping
- evolution previews
- enabled state

It should not expose hidden values, future bargains, or raw modifier lists.

## Save and reload persistence

The following state must survive save and reload:

- mine registry entry
- selected state identity
- commodity profile
- quality
- development
- pressure
- order
- legitimacy
- operating state
- current controller
- original discoverer
- completed projects
- damage
- closure and sealing state
- contracts and foreign actor
- private-security state
- mission state
- evolution records
- Gold Disease condition
- supernatural condition
- late crisis outcome
- contribution-ledger state

The selected human mine target can be rebuilt after reload when the repository pattern treats UI selection as temporary.

Persistent gameplay state must not depend on a stale GUI selection.

## Balance scenario set

The implementation must evaluate at least these scenarios:

1. Stable democracy at peace with one core-state mine
2. Authoritarian major at war with one border-state mine
3. Poor minor with low infrastructure and a foreign concession offer
4. Colonial or occupied mine with low legitimacy and resistance
5. Country controlling three mines under diminishing returns
6. Mine transferred during civil war
7. Resource Curse with successful reform
8. Resource Curse with private enclave outcome
9. Gold Disease contained through closure and revenue settlement
10. Gold Disease met with military clearing
11. Demonic mine permanently sealed after evacuation
12. Demonic mine entering The Bottomless Account
13. Mine lost and regained after heavy damage
14. Event firing twice for the same country in different states
15. Event firing when no valid state exists

The acceptance file defines the expected results.
