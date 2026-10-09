# Event 029 sealing receipt post-integration review

Date: 2026-10-08.

Disposition: the accepted bounded receipt integration is present and source-reviewed. The complete sealing route and native execution proof remain unresolved.

Acceptance basis: the user's post-integration audit instructions and the 2026-10-08 parent acceptance recorded in docs/events/029_riches_found/seal_receipt_contract.md for direct inline resolution at native decision boundaries.

This is a read-only integration audit. The only file created by this audit is this handoff. No gameplay source, Git state, game process, or child task was changed or started.

## Scope and source identity

The audited decisions are decision_riches_found_gold_seal_depths and decision_riches_found_demons_permanent_seal in common/decisions/029_riches_found_decisions.txt.

The current decision file SHA-256 is 6CC508136D8E3B94443204603F16506EC4CB10760E1DEAEB665B57DD69DF4107, matching the requested CURRENT6CC508 source.

The three receipt modules match the source-case report identities:

| File | SHA-256 |
| --- | --- |
| common/scripted_effects/029_riches_found_seal_receipt_effects.txt | 0154EF86F38C47EBF9324252FFC4F662551CE6E819FB934EB40A07CF1649DC81 |
| common/scripted_triggers/029_riches_found_seal_receipt_triggers.txt | 9F8C3F10FD8A7F67652EA5D4E45BBA4CEFC9EB9E38DDB73F49287BFCF5AA5B0E |
| common/script_constants/029_riches_found_seal_receipt_constants.txt | 9C61E175915F607E991A962226D890EE4CF7A613B91D6E733534F08BE1B5DBC4 |

The current on-action file SHA-256 is 6496395468B422822C25337B353A8017038B6347F0BAB04F32E6C7BB27678C95.

The user-provided ownership boundary is preserved. A line comparison against evidence/2026_10_08_seal_receipt_parent_before/common__on_actions__029_riches_found_on_actions.txt shows exactly the owned replacement: the former one-line FROM.FROM handler call is now the four-line FROM.FROM block that invokes rf_seal_note_control_change and then the unchanged handler. The neighboring-state refresh and overview text already exist in the parent-before snapshot and remain untouched.

The comparison verifies that the only on-action delta relative to that parent-before snapshot is the specified block replacement. The parent confirms it will stage only that four-line owner block.

## Findings by severity

### High: full sealing-route acceptance remains open

The bounded receipt integration does not add the broader sealing requirements. docs/events/029_riches_found/seal_project_contract.md says the package remains incomplete and lists entrance control, Demons integrity and affected-group resistance, time-scaled evacuation quality, and the complete dynamic quote as remaining acceptance requirements.

Part 3 requires control of shaft entrances for both projects. Part 4 makes Demons success depend on evacuation, entrance control, sealed-depth integrity, and resistance from affected groups. The current route predicates preserve the accepted Gold localized-containment route and the Demons evacuation-or-purge route, but they do not implement all those broader requirements.

Do not describe the complete seal route as finished. Keep those design and implementation items unresolved for the parent.

### Medium: native factory reservation and timer execution are unproven

Both decisions retain the native civilian_factory_use modifier and native 60-day or 90-day days_remove timer. The receipt helpers store the factory commitment and duration as metadata, but do not debit, reserve, or refund factories.

The existing source cases report nativeTimerExecuted=false and nativeFactoryReservationProven=false. No engine or live-game validation was performed in this audit. Factory reservation ordering, cancellation behavior in a running campaign, and actual native callback execution remain unproven.

### Medium: numeric AI comparison remains unresolved

The prior dedicated report docs/plans/029_riches_found_plans/subagent_handoffs/seal_receipt_probability_2026_10_08.md is the primary probability evidence for the exact current decision hash. It records the connected HOI4 MCP 3.10.0 classifier defect that routes native decisions with days_remove into mission_ai_will_do.

That report compared the pre-receipt decision snapshot with the current 6CC508 source, but the terminal response was misrouted through mission_ai_will_do. It produced no accepted decision score delta, eligibility ranking, click probability, or comparison pass. The report also records that both ai_will_do blocks are unchanged, with normalized block hashes 1DCE6A0F644ED907A13DD25687599CDBFBA073F40146E9B44CC0E70AFB6ED17A and 2A065167BB73A834BA09A8FE4F0815E69B2BA354BCBA80A4BED801543DE52BF5.

No probability query was repeated, as requested. The unchanged source blocks establish textual preservation only, not numeric AI validity or balance.

### Medium: the rendered native decision window did not show the Event 029 category

The category definition in common/decisions/categories/029_riches_found_categories.txt is an ordinary category with a static picture and no scripted_gui attachment. The native decision window countrydecisionview was inspected and rendered because its cost presentation is in scope.

