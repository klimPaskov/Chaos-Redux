# Protective Aid factory-sale decision audit

Disposition: source-only audit completed; native decision lifecycle and probability evidence remain unresolved.

Scope: ordinary and Black Friday Protective Aid targeted decisions, their shared callbacks, factory quotation, escrow and PP receipt ownership, cost localisation, icon wiring, cooldown, cancellation, and active-state cleanup.

Acceptance basis: the accepted correction at docs\specs\chaos_warfare_system_specs\corrections\2026-10-03_protective_aid_native_factory_sale.md authorizes native factory variants with commitments of two and one while preserving the 21-day timer, 90-day per-donor, per-state lock, full five-model physical shipment, exact reservation and refund, and successful-delivery PP receipt settlement.

The companion payment contract at docs\plans\026_black_friday_plans\2026-10-03_cbrn_protective_aid_pp_adapter.md treats all five concrete respirator models as variants in one pooled archetype crate payment, not five independently selected fees.

The before-source identity at docs\testing\2026-10-03_cbrn_protective_aid_factory_sale_before\baseline_identity.json states that all seven saved source snapshots match revision f9f057581c080784b92ed14fd0a736f6f9708958 after line-ending normalization; I relied on that record and did not repeat the obsolete constants-file mismatch claim from an earlier handoff.

## Findings sorted by severity

1. P1 acceptance evidence gap: native cancellation timing and release of the selected factory modifier remain unverified when the post-click quote, target, stock, or PP recheck rejects.

   Source confirms that cbrn_protective_aid_should_cancel becomes true when the selected state has no reservation for this donor or either the donor or target is no longer valid, and both native decision IDs use that same cancel trigger and refund callback.

   The cancellation callback closes the reservation count and selected-mode state, refunds any active unused model receipt to its recorded donor, clears the project marker, and marks the PP receipt as an unsuccessful completion.

   The shared 90-day flag keyed by donor and state is intentionally stamped at selection even when activation fails; the accepted design says the lock mirrors native reenabling and blocks switching between the two IDs.

   Exact cancellation tick, removal of civilian_factory_use, and native reenabling after each failed-start case still need a successful decision scenario; this audit makes no claim that a failed click leaks a factory commitment or remains active for all 21 days.

2. P2 acceptance evidence gap: the current native decision cost row and targeted-state list have no successful rendered scenario evidence in the supplied task artifacts.

   No scripted GUI is attached to these decisions, so no dedicated event-owned GUI worker or new-layout reference contract applies.

   The native decision surface still needs a matching normal, sale, active-project, blocked-cost, source-expiry, and multi-target review to prove cost-row fit, tooltip display, and actual visible target-entry density.

   The source has six unique visible action families at most in cbrn_occupation_measures_category because cbrn_authorize_coercive_security is permanently hidden and the two Protective Aid IDs expose one shared public action at a time; state_target entries can multiply per eligible state, so source counts do not prove the rendered list stays below six entries.

3. P2 evidence gap: the ordinary and sale ai_will_do blocks share the same base score and own-core, allied-core, and positive-trauma modifiers, while the sale variant uses a fixed PP hint of 1.

   Source confirms that actual sale quote, affordability, target eligibility, and one-factory commitment still gate selection; it does not prove AI score ranking, repeated selection, starvation, or sensitivity to the 13 and 7 PP sale quotes.

   The parent-assigned chaosx_ai_probability_auditor was still running when this handoff was written; its scenario-specific MCP result and same-scenario probability comparison must be attached before balance claims.

No source-level defect was confirmed in quote fail-closed behavior, ordinary and sale variant exclusivity, cost-row binding, caller-owned nested outputs, escrow callback scopes, selected-mode retention, or idempotent reservation closure.

## Decision category lifecycle

The owner is cbrn_occupation_measures_category in common\decisions\cbrn_occupation_decisions.txt.

The reviewed IDs are cbrn_deploy_protective_aid and cbrn_deploy_protective_aid_sale.

Before this tranche, cbrn_deploy_protective_aid was the single native definition with a two-factory assignment; after the tranche, that ordinary definition remains and the sale ID exposes the same public name, description, icon, map mode, 21-day duration, 90-day native reenabling, callbacks, and willingness logic with a one-factory assignment during a valid one-factory quote.

The source factory quote calls the canonical family-512 producer with ordinary value two and unit rounding, requires the registered Event 026 source when Black Friday is active, and accepts only a valid result of one or two.

An unsupported or unregistered sale quotation fails closed; the code never clamps it into either native definition.

The start branches are mutually exclusive because the ordinary ID requires a live quote of two and the sale ID requires a live quote of one.

The active-project branches instead use the stored donor and state reservation plus sale-mode flag, so a running sale delivery remains the sale variant after source expiry or donor stock depletion.

The selection callback stamps the shared donor-and-state cooldown before its fresh checks, then rechecks the requested price, continuing donor, positive model stock, PP affordability, target validity, and positive crate quote without rechecking the factories already reserved by the native decision.

