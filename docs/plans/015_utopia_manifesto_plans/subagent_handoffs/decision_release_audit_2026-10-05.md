# Event 015 decision release audit — 2026-10-05

Disposition: the scoped decision, mission, payment, and owned-localisation patches are implemented. The parent-owned survey-cleanup line has also been added. The separate probability and visual evidence gates remain open. No commit was created.

## Acceptance basis and scope

The parent authorized the four military-growth fee reductions, the seven over-budget decision bundles, and the closed-policy Stability-fee removal. The accepted design keeps all formation resource charges and caps, preserves the case-integrity and local-support pressure effects of issuing an ultimatum, and preserves the Closed Order consequences. It removes only the named redundant spendable fees and redundant Auxiliary transfer types.

I changed the Event 015 decision surface and the parent-authorized closed-policy affordability/payment files. I did not change AI weights, focus AI values, or unrelated gameplay files. The parent owns `common/scripted_effects/015_utopia_manifesto_effects.txt`; its decision-runtime cleanup removes the survey mission and clears both the active-survey and first-survey pending flags.

## Changed files and behavior

- `common/decisions/015_utopia_manifesto_decisions.txt`: separated the first-survey early-completion path from paid recounts; reduced the seven named cost bundles; removed the four native Political Power formation fees; corrected the Auxiliary final effect guard so every recheck is inside `if.limit` before payment; retained the existing formation payments, timing, caps, failure flags, and outcome effects.
- `common/scripted_effects/015_utopia_manifesto_decision_effects.txt`: clears `utopia_manifesto_foundation_survey_completion_pending` on survey success and failure. The existing cleanup of `utopia_manifesto_penal_works_report_civilian_loss` is retained.
- Parent-owned `common/scripted_effects/015_utopia_manifesto_effects.txt`: the parent added the pending-flag clear next to survey-mission and `utopia_manifesto_survey_active` cleanup in `utopia_manifesto_clear_decision_runtime`.
- `common/scripted_triggers/015_utopia_manifesto_triggers.txt`: `utopia_manifesto_can_pay_auxiliary_contract` gates the dynamic foundation formation costs plus the full Support Equipment total for the gift.
- `common/scripted_triggers/015_utopia_manifesto_evolution_consumption_triggers.txt` and `common/scripted_effects/015_utopia_manifesto_evolution_consumption_effects.txt`: remove the upfront Stability fee from the Closed Order profile and keep Political Power, Infantry Equipment, Support Equipment, and Command Power.
- `localisation/english/015_utopia_manifesto_decision_completion_l_english.yml`: adds the first-survey mission tooltip and four matching growth cost key families; updates four growth decision descriptions, effects, requirements, and mission timing/cost wording; completes the G3 copy pass in this owned file. The Auxiliary gift amount calls the shared scripted getter so its displayed number comes from the payment constant.
- `common/scripted_localisation/015_utopia_manifesto_scripted_localisation.txt` and `localisation/english/015_utopia_manifesto_l_english.yml`: add the narrow `GetUtopiaManifestoAuxiliarySupportGift` getter and its numeric display key for the fixed Support Equipment transfer.

The four growth cost key families are `utopia_manifesto_cost_citizen_watch_formation`, `utopia_manifesto_cost_engineer_company_formation`, `utopia_manifesto_cost_auxiliary_contract`, and `utopia_manifesto_cost_post_formation_defense`. Each has base, `_blocked`, and `_tooltip` localisation. Every compact row shows at most three resource icons. The expanded tooltip identifies all spendable types and their timing.

## Cost and gate audit

These are source-level fee bundles. `small`, `medium`, `large`, and the foundation variables resolve through the existing dynamic price system, so the literal paid amount can vary with the current Black Friday quote and controlled-state count.

