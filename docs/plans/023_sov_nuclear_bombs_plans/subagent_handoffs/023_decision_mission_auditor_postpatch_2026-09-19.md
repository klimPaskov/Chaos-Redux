# Event 23 post-patch decision and mission audit

Date: 2026-09-19.

Auditor: Chaos Redux decision and mission auditor.

Disposition: source audit complete for the requested surfaces; visual GUI acceptance is blocked, and weighted AI evidence is partial.

Source patch status: no gameplay, decision, mission, effect, trigger, localisation, or GUI source was changed by this audit.

HOI4 launch status: Hearts of Iron IV was not launched.

## Scope and references

Inspected the current post-patch coding prompt, decision map, common/decisions/023_sov_nuclear_bombs_decisions.txt, decision category, Event 23 event file, triggers, effects, cost helpers, scripted localisation, localisation, and prior decision and probability handoffs.

The current decision file contains 68 decision-like entries and 13 mission declarations.

Read the required offline Paradox wiki pages for data structures, triggers, effects, modifiers, localisation, scopes, on actions, events, decisions, ideas, AI, interface, and scripted GUI modding.

Read the installed vanilla decision, scripted GUI, triggers, effects, and script-concept documentation and inspected the vanilla SOV decision and scripted-GUI precedents.

The coding prompt and decision map require no more than six primary visible actions per phase, no more than three active missions per phase, no more than four spendable cost types per action, selected-target or selected-site management, and invalid exact targets that fail closed without random redirection.

## Severity-ranked findings and dispositions

| ID | Severity | Finding and evidence | Disposition |
| --- | --- | --- | --- |
| B1 | Blocker for visual acceptance | Native countrydecisionview GUI inspect reports GUI_ACCIDENTAL_CLIPPING with a 550x1080 surface clipped to 0x0, zero-size production_header_bg, decisionview_title, close_button, and decision_grid_container, and partial Lua sprite execution. The production render reports the same clipping and zero-size diagnostics. | Keep visual acceptance incomplete. Repair or replace the production MCP representation before accepting alignment, spacing, clipping, overflow, assets, text, states, or click regions. Do not dismiss this as renderer variance. |
| B2 | Blocker for full AI acceptance | The probability route is available, but decision_ai_will_do has no dedicated candidates, mission_ai_will_do is score-only with normalizedProbability=false, and most Event 23 scenarios are partial with unresolved nested state. | Treat base values and modifier traces as exact source evidence only. Keep AI balance and route selection unaccepted until unresolved country, state, event-target, war, technology, and dynamic-variable inputs are bound. |
| H1 | High | Back Down is visible while an ultimatum response mission is active because common/decisions/023_sov_nuclear_bombs_decisions.txt:576-581 excludes test, strike-preparation, and retaliation-window missions but not sov_nuclear_bombs_ultimatum_response_mission_active or the shared no-active-project trigger. Its effect clears the response mission without setting the standard cancellation receipt flag at common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt:2373-2400. | Add the response-mission guard, or expose a separately named cancellation action. If intentional, route through sov_nuclear_bombs_cancel_ultimatum_response and localise the consequence. |
| H2 | High | Reserve dispersion stores the selected destination at common/decisions/023_sov_nuclear_bombs_decisions.txt:190-215, but its completion effect clears the source target and chooses a source with random_owned_controlled_state at common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt:1984-2035. | Resolve whether both endpoints must be selected. If yes, add a source selector and fail closed. If automatic source selection is intentional, state it clearly because the player cannot see which site supplies the device. |
| M1 | Medium | Several available blocks are weaker than visible or target-root blocks. collapse_command omits collapse_active at line 126; select_disputed_depot omits collapse_active at line 827; destroy_compromised_site omits collapse, imminent, technical-denial, transferred-device, non-operationalized, and return-request checks at lines 910-911; reduce_to_remote_demonstration only checks a valid test site at lines 663-664; dismantle_batch only checks an assigned device at lines 993-994. | Mirror lifecycle and phase requirements in available and custom tooltips, except for deliberately explicit cancellation or in-flight controls. |
| M2 | Medium | Invite Observers has no no-active-project guard and available = always = yes at lines 1003-1014, so it can overlap the dismantlement inspection mission at lines 1366-1380. | Add the shared project lock or document this as an intentional concurrent action. |
| M3 | Medium | The category header shows only operational devices, readiness, integrity, posture, and knowledge at localisation/english/023_soviet_nukes_l_english.yml:93. Existing phase, site, target, and deadline helpers are not consumed. | Add concise phase, selected-site, selected-target, and actual remaining-deadline context to the ordinary category description or decision tooltips. |
| M4 | Medium | The target tooltip says a registered state is required at localisation/english/023_soviet_nukes_l_english.yml:171, but sov_nuclear_bombs_event_state_is_valid_command_target at common/scripted_triggers/023_sov_nuclear_bombs_event_triggers.txt:153-170 does not require registration. | Change the tooltip to valid command state or narrow the trigger where registration is intended. |
| M5 | Low to medium | Breakaway security requires a positive division count but does not check force strength, supply, or corridor readiness. | Add a narrow existing strength or supply check if intended, or document one division as the accepted minimum. |
| L1 | Low | Hotline partner selection uses random_country at common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt:1559-1573. | This is a diplomatic random choice rather than a selected-site redirect. Keep it documented or replace it with explicit partner selection if player agency is required. |