Successful selection records the exact model escrow, PP fee, receipt, reservation count, active-project flag, and selected factory mode before the 21-day timer resolves.

Completion closes the reservation count, executes delivery against the recorded state, returns unused models through the escrow helper, and marks receipt settlement successful only when the delivery proof is supplied.

Cancellation closes the count and mode, refunds the exact remaining model receipt, clears the project marker, and settles the receipt as an unsuccessful completion.

The variant-independent state flag cbrn_external_aid_purchase_cooldown_@ROOT prevents switching IDs for the same donor and state for 90 days; a different target state may proceed concurrently as accepted.

There are no mission definitions in this tranche.

Each action is a country-owned, state-targeted timed decision in the map-and-decisions view; its region is any foreign-controlled, non-core emergency state with positive current need that can receive this donor’s aid.

## Cognitive load and player-facing values

The category has six unique action families at maximum: protected administration, Protective Aid, state sealing, record destruction, accidental-release admission, and inspection permission; coercive-security authorization is permanently hidden.

The ordinary and sale Protective Aid IDs share one title and description and cannot both show as purchasable variants for the same target state.

Targeted-state row count can exceed the number of action families when multiple states qualify, and the exact on-screen density remains unverified without a declared country and target-state scenario.

No simultaneous mission rows were added; concurrent Protective Aid projects are timed decisions for separate target states and are part of the accepted design.

The visible cost values have clear significance: PP is the administrative payment, the pooled gas-mask archetype amount is the full calculated respirator shipment, and civilian factories remain committed during delivery.

The row shows at most three cost values; the five concrete model amounts are a transparent composition breakdown of the single pooled crate payment and use their registered medium texticons.

The 21-day delivery, 90-day wait before the same donor aids the same state again, sale price changes, and target civilian-coverage goal are explained in the shared description or tooltips.

The description is one sentence and the cost tooltip explains payment timing, sale behavior, full-volume shipment, factory assignment, model refunds, and the state cooldown; no raw trigger block or internal counter is exposed.

No value dump, unexplained threshold, extra tab, category warehouse, or separate scripted GUI was found in this decision surface.

## Cost and requirement clarity

The accepted spendable cost count is three types: Political Power, one pooled respirator-crate archetype payment, and native civilian-factory commitment.

The five stored equipment models are interchangeable variants within that single pooled physical resource; the payment contract and accepted PP adapter plan explicitly establish that interpretation.

The ordinary PP fee is 25; the 50-percent and 25-percent sale quotes are 13 and 7 after whole-unit upward rounding.

The factory commitment is two in ordinary mode and one when the registered canonical family-512 quote returns one.

The respirator quantity is dynamic and stock-capped; selection reserves oldest-first across the five real models without discounting shipment volume.

The inline and blocked cost keys show £pol_power, the pooled £GFX_archetype_gas_mask_equipment_medium sprite, and £civ_factory; the five breakdown sprites are registered in interface\cbrn_protection.gfx.

The requirement predicates retain the established CBRN program, non-human-country exclusion, positive stock, exact factory quote, PP affordability, donor-and-state cooldown, foreign-controlled, non-core emergency target, no competing protection project or external escrow, and positive current need.

Raw requirements are hidden behind the custom-cost and availability gates; the visible row spells out the major project result and its concrete costs.

## AI validity and route locks

Both definitions use the same decision score and the same own-core, allied-core, and trauma factors.

The sale ID uses the static AI PP hint of 1 while its actual quote varies; the payment-ready trigger remains authoritative for the 13 or 7 PP quote.

The country prefilter requires the CBRN program, real respirator stock, an eligible factory quote, and either a valid new target or an active reservation; the state trigger validates a startable target or the exact retained active variant.

The live sale route requires both the Black Friday active flag and the registered Event 026 source identifier; when the source is invalid, a new sale selection is not exposed.

No invalid country or state target was identified by source review; same-state concurrent reservations are blocked, while different donor/state deliveries follow the existing escrow ownership rules.

No direct national-focus decision unlock was found in the bounded search; the existing program-established flag remains the inherited gate and this factory-sale tranche adds no focus route.

## Localisation and tooltip coverage

The title, description, cost, blocked-cost, cost-tooltip, begin, complete, total-crate quote, PP quote, and model-breakdown keys are present in localisation\english\cbrn_occupation_l_english.yml.

Both IDs bind the same accepted public localisation keys, and the scripted factory and PP getters select the current quote before payment or the committed value while a project is active.

The icon families resolve in interface\cbrn_occupation.gfx and interface\cbrn_protection.gfx; no missing alias or literal resource label was found.

The shared tooltip’s unconditional Black Friday sentence is the only text clarity recommendation in this bounded feature.

## Cleanup and exploit risk

The factory variant flag and committed PP variable are cleared by cbrn_occupation_close_external_aid_reservation; the donor active-reservation count is decremented only when its counted receipt exists and is clamped at zero.

The exact model escrow refund is idempotent and returns stock to the stored donor; if the donor object is missing, the existing helper retains the active receipt instead of crediting another country.