The explicit 1920x1080, UI scale 1 render is a blank native decision panel because the synthetic fixture does not establish a registered Event 029 mine state or a visible decision target. No seal decision row or cost string appears, so the cost-row fit and blocked-state appearance remain visually unresolved.

The native window inspection reports clipping from 550x1002 to 544x1002 and visible header overlaps in the shared game window. The full-window render visibly shows the empty native panel. This is a shared vanilla interface finding outside the two-decision source scope. It is recorded for parent ownership and was not edited.

## Before and after behavior

The frozen pre-receipt decision source at SHA-256 88B2F6716F401657251BC79C8C144B081953D71725B81F693F630F28AEE36B8D had no actor/mine/family receipt or controller epoch in these two consumers. It used direct fixed manpower/support payments and the earlier delayed-result refund branch.

The current 6CC508 source retains the same civilian-factory gates, factory modifiers, durations, route effects, and AI blocks. Availability and custom_cost_trigger add the manual receipt gate while preserving the complete existing cost gate. Selection calls the family start helper, which rechecks and records the exact manual quote before one debit. Removal resolves the saved receipt, and only a fresh consumed result permits the preexisting outcome body. Native cancellation refunds the stored quote without applying success. The existing state-control callback advances the epoch before its unchanged mine-control handler.

The Gold success flags, conditional partial-seal step, pressure effects, and refresh calls remain intact. The Demons success flag and entombment-before-terminal-cleanup order remain intact. The helper package does not alter native factory reservation behavior.

## Decision category lifecycle

The category remains riches_found_mine_management, visible only when the country has a registered controlled mine, with visible_when_empty = no. It uses the existing static category picture and ordinary targeted decision rows.

Both seals remain state-targeted with state_target = any_controlled_state, map_and_decisions_view, and fire_only_once = no. Their route, mine-registration, controller, layer, terminal, and existing completion checks remain in the target and availability paths.

Selection calls one matching start wrapper. Native removal calls one matching resolve wrapper, and the old success body runs only when the fresh result equals result_consumed. Native cancellation calls one matching cancel wrapper. Cancellation refunds the saved quote and cannot run the finish body.

No cancel_trigger, cancel_if_not_visible, extra timer, or virtual timeout was added. A pending actor/mine/family slot remains locked until the actual native removal or cancellation callback.

## Cognitive-load notes

This bounded integration adds no decisions, category, mission, tab, or scripted window. It adds one receipt gate to each of the two existing targeted actions.

Within this pair, each row shows three cost values with icons and a 60-day or 90-day duration in the full cost tooltip. The Gold tooltip explains the conditional pressure strain and relief. The Demons tooltip states that a military purge does not evacuate the trapped shift.

The receipt-ready tooltip is the only receipt-specific localisation key found in the current English file. Its wording describes an existing project slot and available crews and tools. It exposes no rf_seal, epoch, pending-count, or receipt identifier.

No Event 029 category-wide simultaneous-action count was established. The blank native GUI fixture contains no decision rows, so this handoff cannot confirm the normal target of three to five primary actions per phase, the six-action ceiling, or the one-to-three active-mission target for the whole category.

## Mission quality

The receipt integration adds or changes no mission, mission category, region, duration, success effect, failure effect, or duplicate mission.

The existing Demons district-cleared predicate still accepts either evacuation or military purge. The permanent-seal effect records entombment harm only on a consumed success receipt and does so before terminal mine cleanup. The existing workforce evacuation mission was not re-audited as part of this two-decision receipt integration.

## Cost and requirement audit

| Decision | Native capacity commitment | Manual spendable costs | Duration | Distinct spendable types |
| --- | --- | --- | --- | ---: |
| decision_riches_found_gold_seal_depths | 2 civilian factories | 300 manpower and 150 support equipment | 60 days | 3 |
| decision_riches_found_demons_permanent_seal | 2 civilian factories | 600 manpower and 150 support equipment | 90 days | 3 |

The original affordability helpers remain in both available and custom_cost_trigger. They require the existing civilian-factory capacity, family manpower, and support-equipment amounts. The added family manual gate is hidden behind riches_found_seal_project_ready_tt in available and runs again in custom_cost_trigger.

The start helper repeats the route and manual reserve checks immediately before publication and debit. It reads manpower_k in thousands, checks the support-equipment stockpile against the same quote, stores the exact quote, publishes the pending flag and count, then performs one manpower debit and one shared support-equipment debit.

The full cost row uses the matching civilian-factory, manpower, and support-equipment texticons. There is no political-power cost, truck cost, hidden fifth cost, or duplicate direct manpower/support debit in either decision block.

The broader event contract counts foregone output as a fourth project tradeoff. It is an outcome consequence rather than a fourth spendable payment under the decision cost budget.

