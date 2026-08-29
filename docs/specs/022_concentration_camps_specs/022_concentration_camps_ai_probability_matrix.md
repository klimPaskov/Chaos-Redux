# Event 22 Concentration Camps AI Probability Matrix

## Purpose

This file defines the AI behavior that implementation must prove. It does not contain guessed final weights. Exact values must be established from the complete candidate pool and evaluated through the HOI4 MCP probability workflow.

No live MCP probability run was available in the planning environment. Every result below is an intended ordering, zero condition, dominance expectation, or starvation guard that the implementation audit must test.

## Mandatory audit sequence

For every weighted surface:

1. Run `hoi4.probability_inspect` on the implemented source.
2. Record the complete candidate pool and every external factor.
3. Classify the result as exact, bounded, sampled, score-only, or unresolved.
4. Use `hoi4.probability_evaluate` for named scenarios.
5. Use `hoi4.probability_sweep` for country size, ideology, war, stability, exposure, resistance, and evolution ranges.
6. Use `hoi4.probability_sequence` when several dependent selections occur in one firing.
7. Use `hoi4.probability_simulate` only when exact evaluation is impossible or sequence behavior needs empirical evidence.
8. Use `hoi4.probability_render` when a visual comparison helps review.
9. After any weight patch, run `hoi4.probability_compare` against the same scenario set.

The probability auditor remains read-only. The parent or owning patch agent chooses the balance target and applies changes.

## AI profile assignment

One active profile is selected from campaign facts.

| Profile | Core signals | Hard blockers | Primary behavior |
| --- | --- | --- | --- |
| Dismantler | humanitarian route, democratic legal constraint, successor disclosure, liberation | current government has no authority to close | freeze intake, relief, records, closure |
| Restrictive Reviewer | moderate legal constraint, uncertain cabinet, low war pressure | active extermination policy not rescinded | inspection, ration reform, registration, gradual closure |
| Exploitative Authoritarian | repressive institutions, high labour demand, war, occupied territory | no valid assignment state or no transport | forced labour, selected expansion, guards, access restriction |
| Extermination Extremist | explicit radical route, historical package, Evolution I, valid target purpose | no valid target purpose, no evolution, closure lock | conversion, killing policy, concealment |
| Cover-up Escalator | high Exposure, expected state loss, public reports, criminal leadership | transparent accountability route locked | falsify, destroy records, relocate, stage inspection |
| Retreat and Collapse | enemy near sites, low supply, state loss, government collapse | no threatened sites | closure, transfer, abandonment, evacuation, liquidation according to ideology and prior policy |
| Liberator and Relief | controls stopped or liberated sites without continuing operation | current controller deliberately reuses site | secure, relief, evidence, survivor registration, resettlement |

Profile assignment must be deterministic from declared flags and campaign values where possible. A random tie break is allowed only between equally valid moderate profiles.

## Surface A: global Event 22 country selection

### Candidate-pool rules

Zero selection chance:

- `is_special_chaos_country = yes`
- no eligible state
- Event 22 disabled for the country
- protected after transparent closure
- active network with no valid incident and same-country cooldown active
- invalid state or country scope
- country is a liberator managing only relief and has no continued operation

Positive candidates:

- never received Event 22
- inherited dormant sites
- existing quiet sites
- occupied non-core territory
- active civil war
- radicalized repressive route
- labour or resource emergency
- high resistance and security pressure
- active famine or migration pressure

### Scenario matrix

| Scenario ID | Situation | Expected result |
| --- | --- | --- |
| `SEL_01_NEW_OVER_REPEAT` | ten valid never-fired countries and two active countries with ordinary incidents | at least 80 percent of total selection mass belongs to never-fired countries |
| `SEL_02_ONLY_REPEAT` | no valid never-fired country and three active countries with incidents | one repeat incident selected, with no attempt to create another opening network |
| `SEL_03_TRANSPARENT_PROTECTION` | one recent transparent closure country and one ordinary new candidate | protected country has zero chance |
| `SEL_04_SECRET_DEMOLITION` | one secretly demolished network and one ordinary new candidate | new candidate preferred, but secret-demolition country retains nonzero rediscovery or recurrence chance after minimum cooldown |
| `SEL_05_SMALL_COUNTRY` | one-state valid country with no other candidate | country receives one site only if capital exception is explicitly valid |
| `SEL_06_SPECIAL_COUNTRY` | Rat Nation, zombie actor, Death actor, and one normal country | every special actor has zero chance and normal country has all valid mass |
| `SEL_07_OCCUPATION_PRESSURE` | two otherwise similar countries, one with large occupied non-core territory | occupation country materially preferred, recommended at least two times the score |
| `SEL_08_CIVIL_WAR` | two otherwise similar countries, one in Event 21 civil war | civil-war country preferred, but no automatic extermination profile follows from the war alone |
| `SEL_09_NO_VALID_STATE` | country has states but every state excluded by protection, collapse floor, or control rule | zero chance and no fallback state substitution |
| `SEL_10_HISTORICAL_ADAPTER` | Germany, Japan, or Soviet Union with a valid established package versus generic peers | adapter availability increases valid selection and routes into the package without duplicating category content |

