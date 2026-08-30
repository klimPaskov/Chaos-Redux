# Event 23 decision and mission audit handoff

Audit status: **NOT READY for parent sign-off**.

Audited snapshot: the shared worktree as observed on 2026-08-30. This audit changed only this handoff file. No gameplay, localisation, or asset file was edited.

## Evidence basis

- Read AGENTS.md, the complete docs/specs/023_sov_nuclear_bombs_specs/ folder, the Event 23 coding and decision-mission prompts, the decisions/missions, events, subagents, and improvement-loop skills, the required offline Paradox wiki pages, and relevant vanilla decision, mission, event, GUI, and documentation files.
- Reviewed common/decisions/categories/023_sov_nuclear_bombs_categories.txt, common/decisions/023_sov_nuclear_bombs_decisions.txt, common/scripted_triggers/023_sov_nuclear_bombs_event_triggers.txt, common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt, common/scripted_effects/023_sov_nuclear_bombs_runtime_effects.txt, the related cost/runtime files, constants, on-actions, event 23, and localisation references.
- Event MCP trace: hoi4.event_inspect on chaosx.nr23.1 returned EVENT_INSPECTED_PARTIAL with revision 7f40f09d54627544a67978bb05c8b699dfe684bc942337d208b79e57d061a139. Artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/38c7f8987f2fe800b2d07f750980c0953f912e7d4ddb8b632855a33c91459e42/55553cda0e6d2859ef274b4cf9ac71349d2ac556a5d8808c26e38e153dafe070/event-trace-7f40f09d5462.json.
- No standalone decision or mission inspection route is exposed by the installed hoi4-agent-tools server. The available probability route was used for decision/mission-weight evidence.
- Mandatory GUI evidence was obtained for the ordinary category. hoi4.gui_inspect returned GUI_INSPECTED with inspectedElementCount 0 because the category is engine-owned rather than a custom GUI window. Artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6412343f897364495b8082f41bd2a349fac15cf8e6b717f32f2dcadda89e25b3/201217998d673852f3c748e531a1ad4d5005d488e4afabd22cc4d5ad382812a4/gui-inspect.3742a24a475d81bd.json.
- hoi4.gui_render produced the ordinary-category render artifact hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8d6aacaf811985589b4473e1bc67ebe5ef62c4c85ef25414541754c5d6989f17/d7efe8710b903c7e2033a043fff5871e2bceff924b247fa2a918df98052f2727/sov_nuclear_bombs_command_category-full.svg. The render did not resolve Event 23 category geometry or actionable click regions, so this is not a visual PASS claim.
- The delegated chaosx_ai_probability_auditor used Operation Postern 1.19.2.0, checksum d245, workspace mod_chaos_redux_ea3b2d67c2c0. Its evidence is recorded below.
- No live game launch or consumer playtest was performed, consistent with repository instructions.

## PASS findings

