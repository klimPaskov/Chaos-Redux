# Event 22 Concentration Camps Decision and Mission Map

## Ownership

Working category identifiers:

- `chaosx_022_camp_network_management`
- `chaosx_022_liberated_site_relief`

The first category belongs to the responsible, successor, or continuing operator. The second belongs to a controller that has stopped operation and is managing liberated or abandoned sites.

The shared Camps and Repression Ledger owns routine management of a registered network: national mandate, economic priority, spending, per-site roles, release, dismantlement and records.
The Event 22 categories carry only the choices the Ledger does not own, so the Event 22 set is 14 decisions and 7 missions (proposal P-022-B in the index).
The legacy `genocide_crisis_category` decisions (`genocide_hide_evidence_from_foreign_observers`, `genocide_suppress_internal_reports`, `genocide_destroy_camp_evidence`, `genocide_deal_with_resistance_sabotage`, `genocide_handle_refugee_waves`, `genocide_manage_military_objections`, `genocide_redirect_trains_and_supplies`, `genocide_intensify_deportations` and the others) are visible only to AI-controlled countries that have not initialized the camp administration.
Event 22 therefore offers concealment, suppression and retreat choices as event options at the moment they matter and adds no permanent concealment decisions.

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

The category shows only decisions valid for the current mode. A country has one primary national policy and several state statuses, and the visible action count stays between three and five in normal play. Six is the hard maximum.

### Relief mode

The relief category appears only when the current country controls at least one liberated, abandoned, destroyed, or recently closed site that still has survivors, disease, contamination, evidence, or displacement work.

It shows one to three missions plus urgent state actions. It closes when all controlled sites reach a stable aftermath state.

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
- evidence or exposure risk as a consequence, not a hidden spendable cost

Final cost localisation must use amount plus matching texticon. Do not write literal resource labels inside the cost string.

Dynamic scaling factors:

- site count
- living custody at the site
- state distance and transport route
- current war
- front distance
- Exposure
- Resistance Pressure
- site type
- contamination or disease
- previous failures
- country size and economy

Centralize base values and scaling in `script_constants`; reuse the shared camp cost constants (`camp_repression_site_cost_constants.txt`, `camp_admin_value`) before defining new ones.

## Opening policy event options

These event options initialize the category. They are not persistent decisions.
Each option sets the shared national controls, so no Event 22 assignment or intensity state exists.

| Working option | Validity | Shared control set | Main consequence |
| --- | --- | --- | --- |
| `chaosx_022_open_close` | always valid unless a country-specific route blocks central authority | starts `chaosx_022_mission_regional_closure` and the shared reform path (`camp_admin_begin_reform`) | freezes intake and opens regional closure |
| `chaosx_022_open_review` | always valid for a functioning government | `camp_admin_mandate` custody | pauses expansion and forced work while cases are reviewed |
| `chaosx_022_open_labour` | valid when the shared coercive mandate is permitted | `camp_admin_mandate` coercive with the default economic priority | forced-work output starts, the Ledger sets industry, works or extraction |
| `chaosx_022_open_expand` | valid when eligible uncovered states remain and the political route permits repression | coercive mandate plus the expansion decision | opens targeted expansion |
| `chaosx_022_open_extermination` | Evolution I plus a derived target source and `camp_admin_can_use_radical_mandate` | radical mandate | accepts the evolved opening |

AI ordering is defined in the probability matrix. The opening must not show an extermination option merely because Evolution I exists if no derived target source or route exists.

## Operator decisions

### `chaosx_022_begin_regional_closure`

Scope: one generated region containing one or more sites.

Merges the original freeze intake, restore food and medicine, register detainees, preserve records, release or transfer survivors, reduce quota and decentralize decisions.
Those steps are the objectives of the closure mission, not separate rows.

Requirements:

- valid controller
- no active extermination or restricted chemical order in the region (use Halt Extermination first)

Spendable costs:

- political capacity
- support equipment
- trucks or trains
- civilian-factory burden

Effects:

- calls the shared intake freeze, survivor release and civilian replacement (`camp_admin_begin_reform`, `camp_admin_close_site`) for the sites in the region
- starts `chaosx_022_mission_regional_closure`
- hardliners and security services may resist (initializes the underground mission when authority is low)

AI: high for Dismantler and successor disclosure, near zero for an active Extermination Extremist unless defeat is imminent.
Cleanup: removed after transparent closure.

### `chaosx_022_place_network_under_review`

Role: move from exploitation or expansion into restrictive review.

Requirements:

- network active
- no binding extermination order remains

Spendable costs:

- political capacity
- civilian-factory burden for inspectors and administration

Effects:

- sets the shared custody mandate and pauses expansion
- invites the inspection event chain (`chaosx_022_inspection_requested`); real access can expose evidence, staged access becomes concealment
- raises short-term Exposure because records become accessible
- can end in closure, a smaller dormant repression network, renewed exploitation, scandal, or refusal by the military or civil service (drift outcomes of Part 2)

AI: high for Restrictive Reviewer, moderate for a weak Exploitative Authoritarian after exposure or collapse.

### `chaosx_022_resume_coercive_operation`

