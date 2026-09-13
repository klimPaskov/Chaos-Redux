# Event 043: Monsters from the Deep

## Part 6: Decisions, missions, and human counterplay

## Interface choice

Event 043 uses two decision categories.

1. **Monster Dominion**, visible to a human-controlled full monster, Cthulhu's Dominion, or an Abyssal Remnant in its reduced form.
2. **Defend the Littoral**, visible to ordinary countries with a current Event 043 threat, active response project, or direct support role.

Working category names describe the surface. Final localisation remains implementation work.

The event does not add a full scripted GUI. Category pictures, map targets, progress, tooltips, and phased visibility can present the mechanic more clearly.

## Visible-action budget

One category state should normally show three to five primary decisions.

Hard limits:

- no more than six visible primary actions in one phase
- no more than three active missions
- no more than four spendable cost types on one action
- no raw internal variable dumps
- no country list covering all sixteen monsters at once
- no target rows for countries that cannot currently be affected

Targeted decision families should use the selected-target pattern when several monsters or states are available.

## Monster Dominion category

### Header

The header should show:

- Hunger band and exact value
- Sea Bond band and exact value
- apex status
- current original lair or nearest valid lair
- one short current objective
- one warning when Hunger, Sea Bond, support cap, or apex position is critical

The header should not show regional score, pact score, terminal score, reinforcement weights, or every controlled port.

### Category picture

Every full monster uses a creature-specific category picture. It may be static or animated.

The picture communicates:

- current apex identity
- its main maritime environment
- current phase through a small approved variant
- no fake buttons
- no painted meter
- no readable generated text
- no miniature map that pretends to be interactive

The animation package needs a static fallback. A full picture variant per Hunger band is not required.

## Monster action family

### Devour a Conquered Shore

**Purpose:** lower Hunger through a controlled populated coastal state.

**Target:** one controlled legal coastal or near-coastal state with remaining feeding capacity.

**Requirements:**

- Hunger at or above the action's threshold
- state inside current operational range
- no active feeding cooldown
- no completed human evacuation that reduced the valid population below the floor
- no contradictory state protection
- route allows the selected feeding method

**Costs:**

- primary cost is civilian death and local destruction
- optional command pressure or temporary apex commitment can support the action
- political power should not be the main cost

**Effects:**

- exact state population loss
- shared Deaths entry
- Hunger reduction based on actual applied loss
- local devastation
- possible reinforcement receipt
- possible Famine and Migration incident facts
- one state cooldown
- human report and memory

**AI:**

AI uses this action when Starving or Frenzied, or when preparing a major brood action. It avoids feeding a nearly empty original lair unless extinction pressure is severe.

### Raise a Brood from a Port

**Purpose:** consume one reinforcement receipt to create a support formation.

**Target:** one controlled registered lair or eligible port.

**Requirements:**

- unconsumed receipt
- support cap available
- selected family unlocked
- target inside legal range
- Sea Bond above the minimum
- no hostile control in the spawn province

**Costs:**

- one receipt
- Hunger increase
- possible local population loss or port damage for selected families
- one cooldown

**Effects:**

- create one support division from the permitted family
- assign event identity and counter
- register unit in support ledger
- consume receipt
- raise Hunger
- update cap and AI role

**AI:**

AI chooses the family needed for the current front. It should prefer a defender when lairs are threatened, a raider when coastal objectives are open, and a heavy unit only when the cap and Hunger can support it.

### Reinforce the Apex Lair

**Purpose:** improve one registered lair for a bounded period or advance its stage.

**Target:** original lair or another registered lair.

**Requirements:**

- control
- no active human purification
- route permission
- required support presence or port
- one available lair stage

**Costs:**

Up to four relevant types:

- Hunger increase
- temporary tied-down support formation
- captured civilian construction capacity
- feeding reserve or local population sacrifice

**Effects:**

- improve Sea Bond contribution
- improve lair defense
- unlock one support spawn location
- increase target value to human counterplay
- create a visible state modifier

A lair improvement cannot create an invisible permanent fortress. Its stage and countermeasure should be clear.

### Mark a Coastal Capital

**Purpose:** choose one important human coastal capital as a campaign objective.

**Target:** a valid reachable ordinary country capital or high-value coastal state.

**Requirements:**

- target within current legal reach
- no active mark
- no pact conflict
- war or valid war-opening route
- target is not protected by another terminal state

**Costs:**

- Hunger growth while active
- apex or support commitment
- cooldown

**Success:**