- The decision category is an ordinary static-picture category with icon, picture, priority, and no scripted-GUI declaration in common/decisions/categories/023_sov_nuclear_bombs_categories.txt:9-20. No Event 23 focus-tree addition or dedicated scripted GUI was found. The forbidden GUI/focus scope is therefore clean.
- Targeted decisions use state_target and save the selected state through global event targets. Exact-purpose validators in common/scripted_triggers/023_sov_nuclear_bombs_event_triggers.txt:281-323, 338-362, and 410-415 revalidate the selected state/site instead of trusting only the saved pointer.
- The reservation handoff is structurally present. common/scripted_effects/023_sov_nuclear_bombs_runtime_effects.txt:201-272 reserves an assigned, operational, or transferred device; :274-316 releases it; :318-382 commits it; and :499-515 clears action context and releases an active reservation.
- Breakaway actions are custody-only at the decision/runtime boundary. The decision block is explicitly labelled custody-only at common/decisions/023_sov_nuclear_bombs_decisions.txt:904-905, and transferred devices do not enter a breakaway native stockpile in common/scripted_effects/023_sov_nuclear_bombs_runtime_effects.txt:354-375.
- Disabled-evolution gates are consistently represented in common/scripted_triggers/023_sov_nuclear_bombs_event_triggers.txt:182-213 and are checked by the opening/progression effects in common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt:55-107 and :617-671.
- The static decision name/description key scan found no missing referenced name or desc keys. This does not establish tooltip quality or dynamic requirement clarity.
- Source cost profiles stay at or below four distinct spendable types per action. The icon-first format is used in localisation rather than literal resource names, but several displayed profiles are wrong or incomplete; see the cost finding below.
- The eight declared mission definitions have explicit visibility/activation, completion, timeout, and cancel fields in common/decisions/023_sov_nuclear_bombs_decisions.txt:978-1104. Several handlers are unsafe or incomplete, so this is only a structural PASS.
- Event 5 control/release callbacks are bounded by saved targets in common/on_actions/005_soviet_collapse_on_actions.txt:15-43 and common/scripted_effects/023_sov_nuclear_bombs_runtime_effects.txt:800-824. No unbounded world scan was found in this handoff.

## Findings sorted by severity

### CRITICAL

1. **Dismantlement cancellation leaks the reservation and mission state.** The mission sov_nuclear_bombs_dismantlement_inspection_mission uses sov_nuclear_bombs_cancel_test as its cancel handler at common/decisions/023_sov_nuclear_bombs_decisions.txt:1090-1104. Dismantlement stages an action context and sets dismantlement_mission_active at common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt:1298-1338, but cancel_test only clears action context when test_prepared is set at :474-483. A cancelled dismantlement can therefore retain the reservation and mission flag. Parent fix: add a dedicated dismantlement cancel/abort helper that always clears the pending demolition, releases the exact reservation, clears the mission flag and selected action context, and restores a safe phase/cooldown.

2. **Retaliation mission cancellation can execute the pending action.** retaliation_window_mission declares complete_retaliation_window for cancel at common/decisions/023_sov_nuclear_bombs_decisions.txt:1026-1040. complete_retaliation_window executes the pending action when the hotline branch is not taken at common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt:1229-1247. Parent fix: use a separate cancel/abort helper that never calls the commit/launch path, releases the reservation, clears authorization and pending target/action flags, and records an abort if the design requires one.

### HIGH

3. **Normal-phase visible action cap is exceeded.** Counting target selectors as primary actions, Phase 4 can expose up to seven rows in common/decisions/023_sov_nuclear_bombs_decisions.txt:366-477 plus the persistent operational selector at :72-88; Phase 5 exposes up to seven rows before certification at :481-579 plus that selector; Phase 6 exposes up to eight rows at :582-695 plus that selector; and Phase 7 exposes up to seven or eight rows at :699-813 plus persistent selectors. Phase 1 and Phase 2 already sit at the six-action ceiling when the operational selector is included. Parent fix: gate selectors to a selection subphase, replace completed actions with mutually exclusive phase states, and keep no more than six visible primary actions in each normal phase.

4. **Ultimatum delay/terminal paths do not reliably clean up.** The delayed event response at events/023_soviet_nukes.txt:166-173 calls resolve_coercion_response. Its delayed branch at common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt:547-550 records the response and opens the response window, but the cleanup at :560-567 only runs for a terminal response. The mission, issued flag, target pointer, and response bookkeeping can remain active. Parent fix: define explicit pending, delayed, accepted, rejected, refused, and timeout states and make every terminal or abandoned path clear the mission, target, issued, response, and cooldown state.

5. **Partial settlement is repeatable while the response flag remains.** sov_nuclear_bombs_accept_partial_settlement is visible whenever the response-window flag exists and is always available at common/decisions/023_sov_nuclear_bombs_decisions.txt:440-450. Its effect at common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt:1002-1008 adds integrity and settlement state but does not clear the response window, ultimatum mission, issued flag, or target pointer. This is an integrity/cost exploit. Parent fix: require a distinct pending response type and clear or consume it atomically with a cooldown.

