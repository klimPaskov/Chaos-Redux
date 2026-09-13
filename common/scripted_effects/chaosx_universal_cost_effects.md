# chaosx_universal_cost_effects

This file documents the neutral universal discounted-cost and transaction effects declared in `chaosx_universal_cost_effects.txt`.

The framework does not decide purchase eligibility, ordinary modifiers, cooldowns, reserve floors, AI weights, or gameplay outcomes.

The caller supplies the ordinary current payable cost and invokes the quote again at confirmation or delayed-installment time.

## Event 026 identifier coverage

The family mask enum includes the broad `equipment` mask `112` (`16 + 32 + 64`) for infantry, support, and motorized equipment, the `trains` alias `128` for `train_equipment`, and the `convoys` alias `256` for `convoy`.

Event 026 also uses dedicated mask bits for `army_experience`, `consumer_goods`, `diplomatic`, `intelligence`, `laws`, `officer_corps`, `personnel`, `special_project`, and `state_project`, all within the matcher’s low-thirty-bit range.

The fixed-point constant `constant:universal_cost_fixed_point.gate_epsilon` is `0.00001`, the smallest declared fixed-point step used by an owner’s strict affordability gate when an exact quoted balance must remain payable.

## Shared storage

The source registry is global and consists of four aligned arrays: `global.universal_cost_source_ids`, `global.universal_cost_source_ratios`, `global.universal_cost_source_priorities`, and `global.universal_cost_source_eligibility_masks`.

An active source is a row in those arrays, and source expiry is the idempotent removal of that row through `universal_cost_source_clear` or a named owner wrapper.

Transaction receipts are regular arrays on the payer country, so quote and payment scratch never share mutable global state between payers.

The transaction arrays retain logical rows in `universal_cost_transaction_ids`, `universal_cost_transaction_states`, `universal_cost_transaction_component_counts`, `universal_cost_transaction_source_ids`, `universal_cost_transaction_primary_component_ids`, `universal_cost_transaction_total_ordinary_costs`, `universal_cost_transaction_total_quoted_costs`, `universal_cost_transaction_total_paid_costs`, and `universal_cost_transaction_total_refunded_costs`.

The component arrays are `universal_cost_component_transaction_ids`, `universal_cost_component_ids`, `universal_cost_component_resource_kinds`, `universal_cost_component_resource_ids`, `universal_cost_component_ordinary_costs`, `universal_cost_component_quoted_costs`, `universal_cost_component_actual_paid_costs`, `universal_cost_component_source_ids`, and `universal_cost_component_refunded_states`.

## universal_cost_source_register

Purpose: create or update one active source row.

Scope: any effect scope that can write global variables, normally a country or event owner scope.

Inputs: temporary `universal_cost_source_id` greater than zero, `universal_cost_source_ratio` from one through `constant:universal_cost_framework.basis`, `universal_cost_source_priority` from zero through `constant:universal_cost_framework.max_source_priority - 1`, and `universal_cost_source_eligibility_mask` from zero through `constant:universal_cost_framework.max_eligibility_mask_exclusive - 1`.

Outputs: temporary `universal_cost_source_register_result`, using `constant:universal_cost_framework.result_success` or `result_no_op`.

Defaults: priority zero is valid and has no implicit replacement; a zero eligibility mask means every family; the caller must supply a positive ratio.

Side effects: updates the row with the same source id or appends one row to all four aligned global arrays.

Composition order: quote traversal sorts registered rows by ascending priority, preserving registry order for equal priorities.

Example:

```txt
set_temp_variable = { universal_cost_source_id = 9001 }
set_temp_variable = { universal_cost_source_ratio = constant:universal_cost_framework.baseline_sale_ratio }
set_temp_variable = { universal_cost_source_priority = 500 }
set_temp_variable = { universal_cost_source_eligibility_mask = constant:universal_cost_family.factory_commitment }
universal_cost_source_register = yes
```

## universal_cost_source_clear

Purpose: expire one source and remove its row from the active registry.

