# Event 026 CBRN Cover-up Decision Audit

Date: 2026-10-07.
Disposition: bounded decision audit complete, with recovery reachability and player-facing recovery wording still unresolved.
Scope: existing decisions cbrn_seal_state and cbrn_destroy_contaminated_records, their shared CBRN category, exact-source quote and affordability helpers, payment receipts, localised costs, AI weights, and recovery flow.
Authority: the parent's bounded read-only audit assignment and the subsequent instruction to assess the completion-tooltip mismatch.
This review made no production edits, ran no tests, and created no commit.
Event 026 remains default-disabled under the parent's b9e4e7540 instruction until the full original goal is accepted and complete.

## Findings ordered by severity

### 1. Blocking integration gap: recovery has no guaranteed owner invocation

The pending refund and settlement records are durable and the bounded queue preserves unvisited IDs, but the queue does not have a guaranteed payer-scoped caller when all targeted purchase actions are unavailable.

The only ordinary call to cbrn_occupation_recover_paid_coverups is in cbrn_occupation_execute_paid_coverup at common/scripted_effects/cbrn_occupation_effects.txt:947-956, which runs after a player or AI takes one of the two existing decisions.
The direct cbrn_occupation_recover_paid_coverup_receipt call in the same file is part of the original payment chain, not a later owner recovery hook.
Repository-wide caller search found no separate owner action or callback invoking the queue helper.

When the coverup outcome applies, the code records phase applied_settlement and clears that state's open receipt pointer before settlement acknowledgement.
If settlement then rejects, the state's response flags hide the original purchase decision and the refund preflight does not accept phase applied_settlement.
The payer can recover that receipt through another eligible paid-coverup click, but has no guaranteed recovery invocation if every state target is absent or fails the original route, control, responsibility, visibility, or response requirements.
The same access gap applies to a pending refund when its target loses the legacy route or control conditions.

Recommended parent action: call the existing queue helper from an existing bounded original-payer owner action or callback.
Keep the ordinary decision target and route requirements unchanged.
Do not add a world scan, guess the payer from a new controller, refund missing proof, or replay a completed outcome.
If no accepted payer-owned path exists, keep recovery integration marked blocked.

### 2. Blocking player-facing mismatch: recovery still advertises the completed coverup

Both decision complete_effect blocks always emit their normal outcome tooltip, at common/decisions/cbrn_occupation_decisions.txt:259-263 and 304-308.
During a valid pending-refund click, the cost row says Payment recovery and its detail says to retry the refund without making a new purchase.
The unconditional cbrn_seal_state_effect_tt and cbrn_destroy_contaminated_records_effect_tt still claim that the evidence will be suppressed and the normal state effects will occur.

This is a source-confirmed contradiction on the recovery decision surface.
The current 86-case source suite exercises the cost/detail getters but does not load the decision file or select either custom_effect_tooltip branch.

Recommended parent action: condition the two custom effect tooltip lines on the same validated refund preflight used by the cost getter.
Show recovery-only wording for an outstanding refund and retain the existing outcome wording for a fresh purchase.
This can be corrected without changing AI weights, target requirements, route gates, or cooldowns.

### 3. Immediate retry remains unproven because the native cooldown still applies

Both decisions retain days_re_enable = constant:cbrn_occupation_timing.coverup_reenable_days at common/decisions/cbrn_occupation_decisions.txt:241 and 286.
The current constant is 30 days at common/script_constants/cbrn_occupation_constants.txt:211.
The offline Decision modding section says days_re_enable delays a taken decision from reappearing.
The source test calls the scripted execute helper directly and does not run the native decision cooldown.

The zero-PP recovery predicate can pass while a valid refund receipt is open, but that does not prove the decision row can be selected immediately after a failed native click.
Treat immediate retry timing as unresolved until the actual decision surface is observed.
The receipt's recovery access still needs the owner path in finding 1 when no other eligible click exists.

### 4. AI hint and scenario behavior are unresolved

