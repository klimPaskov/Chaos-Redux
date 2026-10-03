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

The transaction arrays retain logical rows in `universal_cost_transaction_ids`, `universal_cost_transaction_states`, `universal_cost_transaction_component_counts`, `universal_cost_transaction_component_head_plus_one`, `universal_cost_transaction_component_tail_plus_one`, `universal_cost_transaction_non_political_paid_component_count`, `universal_cost_transaction_source_ids`, `universal_cost_transaction_primary_component_ids`, `universal_cost_transaction_total_ordinary_costs`, `universal_cost_transaction_total_quoted_costs`, `universal_cost_transaction_total_paid_costs`, and `universal_cost_transaction_total_refunded_costs`.

The component arrays are `universal_cost_component_transaction_ids`, `universal_cost_component_ids`, `universal_cost_component_resource_kinds`, `universal_cost_component_resource_ids`, `universal_cost_component_ordinary_costs`, `universal_cost_component_quoted_costs`, `universal_cost_component_actual_paid_costs`, `universal_cost_component_source_ids`, `universal_cost_component_refunded_states`, and `universal_cost_component_next_plus_one`.

Each new transaction stores its payer-scoped row plus one in `universal_cost_transaction_row_plus_one_@var:universal_cost_transaction_id`. Zero means that no direct index exists. Its head and tail arrays link only its own components, and every component's next pointer is another row plus one or zero. A new receipt may therefore be found and refunded without traversing historical transactions or unrelated components, even when transactions append components in an interleaved order. The component count is limited to `constant:universal_cost_framework.max_components_per_transaction` (999) for one logical receipt; the total history arrays have no scripted-loop row cap for indexed receipts.

The current owner allocator writes `universal_cost_allocated_transaction_id_@var:transaction_id` as a numeric proof before first payment. A new row requires this proof, consumes it after creation, and writes its direct row pointer. An absent map without allocation proof is a legacy lookup, not evidence that the ID is free. Legacy lookups and refunds use the original arrays only when the relevant array has at most `constant:universal_cost_framework.legacy_scan_max_rows` (1,000) rows; otherwise they return a rejected result without crediting or settling. There is no automatic migration of older rows. Keep all arrays and refunded states as transaction and achievement evidence.

The non-political paid component count includes only positive, currently unrefunded components whose resource kind is not Political Power. Recording increments it and the first successful native refund or owner acknowledgment decrements it. Event 026 reads this count for receipt proof and keeps its own per-sale committed-family counts and direct achievement row index for later reversal.
Event 026 stores `black_friday_achievement_row_plus_one_@var:transaction_id` after appending a complete achievement row. For the active sale it stores `black_friday_achievement_family_committed_count_@var:family_id` with a family-specific sale generation; native raid equipment-family proof remains a separate flag. Pending receipts increase those counts only on confirmation, committed refunds decrease them once, and a family disappears only when its committed count reaches zero without native raid proof. An already-active sale from a save made before these counters were introduced cannot have its historic family multiplicities reconstructed from the family-presence array; its unindexed achievement reversal fails closed until a later sale begins with indexed accounting.

## universal_cost_source_register

Purpose: create or update one active source row.

Scope: any effect scope that can write global variables, normally a country or event owner scope.

Inputs: temporary `universal_cost_source_id` greater than zero, a represented `universal_cost_source_ratio` greater than zero through `constant:universal_cost_framework.basis`, `universal_cost_source_priority` from zero through `constant:universal_cost_framework.max_source_priority - 1`, and `universal_cost_source_eligibility_mask` from zero through `constant:universal_cost_framework.max_eligibility_mask_exclusive - 1`.

Outputs: temporary `universal_cost_source_register_result`, using `constant:universal_cost_framework.result_success` or `result_no_op`.

Defaults: priority zero is valid and has no implicit replacement; a zero eligibility mask means every family; the caller must supply a positive ratio.

Side effects: updates the row with the same source id or appends one row to all four aligned global arrays.

Source proof order: the primary source has minimum priority, preserving registry order for equal priorities.
Exact price multiplication is commutative and traverses the registry directly.

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

