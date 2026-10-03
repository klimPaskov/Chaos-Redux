# CBRN Occupied Distribution and Export Decision Audit

**Audit disposition:** The bounded source implementation is structurally coherent after the latest parent fixes; no ordinary-path source defect remains in the reviewed export or occupied transaction paths. The source suite and final occupied/export probability comparisons are complete but partial; native consumer evidence and an exceptional-recovery owner remain open.

**Scope:** Existing decision IDs cbrn_export_protective_equipment, cbrn_supply_occupied_population, and cbrn_supply_occupied_population_sale; their transaction helpers, shared state-model escrow hooks, costs, tooltips, and lifecycle callbacks. The accepted correction is docs/specs/chaos_warfare_system_specs/corrections/2026-10-03_occupied_export_sale_transactions.md. Parent-owned source edits were read only. This reviewer changed only this handoff.

**Acceptance basis:** The user accepted the CBRN/Event 026 continuation, full concrete-model shipment escrow/refund, and the recommended continuation. The parent identifies the dated correction as the accepted native export/occupied sale transaction contract.

## Findings by severity

**Medium, exceptional recovery has no in-scope consumer.** A measured stockpile mismatch or failed native refund deliberately retains exact state receipt evidence, sets cbrn_occupied_transaction_recovery_pending, and blocks another purchase/reservation. The CBRN common-source search found this flag being set and used as a start guard, but no consumer that resolves and clears it. This is fail-closed and does not fabricate payment reversal, delivered protection, or achievement credit; it leaves exceptional recovery dependent on a parent-level or manual recovery process. Carry that dependency into integration rather than treating a quarantined receipt as settled.

**Validation blocker, native row and callback behavior are unverified here.** The native decision row has not been rendered in this audit. The exact engine tick for cancel callbacks, release of native factory commitment, measured equipment changes, and save persistence remain pending native consumer evidence. No source-only result is treated as proof of those behaviors.

No high-severity source defect was confirmed in the final reviewed paths.

## Decision lifecycle and transaction behavior

The export action is one targeted native decision over global.enabled_countries_list. ROOT is the paying donor and FROM is the recipient. Start and custom-cost visibility use cbrn_export_transaction_can_start; the target can remain visible for its owned receipt even after the recipient or current price source becomes ineligible. Start freezes recipient, fee, source, sale sequence, and the exact five-model allocation before payment. Completion measures actual model transfer and recipient gain; the 500-unit aid outcome is awarded only with complete measured delivery. Cancellation returns only the exact held original models and keeps the accepted service fee spent.

The occupied ordinary and sale variants are the same 30-day program with 90-day country re-enable timing. Their current purchase quote selects one visible variant; the active committed variant keeps its matching native decision visible through the timer and prevents a competing start. Both callbacks delegate to the shared transaction helper. Start reserves measured model stock by state, pays the frozen political fee only after a positive aggregate reservation, and publishes active receipt fields only after payment is recorded. Completion checks each owned state receipt, ROOT control, non-core status, current positive need, emergency context, and reserve availability. States with no remaining eligible need return unused models. Country-level success credit requires positive usable and consumed protection proof and successful settlement. Accepted cancellation keeps the fee spent and refunds unused original models.

The previously reported generic-project conflict is resolved in current source. cbrn_occupied_country_can_continue and cbrn_occupied_finish_selected_program use cbrn_occupied_state_can_complete_reserved_distribution, which tests the owned receipt and current issue conditions without the start-only generic project busy flag. cbrn_complete_occupied_state_distribution no longer clears that unrelated flag, and the occupied finish callback is its only executable caller.

The shared measured native escrow path now reads each concrete model stock before and after its debit or return, records exact native evidence on mismatch, and quarantines further operations after the first discrepancy. The occupied start preserves the quarantined target marker, refuses fee/publication while recovery is pending, and returns earlier valid state reservations when a later state or payment step rejects the start. The state-control-change callback clears the occupied target marker only after an unblocked refund; a blocked return retains its receipt for recovery. These are source-level controls; native stockpile API behavior still needs engine validation.

The five respirator models are one archetype-crate cost family, not five selectable fees. The decision displays the aggregate crate quote while the receipt records and returns the exact oldest-first model mix. This matches the accepted full-model escrow and refund contract.