The source AI scores remain 20 for cbrn_seal_state and 10 for cbrn_destroy_contaminated_records.
Seal has a zero-weight factor for democratic governments or a closed first-use route.
Destroy has a zero-weight factor for a closed unrestricted-use route.
The destroy route helper checks the unrestricted CBRN route and high-chaos successor flags, but has no separate democracy condition.
Source alone does not establish whether that positive democracy case is invalid.

The native hints remain fixed at 40 and 60 PP, while the custom quote can be discounted below those values or scale above them with Condemnation.
The offline Decision modding section describes ai_hint_pp_cost as a constant amount the AI saves because it expects a custom cost.
That evidence concerns AI saving behavior and does not establish a separate human availability gate.
The scripted availability predicate uses the current quote and shared inclusive PP affordability.
Do not infer native AI affordability, timing, or exact-hint behavior from that source predicate.

The read-only probability route has useful inspect artifacts but no completed evaluation or sweep.
The narrow inspect artifact covers only the two explicitly scoped decisions, not the full category pool.
No normalized selection probability, effective scenario score, rank reversal, or AI pacing result is available.
No AI weight changed, so no probability_compare baseline was created or required.

Useful narrow inspect artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e00ab8066ae40e3039a296a07ca45a4513af5e194055f33586546f3358058cc9/23ca1b59e52f1c63ee9339f6acea3838ee21870d9f198d4a1282d8fe0fbc9d9f/probability-inspect-7551437660a6.json.
Its decision-source revision is 63fe155f22edc01f9d2bc688ccb6057c77114ac4a1a80d15de5d09b1f451b4f8, with a complete pool only for the selected pair.
The broad pool inspect artifact is hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9d67fd8f8510c8f6dba64d2f857ecf5ee300c1ede0d289299195dd67e102822b/947faacf31b8e7d711599e3d1366bcb55d1cb9711321b1294909736402bb0972/probability-inspect-7551437660a6.json and reports poolComplete=false.
The routed probability auditor's eight-case evaluate timed out after 600 seconds, and no sweep, render, or scenario result was returned.

### 5. Targeted rows may multiply beyond the category's semantic action count

The existing cbrn_occupation_measures_category defines eight decision IDs.
One coercive-security migration entry is permanently hidden, and the ordinary and sale protective-aid definitions share one player-facing action.
That leaves six semantic action types, including the two coverup decisions, admission, and inspection.
The four state response decisions can each generate an entry for every eligible state, so the visible row count can exceed six when several states qualify.
No simultaneous target inventory or category raster was returned.
This is a density risk, not a confirmed clipping or six-action violation.

## Category lifecycle and cognitive load

The category is existing ordinary decision-list UI, with no dedicated scripted GUI, additional tab, or mechanic window introduced by this adapter.
The two coverup entries require the country history flag and a state that remains controlled by the responsible country, uses the nerve-suppression route, and has no prior response or discovery.
The seal and destruction flags prevent repeating the same outcome on the same state.
The decision-level re-enable interval remains 30 days.
The same category also carries one-time authorization, timed aid delivery, admission, and inspection actions.

There are no missions or timed objectives in the two audited decisions.
The visible dynamic value is the current Political Power quote.
Its cause is Condemnation scaling, its amount is the actual payment, and the correct response is to pay that quote or wait for the decision's native cooldown.
The source row uses the Political Power texticon and has no second spendable resource.
The ordinary decision descriptions and cost details are concise and do not expose raw counters or helper names.
The pending cost getter clearly identifies refund recovery and displays the saved paid amount.
The static effect tooltip is the exception described in finding 2.

## Cost, requirement, and outcome audit

Each decision has one spendable cost type, Political Power, shown with the £pol_power texticon.
The ordinary base prices are 40 PP for sealing and 60 PP for destroying records, multiplied by the existing Condemnation factor clamped from 1x to 3x.
Without an eligible shared source the ordinary fraction remains unchanged.
With an eligible source the shared quote applies the source and quantizes only the final amount to one PP.
The 86-case source handoff reports exact affordability boundaries and parent getter cases.
Its modeled score 500.12345 values are 80.00987 and 120.01481 ordinarily, and 41 and 61 under the baseline 50 percent sale.
No hidden fifth cost or literal resource-name fallback was found.