Role: leave review and return to detention or labour.

Requirements:

- network under review
- derived target source remains
- no transparent closure lock
- route permits arbitrary detention

Spendable costs:

- political capacity
- stability

Effects:

- restores the coercive mandate
- sharp Exposure increase if inspectors or records already exist

AI: only Exploitative Authoritarian or Extermination Extremist.

### `chaosx_022_expand_network_into_state`

Scope: targeted eligible uncovered state.

Requirements:

- below the generic reach ceiling
- derived target source
- policy permits expansion
- state passes the eligibility rules

Spendable costs:

- civilian-factory burden
- support equipment
- manpower commitment
- trains or convoys

Effects:

- adds a concentration camp through the shared site helpers
- admits a cohort through `camp_admin_admit_detainees` from a proven campaign source (no source, no intake)
- records responsibility and network generation
- raises Exposure and Resistance Pressure

Exploit controls: a protected relief state is never valid, repeated firing cannot bypass the ceiling, and the cohort is bounded by the shared population-share ceiling.

### `chaosx_022_halt_extermination`

Requirements: Evolution I, an active extermination site.

Spendable costs:

- political capacity
- stability under hardliner rule

Effects:

- ends the killing role at the selected sites (shared role set back to custody)
- preserves evidence and responsibility
- starts the closure mission in the region
- risk of coup or underground continuation

### `chaosx_022_activate_restricted_chemical_site`

Requirements:

- valid technology and project gates
- available stockpile
- eligible extermination site
- capacity below the centralized cap

Spendable costs:

- agent stockpile
- support equipment
- specialist manpower or command abstraction
- transport

Effects:

- starts stockpile-backed restricted operation through the existing restricted chemical site system (`genocide_restricted_chemical_site_escalation` owner)
- severe deaths, contamination, accident risk and source-specific evidence

Operation stops automatically when the stockpile debit fails.
The decision is alternate history and carries no procedural content.

### `chaosx_022_broaden_purge_inward`

Requirements:

- derived target source exhausted or inaccessible
- core population available above the protected floor
- extreme route remains committed

Spendable costs:

- stability
- war support
- political capacity

Effects:

- permits domestic-core intake and a temporary security-apparatus effect
- officer, party, factory and administrative collapse, civil-war and terror links, severe resistance

This is a failure spiral, not an efficient way to refresh a workforce.

## Liberated-site relief decisions

### `chaosx_022_secure_liberated_site`

Spendable costs:

- manpower or temporary division commitment
- support equipment
- command power

Effects: ends guard violence and looting risk, protects survivors and records, prevents accidental reuse.

### `chaosx_022_deliver_emergency_relief`

Spendable costs:

- trucks or trains
- support equipment
- civilian-factory burden

Effects: lowers post-liberation mortality and disease, reduces Resistance Pressure in the state.
Also serves a closing site and a camp in a proven Black Plague state (Part 5).

### `chaosx_022_quarantine_and_decontaminate`

Requirements: disease or contamination.

Spendable costs:

- support equipment
- trucks
- civilian-factory burden
- fuel where decontamination uses it

Effects: contains spread and starts a humane, time-limited medical mission with a release condition.

### `chaosx_022_register_survivors_and_missing`

Spendable costs:

- political capacity
- civilian-factory burden

Effects: improves tracing and evidence confidence, unlocks return or resettlement, makes transparent closure possible. Destroyed records raise cost and duration.

### `chaosx_022_preserve_site_and_evidence`

Spendable costs:

- security commitment
- political capacity

Effects: protects physical and documentary proof, blocks local demolition until the investigation ends, supports network verification.

### `chaosx_022_transfer_to_safe_accommodation`

Requirements: receiving capacity, a safe route, a proved living cohort (Part 5 migration contract).

Spendable costs:

- trucks, trains, or convoys
- support equipment
- civilian-factory burden

Effects: reduces local overcrowding and creates the migration or resettlement status through the migration owner.
Without proved capacity and passage the request moves nobody and survivors stay in current accommodation.

### `chaosx_022_dismantle_documented_site`

Requirements: survivors moved or safely housed, evidence complete or transferred, no contamination blocker.

Spendable costs:

- civilian-factory burden
- support equipment

Effects: removes the camp building through the shared site closure, retains historical evidence and aftermath status.

## Missions

Missions run one to three at a time per category.
Goal-style missions complete when the work is done and need no extra paid click.
Easy missions last at least 90 days; emergency front missions can be shorter.

### Operator missions

- `chaosx_022_mission_regional_closure`
  - long mission scaled by site count and condition
  - objectives: stop intake, supply sites, register detainees, preserve records, release or transfer people, remove operation
  - partial success keeps completed components; a half-country network needs several regional missions
- `chaosx_022_mission_prevent_escape`
  - medium mission when Resistance Pressure and the local escape network cross a threshold
  - paths: relief and reduced pressure, guard containment with a higher burden, violent suppression with deaths and evidence
  - failure: escape, testimony, resistance growth, possible discovery
