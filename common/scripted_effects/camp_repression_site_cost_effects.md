# Selected-location cost API

This repression-owned API quotes and charges administrative actions at one explicit location.
Its callers are the selected-location ledger buttons and the equivalent generic targeted decisions.
Countrywide policies retain the existing `camp_rework_cost` and resource-consumer families.
No shared Chaos Redux registry, death accounting, restricted stock-item selection, or outcome helper is changed by this API.

## Quote

`camp_rework_prepare_site_cost_quote = yes` is a country-scope scripted trigger declared in `../scripted_triggers/camp_repression_site_cost_triggers.txt`.
It performs deterministic temporary arithmetic and returns true for a valid supplied state scope.
Every external caller immediately initializes the required unscoped temporary `camp_site_cost_state_id` before the boolean helper call.
The GUI copies `camp_selected_state_id`, targeted decisions and their localisation copy `FROM.id`, and dispatcher execution copies `camp_rework_action_state_id`.
Only the quote calculator enters `var:camp_site_cost_state_id` to read building levels.
Affordability and payment retain the original country scope as payer.
Nested helper calls forward the initialized temporary without replacing it, and payment callers initialize it again after the execution guard.
There is no default target, persistent input cache, or global event target.
For a negated affordability predicate, initialize the input outside `NOT` so the condition retains its meaning.
It never chooses a target or substitutes the capital, owner, controller, or another site.
The quote is not an action-eligibility check: callers separately validate responsibility, route, control, cooldown, and the action's other existing requirements.

All outputs are unscoped temporary variables.
Callers that need an output after the helper returns must initialize that output in their own trigger/effect block first.
The helper does not clear outputs after computing them.
No persistent quote cache or global quote mode exists.

`L = max(1, building_level@concentration_camp + building_level@extermination_camp + building_level@gulag_labor_camp_network)`.
An eligible marker-only location has the minimum administrative quote.
The formula does not infer detainee counts from territory population and does not price actions from deaths.
All coefficients are in `../script_constants/camp_repression_site_cost_constants.txt`, category `camp_site_cost`.

| Output suffix after `camp_site_quote_` | Formula |
| --- | --- |
| `levels` | L |
| `labor_pp` | 10 + 2L |
| `labor_motorized`, `labor_trains`, `labor_support` | 8L, L, 12L |
| `labor_motorized_reserve`, `labor_trains_reserve`, `labor_support_reserve` | Each payment × 0.25, rounded upward, minimum 1 |
| `labor_motorized_start`, `labor_trains_start`, `labor_support_start` | Matching payment + matching reserve |
| `inspect_pp` | 10 + 3L |
| `dismantle_pp`, `dismantle_manpower`, `dismantle_support` | 15 + 3L, 250 + 100L, 5L |
| `evidence_pp`, `evidence_manpower`, `evidence_command`, `evidence_support` | 10 + 2L, 100 + 50L, 2 + L, 3L |
| `restricted_pp` | 20 + 3L |
| `dismantle_manpower_k`, `evidence_manpower_k` | Matching manpower payment divided by 1,000 |

Payment values are rounded once in the calculator.
Reserve ceiling uses native nearest rounding followed by an integer increment only if the rounded result is below the unrounded reserve.
The `integer_step` constant is the integer rounding unit, independently of the minimum reserve.

Example scripted-localisation trigger for the labor truck amount and its resource colour:

```txt
set_temp_variable = { camp_site_quote_labor_motorized = 0 }
set_temp_variable = { camp_site_quote_labor_motorized_start = 0 }
set_temp_variable = { camp_site_cost_state_id = camp_selected_state_id }
camp_rework_prepare_site_cost_quote = yes
check_variable = {
	var = num_equipment@motorized_equipment_1
	value = camp_site_quote_labor_motorized_start
	compare = greater_than_or_equals
}
```

The corresponding localisation prints `[?camp_site_quote_labor_motorized|0]`.
It uses the paid amount for display and payment-plus-reserve for labour affordability.
Each red/normal branch recomputes its own explicit-state quote rather than relying on a previous failed branch retaining temporary values.

## Affordability and payment

`camp_rework_can_pay_site_labor`, `camp_rework_can_pay_site_inspect`, `camp_rework_can_pay_site_dismantle`, `camp_rework_can_pay_site_evidence`, and `camp_rework_can_pay_site_restricted` use boolean `= yes` calls in country scope and consume the required `camp_site_cost_state_id` temporary input.
Each initializes the outputs it reads, recomputes the quote, and checks inclusive native balances.
Manpower gates use `manpower_k` to avoid the deprecated full-manpower variable's overflow risk.
The restricted predicate checks administrative PP only; its existing separate stock and route predicates remain required.

`camp_rework_pay_site_labor`, `camp_rework_pay_site_inspect`, `camp_rework_pay_site_dismantle`, `camp_rework_pay_site_evidence`, and `camp_rework_pay_site_restricted` are scripted effects in the matching TXT file.
They consume `camp_site_cost_state_id`, initialize retained temporary outputs, recompute the same quote, negate separate scratch amounts, and debit each quoted resource once.
Their required precondition is successful action/target validation plus the corresponding affordability predicate in the enclosing execution guard.
They do not supply an alternative target or independently decide whether the requested action is legal.
No live state or resource mutation occurs between the execution guard and payment in their direct call sites.
The restricted payment effect debits only PP.

Selected GUI execution uses these payment effects directly.
Targeted generic decisions have `cost = 0`, use the corresponding custom-cost predicate in both `available` and `custom_cost_trigger`, and pay through their guarded generic dispatcher branches.
The custom-cost decisions keep fixed engine saving hints at their former nominal PP values: 30 for each labor order, 45 for inspection, 60 for dismantlement, 25 for evidence, and 60 for the combined restricted order.
These hints inform AI saving and do not determine the actual debit; each charge still comes from the explicit-state quote.
No `ai_will_do` weight was retuned.
The parent/auditor comparison evidence is in the plan folder's `ai_hint_evidence` and `site_cost_ai_audit.md`.

## Labor lifecycle and legacy boundary

`camp_rework_pay_site_labor` stores the retained reserve as country variables `generic_labor_project_motorized_reserve`, `generic_labor_project_trains_reserve`, and `generic_labor_project_support_reserve`.
The caller then starts `camp_rework_start_generic_labor_project_payload_in_action_state`, which records the existing mission target and type and performs the existing payload without another equipment payment.
Selection changes do not alter these reserve snapshots.
The mission checks these saved values inclusively while present.

`camp_rework_clear_site_labor_reserve` clears those three country variables.
It is called from normal labor success/failure/cancellation cleanup and forced expansion-project cancellation.
The legacy `camp_rework_start_generic_labor_project_in_action_state` retains its old fixed debit, clears any stale selected reserve, and invokes the same payload-only helper.
Legacy missions without a selected reserve keep their existing fixed reserve predicate.
No global event target, global on-action, or external-core cleanup was introduced.

## Validation and future work

Source-derived arithmetic scenarios and before-edit hashes are in `../../docs/plans/system_camp_repression_rework_plans/ui_polish_2026-09-05/`.
The scenarios check exact affordability, each one-resource shortage, debit equality, reserve rounding, and reserve save/clear behavior, including a Gulag-only location.
This is source evaluation, not a HOI4 engine execution.
Parent-owned MCP visual fixtures, localisation integration, and the independent balance audit remain the final integration evidence.
Future coefficient changes must update the same constant table and rerun those payment/reserve boundaries without modifying countrywide cost families.
No new icons are required: the existing PP, manpower, CP, truck, train, and support-equipment texticons identify these same resources.
