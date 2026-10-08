# Event016 KRG Portal Fabrication Repair: Independent Integration Audit

Status: The narrow fabrication receipt repair is present in the current integrated source snapshot. Parent native-field, visual, probability, and final integration checks remain open. This report does not certify Event016 as a whole.

Authority is the accepted contract at docs/plans/016_brilliant_scientist_plans/016_portal_transit_fabrication_receipts_2026-10-08.md. The separate Private Teleportation Deployment commissioning payoff remains accepted and queued at docs/plans/016_brilliant_scientist_plans/016_mengele_transit_deployment_acceptance_2026-10-08.md. The KRG batch does not satisfy or replace it.

## Findings sorted by severity at the original audit reading point (2026-10-08)

1. P2 at the original reading point, later owner-resolved as recorded in the appendix: portal_transit_batch_requirements_tt in localisation/english/016_portal_transit_batch_l_english.yml:19 says “military industry in the Kruger State.” The actual requirement is country-scoped num_of_military_factories > constant:brilliant_scientist_krg_value.zero. Installed triggers documentation says this reader supports COUNTRY scope at 6795-6803. Keep terminal access localized to the Kruger State, but state that at least one military factory is required in the country. This is a wording defect, not a gate defect.

2. P2, visual evidence remains open: the valid hoi4.gui_inspect request for vanilla countrydecisionview with the KRG scenario timed out after about two minutes. hoi4.gui_render returned a complete production artifact, but the rendered decision list was empty and contained no KRG category or Portal batch row. It therefore cannot verify the cost icons, blocked colors, active timer text, wrapping, or row clipping, and there is no matched before/after decision-row comparison. The renderer also reported GUI_ACCIDENTAL_CLIPPING for the vanilla countrydecisionview and background at 550 by 1002 to 544 by 1002, GUI_CHILD_OUTSIDE_CLIPPED_PARENT, GUI_NEAR_CENTRE_OFFSET, and GUI_VISIBLE_OVERLAP between production_header_bg and decisionview_title. These findings point to game:interface/countrydecisionview.gui, outside the feature-owned layout source. Report them as parent-owned shared-window findings rather than treating the Portal cost render as visually accepted. The feature category has no scripted_gui attachment and the repository contains no Portal-owned .gui layout.

3. P2, AI balance comparison remains pending: the probability auditor’s expanded frozen-source evaluation has 41 rows, status partial, four definitively false eligibility rows, 37 unresolved rows, nine unresolved findings across seven unique input types, poolComplete=false, and score_only output. KRG_PORTAL_MILITARY_INDUSTRY_MISSING is definitively false in the frozen source. The artifact is docs/testing/event016_portal_batch_20261008/probability/probability-61d09999dd5f98736cfe6361.json with source hash 06651bae471b230007d92c52e060ec4e992669542a205e212c28f2c0ba0fbd56 and scenario hash 5e795599ff1e6eadc2ae8e23755ac1f8ce8fd5cb51be8e30949a6397b0a79867. The auditor thread remains active and no matching after-source hoi4.probability_compare result is present in the inspected handoff or artifacts. Do not claim AI balance acceptance until that comparison returns.

4. P2 at the original reading point, later owner-resolved as recorded in the appendix: docs/events/016_brilliant_scientist/systems/projects.md:7 says there is no Political Power storefront and Event 016 does not clone native project clocks or rewards. That sentence is in HEAD and describes the fifteen-family portfolio, while the accepted adjacent KRG batch uses a 65 Political Power quote and a native 90-day decision timer. Clarify that the statement applies to the portfolio, or document the separate batch beside it. The new transaction API documentation already describes the batch.

5. P3 at the original reading point, later owner-resolved as recorded in the appendix: common/scripted_effects/016_portal_transit_batch_effects.md:18 calls the BEGIN recheck “nonfactory authority.” The recheck now includes the original military-factory requirement while deliberately skipping the already-reserved four civilian factories. “Non-CIC admission requirements” would distinguish those checks. Lines 72-75 already state the exact military-factory rule.

