# CBRN Immediate Response decision audit

Disposition: read-only audit completed against the current shared source; no unresolved source defect was confirmed after the parent fixes described below.

Scope: Emergency Distribution and Hospitals/Utilities only, including their existing targeted-decision gates and callbacks, the new owner quote/payment adapters, physical issue and model ledgers, display getters, row localisation, receipt metadata, and cleanup.

Acceptance basis: docs\specs\chaos_warfare_system_specs\corrections\2026-10-03_immediate_protection_sale_transactions.md accepts canonical Event 026 pricing for these two owner actions while preserving target rules, CBRN outcomes, exact raid alert behavior, durations, and AI willingness.

The owner architecture handoff at docs\plans\chaos_warfare_system_plans\subagent_handoffs\2026-10-03_cbrn_immediate_protection_cost_architecture_review.md supplies the accepted transaction shape and ownership boundary; shared Event 026 and universal-cost APIs remain owned by their active editors.

## Findings sorted by severity

No current source defect remains in the bounded surface after parent changes.

1. P1 transaction-recovery finding resolved before handoff: the initial owner adapter called native credit and receipt-refund helpers without checking their results.

   Current cbrn_pay_and_record_response_component checks universal_cost_credit_result and retains the exact unrecorded resource kind and amount under the allocated transaction key when the credit fails at common\scripted_effects\cbrn_immediate_response_cost_effects.txt:38-52.

   Current cbrn_refund_unfinished_response_transaction checks rejected or partial refunds and unhandled totals, persists the result by transaction ID, retries the exact unrecorded debit, clears that retry record only after a successful native credit, and clears allocator proof only when no receipt row was written at common\scripted_effects\cbrn_immediate_response_cost_effects.txt:60-99.

   The emergency positive-issue receipt guard remains first in that cleanup path, so a later settlement failure retains the physically issued protection and cannot trigger a crate or Political Power refund or an Event 026 purchase credit.

   These source branches avoid claiming a complete rollback after a partial or rejected refund; no native failure or refund behavior was executed by this audit.

2. P1 player-facing cost-icon finding resolved before handoff: the four Emergency Distribution and Hospitals/Utilities cost-row strings initially contained literal question-mark prefixes where text icons belonged.

   Current cost rows use the real £pol_power, £GFX_archetype_gas_mask_equipment_medium, and £support_equipment_text_icon tokens at localisation\english\cbrn_protection_l_english.yml:71-72,87-88.

   Each dynamic amount getter chooses a separate red or yellow amount key at localisation\english\cbrn_protection_l_english.yml:159-168; the four row strings now bind those getters in the same file.

   I checked the saved text has UTF-8 BOM bytes EF-BB-BF, the icon prefix is U+00A3 (£), and the amount keys contain red or yellow section-sign markup (§R and §Y).

3. P2 outcome-tooltip finding resolved before handoff: the decision callbacks still emit their completion tooltip before the fresh payment gates run, but the current text describes the results conditionally.

   Emergency Distribution now begins its completion text with “If respirator crates can be issued” at localisation\english\cbrn_protection_l_english.yml:74.

   Hospitals/Utilities now begins with “If all supplies can be secured” at localisation\english\cbrn_protection_l_english.yml:90.

   These strings do not promise successful coverage or protection on a stale-click path rejected by the in-effect affordability and target rechecks.

## Decision category lifecycle

Both decisions remain in cbrn_civil_defence_category in common\decisions\cbrn_protection_decisions.txt.

Emergency Distribution is an instant state-targeted decision with a native reenabling interval; its country visibility requires a public chemical emergency, and its FROM state must be controlled by the actor and have a current emergency context, a positive protection gap, and no used surge marker.

Hospitals/Utilities is an instant state-targeted decision with the same response reenabling interval; its row appears for states under the actor’s control with an active exact raid alert and no existing secured flag.

Emergency affordability includes the current canonical Political Power quote and a positive stock-capped physical crate quote; the actual distribution effect then consumes real mask models and applies the existing state issue ledger, wastage, fitting, filter, and military-priority calculations.

Hospital affordability uses the existing per-state mask and support cost anchors, quotes each payable component, allocates the aggregate mask amount oldest-first across the five stored models, and consumes only those models and the support-equipment model.

Neither action adds a mission, a timed decision project, a new category, a new tab, a scripted GUI, a country/world iteration, or a new authorization tier.

The parent-owned follow-up adds only owner-side shared quote and payment helpers and delegates these two existing decision callbacks; unrelated decision families remain outside this audit.

## Cognitive load and player-facing values

Emergency Distribution displays two spendable values: Political Power and the pooled physical respirator issue, with the emergency stock limit and reduced coverage explained in its description and cost tooltip.

