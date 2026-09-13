# Event 35 decision and mission implementation handoff

## Scope and status

This handoff records the original bounded decision/mission patch. Parent-owned scripted helpers, localisation, GFX registration, costs, selected-center execution, mission lifecycle, and AI integration are now present.

The remaining body preserves the worker's implementation-time evidence and requests. Statements that integration was blocked or a parent helper was unresolved describe the original handoff state, not the current runtime source.

No existing Event 35 decision or category file was present before this patch.

Concurrent Event 35 constants and scripted triggers were inspected read-only and remain untouched.

## Changed files

- `common/decisions/categories/035_great_depression_categories.txt`
- `common/decisions/035_great_depression_decisions.txt`
- `docs/plans/035_great_depression_plans/subagent_handoffs/decision_mission_implementation.md`

The category id is `great_depression_category`.

The category uses `GFX_decision_category_great_depression` as its small icon and `GFX_decision_cat_picture_great_depression` as its category picture.

The category uses no scripted GUI because the accepted Event 35 design is one ordinary category with a compact dynamic description.

## Before and after behavior

Before this patch, Event 35 had no ordinary decision category, no decision surface, no selected-center flow, and no decision-owned missions.

After this patch, an active coherent Event 35 crisis can expose the ordinary category and delegate phase, doctrine, target, cost, effect, AI, and cleanup decisions to parent-owned Event 35 helpers.

The category remains visible while empty so the dynamic header can still communicate Severity, band, trend, phase, doctrine, next threshold, causes, selected center, and active objective.

The six opening doctrine choices are episode-scoped through parent visibility and receipt helpers, so `fire_only_once = no` preserves repeatability across later crises.

The selected-center selector is state-targeted and human-facing actions show only the selected state.

AI state-targeted actions remain open to every valid center and use target-value modifiers, so AI does not depend on the human selector.

All instant decisions use `custom_cost_trigger` and `custom_cost_text` and delegate the real debit to a parent scripted effect.

No decision uses a direct `cost =` field, so there is no hidden political-power-only shop or double debit in this surface.

Missions are non-selectable, activate through parent gates, auto-complete through objective triggers, and have separate complete, timeout, and cancellation helper calls.

## Decision ids

### Opening doctrine choices

- `great_depression_choose_emergency_public_works`
- `great_depression_choose_rescue_strategic_industry`
- `great_depression_choose_stabilize_finance_and_trade`
- `great_depression_choose_austerity_and_retrenchment`
- `great_depression_choose_direct_state_planning`
- `great_depression_choose_let_the_market_clear`

### Shared national and center flow

- `great_depression_cabinet_review`
- `great_depression_emergency_policy_review`
- `great_depression_emergency_relief_allocation`
- `great_depression_request_foreign_support`
- `great_depression_select_depression_center`
- `great_depression_protect_depression_center`
- `great_depression_reopen_idled_plants`
- `great_depression_rebuild_shuttered_center`
- `great_depression_restructure_or_consolidate_center`
- `great_depression_abandon_depression_center`

### Emergency Public Works

- `great_depression_launch_regional_works_program`
- `great_depression_start_national_employment_guarantee`
- `great_depression_convert_works_into_lasting_capacity`

### Rescue Strategic Industry

- `great_depression_designate_strategic_plant_network`
- `great_depression_guarantee_essential_orders`
- `great_depression_consolidate_failing_industry`

### Stabilize Finance and Trade

- `great_depression_declare_temporary_bank_holiday_and_audit`
- `great_depression_recapitalize_viable_institutions`
- `great_depression_negotiate_clearing_and_import_agreements`
- `great_depression_establish_durable_credit_guarantee`

### Austerity and Retrenchment

- `great_depression_balance_emergency_budget`
- `great_depression_restructure_public_obligations`
- `great_depression_retrench_relief_administration`
- `great_depression_restore_ordinary_budget_rules`

### Direct State Planning

- `great_depression_establish_emergency_production_board`
- `great_depression_nationalize_failing_industry`
- `great_depression_ration_strategic_inputs`
- `great_depression_start_national_recovery_plan`

### Let the Market Clear

- `great_depression_withdraw_emergency_support`
- `great_depression_auction_or_reorganize_failed_assets`
- `great_depression_remove_emergency_controls`
- `great_depression_begin_cleared_economy_certification`

### Evolution I actions