Scope: any effect scope that can write global variables.

Inputs: temporary `universal_cost_source_id`.

Outputs: temporary `universal_cost_source_clear_result`.

Defaults: an unknown id is a no-op.

Side effects: removes the matching index from every aligned source array and does not alter existing transaction receipts.

## universal_cost_source_register_black_friday

Purpose: expose the stable Event 026 source-registration name without owning Event 026 lifecycle.

Scope: event owner effect scope.

Inputs: optional temporary `universal_cost_source_ratio` and `universal_cost_source_eligibility_mask`.

Defaults: an absent or non-positive ratio uses `constant:universal_cost_framework.black_friday_default_ratio`, a non-positive priority uses the shared Black Friday priority, and a zero mask applies to every caller-declared family.

Outputs: the generic `universal_cost_source_register_result`.

Side effects: registers source id `constant:universal_cost_framework.black_friday_source_id` with the shared source registry.

The Event 026 owner must call this only after its own activation snapshot is valid and must call `universal_cost_source_clear_black_friday` at expiry.

## universal_cost_source_clear_black_friday

Purpose: stable Event 026 source-expiry name.

Scope: event owner effect scope.

Inputs: none.

Outputs: the generic `universal_cost_source_clear_result`.

Side effects: clears only source id `constant:universal_cost_framework.black_friday_source_id`.

## universal_cost_source_matches_quote_family

Purpose: test a source eligibility mask against a quote family mask.

Scope: any effect scope.

Inputs: temporary `universal_cost_source_mask` and positive `universal_cost_quote_family_mask`.

Output: temporary `universal_cost_source_matches_quote` equal to one or zero.

Defaults: source mask zero means all families; non-zero masks use the low thirty bits.

Side effects: only temporary arithmetic variables are changed.

## universal_cost_round_up_to_quantum

Purpose: perform deterministic positive upward quantization.

Scope: any effect scope.

Inputs: temporary `universal_cost_quantize_amount` and optional positive `universal_cost_quantize_quantum`.

Outputs: `universal_cost_quantize_result` and `universal_cost_quantize_units` temporary variables.

Defaults: a non-positive quantum uses `constant:universal_cost_framework.default_rounding_quantum`; zero remains zero; negative values remain negative; a positive amount produces at least one positive quantum.

Side effects: temporary arithmetic only.

## universal_cost_quote_integer

Purpose: compose active source ratios, calculate the final payable cost, and expose one display value for the same transaction input.

Scope: payer or other country scope selected by the owner adapter.

Inputs: temporary `universal_cost_quote_ordinary_cost`, `universal_cost_quote_family_mask`, and optional `universal_cost_quote_rounding_quantum`.

Outputs: `universal_cost_quote_final_cost`, `universal_cost_quote_displayed_cost`, `universal_cost_quote_saved_cost`, `universal_cost_quote_composed_ratio`, `universal_cost_quote_source_count`, `universal_cost_quote_primary_source_id`, and `universal_cost_quote_valid`.

Defaults: no eligible active source leaves a positive ordinary cost unchanged; zero and negative amounts are preserved and receive no discount; a positive quoted amount is rounded upward to the supplied quantum only after all eligible ratios are composed.

Formula: for a positive ordinary cost, the composed ratio starts at 10000 and multiplies each eligible source ratio in priority order, dividing by 10000 after each source, then the final amount is `ceil(ordinary * composed_ratio / 10000 / quantum) * quantum`.

Side effects: temporary arrays are used for deterministic priority traversal, and no registry or payer state is changed.

The ordinary cost must already include all ordinary consumer modifiers because the engine exposes no generic scripted value that returns every purchase surface's current payable price.

## universal_cost_rebuild_custom_quote_ratio_cache

Purpose: materialize the effect-side source composition for HOI4 custom-cost trigger callers that cannot traverse the source arrays or invoke an effect.

Scope: any effect scope that can write global variables.

Inputs: the active source registry.

