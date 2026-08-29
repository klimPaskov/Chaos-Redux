# Event 029: AI probability and timing scenarios

## Purpose

This file defines the named scenarios that the later implementation and `chaosx_ai_probability_auditor` must use.

The scenarios describe expected ordering, valid timing bands, dominance limits, and invalid-action suppression.

They do not claim exact selection probabilities.

A decision `ai_will_do` result is a willingness score, not a direct click probability.

The auditor must inspect the actual candidate pool, availability, costs, cooldowns, route memory, and external state before drawing conclusions.

## Required audit sequence

1. Run `hoi4.probability_inspect` on the exact event option, decision, MTTH, random list, target pool, or strategy surface.
2. Record whether the complete candidate pool and all external factors are known.
3. Run `hoi4.probability_evaluate` for the named scenarios below.
4. Run `hoi4.probability_sweep` across the important value ranges.
5. Use `hoi4.probability_simulate` only for explicitly declared uncertain inputs.
6. Use `hoi4.probability_render` for decision rankings, evolution timing, target matrices, sensitivity, and comparisons when useful.
7. After the implementation owner changes a weighted surface, run `hoi4.probability_compare` with the same scenario IDs and inputs.
8. Mark unresolved engine state as unresolved instead of inventing a probability.

## Surface A: Initial policy choice

Candidate policy families:

- Public Development
- State Extraction
- Concession Economy
- Militarized Mine
- Predatory Extraction

### `RF_POLICY_01_STABLE_DEMOCRACY`

State:

- stable democracy
- peace
- core-state mine
- adequate construction capacity
- good supply
- medium Mine Development
- moderate Local Order
- moderate Revenue Legitimacy
- no foreign emergency
- no evolution active

Expected ordering:

1. Public Development
2. State Extraction or regulated Concession Economy, depending on industry
3. Concession Economy
4. Militarized Mine
5. Predatory Extraction

Acceptance expectation:

Public Development should lead clearly without starving the two economically plausible alternatives.

Predatory Extraction should be negligible.

### `RF_POLICY_02_AUTHORITARIAN_MAJOR_AT_WAR`

State:

- fascist or military major
- major war
- mine is supplied and away from immediate enemy capture
- high war support
- strong industry
- moderate pressure
- no evolution active

Expected ordering:

1. State Extraction
2. Militarized Mine
3. Concession Economy through an aligned strategic partner
4. Public Development
5. Predatory Extraction

Acceptance expectation:

State Extraction and Militarized Mine should dominate.

Predatory Extraction can become material only when the war is going badly, receipts are critical, or the country has a personalist corruption profile.

### `RF_POLICY_03_POOR_MINOR`

State:

- poor minor
- low infrastructure
- low construction capacity
- peace
- valid foreign investor
- moderate legitimacy
- no immediate security threat

Expected ordering:

1. Limited Concession Economy or infrastructure-for-access
2. Slow Public Development
3. State Extraction
4. Militarized Mine
5. Predatory Extraction

Acceptance expectation:

The foreign route should lead because the country cannot build the site quickly alone.

An exclusive concession should not dominate when a limited contract is valid.

### `RF_POLICY_04_COLONIAL_OCCUPIER`

State:

- non-core mine
- low compliance
- meaningful resistance
- foreign or colonial controller
- moderate enemy threat
- low legitimacy

Expected ordering:

1. Militarized Mine or local revenue settlement, depending on controller strategy
2. State Extraction
3. Concession Economy
4. Public Development
5. Predatory Extraction

Acceptance expectation:

The score should be sensitive to expected occupation duration.

A long-term controller should value local sharing more than a controller expecting imminent loss.

## Surface B: Development project selection

Candidate projects:

- Rail Spur
- Port and Convoy Route
- Drain and Reinforce Shafts
- Processing Works
- Worker Housing and Services
- Development Fund
- Drive Deeper

### `RF_DEV_01_INLAND_DEEP_REEF`

State:

- inland deep gold reef
- no adequate rail
- low development
- moderate pressure
- safe local order

Expected ordering:

1. Rail Spur
2. Drain and Reinforce Shafts
3. Worker Housing and Services or Processing Works
4. Development Fund
5. Drive Deeper
6. Port and Convoy Route at zero because geography is invalid

### `RF_DEV_02_ISLAND_GEMSTONE`