- one major feeding receipt
- support receipt
- route progress
- bounded Chaos receipt only when this is a named one-shot event outcome
- possible pact prestige

**Failure:**

- Hunger increase
- Sea Bond pressure
- human confidence
- harder retargeting cooldown

The action should create a timed mission for the monster player, not an instant war-goal purchase.

### Extend the Saltwater Reach

**Purpose:** enact a focus-unlocked operational-range step or creature-specific corridor.

**Target:** current country or a named region.

**Requirements:**

- matching focus complete
- enough legal coastal control
- no current Severed Sea Bond
- required lair count
- no incompatible crisis

**Costs:**

- sustained Hunger pressure
- temporary recovery penalty
- captured construction or support commitment
- time

**Effects:**

- update operational tier
- update core eligibility
- refresh war targets
- reveal new decisions
- change AI front limits

This action should appear only when the focus route requires a player commitment after the focus. Some trees may apply the step directly through the focus when no decision adds gameplay.

### Contract the Realm

**Purpose:** abandon illegal or disconnected territory to preserve the apex.

**Target:** one out-of-range pocket or selected low-value state group.

**Requirements:**

- low Sea Bond, over-cap support, or disconnected territory
- valid human successor or neutral cleanup rule
- no active unit that would become invalid

**Costs:**

- territory
- route prestige
- pact standing
- possible support loss

**Effects:**

- improve Sea Bond
- reduce Hunger growth
- reduce over-cap pressure
- create human liberation or occupation consequences

This action gives a real retreat option. It cannot be used to farm peace or erase an enemy encirclement without cost.

### Sacrifice a Support Formation

**Purpose:** resolve a Frenzied Hunger or over-cap crisis.

**Target:** one eligible support unit or support family group.

**Requirements:**

- crisis active
- at least one non-apex support formation
- no unit currently selected as an essential mission anchor

**Costs:**

- permanent destruction of the support formation
- morale and route consequence

**Effects:**

- Hunger reduction
- cap relief
- possible temporary Sea Bond stability
- no civilian deaths

The action must never target the apex.

## Creature-specific monster actions

Each tree should unlock one or two actions from this family.

| Monster | Signature action direction |
| --- | --- |
| Kraken | Crush a selected port and open a short assault window |
| Scylla | Mark retreating formations for a pursuit burst |
| Leviathan | Enter a slow armored assault stance |
| Cetus | Call a mixed support wake after a successful amphibious objective |
| Hafgufa | Prepare a bait zone around one lair |
| Jormungandr | Poison a connected coastal front for a bounded period |
| Iku-Turso | Conceal one Baltic operation in fog |
| Umibozu | Silence one enemy port through a storm mission |
| Akkorokamui | Begin a regeneration window while Sea Bond remains high |
| Jiaolong | Flood one approved river corridor |
| Bakunawa | Begin one timed eclipse offensive |
| Timingila | Consume a stored feeding reserve for one heavy wave |
| Te Wheke | Pursue a marked enemy across one approved island chain |
| Lusca | Emerge from one registered blue-hole ambush site |
| Cipactli | Feed through many mouths at high local devastation |
| Ipupiara | Terrorize one prepared coastal state before an assault |

Every action needs a public duration, target, cooldown, effect direction, failure, AI rule, and cleanup.

## Pact actions

Pact actions appear only after the matching focus route.

### Sound the Deep

Send a proposal to one valid full monster country.

Requirements include:

- compatible route
- no current war with an unresolvable war leader
- no active betrayal cooldown
- geographic or enemy basis
- target has a pact route or emergency survival basis
- target apex lives

The proposal creates an event for a human target or an AI evaluation for an AI target.

### Hold the Truce

A timed mission tests whether the two countries can avoid border conflict and contribute to one shared objective.

Success opens a compact. Failure restores hostility or records rivalry.

### Bind the Compact

The compact establishes:

- nonaggression
- border validity
- shared target rules
- limited reinforcement support
- pact contribution actions
- betrayal consequences

It does not merge countries.

### Form the Abyssal Faction

A compact group can create the event-owned faction after membership and campaign conditions pass.

The faction needs:

- at least three living apex members
- one shared enemy or regional objective
- no member on a locked solitary route
- sufficient pact stage
- no active world-end conflict that forbids it

### Betray the Compact

A full monster can betray before Cthulhu unification.

The action should:

- require a strategic target
- create Hunger and Sea Bond consequences
- clear support access
- start one rivalry war
- record permanent betrayal memory
- affect future pact AI
- block immediate rejoining

Betrayal should be dangerous. It cannot be a free surprise attack button.

