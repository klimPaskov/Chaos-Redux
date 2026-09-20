# IW-179 FSM decision and mission audit

Date: 2026-09-20.

Status: audited with a bounded source patch; IW-179 package completion is not claimed.

## Scope and guardrails

The audit covered the FSM package-local category, one founding mission, eight decisions, their directly called FSM Pacific trigger/effect helpers, cleanup, and English localisation.

The audited decision file is common/decisions/006_independence_wave_pacific_decisions.txt:287-443.

The directly inspected package-local trigger file is common/scripted_triggers/006_independence_wave_pacific_package_triggers.txt, including the FSM active-project and government-route helpers at lines 119-183 and the strategic-cost helpers at lines 190-207.

The directly inspected package-local effect file is common/scripted_effects/006_independence_wave_pacific_package_effects.txt, including strategic payment at lines 195-203, the FSM delegation adapter at line 492, and IW-179 cleanup at lines 972-1003.

The shared event-log, FORM-48, central allocator/Join/SCN-008, identity/portrait/flag evidence, unrelated Pacific packages, and live Hearts of Iron IV runtime were not changed or promoted.

## Severity-sorted findings

### Fixed P1: founding mission could publish success after capital loss

independence_wave_fsm_keep_island_federation_connected at common/decisions/006_independence_wave_pacific_decisions.txt:288-299 cancels on stable authority or lost capital at line 295.

Before the patch, the successful cancel_effect branch at line 296 checked the FSM package, setup receipt, and stable authority but not capital control, so stable authority plus lost capital could set independence_wave_fsm_founding_crisis_resolved.

The success branch now requires capital_scope = { is_controlled_by = ROOT } at line 296, matching the adjacent HBX/HAW founding-mission precedent.

Lost capital, lost receipt, package loss, or timeout now reaches the failure branch instead of publishing a stable founding result.

### Fixed P1: exact strategic stockpiles were rejected by the FSM affordability gate

The shared HAW/FSM helper can_pay_independence_wave_pacific_island_strategic_cost at common/scripted_triggers/006_independence_wave_pacific_package_triggers.txt:190-195 retains its pre-existing strict-greater contract and was not changed because HAW is outside this audit.

IW-179 now uses the package-local can_pay_independence_wave_fsm_pacific_island_strategic_cost helper at lines 200-207.

That helper requires the setup receipt and uses inclusive NOT = { value < cost } gates for 0.10 stability, 20 command power, 2,500 manpower, and 5 convoys, matching the exact debit in independence_wave_pacific_pay_island_strategic_cost at common/scripted_effects/006_independence_wave_pacific_package_effects.txt:195-203.

Both independence_wave_fsm_accept_protected_ocean_mandate at lines 398-416 and independence_wave_fsm_ratify_autonomous_federation_mandate at lines 418-442 call that same helper from available and custom_cost_trigger at lines 403-404 and 423-424.

### Fixed P1: autonomous federation mandate could start with an already-lost capital

independence_wave_fsm_ratify_autonomous_federation_mandate previously had a capital-loss cancel_trigger at line 429 but no capital-control requirement in available.

Its available block at line 423 now requires capital_scope = { is_controlled_by = ROOT }, so IW-179 cannot debit the strategic cost for a project that is already invalid at activation.

### P1 remaining: shared diplomatic-light payment can select the wrong transport at exact convoy equality

The four FSM decisions independence_wave_fsm_convene_inter_island_revenue_congress (line 302), independence_wave_fsm_settle_external_administration_accounts (line 334), independence_wave_fsm_ratify_federal_council_compact (line 350), and independence_wave_fsm_adopt_inter_island_constitution (line 382) use can_pay_independence_wave_diplomatic_light_cost from common/scripted_triggers/006_independence_wave_decision_triggers.txt:343-349.

That predicate accepts exactly 5 convoys through NOT = { has_equipment = { convoy < ... } } when no trains exist, but the directly called shared payment at common/scripted_effects/006_independence_wave_decision_effects.txt:156-166 chooses convoys only with has_equipment = { convoy > ... } and otherwise debits trains.

At exactly 5 convoys and no trains, the FSM decision can therefore pass its cost gate and enter a payment branch that does not match the accepted resource.

I did not patch the shared helper or create a duplicate FSM payment path because that would broaden this bounded IW-179 task into unrelated packages; the central payment owner needs to align the branch with the inclusive predicate.

### P1 remaining: the category can expose too many simultaneous primary actions

The category is visible only with the Event 006 local-content gate, FSM package predicate, and setup receipt at common/decisions/categories/006_independence_wave_categories.txt:584-591.

IW-179 setup enables all four government route flags at common/scripted_effects/006_independence_wave_pacific_package_effects.txt:768-771.

Before route selection, the category can expose the three common decisions at lines 302, 318, and 334, four government-route decisions at lines 350, 366, 382, and 398, and the autonomous mandate at line 418, for eight primary decision actions plus the founding mission.

