# Asteroid Incoming, Part 2: Targeting and Trajectory

## Chooser ownership

Event 028 is one global transaction. The player country whose event system selected the major event becomes the chooser. The chooser remains fixed until the outcome finishes, even if the human changes country during the two-day delay.

In multiplayer, the first valid Event 028 transaction blocks another copy from opening. The chooser receives the full target event. Other human players receive an observer notice after a trajectory is locked or a close passage is selected. Ghost-copy behavior must not create independent target rolls or several impacts.

The event history row should identify the chooser because that actor exists before the option is selected. The impact outcome must separately record the chosen target country and state.

## Building three target pairs

The event constructs exactly three distinct country and state pairs. A country appears at most once. A state appears at most once. The pairs are locked before the option event opens.

### Valid target country

A target country must meet all of the following conditions at pair construction.

- It exists and controls at least one owned land state.
- It has a viable backup state outside the proposed center so the event does not leave an active country with no possible capital or functioning territory.
- It is not the chooser.
- It is not an actually nonhuman country under the shared classifier.
- It is not an empty carrier, temporary system tag, observer tag, wasteland polity, or country whose only territory is already unusable.
- It has at least one state that can satisfy the impact-state rules.

Special Chaos countries that still represent ordinary human societies may remain eligible when they have normal territory and civilian population. The exclusion should target impossible or system-only actors, not every country with an unusual event origin.

The candidate pool should not filter out enemies, allies, faction partners, subjects, guarantees, or neutral countries for the human chooser. Those relationships create part of the choice. AI option logic handles protected relationships separately.

### Valid impact state

A state is eligible as a main center when it meets all of the following conditions.

- It is land and has real state adjacency data.
- It is owned and controlled by the candidate country when the pair is built.
- It is not already a permanent wasteland, asteroid crater, or invalid map space.
- It contains civilian population.
- It contains at least one meaningful settlement, building, industrial level, logistical asset, or victory point.
- A main impact there leaves the target country with at least one valid surviving state for capital relocation and continuing country scope.

A capital can be selected. Capital impacts need the relocation contract defined below.

### State suitability score

Eligibility creates the pool. A suitability score chooses the state inside each candidate country. The score should reward the following qualities.

- More unique land states within three adjacency steps
- At least two direct land neighbors
- Higher civilian population
- Greater industrial and logistical importance
- A victory point, supply hub, railway junction, air base, naval base, or major infrastructure concentration
- A central continental position that lets the rings cross meaningful borders

The score should penalize the following qualities.

- Isolated islands
- A state with only one narrow neighbor when better options exist
- Very low population and no buildings
- An already devastated or mostly empty state
- A remote appendage that creates almost no outer ring

The system should still allow unusual geography when a country has no better state. The suitability score is a preference model, not a reason to silently replace a selected country with another country.

## Country diversity across the three options

After choosing one best state per candidate country, the event selects three pairs from the global pool. It should use a broad regional diversity preference.

- Prefer at least two continents when enough valid pairs exist.
- Avoid three countries in the same immediate strategic region when broader choices remain.
- Do not force a continent quota that produces weak island targets.
- Do not always favor majors. Population and adjacency matter, but small continental countries can appear.
- Do not use diplomatic relations with the chooser to decide the human target pool.

The result should feel random and globally varied while remaining suitable for the event's damage geometry.

## Information shown on target options

Each impact option should expose enough information for a meaningful choice.

- Target country flag and current name
- Locked state name
- Broad region or continent
- Whether the state is the current capital
- A compact severity summary that states the center will be destroyed and three neighboring rings will be damaged
- When Global Fragmentation is active, a visible statement that unrelated fragments will also strike worldwide
- When Extraordinary Minerals is active, a visible statement that crater control will carry a military resource advantage

The option should not expose hidden scores, exact fragment locations, random damage rolls, AI logic, or future diplomatic reactions.

The miss option should state that the asteroid will pass close to Earth and that no impact or dust will occur. It should not imply a later surprise strike.

## Confirmation

Selecting a country opens a confirmation step that repeats the target country, state, and expected global consequences. Confirmation prevents an accidental campaign-changing click.

After confirmation, the transaction stores the following outcome context.

- Chooser country
- Locked target country
- Locked impact state
- Locked broad region
- Lock date
- Expected impact date
- Whether fragmentation is active
- Whether extraordinary minerals are active
- A snapshot of the target's current display name and flag context for later presentation if the tag changes

Canceling the confirmation returns to the same four choices. It must not reroll targets.

