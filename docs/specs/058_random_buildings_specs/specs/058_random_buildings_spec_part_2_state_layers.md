# Event 58: State construction layers

## The construction provider registry

Random Buildings should not own a permanent hardcoded list of every building in Chaos Redux.

The event owns a construction provider registry. Each building owner can register an entry for one or more Event 58 layers. The registry lets future buildings join the event without copying their validation, lifecycle, or initialization into the Event 58 event chain.

A provider entry defines these design facts:

| Field | Purpose |
| --- | --- |
| Stable entry identity | Lets reports, achievements, probability audits, and future migrations refer to the same construction result. |
| Owner system | Names the event or subsystem responsible for the building after placement. |
| Eligible layer | Baseline, Evolution I, Evolution II, Evolution III, or an approved combination. |
| Risk band | Ordinary, strategic, restricted, advanced, rare, extreme, or exceptional. |
| Relative weight | Controls selection only after the entry passes every validity check. |
| Global availability | Handles DLC, mod option, database, feature toggle, and owner-system availability. |
| State validity | Checks geography, ownership, control, special-country treatment, existing structures, and any owner restriction. |
| Capacity validity | Proves another level or instance can be created without exceeding a cap or shared slot rule. |
| Placement operation | Creates the real building, facility, package, or owner-approved construct. |
| Post-placement callback | Registers the result with the owner system and initializes every required ledger, state marker, actor, lifecycle, or UI fact. |
| Responsibility rule | Resolves a country only when the owner system needs one. |
| Uniqueness scope | None, one per state, one per country, one per world, or another owner-defined restriction. |
| Display family | Gives summaries and achievements a stable player-facing category without exposing internal IDs. |
| Cleanup ownership | Confirms which system handles later capture, destruction, shutdown, discovery, removal, or deactivation. |

A malformed entry fails closed. It cannot enter the candidate pool when its owner, placement, capacity, or callback contract is incomplete.

Event 58 never calls private owner effects by guessing their names. The owner registers an approved public adapter or a complete self-contained placement operation.

## What Event 58 bypasses

Random Buildings creates construction without payment, construction time, ordinary country choice, or the normal build queue.

An entry can bypass a country's usual technology or law requirement when the owner explicitly permits an anomalous grant. The event still respects:

- DLC availability
- database availability
- map and province validity
- building maximum levels
- shared state slot rules
- facility exclusivity
- owner-defined uniqueness
- special-country compatibility
- owner lifecycle requirements

A technology requirement remains active when the owner system needs it for safe initialization or later operation.

## Atomic placement rule

A candidate is selected only after it has passed its current validity and capacity checks.

Immediately before mutation, it is checked once more. If it became invalid because an earlier layer changed the state, it is removed from the local candidate set and the state rerolls among the remaining valid entries allowed by the same risk rules.

A successful placement must create the structure and complete its mandatory owner callback as one logical result. The provider must prove every callback precondition before mutation. Its public placement operation returns success only after the building and owner state are complete.

A rejected or failed provider attempt must leave no building level, facility, marker, ledger row, responsibility record, or other partial mutation behind. When the engine cannot roll back a partial result safely, that provider must use a prevalidated effect path that cannot fail after mutation or remain blocked from the registry. The resolver may try another candidate only after the failed attempt proves that the state is unchanged.

The event does not place a decorative building level and leave its normal mechanics unregistered.

## Rarity protection

The event first selects a risk band, then selects a valid entry inside that band.

This two-stage approach prevents a rare structure from becoming common because ordinary candidates are unavailable in one state.

Fallback moves only toward a safer band.

- A restricted baseline roll can fall back to strategic, then ordinary.
- A strategic baseline roll can fall back to ordinary.
- An extreme Evolution I roll can fall back to rare, advanced, then ordinary expansion.
- A rare Evolution I roll can fall back to advanced, then ordinary expansion.
- An empty ordinary band leaves the layer exhausted.

Fallback never moves upward into a rarer band.

Within a selected band, invalid entries have zero weight. Their weight is not redistributed into another risk band.

## Baseline state construction

The baseline is the main event promise. Every state attempts one result from the baseline registry.