## Action cap and category lifecycle

The source-level action cap passes under the intended phase gates, although B1 prevents production-render confirmation of actual row layout.

Opening exposes four mutually exclusive custody doctrine choices.

Custody peaks at six actions after doctrine selection: operational command, doctrine reform, stockpile audit, storage hardening, reserve dispersion, and atomic moratorium.

Production peaks at six actions because delivery-crew preparation is hidden after crews are ready and command exercise is hidden after completion.

Testing keeps survey separate from the three preparation choices and hides ordinary project actions during the test.

Coercion reaches six actions in the open-target state: close, private signal, public ultimatum, wartime demonstration, limited strike, and Back Down.

Authorization remains below six in each gate combination because certification and safety overrule precede final authorization, while redirect, reduction, and abort are in-flight controls.

Collapse recovery exposes at most six post-selection actions: recall, rail security, joint custody, recovery raid, disablement, and compromised-site destruction.

Moratorium exposes at most six ordinary actions: reserve sealing, dismantlement-site selection, dismantlement, observers, reciprocal restraint, and reactivation.

Breakaway custody exposes at most five actions and technical access, command formation, and delivery integration are sequential.

The category declaration is a normal native decision category with a static picture and no Event 23 scripted-GUI window, consistent with the coding prompt's no-full-scripted-GUI scope.

The shared no-active-project trigger at common/scripted_triggers/023_sov_nuclear_bombs_event_triggers.txt:921-948 covers pending decisions, all ordinary active missions, the shared breakaway mission flag, hotline, and verification flags.

All three breakaway starter helpers at common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt:2867-2937 require no-active-project and the shared breakaway mission flag.

Invite Observers and Back Down are not safely serialized in their current form. Test evacuation, prepared-test cancellation, strike reduction, strike abort, retaliation standdown, and release suspension appear to be deliberate in-flight controls and should remain explicitly documented.

Collapse sequencing passes in source. open_collapse_recovery clears collapse_board_seen at common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt:1826-1846, chaosx.nr23.110 sets it at events/023_soviet_nukes.txt:246-258, and select_disputed_depot requires it at common/decisions/023_sov_nuclear_bombs_decisions.txt:824-827.

The prior random breakaway custody finding is resolved. The custody selector uses state_target and exact FROM validation at common/decisions/023_sov_nuclear_bombs_decisions.txt:1067-1077, and the effect applies only to the saved selected state at common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt:3032-3047.

The prior breakaway starter lock finding is resolved. The three start helpers share no-active-project and one active mission flag.

The prior Soviet delivery-certification endpoint finding is resolved for selected Soviet endpoints. Targeted and selected-test delivery wrappers require both crew certification and the exact selected endpoint at common/scripted_triggers/023_sov_nuclear_bombs_event_triggers.txt:100-146.

