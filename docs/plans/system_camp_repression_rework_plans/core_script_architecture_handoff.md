# Camp Repression Rework: Core Script Architecture Handoff

> **Superseded preimplementation architecture snapshot.** This handoff explains the design that guided the core runtime. Proposed files, migration language, and future-tense requirements are not current status. The implemented runtime now lives in the consolidated files listed in `source_of_truth_and_completion_tracker.md`. Preserve this document as architecture rationale and use `completion_report.md` plus `scenario_contract_validation_report.md` for final status and the recorded engine-runtime validation gap.

Feature id: system_camp_repression_rework

Prepared: 2026-07-10

Status: architecture-only handoff. This document does not implement gameplay, localisation, GUI, assets, workbook changes, or balance.

## 1. Architectural decision

Build the rework as a replacement runtime over the existing camp buildings and existing Deaths, condemnation, discovery, Germany/Mengele, Japan biowarfare, and Soviet collapse bridges. Do not create a parallel camp system.

The core runtime should have these invariants:

1. global.genocide_active_camp_states is the canonical global active-site registry.
2. A state is present at most once, is removed as soon as it is no longer active, and is never retained merely because evidence remains.
3. genocide_responsible_country remains the canonical primary perpetrator pointer stored on the state. It survives owner/controller change and is cleared only by explicit final evidence-resolution cleanup.
4. Deaths are state-linked and victim-linked through the existing Chaos Meter helper. Perpetrator attribution remains a separate camp ledger operation.
5. Each active state makes one consolidated monthly Deaths registration. Site traits contribute factors to that calculation instead of independently stacking several Deaths calls.
6. Dormant historical sites never register, tick, create pressure, or produce routine events.
7. No new daily, weekly, or monthly whole-world scan is added. The current host-only monthly call remains the scheduler, but its recurring every-country registration scan is removed after migration.
8. The chemical/biological override is represented only by abstract script tiers, stockpile use, Deaths factors, short-term coercive-control pressure, and severe adverse consequences. It contains no recipe, dosage, delivery procedure, protected-class selector, or operational targeting logic.
9. The Repression Ledger uses country variables and bounded country arrays. It does not use persistent event targets.

## 2. Live identifiers and call sites that must be preserved or migrated

| Surface | Existing identifier or call site | Current contract | Required treatment |
| --- | --- | --- | --- |
| Buildings | concentration_camp, extermination_camp, gulag_labor_camp_network in common/buildings/chaosx_buildings.txt | Unique state buildings; concentration_camp is currently directly buildable | Preserve the three ids. Make concentration-camp activation decision/effect-owned before removing the recurring registration scan. |
| Scheduler | common/on_actions/chaosx_on_actions_chaos_meter.txt, host-only on_monthly block | Calls genocide_initialize_system_if_needed and genocide_monthly_global_pulse once through is_global_host | Keep this scheduler. Do not add a second monthly system. |
| Startup | common/on_actions/genocide_crisis_on_actions.txt, on_startup | Calls genocide_initialize_system_if_needed from a random existing country | Extend the initializer with a versioned migration call. |
| Global registry | global.genocide_active_camp_states | Stores state scopes added by genocide_track_state_for_monthly_pulse | Keep as canonical global active array; add explicit unregister and stale-entry cleanup. |
| Current registration | genocide_track_state_for_monthly_pulse | Adds THIS state if not already in the global array | Replace call sites with camp_rework_register_active_site; keep this name temporarily as a compatibility adapter. |
| Recurring discovery scan | genocide_register_constructed_concentration_camps | Runs every_country and every_controlled_state each monthly pulse | Remove from recurring runtime after one-time migration and decision-only activation are in place. |
| Monthly pulse | genocide_monthly_global_pulse | Registers constructed camps, then loops global.genocide_active_camp_states | Convert to cleanup, active-state processing, active-country pressure, and optional open-GUI refresh only. |
| Monthly state dispatcher | genocide_apply_monthly_state_effects | Independently calls concentration, extermination, gulag, experiment, biowarfare, and restricted-chemical monthly effects | Replace with a single camp_rework_apply_monthly_state_effects calculation and Deaths call. Keep old names as adapters only while external call sites migrate. |
| Responsibility | state variable genocide_responsible_country; flag genocide_site_has_responsible_country | Scope-valued state variable points to the responsible country | Keep both. The variable is authoritative; the flag is a cheap presence marker and must agree with it. |
| Perpetrator accounting | genocide_credit_state_deaths_to_responsible | Adds PREV.genocide_last_state_deaths to the responsible country's genocide_deaths and hidden condemnation | Preserve the semantic split, but route it through the consolidated Deaths wrapper. |
| Deaths percent helper | chaos_meter_register_state_civilian_deaths_percent in common/scripted_effects/chaos_meter_effects.txt | State scope; consumes chaos_state_deaths_percent and optional multiplier/cap/random inputs; credits OWNER in the Deaths ledger; reduces state population through add_manpower | This is the required state-population path for monthly camp deaths. |
| Deaths exact helper | chaos_meter_register_deaths | Consumes chaos_deaths_change and classification/target inputs | Use only through a camp exact-deaths adapter for event-authored exact deaths, such as Mengele reports. |
| Deaths output | temporary chaos_deaths_change | Rounded actual deaths after cap/randomization | Copy immediately to state variables before any nested helper can overwrite it. |
| Deaths reasons | chaos_meter_deaths_reason.camp_atrocity, extermination_camp, gulag_repression, biowarfare_outbreak; chemical_attack also exists | Drives the Deaths history row and cause totals | Retain these reasons unless dedicated camp chemical/biological reasons are added with matching localisation and Chaos Meter display support. |
| Discovery hook | on_state_control_changed -> genocide_on_state_control_changed | Uses short-lived event targets, then calls genocide_try_discover_state_atrocity | Keep the hook. Replace the discovery calculation with the new state evidence fields while preserving bounded first-discovery events. |
| Discovery flags | genocide_site_discovered, genocide_destroyed_atrocity_site, genocide_evidence_destroyed, genocide_evidence_destroy_failed | Persist physical/discovered evidence | Preserve and incorporate into the canonical evidence phase. |
| Discovery effects | genocide_calculate_discovery_condemnation_from_prev_state and genocide_apply_discovery_to_responsible_from_prev_state | Calculates repeat/site/experiment/chemical/cover-up severity and feeds condemnation | Preserve source-aware condemnation behavior; extend inputs from camp evidence/reach/contamination values. |
| Condemnation bridge | genocide_register_hidden_condemnation_source, genocide_register_public_condemnation_source | Adapters into condemnation_add_source | Reuse. Do not create a parallel condemnation counter. |
| Condemnation ids | condemnation_source.atrocity, biological, chemical, coverup; condemnation_context.camp_operation, camp_discovery, experiment_site, restricted_site_operation, restricted_chemical_site, destroyed_records | Existing source/context enum contract | Reuse these exact constants. |
| Chemical capability | genocide_country_has_restricted_chemical_site_capacity | Checks sarin or soman tech/project plus cylinder gates | Replace with tier resolver, while retaining this trigger as the "any eligible chemical tier" compatibility gate. |
| Chemical execution | genocide_apply_restricted_chemical_site_escalation_in_from | Consumes sarin/soman cylinders, calls chem_apply_state_contamination, registers Deaths, starts a timed state flag | Route through the tier resolver, shared stockpile consumer, consolidated Deaths adapter, and active-site lifecycle. |
| Biological execution | genocide_japan_prisoner_experimentation_in_from | Registers direct Deaths, then may call apply_anthrax_contamination, apply_tularemia_contamination, or apply_plague_contamination | Remove double-registration risk. An explicit disease-contamination helper already registers its own Deaths; copy and credit that result instead of adding a second activation Deaths call. |
| Germany bridge | germany_mengele_register_experiment_deaths | Calculates exact deaths and directly calls chaos_meter_register_deaths in state 88 | Convert to camp_rework_register_exact_state_deaths so state population, Deaths history, state last-deaths, and responsible-country accounting remain aligned. |
| Germany state flags | genocide_auschwitz_experiment_site, genocide_ss_laboratory_site | Mark experiment-linked active/evidence sites | Preserve as specialised traits layered over the canonical site phase/type. |
| Germany country values | mengele_autonomy, mengele_permission_level | Existing Germany/Mengele power and permission contract | Read as calculation inputs; never replace them with duplicate camp variables. |
| Japan scientist | character name JAP_shiro_ishii and character flag chaosx_scientist_jap_shiro_ishii | Startup-generated named scientist; no live Ishii camp runtime currently consumes it | Use a country route flag set by explicit Japan content; do not run random_scientist queries during monthly camp processing. |
| Japan state flag | genocide_japanese_biowarfare_atrocity_site | Current biowarfare experiment-site marker | Preserve as experiment/biological trait. |
| Soviet bridge | soviet_collapse_apply_genocide_gulag_repression_memory | Increases gulag repression memory and bounded Union Crisis/collapse components | Keep as the sole bridge for those collapse variables; call on material Soviet repression actions, not once per state every month. |
| Soviet paranoia | vanilla SOV_paranoia and SOV_paranoia_system_active_flag; vanilla SOV_paranoia_*_increase_effect helpers | Existing No Step Back paranoia system | Read only when the flag is active and use vanilla helpers when a camp action explicitly changes paranoia. Do not create a second paranoia value. |
| Current category ids | genocide_crisis_category, imperial_occupation_crisis, gulag_and_mass_repression_system, genocide_foreign_response_category | Separate current country/response categories | Add a shared compact header/launcher to the three country-management categories; keep foreign response separate. |

