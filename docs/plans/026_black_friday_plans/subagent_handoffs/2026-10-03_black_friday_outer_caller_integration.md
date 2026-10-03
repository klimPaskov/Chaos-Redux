# Event 026 outer caller integration

Disposition: implemented for the bounded source patch, with MCP/native acceptance and other production callers unresolved.
Acceptance basis: the parent instruction dated 2026-10-03 explicitly authorizes caller-owned temporary output initialization in the three named files and prohibits shared producer, receipt-helper, balance, lifecycle, event-enable, unrelated-source, and Git changes.

## Scope and files

Workspace: `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux`.

Changed production files:

- `common/scripted_effects/026_black_friday_effects.txt`
- `common/scripted_triggers/026_black_friday_triggers.txt`, outside `black_friday_quote_custom_cost` only

Added evidence files:

- [Caller declaration audit](black_friday_outer_caller_contract_audit.js)
- [Bounded actual caller scenarios](black_friday_outer_caller_source_tests.js)
- This handoff

Inspected `common/scripted_localisation/026_black_friday_scripted_localisation.txt` without editing it.
Its current 921-line source contains no cost-quote helper invocation, and its SHA-256 remains `665dd28b4cb12380ace61fcbbab36a11e035da885ac5fa38b590a4fc2f17098e`.
Its existing finite sale selectors and direct temporary display assignments were preserved.
Cost getter helper nesting exists in other production localisation files listed under follow-up, not in this allowed file.

There are 272 added scalar/array storage declarations at 152 helper boundaries in 88 existing functions.
The full change inventory can be reproduced with `node docs/plans/026_black_friday_plans/subagent_handoffs/black_friday_outer_caller_contract_audit.js --changes`.
The tables below list every changed function and every distinct added output declaration name.

No helper implementation, quote algorithm, receipt algorithm, gameplay API, tuning constant, native payment branch, event target, persistent flag, achievement rule, recurring hook, GUI layout, localisation key, asset, workbook, or Git index change was introduced.
No simplifications or gameplay fallbacks were made.
Documentation changes are confined to this handoff and the task-specific audit/test artifacts.
The matching shared API documentation remains owned by architect01a10115.

## Storage and boundary contract

Each caller now creates missing temporary output storage before invoking its helper.
Existing declarations remain authoritative when the storage already exists in the same native effect/trigger frame.
Subsequent calls mutate that inherited storage rather than publishing regular globals or resetting input/cursor state.

| Boundary | Added storage where consumed | Initial storage value | Scope and persistent effects |
| --- | --- | --- | --- |
| `universal_cost_quote_integer` | final cost, validity, source count where used | ordinary input for final cost, framework zero for validity and source count | existing payer scope, temporary only |
| `universal_cost_check_quote_affordable` | `universal_cost_quote_affordable` | framework zero | existing payer scope, no debit |
| `universal_cost_pay_component` | `universal_cost_payment_result` | framework result_no_op | existing payer scope, existing native debit unchanged |
| `universal_cost_record_transaction` | `universal_cost_record_transaction_result` | framework result_no_op | existing payer scope, existing receipt writes unchanged |
| `universal_cost_settle_transaction` | `universal_cost_settle_transaction_result` where tested afterwards | framework result_no_op | existing payer scope, existing receipt state unchanged |
| `universal_cost_mark_component_refunded` | acknowledgment result | framework result_no_op | existing payer scope, existing refund acknowledgment unchanged |
| `universal_cost_refund_transaction` | refund result where read afterwards | framework result_no_op | existing payer scope, stored-paid refunds unchanged |
| `black_friday_quote_custom_cost` | `black_friday_quote_final_cost` | `black_friday_quote_ordinary_cost` | existing country/owner-selected scope, central producer untouched |
| `black_friday_allocate_owner_transaction` | `black_friday_owner_transaction_id` | framework zero | existing payer allocator and proof unchanged |
| `black_friday_find_achievement_transaction` | transaction index, lookup result, row pointer | invalid_index, result_no_op, zero | existing payer scope, no receipt mutation |
| Fury component-list preparation | the four aligned component arrays | positive one-element resize placeholder | caller frame owns storage, existing callee clears and rebuilds contents |
| Fury payment wrappers | `black_friday_fury_payment_success` | framework zero | existing selected payer and payment behavior |
| CBRN payment wrappers | their consumed payment success fields | framework zero | existing selected payer and payment behavior |
| CBRN quote/can_pay wrapper layers | forwarded ordinary inputs, quoted prices, quote validity, affordability results | framework zero before the helper overwrites them | existing payer scope, trigger-only temporary writes |