## Cognitive-load notes

The category is within the hard six-action cap, but custody and production sit at the limit rather than the preferred three-to-five range.

Operational devices, readiness, integrity, posture, and knowledge have clear significance in decision descriptions and shared triggers.

Phase, selected site, selected target, and active deadline significance is not visible in the category header even though those values control action visibility.

The deadline localisation reports constant nominal durations rather than remaining time.

Decision descriptions are generally concise, but Back Down does not explain that its current effect can erase an active response window.

The strategic cost tooltip does not explicitly mention its command-power component.

The static category picture cannot be accepted for visual quality while the production render is clipped to zero.

## Mission quality notes

All 13 mission declarations are non-selectable, unavailable by default, explicitly activated, duration-backed, and equipped with completion, cancellation, timeout, and AI hooks.

The intended shared project lock allows one active project mission at a time, which is below the three-active-mission ceiling. No mod-scoped runtime state was available to prove this through gameplay or MCP.

| Mission family | Owner, category, and region | Requirement and duration | Completion, failure, cancellation, and duplicate risk |
| --- | --- | --- | --- |
| Device assembly | SOV; production; national stockpile | Production-active flag; production duration | Normal completion and timeout resolve production; invalid actor cancels; shared production flag serializes |
| Delivery crews | SOV; production/delivery; national network | Delivery-crews-active flag; delivery duration | Completion certifies crews; invalid actor cancels; shared flag serializes |
| Command exercise | SOV; production/command; national network | Command-exercise-active flag; exercise duration | Completion resolves exercise; invalid actor cancels; shared flag serializes |
| Proof test | SOV; testing; selected test state and endpoint | Test-active flag and valid selected site; test duration | Resolver handles success, partial, failure, or accident; invalid site cancels |
| Ultimatum response | SOV; coercion; selected target | Response-active flag and valid response target; response duration | Resolver handles response and timeout; invalid target cancels; H1 bypasses normal serialization |
| Strike preparation | SOV; authorization; selected target and reserved device | Strike-preparation flag and valid prepared chain; strike duration | Completion prepares authorization; invalid chain aborts and recovers |
| Retaliation window | SOV; retaliation; major target or exchange context | Retaliation-window flag and target or standdown gate; hotline duration | Completion resolves retaliation; invalid crisis or target cancels |
| Rail security | SOV; collapse recovery; selected breakaway depot and corridor | Rail flag, route, and security force; rail duration | Completion resolves recall, rail, or raid; invalid route or force cancels |
| Breakaway technical, command, and delivery stages | Breakaway actor; custody; one selected depot and endpoint | One shared active flag plus stage-specific prerequisites and durations | One shared resolver completes or fails each stage; crisis/site cancellation prevents duplicate stages |
| Joint custody transfer | SOV; collapse recovery; selected breakaway depot | Joint-custody flag and selected site; transfer duration | Completion resolves transfer; invalid actor or site cancels |
| Dismantlement inspection | SOV; moratorium; selected registered site | Dismantlement flag and assigned device; dismantlement duration | Completion resolves dismantlement; invalid device cancels; M2 can overlap |

Most timeout effects call the normal resolver rather than a separate failure effect, so timeout failure semantics live in the helper implementations.

## Cost and requirement audit

The four-type cap passes for every action.

| Profile | Spendable types | Texticons |
| --- | --- | --- |
| command | Political power and command power | £pol_power and £command_power |
| security | Political power, support equipment, and manpower | £pol_power, £support_equipment_text_icon, and £manpower_texticon |
| logistics | Command power, trains, and fuel | £command_power, £GFX_train_texticon, and £GFX_fuel_texticon |
| diplomatic | Political power, command power, and convoys | £pol_power, £command_power, and £convoy_texticon |
| strategic | Political power, command power, support equipment, and fuel | £pol_power, £command_power, £support_equipment_text_icon, and £GFX_fuel_texticon |

Every displayed spendable cost uses a texticon and no cost string spells out a resource name.

The custom cost triggers and spend effects use the same profile family, and the decision file has 64 custom-cost triggers.