### Existing decision-to-effect call map

These are live ids in common/decisions/genocide_crisis_decisions.txt and must either keep their current id or receive a compatibility wrapper while their implementation is migrated:

| Package | Decision id | Current completion effect |
| --- | --- | --- |
| Germany | germany_wartime_camp_administration | genocide_germany_camp_administration |
| Germany | germany_expand_occupied_poland_camp_system | genocide_build_concentration_camp_in_from |
| Germany | germany_expand_extermination_site_network | genocide_build_extermination_camp_in_from |
| Germany | germany_intensify_extermination_policy | genocide_germany_intensify_extermination_policy |
| Germany | germany_transfer_prisoners_to_experiment_site | genocide_germany_transfer_prisoners_to_experiment_site_in_from |
| Shared restricted | genocide_restricted_chemical_site_escalation | genocide_apply_restricted_chemical_site_escalation_in_from |
| Shared | genocide_build_extermination_camp | genocide_build_extermination_camp_in_from |
| Shared | genocide_intensify_deportations | genocide_intensify_deportations |
| Shared | genocide_hide_evidence_from_foreign_observers | same-named scripted effect |
| Shared | genocide_suppress_internal_reports | same-named scripted effect |
| Shared | genocide_redirect_trains_and_supplies | same-named scripted effect |
| Shared | genocide_deal_with_resistance_sabotage | genocide_deal_with_resistance_sabotage |
| Shared | genocide_handle_refugee_waves | same-named scripted effect |
| Shared | genocide_manage_military_objections | same-named scripted effect |
| Shared | genocide_destroy_camp_evidence | genocide_destroy_camp_evidence_in_from |
| Shared | genocide_dismantle_extermination_camp | genocide_dismantle_extermination_camp_in_from |
| Shared | genocide_cover_up_liberated_camps | same-named scripted effect |
| Japan | japan_expand_forced_labor_camps | genocide_build_concentration_camp_in_from |
| Japan | japan_conduct_anti_partisan_reprisals | genocide_japan_anti_partisan_reprisals_in_from |
| Japan | japan_transfer_prisoners_to_experimental_facilities | genocide_japan_prisoner_experimentation_in_from |
| Japan | japan_destroy_occupation_records | genocide_destroy_camp_evidence_in_from |
| Soviet | sov_expand_gulag_network | genocide_build_gulag_network_in_from |
| Soviet | sov_deport_suspected_opposition_groups | genocide_soviet_deport_suspected_groups_in_from |
| Soviet | sov_confiscate_food_from_disloyal_regions | genocide_soviet_confiscate_food_in_from |
| Soviet | sov_purge_camp_administrators | genocide_soviet_purge_camp_administrators_in_from |
| Soviet | sov_raise_forced_labor_quotas | genocide_soviet_forced_labor_quotas_in_from |
| Soviet | sov_destroy_gulag_records | genocide_destroy_camp_evidence_in_from |
| Foreign response | genocide_publicize_survivor_testimony | genocide_foreign_publicize_target |
| Foreign response | genocide_support_resistance_networks | genocide_foreign_support_resistance_against_target |
| Foreign response | genocide_prepare_tribunal_records | genocide_foreign_prepare_tribunal_against_target |

### Current defects the rework must not carry forward

- genocide_track_state_for_monthly_pulse has no matching remove_from_array path.
- genocide_register_constructed_concentration_camps is a recurring every-country scan.
- genocide_apply_monthly_state_effects can register several overlapping monthly Deaths entries for one state.
- genocide_destroy_camp_evidence_in_from and genocide_dismantle_extermination_camp_in_from remove buildings or flags without a complete registry/count/modifier teardown.
- condemnation_dismantle_restricted_sites clears specialised flags but does not unregister the state or rebuild responsible-country values.
- germany_mengele_register_experiment_deaths bypasses genocide_credit_state_deaths_to_responsible.
- biological activation can register camp deaths and then register contamination deaths again.

## 3. Canonical data model

### 3.1 Country values

These accepted values are country-scoped and authoritative:

| Variable | Meaning | Update rule |
| --- | --- | --- |
| camp_network_reach | Weighted active registered network size | Rebuilt from valid active-site arrays; never manually incremented without a later rebuild |
| camp_labor_output | Aggregate construction/extraction/logistics pressure | Rebuilt from state outputs and allocation, then reduced by overextension |
| camp_coercive_control | Short-term control pressure | Rebuilt from active sites, guards, current restricted tier, and route |
| camp_population_loss_index | Forward monthly population-loss pressure, not cumulative deaths | Rebuilt before monthly application and updated from actual Deaths only for trend/band display |
| camp_resistance_pressure | Aggregate current resistance/backlash pressure | Rebuilt plus explicit event deltas; clamp centrally |
| camp_stability_damage | Current national stability drag | Rebuilt from active phases, core fallback, exposure, and route |
| camp_evidence_level | Current hidden/discovered physical evidence pressure | Rebuilt from state evidence; this does not replace condemnation hidden buckets |
| camp_overstretch | Guard, supply, rail, convoy, manpower, and administrative strain | Rebuilt from burdens versus reach |
| camp_foreign_visibility | Observer and foreign-awareness pressure | Rebuilt plus discovery/cover-up deltas |
| camp_tribunal_severity | Camp-specific legal/accountability pressure | Rebuilt from evidence, actual deaths, contamination, repeat discoveries, and collaboration shares |
| camp_hardliner_pressure | Internal hardliner influence | Updated by escalation/reform actions and clamped |
| camp_democratic_legitimacy_damage | Democratic/legal legitimacy burden | Updated for democratic/colonial/core-fallback use and reduced by redress |
| camp_reform_pressure | Court, postwar, regime-change, inspection, colonial, and dismantlement pressure | Rebuilt from current route and evidence |

Existing variables genocide_deaths, hidden_atrocity_score, genocide_decisions_taken, genocide_coverup_effort, genocide_discovered_sites, and the condemnation source buckets retain their existing distinct meanings. Do not alias them to the new values.

Existing genocide_resistance_pressure, genocide_visibility, genocide_tribunal_severity, genocide_concentration_sites, genocide_extermination_sites, and genocide_gulag_sites should become compatibility projections rebuilt from the canonical values/arrays while legacy callers remain. There must be one-directional sync from canonical state into legacy projections, never bidirectional writes.

### 3.2 State variables

| Variable | Type | Meaning/default |
| --- | --- | --- |
| camp_site_type | int enum | Primary site type; default none |
| camp_site_phase | int enum | Dormant, active detention, expanded labor, radicalized, restricted, reforming, or dismantled |
| genocide_responsible_country | scope-valued | Primary responsible country; existing canonical pointer |
| camp_site_secondary_responsible_country | optional scope-valued | Collaborator/co-responsible country for Vichy/German or comparable explicit routes |
| camp_site_evidence_depth | fixed point | Physical evidence retained at this state; default 0 |
| camp_site_monthly_death_pressure | fixed point | Pre-application monthly Deaths pressure; default 0 |
| camp_site_last_month_deaths | fixed point | Actual last consolidated Deaths output; default 0 |
| camp_site_local_labor_output | fixed point | Current local output pressure; default 0 |
| camp_site_local_resistance_pressure | fixed point | Current local backlash pressure; default 0 |
| camp_site_foreign_exposure | fixed point | Observer/discovery exposure; default 0 |
| camp_site_pool_type | int enum | Pool provenance used by penalties and GUI |
| camp_site_primary_action_id | int enum | Current GUI action recommendation; default none |

### 3.3 Reused state flags

Keep these existing flags as canonical facts:

- genocide_historical_quiet_camp: dormant and non-processing.
- genocide_site_has_responsible_country: responsibility pointer presence.
- genocide_atrocity_site_known_to_regime: regime knowledge.
- genocide_site_discovered: public/foreign discovery.
- genocide_destroyed_atrocity_site: physically inactive but evidence-bearing.
- genocide_evidence_destroyed: successful partial cover-up.
- genocide_evidence_destroy_failed: failed cover-up.
- genocide_auschwitz_experiment_site and genocide_ss_laboratory_site: Germany traits.
- genocide_japanese_biowarfare_atrocity_site: Japan biological trait.
- genocide_restricted_chemical_site: chemical evidence exists.
- genocide_restricted_chemical_site_active: current restricted chemical use.

Add only lifecycle facts not represented today:

- camp_site_active: state is expected to be in the active registry.
- camp_site_reforming: a dismantlement/reform chain is active.
- camp_site_evidence_resolved: final tribunal/redress/records disposition permits pointer and evidence-array cleanup.
- camp_site_biological_escalation_active: current biological override use.
- camp_site_contaminated_evidence: persistent contaminated evidence independent of a timed active-use flag.

Do not add numeric 0/1 variables for these facts.

### 3.4 Enums

Define integer script-constant enums:

camp_rework_site_type:

- none = 0
- detention = 1
- forced_labor = 2
- gulag = 3
- radicalized = 4
- experiment = 5
- restricted_chemical = 6
- restricted_biological = 7

camp_rework_phase:

- dormant = 0
- active_detention = 1
- expanded_labor = 2
- radicalized_atrocity = 3
- restricted_escalation = 4
- reforming = 5
- dismantled = 6

camp_rework_pool_type:

- occupied_noncore = 1
- colonial_or_subject = 2
- noncore_integrated = 3
- periphery_security = 4
- core_fallback = 5

camp_rework_band:

- none = 0
- low = 1
- guarded = 2
- high = 3
- critical = 4

camp_rework_action:

- none = 0
- expand = 1
- labor_project = 2
- allocate_guards = 3
- reduce_quotas = 4
- inspect = 5
- dismantle = 6
- destroy_evidence = 7
- country_primary = 8

## 4. Registry and cleanup architecture

### 4.1 Arrays

| Array | Scope | Contents and ownership |
| --- | --- | --- |
| global.genocide_active_camp_states | global | Canonical active state scopes |
| global.camp_rework_active_countries | global | Countries with at least one valid responsible active site |
| camp_active_site_states | responsible country | Active state scopes for fast country rebuilds and GUI |
| camp_evidence_site_states | responsible country | Active or inactive state scopes with unresolved evidence |
| global.camp_rework_invalid_site_buffer | global scratch | Cleared before and after the two-pass stale-entry removal |

### 4.2 Registration

camp_rework_register_active_site runs in state scope.

Required inputs:

- genocide_responsible_country must already exist, or temporary camp_registration_responsible_country must identify the country.
- camp_site_type and camp_site_phase should be supplied; defaults are inferred from existing building/trait flags only during migration.
- optional camp_site_secondary_responsible_country.

Outputs and side effects:

1. Resolve and store genocide_responsible_country.
2. Set genocide_site_has_responsible_country, genocide_atrocity_site_known_to_regime, and camp_site_active.
3. Clear genocide_historical_quiet_camp only when an explicit activation action converts a dormant marker.
4. Add THIS once to global.genocide_active_camp_states.
5. Add THIS once to the responsible country's camp_active_site_states and camp_evidence_site_states.
6. Add the responsible country once to global.camp_rework_active_countries.
7. Initialize state evidence/pressure/output variables only if absent; never erase historical evidence on re-registration.
8. Rebuild the responsible country's counts/values.

