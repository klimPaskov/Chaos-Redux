# Event 53 Probability Scenario Contract

Every weighted or random-selection surface must be inspected through the HOI4 MCP probability workflow. Source review and hand arithmetic do not replace this evidence.

## Required workflow

For every scenario:

1. run `hoi4.probability_inspect` on the exact target, demand, or consequence selector
2. declare the complete candidate pool and every external validity factor
3. run `hoi4.probability_evaluate`
4. use `hoi4.probability_sweep` when a threshold or country state changes validity
5. use `hoi4.probability_compare` after any source patch
6. use `hoi4.probability_render` for pool matrices, comparisons, or sensitivity views
7. classify the result as exact, bounded, sampled, score-only, or unresolved

The auditor must record adapter revision, scenario hash, candidate-pool completeness, and artifact references.

## Target-selection scenarios

### `MM-P-TGT-001` Single valid player

**State:** One human-controlled ordinary country exists and passes all target gates.

**Complete pool:** That country only.

**Expected:** Exact probability `1`.

**Failure:** Any AI country, special Chaos actor, nonhuman country, or invalid player appears.

### `MM-P-TGT-002` Four valid players

**State:** Four human-controlled ordinary countries with different sizes, ideologies, war states, and host status all pass the target gates.

**Complete pool:** Four countries, one entry each.

**Expected:** Exact probability `0.25` for each.

**Failure:** Major status, host status, size, ideology, or war state changes the result.

### `MM-P-TGT-003` Mixed valid and invalid players

**State:** Five human-controlled countries. Three are ordinary valid targets. One is an actual nonhuman country. One owns no state.

**Complete pool:** Three valid countries.

**Expected:** Exact probability `1 / 3` for each valid country. Invalid countries are absent.

### `MM-P-TGT-004` No valid player

**State:** Every human-controlled country fails at least one hard target gate.

**Complete pool:** Empty.

**Expected:** Event 53 is unavailable and returns no selection.

## Demand-selection scenarios

### `MM-P-DEM-001` Baseline demand

**State:** Event 53 active with no broader demand evolution behavior.

**Complete pool:** Political Power only.

**Expected:** Exact probability `1` for Political Power.

### `MM-P-DEM-002` Evolution I continental major

**State:** Human continental major with army, navy, air force, rail network, convoys, fuel use, manpower, civilian industry, military industry, Stability, and War Support systems.

**Complete pool:** Every demand type whose applicability trigger passes, with one entry each.

**Expected:** Exact equal normalized probability for every valid type.

**Required evidence:** List every valid and invalid type and the exact trigger reason.

### `MM-P-DEM-003` Evolution I landlocked minor

**State:** Human landlocked minor with no port, no convoys, no navy, limited air system, small industry, and normal land forces.

**Complete pool:** Political Power, Command Power, applicable experience types, applicable land equipment, trucks, trains when meaningful, fuel when meaningful, manpower, valid industrial capacity types, Stability, and War Support. Navy and convoy types must be excluded when their applicability gates fail.

**Expected:** Exact equal normalized probability among the remaining valid types.

### `MM-P-DEM-004` Valid but unaffordable resource

**State:** A country has a meaningful infantry-equipment system but currently holds less than the locked structural-floor demand.

**Complete pool:** Infantry equipment remains a valid demand type.

**Expected:** Its type-selection probability remains equal to other valid types. The later pay option is disabled.

**Failure:** Affordability silently removes the type when the system itself remains applicable.

### `MM-P-DEM-005` Demand-pool threshold sweep

**State changes:** Add a port, add convoys, create naval production, establish an air force, increase civilian factories, increase military factories.

**Method:** Use `hoi4.probability_sweep` across each applicability threshold.

**Expected:** A demand type enters once when its full applicability trigger becomes true. Existing entries retain equal weight.

## Consequence-pool scenarios

### `MM-P-CON-001` Direct-only minimum pool

**State:** All owner adapters are unavailable or invalid. The target is a normal compact country.

**Complete pool:** Every valid direct Event 53 baseline package, including government paralysis exactly once.

**Expected:** Exact equal probability for every direct entry. Pool cannot be empty.

### `MM-P-CON-002` Compact peaceful country

**State:** Small peaceful country, no occupied territory, no viable separatists, no convoy system, no active war, modest industry, normal civilian systems.

**Complete pool:** All valid direct political, stockpile, industrial, disaster, humanitarian, intelligence, diplomatic, disease, and civil packages whose adapters are live. Territorial and maritime packages that fail validity are absent.

**Expected:** Exact equal probability among the declared pool.

### `MM-P-CON-003` Occupation-heavy empire

**State:** Large target controls extensive non-core and occupied territory with several viable movements.

**Complete pool:** Baseline plus valid occupation, uprising, civil, Independence Wave, famine, displacement, war, and other packages permitted by active behavior.

**Expected:** Each package appears once. Several candidate uprisings and movements remain internal targets and do not create extra Event 53 ballots.

### `MM-P-CON-004` Maritime empire

**State:** Large target with ports, convoys, overseas supply, navy, fuel dependence, and colonies.

**Complete pool:** Include valid convoy, embargo, maritime disruption, occupation, displacement, war, and direct packages.

**Expected:** Convoy loss appears once. Each potential convoy route or overseas territory does not add another ballot.

