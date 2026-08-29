# Event 22 Concentration Camps Decision and Mission Map

## Ownership

Working category identifiers:

- `chaosx_022_camp_network_management`
- `chaosx_022_liberated_site_relief`

The first category belongs to the responsible, successor, or continuing operator. The second belongs to a controller that has stopped operation and is managing liberated or abandoned sites.

Country-specific German, Japanese, and Soviet categories replace overlapping generic rows through adapters. They must call the same public Event 22 state, responsibility, population, evidence, and cleanup helpers.

All identifiers in this file are working script labels, not final localisation.

## Category lifecycle

### Management mode

Possible modes:

- opening policy
- restrictive review
- closure
- forced labour
- security expansion
- extermination
- exposure emergency
- retreat emergency
- successor decision

The category shows only decisions valid for the current mode. A country can have one primary national policy and several state statuses, but the visible action count should remain between three and five in normal play. Six is the hard maximum.

### Relief mode

The relief category appears only when the current country controls at least one liberated, abandoned, destroyed, or recently closed site that still has survivors, disease, contamination, evidence, or displacement work.

It shows one to three regional missions plus urgent state actions. It closes when all controlled sites reach a stable aftermath state.

## Dynamic cost rules

Every decision can use at most four spendable cost types. Requirements such as controlling a state, having rail access, or fielding a division do not count as spendable costs.

Cost families:

- political or administrative capacity
- command power
- army experience
- manpower commitment
- support equipment
- infantry equipment
- trucks
- trains
- convoys
- fuel
- civilian-factory burden
- stability or war support loss
- detained workforce
- evidence or exposure risk as a consequence, not a hidden spendable cost

Final cost localisation must use amount plus matching texticon. Do not write literal resource labels inside the cost string.

Dynamic scaling factors:

- site count
- detained capacity
- state distance and transport route
- current war
- front distance
- network reach
- exposure
- resistance pressure
- site type
- contamination or disease
- previous failures
- country size and economy

## Opening policy event options

These event options initialize the category. They are not persistent decisions.

| Working option | Validity | Immediate commitment | Category mode | Main consequence |
| --- | --- | --- | --- | --- |
| `chaosx_022_open_close` | always valid unless a country-specific route blocks central authority | political and administrative burden | closure | freezes intake and opens regional closure missions |
| `chaosx_022_open_review` | always valid for a functioning government | political capacity and inspectors | restrictive review | pauses expansion and harsh assignments while cases are reviewed |
| `chaosx_022_open_labour` | valid when at least one state has a real assignment role | trains or convoys, guards, support equipment | forced labour | opens state assignments and starts workforce depletion |
| `chaosx_022_open_expand` | valid when eligible uncovered states remain and political route permits repression | construction burden, support equipment, manpower | security expansion | opens targeted expansion decisions |
| `chaosx_022_open_extermination` | Evolution I plus valid target purpose and explicit extremist or country route | transport, guards, political commitment | extermination | accepts the evolved opening and starts killing policy |

AI ordering is defined in the probability matrix. The opening must not show an extermination option merely because Evolution I exists if no valid target purpose or route exists.

## National management decisions

### `chaosx_022_freeze_intake`

Role: closure or review opener.

Visible when:

- at least one active site still accepts detainees
- current policy is not already frozen

Spendable costs:

- political capacity
- temporary stability loss when hardliner power is high

Requirements:

- functioning national authority or a valid regional closure actor

Duration:

- immediate policy change with a short administrative cooldown

Public outcome:

- stops normal intake
- closes expansion and deportation decisions
- reduces future mortality pressure
- starts assignment wind-down

Risks:

- underground administrators may disobey
- hardliners may challenge the government

AI:

- high for Dismantler and Liberator
- medium for Restrictive Reviewer
- near zero for active Extermination Extremist unless defeat is imminent

Cleanup:

- replaced by `chaosx_022_resume_intake` only for routes that legally allow continuation
- removed after transparent closure