## AI validity and route locks

Gold start and finish continue to require a registered mine controlled by the decision actor, the Gold layer, a restricted Gold route, a nonterminal state, and no completed Gold seal. A later contract or occupation flag alone still does not invalidate the Gold restricted-route predicate. The prior review records this as an open design question, not an accepted route defect.

Demons start and finish continue to require actor control, registration, the Demons layer, a cleared district, no active contract or occupation, a nonterminal state, and no completed permanent seal. Military purge remains selectable through the existing cleared-district predicate and retains its explicit entombment outcome.

The receipt does not depend on current UI selection state. Targeted-decision ROOT remains the acting country and FROM remains the state target. The control-change callback retains native ROOT as new controller, FROM as old controller, and FROM.FROM as the changed state.

Both declared AI blocks remain textually unchanged from the pre-receipt comparison baseline. Numeric weight validity, eligible rankings, and balance remain unresolved under the prior MCP classifier report.

## Cleanup and exploit risk

The start gate rejects an existing pending flag or any of the seven tuple fields for the exact actor, mine sequence, and family. The same slot cannot be repaid while pending. Different actors have separate country storage, and different mines use separate sequence keys.

A real controller change advances the state epoch before the existing control-change handler. Leaving and returning changes the epoch, so the earlier receipt cannot authorize success. Its own native boundary refunds the exact saved manpower and support-equipment quote once.

rf_seal_close_loaded clears only the matching payer tuple and pending flag, decrements the state count once, and checks exhausted-epoch rollover. The epoch resets to zero only when the module-owned pending count is zero.

The existing cleanup chain reaches riches_found_clear_mine_cleanup and specific contract, mission, occupation, closure, recovery, and stale-target cleanup helpers. A source-wide search found no references to the new rf_seal counters, payer fields, or pending flags outside the receipt module, decisions, and on-action call. Terminal cleanup therefore does not clear another payer's pending receipt or the receipt count.

On Demons success, result_consumed gates the existing body, which sets the seal flag, records entombment harm, then calls riches_found_permanently_seal_mine. The order is unchanged and the receipt for the successful actor is already closed before this body runs.

The current 23-case actual-helper source report covers paid-once pending restart rejection, a reserve change before payment, transfer away and away/back epoch rejection, parallel mines and payers, saved quotes, repeated closure, terminal state with another payer pending, cancellation without a finish result, malformed receipt rejection, and count-zero-only rollover. Current helper hashes match that report.

No source test suite was rerun. The previously reported 23-case result matches the current helper byte hashes, while the post-integration caller blocks were checked directly. This does not prove native timer, factory reservation, save/load, or live campaign behavior.

## Localization and tooltip gaps

The only receipt-specific English key found is riches_found_seal_project_ready_tt at localisation/english/029_riches_found_decisions_l_english.yml:783. It uses player-facing wording and contains no implementation identifier.

Gold and Demons cost rows use £civ_factory, £manpower_texticon, and £support_equipment_text_icon through the existing scripted localization helpers. The parent confirms that full-hover resource labels remain intentionally for clarity, so this audit records no cost-label or missing-texticon defect.

The existing Gold outcome tooltip preserves the conditional pressure-strain explanation. The Demons outcome tooltip preserves the trapped-workforce explanation. No extra localisation key for receipt flags or epochs was introduced.

## Prior-report and documentation disposition

The dated report docs/plans/029_riches_found_plans/subagent_handoffs/seal_safety_review_2026_10_08.md predates receipt wiring and uses decision hash 88B2F6716F401657251BC79C8C144B081953D71725B81F693F630F28AEE36B8D. Its findings that away/back controller cycling could still authorize success, that direct fixed-quote refunds remained, and that no project-generation receipt existed are superseded by this post-integration review.

The prior report's route-completeness, entombment, human-cost, and native-factory-reservation limitations remain relevant unless separately resolved.

The current API and parent callsite contract at the top of docs/events/029_riches_found/seal_receipt_contract.md is the operative implementation record. Its appended initial blocker and equal-input diagnostic are historical and qualified by the recorded parent acceptance of direct inline native-boundary closure. The hypothetical late duplicate callback described there is not evidence that HOI4 delivers duplicate callbacks.

docs/events/029_riches_found/seal_project_contract.md now lists observed native callback execution among its remaining acceptance requirements. This preserves the accepted direct-boundary design while keeping actual engine execution and factory/timer behavior unproven.

## MCP, reference, and vanilla evidence

The narrow hoi4.decision_inspect calls for each decision returned DECISION_ANALYZED_PARTIAL, complete = false, and 100 unresolved definitions. The route did not time out, so no retry was made. The supplied empty-state scenarios could not establish full route eligibility.