## Surface B: repeat-incident selection

Incident families:

- expansion attempt
- labour quota crisis
- evidence leak
- epidemic or famine
- resistance or escape
- front approach
- successor inheritance
- country-package handoff

| Scenario ID | Situation | Expected ordering |
| --- | --- | --- |
| `REP_01_HIGH_EXPOSURE` | Exposure above verified-leak threshold, low disease, stable front | evidence leak dominates ordinary expansion and labour incidents |
| `REP_02_EPIDEPTIC` | severe disease or famine in several sites | epidemic or famine incident dominates, with expansion near zero |
| `REP_03_FRONT_NEAR` | enemy within retreat threshold of one or more sites | front-approach incident dominates all non-emergency incidents |
| `REP_04_WORKFORCE_COLLAPSE` | several assignments have exhausted labour pools | labour quota crisis dominates expansion unless a valid new intake source exists |
| `REP_05_SUCCESSOR` | government or tag changed since last pulse | inheritance incident has priority and ordinary incidents wait until policy is chosen |
| `REP_06_PACKAGE_HANDOFF` | generic active network gains a valid country-specific package | package handoff must occur before another generic incident |
| `REP_07_NO_INCIDENT` | active network stable, no threshold met, cooldown active | candidate receives zero repeat-event chance and no filler popup |

## Surface C: opening policy choice

### Common hard blockers

- forced labour has zero score without at least one useful assignment state
- expansion has zero score at reach cap or without uncovered valid states
- extermination has zero score without Evolution I, valid target purpose, and explicit route support
- immediate closure has zero score only when the government truly lacks authority and a regional alternative must be used

### Scenario matrix

| Scenario ID | Situation | Expected ordering |
| --- | --- | --- |
| `OPEN_01_HUMANITARIAN` | stable legal government, no war, moderate industry, no radical route | closure first, review second, labour and expansion low, extermination zero |
| `OPEN_02_WARTIME_REVIEW` | legal government at war with industrial pressure and moderate security power | review first, closure competitive, labour possible but clearly lower, extermination zero |
| `OPEN_03_EXPLOITATIVE_WAR` | authoritarian government, war, labour shortage, valid factories and rails | forced labour first, expansion second, review lower, closure low but nonzero |
| `OPEN_04_OCCUPATION_SECURITY` | authoritarian occupier with high resistance and many valid non-core states | expansion and labour lead, with relative order based on resource demand |
| `OPEN_05_HISTORICAL_EXTREMIST` | explicit historical or radical extermination route, Evolution I, valid target registry | extermination can lead, but must not reach 100 percent deterministic choice unless the route explicitly requires it |
| `OPEN_06_EVOLUTION_NO_TARGET` | Evolution I active, radical ideology, no valid target purpose | extermination zero, other policies evaluated normally |
| `OPEN_07_NEAR_DEFEAT` | losing war, enemy near core states, low transport | closure or review preferred over new labour and expansion, extremist route can still choose extermination or cover-up with bounded chance |
| `OPEN_08_INHERITED_NETWORK` | successor government with archives and no responsibility for original operation | disclosure and closure dominate, continuation depends on successor route |
| `OPEN_09_LOW_AUTHORITY` | government wants closure but security apparatus controls sites | review or regional closure selected, underground-network risk initialized |
| `OPEN_10_SMALL_ECONOMY` | very small economy and one camp state | policy avoids costs the country cannot pay, no impossible decision path selected |

### Dominance targets

- In `OPEN_01_HUMANITARIAN`, closure plus review should exceed 90 percent combined.
- In `OPEN_03_EXPLOITATIVE_WAR`, labour plus expansion should exceed 70 percent combined.
- In `OPEN_05_HISTORICAL_EXTREMIST`, extermination should be the single highest option but should usually remain below 85 percent unless the focus route hard-locks the outcome.
- In every no-target scenario, extermination must be exactly zero.