Regular event targets are saved only to bridge nested selection and payment or completion and delivery work; the source does not introduce a persistent global target.

The PP transaction ID and sale-sequence receipt are cleared after successful settlement; a failed settlement retains the receipt for recovery under the existing Event 026 contract.

The 90-day state cooldown intentionally survives cancellation and spans both IDs, preventing ordinary-to-sale or sale-to-ordinary bypasses.

No free shipment, repeated completion credit, second PP charge, factory-price substitution, or equipment-farming loop was found in the bounded source path.

## References, artifacts, and validation

The accepted design references are docs\specs\chaos_warfare_system_specs\corrections\2026-10-03_protective_aid_native_factory_sale.md and docs\plans\026_black_friday_plans\2026-10-03_cbrn_protective_aid_pp_adapter.md.

The parent-supplied MCP artifact folder is docs\testing\2026-10-03_cbrn_protective_aid_factory_sale_mcp; it contains connection and tool-list records plus an inspect request, but no successful native decision scenario, cost-row render, or probability comparison result.

hoi4.reference_context returned no result after four approximately 31-second waits and was manually terminated; hoi4.source_lookup returned no result after an initial 11-second wait and two approximately 31-second waits and was manually terminated.

The local offline wiki, installed documentation, vanilla decision file, and existing Chaos Redux variant were read directly to preserve source coverage despite those two stalled routes.

The offline Decision modding page at paradox_wiki\Decision modding - Hearts of Iron 4 Wiki.md:280-365 covers native reenabling, custom costs, selected timers, cancellation, and AI; revision and SHA-256 7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162.

The installed common\decisions\_documentation.md:1-46 documents per-frame visible and available checks and daily target-root and target checks; SHA-256 5e7e686b5582f32c38d898d805e17171e88f3bfeee4a030deb1884f9726de019.

The offline Data structures page at lines 120-125 and 437-442 covers targeted flags and temporary-output boundaries; SHA-256 62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4.

The offline AI modding page at lines 26-36 distinguishes ai_will_do scores and their external factors; SHA-256 917cd261f7da51fe4d8687c5d7663e768a09c5c101ac130ce646bc64637aa818.

The offline Modifiers page line 686 and installed modifiers_documentation.md lines 2202-2205 define civilian_factory_use; the installed trigger documentation lines 6757-6764 defines num_of_civilian_factories_available_for_projects.

The installed vanilla common\decisions\_exiled_governments_decisions.txt:244-292 provides a targeted timed custom-cost and hidden selection-time payment precedent; the in-mod cbrn_sponsor_decontamination_mission and cbrn_sponsor_decontamination_mission_sale at common\decisions\cbrn_diplomacy_decisions.txt:178-338 provide the closest two-variant shared-mode precedent.

The source review covered common\decisions\cbrn_occupation_decisions.txt:91-222; common\scripted_triggers\cbrn_protective_aid_decision_triggers.txt:5-132; common\scripted_effects\cbrn_protective_aid_decision_effects.txt:5-103; common\scripted_effects\cbrn_occupation_effects.txt:68-98; common\scripted_triggers\cbrn_occupation_triggers.txt:210-236 and 303-330; common\script_constants\cbrn_occupation_constants.txt:52-79; common\scripted_localisation\cbrn_occupation_value_localisation.txt:59-78; common\scripted_localisation\cbrn_protection_cost_scripted_localisation.txt:33-65; localisation\english\cbrn_occupation_l_english.yml:15-24; the existing escrow and refund helpers in common\scripted_effects\cbrn_protection_effects.txt:1265-1474; and the existing Event 026 PP receipt owner.

No gameplay or localisation file was edited, no tests were run, no game was launched, and no changes were staged or committed.

Skills read and applied: chaos-redux-decisions-missions, chaos-redux-events for the Event 026 sale-source integration, and chaos-redux-subagents for the bounded handoff.

The scripted-GUI layout skill was not invoked for implementation because the feature owns no scripted GUI definition or layout change; native decision cost-row rendering remains an evidence gap as recorded above.

No skill was created or updated.

Meaningful source validation consisted of tracing the matching decision IDs through quote, eligibility, selection, cancellation, completion, settlement, cost localisation, and sprite definitions, plus comparing the recorded before-source identity against the accepted current-source correction.

Skipped validation: native callback ordering, actual modifier release, rendered decision-list density and cost fit, cross-variant timer behavior, and AI score comparison require completed HOI4 scenario artifacts; no full target fixture was available, and the parent-assigned probability specialist was still in progress.

No dedicated scripted GUI is attached to this feature; the native decision-list cost row still needs a valid actor/state scenario before a matching rendered review can establish its fit.

The only file written by this auditor is docs\plans\chaos_warfare_system_plans\subagent_handoffs\2026-10-03_protective_aid_factory_decision_audit.md.

No plan handoff was created; the remaining work is the bounded native decision, rendered-row, probability, and documentation reconciliation described above.