Gold inspection artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/464bd06f3457e057f79eb2c4ac012873ba8c9d02b50775ca541c06c47afe8971/b050633cfb72644397cb22699ceedbe364bcc1454d804e5dd62e91b4cfbcd5b0/decision-30b44391d1df360dcfb62e88.json.

Demons inspection artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1ccc88684acae525577dffdc12a229c5a58055cfdf7b914b6fa76580945f0fb5/7e0ae083800ef4f17f7065f6fe39fa56521d08e6bd7f3ddf82c27affc7a21a71/decision-ca7dfc30479c183124301acf.json.

GUI inspection covered countrydecisionview at shared source revision 7f529aead7f1215a757ca5c288f15aacc801a26745114364438f5291c8ba2cb4. Artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5cfa24218dd3d1d6371e3d898b7c59080b7abd16cd7aede2269ce6564d539077/9541653d3d5d7144df55f25a57b7d89d0e008c91dd67f1a0c84b6064580bdcc7/gui-inspect.7f529aead7f1215a.json.

The explicit baseline render used scenario event029_native_decisionlist_source_baseline at 1920x1080, UI scale 1, with generated scenarios disabled. Its full-window PNG SHA-256 11745615bd90cf03c811fa07d691838a4696547addb0330a9e101959d30a7e33 was assembled from verified byte ranges and visually inspected. Artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/11745615bd90cf03c811fa07d691838a4696547addb0330a9e101959d30a7e33/1ea2916b69782e79b4f2fb9a772f04cfa3540deaba3c507a0733293239207bc8/countrydecisionview-full.png.

The category source has no scripted GUI, so no Event 029 layout edit, reference image, after-render, or before/after GUI comparison was applicable. The baseline image is blank for the requested mine decisions and does not prove cost-row fit.

Offline Decision modding, custom costs and timer lifecycle, lines 284-356, revision 7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162.

Offline Decision modding, targeted-decision example, lines 550-575, revision 7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162.

Offline On actions, on_state_control_changed scope row, line 450, revision 6822adc85a374a1c1364f2def6f32c6d66da9fb0280319ddd6af4b84b33d882a.

Offline Localisation, text icons, lines 221-243, revision 1a8f72362a34b4bb653186746b9fae0b98e463205cb02f12ccf2c3d9ccd3a064.

Installed common/decisions/_documentation.md, targeted decision scopes and trigger frequency, lines 1-46, revision 5e7e686b5582f32c38d898d805e17171e88f3bfeee4a030deb1884f9726de019.

Installed effects_documentation.md, add_days_remove, lines 1066-1080, revision 2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af.

Vanilla AST_union_strike in game:common/decisions/AST.txt, lines 2-42, source lookup revision 70fb0f00f12835b1eb7c5dff553e2d40f283938477911f9132671e1181aff481. It demonstrates a repeatable native decision with days_remove, a civilian_factory_use modifier, and a delayed remove_effect.

The category GUI references establish that a scripted category display requires an explicit scripted_gui attachment and decision_category context. Event 029 has neither.

## Changed files, validation, and remaining work

Files changed by this audit: docs/plans/029_riches_found_plans/subagent_handoffs/seal_receipt_integration_review_2026_10_08.md only.

Gameplay decision IDs reviewed: decision_riches_found_gold_seal_depths and decision_riches_found_demons_permanent_seal.

Receipt wrappers reviewed: rf_gold_seal_quote, rf_demons_seal_quote, rf_gold_seal_can_start_manual, rf_demons_seal_can_start_manual, rf_gold_seal_start, rf_demons_seal_start, rf_gold_seal_resolve, rf_demons_seal_resolve, rf_gold_seal_cancel, rf_demons_seal_cancel, and rf_seal_note_control_change.

Meaningful evidence reviewed: current source hashes, parent-before on-action comparison, the existing 23-case source report with matching helper hashes, two narrow partial decision-inspect results, prior dedicated probability handoff, native decision-window inspect and baseline render, pertinent offline wiki sections, installed game documentation, and vanilla AST_union_strike.

Skipped validation: no native game run, save inspection, source-case rerun, probability rerun, valid Event 029 mine-state GUI render, or after-render was performed. The source-case run already reports passed = 23 against byte-identical helpers. Probability reruns were explicitly out of scope and the prior report records the 3.10.0 classifier failure. No GUI source was changed.

Remaining parent work: preserve the owner-scoped four-line on-action block when staging; keep entrance control, Demons integrity/resistance, time-scaled evacuation quality, and the complete dynamic quote unresolved; obtain observed native callback, factory, and timer evidence through the parent/user workflow; and leave decision AI balance unresolved until a correctly routed probability result is available.

No plan beyond this audit handoff was written.