## Surface D: state selection for initial coverage and expansion

### State score components

Positive:

- valid occupied or non-core state
- registered target population or detainee source
- rail, port, or convoy access
- existing quiet site
- meaningful labour assignment
- low foreign access for secret operation
- strong regime control

Negative:

- capital
- recently liberated relief state
- protected population floor
- severe infrastructure collapse
- no transport
- current closure or inspection
- imminent enemy capture unless retreat crisis is intended

### Scenario matrix

| Scenario ID | Situation | Expected result |
| --- | --- | --- |
| `STATE_01_QUIET_SITE` | one eligible state already has quiet infrastructure | quiet site selected before new construction |
| `STATE_02_NON_CORE` | matched core and occupied non-core states, both logistically valid | non-core state preferred for occupation-deportation variant, not guaranteed for every policy |
| `STATE_03_CAPITAL_PROTECTION` | several valid states plus capital | capital has zero or near-zero score at baseline |
| `STATE_04_NO_TRANSPORT` | resource-rich state without route versus moderate state with rail | transported state selected unless a local-only variant explicitly supports the isolated site |
| `STATE_05_RELIEF_PROTECTION` | recently liberated state versus ordinary state | relief state zero |
| `STATE_06_ASSIGNMENT_MATCH` | industrial policy with factory state, mine state, and empty rural state | factory state dominates |
| `STATE_07_EXTERMINATION_CONVERSION` | valid target registry and several camp states | conversion selection favors target and transport conditions, not random core-state population |
| `STATE_08_HALF_COUNTRY_COVERAGE` | Evolution III with mixed valid states | target count exactly reaches rounded 50 percent, no duplicates, no invalid substitutions |
| `STATE_09_ODD_SPLIT` | final target count odd | concentration camps receive extra site unless explicit extermination-dominant route |
| `STATE_10_ALREADY_ABOVE_TARGET` | network already exceeds target because of country package | no site deletion and no forced downgrade |

## Surface E: Evolution I automatic conversion

| Scenario ID | Situation | Expected result |
| --- | --- | --- |
| `EVO1_01_TWO_SITES` | two valid concentration sites | one converts |
| `EVO1_02_THREE_SITES` | three valid concentration sites | exactly one converts because the rule uses `floor(3 / 2)` |
| `EVO1_03_ONE_SITE_MODERATE` | one site, no explicit extermination policy | no automatic conversion, crisis decision opens |
| `EVO1_04_ONE_SITE_EXTREME` | one site, explicit extermination route | site converts |
| `EVO1_05_CLOSING_EXCLUDED` | four sites, two closing | conversion count uses only two valid operational sites |
| `EVO1_06_GULAG_ADAPTER` | Soviet network includes gulags | generic conversion does not relabel gulags, adapter returns valid conversion set |
| `EVO1_07_NO_TARGET` | no valid target purpose | automatic conversion blocked or held as unresolved crisis according to route, with no invented target |
| `EVO1_08_SAVE_RELOAD` | evolution job saved between batches | final conversion count remains exact and no state converts twice |

The audit must inspect both count mathematics and state choice probability.

## Surface F: labour assignment choice

| Scenario ID | Situation | Expected ordering |
| --- | --- | --- |
| `LAB_01_FACTORY_STATE` | many factories, no resources, strong rail | industrial dominates |
| `LAB_02_RESOURCE_STATE` | major resource deposit, few factories | extraction dominates |
| `LAB_03_RECONSTRUCTION` | heavy damaged buildings and active construction | construction dominates |
| `LAB_04_FRONT_LOGISTICS` | supply bottleneck and active front nearby | logistics dominates if retreat risk remains acceptable |
| `LAB_05_NO_ROLE` | state has no meaningful role | every assignment zero and state cannot be selected |
| `LAB_06_WORKFORCE_LOW` | detained capacity near exhaustion | lower intensity or closure preferred over starting a new high-intensity assignment |
| `LAB_07_SUPPLY_FAILURE` | trains and support equipment below reserve floor | assignment start zero |
| `LAB_08_BOMBING` | high enemy bombing and damaged rail | construction or closure preferred, logistics and industrial score reduced |
| `LAB_09_FAMINE` | severe famine in site | relief or reduced quota dominates high intensity |
| `LAB_10_NETWORK_CAP` | national administration at assignment cap | no new assignment until capacity frees or administration improves |

## Surface G: intensity and continuation

### Expected-horizon test

AI should compare the expected benefit window with:

- workforce depletion time
- supply reserve
- front distance
- exposure threshold
- resistance threshold
- assignment objective duration

