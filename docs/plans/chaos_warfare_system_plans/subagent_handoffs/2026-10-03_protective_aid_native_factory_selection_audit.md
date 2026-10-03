# Protective aid native factory selection audit

Date: 2026-10-03.

Disposition: The parent applied the bounded protective-aid correction and its occupied-population counterpart, and this audit confirms the focused source diffs; native selection ordering remains unresolved pending engine evidence.

Acceptance basis: The parent assignment records that the user approved the CBRN overhaul and selection-time mask reservation with refund, and it authorizes this specific guard correction.

## Severity-sorted findings

1. **High, conditionally resolved in the parent edit:** `cbrn_deploy_protective_aid` previously re-ran `cbrn_occupation_country_can_supply_external_protective_aid` from its `complete_effect`. That trigger includes the two-free-factory threshold, so if native timed-decision selection commits the `civilian_factory_use` modifier before `complete_effect`, a player who passed availability and selected the lawful cost could receive no mask reservation, Political Power debit, or registered delivery work, after which the native timer can cancel for lack of a reservation. The parent source now uses `cbrn_occupation_country_can_continue_external_protective_aid` and `cbrn_country_has_any_mask_stock` in that post-click guard.
2. **High, conditionally resolved in the parent edit:** `cbrn_supply_occupied_population` had the same pattern. Its two-factory modifier is checked by `cbrn_country_can_start_occupied_mask_reservation`, and `cbrn_begin_occupied_distribution_program` re-ran that full predicate from selection-time code. The parent added `cbrn_country_can_pay_occupied_mask_reservation` for the shared live non-factory checks and positive quote, kept the factory gate in the start predicate, and changed the selection effect to use the shared predicate with existence and non-capitulation checks.

## Protective-aid source trace

`common/decisions/cbrn_occupation_decisions.txt:89-217` owns `cbrn_deploy_protective_aid`, a state-targeted timed decision. Its two-factory modifier, duration, and cooldown remain unchanged. `available` and `custom_cost_trigger` still use `cbrn_occupation_external_aid_payment_ready`, which keeps the pre-click affordability check.

`common/scripted_triggers/cbrn_occupation_triggers.txt:208-229` defines the original supply predicate with the program flag, nonhuman exclusion, positive mask stock, and free-factory threshold. The continuation predicate retains country existence, nonhuman exclusion, non-capitulation, and the program flag. The new explicit stock predicate retains the positive-stock gate after the pre-click factory check is omitted.

The complete effect still requires the selected state to pass `cbrn_occupation_state_can_receive_external_protective_aid`, calculates a fresh `cbrn_quote_external_state_mask_reservation`, and requires a positive quote. `common/scripted_triggers/cbrn_protection_triggers.txt:33-35,530-548,575-585` shows that the quote is capped against the donor's live stock across the five supported mask models.

`common/scripted_effects/cbrn_protection_effects.txt:1265-1357` subtracts the requested model counts from the donor and records the model-specific receipt and donor on the selected state. The effect rejects an already-active receipt for that reservation kind. The payment call follows only after `cbrn_mask_escrow_completed` is positive, and the existing zero-payment branch returns the reservation through `cbrn_refund_external_state_mask_reservation`.

`common/scripted_effects/cbrn_protection_effects.txt:1421-1481` refunds the stored model counts to the stored donor, refreshes the donor snapshot, and clears the receipt and active flag. If the donor no longer exists, the helper retains the active receipt and marks the refund blocked rather than crediting another country.

`common/scripted_effects/026_black_friday_effects.txt:4132-4184,4189-4235` owns the PP fee payment and receipt settlement. Successful expiry closes the counted reservation, clears the active project flag, runs delivery, and settles the PP receipt. Cancellation closes the count, refunds the equipment, clears the project flag, and settles the unsuccessful receipt. These paths remain untouched by the guard correction.

## Neighboring occupied-population follow-up

`common/decisions/cbrn_protection_decisions.txt:369-414` keeps `cbrn_supply_occupied_population` at a two-factory native modifier and calls `cbrn_begin_occupied_distribution_program` from `complete_effect`. `common/scripted_triggers/cbrn_protection_triggers.txt:607-622` shows the current split: the full start predicate keeps the free-factory threshold and delegates to a shared predicate with live emergency and work requirements, active-program guard, PP affordability, and a positive national mask quote. `common/scripted_effects/cbrn_protection_decision_effects.txt:246-275` uses the shared predicate with existence and non-capitulation checks before it reserves masks and debits PP.

