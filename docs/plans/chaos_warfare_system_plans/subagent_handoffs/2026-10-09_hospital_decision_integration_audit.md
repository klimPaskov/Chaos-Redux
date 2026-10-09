# Hospital Decision Integration Audit

Disposition: read-only source review found no defect in the authorized hospital-entry, quote, payment, and continuing-care integration.
This audit does not close the queued Civil Defence history or automatic state-priority work.

## Scope and changed surfaces reviewed

The four gameplay changes reviewed are in `common/scripted_triggers/cbrn_protection_triggers.txt`, `common/decisions/cbrn_protection_decisions.txt`, `common/scripted_triggers/cbrn_immediate_response_cost_triggers.txt`, and `common/scripted_effects/cbrn_immediate_response_cost_effects.txt`.
The aligned player-facing text is in `localisation/english/cbrn_protection_l_english.yml`.
The principal changed identifiers are `cbrn_state_has_hospital_response_need`, `cbrn_state_can_protect_hospitals_and_utilities`, `cbrn_quote_hospital_response_bundle`, `cbrn_country_hospital_response_payment_ready`, `cbrn_execute_hospital_response_order`, `cbrn_complete_paid_hospital_response`, and the decision `cbrn_protect_hospitals_and_utilities`.

Before this patch, the decision was exposed only for exact alerts and its price helper depended on state cache values initialized by alert registration.
After this patch, exact alerts and live contamination both enter the same controlled-state decision path, and the display, affordability gate, and payment effect regenerate the same price from the current state population and real stock.

## Entry and target path

`cbrn_state_has_hospital_response_need` is a narrow OR of an exact chemical raid alert and `cbrn_state_has_chemical_contamination`.
The decision’s country-level `visible` and `target_root_trigger` both use that same need predicate, and its state `target_trigger` uses `cbrn_state_can_protect_hospitals_and_utilities`.
That state trigger preserves the state-controller check, the same alert-or-contamination need, and the existing `NOT = { has_state_flag = cbrn_hospitals_utilities_secured }` guard.
The availability and custom-cost triggers both route to the same hospital payment-ready helper, which rechecks state eligibility before it allows payment.
The public entry no longer depends on response-cost state caches from `cbrn_register_exact_state_chemical_raid_alert`, and the repair does not change the shared `cbrn_country_has_public_chemical_emergency` or `has_enemy_used_chemical_weapons` contracts.

The new helper matches the accepted entry scope: a controlled state with an exact alert or live chemical contamination.
The unchanged Civil Defence category already reveals on controlled chemical contamination through its existing public emergency helper, so no category or broad emergency helper change was needed.
The decision’s target-root precheck remains subject to HOI4’s normal targeted-decision refresh cadence; this source review does not establish native frame/day timing.

## Quote, affordability, payment, and failure path

The quote helper now builds ordinary mask and support-equipment amounts from the target state’s current `state_population_k`, then applies the same configured ratios, minimums, maximums, and rounding order used by `cbrn_calculate_state_raid_response_costs`.
It checks that the target state is still controlled by the payer before computing a quote.
The quote then passes political power, aggregate respirator demand, the concrete five-model respirator allocation, and support equipment through the existing immediate-response cost component helper.
The same quote helper is called by the three dynamic cost getters, the decision affordability/custom-cost gates, and the actual order effect.
The actual order effect predeclares `cbrn_hospital_ordinary_masks` and `cbrn_hospital_ordinary_support` before the quote call and uses those returned values for accounting, eliminating the prior dependency on alert-populated state cache values.
No persistent price cache or new cost source was added.

A click allocates a transaction only after the live gate succeeds.
The order records and pays political power, support equipment, and each available respirator model; incomplete component payment follows the existing unfinished-transaction refund path.
Hospital protection is applied only after all components are paid and `universal_cost_settle_transaction` reports success.
Only that success branch calls `cbrn_complete_paid_hospital_response`, so a failed quote, partial payment, rejected settlement, or lost target cannot create the hospital flag, modifier, or continuing-care interval without successful payment.
The state gate and 14-day native re-enable timer prevent another ordinary response while the existing secured flag is active.
The shared check is recomputed at payment time, so a stale UI quote cannot authorize a different live debit.

The ordinary mask and support prices retain the same population scaling, clamps, and rounding as the previous cache producer.
The distinct spendable costs remain political power, respirator equipment, and support equipment, each displayed with its corresponding texticon.
No coefficient, unit, support model, payment family, or cooldown changed.
The dynamic cost getters continue to show the full quoted amount in blocked state and separate affordability from price.

## Paid response and continuing-care lifecycle

After successful settlement, `cbrn_complete_paid_hospital_response` applies the existing 14-day hospital flag and modifier and records a state-local paid interval with that same duration.
The existing interval helper union-merges overlapping care periods and `cbrn_delivery.4` consumes only their overlap with the scheduled continuing-loss window; the repair adds no loss coefficient or new periodic scan.
The existing same-mask protection floor, medical calculation, burn-treatment factor, rounding point, and loss cadence remain unchanged.

`cbrn_clear_state_raid_dynamic_modifiers` still centralizes verified response resets and now closes future hospital care through `cbrn_end_active_hospital_protection`.
The existing `on_state_control_changed` callback also closes future state-local care on control changes, including zero-mask states, without refunding or moving country stock.
Both paths preserve already elapsed paid care for a pending assessment, clear the active flag/modifier, and are safe when invoked repeatedly.
The decision remains useful for both a live alert and contaminated states because paid protection history is consumed by the same later continuing-loss callback.

## Text, AI, and remaining limits

The revised description identifies a chemical emergency, which covers both accepted entry cases.
The completion tooltip explains the existing 14-day response and describes later death reduction conditionally, consistent with the continuing model’s reliance on paid overlap and current protection/medical inputs.
The cost row remains three icon-first costs, with no literal resource label or hidden fifth cost.

No `ai_will_do` expression or tuning value changed.
The expanded contamination-only candidate class receives the existing base response score and any existing capital/population modifiers; it does not receive the alert-specific AI factor when no alert flag is present.
This is an unchanged weight expression, not a normalized probability result, and no balance or odds claim is made.
A separate AI weighting decision would need the existing probability auditor route and scenarios if the parent later chooses to tune this behavior.

The existing continuing-protection report documents 125 source-model cases passing before this hospital-entry patch.
The parent reports four additional hospital-entry/quote probes are pending in the architect-owned test extension; they were not present in the visible result file during this review, and I did not run or alter tests.
No native game, MCP, log, or GUI validation was performed, so native targeted-row refresh, native cost-row display, and engine transaction settlement remain source-model limitations rather than confirmed failures.

No source file, test file, localisation file, or shared documentation was changed by this audit; its only output is this handoff.
Skills used: `chaos-redux-decisions-missions`, `chaos-redux-events`, and `chaos-redux-subagents`.

Parent validation receipt: the public-entry/live-quote extension passed as part of 157 modeled source cases plus four ROOT-binding probes.
Its 32 added cases include exact payment boundaries, getter/preflight agreement, stale-cache independence, five-model debit, duplicate/control-loss rejection, and no care after rejected settlement/refund.
Native behavior remains unverified.