- `great_depression_ring_fence_domestic_finance`
- `great_depression_extend_emergency_credit`
- `great_depression_shift_import_and_contract_dependence`
- `great_depression_abandon_distressed_market`
- `great_depression_acquire_distressed_assets`
- `great_depression_coordinate_international_rescue`
- `great_depression_request_emergency_credit`
- `great_depression_offer_debt_standstill`
- `great_depression_sell_distressed_assets`
- `great_depression_establish_clearing_bloc`
- `great_depression_accept_external_supervision`
- `great_depression_restrict_capital_outflows`
- `great_depression_prioritize_domestic_recovery`
- `great_depression_offer_boom_supply_contract`
- `great_depression_support_contagion_source`
- `great_depression_withdraw_from_distressed_market`
- `great_depression_exploit_supply_gap`

### Evolution II actions

- `great_depression_negotiate_with_strike_committees`
- `great_depression_national_employment_compact`
- `great_depression_deploy_security_forces`
- `great_depression_break_the_occupations`
- `great_depression_recognize_workplace_or_regional_councils`
- `great_depression_form_an_emergency_government`
- `great_depression_nationalize_or_socialize_occupied_industry`
- `great_depression_guarantee_property_and_credit`

### Evolution III actions

- `great_depression_regional_clearing_agreement`
- `great_depression_coordinated_public_works_and_reconstruction`
- `great_depression_international_debt_conference`
- `great_depression_protectionist_bloc`
- `great_depression_competitive_devaluation_or_currency_break`
- `great_depression_reconstruction_supplier_compact`
- `great_depression_global_recovery_conference`
- `great_depression_emergency_trade_clearing`
- `great_depression_reconstruction_and_employment_fund`
- `great_depression_protect_domestic_market`
- `great_depression_coordinate_industrial_demand`
- `great_depression_withdraw_from_international_commitments`

## Mission ids and quality notes

All missions belong to `great_depression_category` and are owned by the affected `ROOT` country.

The selected-center and source or partner context is stored and validated by parent Event 35 helpers rather than by a second GUI or a public meter.