The four Fury arrays are `black_friday_fury_component_ids`, `black_friday_fury_component_resource_kinds`, `black_friday_fury_component_family_masks`, and `black_friday_fury_component_ordinary_costs`.
They are resized only before the existing begin/clear helper, never between append calls.
Append and prepared-payment helpers consume inherited arrays, so they do not truncate or reset a live component list.
The one-element placeholder establishes storage and is removed by the existing callee's clear operation.
It is neither an actual purchase component nor a tuning/source-count limit.

Forwarded protection fields such as `black_friday_cbrn_protection_pair_ordinary_pp` are outputs of the quote wrapper and inputs of the later payment helper.
Storage initialization occurs before the wrapper that supplies the original constants, at every can_pay/quote/pair boundary.
The source scenarios verify that the resulting ordinary inputs retain their original positive constant values and do not become initializer zeros.

No constants or tuning tables were added or updated.
All initialization values reuse `universal_cost_framework.zero`, `one`, `invalid_index`, and `result_no_op`.
No event-target or cleanup migration is needed.
Temporary storage still ends with its enclosing chain, and the original list-clearing, payment, receipt, sale-expiry, cancellation, and achievement cleanup remains intact.

## Exact changed functions

### Effects

| Function | Patched call boundaries | Distinct added output/storage declarations |
| --- | ---: | --- |
| `black_friday_confirm_achievement_transaction` | 1 | `black_friday_achievement_transaction_index`, `black_friday_achievement_lookup_result`, `black_friday_achievement_row_pointer` |
| `black_friday_retract_achievement_transaction` | 1 | `black_friday_achievement_transaction_index`, `black_friday_achievement_lookup_result`, `black_friday_achievement_row_pointer` |
| `black_friday_pay_fury_bundle` | 5 | `black_friday_owner_transaction_id`, `universal_cost_quote_final_cost`, `universal_cost_quote_valid`, `universal_cost_quote_affordable`, `universal_cost_payment_result`, `universal_cost_record_transaction_result` |
| `black_friday_fury_pay_single_active` | 2 | `black_friday_fury_component_ids`, `black_friday_fury_component_resource_kinds`, `black_friday_fury_component_family_masks`, `black_friday_fury_component_ordinary_costs`, `black_friday_fury_payment_success` |
| `black_friday_fury_pay_prepared_bundle_active` | 1 | `black_friday_fury_payment_success` |
| `black_friday_fury_pay_reinforcement_cost` | 1 | `black_friday_fury_component_ids`, `black_friday_fury_component_resource_kinds`, `black_friday_fury_component_family_masks`, `black_friday_fury_component_ordinary_costs` |
| `black_friday_fury_pay_settlement_cost` | 1 | `black_friday_fury_component_ids`, `black_friday_fury_component_resource_kinds`, `black_friday_fury_component_family_masks`, `black_friday_fury_component_ordinary_costs` |
| `black_friday_fury_pay_core_cost` | 1 | `black_friday_fury_component_ids`, `black_friday_fury_component_resource_kinds`, `black_friday_fury_component_family_masks`, `black_friday_fury_component_ordinary_costs` |
| `black_friday_fury_pay_registers_cost` | 1 | `black_friday_fury_component_ids`, `black_friday_fury_component_resource_kinds`, `black_friday_fury_component_family_masks`, `black_friday_fury_component_ordinary_costs` |
| `black_friday_fury_pay_rail_registry_cost` | 1 | `black_friday_fury_component_ids`, `black_friday_fury_component_resource_kinds`, `black_friday_fury_component_family_masks`, `black_friday_fury_component_ordinary_costs` |
| `black_friday_fury_pay_admin_core_cost` | 1 | `black_friday_fury_component_ids`, `black_friday_fury_component_resource_kinds`, `black_friday_fury_component_family_masks`, `black_friday_fury_component_ordinary_costs` |
| `black_friday_fury_pay_march_core_cost` | 1 | `black_friday_fury_component_ids`, `black_friday_fury_component_resource_kinds`, `black_friday_fury_component_family_masks`, `black_friday_fury_component_ordinary_costs` |
| `black_friday_fury_pay_cooperation_cost` | 1 | `black_friday_fury_component_ids`, `black_friday_fury_component_resource_kinds`, `black_friday_fury_component_family_masks`, `black_friday_fury_component_ordinary_costs` |
| `black_friday_fury_pay_terminal_reserves_cost` | 1 | `black_friday_fury_component_ids`, `black_friday_fury_component_resource_kinds`, `black_friday_fury_component_family_masks`, `black_friday_fury_component_ordinary_costs` |
| `black_friday_fury_pay_terminal_fronts_cost` | 1 | `black_friday_fury_component_ids`, `black_friday_fury_component_resource_kinds`, `black_friday_fury_component_family_masks`, `black_friday_fury_component_ordinary_costs` |
| `black_friday_fury_pay_anti_border_watch_cost` | 1 | `black_friday_fury_component_ids`, `black_friday_fury_component_resource_kinds`, `black_friday_fury_component_family_masks`, `black_friday_fury_component_ordinary_costs` |
| `black_friday_fury_pay_anti_emergency_aid_cost` | 1 | `black_friday_fury_component_ids`, `black_friday_fury_component_resource_kinds`, `black_friday_fury_component_family_masks`, `black_friday_fury_component_ordinary_costs` |
| `black_friday_fury_pay_anti_staff_talks_cost` | 1 | `black_friday_fury_component_ids`, `black_friday_fury_component_resource_kinds`, `black_friday_fury_component_family_masks`, `black_friday_fury_component_ordinary_costs` |
| `black_friday_fury_pay_anti_supply_denial_cost` | 1 | `black_friday_fury_component_ids`, `black_friday_fury_component_resource_kinds`, `black_friday_fury_component_family_masks`, `black_friday_fury_component_ordinary_costs` |
| `black_friday_pay_communism_national_counter_agitation` | 5 | `black_friday_owner_transaction_id`, `universal_cost_quote_final_cost`, `universal_cost_quote_valid`, `universal_cost_quote_affordable`, `universal_cost_payment_result`, `universal_cost_record_transaction_result` |
| `black_friday_pay_communism_local_intervention` | 5 | `black_friday_owner_transaction_id`, `universal_cost_quote_final_cost`, `universal_cost_quote_valid`, `universal_cost_quote_affordable`, `universal_cost_payment_result`, `universal_cost_record_transaction_result` |
| `black_friday_pay_communism_emergency_intervention` | 5 | `black_friday_owner_transaction_id`, `universal_cost_quote_final_cost`, `universal_cost_quote_valid`, `universal_cost_quote_affordable`, `universal_cost_payment_result`, `universal_cost_record_transaction_result` |
| `black_friday_record_bio_medical_component` | 1 | `universal_cost_record_transaction_result` |
| `black_friday_pay_bio_expand_medical_capacity` | 4 | `universal_cost_quote_final_cost`, `universal_cost_quote_valid`, `universal_cost_quote_affordable`, `black_friday_owner_transaction_id`, `universal_cost_payment_result` |
| `black_friday_cbrn_bundle_pay_record_component` | 2 | `universal_cost_payment_result`, `universal_cost_record_transaction_result` |
| `black_friday_pay_cbrn_equipment_bundle` | 4 | `universal_cost_quote_final_cost`, `universal_cost_quote_valid`, `universal_cost_quote_source_count`, `universal_cost_quote_affordable`, `black_friday_owner_transaction_id`, `universal_cost_settle_transaction_result` |
| `black_friday_pay_cbrn_demand_inspections` | 2 | `black_friday_cbrn_inspection_instrument_cost`, `black_friday_cbrn_inspection_support_cost`, `black_friday_cbrn_bundle_payment_success` |
| `black_friday_apply_cbrn_inspection_demand` | 1 | `black_friday_cbrn_inspection_payment_success` |
| `black_friday_pay_cbrn_forensic_publication` | 1 | `black_friday_cbrn_bundle_payment_success` |
| `black_friday_apply_cbrn_forensic_publication` | 2 | `black_friday_cbrn_forensic_instrument_cost`, `black_friday_cbrn_forensic_support_cost`, `black_friday_cbrn_forensic_payment_success` |
| `black_friday_cbrn_decon_pay_record_component` | 2 | `universal_cost_payment_result`, `universal_cost_record_transaction_result` |
| `black_friday_pay_cbrn_decon_sponsorship` | 5 | `black_friday_cbrn_decon_masks_cost`, `black_friday_cbrn_decon_equipment_cost`, `black_friday_cbrn_decon_trucks_cost`, `universal_cost_quote_final_cost`, `universal_cost_quote_valid`, `universal_cost_quote_source_count`, `black_friday_owner_transaction_id`, `universal_cost_settle_transaction_result` |
| `black_friday_pay_cbrn_move_civilians_to_shelters` | 7 | `universal_cost_quote_final_cost`, `universal_cost_quote_valid`, `universal_cost_quote_affordable`, `black_friday_owner_transaction_id`, `universal_cost_payment_result`, `universal_cost_record_transaction_result` |
| `black_friday_apply_cbrn_civilian_shelter_movement` | 1 | `black_friday_cbrn_shelter_payment_success` |
| `black_friday_begin_alien_infantry_landing_reservation` | 3 | `universal_cost_quote_final_cost`, `universal_cost_quote_valid`, `black_friday_owner_transaction_id`, `universal_cost_record_transaction_result` |
| `black_friday_refund_alien_infantry_landing_transaction` | 2 | `universal_cost_mark_component_refunded_result`, `universal_cost_refund_transaction_result` |
| `black_friday_settle_alien_infantry_landing_transaction` | 1 | `universal_cost_settle_transaction_result` |
| `black_friday_record_africa_elephant_logistics_component` | 1 | `universal_cost_record_transaction_result` |
| `black_friday_refund_africa_elephant_logistics_transaction` | 1 | `universal_cost_mark_component_refunded_result` |
| `black_friday_pay_africa_elephant_logistics_contract` | 4 | `universal_cost_quote_final_cost`, `universal_cost_quote_valid`, `universal_cost_quote_affordable`, `black_friday_owner_transaction_id`, `universal_cost_payment_result` |
| `black_friday_pay_cbrn_protection_pair` | 7 | `universal_cost_quote_final_cost`, `universal_cost_quote_valid`, `universal_cost_quote_source_count`, `universal_cost_quote_affordable`, `black_friday_owner_transaction_id`, `universal_cost_payment_result`, `universal_cost_record_transaction_result`, `universal_cost_settle_transaction_result` |
| `black_friday_pay_cbrn_recondition_masks` | 2 | `black_friday_cbrn_protection_pair_ordinary_pp`, `black_friday_cbrn_protection_pair_ordinary_support`, `black_friday_cbrn_protection_pair_pp_cost`, `black_friday_cbrn_protection_pair_support_cost`, `black_friday_cbrn_protection_pair_payment_success` |
| `black_friday_pay_cbrn_convert_mask_industry` | 2 | `black_friday_cbrn_protection_pair_ordinary_pp`, `black_friday_cbrn_protection_pair_ordinary_support`, `black_friday_cbrn_protection_pair_pp_cost`, `black_friday_cbrn_protection_pair_support_cost`, `black_friday_cbrn_protection_pair_payment_success` |
| `black_friday_pay_cbrn_simplify_filters` | 2 | `black_friday_cbrn_protection_pair_ordinary_pp`, `black_friday_cbrn_protection_pair_ordinary_support`, `black_friday_cbrn_protection_pair_pp_cost`, `black_friday_cbrn_protection_pair_support_cost`, `black_friday_cbrn_protection_pair_payment_success` |
| `black_friday_cbrn_theater_pay_record_component` | 2 | `universal_cost_payment_result`, `universal_cost_record_transaction_result` |
| `black_friday_pay_cbrn_theater_assignment` | 5 | `black_friday_cbrn_theater_command_power_cost`, `black_friday_cbrn_theater_decontamination_cost`, `black_friday_cbrn_theater_fuel_cost`, `universal_cost_quote_final_cost`, `universal_cost_quote_valid`, `universal_cost_quote_source_count`, `universal_cost_quote_affordable`, `black_friday_owner_transaction_id`, `universal_cost_settle_transaction_result` |
| `black_friday_pay_cbrn_external_aid_pp_fee` | 4 | `black_friday_cbrn_external_aid_pp_cost`, `black_friday_owner_transaction_id`, `universal_cost_payment_result`, `universal_cost_record_transaction_result` |
| `black_friday_settle_cbrn_external_aid_pp_fee_receipt` | 1 | `universal_cost_settle_transaction_result` |