The expected worldwide distribution should remain weighted toward useful but less explosive buildings. A single firing already touches the whole map, so factories and highly valuable special structures should not dominate.

### Baseline risk envelope

The exact values require a complete candidate pool and probability audit. The intended envelope is:

| Band | Target share in a representative mixed world | Role |
| --- | --- | --- |
| Ordinary | central target around `97.5%` | common development, storage, air support, detection, and limited industry |
| Strategic | central target around `2.4%` | synthetic industry and owner-approved special infrastructure |
| Restricted | central target around `0.1%`, hard ceiling around `0.25%` | camps and similarly dangerous or politically charged structures |

These are world-level balance targets, not a promise that every state has the same final probability. Geography, capacity, DLC, owner type, and existing development change local candidate sets.

### Ordinary baseline families

| Building family | Baseline role | Weight direction |
| --- | --- | --- |
| Infrastructure | Main common result. It should be favored in states below maximum infrastructure and decline as the state approaches its cap. |
| Air base | Common strategic result. It is valid while another level can exist and can be weighted higher in large, central, populated, or contested states. |
| State anti-air | Common defensive result. It should remain available in ordinary and special-country states when the building itself is valid. |
| Radar | Common but less frequent detection result. It should favor states where the building has room and where its map position gives meaningful coverage. |
| Fuel silo | Common storage result. It provides economic value without adding another factory slot. |
| Civilian factory | Uncommon ordinary result. It requires a valid shared industrial slot and should remain less likely than infrastructure, air, defense, or storage. |
| Military factory | Uncommon ordinary result. It requires a valid shared industrial slot and should not exceed the civilian factory's broad world share by default. |
| Dockyard | Low-frequency ordinary result available only in states with a usable sea coastline and a valid industrial slot. Lake-only and otherwise unusable coasts do not qualify. |

A representative ordinary-band balance should keep civilian factories, military factories, and dockyards together near the lower end of the common distribution. The combined industrial share should normally stay around `10-15%` of successful baseline ordinary results.

Infrastructure, air bases, state anti-air, radar, and fuel silos should form most baseline results.

### Strategic baseline families

The strategic band can contain:

- synthetic refineries
- owner-approved electrical or energy infrastructure that is stronger than a fuel silo but ordinary enough for baseline use
- special logistics, communications, or industrial buildings that an owner explicitly classifies as baseline strategic construction
- future Chaos Redux buildings that are useful, valid at low Chaos, and not rare enough for Evolution I

Synthetic refineries should remain uncommon across the whole world. They must not become the fallback result for states with no industrial slots or no ordinary options.

### Restricted baseline families

The restricted band can contain:

- concentration camps
- future owner-approved coercive, penal, secret, or dangerous state buildings that belong at baseline only as rare outcomes

A concentration camp is eligible only through the camp and repression owner's adapter. That adapter determines whether the new site is dormant, operating, discoverable, attributed, hidden, or otherwise initialized under the normal camp rules.

Event 58 does not count the camp event as fired, unlock unrelated camp decisions, force an extermination stage, create deaths, or expose evidence unless the camp owner says those are normal consequences of that exact placed instance.

The restricted band remains tiny. A state becoming ineligible for every ordinary factory does not make a camp more likely.

## Local context weighting

Local weighting should make results plausible without turning the event into country strategy optimization.

Useful local factors include:

- remaining building levels
- free shared industrial slots
- current infrastructure level
- usable coastline
- urban or victory-point importance
- existing air and radar development
- whether the owner uses normal civilian systems
- whether the state is already saturated with one family
- whether a special owner system marks the state as valid

The event should not inspect a country's focus route, production plan, preferred doctrine, trade shortage, or AI desire to decide what it deserves. The outcome remains random.

Context weighting must never produce these failures:

- a fully developed state receives a building above its cap
- a landlocked state receives a dockyard
- a state with no industrial slot receives a factory
- a nonhuman country receives a civilian-only institution that its provider forbids
- a rare result becomes common because a state has few candidates
- every state in one country receives the same result through a country-level roll

## Baseline examples

These examples describe valid result patterns, not fixed outcomes.