| Scenario ID | Situation | Expected result |
| --- | --- | --- |
| `INT_01_SHORT_WAR_WINDOW` | strong supply, full workforce, urgent 120-day war objective | exploitative AI can raise intensity |
| `INT_02_LONG_PEACE` | no urgent objective, moderate workforce | lower or standard intensity preferred |
| `INT_03_COLLAPSE_IN_60` | expected workforce collapse within 60 days | high intensity zero unless extremist liquidation logic applies |
| `INT_04_EXPOSURE_NEAR_VERIFY` | one pulse from public verification | reviewer lowers intensity, cover-up profile may conceal, extremist can continue with bounded chance |
| `INT_05_RESISTANCE_ARMED` | armed resistance threshold crossed | relief, guard response, or closure considered before increased quotas |

## Surface H: concealment, closure, and retreat

| Scenario ID | Situation | Expected ordering |
| --- | --- | --- |
| `COV_01_LOW_EXPOSURE_STABLE` | low Exposure and secure control | concealment decisions low priority |
| `COV_02_CREDIBLE_REPORT` | credible report, state secure, records intact | staged inspection or falsification can compete with real inspection according to profile |
| `COV_03_VERIFIED_SITE` | site already physically verified | falsification and access restriction lose most value, closure or evidence destruction becomes more likely |
| `COV_04_ENEMY_90_DAYS` | enemy projected near site in 90 days, transport available | supplied transfer, closure, and record action dominate ordinary operation |
| `COV_05_ENEMY_20_DAYS` | enemy almost at site, transport unavailable | closure in place or abandonment leads for moderate profiles, forced march or liquidation only for extreme profile |
| `COV_06_HUMANITARIAN_SUCCESSOR` | successor controls archives | preservation and disclosure over 90 percent combined |
| `COV_07_EXTREME_RETREAT` | extremist regime, extermination active, high cover-up effort | liquidation, forced evacuation, or destruction can lead, but at least one nonlethal closure path remains valid unless hard-locked by accepted route |
| `COV_08_CHEMICAL_SITE` | restricted chemical site threatened | deactivation and decontamination considered, destruction has contamination penalty, silent stockpile deletion forbidden |

## Surface I: discovery probability

Discovery should be event-driven. Probability applies to investigation outcomes, inspection deception, leak success, and evidence survival, not a blind global daily roll.

| Scenario ID | Situation | Expected result |
| --- | --- | --- |
| `DISC_01_LIBERATED_ACTIVE` | enemy takes active extermination site with survivors and records | site verification effectively certain after bounded processing |
| `DISC_02_DESTROYED_SITE` | site destroyed, no survivors, partial physical evidence | nonzero discovery with lower initial confidence |
| `DISC_03_MULTIPLE_WITNESSES` | independent survivors plus transport records | high chance to verify site and link network |
| `DISC_04_STAGED_INSPECTION_LOW_EVIDENCE` | strong cover-up, no witness, secure core state | staged inspection can delay verification |
| `DISC_05_STAGED_INSPECTION_CONTRADICTIONS` | foreign transport records and hidden relocation | failed staging materially more likely than success |
| `DISC_06_NATURAL_DISASTER` | disaster exposes graves or records | immediate state discovery attempt, no need for foreign intelligence score |
| `DISC_07_FOREIGN_INTELLIGENCE` | high intelligence access and repeated reports | investigation success higher than low-access peer |
| `DISC_08_ALREADY_DISCOVERED` | source already public | no duplicate source probability or value |

## Surface J: foreign reaction

Candidate reactions depend on confidence and shared Condemnation.

| Scenario ID | Situation | Expected ordering |
| --- | --- | --- |
| `FOR_01_RUMOUR` | fragmentary report only | investigation and witness protection lead, sanctions low |
| `FOR_02_VERIFIED_FORCED_LABOUR` | verified network, moderate deaths | censure, inspection, aid, and targeted restrictions compete |
| `FOR_03_VERIFIED_EXTERMINATION` | verified national extermination network | severe shared Condemnation reactions dominate |
| `FOR_04_ALLY_PERPETRATOR` | responsible country is close ally | reaction may be slower, but verified extreme evidence cannot produce zero response for every eligible government |
| `FOR_05_ENEMY_PROPAGANDA_ONLY` | enemy claim without corroboration | investigation preferred over immediate full sanction |
| `FOR_06_LIBERATOR_RELIEF` | ally controls liberated sites with survivors | relief and evidence cooperation lead |
| `FOR_07_RECEIVING_CAPACITY_LOW` | neighbor asked to receive survivors but lacks supply and housing | aid-in-place or limited admission can beat full reception |
| `FOR_08_PARIAH_ALREADY` | responsible country already above maximum shared threshold | Event 22 adds history and source without repeatedly applying the same top-tier restriction |