### Triggers

| Function | Patched call boundaries | Distinct added output/storage declarations |
| --- | ---: | --- |
| `black_friday_can_reserve_alien_infantry_landing` | 1 | `black_friday_quote_final_cost` |
| `black_friday_can_pay_bio_expand_medical_capacity` | 1 | `black_friday_quote_final_cost` |
| `black_friday_can_pay_cbrn_demand_inspections` | 1 | `black_friday_quote_final_cost` |
| `black_friday_cbrn_forensic_materials_are_affordable` | 1 | `black_friday_quote_final_cost` |
| `black_friday_cbrn_decon_sale_materials_are_affordable` | 1 | `black_friday_quote_final_cost` |
| `black_friday_can_pay_cbrn_move_civilians_to_shelters` | 1 | `black_friday_quote_final_cost` |
| `black_friday_can_pay_fury_target_cost` | 1 | `black_friday_quote_final_cost` |
| `black_friday_can_pay_fury_reinforcement_cost` | 1 | `black_friday_quote_final_cost` |
| `black_friday_can_pay_fury_settlement_cost` | 1 | `black_friday_quote_final_cost` |
| `black_friday_can_pay_fury_registers_cost` | 1 | `black_friday_quote_final_cost` |
| `black_friday_can_pay_fury_rail_registry_cost` | 1 | `black_friday_quote_final_cost` |
| `black_friday_can_pay_fury_admin_core_cost` | 1 | `black_friday_quote_final_cost` |
| `black_friday_can_pay_fury_march_core_cost` | 1 | `black_friday_quote_final_cost` |
| `black_friday_can_pay_fury_cooperation_cost` | 1 | `black_friday_quote_final_cost` |
| `black_friday_can_pay_fury_rivalry_cost` | 1 | `black_friday_quote_final_cost` |
| `black_friday_can_pay_fury_survey_cost` | 1 | `black_friday_quote_final_cost` |
| `black_friday_can_pay_fury_terminal_reserves_cost` | 1 | `black_friday_quote_final_cost` |
| `black_friday_can_pay_fury_terminal_fronts_cost` | 1 | `black_friday_quote_final_cost` |
| `black_friday_can_pay_anti_fury_border_watch_cost` | 1 | `black_friday_quote_final_cost` |
| `black_friday_can_pay_anti_fury_emergency_aid_cost` | 1 | `black_friday_quote_final_cost` |
| `black_friday_can_pay_anti_fury_staff_talks_cost` | 1 | `black_friday_quote_final_cost` |
| `black_friday_can_pay_anti_fury_supply_denial_cost` | 1 | `black_friday_quote_final_cost` |
| `black_friday_can_pay_anti_fury_recognition_denial_cost` | 1 | `black_friday_quote_final_cost` |
| `black_friday_communism_national_counter_agitation_cost` | 1 | `black_friday_quote_final_cost` |
| `black_friday_communism_local_intervention_level_1_cost` | 1 | `black_friday_quote_final_cost` |
| `black_friday_communism_local_intervention_level_2_cost` | 1 | `black_friday_quote_final_cost` |
| `black_friday_communism_local_intervention_level_3_cost` | 1 | `black_friday_quote_final_cost` |
| `black_friday_communism_emergency_intervention_cost` | 1 | `black_friday_quote_final_cost` |
| `black_friday_can_pay_africa_elephant_logistics_contract` | 5 | `black_friday_quote_final_cost` |
| `black_friday_cbrn_protection_pair_quote` | 1 | `black_friday_quote_final_cost` |
| `black_friday_quote_cbrn_recondition_masks` | 1 | `black_friday_cbrn_protection_pair_quote_valid`, `black_friday_cbrn_protection_pair_pp_cost`, `black_friday_cbrn_protection_pair_support_cost`, `black_friday_cbrn_protection_pair_pp_affordable`, `black_friday_cbrn_protection_pair_support_affordable` |
| `black_friday_quote_cbrn_convert_mask_industry` | 1 | `black_friday_cbrn_protection_pair_quote_valid`, `black_friday_cbrn_protection_pair_pp_cost`, `black_friday_cbrn_protection_pair_support_cost`, `black_friday_cbrn_protection_pair_pp_affordable`, `black_friday_cbrn_protection_pair_support_affordable` |
| `black_friday_quote_cbrn_simplify_filters` | 1 | `black_friday_cbrn_protection_pair_quote_valid`, `black_friday_cbrn_protection_pair_pp_cost`, `black_friday_cbrn_protection_pair_support_cost`, `black_friday_cbrn_protection_pair_pp_affordable`, `black_friday_cbrn_protection_pair_support_affordable` |
| `black_friday_can_pay_cbrn_recondition_masks` | 1 | `black_friday_cbrn_protection_pair_ordinary_pp`, `black_friday_cbrn_protection_pair_ordinary_support`, `black_friday_cbrn_recondition_masks_pp_affordable`, `black_friday_cbrn_recondition_masks_support_affordable`, `black_friday_cbrn_recondition_masks_quote_valid`, `black_friday_cbrn_protection_pair_pp_cost`, `black_friday_cbrn_protection_pair_support_cost` |
| `black_friday_can_pay_cbrn_convert_mask_industry` | 1 | `black_friday_cbrn_protection_pair_ordinary_pp`, `black_friday_cbrn_protection_pair_ordinary_support`, `black_friday_cbrn_convert_mask_industry_pp_affordable`, `black_friday_cbrn_convert_mask_industry_support_affordable`, `black_friday_cbrn_convert_mask_industry_quote_valid`, `black_friday_cbrn_protection_pair_pp_cost`, `black_friday_cbrn_protection_pair_support_cost` |
| `black_friday_can_pay_cbrn_simplify_filters` | 1 | `black_friday_cbrn_protection_pair_ordinary_pp`, `black_friday_cbrn_protection_pair_ordinary_support`, `black_friday_cbrn_simplify_filters_pp_affordable`, `black_friday_cbrn_simplify_filters_support_affordable`, `black_friday_cbrn_simplify_filters_quote_valid`, `black_friday_cbrn_protection_pair_pp_cost`, `black_friday_cbrn_protection_pair_support_cost` |
| `black_friday_quote_cbrn_theater_assignment` | 1 | `black_friday_quote_final_cost` |
| `black_friday_can_pay_cbrn_theater_assignment` | 1 | `black_friday_cbrn_theater_command_power_cost`, `black_friday_cbrn_theater_decontamination_cost`, `black_friday_cbrn_theater_fuel_cost`, `black_friday_cbrn_theater_quote_valid`, `black_friday_cbrn_theater_command_power_affordable`, `black_friday_cbrn_theater_decontamination_affordable`, `black_friday_cbrn_theater_fuel_affordable` |
| `black_friday_quote_cbrn_external_aid_pp_fee` | 1 | `black_friday_quote_final_cost` |
| `black_friday_can_pay_cbrn_external_aid_pp_fee` | 1 | `black_friday_cbrn_external_aid_pp_quote_valid`, `black_friday_cbrn_external_aid_pp_cost`, `black_friday_cbrn_external_aid_pp_affordable` |