| Action | Before | After |
|---|---|---|
| `decision_utopia_issue_need_ultimatum` | Political Power large, Infantry Equipment medium, Command Power medium, Stability medium, War Support small | Political Power large, Infantry Equipment medium, Command Power medium |
| `decision_utopia_enforce_need_case` | Political Power major, Infantry Equipment large, Support Equipment large, Command Power large, Stability medium, War Support medium | Political Power major, Infantry Equipment large, Support Equipment large, Command Power large |
| `decision_utopia_impose_assigned_administration` | Political Power medium, Manpower medium, Infantry Equipment medium, Support Equipment medium, Stability medium | Political Power medium, Manpower medium, Infantry Equipment medium, Support Equipment medium |
| `decision_utopia_begin_long_integration` | Political Power major, Manpower large, Support Equipment large, Trains large, Motorized Equipment large | Political Power major, Manpower large, Support Equipment large, Trains large |
| `decision_utopia_close_the_gates` | Political Power medium, Manpower medium, Infantry Equipment large, Support Equipment large, Army XP medium, Stability small | Political Power medium, Infantry Equipment large, Support Equipment large, Army XP medium |
| `decision_utopia_enforce_closed_order` | Political Power large, Infantry Equipment large, Support Equipment medium, Command Power medium, Stability small | Political Power large, Infantry Equipment large, Support Equipment medium, Command Power medium |
| `decision_utopia_found_refugee_municipality` | Political Power large, Manpower large, Support Equipment large, Trains medium, Motorized Equipment medium | Political Power large, Manpower large, Support Equipment large, Trains medium |

The refugee municipality still requires the Common Reserve floor; it no longer spends Reserve. The ultimatum still applies its case-integrity and local-support consequences through `utopia_manifesto_issue_case_ultimatum`. Enforce Case still creates the case war goal through its existing helper. Assignment, long integration, island-gate selection, and Closed Order effects are unchanged apart from the removed charges.

| Formation action | Before | After and timing |
|---|---|---|
| `decision_utopia_raise_a_citizen_watch` | Native Political Power small, its purchase-credit callback, and four live foundation formation costs at mission completion | Four live foundation costs only: Manpower, Infantry Equipment, Support Equipment, and Army XP. No fee is charged when training starts. |
| `decision_utopia_form_engineer_companies` | Native Political Power medium, Motorized Equipment medium at start, and four live foundation formation costs at mission completion | Four live foundation costs only. No fee is charged when training starts. |
| `decision_utopia_hire_auxiliary_contracts` | Native Political Power large, four live foundation formation costs, Support Equipment 50 transfer, Motorized Equipment 50 transfer, and Convoys medium | Four live foundation formation costs plus Support Equipment 50 transfer. The Support affordability gate and compact row use one combined amount: live foundation Support plus the transferred 50. The final guard also rechecks growth capacity, a controlled deployment state, and target peace before paying. |
| `decision_utopia_reinforce_post_formation_defense` | Native Political Power medium plus four live foundation formation costs | Four live foundation formation costs only, paid immediately. |

The four formation actions now have at most four distinct spendable types. The Auxiliary transfer is the same Support Equipment type as the formation payment, so the final distinct-type count remains four. The three compact icon slots show Manpower, Infantry Equipment, and Support Equipment; the full hover text includes Army XP. The transfer amount is read from `constant:utopia_manifesto_decision_cost.support_medium` through the shared scripted getter rather than duplicated as a number in player text. Watch and Engineer tooltips state that the stock must be available when training starts, no fee is then paid, and the full live cost is charged only if formation succeeds at the deadline.

Closed-policy consumers were searched across the repository. The affordability trigger is used by `decision_utopia_enforce_closed_order`. The shared action-payment effect serves the evolution decision family, and its Closed Order branch now debits exactly Infantry Equipment large, Support Equipment medium, and Command Power medium in addition to the decision's native Political Power large. No event directly calls the closed-cost trigger or action-payment effect.

The static affordability idiom is inclusive at equality: the gate negates a `< cost` test, so a stockpile equal to the displayed threshold passes. The standard cost trigger, displayed quote, and payment variable share the same price-level identifiers. Auxiliary formation Support uses the live foundation quote, then adds the fixed 50 Support transfer to the affordability/display total; the formation helper pays the live fee, then the existing prepared-cost helper pays the gift before the recipient stockpile transfer. Engine boundary fixtures are still required for just-below, equal, and just-above values under ordinary and Black Friday quotes.

## Survey lifecycle and mission quality