The strategic tooltip should explicitly mention command power.

The map describes dynamic costs and durations, while the implementation uses centralized fixed profile constants and fixed mission durations. This is a design-depth follow-up, not a four-type violation.

## Targeting, delivery, AI, and cleanup

Normal state-target decisions use state_target, target_trigger, and exact FROM scopes.

Breakaway custody, collapse depot selection, test survey, hardening, reactor, dispersal destination, command target, and strike redirect retain selected states through global event targets.

Soviet delivery crew certification is both delivery_crews_ready and delivery_crews_certified at common/scripted_triggers/023_sov_nuclear_bombs_event_triggers.txt:100-103.

Targeted and selected-test delivery wrappers require certification and revalidate the exact endpoint at lines 128-146.

Public test, wartime demonstration, limited strike, major strike, and retaliation therefore have source-level certification and exact-endpoint gates.

Random state selection remains in bounded setup for initial storage sites, test state, reactor queue, and reserve allocation.

Random state selection also remains after a player-facing reserve-dispersion action, which is H2. The generic action-source fallback at common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt:701-708 is an additional fail-open risk if no selected source exists.

All 68 decisions and 13 missions have ai_will_do blocks.

Selected-site cleanup is handled by the shared selected-state clear helper, breakaway completion clears its shared mission flag and progress stage, rail cancellation clears its mission and selected state, and joint custody and dismantlement have completion and cancellation paths.

No free-bomb, equipment-farming, war-goal-spam, core-spam, or obvious cooldown loop was found in the inspected paths.

## Probability-auditor evidence

The required chaosx_ai_probability_auditor completed a read-only pass.

First MCP route was hoi4.probability_inspect. decision_ai_will_do returned PROBABILITY_SOURCE_DISCOVERED with no dedicated candidates. mission_ai_will_do returned PROBABILITY_SOURCE_INSPECTED with 81 discoverable surfaces, adapter score_only, and normalizedProbability=false.

Current source revision was 696ebb4c1c965776137282006f4f92782ce7d9d214cb832d13a9797436a93a36 with source hash 782063ea23ee0f52de69fd29d372429f26f85334a039e120f57b002453e51fc4.

Inspect artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bb43b7717f146e3b5946c078c004ae67ec34b74a8f399ed482cc794566ab9fe6/ec588b04cffb72c928946fb00650b1dde4f9818e1a96336e21d1db15b9145192/probability-inspect-782063ea23ee0.json.

Target, limited-use, profile, first-use, coercion, retaliation, and collapse scenario groups returned PROBABILITY_ANALYZED_PARTIAL with unresolved nested state. Target artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2be69005ea844873ed1f77466f22aad08c67e3c13db09c920565541aa84d88b5/510f38e34b92d05d2029a40db2e666f00d1950220cb2be269e36624bb5324880/probability-3fabb6631ed4fbbc1c9fcd3e.json.

The breakaway mission-stage pool returned PROBABILITY_ANALYZED with three candidates, zero unresolved outcomes, raw score zero, and PROBABILITY_OUTCOME_NEVER_ELIGIBLE because all three mission declarations use available = always = no. Artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8d9395b7e685beac31d08773e9aacc121b69665477aa772827a081a2e2633559/30104e17c5fc0d61713ceab8aab7b84bb3e2a5c8cd4d6f1d1c5a3edc942c1509/probability-55d1bd85aed214b082ed14ef.json.

The auditor found an unreachable adjust-demand AI modifier requiring demand greater than maximum, while availability requires demand less than maximum.

The requested target ordering by military concentration, logistics node, industrial complex, populated center, and remote demonstration was not encoded directly and remained unresolved.

Collapse weighting is phase-sensitive but unresolved under bound targets. The traced imminent-operationalization modifiers were 1.80 for recovery raid and 2.00 for disable devices while negotiation remained 1.00.

First-use route checks exclude atomic moratorium, but release_orders_suspended is not excluded by the first-use gate itself and is only handled later by authorization and prepared-strike triggers.