| Mission id | Region or context | Requirement trigger | Duration constant | Success and failure | Duplicate and invalid-context handling |
| --- | --- | --- | --- | --- | --- |
| `great_depression_halt_the_panic` | ROOT national opening | `great_depression_halt_the_panic_objective_is_met` after an opening cause and viable center response | `great_depression_event.opening_mission_days` | `great_depression_complete_halt_the_panic` or `great_depression_timeout_halt_the_panic` | Activation gate and episode receipt prevent duplicates, while context cancellation calls `great_depression_cancel_halt_the_panic` |
| `great_depression_keep_essential_freight_moving` | ROOT transport and selected center | `great_depression_keep_essential_freight_moving_objective_is_met` with transport and reserve proof | `great_depression_event.freight_mission_days` | `great_depression_complete_keep_essential_freight_moving` or `great_depression_timeout_keep_essential_freight_moving` | Freight context, selected center validity, and active-cap gate prevent stale or repeated missions |
| `great_depression_reopen_depression_center` | Parent-stored selected center state | `great_depression_reopen_depression_center_objective_is_met` for the doctrine-specific project | `great_depression_event.center_mission_days` | `great_depression_complete_reopen_depression_center` or `great_depression_timeout_reopen_depression_center` | Center context cancellation clears the project without treating state loss as player failure |
| `great_depression_prevent_a_relapse` | ROOT national stabilization | `great_depression_prevent_a_relapse_objective_is_met` keeps Severity below the relapse threshold and completes consolidation | `great_depression_event.relapse_mission_days` | `great_depression_complete_prevent_a_relapse` or `great_depression_timeout_prevent_a_relapse` | Activation receipt and relapse-context validation prevent overlap with a closed episode |
| `great_depression_maximum_severity_emergency` | ROOT Economic Paralysis | `great_depression_maximum_severity_emergency_objective_is_met` after an emergency response lowers the crisis | `great_depression_event.maximum_emergency_days` | `great_depression_complete_maximum_severity_emergency` or `great_depression_timeout_maximum_severity_emergency` | Emergency gate replaces ordinary missions and the cooldown constant blocks emergency spam |
| `great_depression_prevent_national_breakdown` | ROOT baseline political warning | `great_depression_prevent_national_breakdown_objective_is_met` resolves the warning, center response, and one viable action | `great_depression_event.breakdown_mission_days` | `great_depression_complete_prevent_national_breakdown` or `great_depression_timeout_prevent_national_breakdown` | Context helper must mutually exclude Evolution II replacements and cancel on invalid country state |
| `great_depression_contain_financial_contagion` | ROOT and inherited financial links | `great_depression_contain_financial_contagion_objective_is_met` proves exposure containment | `great_depression_event.center_mission_days` | `great_depression_complete_contain_financial_contagion` or `great_depression_timeout_contain_financial_contagion` | Evolution activation receipt and link validation prevent duplicate source-target pressure |
| `great_depression_prevent_general_strike` | ROOT social movement | `great_depression_prevent_general_strike_objective_is_met` settles or contains the active movement | `great_depression_event.center_mission_days` | `great_depression_complete_prevent_general_strike` or `great_depression_timeout_prevent_general_strike` | Social actor context prevents overlap and cancellation avoids failure when the actor disappears |
| `great_depression_international_reconstruction` | ROOT global contraction | `great_depression_international_reconstruction_objective_is_met` proves a valid reconstruction arrangement | `great_depression_event.center_mission_days` | `great_depression_complete_international_reconstruction` or `great_depression_timeout_international_reconstruction` | Global-stage and partner receipt helpers prevent duplicate reconstruction claims |
| `great_depression_national_employment_guarantee` | ROOT public-works employment | `great_depression_national_employment_guarantee_objective_is_met` proves employment and center conditions | `great_depression_event.opening_mission_days` | `great_depression_complete_national_employment_guarantee` or `great_depression_timeout_national_employment_guarantee` | Activation gate shares the active mission cap and cancels on a lost employment context |
| `great_depression_complete_national_recovery_plan` | ROOT planning route | `great_depression_complete_national_recovery_plan_objective_is_met` proves planning targets and stable Severity | `great_depression_event.recovery_proof_days` | `great_depression_complete_complete_national_recovery_plan` or `great_depression_timeout_complete_national_recovery_plan` | Parent receipt blocks repeat proof and context cancellation clears stale planning state |
| `great_depression_certify_cleared_economy` | ROOT market-clearing route | `great_depression_certify_cleared_economy_objective_is_met` proves failed obligations and plants are resolved | `great_depression_event.recovery_proof_days` | `great_depression_complete_certify_cleared_economy` or `great_depression_timeout_certify_cleared_economy` | Liquidation receipt and protected-floor validation prevent repeated certification |
| `great_depression_coordinate_international_rescue_mission` | ROOT and rescue partner context | `great_depression_coordinate_international_rescue_objective_is_met` proves the rescue package | `great_depression_event.center_mission_days` | `great_depression_complete_coordinate_international_rescue` or `great_depression_timeout_coordinate_international_rescue` | Partner receipt, active-cap, and context validation prevent aid farming |
| `great_depression_restore_essential_production` | ROOT and selected or registered center | `great_depression_restore_essential_production_objective_is_met` proves essential production recovery | `great_depression_event.center_mission_days` | `great_depression_complete_restore_essential_production` or `great_depression_timeout_restore_essential_production` | Center registry receipt prevents repeated free production restoration |
| `great_depression_emergency_government_mandate` | ROOT Evolution II emergency government | `great_depression_emergency_government_mandate_objective_is_met` proves the mandate and essential response | `great_depression_event.breakdown_mission_days` | `great_depression_complete_emergency_government_mandate` or `great_depression_timeout_emergency_government_mandate` | Social-stage receipt and active-cap prevent repeated emergency government activation |

The player-facing aliases expected in localisation are `Put the Depression Centers Back to Work` for `great_depression_reopen_depression_center`, `Hold the Social Peace` for `great_depression_prevent_general_strike`, `Prove the Stabilization` for `great_depression_prevent_a_relapse`, and `Prove the Recovery` for the appropriate recovery proof mission.

## Cost and requirement clarity

There are 74 custom-cost decisions and one cost-free state selector.

Every custom-cost decision has one matching `custom_cost_trigger` and `custom_cost_text` pair.

The parent helper for each family must calculate a dynamic cost from usable capacity and enforce `constant:great_depression_event.maximum_spendable_cost_types` as a hard maximum of four spendable types.

Non-consumed requirements such as a selected state, a valid partner, a route, an active evolution, or a stage are kept in `visible`, `available`, and target triggers instead of being mixed into the cost string.