### `chaosx_022_place_network_under_review`

Role: move from exploitation or expansion into restrictive review.

Visible when:

- network active
- no binding extermination order remains

Spendable costs:

- political capacity
- civilian-factory burden for inspectors and administration

Public outcome:

- pauses new expansion
- lowers assignment intensity
- opens registration, ration, and inspection actions
- raises short-term Exposure because records become accessible

Risks:

- local noncompliance
- staged review can become a cover-up if access is restricted

AI:

- high for Restrictive Reviewer
- moderate for a weak Exploitative Authoritarian after exposure or labour collapse

### `chaosx_022_resume_coercive_operation`

Role: leave review and return to detention or labour.

Visible when:

- network under review
- valid target source remains
- no transparent closure lock
- route permits arbitrary detention

Spendable costs:

- political capacity
- stability

Public outcome:

- reopens intake or assignments
- ends some review benefits

Risks:

- sharp Exposure increase if inspectors or records already exist
- stronger internal opposition

AI:

- only Exploitative Authoritarian or Extermination Extremist

### `chaosx_022_centralize_administration`

Role: coordinate a large network.

Visible when:

- at least a regional network exists
- not already centralized

Spendable costs:

- political capacity
- civilian-factory burden
- support equipment or communications abstraction

Duration:

- medium project

Public outcome:

- lowers duplicate transport and administrative disorder
- improves consistent policy application
- raises effective national assignment cap

Risks:

- creates strong documentary linkage
- raises later network-verification severity
- creates an administrator institution for accountability

AI:

- high for exploitative and extremist profiles with several sites
- low for Dismantler

### `chaosx_022_decentralize_or_dissolve_administration`

Role: break the central network during closure or succession.

Spendable costs:

- political capacity
- temporary output loss

Public outcome:

- reduces national coordination
- lowers ability to expand or run intense assignments
- makes regional closure easier

Risks:

- local administrators may continue covertly
- records can fragment

### `chaosx_022_seize_confiscated_property`

Role: temporary exploitative budget and supply action.

Visible when:

- active detention intake or existing confiscation evidence
- not already used in the current network generation for the target region

Spendable costs:

- political capacity

Public outcome:

- temporary equipment, supply, or budget relief scaled to valid records

Risks:

- corruption
- black market
- evidence
- later restitution burden

Exploit controls:

- one bounded use per regional intake generation
- no permanent factories or resources
- cannot create value after the detained capacity is exhausted

## Closure and review decisions

### `chaosx_022_restore_food_and_medicine`

Scope: selected camp state or regional closure group.

Visible when:

- active, closing, or recently liberated site has poor ration, medical, or disease status

Spendable costs:

- trucks or trains
- support equipment
- civilian-factory burden

Requirements:

- valid supply route or accepted air or convoy route

Duration:

- short delivery project with repeat cooldown

Public outcome:

- lowers mortality and disease
- improves detained or survivor condition
- lowers Resistance Pressure

Risks:

- convoy or rail loss in war
- administrator theft

AI:

- high for Dismantler, Reviewer, and Liberator
- low for Extermination Extremist

### `chaosx_022_register_detainees`

Scope: state or region.

Spendable costs:

- political capacity
- civilian-factory burden

Public outcome:

- improves release, transfer, and family tracing
- reduces missing-person confusion
- raises evidence confidence

Risks:

- responsible regime may fear exposure
- records can be stolen or destroyed

Completion:

- state gains registered-population status
- cannot be repeated unless a later intake generation occurred

### `chaosx_022_open_site_to_inspection`

Scope: selected site.

Requirements:

- current policy allows review
- no active killing order at the state

Spendable costs:

- political capacity
- temporary local output loss

Public outcome:

- inspectors gain real access
- improves conditions while active
- can support transparent closure

Risks:

- raises Exposure when evidence exists
- staged access creates cover-up evidence if witnesses are hidden or moved

### `chaosx_022_reduce_labour_quota`

Scope: selected forced-labour site.