It must be idempotent. Repeated registration may refresh type/phase but may not add counts twice.

### 4.3 Unregistration

camp_rework_unregister_inactive_site runs in state scope.

Required behavior:

1. Copy the responsible scope before clearing anything.
2. Remove THIS from global.genocide_active_camp_states.
3. Remove THIS from the responsible country's camp_active_site_states.
4. Clear camp_site_active and active-use timed flags.
5. Remove active-only dynamic modifiers and zero active-only state pressure/output values.
6. Keep genocide_responsible_country, camp_site_secondary_responsible_country, camp_evidence_site_states membership, and evidence/discovery/cover-up flags unless camp_site_evidence_resolved is set.
7. Rebuild responsible-country values.
8. Remove the responsible country from global.camp_rework_active_countries only after its camp_active_site_states array is empty.
9. If evidence is resolved, also remove THIS from camp_evidence_site_states, clear the responsibility flags/variables, and clear only evidence variables explicitly covered by that resolution.

### 4.4 Stale-entry cleanup

camp_rework_clean_invalid_active_sites uses a two-pass buffer:

1. Clear global.camp_rework_invalid_site_buffer.
2. Loop global.genocide_active_camp_states.
3. Add any state failing is_valid_camp_active_site_state to the buffer.
4. Loop the buffer and call camp_rework_unregister_inactive_site.
5. Clear the buffer.

Do not mutate the canonical array inside its own source iteration.

### 4.5 Direct construction and migration

concentration_camp is currently is_buildable = yes, and the system discovers manually constructed buildings through a recurring every-country scan. There is no building-completion on-action in the official on-action list.

To satisfy the accepted no-world-loop rule:

1. Make new camp construction decision/effect-owned before removing the scan.
2. Change concentration_camp to is_buildable = no after every intended construction route has a decision or scripted effect.
3. Keep the building id and all existing sites.
4. Run one versioned startup migration that scans existing countries/states once, infers active versus dormant state, registers valid sites, and removes duplicates/stale entries.
5. Remove genocide_register_constructed_concentration_camps from genocide_monthly_global_pulse.

If direct construction is deliberately retained, the recurring world scan is unavoidable with the currently documented hooks and conflicts with the accepted architecture. That choice requires explicit parent/user approval rather than an implicit fallback.

## 5. Trigger contracts

Implement or adapt these triggers in common/scripted_triggers/genocide_crisis_triggers.txt:

| Trigger | Scope | Contract |
| --- | --- | --- |
| is_valid_camp_active_site_state | state | camp_site_active, responsibility exists, not dormant/dismantled, and at least one active building/experiment/restricted phase remains |
| is_valid_camp_dormant_marker_state | state | historical/dormant marker exists, no active flag, and no monthly processing |
| is_valid_camp_discovery_state | state | unresolved physical evidence, not already fully resolved, responsible pointer exists |
| is_valid_camp_dismantlement_state | state | active or reforming site controlled by acting country and route permits cleanup |
| is_valid_camp_enemy_proximity_state | state | preserve the current nearby enemy division/controller logic |
| has_active_camp_network | country | camp_active_site_states contains at least one valid state |
| has_visible_camp_reform_work | country | unresolved evidence, active reform mission, regime-change cleanup, or redress pressure exists |
| has_camp_category_visible_action | country | active route, valid pool, active network, discovery, or reform work; AI visibility is handled separately |
| has_camp_ai_expansion_capacity | country | current active/radicalized/restricted counts remain under resolved caps and resource/route checks pass |
| has_camp_chemical_override_capacity | country | resolved chemical tier is above none and required stockpile/logistics are available |
| has_camp_biological_override_capacity | country | resolved biological tier is above none and required stockpile/facility/route are available |

Country pool triggers must remain territorial/legal/political:

- is_generic_occupied_camp_pool_state
- is_generic_colonial_camp_pool_state
- is_generic_noncore_security_pool_state
- is_generic_political_opposition_pool_state
- is_generic_core_fallback_pool_state
- the exact U.K./Raj, U.S., France/Vichy, Italy, Belgium, Germany, Japan, and Soviet pool triggers listed in the accepted tracker.

No pool trigger may select a protected class.

## 6. Core effect contracts

| Effect | Scope | Inputs | Outputs/side effects/defaults |
| --- | --- | --- | --- |
| camp_rework_initialize_country_values | country | none | Initializes missing canonical values to 0; does not overwrite live values |
| camp_rework_register_active_site | state | responsibility, type, phase, optional secondary responsibility | Idempotent registration described above |
| camp_rework_unregister_inactive_site | state | optional camp_cleanup_resolve_evidence flag | Active teardown; evidence retained by default |
| camp_rework_clean_invalid_active_sites | global host country/effect chain | none | Two-pass cleanup of the canonical global array |
| camp_rework_recalculate_site_values | state | current phase/type/buildings/traits/responsible context | Writes local output, resistance, evidence, foreign exposure, and monthly death pressure |
| camp_rework_calculate_monthly_deaths | state | state values and responsible-country values | Sets temporary camp_deaths_percent, camp_deaths_mult, camp_deaths_cap_factor, camp_deaths_reason |
| camp_rework_register_state_deaths | state | camp_deaths_percent; optional multiplier/cap/reason | Calls chaos_meter_register_state_civilian_deaths_percent; writes camp_site_last_month_deaths and genocide_last_state_deaths; credits responsibility; defaults multiplier 1 and type-appropriate reason/cap |
| camp_rework_register_exact_state_deaths | state | camp_exact_deaths and reason | Calls chaos_meter_register_deaths with civilian/state-pop/OWNER target inputs, then performs the same output/credit contract |
| camp_rework_apply_monthly_state_effects | state | none | Recalculate site, resolve tiers, consume ongoing stockpile where relevant, make one Deaths call, update pressure/evidence, no routine popup |
| camp_rework_apply_country_monthly_pressure | country | aggregated active sites | Rebuilds national values, applies dynamic modifiers, calls bounded country bridge logic |
| camp_rework_sync_legacy_compatibility_values | country | canonical values/counts | One-way projections into still-used genocide_* fields |
| camp_rework_apply_discovery | state | discovering country available only inside current effect chain | Marks discovery; exposes hidden buckets; condemns primary/secondary responsibility; fires bounded threshold events |
| camp_rework_attempt_evidence_destruction | state | acting country and costs validated | Applies Deaths once if designed, sets success/failure evidence facts, then unregisters only if site ceases operation |
| camp_rework_start_dismantlement | state | acting country, duration/cost already validated | Sets reforming state; does not destroy evidence or unregister until operation actually stops |
| camp_rework_complete_dismantlement | state | resolution type | Removes active structures/modifiers, unregisters, retains or resolves evidence according to the explicit outcome |
| camp_rework_apply_core_fallback_penalties | country/state as caller documents | core-fallback pool fact | Lower output; higher stability, legitimacy, resistance, evidence, and reform pressure |
| camp_rework_resolve_restricted_method_tiers | country | live capability and stockpile | Writes temporary tier choices and persistent display tiers; does not consume equipment |
| camp_rework_consume_restricted_stockpile | country | selected type/tier and usage mode | Removes a constant-defined amount; sets success flag; no stock means no ongoing override |
| camp_rework_apply_ai_cap | country | country/route/resource context | Writes temporary active, radicalized, experiment, and restricted caps and a can-expand flag |
| camp_rework_build_pool_arrays | country | route/country context | Clears and rebuilds bounded tiered state pools in accepted priority order |
| camp_rework_select_ai_state | country | action type | Selects from the first nonempty priority pool using random_scope_in_array; AI never uses GUI selection state |
| camp_rework_route_country_specific_action | country | action id and selected state | Dispatches Germany/Japan/Soviet/colonial/generic bridge without copying their logic |
| camp_rework_rebuild_display_values | country | none | Cleans, recalculates, validates selection, rebuilds arrays, then display variables |
| camp_rework_rebuild_gui_arrays | country | none | Rebuilds bounded aligned arrays only |
| camp_rework_select_state_for_display | country | camp_gui_requested_state_id or selected row | Validates state id through variable scope, stores camp_selected_state_id, rebuilds selected card |
| camp_rework_clear_selected_state | country | none | Clears selected id/index and selected-card values |