## Human response category

### Visibility

**Defend the Littoral** appears when the country:

- borders a full monster
- owns a state threatened by a monster within legal reach
- is at war with a monster
- has received refugees from a threatened state
- is supporting an allied response
- has an active Event 043 mission
- participates in Ocean Watch
- is fighting Cthulhu's Dominion

The category hides after every relevant threat, mission, cooldown, and aftermath item has ended.

### Header

The human header should show:

- nearest or selected monster
- selected threatened coast
- qualitative apex status
- qualitative Sea Bond band when observed
- current mission
- one concise recommendation

It should not show all sixteen monsters at once.

### Target selection

The category uses a selected-monster or selected-threatened-region pattern.

The player can cycle or select one valid active threat. Only decisions for that threat appear. A close action clears the selection.

AI sees all valid actions without using the human selector.

## Human action family

### Evacuate a Threatened Littoral State

**Purpose:** move civilians before feeding or conquest.

**Target:** one owned threatened coastal state.

**Requirements:**

- valid Migration route
- reception or internal destination
- time before the threat is fully occupying the state
- no duplicate cohort transaction

**Costs:**

Up to four:

- convoys or trains
- fuel
- civilian factory burden
- temporary stability or local production loss

**Mission:** protect the route for a defined duration.

**Success:**

- survivor movement through Migration
- lower feeding capacity
- reduced future deaths
- temporary disruption in origin and destination
- Event 043 evacuation receipt

**Failure:**

- trapped population
- route damage
- possible displacement deaths through Migration
- no double debit

### Fortify a Named Port

**Purpose:** create a real defensive objective around one port.

**Target:** a named owned port threatened by one monster.

**Requirements:**

- port inside the monster's current reach
- supplied divisions in the state
- route and construction capacity

**Costs:**

- support equipment
- civilian factory burden
- command power within the project limit
- time

**Mission:**

Hold the port and keep it supplied for `90-150` days, scaled by urgency.

**Success:**

- temporary anti-monster defense
- Sea Bond pressure on the attacker
- one observation or kill-zone receipt
- no permanent free fort stack

**Failure:**

- port damage
- monster feeding or lair opportunity
- local evacuation pressure

### Establish Monster-Hunter Command

**Purpose:** unlock national coordination against Event 043.

**Requirements:**

- direct war or high threat
- enough army experience or command capacity
- one military organization or decision basis

**Costs:**

- army experience
- command power
- support equipment
- temporary officer commitment

**Effects:**

- unlock kill-zone missions
- improve intelligence on Sea Bond
- enable specialist formation or existing-unit modifier
- create AI response strategy
- open allied support actions

This should become a staged idea, not a permanent stack of many tiny spirits.

### Lure an Apex into a Kill Zone

**Purpose:** create a timed, risky attempt to draw the unique apex away from its strongest coast.

**Target:** selected living apex and one approved near-coastal state.

**Requirements:**

- Monster-Hunter Command
- observed apex
- supplied divisions in named states
- one valid retreat or bait path
- target inside the creature's legal range
- no duplicate kill-zone mission

**Costs:**

- infantry or support equipment
- fuel
- command power
- tied-down divisions as a requirement, not a spendable fifth cost

**Success conditions:**

- apex enters the marked state
- human forces hold required adjacent positions
- Sea Bond is below the mission threshold
- mission timer remains active

**Success effects:**

- temporary apex combat penalty
- stronger Sea Bond disruption
- kill achievement tracking
- no automatic apex destruction

**Failure effects:**

- monster breakthrough
- local casualties or equipment loss
- Hunger relief for the monster when it wins the bait battle
- mission cooldown

### Sever the Sea Bond

**Purpose:** attack the lair and port network supporting one apex.

**Target:** selected monster and one named lair or port group.

**Requirements:**

- control or blockade objective
- observed lair
- war with target
- enough naval, air, or land access for the chosen variant

**Variants:**

- land seizure
- naval blockade
- air and port suppression
- resistance-supported sabotage

Each variant uses a distinct real requirement and cost. The player should see only valid variants.

**Success:**

- temporary Sea Bond disruption
- lair stage damage
- support-spawn block
- observation of apex vulnerability

**Failure:**

- lost equipment, ships, aircraft, or resistance network
- monster pact prestige
- lair reinforcement

### Coordinate Ocean Watch

**Purpose:** create a multinational warning and information network.

**Requirements:**

- at least one active Event 043 monster
- valid diplomatic partners
- no special-country exclusion
- selected contribution type

