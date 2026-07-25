# Reviewed Global Survival Candidate 49: The Missing Patrol

## Contract status

The Missing Patrol is a dormant Fallout-owned ordinary candidate in the `chaosx.fallout` namespace. It uses candidate `527`, transaction `710049`, route `7149`, event blocks `527` through `533`, and Event Log history `9154`. The row is eligible only after a produced current-generation Air Winter receipt, a surviving owned state, current state identity and resource rows, a usable Supply Access value, and an exposed winter operation surface are all present.

The candidate does not set a scheduler activation flag, call the ordinary scheduler, declare a war, install a native patrol character, or materialize a new country. Those surfaces remain outside this reviewed tranche and are recorded as engine-sensitive boundaries.

## Deterministic target and ledgers

The Fallout candidate producer selects the lowest native state id that passes the state contract. The country stores durable `fallout_missing_patrol_intelligence_current`, `fallout_missing_patrol_fear_current`, `fallout_missing_patrol_reputation_current`, `fallout_missing_patrol_contact_current`, and `fallout_missing_patrol_cause_memory_current` ledgers. The state stores authenticated generation, owner, and committed-registry values while the chain is open. Cleanup clears transient registry and frozen rows but preserves the durable cause-memory ledgers and state memory flags.

The opening freezes Food, Fuel, Equipment, Scrap, Recognition, Cohesion, War Support, Command Power, Army Experience, state Supply Access, Air Winter exposure, Air Winter reclamation, and the five patrol ledgers. Result and callback triggers recheck generation, owner, target state, state identity, durable resources, state owner, current Air Winter snapshot, and produced source kind before any effect is applied.

## Branch contract

The human and hidden-AI lanes share one deterministic outcome calculation and one result and callback effect path.

1. Search the ruins sends a protected team through the ash cut. It spends Fuel, Equipment, and Scrap. Success raises intelligence, lowers fear, restores Supply Access, and records a recovered patrol memory. Partial success recovers a radio fragment with a smaller route repair. Failure damages a state facility and routes population loss through the Deaths system.
2. Retaliate at the border orders a limited military response without an automatic war declaration. It spends Fuel and Equipment. Success restores War Support and Army Experience while increasing exposure and fear. Partial success creates an armed standoff memory. Failure damages the route, reduces cohesion, and records the loss through the Deaths system.
3. Cover up the disappearance keeps the operation quiet and protects short-term stability. It spends Recognition and Food. Success limits public fear but lowers intelligence and reputation. Partial success keeps the story contained while the missing ledger remains open. Failure turns the cover story into a civilian scandal and records the loss through the Deaths system.
4. Wait for contact holds the route and listens for a return signal. It spends Food and Fuel. Success records a controlled contact and reduces exposure. Partial success leaves a weak signal and a live fear memory. Failure loses the route marker and records the loss through the Deaths system.

The deterministic viability score weights current Supply Access, Cohesion, War Support, Army Experience, Intelligence, exposure, and fear. Branch-specific success and partial thresholds are centralized in `fallout_world_end_missing_patrol_constants.txt`.

## Delayed callback and consequences

The result resolves after 60 days. A command review callback resolves after another 180 days. The callback grades current intelligence, fear, reputation, and contact rather than replaying the opening choice. A successful callback records a closed patrol memory and applies a temporary command-review modifier. A partial callback keeps an open patrol memory and a local-supply penalty. A failed callback records a lost-patrol warning, applies a temporary attrition modifier, damages infrastructure or an arms factory, and routes callback mortality through the Deaths system.

The result and callback update Air Winter exposure and reclamation, state Supply Access, Food, Fuel, Equipment, Scrap, Recognition, Cohesion, War Support, Command Power, Army Experience, Stability, and military modifiers. No branch uses a political-power store, a harmless failure, or a variable-only substitute for state damage.

## Presentation and review boundary

Event blocks use dedicated human result and callback text that names the ash cut, the radio fragment, the border road, and the selected state's government response. Hidden AI uses the same ledgers and delayed effects with no visible event. Event Log history `9154` records twelve result outcomes and three callback outcomes. Dedicated report art is bound only to this chain.

The chain is dormant until scheduler activation, host authority, save recovery, multiplayer input blocking, full-screen Fallout blackout ownership, runtime Event Log rendering, and manual review are proven. Native patrol creation, live neighbor selection, automatic war declaration, and dynamic tag allocation remain unproven and are not represented as completed mechanics.