Temporary variables have no scope. Every helper must document that its temporary inputs are consumed in the same effect chain and must copy outputs before entering another helper.

## 7. Monthly pipeline

genocide_monthly_global_pulse should become this bounded sequence:

1. camp_rework_clean_invalid_active_sites.
2. Loop global.genocide_active_camp_states and call camp_rework_apply_monthly_state_effects.
3. Loop global.camp_rework_active_countries and call camp_rework_apply_country_monthly_pressure.
4. If an active country is player-controlled and camp_repression_ledger_open is set, call camp_rework_rebuild_display_values.
5. Clear scratch buffers.

Within each state monthly call:

1. Validate state and responsible pointer.
2. Recalculate site type/phase values.
3. Resolve the responsible country's restricted tiers.
4. If a restricted phase is active, consume its monthly stockpile/logistics cost. If consumption fails, clear the active-use flag and retain contaminated/evidence facts.
5. Build one percentage, multiplier, cap, and reason with strict phase priority:
   restricted chemical; restricted biological; radicalized/extermination; gulag; experiment; forced labor/detention.
6. Call camp_rework_register_state_deaths once.
7. Apply non-Deaths output/burden/pressure changes.
8. Do not fire routine reports, leaks, sabotage, refugee, or flavor events.

## 8. Deaths and responsibility contract

### 8.1 Percentage path

camp_rework_register_state_deaths must translate its inputs to:

- chaos_state_deaths_percent
- chaos_state_deaths_mult
- chaos_state_deaths_cap_factor
- chaos_deaths_reason

It then calls chaos_meter_register_state_civilian_deaths_percent in state scope.

The existing helper:

- derives deaths from state_population_k;
- applies cap/random parameters;
- sets chaos_deaths_is_civilian = 1;
- sets chaos_deaths_apply_state_pop = 1;
- targets OWNER in the Deaths country ledger;
- calls chaos_meter_register_deaths;
- removes real state population through chaos_meter_apply_state_civilian_pop_loss_from_deaths_change.

Immediately afterward the adapter must copy chaos_deaths_change into both camp_site_last_month_deaths and genocide_last_state_deaths, then call the responsible-country credit adapter.

### 8.2 Victim versus perpetrator

Do not overwrite chaos_deaths_target_country with genocide_responsible_country in the percent path. OWNER is the population-bearing victim/accounting country at the moment of death. The stored responsible country receives:

- genocide_deaths;
- camp_population_loss_index trend;
- evidence;
- hidden condemnation;
- tribunal and visibility pressure.

This separation is required for occupied territories, Raj/colonial burden, Vichy/German collaboration, and state capture.

### 8.3 Exact event deaths

For an exact event-authored amount, camp_rework_register_exact_state_deaths sets:

- chaos_deaths_change = camp_exact_deaths
- chaos_deaths_is_civilian = 1
- chaos_deaths_apply_state_pop = 1
- chaos_deaths_target_country = OWNER
- chaos_deaths_has_target_country = 1
- chaos_deaths_reason = supplied reason

It calls chaos_meter_register_deaths and performs the same state/perpetrator post-processing. germany_mengele_register_experiment_deaths should use this adapter for state 88.

### 8.4 Biological contamination exception

apply_anthrax_contamination, apply_tularemia_contamination, apply_plague_contamination, and apply_smallpox_contamination already call bio_register_state_civilian_deaths, which calls the shared Deaths percent helper.

On initial biological escalation:

1. Consume the selected bomb stockpile.
2. Call exactly one disease contamination effect.
3. Copy its resulting chaos_deaths_change.
4. Credit the responsible country.
5. Do not also call camp_rework_register_state_deaths in that activation chain.

On later monthly active-site processing, use the consolidated camp monthly Deaths calculation and do not reapply the full contamination effect unless a bounded accident/escalation event explicitly requires it.

## 9. Abstract chemical/biological outcome tiers

Internal variable names:

- camp_chemical_killing_efficiency_tier
- camp_biological_killing_efficiency_tier

These are internal numeric selectors. Player-facing text should describe restricted-method severity, capability, or contaminated escalation, not an optimization curve.

### 9.1 Chemical tiers

Use only the live restricted bridge's supported nerve-agent equipment:

| Tier | Capability and stockpile gate | Existing equipment consumed | Outcome |
| --- | --- | --- | --- |
| 0 | No valid sarin/soman capability plus stockpile | none | No chemical override |
| 1 | sarin tech or sp_cw_sarin_program completed, and chemical_sarin_payload_cylinder_1 above a constant gate | chemical_sarin_payload_cylinder_1 | Abstract Deaths multiplier, short-term coercive-control pressure, contamination, evidence, stability/tribunal/visibility pressure |
| 2 | soman tech or sp_cw_soman_program completed, and chemical_soman_payload_cylinder_1 above a constant gate | chemical_soman_payload_cylinder_1 | Stronger abstract Deaths and control factors, larger contamination/evidence/instability/tribunal consequences |

Highest available valid tier wins. Tier resolution does not consume stockpile. Explicit activation and each continuing monthly use consume a separate constant-defined amount.

chemical_tabun_payload_cylinder_1 is not included in the initial camp tier resolver because its equipment is active = no, no live technology enable was found, and the existing genocide restricted-capacity trigger does not recognise it. Adding it silently would create a dead or inconsistent tier. It may be added only after its unlock/production path is made live and audited.