Spendable costs:

- temporary local output loss

Public outcome:

- lowers mortality, disease, and sabotage
- extends detained-workforce duration

AI:

- Reviewer and Exploitative Authoritarian use it when workforce or supply is near collapse

### `chaosx_022_begin_regional_closure`

Scope: one generated region containing one or more sites.

Requirements:

- intake frozen
- no active extermination or restricted chemical order in the region
- valid controller

Spendable costs:

- political capacity
- support equipment
- trucks or trains
- civilian-factory burden

Duration:

- long mission scaled by site count and condition

Public outcome:

- secures sites
- supplies detainees
- registers people
- preserves or transfers records
- releases or relocates survivors
- removes buildings after all subconditions are met

Failure:

- covert operation continues
- records disappear
- disease or disorder rises
- closure progress partially resets

AI:

- high for Dismantler
- moderate for successor disclosure

### `chaosx_022_preserve_records_for_investigation`

Scope: state or central archive.

Spendable costs:

- political capacity
- temporary security commitment

Public outcome:

- protects evidence
- supports transparent closure and tribunal

Risks:

- hardliner sabotage
- foreign exposure

### `chaosx_022_release_or_transfer_survivors`

Scope: state.

Requirements:

- registered detainees or a safe bounded estimate
- safe destination
- transport if destination differs

Spendable costs:

- trucks, trains, or convoys
- civilian-factory burden
- support equipment

Public outcome:

- reduces detained capacity without deaths
- creates return, family, or displacement outcome

Blocked when:

- destination unsafe
- active epidemic without medical transport
- current country intends continued extermination

## Forced-labour assignment decisions

Only one assignment can be active in a state.

### `chaosx_022_assign_industrial_labour`

Requirements:

- active concentration camp
- meaningful civilian or military factory base
- rail or local transport
- sufficient workforce and guards

Spendable costs:

- trains
- support equipment
- manpower commitment
- civilian-factory burden

Duration:

- timed assignment with pulse-based continuation

Public outcome:

- strong local factory-output increase
- possible production-efficiency recovery support

Risks:

- deaths
- accident
- sabotage
- workforce depletion
- evidence

Cleanup:

- ends on conversion, closure, liberation, workforce exhaustion, or supply failure

### `chaosx_022_assign_construction_labour`

Requirements:

- active construction, repair, railway, infrastructure, fort, airbase, factory, or supply project in the state or region

Spendable costs:

- support equipment
- trucks or trains
- manpower commitment
- civilian-factory burden

Public outcome:

- strong local construction and repair increase

Risks:

- injury deaths
- project failure
- bombing exposure
- infrastructure damage after exhaustion

### `chaosx_022_assign_extraction_labour`

Requirements:

- relevant resource, mine, forest, quarry, plantation, or agricultural role

Spendable costs:

- support equipment
- trucks or trains
- manpower commitment
- fuel when mechanized support is used

Public outcome:

- strong local resource-output increase

Risks:

- severe mortality in harsh terrain
- corruption
- environmental or infrastructure damage
- depleted workforce

### `chaosx_022_assign_logistics_labour`

Requirements:

- rail, supply hub, port, airbase logistics, or front-support role

Spendable costs:

- trains or convoys
- trucks
- support equipment
- manpower commitment

Public outcome:

- rail repair, depot handling, port labour, or supply support

Risks:

- strongest front exposure
- transport deaths
- forced evacuation crisis

### `chaosx_022_raise_assignment_intensity`

Scope: selected forced-labour state.

Spendable costs:

- additional guard manpower
- support equipment
- transport

Public outcome:

- stronger short-term assignment effect

Risks:

- nonlinear increase in deaths, disease, sabotage, evidence, and exhaustion

Limits:

- one intensity increase at a time
- blocked at workforce or supply danger threshold
- AI must understand the expected operating horizon

### `chaosx_022_lower_assignment_intensity`

Public outcome:

- lowers output
- reduces mortality and collapse pressure
- no spendable cost beyond lost output