6. P3 at the original reading point, partially owner-resolved as recorded in the appendix: neither recovery text displayed a magnitude. The output tooltip now shows delivered-of-total and the remainder/closure behavior. The refund tooltip now shows three exact owed components; whether that component breakdown is the clearest presentation remains under consideration.

## Decision lifecycle and action load

The existing category is brilliant_scientist_krg_portal_and_temporal_category. The existing primary action remains brilliant_scientist_krg_fabricate_portal_transit_batch. It retains the 90-day native timer, 30-day re-enable interval, four-success cap, and 180-unit Portal equipment output.

There are two recovery decisions: brilliant_scientist_krg_recover_portal_transit_output and brilliant_scientist_krg_recover_portal_transit_refund. The fabrication row is hidden while either valid recovery is pending. In valid receipt phases, only the output or refund recovery path is exposed. The output row can deliver only the remainder or retry settlement; the refund row retries only the recorded amount still owed.

The parent preservation review reports 21 original decision blocks in this category. One existing fabrication block changed and exactly two recovery blocks were added. The category itself is not a decision block. The feature therefore adds one normal action and one phase-specific recovery action. The full category’s simultaneous visible-action count is not certified here because decision_inspect did not return a scenario result and the native decision render was empty. No new mission was added or changed. The 90-day timed decision is not a mission.

The feature itself shows three resource values in the inline cost, plus the four civilian factories and 90 days in the hover text. The 180-unit output and four-success cap have clear consequence and limit text. No wall of prose, extra tab, category, or unexplained status counter was added. At the original reading point the recovery texts omitted exact quantities. The owner has since added delivered-of-total output text and exact refund components. Refund presentation clarity remains under consideration.

## Costs and requirements

| Commitment | Ordinary amount | Player-facing icon | Count |
| --- | ---: | --- | ---: |
| Political Power | 65 | £pol_power | 1 |
| Concrete support_equipment_1 | 200 | £support_equipment_text_icon | 2 |
| Fuel | 1,000 | £GFX_fuel_texticon | 3 |
| Civilian factory reservation | 4 for 90 days | £civ_factory | 4 |

The shared quote system may discount the three resource prices. The displayed row contains those three icons, and its tooltip adds the native four-factory reservation and duration. No hidden fifth cost or literal resource-name fallback was found. The military-factory prerequisite is non-consumed and is not a fifth cost.

Admission uses the full quote and four free civilian factories. The literal native complete_effect sets the temporary native-entry marker immediately around BEGIN. BEGIN consumes it on every path, obtains a fresh quote, publishes the payer/action/serial receipt, and records measured payments through the existing universal-cost APIs. It does not repeat the four-factory check after the native reservation. The cost getters share a single quote and reuse the same per-resource affordability predicates.

The original frozen helper at docs/testing/event016_portal_batch_20261008/before/common/scripted_triggers/016_brilliant_scientist_kruger_state_decision_triggers.txt:245-252 required more than zero military factories. The current requirements_met block at common/scripted_triggers/016_portal_transit_batch_triggers.txt:105-115 retains that exact predicate at line 108 for selection and authorized BEGIN. It is not checked as a repurchase condition at expiry or recovery. The original motorized-equipment and manpower gates were intentionally consolidated into the accepted cost design, and this audit does not flag them as dropped requirements.

## Cognitive load and mission quality

The active feature row count is one in normal play and one recovery row in a valid pending phase. Malformed flags can expose blocked recovery rows together, but no valid receipt path creates both a refund obligation and positive-output obligation. The full category count remains unresolved because the decision inspector and native decision render did not expose the category's live entries. No new active mission, owner, region, duration, or mission duplicate risk was introduced.

The visible values have practical meaning: three dynamic resource quotes, four committed civilian factories for 90 days, 180 output, and a four-success cap. The military-factory threshold is meaningful but its current tooltip places it in the wrong geography. The remaining refund and output quantities are not displayed, so the player sees the kind of work due but not its magnitude.

## AI, routes, and probability evidence