State:

- island gemstone field
- controlled port
- weak convoy route
- high smuggling
- low order

Expected ordering:

1. Port and Convoy Route
2. Camp administration or security prerequisite outside the project pool
3. Processing Works or secure assay project
4. Worker Housing and Services
5. Rail Spur at zero unless a verified internal rail route exists
6. Drive Deeper low while order is weak

### `RF_DEV_03_COLLAPSE_WARNING`

State:

- mature mine
- high pressure
- high collapse risk
- damaged drainage
- positive long-term value

Expected ordering:

1. Drain and Reinforce Shafts
2. Temporary closure or repair action outside the development pool
3. Restore transport if damaged
4. Worker Housing and Services
5. Processing Works
6. Drive Deeper at zero or near zero

## Surface C: Revenue policy

Candidate actions:

- Citizens' Dividend
- Earmark Local Revenue
- Centralize Treasury Receipts
- Stabilization Fund
- Worker or Community Participation
- Tolerate Patronage

### `RF_REV_01_HIGH_LEGITIMACY_DEMOCRACY`

Expected ordering:

1. Citizens' Dividend or Stabilization Fund
2. Earmark Local Revenue
3. Worker or Community Participation
4. Centralize Treasury Receipts
5. Tolerate Patronage

### `RF_REV_02_WARTIME_FINANCIAL_CRISIS`

Expected ordering:

1. Centralize Treasury Receipts
2. Stabilization Fund withdrawal only when a valid stored reserve exists
3. Reduced local settlement
4. Citizens' Dividend
5. Tolerate Patronage unless the regime is personalist

### `RF_REV_03_LOW_LEGITIMACY_NON_CORE`

Expected ordering:

1. Earmark Local Revenue
2. Worker or Community Participation
3. Citizens' Dividend
4. Stabilization Fund
5. Centralize Treasury Receipts
6. Tolerate Patronage

Acceptance expectation:

Local sharing should overtake centralization as resistance and legitimacy pressure rise.

## Surface D: Foreign concession target pool

Target factors:

- distance
- border or port access
- major-power status
- industry
- relations
- faction alignment
- ideology
- strategic need
- rival involvement
- existing concessions
- convoys
- controller invitation
- mine crisis

### `RF_FOREIGN_01_NEAR_ALLIED_MAJOR`

Expected result:

A nearby allied industrial major with access and good relations should outrank a distant neutral major.

### `RF_FOREIGN_02_DISTANT_NAVAL_POWER`

Expected result:

A distant naval power can rank well for a coastal or island mine when it has convoys and strategic interest.

It should rank poorly for an inland mine without transit.

### `RF_FOREIGN_03_HOSTILE_RIVAL`

Expected result:

A hostile rival should have zero or near-zero weight for a normal cooperative concession.

It can have separate weight for sabotage, claimant support, or coercive pressure when those actions are valid.

### `RF_FOREIGN_04_EXISTING_EXCLUSIVE_CONCESSION`

Expected result:

All new exclusive-concession candidates should be invalid.

Limited technical or repair agreements should remain possible only when compatible with the existing contract.

## Surface E: Security response

Candidate actions:

- Mine Police
- Private Guards
- Army Cordon
- Arm Workers
- Negotiate Truce
- Clear Barricades
- Temporary Closure

### `RF_SEC_01_CIVILIAN_CRIME`

State:

- peace
- moderate crime
- high legitimacy
- no armed claimant group

Expected ordering:

1. Mine Police
2. Camp administration or licensing support
3. Private Guards
4. Army Cordon
5. Arm Workers
6. Clear Barricades invalid

### `RF_SEC_02_ARMED_RAID_WARTIME`

State:

- war
- border mine
- supplied divisions present
- active raid mission

Expected ordering:

1. Army Cordon
2. Escort Pay Train or route defense
3. Mine Police
4. Private Guards
5. Negotiate Truce depending on actor
6. Arm Workers

### `RF_SEC_03_WORKER_CLAIM_WAR`

State:

- armed workers or claimants control an entrance
- medium legitimacy
- government lacks overwhelming force

Expected ordering:

1. Negotiate Truce or Claims Court
2. Mine Police if still valid
3. Army Cordon
4. Clear Barricades
5. Private Guards

A military or fascist government can reverse the middle ordering.

### `RF_SEC_04_PRIVATE_ENCLAVE`