Outputs: `global.universal_cost_custom_quote_ratio_political_power`, `global.universal_cost_custom_quote_ratio_command_power`, `global.universal_cost_custom_quote_ratio_manpower`, `global.universal_cost_custom_quote_ratio_equipment`, `global.universal_cost_custom_quote_ratio_trains`, `global.universal_cost_custom_quote_ratio_convoy`, `global.universal_cost_custom_quote_ratio_fuel`, `global.universal_cost_custom_quote_ratio_army_experience`, `global.universal_cost_custom_quote_ratio_navy_experience`, `global.universal_cost_custom_quote_ratio_air_experience`, `global.universal_cost_custom_quote_ratio_stability`, `global.universal_cost_custom_quote_ratio_war_support`, and `global.universal_cost_custom_quote_cache_valid`.

Side effects: invokes `universal_cost_quote_integer` once for each canonical family mask using an ordinary basis-sized probe cost, so each stored ratio is produced by the same source-composition code used for payment. The cache is scalar and deliberately finite; custom triggers using another family mask fail closed.

The cache is cleared by `universal_cost_clear_custom_quote_ratio_cache` when Event 026 is no longer registered. A source expiry does not change any existing transaction receipt.

## universal_cost_check_quote_affordable

Purpose: check the quoted final amount against a native resource without debiting it.

Scope: payer country.

Inputs: temporary `universal_cost_quote_resource_kind` and `universal_cost_quote_final_cost`.

Output: temporary `universal_cost_quote_affordable`.

Defaults: zero and negative amounts are affordable; unsupported owner-adapter resource kinds are not affordable through this helper.

Side effects: none.

## Native resource branch map

The following native kinds are dispatched by both `universal_cost_pay_component` and `universal_cost_credit_component`; each payment branch first runs the same inclusive affordability check, while each credit branch adds the stored actual-paid amount without an affordability gate.

| Resource kind | Kind id | Affordability evidence | Debit effect | Credit effect |
| --- | ---: | --- | --- | --- |
| `political_power` | 1 | `NOT = { political_power < universal_cost_affordability_amount }` | `add_political_power = universal_cost_payment_delta` | `add_political_power = universal_cost_payment_amount` |
| `command_power` | 2 | `NOT = { command_power < universal_cost_affordability_amount }` | `add_command_power = universal_cost_payment_delta` | `add_command_power = universal_cost_payment_amount` |
| `army_experience` | 10 | `NOT = { has_army_experience < universal_cost_affordability_amount }` | `army_experience = universal_cost_payment_delta` | `army_experience = universal_cost_payment_amount` |
| `navy_experience` | 13 | `NOT = { has_navy_experience < universal_cost_affordability_amount }` | `navy_experience = universal_cost_payment_delta` | `navy_experience = universal_cost_payment_amount` |
| `air_experience` | 14 | `NOT = { has_air_experience < universal_cost_affordability_amount }` | `air_experience = universal_cost_payment_delta` | `air_experience = universal_cost_payment_amount` |
| `manpower` | 3 | `NOT = { has_manpower < universal_cost_affordability_amount }` | `add_manpower = universal_cost_payment_delta` | `add_manpower = universal_cost_payment_amount` |
| `fuel` | 4 | `NOT = { has_fuel < universal_cost_affordability_amount }` | `add_fuel = universal_cost_payment_delta` | `add_fuel = universal_cost_payment_amount` |
| `infantry_equipment` | 5 | `NOT = { has_equipment = { infantry_equipment < universal_cost_affordability_amount } }` | `add_equipment_to_stockpile = { type = infantry_equipment amount = universal_cost_payment_delta }` | `add_equipment_to_stockpile = { type = infantry_equipment amount = universal_cost_payment_amount }` |
| `support_equipment` | 6 | `NOT = { has_equipment = { support_equipment < universal_cost_affordability_amount } }` | `add_equipment_to_stockpile = { type = support_equipment amount = universal_cost_payment_delta }` | `add_equipment_to_stockpile = { type = support_equipment amount = universal_cost_payment_amount }` |
| `support_equipment_1` | 11 | `NOT = { has_equipment = { support_equipment_1 < universal_cost_affordability_amount } }` | `add_equipment_to_stockpile = { type = support_equipment_1 amount = universal_cost_payment_delta }` | `add_equipment_to_stockpile = { type = support_equipment_1 amount = universal_cost_payment_amount }` |
| `motorized_equipment` | 7 | `NOT = { has_equipment = { motorized_equipment_1 < universal_cost_affordability_amount } }` | `add_equipment_to_stockpile = { type = motorized_equipment_1 amount = universal_cost_payment_delta }` | `add_equipment_to_stockpile = { type = motorized_equipment_1 amount = universal_cost_payment_amount }` |
| `train_equipment` | 8 | `NOT = { has_equipment = { train_equipment < universal_cost_affordability_amount } }` | `add_equipment_to_stockpile = { type = train_equipment amount = universal_cost_payment_delta }` | `add_equipment_to_stockpile = { type = train_equipment amount = universal_cost_payment_amount }` |
| `train_equipment_1` | 12 | `NOT = { has_equipment = { train_equipment_1 < universal_cost_affordability_amount } }` | `add_equipment_to_stockpile = { type = train_equipment_1 amount = universal_cost_payment_delta }` | `add_equipment_to_stockpile = { type = train_equipment_1 amount = universal_cost_payment_amount }` |
| `convoy` | 9 | `NOT = { has_equipment = { convoy_1 < universal_cost_affordability_amount } }` | `add_equipment_to_stockpile = { type = convoy_1 amount = universal_cost_payment_delta }` | `add_equipment_to_stockpile = { type = convoy_1 amount = universal_cost_payment_amount }` |
| `stability` | 15 | `NOT = { has_stability < universal_cost_affordability_amount }` | `add_stability = universal_cost_payment_delta` | `add_stability = universal_cost_payment_amount` |
| `war_support` | 16 | `NOT = { has_war_support < universal_cost_affordability_amount }` | `add_war_support = universal_cost_payment_delta` | `add_war_support = universal_cost_payment_amount` |