The fabrication and both recovery decisions use the unchanged medium AI base. The fixed ai_hint_pp_cost mirrors the nominal 65 Political Power amount. The action remains gated by active KRG decision authority, operational Teleportation, the recruitment focus, the existing raid-AI OR linked-network condition, actual Portal technology, non-capitulation, the batch cap, pending-receipt state, resources, and factory reservation. No invalid target or new AI route was found.

The 41-scenario frozen-source artifact is baseline evidence only. Its adapter is mission_ai_will_do with score_only selection, no normalized probability, and no complete candidate pool. The initial 36-scenario result is historical prefix evidence, not the final matching fixture. The parent has notified the dedicated probability auditor; this audit did not launch another probability call. The current result does not support a balance or selection-frequency claim.

## Localization, scripted localization, and CXT

The native custom-cost base, blocked, and tooltip keys are present. The inline values use the matching Political Power, support-equipment, and fuel texticons. GetPortalTransitBatchCost owns the four consumed quote outputs and calls the quote helper once; the nested getters use the shared affordability predicates without requoting. Integer and five-decimal formatting uses round_temp_variable. Installed triggers documentation confirms this trigger is supported in any scope at 7440-7449.

The recovery titles, descriptions, requirement tooltips, and effect tooltips exist. At the original reading point the military-factory wording and recovery magnitudes were open. The owner corrected the countrywide requirement text and added both output and refund amounts; refund component presentation remains under consideration.

The CXT observer is chaosx_cxt_event016_probe_portal_transit_receipt in common/scripted_effects/016_portal_transit_batch_cxt_effects.txt, called from the existing CXT ownership hook in common/scripted_effects/016_mengele_native_ownership_cxt_effects.txt. The quote helper is invoked in if.limit inside KRG scope, and the caller owns its quote outputs. CXT copies receipt, paid, output, pending, and fresh-quote data to test-country fields. It creates no batch, pays no cost, refunds nothing, and grants no equipment.

## Cleanup and exploit risk

Zero delivered output can refund measured actual payments once. Positive partial output retains the funded receipt and owes only the remaining quantity. Exact full output advances the existing KRG batch counter once; settlement retries do not redeliver or increment history again. Repeated refund, output recovery, cancellation, and settlement calls are bounded by the saved receipt, component rows, measured remainder, and closed flags. The four-success cap and native timer/cooldown remain the repeat limits. No free-output loop, resource farming, counter replay, or refund-after-positive-output path was confirmed by the 59-case source driver.

The explicit cleanup helper cancels and retires the receipt before remove_decision. Installed effects documentation says remove_decision does not run remove_effect or start a cooldown at effects_documentation.md:5959-5967. No claim is made that it does. The source driver models adverse synchronous/deferred reentry but does not prove native callback generation isolation, timer ordering, factory reservation ordering, or engine serialization.

## Before and after behavior

Before the repair, the existing timed action lacked an owner receipt proving payer, quote, measured debits, shared component rows, and delivered quantity. Its frozen source already required at least one military factory.

After the repair, the existing action still commits its ordinary 65 Political Power, 200 support_equipment_1, and 1,000 fuel quote, with four civilian factories reserved for 90 days. It records actual payments under one actor/action/serial receipt, returns measured equipment from the existing Portal family, preserves partial output without a whole refund, and advances the existing counter only after exact full delivery. The original one-military-factory admission condition is preserved, with no retest at finish. Two gated recovery decisions settle output or refund obligations without new costs, timers, factory reservations, or duplicate history.

## Original audit reading-point source identity and validation (2026-10-08)

The integrated after manifest is docs/testing/event016_portal_batch_20261008/after/source_manifest.json, SHA-256 73c9ec47424df74fac6b05b8438eee70e6ef579a1fe518274f309224e0758ede, captured at head 92ce42facc32e03af11ecfe04dc756492d1bdc16. All nine snapshot files and all nine corresponding live files matched the manifest at seal time.

At the original audit reading point, docs/testing/event016_portal_batch_20261008/parent_source_result.json had SHA-256 fbea367284c0af6b369d0d1ce5d391f0a66179b6e2600a3a635df803da3bcff6 and reported 59 passing actual-source scenarios. The refreshed result after owner wording updates is recorded in the owner-resolved appendix. I did not rerun the CommonJS driver.