Chemical state contamination continues through chem_apply_state_contamination. Do not duplicate chemical formulas or delivery logic.

Equipment types are static tokens, not numeric variable values. camp_rework_consume_restricted_stockpile should use explicit tier branches with the existing equipment ids (or a reviewed meta_effect), and must negate a copied temporary amount before add_equipment_to_stockpile. It must not use unary minus on a variable token.

### 9.2 Biological tiers

| Tier | Capability and stockpile gate | Existing equipment consumed | Existing activation effect |
| --- | --- | --- | --- |
| 0 | No valid biological capability plus stockpile | none | none |
| 1 | anthrax_bomb_delivery_systems plus anthrax_bomb_1 and an explicit experiment route/facility | anthrax_bomb_1 | apply_anthrax_contamination |
| 2 | tularemia_bomb_delivery_systems plus tularemia_bomb_1 and route/facility | tularemia_bomb_1 | apply_tularemia_contamination |
| 3 | plague_bomb_delivery_systems plus plague_bomb_1 and route/facility | plague_bomb_1 | apply_plague_contamination |
| 4 | smallpox_bomb_delivery_systems plus smallpox_bomb_1 and route/facility | smallpox_bomb_1 | apply_smallpox_contamination |

The order follows the existing application Deaths percentages in chaos_meter_contamination_deaths_percent. Highest available valid tier wins.

### 9.3 Required adverse coupling

Every chemical or biological tier use must:

- consume stockpile and a logistics/administrative burden;
- raise camp_site_evidence_depth and camp_site_foreign_exposure;
- set camp_site_contaminated_evidence;
- raise camp_evidence_level, camp_stability_damage, camp_foreign_visibility, and camp_tribunal_severity;
- increase long-term local/national resistance pressure even if camp_coercive_control receives a short-lived positive factor;
- add appropriate hidden condemnation with restricted_site_operation or experiment_site context;
- become ineligible for AI when relevant caps, shortages, discovery, collapse, reform, or route restrictions apply.

No tier may improve deaths per unit of stockpile in player-facing terms. A higher tier is a more dangerous outcome package with higher costs and liabilities.

## 10. Script-constant schema

Keep shared tuning in common/script_constants/genocide_crisis_constants.txt unless a value is owned by the chemical or biological subsystem. All categories begin with an explicit schema.

Recommended categories:

| Category | Data type | Required keys |
| --- | --- | --- |
| camp_rework_site_type | int | enum keys from section 3.4 |
| camp_rework_phase | int | enum keys from section 3.4 |
| camp_rework_pool_type | int | enum keys from section 3.4 |
| camp_rework_band | int | enum keys from section 3.4 |
| camp_rework_action | int | enum keys from section 3.4 |
| camp_rework_common | fixed_point | value clamps, core-fallback factors, active/reform/evidence scaling, collaboration responsibility shares |
| camp_rework_death_percent | fixed_point | detention, forced_labor, gulag, radicalized, experiment, restricted_chemical, restricted_biological, famine, evidence_destruction |
| camp_rework_death_multiplier | fixed_point | reach, overextension, occupied_noncore, colonial, noncore, core_fallback, famine, experiment, contamination, permission, guards, supply, rail, chaos, retreat, relief, reform, chemical tier factors, biological tier factors, maximum |
| camp_rework_death_cap | fixed_point | phase-specific cap factors and hard maximum adapters |
| camp_rework_output | fixed_point | labor/output factors, guard relief, rail/logistics relief, overextension reduction, pool factors |
| camp_rework_pressure | fixed_point | resistance, stability, evidence, visibility, tribunal, hardliner, legitimacy, reform, contamination consequences |
| camp_rework_cost | fixed_point | proportional manpower/factory/stability/support burdens that are not integral counts |
| camp_rework_cost_int | int | infantry/support equipment, trucks, trains, convoys, cylinders, biological bombs, command/political costs |
| camp_rework_chemical | fixed_point | tier Deaths/control/evidence/contamination/tribunal factors |
| camp_rework_chemical_int | int | sarin/soman gates, activation consumption, monthly consumption |
| camp_rework_biological | fixed_point | tier Deaths/control/evidence/outbreak/tribunal factors |
| camp_rework_biological_int | int | anthrax/tularemia/plague/smallpox gates, activation consumption, monthly consumption |
| camp_rework_ai_weight | fixed_point | activation, expansion, route, shortage, discovery, reform, enemy-proximity, country factors |
| camp_rework_ai_cap | int | active, radicalized, experiment, restricted, project-cycle caps by country/group |
| camp_rework_pool_score | fixed_point | occupied_noncore, colonial_or_subject, noncore_integrated, periphery_security, core_fallback and contextual modifiers |
| camp_rework_display_threshold | fixed_point | low/guarded/high/critical thresholds for each displayed family |
| camp_rework_gui | int | maximum pool rows, active-site rows, country-value rows |
| camp_rework_mission_days | int | all accepted mission/timed-chain durations |
| camp_rework_schema | int | current migration version |

Do not mix int and fixed_point values in one schema. Do not assume constant: tokens work in every duration field; copy duration constants into a normal or temporary variable when the target field requires a variable.

Existing genocide_death_percent, genocide_death_cap, genocide_death_multiplier, genocide_crisis_value, genocide_condemnation, genocide_chemical_bridge, and genocide_ai_* remain until their call sites are migrated. Move or map values deliberately; do not leave two independently tunable copies.

## 11. Germany, Japan, and Soviet integration

### Germany/Mengele

- Treat mengele_autonomy and mengele_permission_level as inputs to site Deaths/evidence/overstretch.
- Keep genocide_auschwitz_experiment_site and genocide_ss_laboratory_site as state traits.
- Refactor germany_mengele_register_experiment_deaths through the exact state Deaths adapter.
- Keep germany_mengele_add_autonomy as the only autonomy mutation helper.
- Existing extermination registration/monthly hooks that add autonomy should be routed once per material site action/monthly state, not duplicated by overlapping monthly handlers.
- Preserve state 88 and current emergency state-loss/coup routing.

### Japan/Ishii

Add country state owned by the Japan package:

- ishii_influence
- kwantung_medical_autonomy
- occupation_experiment_reach
- epidemic_accident_risk
- camp_japan_ishii_program_active
- camp_japan_army_review_active

The startup scientist flag chaosx_scientist_jap_shiro_ishii is evidence that the named scientist exists, but monthly runtime should read the explicit country route flags/values. Use genocide_japanese_biowarfare_atrocity_site as the state trait and the biological tier resolver for stockpile/capability.

### Soviet Union