6. **Limited-strike target validation admits Soviet-owned or Soviet-controlled states.** common/scripted_triggers/023_sov_nuclear_bombs_event_triggers.txt:338-350 allows owner/controller ROOT as a valid limited-strike target. common/on_actions/023_sov_nuclear_bombs_on_actions.txt:11-54 treats a struck state owned or controlled by SOV as confirmed enemy use, with no explicit ROOT != SOV guard. Parent fix: make limited-strike targets fail closed to enemy-owned or enemy-controlled states and add an explicit actor/target inequality in the nuclear-use callback.

7. **No enforceable maximum of three active mission families exists.** event_no_active_project at common/scripted_triggers/023_sov_nuclear_bombs_event_triggers.txt:374-385 is not applied to all action starters. Public ultimatum and limited-strike preparation can overlap at common/decisions/023_sov_nuclear_bombs_decisions.txt:398-436; rail security and joint custody can overlap at :731-755; and separate breakaway operationalization starts have no global family lock. Parent fix: add one central no-conflicting-mission trigger or explicit mutually exclusive phase flags and prove the active family count under each phase.

8. **Displayed cost localisation disagrees with the actual cost profiles.** Cost definitions are in common/scripted_triggers/023_sov_nuclear_bombs_cost_triggers.txt:9-37 and common/scripted_effects/023_sov_nuclear_bombs_cost_effects.txt:9-36, while the visible strings are localisation/english/023_soviet_nukes_l_english.yml:80-84. Security actually uses political power, support equipment, and manpower but the string shows command power. Logistics actually uses light command power, trains, and fuel but the string shows standard command power. Diplomatic actually uses political power, light command power, and convoys but omits convoys. Strategic actually uses political power, heavy command power, support equipment, and fuel but shows manpower instead of support equipment. Parent fix: align each cost key with its exact effect and use the correct texticon for every spendable value.

9. **Several timed decision-map actions have no matching mission lifecycle, and the production mission is orphaned.** The map specifies timed or mission-style handling for actions including storage hardening, assembly, delivery preparation, command exercise, moratorium sealing, and restraint, but their current decision blocks are immediate effects in common/decisions/023_sov_nuclear_bombs_decisions.txt:111-139, :208-246, and :816-887. complete_production_mission exists at common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt:751-773, while begin_production at :888-898 does not activate a declared mission. Parent fix: either implement the bounded mission lifecycle for each accepted timed action or explicitly reconcile the decision map/spec; do not leave dead timers and dead completion helpers.

10. **Other-nuclear-major gating checks major status and technology but not an operational device.** common/scripted_triggers/023_sov_nuclear_bombs_event_triggers.txt:107-115 and :457-464 use major plus nuclear technology, without requiring an operational or assigned arsenal. This can open cross-major routes with a technically nuclear but operationally empty country. Parent fix: use the operational-major trigger consistently for route availability, AI targeting, and evolution gates.

11. **Demand adjustment has no observed direction setter and is repeatable.** The decision is always available at common/decisions/023_sov_nuclear_bombs_decisions.txt:454-465. The effect at common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt:1010-1014 branches on pending_demand_direction, but the current source scan found no setter outside that read, so the fallback repeatedly lowers the demand and only clamps it. Parent fix: expose an explicit bounded increase/decrease choice or set the direction before the helper, then consume the response action and apply a cooldown.

12. **Strike-preparation completion does not revalidate the exact strike route.** complete_strike_preparation at common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt:1177-1194 checks only that an event target exists before completing. The final authorization path rechecks a target, but invalid ownership, control, war, or site state can strand the reservation between preparation and authorization. Parent fix: revalidate sov_nuclear_bombs_event_has_valid_limited_strike_target or a route-specific equivalent at mission completion and recover safely on failure.