The core source hashes in the after manifest are: decision 1500ddc67c8804c2d019240f4e15f585a3d2823db1c68e69d825c9f976a13967; Portal trigger 81d338f499ccda57b72326c3057db888e6996618c21f6bc0575875e316a151a8; Portal effects 5d0bae27543f17d8213481a0c14ae1522a61ab91cac88c2684df7ec1a32f947a; Portal constants 95444bc506a1e3ab264a9bbf7f73f5009fb82f6571a04dcaa5c1ce85694a46a0; and CXT observer a5265f3df4a9988703564a48efa6db9f08522108b322952348328635a03bb76f.

Parent-owned mixed-source checksums at the original audit reading point were: completion wrapper a9a554e67a0dab4b079bafc6e56ab498b5d4ed47ce42f8195ab54037938bde45; root cleanup caller ea56bf8d11b777752d87bce5e98001250f93674e389eb8d6ed31d76610773bd0; CXT call-site file 54b14b4d5170749a40bf66eeeaaf6dc9efc9dbe3dc3df881ed9438e6e49400b5; cost localization 250b094ab6827c99da26814a0ede297ccf00ef9f8dfea6ca381fa653facc4c69; and dynamic-effect registry file f8fe39f34ed3bfd5737c125d200610f9e9e8c1eae4ec49655672aa1a4f73a9cd. Review only the named wrapper, cleanup call, CXT call, and registry row within those mixed files.

The connected source_lookup route located the current fabrication decision at lines 215-263, revision 5e5c64aaeb122afa9cb918d2cf5e3e5468320bf61399943db8e42573c12c7656, and the restored requirements trigger at lines 105-115, revision 92a6ccb451567401cd8874602b7c40d82435dbf400e44e8a46ea47f2bb5a3506. The trigger documentation confirms num_of_military_factories is COUNTRY scope at triggers_documentation.md:6795-6803, revision 7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29. The offline Scopes page's strict greater-than example is at Scopes - Hearts of Iron 4 Wiki.md:97-129, revision 18ef5249e4991f5427eca9ec4a2f66dd47f51e26a491c730adc622f1f5db1b49. Decision cost and timer references are Decision modding - Hearts of Iron 4 Wiki.md:284-356, revision 7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162. The installed remove_decision entry is effects_documentation.md:5959-5967, revision 2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af.

The installed GUI documentation says a custom decision-category GUI requires a scripted_gui attachment to that category. The current category has no such attachment, and no Portal-owned .gui file exists. The available native view is the game-owned countrydecisionview at interface/countrydecisionview.gui:3-74; the decision item is at 399-483. The GUI render artifact is hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/11745615bd90cf03c811fa07d691838a4696547addb0330a9e101959d30a7e33/672d56453dfb855512dd7d52c02fd548b90eb6a23c464b463eaf7e152199d485/countrydecisionview-full.png, 109428 bytes, SHA-256 11745615bd90cf03c811fa07d691838a4696547addb0330a9e101959d30a7e33. I retrieved it in four byte ranges and verified the full digest. It shows the empty vanilla decision panel for the supplied scenario; no Portal row was rendered. The GUI tools therefore do not establish visual acceptance of the cost row.

The CXT file-level script_validate result was partial: 61 commands checked, zero unresolved findings, 36 argument blocks unchecked, and one root of unknown scope. The current trigger-file script_validate request did not return within two minutes and was terminated. Parent-reported partial validation is not upgraded here to a complete syntax or parameter proof. The tool also reported the neutral output body and core trigger/effect checks as partial; native parameter behavior remains open.

The valid decision_inspect request returned DECISION_SOURCE_STALE when its expected revision was 5e5c64aa and the analyzer observed a08b04c1. Retrying with the observed revision did not return within two minutes. The current source_lookup results above are the successful bounded source-location evidence.

## Remaining parent work and completion boundary

The owner has resolved the countrywide military-factory wording, project-portfolio documentation scope, and BEGIN API phrase. Before visual or balance acceptance, the parent still needs a scenario that renders the native KRG decision row, review of the shared vanilla clipping warnings, and the dedicated auditor's matching 41-scenario comparison with its unresolved pool limits.

