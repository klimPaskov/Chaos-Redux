# Protective Aid native factory selection repair

Disposition: implemented in source; native decision execution remains unverified.

The accepted [selection-guard correction](../../specs/chaos_warfare_system_specs/corrections/2026-10-03_protective_aid_native_factory_selection.md) changes the country check inside `cbrn_deploy_protective_aid.complete_effect` in `common/decisions/cbrn_occupation_decisions.txt` and the corresponding occupied-population helper checks.
The pre-click payment predicate still requires two free civilian factories, the program, stock, Political Power, and an eligible selected state.
The selection effect checks the existing continuation predicate, real mask stock, the current fee, and the selected-state quote without asking for two additional free factories.
The native two-factory commitment, 21-day timer, exact-model escrow, registered donor, completion delivery, unused-crate refunds, and delayed PP receipt settlement retain their existing owners.
No public label, cost row, icon, or explanation changes, because their existing prices and consequences are unchanged.

The [before-source bundle](../../testing/2026-10-03_cbrn_aid_native_factory_before/) contains the source and HEAD revision saved before the edit.
The [source-contract model](../../testing/2026-10-03_cbrn_aid_native_factory_before/selection_source_contract.json) confirms that replacing the new guard by the old guard reconstructs the entire decision file exactly.
At one free factory the unchanged pre-click gate fails; at two or three it passes given the other requirements.
If native selection commits two factories first, the old post-click factory gate fails with zero or one left free, while the corrected country/stock check permits the existing paid shipment path.
If the native commitment occurs after the selection effect, the same corrected check is valid.
Missing stock, a withdrawn program, an invalid country, or capitulation still rejects selection-time execution.
These are declared source cases, not engine-observed timer ordering or payments.

The neighboring `cbrn_supply_occupied_population` decision uses the same two-factory native modifier and called the full start gate from `cbrn_begin_occupied_distribution_program` after selection.
Its source correction factors every original non-factory condition into `cbrn_country_can_pay_occupied_mask_reservation`, keeps the two-factory check in the full start predicate, and checks existence/non-capitulation in the selection effect.
The 30-day occupied timer, Political Power price, eligible-state loop, positive aggregate reservation rule, per-model escrow, target markers, and completion/refund body remain unchanged.
The [helper contract](../../../common/scripted_effects/cbrn_scripted_effects.md) records scope, inputs, scratch output, side effects, and the allowed native caller pattern.
Neither action's full pre-click gate or willingness changes in eligibility or pricing.

## Reference and MCP evidence

Installed `common/decisions/_documentation.md:1â€“46`, revision `5e7e686b5582f32c38d898d805e17171e88f3bfeee4a030deb1884f9726de019`, distinguishes pre-click availability and actor/target scopes.
Offline `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md:337â€“356`, revision `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162`, describes selection effects, native timed modifiers, completion, and cancellation.
Vanilla `common/decisions/_exiled_governments_decisions.txt:244â€“292` supplies the targeted selection-time custom-payment and native timed-modifier shape.
The existing Forensic Publication transaction in `common/scripted_effects/026_black_friday_effects.txt` checks materials after selection separately from the pre-click factory requirement.
The parent read these sections and the exact current predicates in `common/scripted_triggers/cbrn_occupation_triggers.txt:210â€“229` before editing.

The live `hoi4.decision_inspect` schema was verified.
An initial `mode = inspect` request without scenarios was rejected immediately with the requirement for declared scenarios.
The corrected `aid_exact_two_factories_source_probe` declared ENG, 14 August 1939, 25 Political Power, two free factories, one basic crate, and a typed FROM state 60; the target's further facts were deliberately unresolved and it was not a complete acceptance fixture.
That request returned no result during bounded waits and was terminated before the source edit.
A narrower single-ID inventory retry also returned no result during bounded waits and was terminated.
Both used the known workspace identifier and `refresh = false`.
No artifact, source revision, helper coverage, scenario outcome, or native visual proof was returned by these calls.
The mandatory route gap is retained; local source cases do not replace MCP or live execution evidence.

After the family source edits, a post-change inspect repeated the same `aid_exact_two_factories_source_probe` request, actor, date, country facts, and typed FROM binding.
It also returned no result during bounded waits and was terminated.
There is therefore no matching before/after artifact or supported native scenario outcome, and no numeric AI comparison is claimed.

## Remaining acceptance

Native evidence must confirm a valid exact-two-factory click, its paid model reservation, normal completion, cancellation, target loss, stock loss, and unchanged refund/receipt behavior.
The [independent family source audit](subagent_handoffs/2026-10-03_protective_aid_native_factory_selection_audit.md) traces both corrected paths, exact-model escrow/refunds, current PP receipts, and existing timed-factory precedents without confirming native ordering.
The one-factory Event 026 sale commitment is a separate unresolved tranche and is not claimed by this guard repair.
The overall CBRN overhaul remains incomplete.