- `chaosx_022_mission_contain_epidemic`
  - medium to hard mission when overcrowding, famine (`famine_food_stage_requires_mortality`), plague, contamination or destroyed infrastructure raises disease pressure
  - success needs food, medicine, transport and time; failure causes deaths, regional spread, escape and discovery
- `chaosx_022_mission_underground_network`
  - starts when local administrators resist a national closure order
  - paths: prosecute operators, negotiate surrender, restore central coercive control, expose the network publicly
  - failure: covert deaths continue, records disappear, local armed resistance grows

### Relief missions

- `chaosx_022_mission_emergency_survival`
  - 90 to 120 days; keep post-liberation mortality below a dynamic threshold through food, medicine, security and transport
- `chaosx_022_mission_document_network`
  - 120 to 240 days depending on destroyed evidence and site count; preserve several evidence categories and link responsible institutions
- `chaosx_022_mission_resettle_and_reunite`
  - 180 to 365 days; register a required share of survivors, trace families and move survivors into stable housing, return or accepted resettlement without creating a new humanitarian crisis (merges trace and reunite with regional resettlement)

## Foreign-reaction adapters

Event 22 exposes triggers and effects to the shared Condemnation or diplomacy categories (`genocide_publicize_survivor_testimony`, `genocide_support_resistance_networks`, `genocide_prepare_tribunal_records` and the Condemnation response effects) for:

- investigate credible reports
- protect witnesses
- share intelligence
- demand inspection
- receive survivors
- fund relief
- impose or support shared sanctions
- cooperate with tribunal

These are adapters, not duplicate Event 22 decisions. The owning systems define their final costs and visibility.

## Choices that live in events

The following choices from the original map are options of the named events, so they appear when the situation exists and never as permanent rows:

| Original working identifier | Disposition |
| --- | --- |
| `restrict_foreign_access`, `falsify_camp_records`, `stage_inspection` | options of `chaosx_022_foreign_leak` and `chaosx_022_inspection_requested` |
| `destroy_records`, `destroy_site_and_records`, `abandon_site` | options of `chaosx_022_front_approaches_site` and `chaosx_022_foreign_leak`; physical destruction reuses `genocide_destroy_camp_evidence_in_action_state` |
| `close_and_await_liberation`, `order_supplied_transfer`, `force_evacuation_on_foot`, `liquidate_remaining_detainees` | options of `chaosx_022_front_approaches_site`, resolved by `chaosx_022_retreat_outcome` |
| `mission_keep_site_from_enemy` | the options above replace the mission |
| `suppress_resistance_network`, `reinforce_guard_system` | options of `chaosx_022_coordinated_escape` and the escape mission; legacy `genocide_deal_with_resistance_sabotage` remains the AI route |

## Dropped or moved to the shared owner

| Original working identifier | Disposition |
| --- | --- |
| `freeze_intake`, `restore_food_and_medicine`, `register_detainees`, `preserve_records_for_investigation`, `release_or_transfer_survivors`, `reduce_labour_quota`, `decentralize_or_dissolve_administration` | merged into `begin_regional_closure` and its mission, or into the relief decisions |
| `open_site_to_inspection` | folded into `place_network_under_review` and the inspection events |
| `assign_industrial_labour`, `assign_construction_labour`, `assign_extraction_labour`, `raise_assignment_intensity`, `lower_assignment_intensity` | replaced by the shared economic priority (industry, works, extraction) and spending ceiling in the Ledger; the shared caps (40 percent industrial, 25 percent national, 40 percent construction and extraction) replace the Event 22 caps |
| `assign_logistics_labour` | dropped; no shared priority supports it and its rail-repair bonus is not read by any other rule |
| `import_detainees` | merged into `expand_network_into_state` (cohort admission from a proven source); transfers between existing sites use the shared exact-cohort transfer and `genocide_intensify_deportations` |
| `centralize_administration`, `seize_confiscated_property` | dropped; their only effects were the assignment cap and a temporary budget, and the corruption theme remains in `chaosx_022_administrator_corruption` |
| `convert_site_to_extermination` | the Evolution I conversion and the Ledger's killing-role conversion under the radical mandate |
| `set_target_purpose`, `raise_extermination_intensity` | dropped; the target source is derived from campaign facts and killing intensity is the shared killing role's rate |
| `mission_trace_and_reunite`, `mission_regional_resettlement` | merged into `mission_resettle_and_reunite` |

## Decision replacement rules

- `place_network_under_review` and `resume_coercive_operation` replace each other.
- Expansion disappears at the current reach ceiling.
- Retreat options appear only for threatened states and replace normal state actions through the event.
- Relief decisions never appear to a controller that continues operation.
- Regional closure groups replace individual closure rows in large networks.
- Country-specific adapters hide generic duplicates.
- Completed state decisions record one-time flags and do not remain as disabled clutter.

## Required dynamic tooltips

Tooltips must explain:

- selected state or region
- current site role
- cost breakdown with icons
- main visible benefit
- Exposure and Resistance direction
- exact blocked reason
- whether the action ends, replaces, or intensifies the current policy

Hidden future incidents and secret probability rolls should not be exposed.
A tooltip lists at most the cost, the main benefit, the main risk and the blocked reason; it does not list state internals.
