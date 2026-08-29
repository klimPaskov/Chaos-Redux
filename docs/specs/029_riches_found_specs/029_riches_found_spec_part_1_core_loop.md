# Event 029: Riches Found

## Catalog identity

- Event ID: `29`
- Event name: Riches Found
- Type: Minor Repeatable
- Current status evidence: `To Be Reworked` in the user task and `Unavailable` in the supplied CSV export
- Status target after implementation: Use the authoritative workbook's verified post-implementation status
- Cluster: None
- Recommended baseline chaos level: Calm World, subject to confirmation against the authoritative workbook and current event registration

## Event promise

A completely random ordinary country discovers a source of exceptional mineral wealth in one suitable state.

The discovery delivers an immediate national windfall of exactly 1,000 political power.

The selected state becomes a persistent source of revenue and industrial leverage, and its value follows whoever controls it.

The discovery starts an ordinary mining rush with workers, prospectors, transport firms, merchants, engineers, guards, criminals, officials, foreign concession seekers, and neighboring states competing around one location.

The player manages how quickly the mine is developed, who receives the revenue, who controls access, how the site is protected, and how much political authority is surrendered to private or foreign interests.

The mine can become a durable development engine, a captured patronage system, an armed enclave, an obsessive killing ground, or a place where impossible bargains are made.

## Separation from Event 018 Resources Found

Riches Found must not operate as another strategic-resource discovery roll.

Event 018 owns deposits that add or expand map resources, deeper physical discoveries, caves, fossils, Oth-Kesh, and its underground terminal route.

Event 029 owns windfall governance and control of one exceptionally valuable mining site.

The ordinary reward comes from a persistent state modifier and a controller-wide aggregate, not from adding steel, oil, aluminium, chromium, tungsten, or rubber to the map.

Commodity identity is narrative and mechanical flavor unless a later accepted spec explicitly adds a separate conversion rule.

A state carrying an Event 018 resource-site marker is not eligible for Event 029.

A state already carrying an Event 029 mine is not eligible for another Event 029 mine.

The supernatural track never reveals Oth-Kesh, never calls the Event 018 cave chain, and never selects The World Opens Below.

## Valid recipient country

The entry event selects one existing country from the ordinary country pool.

A valid recipient must meet all of these conditions:

- It exists and has at least one owned and controlled eligible state.
- It is not classified by `is_special_chaos_country`.
- It is not classified by `is_actual_nonhuman_country`.
- It is not a civil-war shell, scripted system carrier, or temporary country that the repository already excludes from ordinary civilian events.
- It can receive political power and country modifiers normally.
- It has a valid government and capital.

The selection pool should use the normal Event 029 target gate before the event receives live weight.

When no valid country and state pair exists, the event shows `N/A` in Event Details and does not enter selection.

Force-trigger mode may bypass ordinary selection restrictions only through the existing settings contract.

## Suitable state selection

The event selects one state owned and controlled by the recipient.

A suitable state should favor a location that can support a visible rush and a contest over control.

Positive selection factors include:

- meaningful population
- at least one building slot or realistic room for development
- land connection to the recipient or a usable port connection
- existing infrastructure, rail, or a plausible route that can be improved
- meaningful local industry or an existing settlement
- adjacency to other land states
- a non-core or colonial location when the event needs a higher-risk variant
- strategic proximity to a border when armed competition is plausible

Negative selection factors include:

- wasteland or permanently ruined state
- empty or nearly empty island with no usable port
- impassable terrain
- state already reserved by another persistent site system
- active catastrophic disaster that makes the ordinary discovery impossible
- current occupation without a stable controller when the initial event cannot resolve the recipient cleanly
- state whose ownership or control is in the middle of a scripted transfer transaction

The selection should remain random after weighting.

It should not always choose the capital, richest state, or highest-population state.

The chosen state is saved as the mine's stable identity and added to a bounded Event 029 mine registry.