## Surface K: relief AI

| Scenario ID | Situation | Expected ordering |
| --- | --- | --- |
| `REL_01_MASS_MEDICAL` | high post-liberation mortality and disease | emergency relief first, evidence and demolition wait |
| `REL_02_RECORDS_AT_RISK` | survivors stable, records about to be destroyed | secure and preserve evidence lead |
| `REL_03_CONTAMINATION` | chemical contamination active | quarantine and decontamination lead, transfer blocked until safe |
| `REL_04_OVERCROWDING` | site secure, food stable, housing crisis | safe accommodation and resettlement lead |
| `REL_05_NO_DESTINATION` | transport exists but no receiving capacity | transfer zero, local relief continues |
| `REL_06_DOCUMENTED_COMPLETE` | survivors moved, evidence transferred, no contamination | dismantle site leads |
| `REL_07_REUSE_ATTEMPT` | new controller chooses forced labour | Liberator profile removed and new responsibility generation begins |

## Evolution sequence tests

### `SEQ_01_BASE_TO_EVO3`

Sequence:

1. baseline opening at 20 percent concentration camps
2. Evolution I converts 50 percent of valid sites
3. Evolution II applies 1 percent shock
4. Evolution III expands to 50 percent and applies 2 percent shock

Proof required:

- exact final reach
- no duplicate state
- no automatic downgrade
- each existing state receives each active-stage shock once
- newly added Evolution III sites receive only the 2 percent shock

### `SEQ_02_PREFIRE_EVO3`

Sequence:

1. no prior Event 22 state
2. first firing with Evolution III already available

Proof required:

- 50 percent reach
- roughly even split
- 2 percent shock once
- no 1 percent opening shock

### `SEQ_03_CONTROLLER_CHANGE_DURING_JOB`

Sequence:

1. large evolution job queued
2. state changes controller before its batch executes

Proof required:

- state revalidated
- shock and building action apply only under the accepted responsibility and operation rule
- no fallback target is silently selected

### `SEQ_04_SAVE_RELOAD`

Sequence:

1. event saved during delayed batch
2. reload
3. batch completes

Proof required:

- same selected states and counts
- no repeated shock
- no duplicate Condemnation source

### `SEQ_05_CIVIL_WAR_SPLIT`

Sequence:

1. network active
2. Event 21 splits country
3. both sides control sites

Proof required:

- original responsibility preserved
- later operation recorded separately
- profiles and categories load for each side
- no shock reapplication

## Sweep dimensions

Run sweeps across:

- eligible states: 1, 2, 3, 5, 10, 25, 50, 100
- baseline site count and existing quiet sites
- Network Reach: 0 to 50 percent
- Exposure: 0 to 100
- Resistance Pressure: 0 to 100
- stability: very low to very high
- war support: very low to very high
- front distance bands
- train, convoy, truck, support-equipment, and manpower reserves
- occupation share
- core versus non-core state mix
- famine and disease severity
- Evolution stage
- AI profile
- country-specific adapter present or absent

Review for abrupt inversions, impossible actions, one-option dominance, and candidate starvation.

## Starvation and overdominance guards

- Never-fired countries should not be permanently starved by high-weight repeat incidents.
- Relief actions should not be starved by evidence actions while survivors are dying.
- Closure must remain possible for a player and a valid AI even after an extreme route, unless a specific accepted country route creates an internal conflict mission first.
- Extermination must never receive nonzero probability without a valid target purpose.
- Cover-up should not dominate before evidence or defeat makes it relevant.
- High-intensity labour should not dominate when expected benefit duration is shorter than the setup cost or collapse time.
- One large country should not absorb most Event 22 firings through repeated incidents.
- Country-specific historical adapters should be meaningfully favored under their own conditions without making alternate history impossible.

## Required audit report fields

For each scenario, record:

- source surface
- scenario ID
- candidate pool
- external factors included
- evidence classification
- option or target scores
- normalized probability where exact
- expected ordering
- actual ordering
- dominance ratio
- zero-condition proof
- starvation finding
- pass, fail, or unresolved
- linked inspect, evaluate, sweep, sequence, simulate, compare, or render artifact
- patch required
- post-patch comparison result

Implementation is blocked when a required candidate pool or external factor cannot be reconstructed accurately.
