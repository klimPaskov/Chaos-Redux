# Event 54: Technology Pool and Eligibility Registry

## Eligibility principle

A technology enters an Event 54 draw only when granting it directly is safe for the recipient at that moment.

Safety is stricter than ordinary research availability. Event 54 may ignore year and strategy, but it must preserve mutually exclusive branches, owner-controlled rewards, DLC compatibility, technology-tree integrity, and the lifecycle of other Chaos Redux systems.

Every draw uses the recipient's current state. A technology that is safe for one country may be unsafe for another.

## Ordinary technology pool

The ordinary pool is the default source for the baseline and Evolution I.

A conventional technology is eligible when all of these statements are true:

- the recipient has not researched it
- direct grant is supported by the technology's effects
- the technology is not a doctrine node
- the technology is not a special project or project completion marker
- the technology is not hidden, deprecated, test-only, AI-only, or setup-only
- the technology does not belong to an event or system that reserves it
- the recipient has not chosen an incompatible branch
- the grant does not require a missing owner transaction
- the current DLC and technology graph support the technology
- the technology is not temporarily blocked by a registered safety rule

The ordinary pool can include standard industry, engineering, electronics, infantry, armor, artillery, support, air, naval, rocketry, nuclear, and other conventional research folders when their individual nodes pass the safety review.

A normal technology remains eligible even when it is strategically poor for the recipient. Event 54 does not favor landlocked countries away from naval research, or small countries toward cheap technology.

## Ahead-of-time technology

The event may grant a technology from a future year. No ahead-of-time cap should be added.

A future technology can be selected even when some earlier technologies in its chain are missing. The recipient keeps the granted node and may later research the missing chain normally.

This direct jump is allowed only when the granted node has a self-contained result. A node whose effects depend on a prior scripted setup, a project ledger, a hidden capability marker, a country package, or another owner-controlled state needs a stricter profile.

The implementation audit must distinguish a harmless graph gap from a broken technology state. The visual presence of an unresearched prerequisite is not enough to exclude a node. The exclusion should follow actual engine behavior and owner dependencies.

## Default exclusions

The following technology classes stay outside Event 54 unless a specific owner contract says otherwise:

### Military doctrines

Land, naval, air, and Chaos Warfare doctrine nodes remain excluded from the ordinary pool. Doctrine Research owns sudden doctrine progress and doctrine branches carry extensive exclusivity and mastery rules. This separation preserves the identity of Event 27 and prevents Event 54 from choosing an incompatible doctrine path.

### Special projects

Special project progress, project rewards, facility unlocks, prototype completion markers, and project-only technologies stay excluded. A project owner may expose a final technology through the registered pool only when that grant does not simulate the project, consume its reward, or mark the project complete.

### Event-owned technologies

A technology created as a reward, stage marker, route key, country identity marker, or project result for another event is excluded by default. Its owner must explicitly register it.

### Hidden state technologies

Technologies used only as invisible script state, compatibility markers, tests, startup setup, migration flags, deprecated aliases, or one-time conversion markers stay excluded.

### Country-specific exclusive technologies

A technology that depends on a specific national tree, country package, designer, institution, character, law, or tag remains excluded unless its owner proves a safe recipient rule.

### Incompatible branch nodes

A technology is excluded when the recipient already owns a mutually exclusive sibling or when the grant would open two incompatible branches at once.

## Compatibility families

The technology audit must maintain explicit compatibility families for every mutually exclusive research choice.

At minimum, the review must cover:

- concentrated industry and dispersed industry
- flexible production and streamlined production
- every vanilla branch that uses exclusive prerequisites or path locks
- DLC-specific alternative branches
- Chaos Redux technology families with exclusive routes
- owner-defined incompatibility groups for registered technologies

A country that has already entered one branch may receive later nodes from that branch when safe. It may not receive a node from the opposing branch.

When a country has not entered either branch, one eligible node may be drawn. The grant commits the country to the resulting branch only when the engine treats that node as a real branch choice. Every later draw in the same firing must recheck the new state so the opposite branch leaves the pool immediately.

## Grant profiles

Every eligible technology has one safety profile. These profiles describe behavior, not implementation syntax.

### Direct jump

The technology can be granted by itself even when earlier nodes are missing. Most conventional technologies should use this profile after inspection proves that their effects are self-contained.

### Prerequisites required

The technology is eligible only when the recipient already has every required prerequisite. Use this for nodes whose direct effect is safe but whose meaning or engine behavior depends on an intact chain.

### Grant package

The technology represents one breakthrough but needs a bounded prerequisite or setup package applied with it. The owner must define every extra node or state change. The extras do not consume additional Event 54 slots, because they are required to make one selected result valid.