The route decisions are visible before their stable-authority availability gate is met, and the autonomous mandate is visible before its stable-authority and recognition gates are met.

This exceeds the six-action ceiling and makes the player scan blocked policy rows rather than see a phased next action.

A safe fix needs accepted pacing/phasing design, such as delaying route rows or separating late route actions, so it was not invented in this bounded audit.

### P1 remaining: ordinary FSM decision timers are not individually receipt-cancelled

The founding mission mirrors independence_wave_iw_179_setup_complete in activation, cancel_trigger, and successful cancel_effect at lines 292, 295, and 296.

The eight ordinary FSM decisions use the receipt-gated category and the complete IW-179 cleanup, but their individual cancel_trigger blocks at lines 313, 329, 345, 361, 377, 393, 409, and 429 do not all include NOT = { has_country_flag = independence_wave_iw_179_setup_complete }.

The current source path clears the receipt during setup before projects are created and removes all FSM projects during independence_wave_cleanup_iw_179_micronesia, so no normal receipt-clearing-with-live-project caller was found.

If another adapter or future lifecycle path clears only the receipt while a timer remains active, an ordinary decision could still reach its package-guarded remove effect.

The parent should either prove receipt clearing is atomic with project cleanup or add the receipt-loss cancellation guard to all eight ordinary FSM decisions.

## Decision and mission lifecycle notes

independence_wave_fsm_keep_island_federation_connected is an auto-activated mission with available = { always = no }, a constant timeout, stable-authority success, capital/package/receipt cancellation, and explicit timeout failure.

The eight decisions have one days_remove timer each, manual upfront payment in complete_effect, visible result text in remove_effect, and failure effects on invalidation.

The active-project trigger at common/scripted_triggers/006_independence_wave_pacific_package_triggers.txt:149-160 enumerates the mission and all eight decisions, so the package serializes to one active project.

The IW-179 cleanup at common/scripted_effects/006_independence_wave_pacific_package_effects.txt:972-1003 removes the mission and all eight decisions, removes FSM ideas, clears the authority variable, clears lifecycle/route/project/founding flags, and restores the generic focus tree.

No free-unit loop, war-goal loop, core loop, repeated completion flag, or uncapped active-project loop was found in the audited surfaces.

## Cognitive-load notes

The category description at localisation/english/006_independence_wave_pacific_l_english.yml:36-37 is concise and communicates the federation-wide purpose.

The decision descriptions are one sentence each and explain the public action, while remove-effect tooltips at lines 95, 98, 101, 104, 107, 110, 113, and 116 explain the visible project result.

The category does not expose the current inter-island authority value, stable threshold, recognition gate, capital-control status, or route-lock state next to the action list.

The visible route rows therefore present blocked actions without a concise package-specific reason, and the eight-action maximum is the main cognitive-load defect.

No dedicated IW-179 scripted GUI exists in the audited scope.

## Mission quality notes

Owner: FSM/IW-179 package.

Category: independence_wave_fsm_micronesia_category.

Region: Micronesian island federation package; the mission itself does not use an invalid country target or external target pointer.

Requirement: FSM package, IW-179 setup receipt, and unresolved founding flags at activation.

Duration: constant:independence_wave_pacific_duration.founding_mission_days.

Success: stable inter-island authority while the package, receipt, and capital-control proof remain valid.

Failure: timeout, package loss, receipt loss, capital loss, or failure to establish stable authority.

Duplicate risk: low; the activation flags, active-project helper, and cleanup all enumerate one mission id.

## Cost and requirement clarity

The FSM cost palette is within the four-distinct-spendable-type hard cap.

The diplomatic-light actions use command power plus either convoys or trains through shared localisation and payment helpers.

The security-light actions use command power, infantry equipment, and support equipment.

The two FSM strategic actions use stability, command power, manpower, and convoys, exactly four types.

independence_wave_cost_pacific_island_strategic at localisation/english/006_independence_wave_pacific_l_english.yml:117-119 uses £stability_texticon, £command_power, £manpower_texticon, and £convoy_texticon with matching normal, tooltip, and blocked keys.

No fifth spendable cost is hidden in an effect or secondary panel.

The strategic inline string still shows four values, which exceeds the decision skill's three-value inline presentation limit even though it satisfies the four-type gameplay budget.

The diplomatic and security base, tooltip, and blocked cost keys are shared in localisation/english/006_independence_wave_decisions_l_english.yml:42,49,78-79,98-99 and all resolve.

Non-consumed requirements such as capital control, stable authority, recognition, living former host, route availability, and no active project remain separate from payment, but they have no dedicated concise FSM blocked-reason localisation.

## AI validity and route-lock notes

All nine weighted surfaces have ai_will_do: mission urgent at line 299; common actions at lines 315, 331, and 347; government routes at lines 363, 379, 395, and 411; autonomous delegation at line 431.