There are no separate mission definitions in this bounded pair. The native decision timers serve as the 14-day export preparation and 30-day occupied program windows; cancel and remove callbacks are attached to the decision definitions.

## Costs, localisation, and clarity

| Decision surface | Spendable cost types | Visible cost texticons | Source behavior |
| --- | --- | --- | --- |
| cbrn_export_protective_equipment | Political power, one pooled respirator shipment, one assigned civilian factory | £pol_power, £GFX_archetype_gas_mask_equipment_medium, £civ_factory | Fee is 15 ordinary, 8 half-price, or 4 quarter-price; start requires at least 1,500 crates; exactly 500 models are reserved; 1 factory is committed. |
| cbrn_supply_occupied_population and _sale | Political power, one pooled state-program respirator quote, assigned civilian factories | £pol_power, £GFX_archetype_gas_mask_equipment_medium, £civ_factory | Ordinary program fee is 25/13/7 by source and uses 2 factories; sale variant uses 1 factory; model quote is based on current state need and the same source family. |

Each surface has three spendable types, within the four-type limit, and its inline row shows only those three icon/value pairs. Ordinary and sale occupied rows use the same icon layout; the sale amount is dynamically sourced. Availability and custom_cost_trigger use the same payment-ready helper, while the effect pays through the transaction receipt once, avoiding an ordinary native-plus-scripted double debit. The model archetype is one pooled displayed cost even though each concrete model is escrowed separately.

The current factory scripted-localisation getter returns ready-coloured keys for active ordinary/sale values and a red short key for a fresh invalid or insufficient one- or two-factory quote. It no longer applies an unconditional yellow wrapper. The export getter has matching ready/short behavior. Active fee, factory, and model rows read the committed transaction values rather than refreshing against a changed source.

Player-facing values have direct significance: political power pays service, the mask icon shows reserved physical stock, and the factory icon shows temporary capacity commitment. Export text explains the minimum reserve, shipment, destination, and cancellation return. Occupied text explains payment, reservation, factory commitment, unused-model return, program duration, coverage, and local outcome. The existing Event 026 campaign surface explains the sale context, and the decision row shows the exact active quote; no extra row or administrative action is warranted.

The English localisation file retains a UTF-8 BOM. A read-only byte check confirmed actual U+00A3 pound and U+00A7 section characters in the current YAML; scripted-localisation source selects local keys instead of embedding format characters.

## Category density and player interaction

The two occupied choices are mutually exclusive by the quoted factory variant. The export decision is target-specific, with one action per currently eligible recipient, which preserves the required recipient choice. No new category or scripted GUI was introduced.

The containing source file has 15 decision definitions. This audit is bounded to the three named IDs and does not certify the number of simultaneously visible actions across every existing CBRN decision or how the native category lays out target-array rows. Parent review should retain the wider-category visibility and render check as a separate integration item. No separate active mission count applies to these decisions.

## AI validity and route locks

Export targets must pass cbrn_target_can_receive_exported_masks; its source checks existence, non-self recipient, non-capitulation, diplomatic/humanitarian route eligibility, and recipient stock ceiling. The active-receipt path keeps the selected recipient addressable for completion/cancellation when a new start would no longer be valid. Occupied ordinary/sale selection requires the matching current quote; neither variant can be started while a country program or recovery lock is active. In-flight source expiry does not trigger a fresh quote, and country cooldown is shared across variants.