## Security and expansion decisions

### `chaosx_022_expand_network_into_state`

Scope: targeted eligible uncovered state.

Requirements:

- below current reach cap
- valid target source
- policy permits expansion
- state passes eligibility

Spendable costs:

- civilian-factory burden
- support equipment
- manpower commitment
- trains or convoys

Duration:

- construction and transfer project

Public outcome:

- adds concentration camp
- registers responsibility and generation
- initializes detained capacity
- raises Network Reach

Risks:

- Exposure
- Resistance Pressure
- transport incident

### `chaosx_022_reinforce_guard_system`

Scope: state or region.

Spendable costs:

- manpower commitment
- support equipment
- command power

Public outcome:

- lowers immediate escape and sabotage chance

Risks:

- army or garrison weakness elsewhere
- abuse and evidence under violent policy
- long-term pressure remains

### `chaosx_022_import_detainees`

Scope: destination camp state plus valid source region.

Requirements:

- valid target source
- destination capacity
- transport route

Spendable costs:

- trains or convoys
- guards or manpower
- support equipment
- political capacity

Public outcome:

- transfers detained capacity to destination
- can restore a depleted labour assignment

Risks:

- deportation deaths
- escape
- bombing
- Exposure
- source-state resistance

Exploit controls:

- actual source capacity is reduced
- no source marker means no intake
- conversion or repeated clicking cannot create population

### `chaosx_022_suppress_resistance_network`

Scope: selected camp state.

Possible methods are expressed through event outcome, not separate duplicate decisions:

- relief and de-escalation
- guard and intelligence action
- violent repression

Spendable costs vary by method and remain under four types.

Public outcome:

- resolves the immediate mission

Long-term result:

- relief lowers underlying pressure
- security action delays the next incident
- violent repression raises deaths and evidence

## Concealment decisions

### `chaosx_022_restrict_foreign_access`

Spendable costs:

- political capacity
- relations or intelligence openness as a consequence

Public outcome:

- lowers immediate foreign-observer pressure

Risks:

- suspicion
- diplomatic damage
- ineffective in open or contested states

### `chaosx_022_falsify_camp_records`

Spendable costs:

- political capacity
- administrative capacity

Public outcome:

- chance to reduce immediate Exposure

Risks:

- creates cover-up evidence
- contradictions with transport and factory records
- whistleblower incident

AI:

- Cover-up Escalator weighs current Exposure, confidence, and expected state loss

### `chaosx_022_destroy_records`

Scope: selected archive or state.

Spendable costs:

- political capacity
- security commitment

Public outcome:

- destroys one evidence component

Risks:

- cover-up evidence
- harder survivor tracing
- administrator conflict
- later physical evidence remains

One-time:

- each archive or state record source can be destroyed once

### `chaosx_022_stage_inspection`

Requirements:

- foreign inspection request
- operator still controls the state

Spendable costs:

- political capacity
- trains or trucks for relocation
- administrative capacity

Public outcome:

- chance to delay site verification

Risks:

- moved detainees can die or escape
- inspectors can discover inconsistencies
- failed staging creates a larger cover-up source

### `chaosx_022_abandon_site`

Scope: selected threatened or unsupplied state.

Spendable costs:

- loss of operation and later consequences

Public outcome:

- stops organized operation
- leaves state in abandoned status

Risks:

- relief deaths
- rapid discovery
- guard and survivor disorder

## Evolution I decisions

### `chaosx_022_convert_site_to_extermination`

Requirements and effects follow Part 3.

Spendable costs:

- trains or convoys
- support equipment
- manpower commitment
- political capacity

Public outcome:

- conversion
- forced-labour assignment removed
- death pressure and evidence rise

### `chaosx_022_set_target_purpose`

Scope: national policy.

Requirements:

- at least one valid target-purpose registry entry
- explicit route support

Spendable costs:

- political capacity
- stability

Public outcome:

- selects one valid campaign target purpose
- unlocks extermination intensity decisions