## Validation and preservation evidence

`node docs/plans/026_black_friday_plans/subagent_handoffs/black_friday_outer_caller_contract_audit.js` returns 739 inspected known scripted boundaries and zero missing consumed-output declarations under its conservative structural analysis.
The inventory comprises 427 effect calls, 227 trigger calls outside the protected central definition, and 85 localisation predicate calls.
These totals include predicates with no temporary output and do not imply 739 cost calculations.
The audit restricts shared receipt candidates to documented public outputs, treats prepared arrays as inherited inputs, and propagates forwarded field demands through the known wrapper graph.
It never resets storage or executes gameplay.

`node docs/plans/026_black_friday_plans/subagent_handoffs/black_friday_outer_caller_source_tests.js` passes nine bounded scenarios:

- all scoped known caller declarations and absence of quote calls in the allowed localisation file
- cold and repeated Fury clear/append/spend preparation, with exactly two real rows and no surviving placeholder
- actual protection owner limit through can_pay, quote wrapper, pair quote, and central quote, for active and expired sales
- component shortage and a missing live source reject the same purchase gate
- a negative control without outer declarations loses forwarded prices and ordinary inputs after return
- the parent's six receipt lookup declarations and receipt-proof output storage remain present
- removing only this patch's marked declarations leaves effect logic identical to HEAD after accounting for the parent's pre-existing lookup/proof declarations
- removing only this patch's marked declarations leaves trigger logic outside the architect-owned central block identical to HEAD
- the allowed localisation file remains byte-identical to the captured baseline