## Commodity profiles

The discovery assigns one narrative profile.

The profile changes report imagery, incident weights, foreign interest, development needs, and collapse risks.

It does not create a strategic resource deposit by default.

### Alluvial gold field

This profile produces the fastest early rush, the largest transient camp, the weakest initial claim system, and the strongest early crime pressure.

Development leans toward roads, water control, washing works, depots, policing, and settlement administration.

The field is easier to enter and harder to regulate.

### Deep gold reef

This profile has slower opening output and stronger long-term value.

Development leans toward shafts, drainage, reinforcement, power, rail, processing works, and specialist labor.

Collapse and deep-excavation pressure rise faster after aggressive development.

### Gemstone field

This profile produces easier concealment, smuggling, substitution, theft, and private handling.

Revenue legitimacy is harder to preserve because small high-value material can leave the official ledger unnoticed.

Foreign buyers, criminal networks, and private guards receive higher incident weight.

### Platinum or precious-metal seam

This profile produces stronger strategic industrial interest, more state involvement, and greater foreign pressure for long-term supply contracts.

Development is capital intensive.

A weak country is more likely to accept foreign finance, while a major country is more likely to nationalize or militarize the site.

## Immediate discovery package

The receiving country gains exactly 1,000 political power once.

The selected state receives the persistent Riches Found state identity.

The mine begins at low development, manageable local order, uncertain revenue legitimacy, and low to moderate extraction pressure.

Starting values vary through dynamic factors:

- Low stability raises disorder and lowers legitimacy.
- Corruption or atrocity conditions raise hidden capture pressure.
- A core state begins with higher legitimacy than an occupied or colonial state.
- Existing infrastructure raises initial development.
- War, nearby fronts, resistance, and low supply raise order pressure.
- High chaos raises the chance that the opening rush starts with fraud, violence, or unusual incidents.
- Strong institutions, democratic competition, and public-service capacity improve the opening governance state.
- Existing private-security or concession systems can shift the opening toward company control.

The initial report must show a real social and economic change in the selected state.

It should focus on workers arriving, prices changing, claims being staked, transport routes filling, and officials losing control of access.

It should not read as a reward list.

## Persistent state identity

The mine belongs to the state, not to the country that first discovered it.

The state carries a permanent mine identity until one of these terminal local outcomes occurs:

- the deposit is permanently exhausted through a defined failure or exploitation route
- the mine is permanently sealed
- a catastrophic collapse destroys the workings beyond recovery
- a supernatural closure consumes or removes the site
- a later accepted event explicitly converts the site through a safe adapter

Temporary closure, occupation, sabotage, damaged infrastructure, loss of the state, or a government change do not erase the identity.

The original discovering country keeps the one-time political-power windfall.

It loses ongoing controller benefits when it no longer controls the state.

The new controller gains the ongoing benefits only after the controller refresh resolves once.

The transfer must never duplicate the contribution for both countries.

## Controller transfer contract

Control changes are a normal part of the event.

The mine must follow the current controller during war, occupation, civil war, peace settlement, annexation, liberation, and release.

The controller refresh performs these conceptual steps:

1. Remove the mine's contribution from the previous controller aggregate.
2. Save the new controller.
3. Recalculate control quality, core status, compliance, resistance, supply, local order, revenue legitimacy, security policy, and current mine condition.
4. Add the mine's bounded contribution to the new controller aggregate.
5. Replace controller-specific decisions and missions.
6. Preserve state development, physical damage, closure state, extraction pressure, incidents, and evolution history.
7. Clear invalid foreign-concession targets and re-evaluate surviving contracts.
8. Create a transfer report only when the change is strategically meaningful or the mine has an active crisis.

This refresh should use a narrow ownership or control hook, an event-driven state registry refresh, or another bounded repository pattern.

It must not rely on a whole-world daily, weekly, or monthly scan.