- Read vanilla SOV_paranoia only when SOV_paranoia_system_active_flag is set.
- Use vanilla SOV_paranoia_* effects for explicit paranoia changes.
- Keep soviet_collapse_apply_genocide_gulag_repression_memory as the bridge to Union Crisis/collapse components.
- Apply that bridge on activation, expansion, quota, deportation, famine, or purge actions; do not call it once per active gulag state every monthly pulse.
- Resolve a suppression-relief cap through camp_rework_ai_cap/country pressure so high Union Crisis threat cannot be erased by repeated repression.
- Preserve existing Soviet decision ids during migration: sov_expand_gulag_network, sov_deport_suspected_opposition_groups, sov_confiscate_food_from_disloyal_regions, sov_purge_camp_administrators, sov_raise_forced_labor_quotas, and sov_destroy_gulag_records.

## 12. AI selection and caps

### 12.1 Selection

camp_rework_build_pool_arrays runs only when a player opens/rebuilds the ledger or an AI is about to perform a camp action. It may iterate that country's owned/controlled states, but it must not be called for all countries every month.

Build five temporary or country scratch scope arrays:

1. camp_pool_occupied_noncore_states
2. camp_pool_colonial_or_subject_states
3. camp_pool_noncore_integrated_states
4. camp_pool_periphery_security_states
5. camp_pool_core_fallback_states

camp_rework_select_ai_state chooses randomly from the first nonempty valid array in that order. A country-specific pool trigger may further restrict candidates. Core fallback requires its explicit route gate and punitive penalties.

AI uses the same eligibility triggers and action effects as the player. It does not set camp_selected_state_id and does not click scripted-GUI controls.

### 12.2 Cap dimensions

camp_rework_apply_ai_cap must resolve, at minimum:

- camp_ai_active_site_cap
- camp_ai_radicalized_site_cap
- camp_ai_experiment_site_cap
- camp_ai_restricted_site_cap
- camp_ai_active_project_cap
- camp_ai_can_expand

Caps come from camp_rework_ai_cap country/group keys and are then reduced by manpower, train, truck, convoy, supply, stability, overextension, discovery, enemy proximity, capitulation, and reform conditions.

Required group keys:

- germany_active/radicalized/experiment/restricted
- japan_active/radicalized/experiment/restricted
- soviet_active/radicalized/restricted
- uk_active/project
- usa_active/project
- france_active/project
- italy_active/project
- belgium_active/project
- generic_authoritarian_active/radicalized/restricted
- generic_democratic_active

The implementation/balance owner should assign and validate initial numbers. This architecture deliberately does not freeze untested cap values.

AI must hard-block:

- dormant-only routes;
- invalid or already active states;
- over-cap actions;
- protected-class targeting;
- chemical/biological use without both capability and consumable stockpile;
- democratic radicalization without the explicit extreme emergency route;
- new expansion during reform/dismantlement;
- repeated restricted escalation while an active restricted site is already at cap.

## 13. Repression Ledger data architecture

### 13.1 GUI ids and contexts

Implement two linked scripted GUIs:

1. repression_ledger_category_scripted_gui
   - context_type = decision_category
   - compact summary and open button
   - attach to genocide_crisis_category, imperial_occupation_crisis, and gulag_and_mass_repression_system

2. repression_ledger_window_scripted_gui
   - context_type = player_context
   - parent_window_token = top_bar
   - window_name = repression_ledger_window
   - visible while country flag camp_repression_ledger_open is set
   - ai_enabled = no

Recommended UI state:

- camp_repression_ledger_open
- camp_ledger_tab_overview
- camp_ledger_tab_state_pools
- camp_ledger_tab_sites
- camp_ledger_tab_country
- camp_ledger_tab_discovery
- camp_selected_state_id
- camp_gui_selected_pool_row
- camp_gui_selected_site_row

The open effect sets the default tab, calls camp_rework_rebuild_display_values, then opens the player-context window. The close effect clears open/tab flags, selected state, display scratch values, and all GUI arrays.

### 13.2 Required display values

camp_rework_rebuild_display_values owns:

- display_camp_network_reach
- display_camp_active_site_count
- display_camp_concentration_sites
- display_camp_radicalized_sites
- display_camp_gulag_sites
- display_camp_experiment_sites
- display_camp_contaminated_evidence_sites
- display_camp_labor_output
- display_camp_coercive_control
- display_camp_population_loss_pressure
- display_camp_stability_drag
- display_camp_resistance_pressure
- display_camp_guard_burden
- display_camp_rail_burden
- display_camp_evidence_risk
- display_camp_foreign_visibility
- display_camp_tribunal_severity
- display_camp_reform_pressure
- display_camp_overstretch

Country-specific display bands read existing country values where available, including mengele_autonomy and mengele_permission_level, and new Japan/Soviet/colonial route values.

### 13.3 Required aligned arrays

Country-scoped arrays:

- camp_gui_pool_state_ids
- camp_gui_pool_type_ids
- camp_gui_pool_eligibility_ids
- camp_gui_active_site_state_ids
- camp_gui_active_site_type_ids
- camp_gui_active_site_evidence_ids
- camp_gui_active_site_pressure_ids
- camp_gui_active_site_action_ids
- camp_gui_country_value_ids
- camp_gui_country_value_band_ids

Every rebuild begins by clearing every aligned array. Every row append writes every column in that row. Store numeric state ids for GUI/localisation and use var:camp_selected_state_id to enter state scope for actions.

Also write:

- camp_gui_pool_row_count
- camp_gui_active_site_row_count
- camp_gui_country_value_row_count

Bound each list with camp_rework_gui constants. Pool rows come only from valid country pools. Active rows come only from camp_active_site_states/camp_evidence_site_states as appropriate. Never add every world state.

### 13.4 Rebuild order

camp_rework_rebuild_display_values:

1. Clean invalid registrations.
2. Recalculate site counts by type.
3. Recalculate country-specific values.
4. Recalculate pool availability counts.
5. Recalculate output, burden, damage, evidence, and reform values.
6. Validate camp_selected_state_id.
7. Rebuild aligned GUI arrays.
8. Refresh scripted-localisation bands.

Call it on:

- ledger open;
- relevant GUI/decision click;
- state-control change for affected player country;
- discovery;
- dismantlement completion;
- regime change/annexation;
- host monthly pulse only for a country whose ledger is open.

Do not use event targets in scripted GUI. The offline wiki explicitly states they are not available there, and regular event targets would not persist across clicks anyway.

## 14. Discovery and responsibility lifecycle

camp_rework_apply_discovery must preserve the current physical-evidence model:

1. Validate unresolved evidence in the state.
2. Save only short-lived event targets required by the current event chain.
3. Set genocide_site_discovered.
4. Calculate severity from site type, evidence depth, failed/successful cover-up, experiment/contamination traits, actual deaths, network reach, repeat discovery, and foreign visibility.
5. Expose hidden atrocity and cover-up buckets with existing condemnation_expose_hidden_bucket calls.
6. Apply public condemnation to var:genocide_responsible_country.
7. If camp_site_secondary_responsible_country exists, apply the constant-defined collaborator share separately; do not overwrite the primary pointer.
8. Update camp_foreign_visibility, camp_tribunal_severity, camp_reform_pressure, and existing discovery counters.
9. Fire only bounded first-discovery, major-news, threshold, or tribunal events.
10. Unregister only if the site is physically inactive. Discovery by itself does not stop an active site.