The ordinary and sale occupied AI willingness bodies are identical; the sale does not add a competing balance formula. The small ai_hint_pp_cost value is a native saving hint and does not replace the exact PP affordability/debit helpers. The separate probability handoff at docs/plans/chaos_warfare_system_plans/subagent_handoffs/2026-10-03_cbrn_occupied_export_probability/finalhandoff.md records the final matched occupied comparison against source revision d8354fd0dd5ce76637dccecce6bda771eb8a46d5f6a2562d3aff142f9774b383. That MCP pass is partial across 54 candidate rows and 27 scenarios, with 10 excluded rows, 66 unresolved items, and 44 unresolved candidate rows, and no diagnostics. The archived response is [occupied_export_occupied_final_compare.json](../../../testing/2026-10-03_cbrn_occupied_export_mcp/occupied_export_occupied_final_compare.json), indexed by [artifact_manifest.json](../../../testing/2026-10-03_cbrn_occupied_export_mcp/artifact_manifest.json). The final export comparison now also exists at source revision 4cd583f39aeb18de5eaa678e09f78663a8a8617f171e5bc286a1e435a0e2fc7e, with source hash 68d15e5e3099be35464584d03dcaeb1469a71ea3c3ecf424cc7b2e9c36a89f85 and the same 17-scenario hash 4f6b363804094a98d50736596b7cf3f5205f6f2ed0cb3b78ba741afcb9bef86b. It returned PROBABILITY_ANALYZED_PARTIAL, with 3 excluded rows, 14 unresolved candidate rows, 44 unresolved items, 17 coverage flags, and no diagnostics or blockers. Its archived response and compact entry are [occupied_export_export_final_compare.json](../../../testing/2026-10-03_cbrn_occupied_export_mcp/occupied_export_export_final_compare.json) and [compact_candidate_rows.json](../../../testing/2026-10-03_cbrn_occupied_export_mcp/compact_candidate_rows.json); the archive is indexed by [artifact_manifest.json](../../../testing/2026-10-03_cbrn_occupied_export_mcp/artifact_manifest.json). These completed comparisons remain partial: unresolved helper analysis prevents claims about full eligibility, candidate-pool completeness, or engine selection behavior. Do not infer a balance regression from unresolved rows or the earlier pre-fix compare.

## Cleanup and exploit review

The reviewed callbacks bind each receipt to its donor, recipient or state, transaction id, source, variant, and exact model rows. Export completion compares donor release and recipient gain before awarding complete-shipment outcomes; unsent or undelivered stock is not counted as delivered. Occupied completion consumes only state escrow and reports success only after positive delivery proof. Fee credit and settlement outputs are checked; a failed credit/refund retains keyed evidence and blocks duplicate settlement instead of claiming successful rollback.

The on_state_control_changed cleanup now checks the occupied refund result before clearing its target marker. Repeated finish/cancel paths are keyed or closed idempotently, and one successful native decision cannot switch from ordinary to sale mid-program. A native model mismatch or blocked return remains quarantined and blocks new starts until recovery is explicitly resolved; no alternate free-stock fallback or model substitution is present.

## Documentation and reference notes

The current scripted helper overview at common/scripted_effects/cbrn_scripted_effects.md lines 777-781 and 959-960 reflects the occupied receipt continuation and no longer claims that occupied completion owns the generic project flag.

Local Decision modding reference sections reviewed: paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md lines 305-356; installed game common/decisions/_documentation.md lines 12-35 (SHA-256 5e7e686b5582f32c38d898d805e17171e88f3bfeee4a030deb1884f9726de019). ROOT/FROM targeting reference: paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md lines 437-442. Scope reference: paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md lines 260-263. The vanilla targeted-decision precedent reviewed was Hearts of Iron IV/common/decisions/_generic_decisions.txt lines 272-298 (SHA-256 83cd276f8fd2c0c90470225c996d7afee7b8c08437289dd23d819a4a29edb187).

## Validation and remaining work

This was a read-only source audit. It manually cross-checked the decision start/finish/cancel wiring, transaction quote and callback paths, current state continuation predicate, failure refunds, receipt typing, localized cost keys, and shared measured-state escrow implementation. It confirmed the current YAML BOM and £/§ codepoints. No source tests were run by this reviewer.

The parent reports that the final actual-source suite completed with 46 checks and zero failures. This reviewer did not independently execute that suite. The probability handoff and archived outputs include the final occupied and export comparisons; both are partial, so their unresolved rows limit what can be concluded about AI eligibility or score movement.

No HOI4 MCP call was made by this reviewer because the parent owns the isolated live client and the probability auditor owns the weighted workflow. The final occupied probability result is cited through that auditor's handoff; there is no native decision-row render or full-game callback evidence in this audit. The user owns live-game validation; no game or logs were opened.

Recommended closeout is to verify the decision cost rows and native callback/factory release behavior in the user's live game, and to provide an explicit recovery owner for quarantined receipts before clearing recovery-pending state. Normal-path pricing and cancellation remain source-backed; exceptional quarantine must not be cleared without reconciling the retained stock evidence.

Skills used: chaos-redux-decisions-missions and chaos-redux-subagents. No skill was created or modified.