AI weights use centralized constants and the autonomous delegation has a host-collapse blocker/priority modifier without introducing a new target country.

The four government decision effects call the existing central independence_wave_select_government_route only after can_choose_independence_wave_fsm_government_settlement and their route-availability flags, so the central route lock remains authoritative.

No FSM decision exposes FORM-48 membership, promotes central attestation, changes allocators, calls Join/SCN-008, or invents identity/portrait/flag evidence.

The required probability audit was routed to chaosx_ai_probability_auditor agent 01a0c036-fd7a-7c42-9e6e-4a5f4e9637fc with all nine weighted ids.

The agent remained running through repeated waits without returning hoi4.probability_inspect, hoi4.probability_evaluate, hoi4.probability_sweep, or hoi4.probability_compare artifacts and was then shut down.

AI willingness and before/after probability conclusions are therefore unresolved; source inspection is not being substituted for the mandatory MCP probability evidence.

## Localisation coverage

All FSM name, desc, custom_effect_tooltip, category, and cost references resolve in the English localisation set.

All three cost families have base, _tooltip, and _blocked keys.

The inspected English localisation files retain UTF-8 BOM bytes EF-BB-BF.

No localisation file was changed because coverage was complete.

## MCP GUI evidence

The native decision surface is the shared countrydecisionview, not a dedicated FSM scripted GUI.

Read-only inspection used scenario iw179_fsm_decisions, emitted scenario iw179_fsm_decisions-generated-1, source revision 6c702d4c25e95933c84091b0fc2e2d6dfaa54762af91a822143c29a4aab26a69, and workspace mod_chaos_redux_ea3b2d67c2c0.

Inspection artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1ce55e56fd860b432708990a98278140b4cd741d555a7d348d1dc58189b48582/6a2a01b08042d325dbe299c5df27dfc654640fd250034989d2c75ef20869a2f0/gui-inspect.6c702d4c25e95933.json.

Matching render artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/397d44367a8a781890ca2bc55c286a9b4f1f5d87c380f87d08bbe82d9d756820/cec4ef299da81ef387f5cec385189e682bd03d97afa1ed2aebffc5d09b065c2e/countrydecisionview-full.png.

Render validation artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/903a62334140bca1bf3587b7f3f881369b6c85a7923ee25e6cb3b0eebf540acf/4675f447b93908d0ff6b06a5aa91bcd64c729a7c36feaf173d0e823c5a5fd5d8/countrydecisionview-validation.json.

The read-only shared-window render reports GUI_ACCIDENTAL_CLIPPING, zero-sized shared controls, and partial sprite modelling in the offline renderer.

These are shared game:interface/countrydecisionview.gui findings, not an IW-179-owned GUI source defect, and no GUI source was changed.

## Validation

The scoped source assertions confirmed four FSM strategic helper call sites, the founding-mission capital guard, inclusive FSM strategic gates, and all eight cleanup decision removals.

The English localisation scan found no missing FSM display keys or cost base/tooltip/blocked keys.

The inspected English localisation files were checked for the required UTF-8 BOM.

Scoped git diff --check produced no whitespace errors.

The offline Paradox wiki pages consulted were Decision modding, Effects, Triggers, Localisation, Data structures, Scopes, Modifiers, On actions, Event modding, Idea modding, and AI modding.

The installed vanilla documentation consulted was documentation/effects_documentation.md, documentation/triggers_documentation.md, and documentation/script_concept_documentation.md.

Vanilla decision precedents consulted included common/decisions/BEL.txt custom-cost payment/cancellation patterns and the adjacent Pacific HBX/HAW founding mission implementations in the repository.

The required probability evidence was skipped because the delegated auditor route returned no artifacts before shutdown.

Live-game validation was not run because AGENTS.md assigns runtime validation to the user.

## Changed files and behavior handoff

Changed gameplay files:

- common/decisions/006_independence_wave_pacific_decisions.txt: capital-control requirement in FSM founding success, FSM strategic helper call sites, and autonomous mandate activation gate.
- common/scripted_triggers/006_independence_wave_pacific_package_triggers.txt: new receipt-gated inclusive IW-179 strategic affordability helper.

Changed documentation file:

- docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_iw179_decision_mission_audit_2026-09-20.md.

No localisation, central route, allocator, event-log, FORM-48, Join, SCN-008, identity, portrait, flag, or unrelated-package file was changed.

Before: exact strategic resources could be rejected, stable authority plus lost capital could mark the founding crisis resolved, and the autonomous mandate could start after capital loss.

After: exact IW-179 strategic resources qualify through a receipt-gated inclusive helper, lost capital routes the founding mission to failure, and autonomous activation requires capital control.

Remaining blockers are listed above; this handoff is an audit and bounded patch record, not a package-completion report.