| Cost family | Decision ids using it | Parent payment trigger | Spendable types permitted by this surface |
| --- | --- | --- | --- |
| Doctrine choice | Six `great_depression_choose_*` ids | `great_depression_can_pay_doctrine_choice` | Political power for cabinet authority, civilian commitment, stability or war support only when the helper has a genuine route reason |
| Policy review | `great_depression_cabinet_review`, `great_depression_emergency_policy_review` | `great_depression_can_pay_policy_review` | Political power plus civilian or administrative commitment, capped at four |
| Emergency relief | `great_depression_emergency_relief_allocation` | `great_depression_can_pay_emergency_relief` | Civilian commitment, manpower, support equipment, fuel, or stability, capped at four |
| Foreign support | `great_depression_request_foreign_support` | `great_depression_can_pay_foreign_support` | Convoys, fuel, civilian commitment, political authority, or war support, capped at four |
| Center protection | `great_depression_protect_depression_center` | `great_depression_can_pay_center_protection` | Civilian commitment, trains or trucks, support equipment, and fuel, with no fifth type |
| Center reopening | `great_depression_reopen_idled_plants`, `great_depression_rebuild_shuttered_center` | `great_depression_can_pay_center_reopen` | Civilian commitment, trains or trucks, support equipment, and manpower, with no fifth type |
| Center restructuring | `great_depression_restructure_or_consolidate_center` | `great_depression_can_pay_center_restructure` | Civilian commitment, military output sacrifice, trains or trucks, and support equipment, with no fifth type |
| Center abandonment | `great_depression_abandon_depression_center` | `great_depression_can_pay_center_abandon` | Political authority, civilian commitment, stability, or war support, capped at four |
| Public works | Public Works doctrine actions | `great_depression_can_pay_public_works` | Civilian commitment, trains or trucks, support equipment, and manpower or fuel, capped at four |
| Strategic rescue | Strategic Industry doctrine actions | `great_depression_can_pay_strategic_rescue` | Civilian commitment, military output sacrifice, fuel, and support equipment or trains, capped at four |
| Finance and trade | Finance doctrine actions | `great_depression_can_pay_finance_trade` | Civilian commitment, convoys, fuel, political authority, or stability, capped at four |
| Austerity | Austerity doctrine actions | `great_depression_can_pay_austerity` | Political authority, stability, war support, and civilian commitment, capped at four |
| State planning | Planning doctrine actions | `great_depression_can_pay_state_planning` | Civilian commitment, military output sacrifice, political authority, and support equipment, capped at four |
| Market clearing | Market doctrine actions | `great_depression_can_pay_market_clear` | Civilian commitment, stability, war support, and political authority, capped at four |
| Contagion | Evolution I actions | `great_depression_can_pay_contagion` | Civilian commitment, convoys, fuel, political authority, or stability, capped at four |
| Social response | Evolution II actions | `great_depression_can_pay_social_response` | Manpower, support equipment, civilian commitment, stability, or war support, capped at four |
| Global reconstruction | Evolution III actions | `great_depression_can_pay_global_reconstruction` | Civilian commitment, convoys, fuel, political authority, or war support, capped at four |

The parent payment helpers should use the Event 35 base constants `base_civilian_cost`, `base_military_cost`, `base_train_cost`, `base_truck_cost`, `base_convoy_cost`, `base_support_equipment_cost`, `base_fuel_cost`, `base_manpower_cost`, `base_political_power_cost`, `base_stability_cost`, and `base_war_support_cost`.

Each cost localisation family requires the normal key, `_blocked`, and `_tooltip` variants with `£GFX_*` texticons for every spendable value.

No literal resource names, prose padding, or hidden fifth cost appears in the decision source.

## AI profiles, target validity, and route locks

The six doctrine decisions encode profile ordering through additive weights and use parent profile triggers.

The intended ordering anchors are Public Works `14`, Finance `12`, Planning `10`, Austerity `8`, Market `6`, and Strategic `4` for the relief-oriented balanced choice.

Wartime strategic choices use Strategic `14`, Planning `12`, Finance `10`, Public Works `8`, Austerity `6`, and Market `2`.

Blockade choices use Planning `14`, Public Works `12`, Strategic `10`, Austerity `8`, Finance `4`, and Market `2`.

Fiscal choices use Austerity `14`, Finance `12`, Market `10`, Public Works `8`, Planning `6`, and Strategic `4`.

