# Event 54: AI, Multiplayer, Balance, and Validation

## Randomness policy

Event 54 uses genuine random selection from each recipient's safe pool.

The event does not guide countries toward sensible research. It does not read AI strategy, active production, army composition, terrain, coastline, enemies, resources, or research plan when assigning candidates.

The only filters are safety and ownership filters.

This means a landlocked country can receive naval technology, a minor can receive advanced armor, and a major can receive a low-impact support technology. These mismatches are part of the event's identity.

## AI parity

AI countries use the same recipient check, pool construction, equal candidate weight, without-replacement rule, grant count, and pool exhaustion rule as human countries.

The AI does not receive hidden rerolls, better categories, extra grants, prerequisite completion, or compensation for a poor result.

The player does not receive protection from a poor result.

AI handling is needed only after the grant. The normal AI should be able to use newly unlocked equipment, modules, or capabilities under existing research and production logic. A registered owner technology must include any AI compatibility needed for its safe use.

## No strategic weighting

The following factors must not change candidate weight:

- technology year
- research cost
- technology category
- country size
- major status
- number of research slots
- current doctrine
- current production lines
- equipment shortages
- naval access
- current wars
- ideology
- faction
- current AI plan
- player or AI control

Registered technologies also use equal weight. Owners cannot buy more exposure through hidden weight values.

## Power variance

The event deliberately creates unequal rewards.

Balance comes from these controls:

- every country receives the same target number of draws
- every draw comes from that country's safe missing pool
- duplicate grants are blocked
- branch incompatibility is enforced
- custom technologies require explicit owner approval
- event-owned reward packages remain excluded
- direct Chaos gains use one-time guards
- normal Minor Repeatable weight decay limits return frequency

The event should not normalize technology power through a tier budget. Such a budget would make the outcome more predictable and would require subjective power scores that become stale.

## Snowball control

Event 54 grants completed technology but does not grant:

- research slots
- research speed
- ahead-of-time reduction
- production efficiency
- factories
- resources
- equipment stockpiles
- units
- doctrines
- special project progress
- technology-sharing membership

A powerful result can still accelerate a country, especially at higher evolutions. The global distribution and random mismatch reduce the chance that one country alone receives a reliable advantage.

## Small-country outcomes

A weak country can gain advanced technology that it cannot produce effectively. This is acceptable.

The event should not add free factories, resources, designers, templates, modules, or equipment to make every grant immediately useful.

A technology that is entirely inert without an owner-specific capability may need an approved callback or should remain excluded.

## Advanced-country outcomes

A leading country may have a small eligible pool. It can receive a low-impact result or exhaust its pool before the evolution target.

The event should not create synthetic placeholder technologies to guarantee ten grants.

Pool exhaustion gives advanced countries a natural upper bound while less developed countries retain large, unpredictable pools.

## Repeated firing outcomes

A repeated firing selects from what remains. This naturally reduces duplicate categories and pushes countries deeper into unresearched parts of the graph over time.

A country that eventually researches every eligible technology receives no further benefit until new eligible content enters the graph.

The event does not reset the pool or forget previous grants.

## Multiplayer fairness

The same synchronized transaction determines results for every client.

No player can reroll by reopening the report, changing a local setting, switching tabs, or delaying acknowledgement.

The random sequence should be committed before the first human report appears.

A player who changes country after commitment does not receive a new draw. A newly controlled country keeps the result that was assigned to it as an AI recipient.

## Exploit controls

The implementation review must test these abuse cases:

- saving after seeing the report and reloading to reroll
- switching tags before or during report delivery
- releasing many tiny countries immediately before the firing
- creating temporary civil-war tags during the transaction
- registering one technology under several providers
- registering aliases of the same technology
- grant packages that hide several unrelated rewards
- owner callbacks that mark their event fired
- custom providers that flood the expanded pool with low-value variants
- a branch choice granting both sides across several slots
- a technology removed and regranted repeatedly by another system
- duplicate human reports creating repeated grants

The normal event system decides when Event 54 fires. The spec does not add special anti-release penalties merely because more countries mean more total world technology. Each valid country remains entitled to the world event.

## Probability audit goals

The random pool and Scientific Research cluster require a formal probability pass.

The audit should start from actual candidates and named scenarios. It must distinguish exact probabilities, bounded results, sampled results, score-only findings, and unresolved cases.

The audit should prove:

- equal eligible candidate weight inside one recipient pool
- no hidden category preference
- no duplicate candidate identity
- no incompatible branch pair across multiple grants
- no custom provider dominance in representative 1936, 1940, and late-game pools
- stable behavior when the eligible pool is smaller than the grant target
- cluster participation ordering that matches the targets in Part 5
- no optional cluster member starvation
- no repeat sequence that can loop forever after rejection

The separate probability matrix defines the required scenarios.

## Technology graph audit goals

The implementation must inspect and render the affected technology graph before finalizing eligibility.

The audit should cover:

- every ordinary candidate folder
- every excluded doctrine folder
- every branch exclusivity family
- every registered custom candidate
- every grant package
- every callback-owned setup dependency
- every DLC variant
- every technology icon and localization reference used in the report

The before-and-after technology comparison should confirm that Event 54 changes grant access and registry behavior without changing the normal research graph itself.

## Event-chain audit goals

The event chain should be inspected as one global orchestration event plus country report events.

The audit should confirm:

- one global history entry
- one pacing transaction
- one grant transaction per firing
- no AI report spam
- one report per human recipient
- no duplicate grant after save and reload
- evolution stage selected once before country processing
- disabled evolution fallback
- temporary state cleanup
- safe continuation after one country's pool or callback fails

## Cluster audit goals

The Scientific Research cluster audit should confirm:

- stable cluster identity
- Minor Repeatable cluster behavior
- 200+ unlock
- accepted five-member roster
- correct per-member severity
- Event 27 many-to-many membership
- selected anchor handling
- optional participation and skip reasons
- continued availability after fire-once members leave
- one global pacing count
- correct member history and event details

## Balance scenarios

Balance should be evaluated in at least these campaign states:

### Early world

Most countries have large ordinary pools. Baseline and Evolution I should almost always reach their full target.

### Uneven 1940 world

Majors have different research histories, minors remain far behind, and branch choices are established. Results should stay independent and safe.

### High-chaos expanded pool

Evolution II is active and several owners have registered custom technologies. Ordinary candidates should remain substantial in representative pools.

### Scientific Deluge

Evolution III grants ten technologies. The transaction should finish in bounded time and reports should remain readable.

### Near-complete research power

A late-game major has fewer than ten safe missing technologies. Pool exhaustion should produce a partial report without fallback grants.

### New country

A recently created valid country has a large missing pool and receives the full current target after its creation transaction is complete.

### Special research actor

A nonhuman or special Chaos country with a valid research system participates. A system actor without safe research is excluded.

### Same-cluster setback

Gift from Scientists and Research Failure affect the same human country. Completed grants and reduced slot capacity both remain.

## Acceptance threshold

The event is balanced when its unpredictability remains visible, every country follows the same selection rules, custom rewards stay owner-controlled, repeat firing cannot farm direct Chaos, and no technology or cluster combination creates an invalid state.

Balance does not require equal strategic value between countries. Unequal strategic value is the intended result.
