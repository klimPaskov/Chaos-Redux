# Event 018 Resources Found, Part 1 Core Design

All names in this file are working labels only. They are not final localisation. Final event titles, options, decision names, focus names, country names, super-event titles, quotes, cultural remarks, and spreadsheet text must be written during implementation from the direction in this package.

## Core event identity

Event 018 begins as a small economic windfall. A state that looked ordinary becomes valuable because survey crews, miners, oil teams, local officials, or prospectors find a deposit far larger than expected. The baseline should feel simple and readable in play: a random valid state gains around 100 production of a random resource, the owning country receives a discovery popup, and a decision category opens for exploitation and trade.

The deeper identity is the resource curse. A harmless boom can become a diplomatic prize, a smuggling zone, a militarized concession, a dangerous excavation, and eventually an opening to something below the earth. The player should be able to treat the find as a normal economic opportunity and never see the deeper branch if they manage extraction conservatively or close the site. The hidden danger should come from repeated deep exploitation, high chaos, larger evolved openings, and refusal to stop after the evidence turns physical.

The event stays useful as a repeatable minor event even after the monster branch exists. Most firings should remain normal deposits. The dangerous cave route should attach to one tracked primary site at a time unless a later implementation deliberately supports multiple active deep sites. This keeps the ordinary economic effect useful and prevents the high-chaos branch from creating unmanageable duplicate crisis actors.

## Player experience

The first experience should be rewarding. The player sees that a state has received a major resource deposit. The popup should communicate a public discovery and the first decisions should help the player exploit the deposit, improve trade, and stabilize the region. The state should feel worth protecting. The owner should want to build infrastructure, negotiate trade, invite foreign capital, nationalize the field, or place security around the site.

The second experience is diplomatic pressure. Other countries notice the field because the resource is scarce, because they need imports, because the state is near a border, because the owner is weak, or because a rival has claims. The player should gain economic opportunities through trade and concessions, but those choices should raise foreign interest and make the state more politically sensitive.

The third experience is the hidden cost of overexploitation. Extraction depth, worker risk, and public fear grow when the owner keeps pushing the site. Early signs should be ambiguous and local. Workers become exhausted, crews report corroded tools and strange air, mine animals avoid shafts, and settlement life becomes distorted by the boom. The event should not announce that monsters exist before the public stage. The player should infer that the field is becoming wrong because the state gains more resources at a cost, population starts ticking down, safety decisions become expensive, and unusual incidents repeat.

The fourth experience is crisis management. In Evolution III the danger becomes public. The site can still be closed, which removes the event-added resources and prevents the final cave monster country. The price is losing the boom and facing economic anger. Keeping the site open preserves the resources, but public attacks, evacuation, worker deaths, and cave hunts become a recurring state crisis.

The final experience is a hostile nonhuman country. If the player or AI pushes the site to the breaking point, the Cave Host appears from the excavated state. It is slow, heavily armored, and aggressive. It does not use manpower or equipment. It grows from captured resources. It is not a normal country with normal production logic. It is a living consequence of the deposit.

## Repeatable event model

The event remains classified as Minor Repeatable.

Each ordinary firing creates one resource field instance:

| Field concept | Meaning |
| --- | --- |
| Discovery state | The selected valid state that receives the resource deposit. |
| Discovery owner | The country that owns the state at the moment of discovery. |
| Resource type | One random vanilla strategic resource type selected by equal or implementation-verified weighted chance. |
| Deposit size | Around 100 for baseline, dynamically larger for evolved pre-fire openings. |
| Field status | Ordinary, politicized, deepened, sickened, public danger, sealed, exhausted, or breached. |
| Primary deep site | The one active field that can progress into the cave monster branch. |

Ordinary fields can coexist. The state receives resources and may hold local modifiers, trade interest, and concession flags. Only one field should become the primary deep site at a time unless the implementation explicitly builds a multi-site system. If a new field is found while a primary deep site already exists, it may remain ordinary or politicized. It should not start a second independent Cave Host chain.

When a state changes owner, the field follows the state. The new owner inherits the active field decisions, any visible problems, foreign-interest history, and deep-site risk. This is important for border wars, conquests, civil wars, and the Cave Host emergence. The event should not tie the site permanently to the original owner if the map changes.

## Valid state selection

The implementation should build a valid state pool from land states with an owner and controller that can use ordinary resources. It should avoid nonhuman chaos countries, states owned by terminal world-end actors, sea or impassable special states, and states where adding resources would create an engine problem. It should prefer states that are not already event-locked by another terminal system.

The pool should not overfit to existing industrial states. The premise is that a forgotten or ordinary place suddenly matters. Weighting can prefer states with low or moderate existing resources, some population, and enough infrastructure or terrain plausibility to support survey activity. Remote states are valid and can create a stronger infrastructure gameplay loop.