Social-strain choices use Public Works `14`, Planning `12`, Strategic `10`, Finance `8`, Austerity `4`, and Market `1`.

Private-capacity choices use Market `14`, Finance `12`, Austerity `10`, Public Works `8`, Strategic `6`, and Planning `4`.

Action AI weights also require parent affordability, urgency, fiscal, freight, social, blockade, recovery, and safety triggers, so a profile never overrides material invalidity.

Targeted country decisions use target triggers for real countries and partner relationships.

Targeted state decisions use `state_target = any_controlled_state`, `on_map_mode = map_and_decisions_view`, and state-specific target triggers.

Market liquidation, security force, currency-break, and boom-supplier actions include explicit parent safety or route-lock helpers that can return a zero AI factor.

Center AI modifiers use `great_depression_target_weight.base`, `major`, `connected_state`, `stable_country`, and `great_depression_scaling.center_industry_weight` where applicable.

The required named scenario set is `TGT-01` through `TGT-10`, `DOC-01` through `DOC-07`, `ACT-01` through `ACT-05`, `CTG-01` through `CTG-10`, `BDP-01` through `BDP-04`, `SOC-01` through `SOC-05`, `GLB-01` through `GLB-10`, and `EVO-01` through `EVO-08`.

Those scenarios require a complete parent helper and cost implementation before exact probability or timing claims are valid.

## Parent helper dependency contract

The only currently defined Event 35 decision-surface trigger found during inspection is `great_depression_active_crisis_is_coherent`.

The source calls the following parent-owned root surface and visibility triggers, which are currently unresolved in the inspected repository:

- `great_depression_is_active_decision_surface`
- `great_depression_should_show_doctrine_choice`
- `great_depression_should_show_cabinet_review`
- `great_depression_should_show_emergency_policy_review`
- `great_depression_should_show_emergency_relief`
- `great_depression_should_show_foreign_support`
- `great_depression_should_show_center_selection`
- `great_depression_should_show_center_actions`
- `great_depression_should_show_doctrine_primary_actions`
- `great_depression_doctrine_is_*`
- `great_depression_should_show_*` for each action id
- `great_depression_*_surface_is_active` for Financial Contagion, Social Collapse, and Second Great Depression

Every national action calls a clearly named `great_depression_<action>` scripted effect.

Every state action calls the same named effect inside `FROM` state scope so the parent can read the selected state and `ROOT` country.

Every country-targeted action calls the same named effect inside `FROM` country scope so the parent can debit the provider or recipient correctly.

Every action `available` block calls `great_depression_action_slot_is_open` plus a named `great_depression_can_start_*` or target-specific equivalent.

The parent must implement the target triggers named in the decision file, including center validity, partner validity, creditor or provider validity, Event 34 supplier validity, and Evolution II occupied-industry validity.

The parent must implement the `great_depression_can_pay_*` triggers and the corresponding dynamic cost effects for all 17 cost families listed above.

Mission `N` expects `great_depression_should_activate_N`, `great_depression_N_objective_is_met`, `great_depression_N_context_is_valid`, `great_depression_complete_N`, `great_depression_timeout_N`, and `great_depression_cancel_N`.

The mission context helper must enforce the shared active-objective cap and mutual exclusion between baseline National Breakdown and Evolution II replacement missions.

The parent must clear the selected-center pointer on transfer, recapture, annexation, recovery, invalid state scope, and crisis closure.

The parent must release reserved resources exactly once on cancellation or proven unspent timeout and must not refund consumed resources.

The Event 34 supplier adapter is required by `great_depression_offer_boom_supply_contract` and `great_depression_reconstruction_supplier_compact`.

## Localisation and icon dependencies

Localisation was intentionally not edited because it is outside this subagent ownership.

The parent localisation pass must add `great_depression_category`, `great_depression_category_desc`, every decision id and `_desc`, every mission id and `_desc`, and concise blocked-reason tooltips.

The category description must be dynamic and compact, with no paragraph above the action list.

The cost keys are `great_depression_cost_doctrine_choice`, `great_depression_cost_policy_review`, `great_depression_cost_emergency_relief`, `great_depression_cost_foreign_support`, `great_depression_cost_center_protection`, `great_depression_cost_center_reopen`, `great_depression_cost_center_restructure`, `great_depression_cost_center_abandon`, `great_depression_cost_public_works`, `great_depression_cost_strategic_rescue`, `great_depression_cost_finance_trade`, `great_depression_cost_austerity`, `great_depression_cost_state_planning`, `great_depression_cost_market_clear`, `great_depression_cost_contagion`, `great_depression_cost_social_response`, and `great_depression_cost_global_reconstruction`.