No menu entry can represent an invented ethnicity.

### `chaosx_022_raise_extermination_intensity`

Spendable costs:

- guards or manpower
- transport
- support equipment

Public outcome:

- severe death increase
- temporary hardliner or security control

Risks:

- rapid target depletion
- resistance
- military objection
- exposure
- collapse

### `chaosx_022_halt_extermination`

Spendable costs:

- political capacity
- stability under hardliner rule

Public outcome:

- stops killing pulse
- starts secure detention and relief transition

Risks:

- coup or underground continuation

### `chaosx_022_activate_restricted_chemical_site`

Requirements:

- valid technology and project gates
- available stockpile
- eligible extermination site
- capacity below cap

Spendable costs:

- agent stockpile
- support equipment
- specialist manpower or command abstraction
- transport

Public outcome:

- starts stockpile-backed restricted operation

Risks:

- severe deaths
- contamination
- accident
- source-specific evidence

Operation stops automatically when stockpile debit fails.

### `chaosx_022_broaden_purge_inward`

Requirements:

- earlier target source exhausted or inaccessible
- core population available above protected floor
- extreme route remains committed

Spendable costs:

- stability
- war support
- political capacity

Public outcome:

- permits domestic-core intake
- temporary security hardliner effect

Risks:

- officer, party, factory, and administrative collapse
- civil-war and terror links
- severe resistance

## Emergency retreat decisions

These replace ordinary management for the threatened state.

### `chaosx_022_close_and_await_liberation`

Spendable costs:

- political or command capacity
- support equipment for basic supply

Public outcome:

- stops operation
- leaves survivors in place
- preserves evidence

### `chaosx_022_order_supplied_transfer`

Requirements:

- valid receiving site or safe destination
- real transport and food route

Spendable costs:

- trains, convoys, or trucks
- support equipment
- guards or manpower
- fuel

Public outcome:

- transfers population with bounded survival chance

Risks:

- bombing, disease, escape, and Exposure

### `chaosx_022_force_evacuation_on_foot`

Requirements:

- retreat emergency
- extreme or cover-up route

Spendable costs:

- guards or manpower
- support equipment

Public outcome:

- starts route mission

Risks:

- severe deaths
- escape
- witnesses
- linked-state evidence

### `chaosx_022_liquidate_remaining_detainees`

Requirements:

- active extermination or extreme cover-up route
- detainees remain

Spendable costs:

- guards or manpower
- political capacity

Public outcome:

- immediate exact loss

Risks:

- strongest evidence and internal collapse pressure

### `chaosx_022_destroy_site_and_records`

Spendable costs:

- support equipment or explosives abstraction
- manpower commitment
- political capacity

Public outcome:

- damages or removes physical operation

Risks:

- deaths
- destroyed-site evidence
- contamination
- failed cover-up

The script must not include procedural demolition instructions in localisation.

## Management missions

### `chaosx_022_mission_prevent_escape`

Typical duration: medium.

Starts when:

- Resistance Pressure and local escape network cross threshold

Success paths:

- relief and reduced underlying pressure
- security containment with increased burden
- violent suppression with deaths and evidence

Failure:

- population escape
- testimony
- resistance growth
- possible foreign discovery

### `chaosx_022_mission_contain_epidemic`

Typical duration: medium to hard.

Requirements for success:

- food
- medicine abstraction
- transport
- sanitation or medical support

Failure:

- disease deaths
- spread to nearby state
- abandonment or escape
- discovery

### `chaosx_022_mission_keep_site_from_enemy`

Typical duration: short emergency.

Ends when:

- site closes
- population transfers
- site is abandoned
- site is liberated
- operator retains secure control beyond the emergency window

Failure is determined by the selected retreat policy, not one generic penalty.

### `chaosx_022_mission_complete_regional_closure`

Typical duration: long.

Objective components:

- stop intake
- supply sites
- register detainees
- preserve records
- release or transfer people
- remove operation

