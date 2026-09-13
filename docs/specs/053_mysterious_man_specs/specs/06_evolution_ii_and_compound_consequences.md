# 6. Evolution II and Compound Consequences

## Evolution II activation

Evolution II becomes eligible at `800+` Chaos.

If Event 53 has not fired yet, the first appearance can begin with Evolution II behavior when the evolution is enabled. The setup records the Event 53 evolution milestones that are actually enabled and needed by the active behavior.

If the chain is active, Evolution II uses the same target-local paced activation model as Evolution I. The milestone identifies the selected country as actor and gives zero Chaos by itself.

A disabled Evolution I must not make an enabled Evolution II unusable. Evolution II independently unlocks the full demand family required for its larger demands and activates only its own Evolution II registry additions. Disabled Evolution I package additions remain inactive. Evolution II does not falsely record or display a disabled lower evolution.

## Demand behavior

Evolution II keeps one demand per visit. It raises minimums, proportional shares, progression strength, and caps.

A large country should sometimes face a demand that changes war plans, production, doctrine spending, mobilisation, or political timing. A small country should face an amount scaled to its real capacity, not a major-power absolute value that makes every visit an automatic refusal.

The Command Power cap remains 60. Industrial-capacity demands remain timed burdens instead of permanent factory deletion.

## Evolution II registry additions

### `mm_ii01_several_independence_movements`

**Owner:** Event 006 Independence Wave.

Several valid independence movements become independent from the selected player's territory in one frozen release transaction. The owner determines the number from target size, valid movements, controlled territory, refusal history, and campaign safety.

Each new country receives a viable package. The transaction must reserve territory before release, prevent duplicate state grants, retain a viable remnant for the target when possible, and define immediate wars against the former host where appropriate.

The entire release wave is one Event 53 ballot. Each movement does not receive a separate ballot.

### `mm_ii02_multi_front_civil_war`

**Owner:** Event 021 Random Civil War or a shared civil-fracture system.

The selected country enters a civil war with several fronts, regional commands, or rival political centers. The owner can create more than one rebel actor when it can divide states, forces, equipment, leaders, supply, and claims safely.

This package is distinct from the baseline civil-war ballot because it creates a broader national rupture with multiple simultaneous fronts.

### `mm_ii03_smallpox_outbreak`

**Owner:** the disease system.

A severe smallpox outbreak begins in several valid population centers or one highly connected region. The disease owner controls agent behavior, spread, mortality, containment, vaccination or treatment routes, Air Cleanliness interaction when applicable, and cleanup.

The package is invalid when the smallpox agent or required outbreak infrastructure is unavailable.

### `mm_ii04_plague_outbreak`

**Owner:** the disease or plague owner.

A severe plague outbreak begins under the real plague mechanics. The owner controls state seeding, spread, mortality, containment, rat or vector interactions where applicable, and cleanup.

This package does not automatically fire a plague source event, unlock plague-created countries or leaders, advance plague evolutions, or start a plague world-end route. A bounded plague outbreak adapter must separate ordinary outbreak behavior from source-event lifecycle.

### `mm_ii05_several_natural_disasters`

**Owner:** Event 013 Natural Disasters.

Several disaster jobs are created in separated valid targets. The owner chooses compatible families and states, prevents duplicate targets, applies deaths and damage, and owns reports and cleanup.

This package is invalid when the Natural Disasters gateway cannot commit the complete multi-disaster transaction.

### `mm_ii06_severe_intelligence_compromise`

**Owner:** Event 52 Intel Leaked.

The target suffers the strongest nonterminal intelligence-compromise package currently safe for Event 52. More foreign governments can gain broader categories of intelligence for longer periods, with stronger network and planning exposure.

The adapter must retain Event 53 attribution and leave Event 52's firing, weight, evolution, history, super-event, and world-end state untouched.

### `mm_ii07_severe_embargo`

**Owner:** Event 50 Great Embargo.

A broad coalition applies a high-severity embargo with stronger trade, lend-lease, diplomatic, foreign-support, and strategic-resource pressure. The owner controls coalition validity, participation, duration, DLC-aware enforcement, target receipts, and cleanup.

Event 50 remains eligible to fire later.

### `mm_ii08_mass_military_mutiny`

**Owner:** a reusable military-fracture system.

Large parts of the armed forces refuse orders across several commands. Units can defect, dissolve, seize depots, destroy equipment, or form armed authorities. The package can affect land, naval, and air institutions where valid.

The owner must prevent double transfer of units and equipment, preserve a viable government force when possible, and define cleanup for temporary military actors.

### `mm_ii09_several_neighboring_wars`

**Owner:** a reusable war-crisis system.

Several valid neighboring or strategically connected countries enter wars against the selected player. The owner constructs a safe actor set, checks access, faction and subject relations, truces, guarantees, existing wars, strength floors, and conflict compatibility.

The package is absent when it cannot create at least two valid foreign fronts.

### `mm_ii10_enormous_industrial_destruction`

**Owner:** Event 53 or a shared industrial-catastrophe owner.

A large share of industrial and logistics capacity is damaged or destroyed across several major states. Civilian factories, military factories, dockyards, railways, infrastructure, ports, airbases, and supply facilities can be affected according to state role.