These caller scenarios reuse `exact_quote_source_tests.js` and its conservative scripted-call cleanup.
They do not duplicate exact arithmetic or ledger algorithms.
Only native resource affordability queries are modeled for the selected quote scenarios.
The outer central-quote entry assertion checks its consumed final-cost output, while internal exact-producer assertions retain the architect VM's complete contracts.
No receipt API, quote producer, or payment provider is mocked.

The architect-owned suites were also executed without editing them:

- `exact_quote_source_tests.js`: 434 quote scenarios, 56 quantizer scenarios, and its existing lifetime, source mutation, and boundary checks passed
- `universal_cost_receipt_lifetime_source_tests.js`: 45 receipt scenarios passed, including its actual Black Friday scanner cases and 29 native dispatch pairs

The receipt suite reports identical captured/final Event 026 effects hashes and unchanged selected scanner bodies during its run.
These are source-semantic results, not native debit, engine lifetime, or save/reload evidence.

Final captured production SHA-256 values:

| File | SHA-256 |
| --- | --- |
| `common/scripted_effects/026_black_friday_effects.txt` | `62398cd3d6bd431b54d36190f497913a3ebe44c8be02d0abc06f2e3806fd727b` |
| `common/scripted_triggers/026_black_friday_triggers.txt` | `53783b7a3d8b125eb1c24bef6f59cdfd6b5265b89a0f6cfc67e45948afb43d5b` |
| `common/scripted_localisation/026_black_friday_scripted_localisation.txt` | `665dd28b4cb12380ace61fcbbab36a11e035da885ac5fa38b590a4fc2f17098e` |