Partial success should preserve completed components.

### `chaosx_022_mission_underground_network`

Starts when local administrators resist national closure.

Player paths:

- prosecute operators
- negotiate surrender
- restore central coercive control
- expose the network publicly

Failure:

- covert deaths continue
- records disappear
- local armed resistance grows

## Liberated-site relief decisions

### `chaosx_022_secure_liberated_site`

Spendable costs:

- manpower or temporary division commitment
- support equipment
- command power

Public outcome:

- ends guard violence and looting risk
- protects survivors and records

### `chaosx_022_deliver_emergency_relief`

Spendable costs:

- trucks or trains
- support equipment
- civilian-factory burden

Public outcome:

- lowers post-liberation mortality
- improves medical and food status

### `chaosx_022_quarantine_and_decontaminate`

Requirements:

- disease or contamination

Spendable costs:

- support equipment
- trucks
- civilian-factory burden
- fuel where decontamination uses it

Public outcome:

- contains spread
- starts a humane, time-limited medical mission

### `chaosx_022_register_survivors_and_missing`

Spendable costs:

- political capacity
- civilian-factory burden

Public outcome:

- improves tracing and evidence
- unlocks return or resettlement

### `chaosx_022_preserve_liberated_evidence`

Spendable costs:

- security commitment
- political capacity

Public outcome:

- protects physical and documentary proof
- supports network verification

### `chaosx_022_transfer_to_safe_accommodation`

Spendable costs:

- trucks, trains, or convoys
- support equipment
- civilian-factory burden

Requirements:

- receiving capacity
- safe route

Public outcome:

- reduces local overcrowding
- creates migration or resettlement status

### `chaosx_022_dismantle_documented_site`

Requirements:

- survivors moved or safely housed
- evidence complete or transferred
- no contamination blocker

Spendable costs:

- civilian-factory burden
- support equipment

Public outcome:

- removes physical camp building
- retains historical evidence and aftermath status

## Relief missions

### `chaosx_022_mission_emergency_survival`

Typical duration: 90 to 120 days.

Objective:

- keep post-liberation mortality below a dynamic threshold through food, medicine, security, and transport

### `chaosx_022_mission_trace_and_reunite`

Typical duration: 120 to 180 days.

Objective:

- register a required share of survivors and provide safe destinations

### `chaosx_022_mission_document_network`

Typical duration: 120 to 240 days depending on destroyed evidence and site count.

Objective:

- preserve several evidence categories and link responsible institutions

### `chaosx_022_mission_regional_resettlement`

Typical duration: 180 to 365 days.

Objective:

- move survivors into stable housing, return, or accepted resettlement without creating a new humanitarian crisis

## Foreign-reaction adapters

Event 22 should expose triggers and effects to the shared Condemnation or diplomacy categories for:

- investigate credible reports
- protect witnesses
- share intelligence
- demand inspection
- receive survivors
- fund relief
- impose or support shared sanctions
- cooperate with tribunal

These are adapters, not duplicate Event 22 decisions. The owning systems define their final costs and visibility.

## Decision replacement rules

- `freeze_intake` disappears after intake is frozen.
- forced-labour assignment choices disappear after state conversion to extermination.
- expansion disappears at the current reach cap.
- concealment decisions close after the operator loses control, except remote evidence-destruction hooks already in progress.
- retreat decisions appear only for threatened states and replace normal state actions.
- relief decisions never appear to a controller that continues operation.
- regional closure groups replace individual closure rows in large networks.
- country-specific adapters hide generic duplicates.
- completed state decisions record one-time flags and do not remain as disabled clutter.

## Required dynamic tooltips

Tooltips must explain:

- selected state
- current site type and assignment
- current reach cap
- current workforce condition
- cost breakdown with icons
- main visible benefit
- mortality, resistance, exposure, and evidence direction
- exact blocked reason
- whether action ends, replaces, or intensifies the current state policy

Hidden future incidents and secret probability rolls should not be exposed.