13. **AI target selection is not target-aware, and the decision ranking route did not produce usable evidence.** Target selectors use flat bases such as common/decisions/023_sov_nuclear_bombs_decisions.txt:380-381, :646-653, and :705-714 without target-specific threat, route, distance, ownership, or operational-state scoring. The probability adapter returned INTERNAL_ERROR for decision_ai_will_do, classified 73 mixed candidates as mission-style candidates, and found zero usable decision candidates. Parent fix: add safe target score modifiers and rerun the same named scenarios through the probability auditor after the patch.

### MEDIUM

14. **Category visibility can leave an empty command board.** visible_when_empty = yes is set at common/decisions/categories/023_sov_nuclear_bombs_categories.txt:16, while category visibility only checks the actor/event or breakaway crisis at :10-15. Parent fix: remove visible_when_empty or add a bounded child-action/phase visibility condition if an empty board is not intentional.

15. **The category header does not expose the four required player-facing state signals.** localisation/english/023_soviet_nukes_l_english.yml:62-63 shows operational devices, readiness, command integrity, and cumulative arsenal, while docs/specs/023_sov_nuclear_bombs_specs/decision_map.md:16-25 calls for operational bombs, readiness, integrity, and compact posture plus knowledge. The selected target/site, active deadline, and current phase are also absent. Parent fix: replace cumulative arsenal or supplement it with compact posture/knowledge and selection/deadline context without creating a text wall.

16. **Selection pointers persist and can be replaced without a clear/close path.** Operational selection at common/decisions/023_sov_nuclear_bombs_decisions.txt:72-88 and collapse selection at :91-107 remain available across broad non-moratorium phases; coercion selection at :366-380 is available until coercion_open rather than until a valid selection is committed. Parent fix: gate re-selection to an explicit selector state, clear the old global event target on replacement/abort, and show the selected state/site in the action tooltip.

17. **Coercion target ownership/controller semantics are ambiguous.** prepare_coercion at common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt:493-500 saves the owner and then may overwrite the target with the controller. Later validators and effects assume a single target contract. Parent fix: choose and document owner-versus-controller semantics, retain separate event targets if both are needed, and use the same scope for requirements, localisation, AI, and cleanup.

18. **Breakaway missions lack complete actor/crisis guards and cancel cleanup.** breakaway_operationalization_mission at common/decisions/023_sov_nuclear_bombs_decisions.txt:1058-1072 is keyed mainly to a mission flag rather than a current custody crisis and valid actor. Its cancel handler clears only the mission flag, while the helper at common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt:1341-1386 can leave progress-stage state behind. Joint custody has the same flag-only cancel pattern at :1074-1088 and rail cancellation at :1042-1056 clears only its flag. Parent fix: require the current breakaway custody target/actor on visibility and activation, and clear operation, progress, target, and mission flags on every cancel/timeout path.

19. **Rail and joint custody can start concurrently and rail recovery can overwrite the operation variable.** Both decisions are independently visible at common/decisions/023_sov_nuclear_bombs_decisions.txt:731-755. conduct_recovery_raid at :763-769 reuses rail_corridor_mission_active and collapse_operation without excluding the other rail action. Parent fix: make rail operation selection mutually exclusive and preserve one authoritative operation state.

20. **The retaliation window duration is outside the stated map range.** The constant is 45 days at common/script_constants/023_sov_nuclear_bombs_constants.txt:385-404, while docs/specs/023_sov_nuclear_bombs_specs/decision_map.md:1054-1074 specifies a 3-30 day retaliation window. Parent fix: reconcile the constant and localisation with the accepted specification.

21. **Requirement failures are not presented through custom trigger tooltips.** No custom_trigger_tooltip appears in common/decisions/023_sov_nuclear_bombs_decisions.txt. Long target/evolution/phase requirements are therefore exposed as generic disabled decisions or raw scripted conditions, including target selectors at :374-380 and final authorization at :513-520. Parent fix: add concise dynamic trigger tooltips for target, selected site, route, evolution, cooldown, and blocked-state reasons while keeping spendable costs separate.