The resource type should be fully random at baseline. The spec intentionally allows rare absurdity, such as a small rural state suddenly gaining a large rubber field. If implementation uses a geography-sensitive subweight, it must still preserve the event fantasy that any resource can appear in unlikely places. The ordinary option text and event detail direction should frame the discovery as surprising rather than as a normal geological survey result.

## Resource addition model

The baseline deposit should add around 100 production of one random resource. This number is deliberately large enough to affect trade. It should not be a tiny modifier. The implementation can tune by state size, chaos tier, repeat count, and resource scarcity, but the ordinary player-facing result should feel like a major discovery.

Recommended dynamic deposit model:

| Situation | Deposit direction |
| --- | --- |
| Baseline ordinary firing | Around 100 of one random resource. |
| Poor infrastructure state | Same deposit, but exploitation decisions need infrastructure, rail, or civilian construction before full trade benefits appear. |
| Resource-scarce world | Slightly higher diplomatic interest and trade value, not necessarily more resource production. |
| High-chaos baseline firing | Deposit stays readable, but hidden deep-site chance and foreign interest rise. |
| Evolution I pre-fire opening | Several large resource rolls in the same state, with repeated type rolls allowed. |
| Evolution II pre-fire opening | Larger ordinary discovery plus early unsafe-extraction state flags. |
| Evolution III pre-fire opening | Very large deposit of every resource in the same state, with the deeper branch starting gradually if this is the first time the event appears. |
| Cave Host emergence | The origin state transfers to Cave Host and its event-added resource total becomes the starting army capacity reference. |

If a repeated random roll selects the same resource during evolved openings, it stacks. This is intentional. It can create a state with an absurd amount of one resource and shift trade behaviour.

## Resource field values

Each active field should use a compact set of values. These values are design names and can become variables, scripted localisation, or GUI values during implementation.

| Value | Visibility | Role |
| --- | --- | --- |
| Field richness | Visible | The total economic value created by event-added resources in the state. |
| Extraction pressure | Visible after the category opens | How aggressively the owner is expanding the site. Drives output, incidents, worker risk, and monster risk. |
| Survey confidence | Visible | How well the owner understands the deposit. Higher confidence improves trade deals and reduces surprise failures. |
| Worker safety | Visible | Reduces population loss, sickness events, and hunt casualties. |
| Foreign interest | Visible | Tracks diplomatic attention, trade offers, concession pressure, smuggling, and border tension. |
| Local dependence | Visible | Tracks how much the state economy depends on the site. High dependence makes closure harder. |
| Public panic | Hidden until incidents become public, then visible | Tracks fear, evacuation pressure, and city flight after Evolution III. |
| Below pressure | Hidden until Evolution II, then partially visible through symptoms | Tracks the hidden cave danger. It rises with deep extraction and feeds the monster branch. |

The owner should see enough to make sensible choices. Hidden danger should not be a pure surprise with no feedback. Before Evolution II, the player sees ordinary economic and diplomatic pressure. During Evolution II, the player sees sickness and unsafe excavation. During Evolution III, the player sees public panic and attacks. By then, keeping the site open is an informed risk.

## Baseline event flow

The baseline chain starts with one popup to the owner and then opens a decision category tied to the state.

Working event flow labels:

| Working label | Role |
| --- | --- |
| Discovery popup | Owner learns that a state has gained a major resource deposit. |
| State boom note | Optional follow-up that frames the state economy around the discovery. |
| Foreign interest note | Triggered if nearby countries or major importers notice the deposit. |
| Concession offer | A foreign country asks for trade access, investment rights, or survey rights. |
| Smuggling incident | Appears if foreign interest is high and owner security is weak. |
| Border tension incident | Appears if the state borders a rival, claimant, or country with resource shortage. |
| Expansion report | Appears after exploitation decisions add more resource or increase field richness. |
| Closure report | Appears if the owner closes the site and loses the event-added resources. |

The baseline should not flood the player with popups. Most follow-ups should be decision results, log entries, or short report events. Popups should appear when the state changes strategic meaning, diplomacy escalates, the field is closed, or a strange stage begins.

## Baseline owner choices

The first popup should give the owner clear choices. The exact option text is implementation-owned. The direction should be:

| Option role | Meaning | Tone direction |
| --- | --- | --- |
| Public economic celebration | Accept the find as a national opportunity and open the decision category. | Confident and practical, with room for mild resource-boom pride. |
| State-led survey | Start with higher survey confidence and lower foreign influence. | Technocratic and cautious. |
| Invite foreign interest | Start with faster economic benefit and higher foreign interest. | Opportunistic and trade-focused. |
| Quiet security review | Start with higher worker safety and lower foreign interest, but slower exploitation. | Serious and controlled. |

If the implementation only uses one baseline option, the event should still open the category and apply the resource deposit in the immediate hidden effect so the option does not duplicate the resource grant.

## Decision category role

The owner decision category should represent a living field management surface, not a store. The player should use it to choose how the field grows, who participates, how safe the work is, how public the benefits are, and whether the state becomes a diplomatic flashpoint.

The category should show:

- selected state name
- resource type or mixed resource summary
- field richness
- extraction pressure
- worker safety
- foreign interest
- local dependence
- public panic when public danger exists
- closure state
- active mission count if missions are running

The category should hide obsolete actions. Early ordinary fields should not show monster hunts. Public attack stages should not show only basic survey decisions. Closed fields should remove exploitation decisions and leave a short aftermath or reopening block only if the design deliberately allows a dangerous reopening.

## Economy loop

The ordinary economy loop has four paths:

1. Survey and stabilize the field.
2. Expand extraction for more resource output and industry effects.
3. Convert the find into trade and diplomacy.
4. Protect the state from theft, pressure, and overdependence.

The owner should not be able to click every action freely. Important decisions need costs and cooldowns based on state infrastructure, owner industry, resource value, foreign interest, and worker safety. Repeated expansion should become more expensive and risky. Strong countries can exploit faster, but their large extraction capacity should also drive below pressure faster if they ignore safety.

Economic benefits should be meaningful. The state may gain temporary local construction speed, infrastructure repair speed, building slots, civilian factory construction speed, trade opinion, or off-map civilian factory investment from concessions. The core benefit remains the large resource production.

## Diplomacy loop

The discovery should affect other countries.

Foreign countries can react because:

- they import the resource type
- they have a deficit of that resource
- they border the discovery state
- they have claims on the state
- they are at war and need the resource
- they are a faction leader trying to secure supply
- they are a rival or hostile ideology
- they are a major power with resource-hungry industry

Foreign reaction should not always be hostile. Some countries offer trade recognition, investment, infrastructure aid, or military survey missions. Others sponsor smuggling, threaten concessions, or start a border crisis.

The owner can use diplomacy to profit, but every concession increases foreign interest. Foreign interest is not automatically bad. It brings investment and opinion, but it makes the state less purely domestic and increases the chance of disputes.

## Border crisis loop

A border crisis can happen when the discovery state is near an eligible rival or claimant. It should not trigger from every border. It should require a meaningful combination of high field richness, foreign interest, neighbour resource need, poor relations, claims, rival ideology, existing border tension, war pressure, or high chaos.

The border crisis should begin with diplomatic pressure. A border war should be a later step if the crisis escalates. If the owner loses the border war, the state transfers to the challenger and the field follows the state. The new owner inherits the economic value and the hidden danger. This is important because an aggressive country can win the deposit and then pay the price for overexploitation.

## Closing the site

The owner can close the site. Closing is the safe hard stop before the final breach. It removes all event-added resources from the state, clears most extraction decisions, lowers below pressure, and prevents the cave monster chain from completing at that site. It should create immediate pain through local dependence, foreign anger, industrial disappointment, or stability loss. Those costs should be manageable and should be lower than letting the public crisis spiral.

Closing can be framed differently by stage:

| Stage | Closure direction |
| --- | --- |
| Ordinary boom | Economic disappointment, local anger, lost trade opportunity. |
| Politicized field | Foreign pressure, concession disputes, smuggler backlash. |
| Sickness stage | Safety inquiry, worker relief, compensation, lost resource output. |
| Public attack stage | Emergency sealing, evacuation, costly demolition, public trauma. |

Closure should not be reversible by a cheap button. A later reopening can exist as a rare high-risk decision only if the implementation wants a deliberate player trap. The default design is that closure ends the dangerous branch for that field.

## Event details and spreadsheet direction

The Event Details window and spreadsheet details should describe the premise, not mechanical effects. The direction should focus on surprising resource discovery, the boom economy, foreign attention, and the possibility that overexploitation changes the state. It should not list the exact resource amount, exact modifiers, hidden values, or cave monster outcome. The evolution detail fields can reveal more as each evolution is implemented, but early details should not spoil the final country.

The cluster detail should place Event 018 in the economy positive cluster as a medium severity member. The detail should describe an economic windfall that can become politically dangerous if pushed too far.

## System connections

Event 018 should connect to these Chaos Redux systems:

| System | Connection |
| --- | --- |
| Random event system | Event remains Minor Repeatable. |
| Event log | Every discovery records state, owner, resource type, and field status. Evolutions record actor and stage. |
| Evolution system | Evolutions I through IV change active site behaviour and pre-fire openings. |
| Chaos Meter | Ordinary discovery can add a small amount of chaos only when diplomacy or violence follows. Later public death and world-end stages add more. |
| Deaths system | Evolution II and III worker loss and monster attacks reduce real state population through the shared deaths system. |
| World threat framework | The Cave Host and world-end branch should register as a world threat source. |
| Event clusters | The event belongs to economy positive and can become a bridge to anomalies at high chaos. |
| Decisions and missions | The field category manages exploitation, trade, safety, crisis, closure, hunts, and evacuation. |
| Super-events | Cave Host reveal, world-end, and costly defeat aftermath deserve super-event treatment. |
| Assets | The event needs report images, decision icons, idea icons, Cave Host assets, super-event images, and animated UI states. |