The parent already had 20 added effect lines, and the central trigger had the architect's quote replacement, before this patch.
The effect preservation test explicitly accounts for those existing changes.
The central definition is excluded from this writer's audit/edit surface.
The shared effect file and both architect-owned VM files were not edited.

External ordinary-cost helpers were inspected separately where reachable from the bounded adapters.
`prepare_communism_local_intervention_costs` and `prepare_communism_national_action_costs` in `common/scripted_effects/001_communism_spread_effects.txt` publish their payable costs as regular scoped variables.
`cbrn_calculate_state_raid_response_costs` in `common/scripted_effects/cbrn_protection_decision_effects.txt` likewise publishes regular state cost fields.
Those outputs must not be shadowed by temporary initialization.
`cbrn_debit_protection_political_power` consumes the supplied temporary amount and has no consumed output in this caller.

## Reference evidence and MCP blocker

The live callable tool catalog in this child exposes no HOI4 reference_context, reference_search, reference_read, source_lookup, event_inspect, event_render, event_compare, health/version, script_validate, helper-expansion, job, or native-task route.
There is also no callable tool-search route to load their schemas.
A narrow MCP reference/source request therefore cannot be sent from this child.
The parent's reported 600-second reference timeout and 20-second narrow retry failures were treated as supplied context, not as child-run results.
No MCP artifact URI, returned revision, render, validation result, or native acceptance is claimed.