Requirements remain separate from the PP cost row.
The displayed requirement names the selected state and the responsibility, control, route, and prior-response conditions.
The cost gates and normal hover colour use the same inclusive shared affordability helper.
The validated refund preflight bypasses current PP affordability only for the matching saved refund receipt.
Fresh payment rejects any existing open pointer, including malformed pointers, and cannot reuse the old paid price.

No change to target UID selection, route, responsible country, outcome bodies, deaths, contamination, inspection upkeep, AI weights, or decision cooldown was found in the current bounded source diff.
The outcome mapper still uses the exact saved chemical record UID and does not fall back to another row.
The queue rotates unresolved receipts and preserves the unvisited suffix at the native 1,000-iteration boundary.
The 86-case source handoff reports no duplicate debit, no outcome replay, and exact receipt cleanup across multiple pending IDs.
Native save serialization and an unexpected engine interruption between the native debit and all receipt fields being written remain untested.

## Localisation and tooltip review

The fresh cost and detail getters use the shared price outputs and show price unavailable when the quote is invalid.
The pending cost row displays Payment recovery.
Its tooltip includes the saved PP amount and states that retry makes no new purchase.
All four getter chains are covered by the separate localisation audit's 133 source-model scenarios.
That audit closed its three earlier cost/getter findings without production changes.

The normal seal and destruction effect tooltips remain unconditional in the decision definitions.
They conflict with the recovery-only cost tooltip while a pending refund target is visible.
No other localization defect in the bounded cost and recovery keys was found.

## Validation, MCP evidence, and limits

The architect's current handoff reports 86 source-model scenarios passed, with 21,550 production helper returns and 82,017 helper-local temporary values discarded under the conservative frame model.
It exercises real quote, affordability, pay, record, refund, settlement, state mapper, exact UID, outcome, achievement, and parent getter definitions.
Fault injection changes persistent fixture inputs before the real shared helpers run.
I reviewed the test harness and the new payment-time eligibility cases but did not rerun the suite.
The current parent repair snapshots receipt-specific eligibility at payment and requires that exact receipt ID during delayed settlement recovery.
The added cases cover AI-to-human and debug-to-normal recovery, reverse transitions, and exact eligibility-ID cleanup.

The separate probability inspect results and the updated adapter handoff do not provide native scenario evaluations.
Both corrected hoi4.decision_inspect requests for the two IDs timed out after 600 seconds.
The hoi4.gui_inspect and hoi4.gui_render attempt using the ordinary category ID returned no render artifact before the bounded review ended.
The category has no mod-owned scripted GUI window, so no visual alignment or native cost-row rendering claim is made.
No game launch, log search, or native runtime test was performed.

Reference evidence:

- Installed common/decisions/_documentation.md, lines 12-46, revision 5e7e686b5582f32c38d898d805e17171e88f3bfeee4a030deb1884f9726de019.
- Offline Decision modding wiki, custom-cost and ai_hint_pp_cost section, lines 284-336, revision 7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162.
- Offline Decision modding wiki, re-enable cooldown section, lines 278-283, same revision.

## Handoff

Production files edited by this reviewer: none.
This report is the only file created by this review.
Audited decision IDs: cbrn_seal_state and cbrn_destroy_contaminated_records.
No mission, event registration, default-enable gate, AI weight, asset, or cost constant was changed.
No gameplay simplification or fallback was made.
The separate completion audit handoff still records the pre-repair payment-time eligibility defect and older 79-case source hashes.
Treat that historical F1 as superseded by the current adapter handoff and 86-case result.
Its owner-invocation gap and native AI, cooldown, persistence, and GUI evidence limits remain relevant.
This bounded review does not claim Event 026 or universal-cost system completion.
Skills used: chaos-redux-decisions-missions, chaos-redux-events, and chaos-redux-subagents.
No skill was created or modified.