If the installed engine and repository do not expose a proven narrow controller-change route, implementation must stop and report that blocker. Do not add an unauthorized global scan.

## Visible mechanic values

The decision category presents four values because each one has a separate cause, consequence, threshold, and player response.

### Extraction Pressure

Extraction Pressure is the primary value.

Range: 0 to 100.

It represents how hard the site is being pushed, how much untouched material is being opened, how many workers and guards are exposed, and how quickly later dangers accumulate.

It rises through deep mining, output drives, military requisition, exclusive concessions, weak oversight, wartime desperation, and predatory policies.

It falls through closure, reduced shifts, reinforcement, revenue settlement, safety investment, sealed sections, and controlled recovery.

High pressure raises current rewards and incident frequency.

It also raises collapse risk, corruption, Gold Disease severity, deep-excavation pressure, and supernatural escalation.

The player must see the next important pressure threshold and the broad consequence attached to it.

### Mine Development

Mine Development is a supporting value.

Range: 0 to 100.

It represents roads, rail, drainage, power, processing works, shafts, housing, administration, and extraction capacity.

It rises through construction missions, investment, foreign capital, engineering, local revenue, and successful repairs.

It falls through raids, sabotage, fighting, neglect, closure decay, and collapse.

Development increases the mine's possible contribution and improves recovery from ordinary incidents.

High development also makes the site more attractive to foreign actors and raises the cost of abandoning it.

### Local Order

Local Order is a supporting value.

Range: 0 to 100.

It represents enforceable claims, safe transport, accepted policing, worker discipline, guard reliability, and the state's ability to keep armed groups from controlling the site.

It rises through fair claim resolution, mine police, pay protection, supplied garrisons, community agreements, and trusted administration.

It falls through claim jumping, wage theft, private-army rivalry, raids, smuggling, military requisition, labor conflict, Gold Disease, and occupation.

Low order raises theft, killing, sabotage, foreign interference, and temporary shutdown risk.

Order created through terror is less durable than order created through legitimacy and administration.

### Revenue Legitimacy

Revenue Legitimacy is a supporting value.

Range: 0 to 100.

It represents whether workers, local residents, government bodies, and outside observers accept who receives the mine's income and how contracts were awarded.

It rises through dividends, local development, transparent auctions, public ledgers, community agreements, and credible audits.

It falls through secret concessions, patronage, forced displacement, unpaid labor, private guard abuses, central seizure, colonial extraction, hidden owners, and exposed theft.

High legitimacy reduces corruption, resistance, foreign propaganda opportunities, and security costs.

Low legitimacy accelerates the Resource Curse and makes violent control less effective.

## Hidden state

The event may use hidden values for implementation and surprise.

Suggested hidden values include:

- concession exposure
- illicit capture
- deep excavation
- private-security autonomy
- foreign claim pressure
- Gold Disease pressure
- supernatural pressure
- sealed-depth integrity

The player should not see a raw ledger of these values.

Their visible effects appear through report incidents, stage labels, decision availability, modifier changes, and concise tooltips.

Basic cause and effect must still remain clear.

## State modifier lifecycle

The state uses one persistent mine ledger and exactly one active state-modifier presentation.

Prefer one dynamic modifier with a stable public identity and a stage line in its tooltip. If the engine requires separate names or icons for the visible stages, replace mutually exclusive modifier variants through one lifecycle helper. Never stack the stage variants.

Working lifecycle states:

- Newly Discovered Riches
- Expanding Mine District
- Established Riches District
- Contested Mine District
- Closed Mine District
- Ruined Workings
- Permanently Sealed Workings
- Corrupted Mine District
- Gold-Sick Mine District
- Opened Depths

These are working labels for planning and should not be pasted as final localisation without a writing pass.

The modifier's effects derive from development, pressure, order, legitimacy, closure, damage, control status, and active evolution.

The state modifier should not become a stack of separate permanent modifiers.

## Controller aggregate lifecycle