### Low-infrastructure inland state

Infrastructure should be a strong ordinary candidate. Air bases, state anti-air, radar, fuel silos, and factories can remain valid when they have room. Dockyards are absent. A restricted structure can appear only through its own very small band.

### Developed industrial capital

Infrastructure may have no capacity or a much lower weight. Industrial buildings remain candidates only with a free slot. Air, anti-air, radar, and fuel storage remain useful ordinary results. Advanced or exceptional construction does not enter the baseline unless its owner deliberately registered a baseline entry.

### Coastal industrial state

Dockyards join the ordinary pool. The state still rolls only one baseline result. Coastline does not guarantee naval construction.

### State controlled by a special Chaos country

The state stays in the transaction. Civilian-only provider entries can be absent through `uses_normal_civilian_systems` or an owner equivalent. Military, transport, detection, storage, fortification, and owner-approved special structures can still compete.

### Saturated state

Every capped or incompatible entry is removed. If no baseline candidate remains, the state records a baseline exhaustion reason and receives no substitute modifier, building slot, political power, or equipment.

## Evolution I: Expanded State Construction

### Threshold

- Chaos requirement: `200+`

Each state attempts one additional state-level result from the expanded registry after baseline placement.

The expanded pool includes ordinary entries and a controlled set of advanced, rare, and extreme entries. This matters for balance. Evolution I does not turn every state into a nuclear or special-project center.

### Evolution I risk envelope

The exact values require full-pool analysis. The intended envelope is:

| Band | Target share in a representative mixed world | Role |
| --- | --- | --- |
| Ordinary expansion | central target around `94%` | a second valid ordinary or strategic state building |
| Advanced | central target around `5%` | rocket, nuclear, grid, stronghold, and comparable advanced structures |
| Rare | central target around `0.9%`, hard ceiling around `1.5%` | civilian nuclear, heavy-water, gulag, and similarly unusual owner entries |
| Extreme | central target around `0.1%`, hard ceiling around `0.2%` | extermination camps or equally severe and powerful structures |

The expanded layer is noticeable even when most states receive an ordinary second building because it doubles the number of state-level construction attempts.

### Advanced families

The advanced band can include:

- rocket sites
- ordinary nuclear reactors
- stronger electrical-grid buildings
- stronghold-type state buildings
- owner-approved research, communications, logistics, or defense buildings that are too powerful for baseline

Each entry still requires capacity and owner approval. Event 58 can bypass ordinary construction access only when the owner permits it.

### Rare families

The rare band can include:

- civilian nuclear reactors
- heavy-water reactors
- gulag networks
- powerful owner-specific energy, research, industrial, detention, or security buildings

A rare building should retain a low absolute world frequency even if only one rare entry is currently installed.

### Extreme families

The extreme band can include:

- extermination camps
- future buildings with severe humanitarian, strategic, or world-system consequences

Extreme entries require an explicit opt-in from their owner. Their provider must define normal initialization, responsibility, evidence, discovery, harm, shutdown, capture, and cleanup.

Event 58 does not treat an extermination camp as a larger concentration camp and does not infer missing lifecycle behavior.

## Interaction with owner event history

Receiving a special building through Random Buildings does not automatically mark its original event as fired.

The owner can expose a separate fact such as `building instance exists because of Event 58`. This allows its normal systems to react without creating false event history.

The same rule applies to reactors, facilities, strongholds, electrical systems, camps, gulags, and future event-owned buildings.

If an owner wants Event 58 placement to unlock a subset of its public mechanics, it must say so in its provider contract. Event 58 does not unlock the owner's full event chain by default.

## Repeat firing and saturation

On later firings, the state layers can add another level to an existing building when that building has room. They can also select a different family.

The event does not prefer novel building families merely to make reports varied. Randomness and local weights remain authoritative.

An owner can prevent duplicates through its uniqueness scope. A one-per-state civilian reactor cannot receive another instance if the owner says the structure is unique. A multi-level radar or air base can grow normally.

Saturation is a valid long-term outcome. It reduces successful placements and eventually makes the event unavailable only when every active layer is exhausted worldwide.