Hospitals/Utilities displays three spendable values: Political Power, pooled mask material, and Support Equipment; its completion text names the medical-protection consequence and duration.

Both actions have at most three inline values, each with a corresponding text icon and an individual red or yellow amount state; the five concrete mask models are receipt and allocation rows inside one pooled mask cost.

The decision family adds no active missions, raw trigger text, unlabelled counter, unrelated timer, or GUI explanation wall.

Targeted entries can appear for multiple qualifying states, so exact native list density remains a scenario-render question rather than a source-only count claim.

## Mission and outcome notes

There are no mission definitions in this tranche.

Emergency Distribution belongs to the acting country and resolves in the selected controlled state; zero consumed crates call the refund path and do not set the surge flag, apply the congestion outcome, settle an achievement purchase, or claim successful distribution.

A positive physical issue sets a transaction-keyed committed receipt, applies the existing emergency state outcome, and only records Event 026 purchase credit after successful transaction settlement.

Hospitals/Utilities belongs to the acting country and the selected controlled state with an active exact alert; its flag and dynamic protection modifier are applied only after every component is recorded and the transaction settles successfully.

An incomplete hospital payment or failed settlement skips the paid outcome and invokes the exact receipt-refund path; actual refund results are retained for unresolved partial or rejected cases.

The same-country, same-state concurrency lock is supplied by the existing emergency surge flag or hospital secured flag; other states remain independent.

## Cost, requirement, and boundary clarity

Emergency Distribution has two cost types: one Political Power fee and the pooled respirator-crate issue; nominal PP is 10, and the canonical normal, half-price, and quarter-price quotes are 10, 5, and 3.

The physical emergency shipment is not discounted; its quantity remains the current state issue quote capped to real donor stock.

Hospitals/Utilities has three cost types: one PP fee, pooled mask material, and Support Equipment; at population_k 1000 the accepted ordinary material totals are 30 masks and 20 support, half-sale totals are 15 and 10, and quarter-sale totals are 8 and 5 after whole-unit upward rounding.

The support anchor uses ratio 0.01 with minimum 20, so at population_k 1000 the minimum governs the ordinary support cost; the mask anchor uses ratio 0.03 and produces 30.

Each action has one source of truth for quote, affordability, display, and payment; the complete-effect adapters quote and validate again immediately before the first debit.

Exact affordability is inclusive: native resource checks use universal_cost_component_is_affordable, whose positive-resource branches accept an exact balance, and hospital mask allocation passes when its post-allocation remainder is zero.

Hospital mask payment allocation runs reconditioned, basic, improved, advanced, and sealed models in the same order used by its quote; each concrete receipt component has a unique positive component ID equal to its distinct resource-kind ID.

Hospital Support Equipment is paid and refunded as support_equipment_1; the archetype-level cost row is a pooled display for the real oldest-first mask-model composition.

Custom-cost availability and custom-cost row status call the same payment-ready predicate; target eligibility remains separate so insufficient resources can still produce red per-cost values instead of hiding the target.

No literal resource name or fourth spendable type is added, and no ordinary owner debit helper is called after the new adapter payment.

## AI validity and route locks

The two ai_will_do willingness bodies and their target factors remain unchanged; only their fixed Political Power saving hints use the minimum whole-unit hint of 1.

Emergency target checks require a public chemical emergency plus a controlled state with a current warning or contamination and a positive physical issue gap.

Hospital target checks require the selected state to be controlled by the actor, to carry the exact current raid-alert flag, and not to be already secured; the country preflight checks the same target before spending.

No invalid target, dead country, closed sale source, disabled route, or free issuance path was found in these owner helpers.

The separate probability auditor and parent MCP client own weighted-logic evaluation and comparison; this handoff makes no AI score or selection-rate claim.

## Localisation, tooltip, and icon coverage

The Emergency Distribution title, description, ready and blocked cost rows, cost tooltip, completion text, cost getters, and ten amount-color keys are present in localisation\english\cbrn_protection_l_english.yml.

The Hospitals/Utilities title, description, ready and blocked cost rows, cost tooltip, completion text, three cost getters, and six amount-color keys are present in the same file.

The archetype gas-mask sprite is registered in interface\cbrn_protection.gfx and the support-equipment text icon is registered in interface\chaosx_texticons.gfx.

The current completion text is conditional on issue or full payment; the cost text says the displayed resources are consumed when the order is given.

No missing alias, raw resource-name cost, malformed prefix, or missing icon registration was found in the two audited rows.

## Receipt metadata, cleanup, and exploit risk

Emergency Distribution records one PP component under the political_power family and primary_component basis; all source IDs, fee quotes, and actual-paid values are populated from the same current quote.