22. **The event response/test distributions do not cover the specified response branches.** chaosx.nr23.120 currently contains accepted, partial, delay, and refusal options at events/023_soviet_nukes.txt:148-183, but the specification calls for public exposure, foreign support, and route-valid special responses. The test random pool in common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt:359-363 has only success, failure, and accident. Parent fix: reconcile the accepted response set and add the missing outcome riders before treating the probability surface as balanced.

### LOW

23. **A flat positive-political-power helper is unused.** common/scripted_triggers/023_sov_nuclear_bombs_event_triggers.txt:215-217 defines a simple political-power check with no current reference found. Remove it or wire it into a meaningful bounded requirement so stale helpers do not obscure audits.

## Decision category lifecycle notes

- Opening and doctrine decisions can coexist with the operational selector because event_can_open_command at common/scripted_triggers/023_sov_nuclear_bombs_event_triggers.txt:16-20 does not encode a phase-specific selector state.
- The selector saves a global state target and fires an event, but there is no universal close, replacement, or stale-target cleanup path.
- Phase transitions are represented by flags and variables, but visible actions are not consistently mutually exclusive after a phase advances.
- The category description is compact enough to avoid a prose wall, but it does not expose enough state to explain why an action is currently relevant or blocked.
- The ordinary category has no dedicated scripted GUI. No event-owned GUI handoff is required, and no GUI worker should be routed for this existing category.

## Cognitive-load and action-count audit

| Surface | Observed visible primary actions | Result |
| --- | ---: | --- |
| Phase 1 | Six including operational target selection | At ceiling; selector must not remain persistent |
| Phase 2 | Six including operational target selection | At ceiling; no spare action slot |
| Phase 3 | No more than six observed by stage | Conditional PASS, but selector persistence remains |
| Phase 4 | Up to seven including selector and response actions | FAIL |
| Phase 5 | Up to seven before certification and six after | FAIL before certification |
| Phase 6 | Up to eight including selector, hotline, retaliation, restraint, release, and moratorium actions | FAIL |
| Phase 7 | Up to seven or eight including depot selection and recovery actions | FAIL |
| Phase 8 | Up to five ordinary moratorium actions | Count PASS; selection persistence still unclear |
| Breakaway custody | Five progression actions | Count PASS; mission overlap and cleanup fail |

There are eight declared mission families, but no central proof that no more than three can be active. The likely overlaps are ultimatum plus strike preparation, rail plus joint custody, and repeated breakaway operationalization. Visible values lack a consistent explanation of cause, threshold, consequence, and player response, especially cumulative arsenal, posture/knowledge, selected target, and mission deadlines.

## Mission quality and lifecycle notes