The parent also owns native decision cost/default/entry/table-shape validation and the final CXT-driver layer check. Native field parameters, reservation and callback ordering, stockpile getter immediacy, producer/design restoration, and same-action callback-generation proof remain unverified. User live-game evidence remains separate. Parent should isolate the single cleanup call, single dynamic registry row, CXT hook/documentation hunks, and all other owned edits from unrelated shared-tree work at commit.

No unauthorized simplification was found in this batch repair. The original support/motorized/manpower resource gates were consolidated as accepted costs; the original countrywide military-factory requirement was restored. No new category, mission, unit, template, equipment family, model asset, or private commissioning payoff was introduced. No plan handoff was required.

This audit wrote only this handoff. It made no gameplay, index, Git, or other-document changes and did not launch HOI4. The parent owns final review and commit.

## Owner-resolved appendix (2026-10-08)

This appendix records owner changes after the original audit reading point. Findings above remain as dated evidence and are not current defects unless stated here.

- The requirement tooltip now says “At least one military factory is required in this country.” This matches the COUNTRY-scoped gate and removes the false Kruger State location implication. Current localization SHA-256: aed9ffb61750399402c6c895423811f70b5eefaeab0180ecbd35a6679541e96c.
- The project portfolio document now scopes native Prototype clocks and output authority to that portfolio and links the separate Portal transit fabrication action at docs/events/016_brilliant_scientist/systems/projects.md:7. The linked action contract is docs/events/016_brilliant_scientist/systems/portal_transit_fabrication.md. Current hashes are 26514e94891020288b605565481eddfba6c16f1ec963aafa81d6d9173edceeb6 and d4c99c92aad30fa994bc2c8a8e8a7169edd7e753785290dcad18d56229edeb45.
- The BEGIN API table now says “non-CIC admission requirements,” separating the countrywide military prerequisite from the four already-reserved civilian factories. Current API documentation SHA-256: 779887ae50229cba305450e4651f6c1b5ef732ba809be47ef75828d0823a1e56.
- The output recovery tooltip displays delivered-of-total units and promises only the remainder or final closure.
- Refund recovery now calls GetPortalTransitBatchRefundAmounts. The getter first requires brilliant_scientist_krg_portal_batch_can_recover_refund, then reads the three krg_portal_batch_refund_remaining entries into temporary Political Power, support-equipment, and fuel display scalars. Invalid or unverified recovery state falls back to portal_transit_batch_refund_unverified. The getter does not quote, debit, credit, refund, or change KRG history. Its caller and three texticon values are present in the owner front-end source snapshot.
- The exact refund components are now displayed. The owner still considers whether that three-component magnitude presentation is clearest; this is a presentation question, not evidence of an incorrect refund calculation. No visual acceptance is inferred.
- The correct preservation count is 21 original decision blocks total. One existing fabrication block changed, 20 other original blocks remain, and two recovery blocks were added. The category itself is not a decision.
- The parent reran the retained source driver after the API wording change. The refreshed docs/testing/event016_portal_batch_20261008/parent_source_result.json reports 59 passing scenarios and has SHA-256 c710037841b3616d15b0c0dce13c642be6e769b1c88d01f3e74a9cdad094d4cf. Its 12 source hashes match the live files. The nine-source after manifest remains SHA-256 73c9ec47424df74fac6b05b8438eee70e6ef579a1fe518274f309224e0758ede. Its snapshots remain intact, but the scripted-localisation live source has since advanced and is captured with the YAML in the frontend review manifest.
- The frontend review manifest docs/testing/event016_portal_batch_20261008/frontend_review/source_manifest.json has SHA-256 c159332014772517ae8b17d7ac7b42db2d42e77677e9d85c80df05e9f57fcee2. Both current front-end source files match their snapshot hashes. This is source snapshot evidence, not production GUI acceptance. The older after snapshot is preserved.
- The empty countrydecisionview render and shared vanilla clipping warnings remain open. The dedicated probability auditor still owns the matching weighted comparison. Neither visual nor AI acceptance is claimed.