The directed local-reference route was used and its exact file identities are recorded below.
`V` denotes `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV`.

| Local source | Read section / line span | SHA-256 |
| --- | --- | --- |
| `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md` | variable lifetime/scoping 435-449, arrays 1069-1089, especially 440 and 1073-1076 | `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4` |
| `paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md` | scripted triggers 2359-2384 | `abc51ad18a2c46e46d47baa795c5a840ebaf7c4ae3e777426c64a9f4c0c0ce06` |
| `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md` | scripted effects 4683-4698 | `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c` |
| `paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md` | scope semantics 24-41, unchanged callers retain their existing scope | `18ef5249e4991f5427eca9ec4a2f66dd47f51e26a491c730adc622f1f5db1b49` |
| `paradox_wiki/Localisation - Hearts of Iron 4 Wiki.md` | scripted localisation trigger and temporary-value lifetime 668-686 | `1a8f72362a34b4bb653186746b9fae0b98e463205cb02f12ccf2c3d9ccd3a064` |
| `V\documentation\triggers_documentation.md` | clear_temp_array 2154-2162, resize_temp_array 7414-7427, set_temp_variable 7482-7500 | `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29` |
| `V\documentation\effects_documentation.md` | clear_temp_array 2763-2771, resize_temp_array 6412-6425, set_temp_variable 7820-7839 | `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af` |
| `V\documentation\script_concept_documentation.md` | Script Constants 216-236 | `884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7` |
| `V\common\script_constants\documentation.md` | constant access and schema 1-32 | `e2812efbddc7961038e1f1f2b6dd6b059bdc70704ec87d1fe530835d9141be1c` |
| `V\common\scripted_effects\00_scripted_effects.txt` | temporary arithmetic in effect-limit triggers 498-520 | `93ddd0d2e9f7a1a5640cfdafbae6b9ff0e1b4ee57e829c81d13b0cac23ad90bf` |
| `V\common\scripted_localisation\00_scripted_localisation.txt` | installed localisation consumer contract/header and example 1-62 | `6f490e33736f4dc31568add5753a1afdef916f3993804febfbbe6d1583827587` |