Evidence for the three added native branches is the installed vanilla documentation at `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/triggers_documentation.md`, which documents `has_army_experience` and `has_equipment`, and `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md`, which documents the country-scope `army_experience` effect and country-scope `add_equipment_to_stockpile` effect.

The installed equipment definitions corroborate the concrete aliases at `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/units/equipment/support.txt` (`support_equipment_1`) and `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/units/equipment/trains.txt` (`train_equipment_1`).

Event 026 consumes these exact aliases in `common/scripted_effects/026_black_friday_effects.txt` and `common/scripted_triggers/026_black_friday_triggers.txt`, so the framework keeps their resource-kind ids distinct while dispatching the exact native equipment tokens.

## universal_cost_pay_component

Purpose: debit one positive quoted component through a supported native resource effect.

Scope: payer country.

Inputs: temporary `universal_cost_payment_resource_kind` and positive `universal_cost_payment_amount`.

Output: temporary `universal_cost_payment_result`.

Supported kinds: Political Power, Command Power, Army Experience, Navy Experience, Air Experience, Stability, War Support, Manpower, Fuel, Infantry Equipment, Support Equipment, Support Equipment 1, Motorized Equipment 1, Train Equipment, Train Equipment 1, and Convoy 1.

Defaults: zero and negative amounts are successful no-ops; unsupported kinds do not mutate the payer and return `result_no_op`.

Side effects: subtracts only after the corresponding inclusive affordability check succeeds.

## universal_cost_credit_component

Purpose: credit one stored actual-paid amount for a refund.

Scope: payer country.

Inputs: temporary `universal_cost_payment_resource_kind` and `universal_cost_payment_amount`.

Output: temporary `universal_cost_credit_result`.

Defaults: zero and negative amounts are successful no-ops; unsupported kinds return `result_no_op`.

Side effects: adds the exact supplied amount to the matching native resource and never infers a refund from ordinary or quoted cost.