The first paid `decision_utopia_count_houses_and_hands` spends Political Power small, Trains small, and Motorized Equipment small, then sets `utopia_manifesto_foundation_survey_completion_pending`. The shared `mission_utopia_count_houses_and_hands` can complete early only when that flag and the completed-foundation flag are both present. The paid `decision_utopia_recount_the_country` spends Political Power medium, Trains medium, and Motorized Equipment medium, but does not set the pending flag, so a completed first-survey flag no longer completes each recount immediately. Recounts still run to their mission deadline and call `utopia_manifesto_complete_national_survey`, which refreshes all survey values. Neither path charges an additional completion fee.

Survey success, failure, and route-wide runtime cleanup clear the pending flag. The existing `utopia_manifesto_first_survey_event_seen` gate means the first-report event fires once; the shores follow-up uses its own scheduled/seen guards. Thus recounts refresh measurements without farming the first report or repeating the follow-up popup. The parent-added clear in `utopia_manifesto_clear_decision_runtime` covers the path that removes the survey mission and clears `utopia_manifesto_survey_active`.

The shared survey mission is owned by the country, appears in `utopia_manifesto_ledger_category`, and has no state-region target. Its duration is the prepared `utopia_manifesto_survey_days` value. It completes early on the first survey's existing foundation condition; otherwise timeout completes the survey. Cancellation on loss of Common Provision or capital control fails the survey and applies its existing Need/Concord consequence. A single `utopia_manifesto_survey_active` flag blocks overlapping initial surveys and recounts. The pending flag distinguishes the first survey lifecycle from later paid refreshes.

Citizen Watch and Engineer missions each use the existing dynamic defense duration, shown as 90–240 days, and retain their success, understrength, and cancellation outcomes. Costs are paid only when their completion helpers can afford and create the formation. Auxiliary hiring remains one-shot through `utopia_manifesto_auxiliary_contract_ever_hired`, and post-formation Guard reinforcement remains one-shot through `utopia_manifesto_post_formation_defense_reinforced`.

## Player-facing clarity and category notes

The affected ordinary decisions retain their existing category and phase lifecycle. The post-formation Guard remains hidden until the Commonwealth is formed. Citizen Watch and Engineer retain their focus/route gates. Auxiliary hiring still requires an eligible neighbor and an available formation slot. I made no new category or GUI surface and changed no category button count.

The relevant decision values now communicate what they buy and when payment occurs. The deferred Watch and Engineer fees, immediate Guard fee, and combined Auxiliary Support transfer are all named in their detail text. Player-facing copy in the owned completion file contains no raw implementation identifiers, `Ledger` or similar audit terms, sentence semicolons, em dashes, or replacement characters. The file retains its UTF-8 BOM. Four custom-cost key families each have base, blocked, and tooltip coverage with texticons.

I did not make a fresh visual claim about cost-row clipping or category density. The current `utopia_manifesto_ledger_container` GUI inspect and baseline render requests were attempted read-only and timed out; the dedicated GUI worker also reported 600-second timeouts. No current visual artifact or comparison exists, so source text fit and live click-region behavior remain unverified.

## AI, exploit risk, and remaining issues

No AI numeric weights changed. The four growth actions remain capacity-limited; Auxiliary has a one-contract lifetime flag and pays its complete stock requirement before transfer; the survey and formation missions retain their existing success/failure and cleanup effects. No new repeatable resource refund or unit-creation path was added.

Source route locks remain intact: Watch and Engineer require their focus or route unlock, Auxiliary requires an eligible neighboring contractor, and post-formation Guard requires an established Commonwealth. The Auxiliary target is checked for peace both at availability and immediately before dispatch. I did not change target selection or any AI numeric weights. The category’s total simultaneous action count and cross-category mission count were not scenario-evaluated, so this audit does not claim they meet a numeric density limit; this patch adds no category or mission.

Remaining issues, sorted by severity:

1. Medium — current GUI inspect/render calls timed out, so cost-row clipping, panel fit, and visible cost states have no current production-render evidence.
2. Medium — the named Closed Order `decision_inspect` and the parent’s mandatory same-scenario probability compare have no returned artifact yet. AI eligibility changes from removing fees remain unquantified, though source AI weights are unchanged.
3. Medium — just-below/equal/above fee, Black Friday quote, mission timing, and exact debit fixtures still require the user’s live-game validation.