The package must distribute damage through a dynamic state-selection plan and must feed ordinary death or population-loss systems only where the chosen damage model actually causes casualties.

### `mm_ii11_catastrophic_famine`

**Owner:** the famine system.

A large food-security crisis begins across several proven vulnerable states. The request uses a high severity profile, but famine retains ownership of production, transport, extraction, need, environment, relief, mortality, evacuation requests, and recovery.

The adapter cannot bypass famine validity merely because Event 53 selected the package.

### `mm_ii12_mass_displacement`

**Owner:** the migration system.

Several large civilian cohorts are forced into internal displacement, cross-border flight, evacuation, or trapped-population states through proven movement causes and routes. The migration owner controls exact transfers, route deaths, reception, settlement, return, and cleanup.

The package must never debit the same population twice through a separate Event 53 population effect.

## Compound packages

Every compound package below is one registered entry with one equal ballot.

A compound package is valid only when every component can be committed safely. It cannot enter the pool and later drop a component because one adapter became inconvenient.

### `mm_ii13_independence_and_armed_war`

**Owners:** Independence Wave and the reusable war system.

Several viable independence movements are released through one frozen territory transaction. Every released country receives military preparation and enters an immediate war against the former host, subject to the owner's conflict rules.

Execution order:

1. reserve all release candidates and state packages
2. reserve force, equipment, leader, and capital packages
3. release countries and establish ownership
4. assign armies, claims, and diplomacy
5. create wars against the selected target
6. reconcile the Event 53 target marker
7. return one combined receipt

The Event 53 target remains the former host unless a later legal-successor transaction proves otherwise.

### `mm_ii14_civil_war_and_intelligence_exposure`

**Owners:** Random Civil War and Intel Leaked.

A serious civil war begins, followed by a severe intelligence exposure that affects the legal government and can also expose valid rival-command information according to the adapter design.

Execution order:

1. reserve civil-war actors, states, leaders, units, and equipment
2. create the civil war
3. identify the continuing Event 53 target government
4. resolve intelligence recipients and exposed categories for the new conflict state
5. apply exposure without firing Event 52
6. return one combined receipt

The intelligence component cannot leak event-target pointers from the pre-split country state.

### `mm_ii15_disease_and_food_collapse`

**Owners:** disease and famine.

A severe disease outbreak and a connected food-security collapse begin in compatible regions. Disease pressure can damage labour, transport, and relief access. Famine receives only proven effects and retains its own stage logic.

Execution order:

1. reserve outbreak states and food-security states
2. ensure that the combined state set does not cause duplicate population transactions
3. seed the disease through its owner
4. register food-security pressure through the famine adapter
5. establish versioned disease and famine receipts
6. return one combined receipt

Deaths must be recorded once by the system that removes the population.

### `mm_ii16_embargo_and_stockpile_destruction`

**Owners:** Great Embargo and Event 53 stockpile helpers.

A severe embargo begins while a large strategic reserve is destroyed. The reserve type is selected after the compound package receives its ballot, from valid equipment, fuel, trains, or convoys.

Execution order:

1. reserve a valid embargo coalition
2. lock one valid strategic reserve type and amount
3. commit the embargo
4. debit the locked reserve once
5. return one combined receipt

The reserve subtype does not receive an extra Event 53 ballot.

### `mm_ii17_mutiny_and_external_war`

**Owners:** military fracture and war crisis.

A mass military mutiny begins immediately before one or more valid foreign actors attack. The foreign war must use the post-mutiny force state when evaluating safety and scale.

Execution order:

1. reserve mutiny commands, units, and depots
2. reserve valid foreign actors and conflict form
3. apply the mutiny
4. reconcile target military strength and Event 53 target ownership
5. start the external war
6. return one combined receipt

The package is invalid when the combined result would create a broken war with no viable participants or no reachable front.

## Compound rollback and partial failure

Most HOI4 state mutations cannot be rolled back safely after execution. Compound adapters must therefore reserve and prove all required actors, states, characters, and resources before the first irreversible mutation.

If prevalidation fails, the package stays out of the pool. If an engine race invalidates the package after selection but before mutation, the adapter rejects and Event 53 performs its bounded redraw.

Once the first irreversible component commits, the adapter owns completion of the remaining sequence. It cannot return a false clean rejection after leaving partial consequences behind.

## Evolution II severity changes to earlier packages

When Evolution II behavior is active:

- government paralysis lasts longer and affects more state capacity
- political collapses can open serious secondary unrest through their owner
- mutiny, separatist, civil-war, border, and external-war packages receive stronger initial forces
- stockpile losses threaten operational plans instead of only reducing minor reserves
- factory and infrastructure packages can damage several major regions
- ordinary disease, disaster, famine, and displacement requests use high safe severity profiles
- assassination can target the most consequential valid characters

Earlier packages still appear once each.

## Probability consequence of registry expansion

Evolution II does not make an existing severe package more likely. Its effect comes from adding new high-severity and compound entries.

The active pool size must be visible to debug and probability tools, but it remains hidden from ordinary player-facing text.

The probability auditor must test at least:

- a compact peaceful target with few territorial packages
- a continental major at war
- a colonial or occupation-heavy power
- a maritime empire
- a country with several valid independence movements

For each scenario, the auditor must show that every active package has the same normalized probability.