**Costs:**

- convoys or aircraft allocation
- civilian factory burden
- political power only as a minor diplomatic component
- intelligence exposure

**Effects:**

- improves emergence observation
- identifies lairs
- helps allies select threats
- reduces surprise from creature-specific powers
- unlocks limited support missions

Ocean Watch is not a faction and should not replace existing alliances.

### Send Specialist Support

**Purpose:** support another ordinary country fighting a monster.

**Target:** valid ally or threatened partner.

**Costs:**

- equipment
- convoys
- fuel
- temporary domestic readiness

**Effects:**

- recipient mission progress
- Monster-Hunter Command growth
- opinion and cooperation
- no free division transfer unless the route explicitly creates one

### Purify a Retaken Lair

**Purpose:** clear the persistent lair record after retaking a state.

**Requirements:**

- own and control state
- no full monster control
- hold for confirmation period
- enough supplied divisions or specialist support

**Costs:**

- support equipment
- fuel
- civilian factory burden
- time

**Success:**

- clear lair
- reduce former monster Sea Bond
- unlock reconstruction
- preserve death and feeding history

This action cannot restore killed population.

## Human missions

The category can activate up to three missions from the highest-priority set.

### Hold the Port

- duration: `90-150` days
- objective: hold and supply one named port
- success: defense receipt and Sea Bond pressure
- failure: lair opportunity and evacuation pressure

### Keep the Coastal Capital Supplied

- duration: `120-180` days
- objective: preserve land or sea supply to one named capital
- success: deny a major monster objective
- failure: feeding reserve and local crisis

### Hunt the Apex

- duration: `120-240` days
- objective: damage or isolate the selected apex while holding the kill-zone states
- success: vulnerability window and achievement receipt
- failure: higher monster Hunger relief and local casualties

### Break the Lair Network

- duration: `150-240` days
- objective: retake or blockade a named set of ports
- success: major Sea Bond disruption
- failure: improved lair stage and support wave

### Guard the Evacuation Route

- duration: `90-140` days
- objective: hold named rail, port, or destination states
- success: survivor transfer
- failure: trapped population or route deaths through Migration

### Survive the Eclipse or Storm

- duration: creature-specific
- objective: hold key states until Bakunawa or Umibozu power expires
- success: route resilience and observation
- failure: port shutdown or island loss

## Mission priority

Human mission selection should consider:

- apex distance to player territory
- current war
- coastal capital threat
- port importance
- population at risk
- allied request
- existing mission count
- creature power active
- Sea Bond vulnerability
- player and AI capacity
- terminal status

A player should not receive three minor missions while its capital is under direct apex attack.

## Costs and tooltips

Every action uses compact icon-first cost text.

Non-cost requirements appear in concise tooltips with exact states, unit counts, ports, routes, or values.

No action may hide a fifth spendable cost inside an effect tooltip.

Costs should be dynamic where relevant:

- larger evacuations use more transport
- longer coastlines need more support equipment
- distant allies need more convoys and fuel
- stronger lairs need longer purification
- high observation lowers kill-zone risk
- repeat actions can escalate in cost

Command power remains conservative and never exceeds the project limit.

## AI equivalence

Every action available to AI countries needs a direct AI evaluation path.

AI should:

- select the nearest urgent monster
- defend coastal capitals and high-value ports
- evacuate high-risk population when transport exists
- avoid impossible kill zones
- refuse support when its own coast is collapsing
- coordinate with faction allies
- exploit low Sea Bond
- stop spending on a threat that has died
- clean stale target selections
- change strategy under Cthulhu

Monster AI should:

- feed before Frenzied when a valid state exists
- avoid empty-state feeding
- raise support units needed for current fronts
- protect the apex
- contract illegal pockets
- propose pacts only to valid targets
- betray only when strategic benefit outweighs pact loss
- use signature powers against meaningful targets
- preserve one receipt for emergency defense when threatened

Every weighted surface requires probability audit before and after tuning.

## Cleanup

Decision cleanup occurs when:

- target monster dies
- selected apex transfers to Cthulhu
- war ends
- state changes owner
- mission target becomes invalid
- pact changes relations
- event threat ends
- scenario setup clears
- player switches country
- remnant replaces full monster
- terminal state replaces all old tags

Cleanup must clear target flags, selected IDs, event targets, missions, cooldown displays, and temporary modifiers. Permanent death, feeding, and achievement receipts remain.

## End of Part 6

Part 7 defines evolutions, monster pacts, terminal readiness paths, Cthulhu unification, and terminal defeat.