Hospitals/Utilities records PP, support_equipment_1, and up to five mask-model components under the state_project family and primary_group basis; PP is excluded from the paid material group and the exact mask plus support paid totals are used for purchase metadata.

The unique component IDs are Political Power 1, Support Equipment 11, and mask models 20 through 24; the transaction framework allows up to 999 components, so this seven-row maximum fits.

All current native payment and credit kinds used by these receipts are present in the shared dispatchers; the owner never sends custom_adapter to a native payment branch.

The emergency receipt guard prevents refunds after positive physical issue; zero-issue emergency orders refund the fee and do not grant issue outcomes or purchase credit.

The hospital receipt either settles once before its outcome or refunds recorded components and retries any unrecorded native credit by the exact transaction-keyed resource and amount.

The allocator proof is cleared only when no first receipt row exists; recorded, partially refunded, and issued receipts retain the receipt state needed to prevent ID reuse or duplicate credit.

No repeat-payment, repeated-credit, free-crate, model-farming, cross-state suppression, or post-alert outcome loop was found in the bounded source path.

## References and validation limits

The accepted correction is docs\specs\chaos_warfare_system_specs\corrections\2026-10-03_immediate_protection_sale_transactions.md, and the implementation boundary is docs\plans\chaos_warfare_system_plans\subagent_handoffs\2026-10-03_cbrn_immediate_protection_cost_architecture_review.md.

Offline Decision modding lines 305-356 describe custom-cost localisation, hidden payment callbacks, AI hints, and instant decision effects; SHA-256 7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162.

Offline Data structures lines 437-442 describe temporary-variable lifetimes and unscoped behavior; SHA-256 62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4.

Offline Scopes lines 260-263 describe ROOT and FROM in targeted decisions; SHA-256 18ef5249e4991f5427eca9ec4a2f66dd47f51e26a491c730adc622f1f5db1b49.

Offline Effects line 2253 documents add_equipment_to_stockpile; SHA-256 997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c.

Offline Localisation lines 221-242 document text-icon syntax and GFX registration; SHA-256 1a8f72362a34b4bb653186746b9fae0b98e463205cb02f12ccf2c3d9ccd3a064.

Offline Triggers lines 723 and 1516 document Political Power and equipment checks; SHA-256 abc51ad18a2c46e46d47ba795c5a840ebaf7c4ae3e777426c64a9f4c0c0ce06.

Installed common\decisions\_documentation.md lines 12-35 records native visible/available and targeted decision scopes and cadence; SHA-256 5e7e686b5582f32c38d898d805e17171e88f3bfeee4a030deb1884f9726de019.

Installed effects_documentation.md lines 1252-1264 documents stockpile additions and negative removal; SHA-256 2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af.

Installed triggers_documentation.md lines 3835-3843 and 4547-4555 documents equipment and Political Power checks; SHA-256 7d27ed77dadf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29.

Installed vanilla common\decisions\_generic_decisions.txt lines 272-298 provides a decision cost, stock check, and effect precedent; SHA-256 83cd276f8fd2c0c90470225c996d7afee7b8c08437289dd23d819a4a29edb187.

Source review covered common\scripted_triggers\cbrn_immediate_response_cost_triggers.txt:7-165, common\scripted_effects\cbrn_immediate_response_cost_effects.txt:8-219, common\scripted_localisation\cbrn_immediate_response_cost_localisation.txt:4-117, common\decisions\cbrn_protection_decisions.txt:343-452, common\scripted_triggers\cbrn_protection_triggers.txt:424-483 and 736-779, common\scripted_effects\cbrn_protection_decision_effects.txt:145-147, 462-479, and 537-539, common\scripted_effects\cbrn_protection_effects.txt:1477-1603 and 1803-1896, common\script_constants\cbrn_system_constants.txt:977 and 1003-1010, localisation\english\cbrn_protection_l_english.yml:68-90 and 159-168, interface\cbrn_protection.gfx:24, and interface\chaosx_texticons.gfx:90.

The parent reports its actual-source parser suite passed 19 checks after the latest fixes; I did not run that suite.

No HOI4 MCP call, decision scenario, probability pass, or native GUI render was run by this auditor; the parent’s separate MCP client and probability assignment own those pending checks.

No game was launched, no logs were searched, and no source file was edited, staged, or reverted by this auditor.

Skills read and applied: chaos-redux-decisions-missions, chaos-redux-events, and chaos-redux-subagents; no skill was created or updated.

The only file written by this auditor is docs\plans\chaos_warfare_system_plans\subagent_handoffs\2026-10-03_cbrn_immediate_response_decision_audit.md.