Purpose: quantize a represented positive amount upward to an arbitrary represented positive quantum without constructing a scalar amount/quantum quotient.

Scope: an existing payer or owner-selected object scope.

Inputs: temporary `universal_cost_quantize_amount` and optional `universal_cost_quantize_quantum`.

Outputs: temporary `universal_cost_quantize_result`, `universal_cost_quantize_valid`, `universal_cost_quantize_units`, and `universal_cost_quantize_units_valid`, plus exact unit limbs in `uc_exact_units`.

Defaults: an absent or non-positive quantum uses the existing one-unit default; zero and negative values are preserved.
A positive value produces at least one quantum.
A nonrepresentable mathematical price is invalid and must not be paid.
If the price fits but its integer quantum count cannot fit in one scalar, units-validity is zero and scalar units zero means unavailable; the exact unit limbs retain the count.
The inspected production consumers do not read scalar units.

Side effects: temporary arithmetic only, through `universal_cost_exact_quantize_scalar`.

Example:

```txt
set_temp_variable = { universal_cost_quantize_amount = owner_amount }
set_temp_variable = { universal_cost_quantize_quantum = owner_quantum }
set_temp_variable = { universal_cost_quantize_result = constant:universal_cost_framework.zero }
set_temp_variable = { universal_cost_quantize_valid = constant:universal_cost_framework.zero }
set_temp_variable = { universal_cost_quantize_units = constant:universal_cost_framework.zero }
set_temp_variable = { universal_cost_quantize_units_valid = constant:universal_cost_framework.zero }
resize_temp_array = { array = uc_exact_units size = constant:universal_cost_framework.one }
universal_cost_round_up_to_quantum = yes
```

## universal_cost_quote_integer

Purpose: calculate one exact payable quote from the represented ordinary current price and every eligible source ratio.

Scope: payer or other existing object scope selected by the owner adapter.

Inputs: temporary `universal_cost_quote_ordinary_cost`, `universal_cost_quote_family_mask`, and optional `universal_cost_quote_rounding_quantum`.
The ordinary cost includes all ordinary consumer modifiers.

Outputs: temporary final/displayed/saved cost, source count, primary source ID, and `universal_cost_quote_valid`.
The retired `universal_cost_quote_composed_ratio` scalar is basis without participating sources and zero meaning unavailable with participating sources; it never controls price or validity.
The exact live source registry replaces scalar composition.

Defaults: an absent or non-positive quantum uses the existing one-unit default.
No eligible source preserves the ordinary amount without rounding.
Zero and negative amounts are preserved.
With an eligible source, the final amount is `ceil(Cticks * product(Rticks) / (Qticks * 1000000000^N)) * Qticks` converted back to scalar units.
No source is rounded separately and no epsilon is added.
Identity sources contribute proof while cancelling their numerator and denominator exactly.
Priority selects the primary source with stable registry-order ties; exact multiplication is commutative.

Side effects: temporary variables and limb arrays only.
The effect calls the same `universal_cost_quote_exact` producer used by the central Black Friday trigger.
A malformed aligned registry or nonrepresentable mathematical scalar output sets quote-validity zero.
The initialized final amount is then diagnostic only; shared quoted affordability rejects it, and owner-specific payment providers must honor the validity result.

Example:

```txt
set_temp_variable = { universal_cost_quote_ordinary_cost = owner_current_cost }
set_temp_variable = { universal_cost_quote_family_mask = constant:universal_cost_family.equipment }
set_temp_variable = { universal_cost_quote_rounding_quantum = owner_quantum }
set_temp_variable = { universal_cost_quote_final_cost = constant:universal_cost_framework.zero }
set_temp_variable = { universal_cost_quote_displayed_cost = constant:universal_cost_framework.zero }
set_temp_variable = { universal_cost_quote_saved_cost = constant:universal_cost_framework.zero }
set_temp_variable = { universal_cost_quote_valid = constant:universal_cost_framework.zero }
set_temp_variable = { universal_cost_quote_source_count = constant:universal_cost_framework.zero }
set_temp_variable = { universal_cost_quote_primary_source_id = constant:universal_cost_framework.zero }
set_temp_variable = { universal_cost_quote_composed_ratio = constant:universal_cost_framework.zero }
universal_cost_quote_integer = yes
# Check universal_cost_quote_valid before affordability or owner payment.
```