| Mission | Owner/category/region | Requirement and duration | Success | Timeout/cancel | Main risk |
| --- | --- | --- | --- | --- | --- |
| sov_nuclear_bombs_proof_test_mission | SOV command category; selected owned test site | Valid SOV plus test_mission_active; 120 days | resolve_test | cancel_test plus event 102 on timeout; cancel_test on cancel | Handler is safe for test state but must not be reused by other reservations |
| sov_nuclear_bombs_ultimatum_response_mission | SOV command category; selected coercion target | Valid SOV plus ultimatum flag; 14 days | resolve_coercion_response | Same resolver for completion, timeout, and cancel | Delayed and partial paths can leave mission/target state active |
| sov_nuclear_bombs_strike_preparation_mission | SOV command category; selected limited-strike site | Valid SOV plus strike-preparation flag; 7 days | complete_strike_preparation | abort_and_recover on cancel; completion on timeout | Completion lacks exact route revalidation |
| sov_nuclear_bombs_retaliation_window_mission | SOV command category; selected enemy nuclear-major site | Valid SOV plus retaliation flag; 45 days | complete_retaliation_window | The same committing helper is used for cancel and timeout | Cancel can launch/commit; duration exceeds spec |
| sov_nuclear_bombs_rail_corridor_security_mission | SOV collapse-custody category; selected breakaway site/rail corridor | rail mission flag; 120 days | complete_rail_security | Completion on timeout; cancel clears only flag | Stale collapse_operation and overlap with joint custody |
| sov_nuclear_bombs_breakaway_operationalization_mission | Breakaway custody surface; transferred custody site | Mission flag only; 180 days | complete_breakaway | Cancel clears only flag | No current actor/crisis guard or progress cleanup |
| sov_nuclear_bombs_joint_custody_transfer_mission | Breakaway custody surface; transferred custody site | Mission flag only; 120 days | complete_joint | Cancel clears only flag | Can overlap rail and can retain target/progress state |
| sov_nuclear_bombs_dismantlement_inspection_mission | SOV command category; selected dismantlement site | Dismantlement flag and staged reservation; 180 days | complete_dismantlement | cancel_test on cancel; completion on timeout | Critical reservation leak and wrong cancel helper |

## Cost and requirement clarity

| Cost profile | Actual spendable types | Displayed profile | Audit |
| --- | --- | --- | --- |
| Command | Political power plus command power | Political power plus standard command power | PASS for count/icon style; verify exact amount |
| Security | Political power, support equipment, manpower | Political power, command power, support equipment | FAIL: wrong type and omitted manpower |
| Logistics | Light command power, trains, fuel | Standard command power, trains, fuel | FAIL: wrong command-power tier |
| Diplomatic | Political power, light command power, convoys | Political power plus light command power | FAIL: convoy omitted |
| Strategic | Political power, heavy command power, support equipment, fuel | Political power, heavy command power, manpower | FAIL: support equipment/fuel mismatch and fuel omission |

No profile exceeds four spendable types, and the visible strings use texticons rather than literal resource names. The parent must still correct the profile/content mismatch and ensure every spendable type is represented with its correct icon. Non-consumed requirements such as evolution, target ownership, war state, selected site, and cooldown should be separated into custom trigger tooltips instead of being blended into cost prose.

## AI, probability, and route-lock notes

- The probability auditor evaluated the four chaosx.nr23.120 option weights in scenarios P23_COERCE_ISOLATED_LOSING_MINOR, P23_COERCE_PROTECTED_STABLE_MINOR, P23_COERCE_UNTESTED_SECRET, and P23_COERCE_EMPTY_THREATS. Current weights are 35/25/20/20 in every scenario with no modifiers, so the picker has no scenario-sensitive ranking and cannot prove the required response behavior. Artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f7d1c9867b7cc28184df5e68319ac98b76cb29dd5a43f01827f93a9363d72114/d23fe99cec3f68a46f8a5d3dc864b7564014b33b18812ba322b94b9499c0a3cb/probability-e381a33e52820ee51ba98878.json. Render: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/aa0dfca86af13bb82ea53c206f8cda98764f4b593aeb771dd684d9fb53442352/acb53a7c375bf7c32f97ac5d28c1793b6911ef1f2051fb94ba75e2771bf1d862/probability-probability-e381a33e52820ee51ba98878-ranking.svg.
- The test random list evaluates 70/20/10 in all named test scenarios, including invalid-site input to the direct adapter. The adapter did not include the outer accepted-action/route gate, so this is arithmetic evidence only and not proof that an invalid site detonates. Artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c3c64b4db3d76e484b7eb0418587043374ee88845d549cd173cd998126e5d38b/fc1002b2ea995f32652684f0b1c6b7a77b2b63f3eee3e9302a62d6759567a6de/probability-8b56e767cef9cb4d3e976abc.json.
- Mission analysis found all eight missions available = always no, with score-only bases ranging from 0.20 to 1.00. These positive AI weights are not meaningful selection evidence if the missions are timeout-only. Artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ed58f74bdd83868820458576425861affbd01339a510593374d3bb971f57083c/87b459e4f60a6c9327c370a396a40d748e9892c299b977e11f5d6d5b2716e04e/probability-5996e42d0d5bd74b61b31976.json.
- decision_ai_will_do returned INTERNAL_ERROR, so no decision score, target dominance, or AI choice claim is valid. The probability sweep also stopped with PROBABILITY_SWEEP_RANGE_REQUIRED for the coercion base path. No probability_compare was appropriate because this audit applied no patch.
- Source-level route locks are strong for evolution disablement and exact test/collapse selectors, but the operational-major, limited-strike, active-mission, and custody-target issues above prevent a complete AI/route PASS.
- Current first-use source gating is conservative: Evo IV and the severe first-use conditions are present at common/scripted_triggers/023_sov_nuclear_bombs_event_triggers.txt:149-180. This is a source-level PASS only; the required scenario probability remains unresolved.