The guessed `V\documentation\scripted_localisation_documentation.md` file is absent.
Its relevant installed consumer documentation was located in the actual `common\scripted_localisation\00_scripted_localisation.txt` header instead.
The exact shared quotation frontend and its markdown contract were inspected for the established positive-array-placeholder pattern.
The existing dynamic helper registry and relevant helper documentation were checked before adding declarations.
No new helper was required.

The reference documentation establishes the resize/clear operations and the conservative caller-lifetime obligation.
It does not independently prove cold empty-array storage creation by clear, or native retention of an array through clearing.
The positive placeholder follows the already implemented exact frontend and passes the reused source VM.
Native storage behavior, full owner debit/refund chains, save persistence, real display consumers, and production timing remain unresolved.
No HOI4 launch, log search, live-game validation, native task, or Git commit was attempted.
No GUI, focus, or map surface was redesigned or inspected as completed engine evidence.

Skills used: chaos-redux-events, chaos-redux-subagents, and the relevant cost-integrity guidance from chaos-redux-decisions-missions.
No skills were created or updated.

## Unresolved owners and other production callers

The following paths are discovered production caller touchpoints, not a claim that every call in each file is defective.
They remain unedited and require their owner's caller-storage review before repository-wide completion.

| Owner | Unresolved paths / surfaces |
| --- | --- |
| Parent, RSA012 | `common/scripted_effects/012_africa_rsa_purchase_effects.txt`, `common/scripted_triggers/012_africa_rsa_purchase_triggers.txt` |
| Parent or CBRN display owner | `common/scripted_localisation/cbrn_protection_cost_scripted_localisation.txt`, `common/scripted_localisation/cbrn_decontamination_cost_scripted_localisation.txt`, including getter-to-quote and getter-to-affordability nesting |
| Parent or CBRN owner | `common/scripted_effects/cbrn_protective_aid_decision_effects.txt`, `common/scripted_effects/cbrn_doctrine_effects.txt`, `common/scripted_triggers/cbrn_protective_aid_decision_triggers.txt`, `common/scripted_triggers/cbrn_protection_triggers.txt`, `common/scripted_triggers/cbrn_occupation_triggers.txt`, `common/scripted_triggers/cbrn_doctrine_triggers.txt` |
| Parent or event owner | `common/scripted_effects/001_communism_spread_effects.txt`, `common/scripted_effects/007_fury_effects.txt`, `common/scripted_effects/016_alien_infantry_api_effects.txt`, `common/scripted_effects/017_random_faction_effects.txt`, `common/scripted_effects/germany_mengele_effects.txt`, `common/scripted_triggers/017_random_faction_triggers.txt`, `common/scripted_triggers/germany_mengele_triggers.txt` |
| Parent or decision owner | `common/decisions/001_communism_spread_decisions.txt`, `common/decisions/007_fury_decisions.txt`, `common/decisions/012_africa_elephant_operations_decisions.txt`, `common/decisions/016_alien_infantry_landing_decisions.txt`, `common/decisions/biowarfare_disease_containment_decisions.txt`, `common/decisions/cbrn_diplomacy_decisions.txt`, `common/decisions/cbrn_protection_decisions.txt` |
| architect01a10115 | shared exact producer, shared receipt helper bodies, their two source VM suites, and matching shared API markdown contracts |
| Parent / connected MCP owner | restore callable narrow reference/source/event routes and retain actual returned engine evidence before native acceptance |

The static caller audit covers the explicitly loaded helper definitions and source-visible calls in the three allowed files.
It does not establish dynamic consumer coverage outside those files, unknown external provider contracts, full gameplay balance, or native execution.
No AI weights or probability-bearing fields changed, so no probability audit/compare cycle was represented as completed or substituted with arithmetic tests.

Parent review should retain the bounded patch, review the above outer callers under their own write scopes, and coordinate any new consumer obligations with architect01a10115 through this handoff.