The test random list is structurally complete with four entries and weights 60/20/12/8, but dynamic test weights were VALUE_UNRESOLVED.

Probability compare, simulate, sequence, and non-degenerate sweep conclusions were skipped because no before/after source pair, explicit uncertain-input distributions, complete cadence contract, or sweep range existed.

## Localisation, tooltip, MCP failures, and validation

Decision and mission name and description keys were found in the Event 23 English localisation file, including the shared breakaway mission family.

The target-state tooltip mismatch, Back Down lifecycle wording, nominal deadline wording, and unused category helper localisation remain open as described above.

No hoi4.decision_inspect route is exposed by the installed MCP service.

Native GUI inspect returned GUI_INSPECTED with status ok, validation passed, 5 inspected elements, and a complete source graph. Artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/94f97e0a268247bc0194eae2230bba6eced9a5f0528cdc7224fc19eaaad9a08e/ca26d9f399bfe2005549c8a86d6ea1b9de83dc50c135cf56c84a0c5a09f1d2b8/gui-inspect.fc4e9f0b096e7613.json.

Native GUI render returned GUI_RENDERED for 1920x1080 and 1280x720 with the requested normal, hover, selected, locked, disabled, warning, active, completed, empty-list, full-list, long-text, and missing-localisation states. Principal artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/397d44367a8a781890ca2bc55c286a9b4f1f5d87c380f87d08bbe82d9d756820/2aede93fec931960235d98093c9e264502808c1e74f36ae79d706b13d74724f7/countrydecisionview-full.png.

The custom window probe for sov_nuclear_bombs_command_category returned GUI_INSPECTED with zero inspected elements and validation false after graph and validation diagnostic truncation. Dropped diagnostics included GUI_WINDOW_MISSING and GUI_UNRESOLVED_REFERENCE. Artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/74055e82feef2d1e574826f18a7e3eeff553c78898a8991a1608035ee0e9ea6b/3c83bcdb71f052f41a005f0eea0bbee4d74308320503ac2fd8fa6123b4f4a72e/gui-inspect.4de8a2274025b4d3.json.

Event inspect and render returned EVENT_INSPECTED_PARTIAL and EVENT_RENDERED_PARTIAL with vanilla-bounded scans, validation false, and no mod-scoped Event 23 lifecycle graph. Scan artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fae7286c0d10e81679e052972876630155d547e592657d9cb5c87cf4e228bbfd/57fbdd2609d548b314562971a8d5ae0f40e8b881117816014e9ba458695e72c5/event-scan-3ddf1e273e51.json.

## Concrete recommendations

1. Guard Back Down against the active ultimatum-response mission and use dedicated cancellation bookkeeping for any intentional abort.

2. Decide whether reserve dispersion needs an explicit source selector and remove the runtime random source if it does.

3. Align visible, target-root, available, custom tooltip, and cancel predicates for the M1 availability mismatches.

4. Add no-active-project to Invite Observers or document it as a deliberate concurrent action.

5. Correct the registered-state tooltip or narrow the shared command-target trigger.

6. Add concise phase, selected endpoint, and real remaining-deadline context.

7. Mention command power in the strategic cost tooltip.

8. Resolve the unreachable demand modifier, bind the unresolved target and collapse contexts, and rerun the named probability scenarios before accepting AI balance.

9. Repair the native countrydecisionview MCP render before accepting GUI quality.

## Remaining issues, omissions, and handoff

No gameplay source was patched, so all findings remain recommendations for the parent implementation owner.

The source-level action cap, cost cap, selected breakaway custody, Soviet delivery certification, collapse sequencing, and breakaway starter serialization checks are substantially satisfied.

The audit remains incomplete for production GUI acceptance and full AI probability acceptance because of B1 and B2.

H1 and H2 require parent review before final completion, with H1 affecting cancellation bookkeeping and H2 affecting exact-site player trust.

Live HOI4 validation was skipped because the user prohibited launching HOI4.

Handoff path: docs/plans/023_sov_nuclear_bombs_plans/subagent_handoffs/023_decision_mission_auditor_postpatch_2026-09-19.md.