Each cost key needs normal, `_blocked`, and `_tooltip` forms and must use texticons rather than literal resource labels.

The source references `GFX_decision_category_great_depression`, `GFX_decision_cat_picture_great_depression`, `GFX_decision_great_depression_*`, and `GFX_decision_mission_great_depression_*` sprites.

The Event 35 asset handoff reports the category picture DDS at `gfx/interface/decisions/035_great_depression/decision_cat_picture_great_depression.dds`, but no matching GFX registration or complete decision-icon registration was found during this audit.

The category picture will not render until `great_depression_category_desc` exists, as required by the vanilla decision-category contract.

## Cleanup, cancellation, and exploit notes

The category closes when `great_depression_active_crisis_is_coherent` fails, and action visibility is delegated to phase and receipt helpers so recovery hides obsolete crisis actions.

Instant decisions intentionally have no decision timer, so their parent complete effects must be idempotent and must record a receipt before any resource debit or mission activation.

Missions have separate cancellation and timeout calls, and cancellation must not apply timeout failure consequences.

`fire_only_once = no` on repeatable decisions and missions is deliberate because Event 35 can recur, while parent episode, action, center, aid, and liquidation receipts must prevent farming.

The parent must cap simultaneous projects and missions, preserve at least one viable center for liquidation, reject unsafe supplier contracts, and prevent repeated aid or doctrine-switch loops.

No direct factory grant, free equipment loop, war-goal loop, or raw meter mutation is present in these decision files.

## Validation and audit evidence

The touched source files have balanced Clausewitz braces and no duplicate top-level decision or mission ids.

The decision source contains 90 category children, 75 decisions, 15 missions, and 74 custom-cost pairs.

The state-targeted decisions all have `state_target`, a target trigger, and `map_and_decisions_view`.

The missions all have activation, objective availability, cancellation, timeout, complete, dynamic duration, and non-selectable behavior.

No `cost =` field, unsupported `<=` or `>=` operator, or mission `visible` block is present in the touched decision source.

The mandatory `hoi4.gui_inspect` attempt was made for the ordinary Event 35 decision category and returned `MCP tool hoi4_agent_tools/hoi4.gui_inspect is not available to the model`.

The mandatory `hoi4.gui_render` route was not callable in this runtime and returned a JavaScript `TypeError` because `tools.mcp__hoi4_agent_tools__hoi4_gui_render` was not a function.

The mandatory `hoi4.probability_inspect` route was not callable in this runtime and returned a JavaScript `TypeError` because `tools.mcp__hoi4_agent_tools__hoi4_probability_inspect` was not a function.

No production GUI render, probability evaluation, probability sweep, probability comparison, decision lint, or live game test can therefore be claimed.

No game was launched.

## Severity-sorted blockers and remaining issues

1. Critical integration blocker: the parent-owned decision triggers, cost triggers, action effects, mission activation gates, mission objective triggers, mission completion effects, timeout effects, and cancellation effects are not currently defined in the inspected repository.

2. Critical presentation blocker: Event 35 decision and mission localisation, dynamic category header localisation, custom cost text, blocked reasons, and texticon coverage are outside this ownership and currently absent or incomplete.

3. High asset blocker: the category picture DDS is reported present, but the category sprite and the decision and mission sprite registrations are not present in the inspected interface files.

4. High evidence blocker: the installed HOI4 MCP GUI and probability routes were unavailable, so source review is not equivalent to engine or visual evidence.

5. High balance blocker: the four-spendable-type cap is encoded as a parent contract and existing constant, but cannot be verified until each parent cost helper has an implementation and the named probability scenarios have complete inputs.

6. Medium integration issue: the evolution action aliases and Event 34 supplier adapter names must be reconciled with the parent evolution implementation before localisation and helper wiring are finalized.

No requested baseline doctrine, selected-center action, shared action, evolution action, or mapped mission was intentionally omitted from this source tranche.

The implementation should not be called runtime-complete until the blockers above are resolved and the same named AI scenarios receive the required inspect, evaluate or sweep, and compare evidence.