Grant packages should be rare. They must not become a way for an owner to hide several rewards inside one registry entry.

### Owner callback required

The technology can be granted only after an owner-provided recipient check and must run a narrow post-grant callback. The callback may establish the minimum state needed for the technology to work. It may not fire the owner event, complete its route, consume its normal reward, create a country, start a project, or grant unrelated bonuses.

### Excluded

The technology cannot be granted safely and never enters the pool.

## Registered Chaos technology pool

The registered pool contains individual technologies that another event or system has approved for Event 54.

This pool becomes available through Evolution II and remains available through Evolution III. Baseline and Evolution I use ordinary technologies only.

Registration is explicit and technology-specific. Registering one technology does not expose its whole folder, project, doctrine, or owner event.

Each registered entry must define:

- a stable technology identity
- the owning event or system
- a player-facing technology name source
- the safety profile
- a recipient eligibility rule
- any incompatibility family
- the prerequisite policy
- the narrow grant package or callback, when required
- whether the entry needs a DLC
- whether the entry can be received by special or nonhuman countries
- whether the entry is temporarily disabled
- the owner event state that must remain unchanged
- a test case proving that the owner can still fire normally afterward

The registry should support additions from future systems without requiring Event 54 to copy their full lifecycle logic.

## Owner responsibility

The owner of a registered technology remains responsible for its meaning and safe use.

The owner must ensure that a direct grant does not:

- mark the owner event as fired
- mark a unique project as completed
- consume a one-time reward
- set evolution milestones that did not occur
- create an owning character, laboratory, faction, or country
- bypass a route commitment
- grant equipment, units, facilities, resources, or decisions that are not part of the technology itself
- create a second copy of a unique institution
- make the normal owner path unavailable

The owner may expose a narrow setup callback when the technology would otherwise be inert. That callback must be idempotent and limited to the selected technology's operation.

## Event 54 responsibility

Event 54 owns the recipient transaction, candidate selection, duplicate prevention, compatibility recheck, report list, and grant receipt.

Event 54 must not learn the internal history of every owner system. It asks the owner whether one registered candidate is safe, grants it through the declared profile, then records the result.

A malformed registration fails closed. The candidate leaves the pool for that draw and the country rerolls without losing a grant slot.

## Provider-style registry

The registry should allow each owner system to publish its own candidates through a stable provider identity.

This keeps ownership clear:

- Event 54 owns the registry and draw contract
- each owner publishes only its approved candidates
- owner checks stay with the owner
- Event 54 receives a bounded list of safe candidate identities
- the grant receipt records both the candidate and provider

A large owner family must not register every hidden stage marker or minor upgrade. Only player-meaningful technologies that can function outside the normal owner route belong in the pool.

The registry needs a review whenever an owner adds, removes, renames, replaces, or changes a registered technology.

## Selection weight

Every eligible technology has equal selection weight by default.

The event does not use year, category, research cost, current strategy, country size, technology level, or owner importance as weight factors. The surprise should come from the actual eligible pool.

A custom provider must not raise the weight of its own technologies. If later content causes registered technologies to overwhelm the ordinary pool, the correct response is to review which technologies deserve registration. Hidden rarity weights would make the event harder to understand and audit.

## Duplicate and family protection

A candidate leaves the recipient's temporary pool as soon as it is selected.

After every grant, the remaining pool is rebuilt or revalidated. This catches:

- new branch commitments
- prerequisite changes
- owner callback state changes
- technologies granted as part of a package
- technologies made redundant by the selected node
- DLC or country-state changes during the transaction

A technology added as part of a grant package must also leave the pool and cannot consume a later slot.

## DLC behavior

Event 54 should work with any supported DLC combination.

A technology that does not exist or is replaced without a DLC never enters the pool. A technology whose effect changes by DLC uses the active graph and current recipient state.

The event must not substitute an unrelated technology when a DLC-specific candidate is missing. It simply draws from the smaller valid pool.

## Initial connection candidates

The first implementation review should consider individual entries from these owners:

- Event 16 Brilliant Scientist
- Event 25 Alien Technology in Antarctica
- chemical and biological warfare systems
- unusual weapon systems
- future experimental technologies

The review should not assume that every technology from those systems is safe. Each candidate needs an explicit owner decision.

## Technology inventory requirement

Before implementation is accepted, the normal technology graph and every registered candidate must be inspected against the installed game and current mod.

The implementation must use the technology inspection, rendering, and comparison workflow to prove:

- candidate existence
- folder and graph placement
- prerequisites
- exclusivity
- unlock effects
- DLC conditions
- asset references
- owner references
- safe direct grant behavior

The resulting eligible inventory should be generated or maintained from reviewed source data. It should not depend on memory or a short handwritten list that becomes stale when the technology graph changes.