The applied family split is source-consistent: `available` and `custom_cost_trigger` still call the complete start predicate, which adds the same factory threshold before delegating to the shared non-factory predicate. The selection effect calls the shared predicate with existence and non-capitulation checks, and it retains emergency, work, active-program, PP, and positive quote requirements. The native factory price and timer remain unchanged.

## Lifecycle, cognitive load, costs, and AI

The protective-aid action remains one state-targeted timed decision owned by the donor country, with the selected recipient state in `FROM`, duration `constant:cbrn_occupation_timing.protective_aid_days`, a positive delivery proof on completion, and reservation refund on cancellation. The state receipt prevents a second reservation of the same kind, while the donor-side active-reservation count is closed on completion and cancellation. The broader category action count was outside this bounded audit.

The displayed decision cost has three resource types: Political Power spent, respirator equipment reserved, and civilian factories committed. `localisation/english/cbrn_occupation_l_english.yml:19-22` uses the `pol_power`, `GFX_archetype_gas_mask_equipment_medium`, and `civ_factory` texticons for both normal and blocked cost rows. The mask-model breakdown and refund behavior are explained separately in the cost tooltip. The four-type budget and spendable texticon requirements are satisfied by the inspected row.

The inspected target and owner guards align with an external aid transfer. AI weight values and target prioritization are unchanged and were not probability-audited in this narrow source-order task. No localisation changes were made.

## References and validation limits

The offline `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md:337-356` section describes `complete_effect` as selection-time setup for a decision timer and `modifier` as active during the timer. The parent supplied wiki revision `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162`. Installed documentation at `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\decisions\_documentation.md:1-46` provides the decision trigger-scope reference; the parent supplied revision `5e7e686b5582f32c38d898d805e17171e88f3bfeee4a030deb1884f9726de019`. Those sections do not prove the engine's exact ordering of factory reservation and `complete_effect` execution.

The parent reports that a no-scenario `hoi4.decision_inspect` request was rejected by live validation and the later narrow single-ID requests returned no result during bounded waits. The parent also reports that no native ordering or accepted MCP scenario result is available. Its pre-edit source snapshot is under `docs/testing/2026-10-03_cbrn_aid_native_factory_before/`. This audit did not repeat the MCP request, launch HOI4, run gameplay tests, or claim engine-order proof.

## Handoff

This subagent changed only `docs/plans/chaos_warfare_system_plans/subagent_handoffs/2026-10-03_protective_aid_native_factory_selection_audit.md`. The parent owns the source edits in `common/decisions/cbrn_occupation_decisions.txt`, `common/scripted_triggers/cbrn_protection_triggers.txt`, and `common/scripted_effects/cbrn_protection_decision_effects.txt`. The changed gameplay identifiers are decision `cbrn_deploy_protective_aid`, helper trigger `cbrn_country_can_pay_occupied_mask_reservation`, and call site `cbrn_begin_occupied_distribution_program`; no gameplay, mission, AI, GUI, or localisation identifiers were changed by this subagent.

Before the parent edits, both selection paths could recheck factory availability after a lawful pre-click check. After the edits, protective aid checks continuation eligibility and any remaining mask stock, then retains its target check, fresh positive stock-capped quote, model escrow, PP fee, reservation registration, timed delivery, refund, settlement, and existing AI weights. Occupied distribution retains the full factory threshold at selection eligibility and uses the shared non-factory check when the click effect starts reservations.

Meaningful validation consisted of reviewing the focused three-file source diff and tracing the decision gates, helper definitions, escrow and refund paths, payment receipt, adjacent occupied-population path, relevant offline wiki excerpt, installed decision documentation, and existing timed-factory precedents in source. The parent reports that source reconstruction matched both intended condition splits and restored the original factory threshold and selection limits. No gameplay source mutation or task-specific runtime test was performed by this subagent. The unresolved limits are native factory-selection ordering and the parent-owned MCP scenario query.