### `MM-P-CON-005` Evolution II major at war

**State:** Continental major in a large war, with several neighbors, occupied territory, strong armed forces, valid disease and disaster targets, and live owner adapters.

**Complete pool:** Every valid baseline, Evolution I, and Evolution II package, including each compound package only when all components prevalidate.

**Expected:** Exact `1 / N` for every active entry.

### `MM-P-CON-006` Evolution III maximum registry

**State:** Large empire at 1000+ Chaos with every accepted adapter live and every package validity condition deliberately satisfied.

**Complete pool:** All 57 accepted packages, unless a documented package has a mutually exclusive hard state that cannot coexist with the scenario.

**Expected:** If all 57 are valid, exact probability `1 / 57` for each and aggregate Evolution III catastrophe chance `7 / 57`.

**Required evidence:** Any missing package must have an explicit validity reason. The auditor cannot assume all 57 without inspection.

### `MM-P-CON-007` Previous package remains valid

**State:** The last refusal selected a package that remains valid on the next visit.

**Complete pool:** Fresh current pool including the previous package once.

**Expected:** Previous selection does not reduce or increase its probability.

### `MM-P-CON-008` Invalid package exclusion

**State:** Begin with an occupation-heavy target, then remove all qualifying occupied territory before the next refusal.

**Method:** Compare the two complete pools.

**Expected:** Occupation revolt and any dependent compounds disappear. Every remaining package renormalizes equally.

### `MM-P-CON-009` Variant inflation check

**State:** Natural Disasters has several valid disaster families. Independence Wave has several valid movement targets. Assassination has several valid characters.

**Complete pool:** One Natural Disaster entry, one applicable Independence Wave package entry, and one assassination entry.

**Expected:** Internal candidate counts do not change Event 53 package probabilities.

### `MM-P-CON-010` Compound one-ballot check

**State:** All five Evolution II compound packages are valid.

**Complete pool:** Each compound appears once alongside every other valid package.

**Expected:** A compound's several components do not create several selector entries.

### `MM-P-CON-011` Disabled evolution

**State:** Evolution I disabled, Evolution II enabled and active at 800+ Chaos.

**Complete pool:** Baseline entries plus valid Evolution II entries. Evolution I entries are absent. The full demand family remains available because Evolution II independently requires it.

**Expected:** Every active package remains equal, and no disabled Evolution I package appears.

### `MM-P-CON-012` Source event disabled

**State:** Source random event disabled, underlying owner mechanic otherwise enabled, and no separate adapter toggle exists.

**Complete pool:** The matching borrowed package is absent.

**Expected:** Event 53 respects the source event toggle. If an owner later exposes a separately named adapter toggle, test that explicit contract in an additional scenario.

### `MM-P-CON-013` Adapter rejection recovery

**State:** Force one selected adapter to return a documented pre-mutation rejection after initial validity.

**Complete first pool:** Includes rejected package.

**Complete rebuilt pool:** Fresh current valid pool with rejected package excluded for this transaction only.

**Expected:** Uniform redraw from the rebuilt pool. If the second adapter rejects, government paralysis applies without another random roll.

**Classification:** Bounded transaction behavior, not a long-run probability claim unless the rejection process is fully declared.

## Timing scenarios

### `MM-P-TIM-001` Baseline interval distribution

**State:** First completed baseline visit, no refusals.

**Expected:** Every result lies within the baseline constants and above the 45-day floor.

### `MM-P-TIM-002` Refusal compression sweep

**State:** Consecutive refusals from zero through the configured cap.

**Method:** `hoi4.probability_sweep` or timing evaluation across each refusal count.

**Expected:** Intervals shorten monotonically until the cap, then stop shortening. No result falls below 45 days.

### `MM-P-TIM-003` Payment reset

**State:** Several consecutive refusals followed by a payment.

**Expected:** Consecutive-refusal interval pressure clears, while total historical refusal pressure remains only if the constants define it.

### `MM-P-TIM-004` Evolution interval comparison

**State:** Same target and visit history across Baseline, Evolution I, Evolution II, and Evolution III behavior.

**Expected:** Later tiers use shorter configured distributions, with overlap permitted and floor preserved.

## Affordability sampling scenarios

### `MM-P-AFF-001` Country-size matrix

Sample a minor, regional power, major, and very large empire at each behavior tier.

Record:

- selected demand type
- locked amount
- structural anchor
- current reserve anchor
- progression multipliers
- cap
- affordability result

Compare the observed affordability bands with the balance targets in the core specification.

### `MM-P-AFF-002` Repeated compliance

Evaluate five or more successful payments with otherwise stable country state.

Expected demand strength rises clearly at first, then flattens under the configured cap.

### `MM-P-AFF-003` Stockpile dumping sensitivity

Evaluate the same equipment demand across declining current stockpiles while structural capacity remains constant.

Expected amount does not collapse below the structural floor. Affordability can change from true to false.

## Comparison requirement

Any patch to:

- target selection
- demand-type validity
- demand-type weights
- consequence registration
- package validity
- random index logic
- interval randomization
- amount progression
- AI owner weights inside connected systems

requires a baseline audit, owner-applied patch, and `hoi4.probability_compare` using the same named scenarios.