## Two-day trajectory lock

The impact resolves two game days after confirmation. The delay is long enough to present a target response and build anticipation. It is too short for a full construction mechanic.

The locked state is a geographic coordinate. During the delay:

- A peace conference does not move the impact.
- Annexation does not move the impact.
- A civil war does not move the impact.
- A state transfer does not move the impact.
- A cosmetic tag or country-name change does not move the impact.
- The target snapshot remains available for the super-event and global news.

The current owner and controller at the moment of impact receive state losses and grouped reports for the territory they actually hold. The original selected country remains named as the intended target.

If the state becomes invalid through another permanent map transformation during the two-day delay, the transaction must fail closed. It should produce a rare global near-miss or atmospheric break-up report and must never redirect to an unchosen state. This contingency should not grant dust, fragments, crater material, or impact deaths.

## Target-country emergency response

The locked target country receives one emergency event. The event offers three preparedness stances. These are working route labels and are not final option text.

### Preserve command continuity

The government moves archives, senior officials, communications staff, and military command elements away from the center.

- Best when the impact state is the capital or contains major command infrastructure
- Reduces the duration and severity of the post-impact coordination penalty
- Improves capital-relocation readiness
- Does not reduce the fixed center or ring population losses

### Disperse transport and stockpiles

Rail yards, fuel, trains, trucks, aircraft, and movable stockpiles are pushed toward safer states.

- Preserves part of the country's mobile logistical reserve
- Improves the first emergency rail and debris-clearing actions
- May temporarily disrupt national supply before the impact
- Does not preserve buildings inside the center

### Prepare hospitals and shelters

Medical staff, shelters, water stores, and local rescue units prepare for mass casualties outside the center.

- Reduces the opening recovery burden in outer rings
- Reduces continuing rescue-period deaths after the initial impact
- Improves the first medical response action
- Does not change the required immediate population percentages

The target AI should choose the stance that addresses the largest expected problem. Capital impact, low stability, weak transport reserves, population density, and medical readiness should matter.

## Capital relocation

When the locked center is the current capital, the impact transaction relocates the capital before destroying the state.

The backup-capital score should favor:

- Owned and controlled core territory
- A populated state outside the main center and first ring
- Useful infrastructure and supply
- A victory point or established city
- Distance from an active frontline
- Connection to the country's remaining territory

The score should avoid:

- Another asteroid crater or wasteland
- An occupied or contested state
- A state inside the first damage ring when safer options exist
- An isolated empty region

If no controlled core state is valid, use the best controlled owned state. If none remains valid, the original target country was not a valid target and should have been excluded during pair construction.

The relocation should preserve government continuity. It should not create a new country identity, leader, flag, or focus tree.

## Land-adjacency ring construction

The damage footprint uses shortest land-state adjacency from the locked center.

- Ring 0 is the locked center.
- Ring 1 contains every eligible land state directly adjacent to Ring 0.
- Ring 2 contains every eligible land state adjacent to Ring 1 that is not already in Ring 0 or Ring 1.
- Ring 3 contains every eligible land state adjacent to Ring 2 that is not already in an earlier ring.

A state that can be reached through several paths belongs to the smallest ring number. It is processed once.

The ring builder should follow actual state adjacency across national borders. Sea-zone proximity does not count. A purely maritime gap does not create a damage link. A verified strait connection may count only when the engine state-adjacency data treats the states as connected for the chosen helper.

Impassable land states can carry the physical ring outward when their adjacency is real, but they should not receive normal population or building transactions when they contain no valid civilian or building surface.

## Fragment footprint separation

Global Fragmentation uses the same shortest-path approach for its two rings. Fragment centers must be distributed to avoid repeated damage in one region.

- A fragment center cannot be inside the main three-ring footprint.
- A fragment center cannot be another fragment center's first ring.
- Prefer one fragment center per country until the pool is exhausted.
- Prefer several continents when valid states exist.
- If outer fragment rings overlap, a state receives only the strongest fragment damage level.
- If a fragment ring overlaps a main ring, the state receives only the stronger of the main and fragment profiles.

The system should reduce the fragment count when the world cannot provide enough separated valid centers. It must not force overlapping centers, invalid states, empty islands, or repeated damage transactions to meet a numeric target.

## Target generation failure states

The event should show `N/A` in Event Details and remain outside automatic selection when fewer than three valid target pairs exist.

Manual force-trigger behavior may bypass normal timing. It should not bypass the requirement to build three real options. A forced event with an invalid world state should return a clear blocked result instead of opening broken options.