The mandatory same-scenario probability baseline/compare is delegated to the parent’s read-only probability auditor. The before snapshots are under `docs/plans/015_utopia_manifesto_plans/probability_snapshots/unit_growth_pre_fee_reduction_2026-10-05/` and `closed_order_pre_stability_removal_2026-10-05/`. The unit-growth decision and trigger source snapshots were captured immediately before the four fee reductions; no weight or score code changed afterward. Current decision hash before the Auxiliary guard-context correction was `0FE94F10F6839F58E7AC006DCF2AE809AD42AE78BF0EAEF414B1E8492410D822`; recompute it after the correction for the compare result.

`hoi4.decision_inspect` for `decision_utopia_enforce_closed_order`, USA, scenario `current-usa-baseline`, remained pending beyond 60 seconds and returned no artifact. The parent instructed this worker not to retry GUI/MCP routes. A prior survey-trigger `hoi4.script_validate` result was `valid=true` for its native trigger scopes; the Closed Order trigger check returned partial validation with variable/native argument blocks unchecked. These checks do not prove engine behavior. The current decision source hash after the Auxiliary guard correction is `BE3FD76DEE2516FE9241BA47B1F8D52942C763800C868BE8CACA24A742A9ED1F`; the current completion-localisation hash after the start/deadline clarity pass is `BB50DEA68F39BD78B8601685907AD3D317DE2F62227C76F171E7F65483A26D76`. The parent-owned runtime-effects hash after its survey pending-flag cleanup is `0E05DAFECBBF2364716FEBB1C19FD6BE069F201C43ABE9320C53623B367F1EB2`. The getter file hash is `DF25359721AFF010548106C6936351D39A3425FB114B3016E3AB0695603F279E`, and the other Event 015 localisation file hash is `33A4F090B3ACA01AA8524F7CD1D58C1AA51E86876401C135C758FBDE8F110E81`.

The user owns live-game validation. Setup fixtures should test each retained fee at just below, exactly equal to, and just above the current quote, including ordinary and Black Friday-priced scenarios. The Auxiliary fixture must separately test each foundation resource and total Support at those boundaries, then confirm exactly one formation debit, one 50 Support transfer, and no Motorized/Convoy transfer. Watch/Engineer fixtures should verify no charge at mission start, a single four-resource debit on successful deadline completion, no debit on cancellation or insufficient completion stock, and no immediate recount completion. The Guard fixture should confirm one immediate four-resource debit and one formation.

## Source and precedent evidence

- Offline Decision modding wiki, `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md`, revision `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162`, lines 284–336.
- Installed decision documentation, `common/decisions/_documentation.md`, revision `5e7e686b5582f32c38d898d805e17171e88f3bfeee4a030deb1884f9726de019`, lines 1–46.
- Installed effects documentation, `effects_documentation.md`, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`, `add_stability` lines 2173–2181; installed dynamic-variable documentation revision `538525747f0c285062c9ce8db14b4e07c3cf6bac1013115fa4f57291cb4ebdda`, `has_stability` lines 435–438.
- Installed trigger documentation revision `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29`, `has_country_flag` lines 3624–3643, `has_equipment` lines 3835–3843, and `set_temp_variable` lines 7482–7493.
- Offline Localisation wiki snapshot, captured 2026-09-19, `paradox_wiki/Localisation - Hearts of Iron 4 Wiki.md`, SHA-256 `1A8F72362A34B4BB653186746B9FAE0B98E463205CB02F12CCF2C3D9CCD3A064`, lines 656–791, documents `defined_text` trigger scopes and temporary-variable calculation inside a scripted-localisation trigger.
- Installed scripted-localisation precedent, `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/scripted_localisation/00_scripted_localisation.txt`, SHA-256 `6F490E33736F4DC31568ADD5753A1AFDEF916F3993804FEBFBBE6D1583827587`, lines 1–9, documents `defined_text`, candidate `text` entries, and trigger-based selection.
- Vanilla decision precedent `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/decisions/AFG.txt`, SHA-256 `DABC91C3F7FB1810D64D91D07147E827068D42540326CE10554A0752EE48D7A7`, lines 480–500, uses a custom Command Power gate with its matching payment.

The reference routes returned these targeted sources. Direct `reference_read` calls and the vanilla `source_lookup` attempt remained pending, so the cited sections were read from their local files. No web wiki was used.