The [exact predicate documentation](../scripted_triggers/chaosx_universal_cost_exact_triggers.md) gives every internal helper's inputs/outputs, bounds, iteration mechanism, and direct call sites.
Every owner caller must predefine the temporary outputs it reads after a public helper returns, before that call.
Initializing outputs inside the public helper protects nested producers but does not export new names into its outer caller.
The same caller-storage contract covers Black Friday register/clear results, quoted-affordability results, and standalone unit-limb arrays.
The [caller lifetime contract](../scripted_triggers/chaosx_universal_cost_exact_triggers.md#caller-owned-temporary-lifetime) records all internal boundaries and the conservative actual-source VM.
The [implementation handoff](../../docs/plans/026_black_friday_plans/subagent_handoffs/2026-10-03_exact_quote_implementation.md) separates actual source-semantic checks from missing MCP and native evidence.

## universal_cost_rebuild_custom_quote_ratio_cache

Purpose: publish the existing Event 026 source-readiness marker and retire lossy scalar cache rows.
The aligned live source registry is the exact quotation cache for all caller family masks, including combinations and noncanonical bits.

Scope: existing owner effect scope.

Inputs: the current source registry, already mutated by registration or source-identified clear.

Output: `global.universal_cost_custom_quote_cache_valid = 1`.

Side effects: calls `universal_cost_clear_custom_quote_ratio_cache` to remove twelve obsolete `global.universal_cost_custom_quote_ratio_*` variables before publishing readiness.
It never rounds a probe price, visits twelve families, or replaces another source row.
It does not touch payer receipts.

## universal_cost_clear_custom_quote_ratio_cache

Purpose: invalidate the existing Event 026 readiness marker and remove the twelve obsolete scalar cache variables.

Scope: existing owner effect scope.

Inputs: none.

Output: `global.universal_cost_custom_quote_cache_valid = 0`.

Side effects: removes only retired scalar cache variables.
The exact live source registry and all historical receipts remain intact.
Source expiry is performed by `universal_cost_source_clear`, which removes only the matching aligned source row.
Remaining sources continue to participate in generic exact quotes.

## universal_cost_check_quote_affordable

Purpose: check the quoted final amount against a native resource without debiting it.

Scope: payer country.

Inputs: temporary `universal_cost_quote_resource_kind`, `universal_cost_quote_final_cost`, and `universal_cost_quote_valid` from a fresh quote.

Output: temporary `universal_cost_quote_affordable`.

Defaults: a quote must have `universal_cost_quote_valid = 1` before resource affordability is evaluated.
Within a valid quote, zero and negative amounts are affordable; unsupported owner-adapter resource kinds are not affordable through this helper.

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
| `cbrn_instrument_equipment_1` | 17 | `NOT = { has_equipment = { cbrn_instrument_equipment_1 < universal_cost_affordability_amount } }` | `add_equipment_to_stockpile = { type = cbrn_instrument_equipment_1 amount = universal_cost_payment_delta }` | `add_equipment_to_stockpile = { type = cbrn_instrument_equipment_1 amount = universal_cost_payment_amount }` |
| `cbrn_instrument_equipment_2` | 18 | `NOT = { has_equipment = { cbrn_instrument_equipment_2 < universal_cost_affordability_amount } }` | `add_equipment_to_stockpile = { type = cbrn_instrument_equipment_2 amount = universal_cost_payment_delta }` | `add_equipment_to_stockpile = { type = cbrn_instrument_equipment_2 amount = universal_cost_payment_amount }` |
| `cbrn_instrument_equipment_3` | 19 | `NOT = { has_equipment = { cbrn_instrument_equipment_3 < universal_cost_affordability_amount } }` | `add_equipment_to_stockpile = { type = cbrn_instrument_equipment_3 amount = universal_cost_payment_delta }` | `add_equipment_to_stockpile = { type = cbrn_instrument_equipment_3 amount = universal_cost_payment_amount }` |
| `gas_mask_equipment_reconditioned` | 20 | `NOT = { has_equipment = { gas_mask_equipment_reconditioned < universal_cost_affordability_amount } }` | `add_equipment_to_stockpile = { type = gas_mask_equipment_reconditioned amount = universal_cost_payment_delta }` | `add_equipment_to_stockpile = { type = gas_mask_equipment_reconditioned amount = universal_cost_payment_amount }` |
| `gas_mask_equipment_1` | 21 | `NOT = { has_equipment = { gas_mask_equipment_1 < universal_cost_affordability_amount } }` | `add_equipment_to_stockpile = { type = gas_mask_equipment_1 amount = universal_cost_payment_delta }` | `add_equipment_to_stockpile = { type = gas_mask_equipment_1 amount = universal_cost_payment_amount }` |
| `gas_mask_equipment_2` | 22 | `NOT = { has_equipment = { gas_mask_equipment_2 < universal_cost_affordability_amount } }` | `add_equipment_to_stockpile = { type = gas_mask_equipment_2 amount = universal_cost_payment_delta }` | `add_equipment_to_stockpile = { type = gas_mask_equipment_2 amount = universal_cost_payment_amount }` |
| `gas_mask_equipment_3` | 23 | `NOT = { has_equipment = { gas_mask_equipment_3 < universal_cost_affordability_amount } }` | `add_equipment_to_stockpile = { type = gas_mask_equipment_3 amount = universal_cost_payment_delta }` | `add_equipment_to_stockpile = { type = gas_mask_equipment_3 amount = universal_cost_payment_amount }` |
| `gas_mask_equipment_4` | 24 | `NOT = { has_equipment = { gas_mask_equipment_4 < universal_cost_affordability_amount } }` | `add_equipment_to_stockpile = { type = gas_mask_equipment_4 amount = universal_cost_payment_delta }` | `add_equipment_to_stockpile = { type = gas_mask_equipment_4 amount = universal_cost_payment_amount }` |
| `decontamination_equipment_1` | 25 | `NOT = { has_equipment = { decontamination_equipment_1 < universal_cost_affordability_amount } }` | `add_equipment_to_stockpile = { type = decontamination_equipment_1 amount = universal_cost_payment_delta }` | `add_equipment_to_stockpile = { type = decontamination_equipment_1 amount = universal_cost_payment_amount }` |
| `decontamination_equipment_2` | 26 | `NOT = { has_equipment = { decontamination_equipment_2 < universal_cost_affordability_amount } }` | `add_equipment_to_stockpile = { type = decontamination_equipment_2 amount = universal_cost_payment_delta }` | `add_equipment_to_stockpile = { type = decontamination_equipment_2 amount = universal_cost_payment_amount }` |
| `decontamination_equipment_3` | 27 | `NOT = { has_equipment = { decontamination_equipment_3 < universal_cost_affordability_amount } }` | `add_equipment_to_stockpile = { type = decontamination_equipment_3 amount = universal_cost_payment_delta }` | `add_equipment_to_stockpile = { type = decontamination_equipment_3 amount = universal_cost_payment_amount }` |
| `motorized_equipment_0` | 28 | `NOT = { has_equipment = { motorized_equipment_0 < universal_cost_affordability_amount } }` | `add_equipment_to_stockpile = { type = motorized_equipment_0 amount = universal_cost_payment_delta }` | `add_equipment_to_stockpile = { type = motorized_equipment_0 amount = universal_cost_payment_amount }` |
| `motorized_equipment_1` | 29 | `NOT = { has_equipment = { motorized_equipment_1 < universal_cost_affordability_amount } }` | `add_equipment_to_stockpile = { type = motorized_equipment_1 amount = universal_cost_payment_delta }` | `add_equipment_to_stockpile = { type = motorized_equipment_1 amount = universal_cost_payment_amount }` |
| `motorized_equipment` | 7 | `NOT = { has_equipment = { motorized_equipment_1 < universal_cost_affordability_amount } }` | `add_equipment_to_stockpile = { type = motorized_equipment_1 amount = universal_cost_payment_delta }` | `add_equipment_to_stockpile = { type = motorized_equipment_1 amount = universal_cost_payment_amount }` |
| `train_equipment` | 8 | `NOT = { has_equipment = { train_equipment < universal_cost_affordability_amount } }` | `add_equipment_to_stockpile = { type = train_equipment amount = universal_cost_payment_delta }` | `add_equipment_to_stockpile = { type = train_equipment amount = universal_cost_payment_amount }` |
| `train_equipment_1` | 12 | `NOT = { has_equipment = { train_equipment_1 < universal_cost_affordability_amount } }` | `add_equipment_to_stockpile = { type = train_equipment_1 amount = universal_cost_payment_delta }` | `add_equipment_to_stockpile = { type = train_equipment_1 amount = universal_cost_payment_amount }` |
| `convoy` | 9 | `NOT = { has_equipment = { convoy_1 < universal_cost_affordability_amount } }` | `add_equipment_to_stockpile = { type = convoy_1 amount = universal_cost_payment_delta }` | `add_equipment_to_stockpile = { type = convoy_1 amount = universal_cost_payment_amount }` |
| `stability` | 15 | `NOT = { has_stability < universal_cost_affordability_amount }` | `add_stability = universal_cost_payment_delta` | `add_stability = universal_cost_payment_amount` |
| `war_support` | 16 | `NOT = { has_war_support < universal_cost_affordability_amount }` | `add_war_support = universal_cost_payment_delta` | `add_war_support = universal_cost_payment_amount` |

Evidence for the three added native branches is the installed vanilla documentation at `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/triggers_documentation.md`, which documents `has_army_experience` and `has_equipment`, and `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md`, which documents the country-scope `army_experience` effect and country-scope `add_equipment_to_stockpile` effect.

The installed equipment definitions corroborate the concrete aliases at `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/units/equipment/support.txt` (`support_equipment_1`) and `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/units/equipment/trains.txt` (`train_equipment_1`).

Event 026 consumes the support and train aliases in `common/scripted_effects/026_black_friday_effects.txt` and `common/scripted_triggers/026_black_friday_triggers.txt`, so the framework keeps their resource-kind ids distinct while dispatching the exact native equipment tokens.
The CBRN instrument kinds dispatch only their concrete models from `common/units/equipment/cbrn_protective_equipment.txt`, preserving model identity for a later receipt refund.
The five gas-mask and three decontamination kinds likewise dispatch exact models from that file, while `motorized_equipment_0` and `motorized_equipment_1` dispatch exact vanilla models from `common/units/equipment/motorized.txt`.
The older `motorized_equipment` kind retains its existing model-1 dispatch for existing consumers.
An exact-model credit restores the model count recorded in the receipt, but the stockpile effect cannot reconstruct the original producer or equipment-design variant provenance.

## universal_cost_pay_component

Purpose: debit one positive quoted component through a supported native resource effect.

Scope: payer country.

Inputs: temporary `universal_cost_payment_resource_kind` and positive `universal_cost_payment_amount`.

Output: temporary `universal_cost_payment_result`.

Supported kinds: Political Power, Command Power, Army Experience, Navy Experience, Air Experience, Stability, War Support, Manpower, Fuel, Infantry Equipment, Support Equipment, Support Equipment 1, CBRN Instrument Equipment 1 through 3, Gas Mask Equipment Reconditioned and 1 through 4, Decontamination Equipment 1 through 3, the existing Motorized Equipment kind, concrete Motorized Equipment 0 and 1, Train Equipment, Train Equipment 1, and Convoy 1.

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

Inputs: positive owner-allocated `universal_cost_transaction_id`, positive unique `universal_cost_transaction_component_id`, positive `universal_cost_transaction_resource_kind`, non-negative `universal_cost_transaction_ordinary_cost`, `universal_cost_transaction_quoted_cost`, and `universal_cost_transaction_actual_paid_cost`, plus optional `universal_cost_transaction_resource_id`, `universal_cost_transaction_source_id`, and positive `universal_cost_transaction_primary_component`.

Outputs: `universal_cost_record_transaction_result` and `universal_cost_recorded_component_index`.

Defaults: a new transaction row starts in recorded/refundable state; repeated component ids, reused refunded/settled transaction ids, negative amounts, and actual-paid values that differ from the quote are rejected.

Side effects: appends the component, updates aligned totals and the transaction's component links, and retains actual paid amount as the only refund basis. A first row consumes the allocator proof; an existing indexed transaction can accept another distinct component while recorded. A map-absent legacy row cannot be extended through the linked path.

Multi-resource contract: call once per component with the same logical transaction id and a different component id, then settle or refund the transaction once.
For an aggregate stockpile quote distributed across concrete models, the owner must use one distinct component id per model and record exact model-specific quoted and paid amounts while preserving the single aggregate ordinary and quoted totals.
If sale affordability permits fewer units than the ordinary price, any unfilled ordinary counterfactual amount may be assigned to a participating model's ordinary receipt field or a zero-paid model component; that amount is accounting only and must never be debited.
The shared record helper requires quoted and actual-paid amounts to match per component but does not independently apply a sale ratio to each component.

## Internal ledger helpers

The following internal helpers maintain the same payer-country scope as `universal_cost_record_transaction`.
`universal_cost_find_transaction_row` accepts temporary `universal_cost_transaction_lookup_id` and returns `universal_cost_transaction_found_index`, `universal_cost_transaction_is_indexed`, `universal_cost_transaction_lookup_result`, and `universal_cost_transaction_pointer`; it validates a targeted row pointer or performs a bounded legacy scan, and has no persistent side effects.
`universal_cost_find_component_row` accepts temporary transaction and component lookup IDs and returns `universal_cost_component_found_index` and `universal_cost_component_lookup_result`; it traverses and validates every link for an indexed receipt, or performs a bounded legacy scan, and has no side effects.
`universal_cost_validate_component_chain` accepts the current transaction ID and row index and returns temporary `universal_cost_chain_valid`; it checks count, every pointer and transaction ID, and the tail before crediting, and has no side effects.
`universal_cost_refund_component_at_cursor` accepts the current component cursor and credits its stored actual-paid amount only when still unrefunded; it changes the component state, refund totals, and current non-political count after a successful credit.
`universal_cost_decrement_non_political_paid_count` accepts the current transaction and component row indices and decrements the current non-political component count only for a positive non-Political-Power component's first refund acknowledgment.

For example, an owner that has allocated ID `black_friday_owner_transaction_id` sets `universal_cost_transaction_id` to that ID and calls `universal_cost_record_transaction = yes` once per component; on a failed later component it calls `universal_cost_refund_transaction = yes` with the same ID and checks `universal_cost_refund_transaction_result` before claiming rollback.

## Receipt API temporary return contract

Every caller creates the temporary outputs it reads after a scripted helper returns BEFORE invoking that helper.
Initializing those fields inside the helper protects its children, not its outer caller.
Regular payer receipt arrays, targeted row pointers and native resources persist independently of temporary helper frames.
Private lookup scratch created inside `record`, `settle`, `mark`, or `refund` is not an exported public result unless its outer caller also declared that exact temporary name.
Owners needing a row after a public receipt operation should initialize and invoke the public lookup explicitly.

| Helper | Caller-defined temporary outputs / in-out fields | Persistent side effects |
| --- | --- | --- |
| `universal_cost_pay_component` | `universal_cost_payment_result` | native debit only after inclusive resource affordability |
| `universal_cost_credit_component` | `universal_cost_credit_result` | native credit of the supplied stored-paid amount |
| `universal_cost_find_transaction_row` | found index, indexed flag, lookup result, pointer | none |
| `universal_cost_find_component_row` | component found index and lookup result | none |
| `universal_cost_record_transaction` | record result and recorded component index | regular receipt rows, links, totals and allocator-proof consumption |
| `universal_cost_settle_transaction` | settle result | existing receipt state |
| `universal_cost_decrement_non_political_paid_count` | no temporary return; transaction/component indices and indexed flag are inputs | existing non-political-paid count |
| `universal_cost_mark_component_refunded` | acknowledgement result | component state, refund total and non-political-paid count |
| `universal_cost_validate_component_chain` | `universal_cost_chain_valid` | none |
| `universal_cost_refund_component_at_cursor` | inherited refund total, unhandled total, all-complete flag | stored-paid native credit, component state and count |
| `universal_cost_refund_transaction` | refund result, newly credited total and unhandled total | validated receipt/component states and refund accounting |

Transaction lookup output storage is initialized at all five nested lookup call sites, including inside the component finder.
Component lookup outputs are initialized before record/acknowledgement checks.
Refund initializes chain validity before its validation call, and the component-credit callback initializes `universal_cost_credit_result` before native credit dispatch.
These are local caller declarations of specific callee outputs; they do not reset outer refund cursors, running totals, accumulated incomplete flags, or unrelated scratch.
Refund totals and all-complete status are inherited in-out state across component callbacks and are not cleared between components.

Example lookup in an existing owner effect:

```txt
set_temp_variable = { universal_cost_transaction_lookup_id = owner_transaction_id }
set_temp_variable = { universal_cost_transaction_found_index = constant:universal_cost_framework.invalid_index }
set_temp_variable = { universal_cost_transaction_is_indexed = constant:universal_cost_framework.zero }
set_temp_variable = { universal_cost_transaction_lookup_result = constant:universal_cost_framework.result_no_op }
set_temp_variable = { universal_cost_transaction_pointer = constant:universal_cost_framework.zero }
universal_cost_find_transaction_row = yes
```

Before calling record, define `universal_cost_record_transaction_result` and `universal_cost_recorded_component_index` in that owner frame.
Before refund, define `universal_cost_refund_transaction_result`, `universal_cost_refund_total`, and `universal_cost_refund_unhandled_total` in the owner frame.
Apply the same rule to payment, credit, settlement and acknowledgement results whenever the owner reads them after return.

[Real receipt source tests](../../docs/plans/026_black_friday_plans/subagent_handoffs/universal_cost_receipt_lifetime_source_tests.js) reuse the quotation VM with conservative cleanup on ALL scripted returns and execute the actual receipt, debit, credit and native-affordability helper definitions.
Shared receipt APIs are not mocked.
Only native resource effects/queries use modeled balances; allocator proofs are explicit persisted fixture inputs that the actual record helper validates and consumes.
The suite covers cold/warm returns, interleaved links, owner-credited partial refunds and retries, zero-paid components, corrupt pointers/counts/tails/cycles, payer isolation, legacy mapless behavior, indexed receipts beyond row 1,000, all 29 native dispatch pairs, and quote/payment/record/expiry/refund integration.
These are authoritative source-semantic checks under the documented lifetime model, not native resource, save/reload, or performance proof.

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

Side effects: an indexed transaction's complete linked chain is validated before any credit. Native components are credited once, their per-component state changes to refunded, and a fully refunded row changes to the refunded transaction state. A repeat call skips already-refunded components, while an invalid linked chain returns rejected before any credit.

## Engine boundary

The engine does not provide one generic effect that accepts an arbitrary dynamic resource token, one generic value for every ordinary purchase modifier, a dynamic global-flag name, or a transactional rollback spanning unrelated native effects.

The framework therefore uses numeric source/family/resource enums, aligned arrays, twenty-nine fixed native payment branches, fixed-point quanta for deliberate Stability and War Support payments, and an explicit owner adapter for factory commitments, technology, advisor, idea, operation, equipment-design, and other inaccessible surfaces.

The native resource contract includes Political Power, Command Power, Army Experience, Navy Experience, Air Experience, Manpower, Fuel, Infantry Equipment, Support Equipment, Motorized Equipment, Trains, Convoys, Stability, and War Support. Stability and War Support callers must pass `constant:universal_cost_fixed_point_quantum.stability` or `constant:universal_cost_fixed_point_quantum.war_support` as their rounding quantum; integer callers use the default one-unit quantum.

`custom_adapter` remains an explicit owner-paid and owner-refunded resource kind and is intentionally absent from the native branch map.

An owner adapter must keep eligibility and reserve checks unchanged, compute the ordinary current payable cost, call `universal_cost_quote_integer` for display and again immediately before payment, execute its own unsupported payment effect, call `universal_cost_record_transaction` with actual paid amount equal to the displayed quote, and call either `universal_cost_mark_component_refunded` after an external refund or `universal_cost_settle_transaction` after the cancellation window closes.