State:

- private guards
- low legitimacy
- high private-security autonomy
- government has regular forces

Expected ordering:

1. Disarm Private Forces or negotiated buyout
2. Replace administration
3. Army Cordon
4. Accept enclave authority only for weak or dependent governments

## Surface F: Evolution I MTTH

Base target: Roughly 90 days once core conditions are met.

### `RF_EVO1_01_MANAGED_MINE`

State:

- chaos 600
- moderate pressure
- high legitimacy
- high order
- public contract or state terms
- stabilization route

Expected timing:

Longer than the base band, potentially several hundred days or effectively starved while management remains strong.

### `RF_EVO1_02_CAPTURED_CONCESSION`

State:

- chaos 600
- high pressure
- low legitimacy
- exclusive concession
- private guards
- failed audit

Expected timing:

Shorter than the base band.

The evolution should usually enter before a full year if the state remains unchanged.

### `RF_EVO1_03_MULTIPLE_MINES`

State:

- chaos 600
- controller has three mines
- aggregate dependence high
- mixed local conditions

Expected timing:

The most corrupt or dependent mine should receive the highest entry score.

The system should not trigger the evolution on every mine on the same day.

## Surface G: Evolution II MTTH

### `RF_EVO2_01_HIGH_PRESSURE_GEMSTONE`

State:

- chaos 800
- high pressure
- gemstone field
- private guards
- repeated theft incidents
- low order

Expected timing:

Clearly shorter than the base band.

### `RF_EVO2_02_SHARED_REVENUE_CONTROLLED_ACCESS`

State:

- chaos 800
- moderate pressure
- trusted revenue sharing
- high order
- controlled shifts

Expected timing:

Longer than base and capable of remaining inactive.

### `RF_EVO2_03_CLOSED_MINE`

State:

- chaos 800
- temporary closure
- no exposed workforce or shipments

Expected timing:

Evolution entry should be blocked or heavily suppressed until the mine reopens or a specific concealed-material incident occurs.

## Surface H: Evolution III MTTH

### `RF_EVO3_01_AGGRESSIVE_DEEP_MINE`

State:

- chaos 1,000
- high pressure
- repeated Drive Deeper
- high development
- recent mine deaths
- opened or unstable deep section

Expected timing:

Shorter than base.

### `RF_EVO3_02_PARTIALLY_SEALED`

State:

- chaos 1,000
- moderate pressure
- deep sections sealed
- strong integrity
- no recent violence

Expected timing:

Longer than base or blocked while the seal remains intact.

### `RF_EVO3_03_GOLD_DISEASE_MASS_VIOLENCE`

State:

- chaos 1,000
- Gold Disease active
- recent massacre or collapse
- high deep-excavation pressure

Expected timing:

The supernatural evolution should receive a major acceleration.

The result must not be instantaneous merely from the death transaction unless the event chain deliberately treats that incident as the reveal.

## Surface I: Gold Disease crisis response

Candidate actions:

- Revenue Sharing
- Controlled Access
- Workforce Replacement
- Military Control
- Quarantine
- Temporary Closure
- Seal Deep Sections

### `RF_GOLD_01_STABLE_HIGH_LEGITIMACY`

Expected ordering:

1. Revenue Sharing
2. Controlled Access
3. Temporary Closure
4. Seal Deep Sections
5. Workforce Replacement
6. Quarantine
7. Military Control

### `RF_GOLD_02_AUTHORITARIAN_WARTIME`

Expected ordering:

1. Military Control or Controlled Access
2. Workforce Replacement
3. Seal Deep Sections
4. Quarantine
5. Temporary Closure
6. Revenue Sharing

### `RF_GOLD_03_COLLAPSE_IMMINENT`

Expected ordering:

1. Temporary Closure
2. Evacuation
3. Seal Deep Sections
4. Quarantine
5. Revenue Sharing
6. Continued extraction at zero unless a desperation override is explicitly valid

## Surface J: Demonic response

Candidate actions:

- Permanent Sealing
- Evacuation
- Scientific Assistance
- Religious Assistance
- Occult Assistance
- Military Purge
- Controlled Exploitation
- Agreement

### `RF_DEMON_01_STABLE_DEMOCRACY_PEACE`

Expected ordering:

1. Scientific Assistance or Religious Assistance based on country context
2. Evacuation
3. Permanent Sealing
4. Controlled Exploitation only after evidence supports it
5. Occult Assistance
6. Military Purge
7. Agreement at negligible weight

### `RF_DEMON_02_COLLAPSING_AUTHORITARIAN_WAR`

Expected ordering:

1. Controlled Exploitation or Military Purge
2. Agreement
3. Scientific or Occult Assistance
4. Permanent Sealing
5. Evacuation
6. Religious Assistance depending on regime context

The Agreement should become material only when mine dependence and war desperation are high.

### `RF_DEMON_03_EVACUATION_COMPLETE`

Expected ordering:

1. Permanent Sealing
2. Bound-terms containment when available
3. Controlled upper workings
4. Agreement low
5. Military Purge invalid when no hostile group remains

## Surface K: The Gilded Sovereignty response

Candidate actions:

- Revoke Charter
- Buy Back District
- Share Sovereignty
- Recognize Local Board
- Violent Nationalization
- Let It Govern

### `RF_GILDED_01_WEALTHY_REFORMIST`

Expected ordering:

1. Buy Back District or Recognize Local Board
2. Revoke Charter
3. Share Sovereignty
4. Violent Nationalization
5. Let It Govern

### `RF_GILDED_02_WEAK_DEPENDENT_STATE`

Expected ordering:

1. Share Sovereignty or Let It Govern
2. Recognize Local Board
3. Buy Back District
4. Revoke Charter
5. Violent Nationalization

### `RF_GILDED_03_MILITARY_MAJOR`

Expected ordering:

1. Revoke Charter or Violent Nationalization
2. Buy Back District
3. Share Sovereignty
4. Recognize Local Board
5. Let It Govern

The violent route must account for mine damage, deaths, foreign backing, and relative force.

## Surface L: The Bottomless Account response

Candidate actions:

- Close Account
- Bind Terms
- Pay in Material
- Spend Authority
- Accept Predatory Prosperity

### `RF_ACCOUNT_01_STABLE_STATE`

Expected ordering:

1. Close Account or Bind Terms
2. Pay in Material
3. Spend Authority
4. Accept Predatory Prosperity at negligible weight

### `RF_ACCOUNT_02_DESPERATE_WAR_STATE`

Expected ordering:

1. Pay in Material or Accept Predatory Prosperity
2. Spend Authority
3. Bind Terms
4. Close Account

The predatory route should still remain bounded by visible benefit and breach risk.

### `RF_ACCOUNT_03_LOW_STABILITY_HIGH_DEPENDENCE`

Expected ordering:

1. Spend Authority or Accept Predatory Prosperity for personalist and authoritarian profiles
2. Pay in Material when stockpiles exist
3. Bind Terms
4. Close Account

A democracy with the same numbers should rank Close Account and Bind Terms higher.

## Surface M: Incident random lists

Every incident pool must be inspected with its complete candidate list.

Required pools include:

- claims incidents
- rush incidents
- development setbacks
- corruption incidents
- foreign interference
- raids
- collapse severity
- Gold Disease incidents
- supernatural incidents
- contract outcomes

Acceptance expectations:

- no candidate with an invalid target receives positive weight
- common low-severity incidents do not starve major but plausible incidents forever
- catastrophic results require severe state and should remain rare
- repeated identical incidents use memory or cooldown to prevent spam
- a mine under good management still receives occasional flavor and minor problems
- high pressure changes the pool visibly without guaranteeing the same crisis every time

## Surface N: Repeat recipient selection

Candidate countries are all valid ordinary countries with at least one suitable state.

Expected factors:

- every valid recipient country receives the same country-selection weight
- existing Event 029 mine count does not change the country-selection weight
- country size, major status, ideology, faction, and player control do not change the country-selection weight
- a country with no suitable state has zero weight and shows `N/A`
- the selected state uses its separate suitability weighting after the country has been chosen

## Required comparison evidence

Every weighted patch should return:

- scenario ID
- inspected source surface
- pre-change result
- post-change result
- expected ordering
- actual ordering
- rank reversals
- starvation or dominance finding
- unresolved inputs
- whether availability and cost were included
- rendered artifact URI when used
- source revision or comparison identifier

A passing audit means the scenarios behave in the intended order and invalid actions remain suppressed.

It does not mean the event is fully balanced in live play.