The controller receives one aggregate country modifier or staged idea that summarizes all controlled Event 029 mines.

Working lifecycle:

- Windfall Receipts
- Managed Mineral Revenue
- Resource-Dependent Treasury
- Captured Revenue State
- Corrupted Mine Administration
- Gold-Sick Administration
- Infernal Accounts

The aggregate is rebuilt from controlled mine contributions.

The controller should not receive one permanent national spirit for every mine.

The tooltip lists the number of controlled mines, the selected mine's current state, the total bounded contribution, and the major reasons a mine is underperforming.

## Controller benefits

The user-supplied benefit set is preserved:

- ticking political power
- nationwide construction speed
- production efficiency
- military factory output
- civilian factory benefit

The civilian-factory benefit must use a real supported HOI4 effect.

The preferred design is a bounded combination of consumer-goods relief, civilian construction capacity, and construction speed.

It must not claim to provide a literal civilian factory output modifier if the engine has no such modifier.

The contribution of one mine is based on:

`mine quality x development x operating state x extraction policy x control quality x local order x revenue legitimacy x evolution factors`

The design should use script constants and reusable calculation helpers.

The exact tuning belongs to implementation and probability review.

## Diminishing returns and country cap

Event 029 is repeatable, so multiple mines can exist in one country and across the world.

The first controlled mine contributes at full bounded value.

The second controlled mine contributes a lower marginal share.

The third and later mines contribute sharply reduced marginal shares.

The total country-wide benefit has a hard cap.

Development, legitimacy, and order still matter for every mine because they affect local incidents, state value, and which mine is most productive.

Diminishing returns apply to the nationwide aggregate.

They do not erase local state development or physical mine value.

The cap prevents a country that captures several mines from obtaining unlimited political power, construction, and factory output.

The implementation must expose the cap and marginal-contribution rule in tooltips without showing a complicated formula.

## Mine operating states

A mine can be in one of these broad operating states:

- Open and expanding
- Open and regulated
- Open under concession
- Open under military control
- Open under predatory extraction
- Contested
- Temporarily closed
- Quarantined
- Partially sealed
- Permanently sealed
- Collapsed
- Exhausted

Only open states provide the normal positive controller contribution.

Contested, quarantined, and partially sealed states provide reduced or conditional value.

Temporarily closed mines preserve physical development but provide no ordinary output.

Permanently sealed, collapsed, and exhausted mines leave a historical state identity and aftermath effects without ongoing positive output.

## Presentation choice

The event uses one ordinary decision category with a static category picture.

The category picture establishes the mine's atmosphere through a documentary-style scene of a crowded mine entrance, railhead, pay wagons, workers, guards, and rough construction.

It must not contain fake controls, meters, labels, or generated text.

The normal decision list carries the gameplay.

The category header shows:

- selected mine state
- current controller
- operating state
- Extraction Pressure
- Mine Development
- Local Order
- Revenue Legitimacy
- one concise line explaining the next important risk or objective

A country controlling one mine sees that mine directly.

A country controlling several mines uses a selected-mine flow that shows one mine's actions at a time.

AI evaluates all valid mines without using the human selection flow.

The presentation should normally expose three to five primary actions and one to three active missions in the current phase.

Obsolete actions disappear when the phase, controller, contract, crisis, or operating state changes.

## Player experience arc

The first decision is about access and claims.

The second set is about whether the rush becomes a settlement, a state project, or a private enclave.

The middle game is about transport, revenue, contracts, labor, and protection.

The later ordinary game is about keeping the site productive without allowing violence, corruption, or foreign control to make the mine stronger than the government.

At high chaos, the same choices acquire new costs.

Extraction can still deliver major rewards, but pressure becomes a direct invitation to obsession and supernatural bargaining.

The event remains useful when managed well.

It should not punish the player simply for receiving the discovery.

Failure follows visible choices, neglected pressure, weak control, war, conquest, and bad crisis management.