## Localisation and tooltip gaps

- Static decision name/desc references are covered, but no custom trigger tooltip is present in the decision file.
- The category header omits posture/knowledge and selected target/site/deadline context, contrary to docs/specs/023_sov_nuclear_bombs_specs/decision_map.md:16-25.
- Cost keys at localisation/english/023_soviet_nukes_l_english.yml:80-84 need exact profile correction.
- Always-available decisions such as partial settlement and demand adjustment provide no blocked reason or response-state guard.
- Long scripted requirements for target validity, evolution, war, cooldown, and selected site need concise dynamic localisation rather than raw disabled rows.

## Cleanup and exploit-risk notes

- Critical reservation leaks: dismantlement cancel.
- Critical action-on-cancel risk: retaliation cancel can commit the pending action.
- Repeatable integrity gain: partial settlement.
- Repeatable demand adjustment: no observed direction setter and no response consumption.
- Stale target/mission flags: delayed ultimatum, back down, breakaway cancel, rail cancel, and joint custody cancel.
- Possible self-hit accounting: own-state limited strike plus the on_nuke callback.
- Mission overlap/overwrite: ultimatum plus strike, rail plus joint custody, and recovery raid reuse of rail state.
- No free native-stockpile path was found for transferred breakaway devices; the custody-only runtime branch is a PASS.

## Required parent fixes

1. Fix the two critical cancel handlers first and add focused cleanup paths for every mission completion, timeout, cancel, target invalidation, actor invalidation, and disabled-evolution path.
2. Enforce the six-visible-primary-action cap and three-active-mission-family cap by phasing selectors and mutually excluding action families.
3. Make target routes fail closed, especially limited strike, operational-major checks, coercion owner/controller semantics, and exact strike completion.
4. Align localisation cost strings with the cost triggers/effects and verify texticon coverage for every spendable value.
5. Add concise custom trigger tooltips and a compact header state model with posture/knowledge, selection, phase, and deadline significance.
6. Reconcile the eight mission definitions with the decision map, including the orphaned production lifecycle and the 45-day retaliation duration.
7. Add scenario-sensitive event response/test outcomes and rerun the same named probability scenarios through chaosx_ai_probability_auditor, including a before/after probability_compare after any AI-weight patch.
8. Do not add a scripted GUI or focus tree for this audit. The existing ordinary category is not an event-owned dedicated GUI surface.

## Simplifications, omissions, and blockers

- No gameplay, localisation, or asset patch was applied.
- Balance sign-off is blocked by the decision probability adapter INTERNAL_ERROR, missing response scenarios, and the absence of a valid before/after patch for probability_compare.
- GUI visual sign-off is not claimed because the category is engine-owned, gui_inspect resolved zero Event 23 elements, and gui_render returned no actionable Event 23 category geometry.
- No live game validation was performed.
- The parent owns all fixes, integration, and final review.