On state control change, the new controller is the discoverer or liberator, not automatically the perpetrator. Responsibility changes only through an explicit reuse/reactivation effect. That effect must first resolve or preserve old evidence, then assign a new primary pointer.

If the stored responsible country no longer exists, retain the pointer/evidence and mark discovery normally, but do not silently transfer condemnation to the current owner. A successor-liability or postwar-settlement decision may redirect accountability only through an explicit country-specific rule. Annexation cleanup stops active use and removes active-array membership; it does not erase the historical pointer.

## 15. Versioned migration and implementation order

### Tranche 1: schema and compatibility

1. Add enums/constants and camp_rework_schema.current.
2. Add camp_rework_initialize_country_values.
3. Add a versioned global migration variable, global.camp_rework_schema_version.
4. Keep all old helpers callable.

### Tranche 2: one-time migration

1. On startup, when schema version is behind, clear/rebuild global.genocide_active_camp_states and new country arrays once.
2. Scan existing camp buildings and specialised state flags.
3. Leave genocide_historical_quiet_camp sites dormant.
4. Preserve existing genocide_responsible_country where valid.
5. Infer responsibility only for a legacy active site with no pointer, using the current controller/owner under a documented migration-only rule.
6. Rebuild legacy counts from registered states.
7. Set the schema version only after the pass finishes.

### Tranche 3: registry and monthly runtime

1. Add register/unregister/cleanup effects and triggers.
2. Convert every construction/activation/dismantlement/condemnation cleanup call site.
3. Make concentration-camp construction decision-owned.
4. Remove the recurring every-country registration scan.
5. Consolidate monthly Deaths into one call per active state.

### Tranche 4: Deaths, discovery, and restricted tiers

1. Add percentage and exact Deaths adapters.
2. Convert Germany/Mengele exact deaths.
3. Remove biological activation double-registration.
4. Add chemical/biological tier resolution and stockpile consumption.
5. Extend discovery severity and collaborator responsibility.

### Tranche 5: country systems and AI

1. Route Germany, Japan, Soviet, U.K./Raj, U.S., France/Vichy, Italy, Belgium, and generic actions through shared helpers.
2. Add country pools and cap resolution.
3. Add AI target selection using priority arrays.
4. Add regime-change/reform/annex cleanup hooks.

### Tranche 6: full GUI

1. Stabilise final display ids and arrays.
2. Implement the compact category header.
3. Implement the full player-context repression_ledger_window.
4. Wire selected-state actions and AI-equivalent effects.
5. Finalise sprites/localisation only after dimensions and ids are stable.

### Tranche 7: compatibility retirement

1. Search all old helper/variable call sites.
2. Remove compatibility adapters only when no external caller remains.
3. Update genocide-crisis docs, dynamic-helper docs if a genuinely generic helper was added, event logs/details, asset manifest, and workbook facts.
4. Run country, AI, GUI, Deaths, discovery, and cleanup audits before completion.

## 16. Risks and required tests

| Risk | Required evidence |
| --- | --- |
| Duplicate array entries | Repeated activation/registration leaves one global and one country entry |
| Stale states after destruction/dismantlement | Next cleanup pass removes active membership, active modifiers, counts, and country membership while retaining unresolved evidence |
| Victim/perpetrator inversion | Occupied non-core state loses population and OWNER receives Deaths country total; stored responsible country receives camp deaths/evidence/condemnation |
| Multiple monthly Deaths calls | A state with extermination, experiment, and restricted traits produces one monthly row with the highest-priority reason |
| Biological double deaths | Initial contamination produces the one existing bio Deaths call and one responsibility credit |
| Free restricted continuation | Monthly stockpile shortage stops the active override and preserves evidence/contamination |
| GUI array drift | Every aligned array has the same row count after open, click, control change, dismantlement, and close |
| Invalid selected state | camp_selected_state_id clears when control/eligibility changes |
| Event-target misuse | No persistent/global event target is used for GUI selection; discovery targets remain short-lived |
| Dormant noise | Historical quiet sites stay unregistered and generate no monthly pressure/events |
| World-scan regression | Monthly runtime loops registered states/countries only; one-time schema migration is the only broad reconstruction |
| Germany bypass | germany_mengele_register_experiment_deaths updates real state population, Deaths history, state last deaths, and responsible-country totals |
| Soviet runaway | The collapse-memory bridge fires on material actions, not per state/month; high Union Crisis suppression cap holds |
| Core fallback abuse | Output is lower and legitimacy/stability/reform/backlash costs are higher; AI selects it only when all higher pools are empty and route permits |
| Annexed perpetrator | Active use stops, unresolved evidence and the original responsibility pointer remain, and no current owner is blamed implicitly |

## 17. File ownership map for implementation

Primary:

- common/script_constants/genocide_crisis_constants.txt
- common/scripted_triggers/genocide_crisis_triggers.txt
- common/scripted_effects/genocide_crisis_effects.txt
- common/on_actions/genocide_crisis_on_actions.txt
- common/on_actions/chaosx_on_actions_chaos_meter.txt
- common/decisions/genocide_crisis_decisions.txt
- common/decisions/categories/genocide_crisis_categories.txt
- common/ai_strategy/genocide_crisis_ai_strategy.txt
- common/scripted_guis/genocide_crisis_scripted_guis.txt
- interface/genocide_crisis.gui
- interface/genocide_crisis.gfx

Bridges requiring coordinated review:

- common/scripted_effects/chaos_meter_effects.txt and common/script_constants/chaos_meter_constants.txt only if new Deaths reason ids are introduced
- common/scripted_effects/condemnation_response_effects.txt
- common/scripted_effects/germany_mengele_effects.txt
- common/scripted_triggers/germany_mengele_triggers.txt
- common/scripted_effects/biowarfare_effects.txt
- common/scripted_effects/chemical_ability_effects.txt
- common/scripted_effects/005_soviet_collapse_effects.txt
- country-specific decision/idea/focus or route-hook files

The camp-owned effects belong in genocide_crisis_effects.txt. Do not add them to chaosx_dynamic_effects.txt unless an effect is genuinely reusable outside the camp/repression system; if that happens, update chaosx_dynamic_effects.md in the same change.

## 18. Parent implementation decisions requiring explicit confirmation

1. Approve decision-only construction for concentration_camp so the recurring every-country scan can be removed.
2. Approve the optional secondary responsibility pointer for explicit collaboration routes.
3. Decide whether to add dedicated Deaths reasons for camp chemical and camp biological atrocities or reuse current reasons with contextual tooltips.
4. Assign initial numeric AI caps and balance constants after scenario review.
5. Confirm final GUI dimensions and stable sprite paths before asset generation.

No fallback or simplification is embedded in this handoff. The only unresolved choices above are implementation-policy or balance decisions that must be recorded before their tranche is claimed complete.