## universal_cost_record_transaction

Purpose: append one paid component to a payer-scoped receipt and aggregate it under one logical transaction id.

Scope: payer country.

Inputs: positive `universal_cost_transaction_id`, positive unique `universal_cost_transaction_component_id`, positive `universal_cost_transaction_resource_kind`, non-negative `universal_cost_transaction_ordinary_cost`, `universal_cost_transaction_quoted_cost`, and `universal_cost_transaction_actual_paid_cost`, plus optional `universal_cost_transaction_resource_id`, `universal_cost_transaction_source_id`, and positive `universal_cost_transaction_primary_component`.

Outputs: `universal_cost_record_transaction_result` and `universal_cost_recorded_component_index`.

Defaults: a new transaction row starts in recorded/refundable state; repeated component ids, reused refunded/settled transaction ids, negative amounts, and actual-paid values that differ from the quote are rejected.

Side effects: appends the component, updates aligned totals, and retains actual paid amount as the only refund basis.

Multi-resource contract: call once per component with the same logical transaction id and a different component id, then settle or refund the transaction once.

## universal_cost_settle_transaction

Purpose: close a successful receipt after the owner no longer permits cancellation refunds.

Scope: payer country.

Inputs: temporary `universal_cost_transaction_id`.

Output: temporary `universal_cost_settle_transaction_result`.

Defaults: unknown, partial, refunded, or already settled rows are no-ops.

Side effects: changes a recorded row to settled without deleting its proof arrays.

## universal_cost_mark_component_refunded

Purpose: acknowledge a refund performed by an owner adapter for a resource kind the shared native credit helper cannot execute.

Scope: payer country.

Inputs: temporary `universal_cost_transaction_id` and `universal_cost_transaction_component_id`.

Output: temporary `universal_cost_mark_component_refunded_result`.

Side effects: marks the exact stored component refunded and adds its stored actual-paid amount to the transaction refund total.

The owner adapter must perform the external credit first and must credit exactly the stored actual-paid amount.

## universal_cost_refund_transaction

Purpose: refund every still-pending component using stored actual-paid amounts and prevent duplicate refunding.

Scope: payer country.

Inputs: temporary `universal_cost_transaction_id`.

Outputs: `universal_cost_refund_transaction_result`, `universal_cost_refund_total`, and `universal_cost_refund_unhandled_total`.

Defaults: unknown or settled/refunded rows are no-ops; unsupported positive components remain pending and return `result_partial`.

Side effects: native components are credited once, their per-component state changes to refunded, and a fully refunded row changes to the refunded transaction state.

## Engine boundary

The engine does not provide one generic effect that accepts an arbitrary dynamic resource token, one generic value for every ordinary purchase modifier, a dynamic global-flag name, or a transactional rollback spanning unrelated native effects.

The framework therefore uses numeric source/family/resource enums, aligned arrays, sixteen fixed native payment branches, fixed-point quanta for deliberate Stability and War Support payments, and an explicit owner adapter for factory commitments, technology, advisor, idea, operation, equipment-design, and other inaccessible surfaces.

The native resource contract includes Political Power, Command Power, Army Experience, Navy Experience, Air Experience, Manpower, Fuel, Infantry Equipment, Support Equipment, Motorized Equipment, Trains, Convoys, Stability, and War Support. Stability and War Support callers must pass `constant:universal_cost_fixed_point_quantum.stability` or `constant:universal_cost_fixed_point_quantum.war_support` as their rounding quantum; integer callers use the default one-unit quantum.

`custom_adapter` remains an explicit owner-paid and owner-refunded resource kind and is intentionally absent from the native branch map.

An owner adapter must keep eligibility and reserve checks unchanged, compute the ordinary current payable cost, call `universal_cost_quote_integer` for display and again immediately before payment, execute its own unsupported payment effect, call `universal_cost_record_transaction` with actual paid amount equal to the displayed quote, and call either `universal_cost_mark_component_refunded` after an external refund or `universal_cost_settle_transaction` after the cancellation window closes.
