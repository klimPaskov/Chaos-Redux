# Event 23 decision and mission auditor final current

Disposition: implemented with bounded patches.

Audit date: 2026-09-05.

## Scope and source review

I read every file under docs/specs/023_sov_nuclear_bombs_specs/, including the decision map, decision-mission prompt, probability scenarios, accepted objective, and all specification, research, integration, asset, super-event, achievement, technology, DLC, and catalog notes.

I also read AGENTS.md, the decisions, events, and subagents skills, the scripted-GUI skill for the ordinary decision-tab evidence contract, the required offline Paradox wiki pages, and the relevant vanilla decision and documentation precedents.

The audited surface is Event 23 root chaosx.nr23.1 and the ordinary category in common/decisions/023_sov_nuclear_bombs_decisions.txt.

## Issue list sorted by severity

| Severity | Finding | Disposition |
| --- | --- | --- |
| P0 | No invalid strike-authorization route was found in the owned decision surface. | The final authorization remains separate from target preparation, and the runtime path read-only review rechecks the exact prepared strike, major-exchange gate, and valid target before the shared action. |
| P1 | Several command, custody, production, and target actions could remain available during an active project or against a prohibited major target. | Patched with phase, actor, active-project, selected-target, and route guards. |
| P1 | The test-evacuation decision was unreachable because it required no active project while requiring the active test mission. | Patched to require test preparation plus the active test mission and to cancel when the test mission ends. |
| P1 | Reciprocal stand-down was unreachable because its prior no-active-project and no-retaliation conditions contradicted its hotline and retaliation-window lifecycle. | Patched to require the hotline and retaliation-window pair and to use the existing restraint and verification effects. |
| P1 | The collapse site selector could remain visible after a site had been selected, creating an extra primary surface. | Patched to close the selector after sov_nuclear_bombs_collapse_site_selected. |
| P1 | A generic breakaway operationalization mission duplicated the three stage-specific mission definitions. | Removed the duplicate engine mission block while retaining the shared family name, shared active flag, and three exact stage mission identifiers. |
| P2 | Every mission needed a stale actor, target, or site cancellation path. | Added cancel_trigger coverage to all 13 surviving mission definitions. |
| P2 | The decision probability adapter is unavailable in the installed MCP service. | The required auditor was run, the fallback mission adapter and bounded breakaway comparison were recorded, and no AI weight was changed. |
| P2 | The production GUI render route timed out twice after 180 seconds. | The ordinary decision surface was inspected read-only; no Event 23 scripted GUI exists and no GUI rewrite was authorized or needed. |
| P2 | Cost helpers use strict greater-than checks against the displayed amount. | Unresolved outside this ownership boundary because the helper file is not an owned decision/localisation file; the parent should decide whether to change helper semantics or display policy. |

## Changed file and exact identifiers

Only common/decisions/023_sov_nuclear_bombs_decisions.txt was patched for gameplay. The Event 23 localisation file was not edited because all audited identifiers already resolve.

The bounded changes are:

- sov_nuclear_bombs_centralize_release_authority and sov_nuclear_bombs_delegate_emergency_retaliation now require a valid actor, the custody phase, no active project, and their intended authority/network prerequisites.
- sov_nuclear_bombs_install_stronger_authentication now requires a valid actor, the production phase, no active project, and the uncompleted authentication state.
- sov_nuclear_bombs_prepare_instrumented_proof_test, sov_nuclear_bombs_prepare_concealed_field_test, and sov_nuclear_bombs_prepare_public_test now hold the no-active-project lock through the full preparation path.
- sov_nuclear_bombs_select_coercion_target, sov_nuclear_bombs_send_private_signal, sov_nuclear_bombs_issue_public_ultimatum, sov_nuclear_bombs_stage_wartime_demonstration, sov_nuclear_bombs_prepare_limited_strike, sov_nuclear_bombs_accept_partial_settlement, sov_nuclear_bombs_adjust_demand, and sov_nuclear_bombs_raise_demand reject a selected major controller for the ordinary coercion route.
- sov_nuclear_bombs_collapse_command now closes after site selection.
- sov_nuclear_bombs_recall_devices, sov_nuclear_bombs_secure_rail_corridor, sov_nuclear_bombs_negotiate_joint_custody, sov_nuclear_bombs_conduct_recovery_raid, sov_nuclear_bombs_disable_devices, and sov_nuclear_bombs_destroy_compromised_site now require a valid selected collapse site where their action uses that site.
- sov_nuclear_bombs_breakaway_attempt_technical_access, sov_nuclear_bombs_breakaway_form_command, and sov_nuclear_bombs_breakaway_integrate_delivery now require the crisis, the exact prior stage, a selected site valid for the actor, and no active stage mission, with delivery also requiring local delivery capability.
- sov_nuclear_bombs_breakaway_request_return now respects the no-active-project lock.
- sov_nuclear_bombs_strengthen_test_evacuation is reachable only during a prepared active test and cancels when the test mission or actor becomes invalid.
- sov_nuclear_bombs_propose_reciprocal_standdown is reachable during the hotline and retaliation-window pair, with the existing restraint and pending-state guards.
- The generic sov_nuclear_bombs_breakaway_operationalization_mission block was removed. The surviving stage identifiers are sov_nuclear_bombs_breakaway_technical_access_mission, sov_nuclear_bombs_breakaway_command_formation_mission, and sov_nuclear_bombs_breakaway_delivery_integration_mission.
- All surviving mission blocks have activation, available = { always = no }, a dynamic days_mission_timeout, complete_effect, cancel_trigger, cancel_effect, timeout_effect, and ai_will_do.

The decision source currently contains 67 decisions and 13 mission definitions inside the Event 23 category. The file was an untracked shared implementation artifact at audit start, so it was not staged or committed; committing it would capture pre-existing parent implementation beyond this bounded patch.

## Before and after behavior

| Surface | Before | After |
| --- | --- | --- |
| Authority, custody, and authentication actions | Some actions used unconditional availability or lacked the active-project lock. | Phase, actor, lifecycle, and duplicate-state checks prevent unrelated projects from being started over one another. |
| Test preparation and evacuation | Test preparation could start without the full stale-project guard, while evacuation contradicted its own active-mission requirement. | Preparation is locked to an idle project state, and evacuation is a reachable active-test support action with cleanup. |
| Ordinary coercion | The generic coercion helper admitted major controllers to the minor/breakaway route. | The selected state must be controlled by a non-major for ordinary coercion; major exchange remains on its dedicated gate. |
| Collapse command | Site selection could remain open after selection. | The selector closes after the selected site is recorded, preserving the primary-action cap. |
| Breakaway operationalization | A generic mission block duplicated stage-specific mission blocks. | One shared visible family uses three stage-specific engine definitions and one active flag, with exact stage durations. |
| Mission invalidation | Mission blocks lacked local cancellation conditions. | Actor, target-response, prepared-strike, test-site, breakaway-site, and assigned-device invalidation cancel through existing cleanup effects. |
| Reciprocal stand-down | Its availability conditions were mutually exclusive with its intended hotline lifecycle. | It appears during the active hotline and retaliation-window state and feeds the existing restraint verification flow. |

## Decision category lifecycle notes

Event 23 is an ordinary decision category with one static picture and no Event 23 scripted GUI. The source and localisation provide a concise phase/site/target/deadline/readiness/integrity header rather than a wall of implementation text.

The opening phase presents the custody-doctrine choice and the operational command selector. The custody phase presents audit, hardening, dispersal, centralization, and delegation actions around the selected storage state.

The production phase presents reactor, assembly, delivery-crew, command-exercise, and authentication actions. Production missions use dynamic duration constants and do not create a second visible project while active.

The test phase presents site survey and three distinct test-preparation choices. During an active test, the evacuation support decision is reachable, and its visibility is intentionally separate from the ordinary idle-project actions.

The coercion phase first records one exact state target. The selector then closes, and the player sees the target-response actions, demonstration, limited-strike preparation, settlement, demand adjustment, and close/back-down controls according to their state flags.

The authorization phase keeps certification, overrule, authorization, hold, redirect, remote demonstration, and abort as separate deliberate actions. Strike preparation does not itself authorize a detonation.

The retaliation phase uses the hotline, reciprocal stand-down, limited response, reserve preservation, and major-target retaliation surfaces. Reciprocal stand-down is a support action inside the active hotline lifecycle rather than an idle-project action.

The collapse phase first selects one exact site and then presents recall, rail security, joint custody, recovery or disablement, and ledger restoration actions. The selector close guard prevents the selection control from adding a seventh primary surface.

The moratorium and dismantlement phase presents preservation, sealing, restraint, reactivation, and inspection actions only under their corresponding flags and cooldown/validity conditions.

The source audit found no intended state with more than six visible primary decision surfaces. The three breakaway stage mission definitions share one active operationalization family and are counted as one family under the accepted objective. Phase and active-project guards keep the intended simultaneous mission-family count at three or fewer.

## Cognitive-load notes

The raw source count is 80 category entries, but phase and lifecycle gating means the player does not scan all 67 decisions and 13 engine mission definitions at once. The primary surfaces are organized by opening, custody, production, test, coercion, authorization, retaliation, collapse, and moratorium lifecycle.

Player-facing values include phase, selected site, selected target, target response, deadline, readiness, stockpile, integrity, credibility, demand, route capability, and device assignment. Their significance and response are localized in the category header, decision names, custom requirement tooltips, or effect text; no new raw number dump was added.

The ordinary decision surface does not need an extra tab or scripted GUI. A selected target or site is carried by an event target and every relevant completion/cancel path rechecks that target or site rather than silently redirecting to a new one.

## Mission quality notes

All missions are owned by the SOV Event 23 category. They are country-level mission entries with a global category context and an exact state/target binding wherever the mechanic requires one. Each uses a dynamic duration constant, explicit completion, explicit timeout routing, and explicit cancellation.

| Mission identifier | Requirement and region binding | Duration | Success, timeout, and failure handling | Duplicate risk |
| --- | --- | --- | --- | --- |
| sov_nuclear_bombs_device_assembly_mission | Production active flag; Soviet actor; production context. | sov_nuclear_bombs_duration.production_mission | Complete and timeout use sov_nuclear_bombs_complete_production_mission; invalid actor cancels through sov_nuclear_bombs_cancel_production_mission. | None; one production family. |
| sov_nuclear_bombs_delivery_crews_mission | Delivery-crews active flag; Soviet actor; route context. | sov_nuclear_bombs_duration.delivery_crews_mission | Complete and timeout use sov_nuclear_bombs_complete_delivery_crews; invalid actor cancels. | None; no generic duplicate. |
| sov_nuclear_bombs_command_exercise_mission | Command-exercise active flag; Soviet actor; delivery/command context. | sov_nuclear_bombs_duration.command_exercise_mission | Complete and timeout use sov_nuclear_bombs_complete_command_exercise; invalid actor cancels. | None. |
| sov_nuclear_bombs_proof_test_mission | Active proof test and exact selected test site valid for the Soviet actor. | sov_nuclear_bombs_duration.test_mission | Complete and timeout resolve through sov_nuclear_bombs_resolve_test; invalid actor or site cancels through sov_nuclear_bombs_cancel_test. | One test family. |
| sov_nuclear_bombs_ultimatum_response_mission | Active ultimatum response and exact selected target response valid. | sov_nuclear_bombs_duration.ultimatum_response | Complete and timeout resolve through sov_nuclear_bombs_resolve_coercion_response; invalid actor or target response cancels. | One coercion-response family. |
| sov_nuclear_bombs_strike_preparation_mission | Active preparation and exact prepared strike remains valid. | sov_nuclear_bombs_duration.strike_window | Complete and timeout use sov_nuclear_bombs_complete_strike_preparation; invalid preparation cancels through sov_nuclear_bombs_abort_and_recover. | Separate from final authorization. |
| sov_nuclear_bombs_retaliation_window_mission | Active retaliation window, major-exchange world gate, and valid major strike target. | sov_nuclear_bombs_duration.hotline_mission | Complete and timeout use sov_nuclear_bombs_complete_retaliation_window; invalid gate, target, or actor cancels. | One retaliation family. |
| sov_nuclear_bombs_rail_corridor_security_mission | Active rail mission and exact selected breakaway site valid. | sov_nuclear_bombs_duration.rail_security_mission | Complete and timeout use sov_nuclear_bombs_complete_rail_security; invalid actor or site cancels. | One collapse-support family. |
| sov_nuclear_bombs_breakaway_technical_access_mission | Breakaway custody crisis, technical stage, and selected site valid for the actor. | sov_nuclear_bombs_tuning.breakaway_technical_access_days | Complete and timeout use the shared operationalization resolver; crisis or site invalidation cancels. | Shares one bounded active family and flag with the other two stages. |
| sov_nuclear_bombs_breakaway_command_formation_mission | Breakaway custody crisis, command stage, and selected site valid for the actor. | sov_nuclear_bombs_tuning.breakaway_command_formation_days | Complete and timeout use the shared operationalization resolver; crisis or site invalidation cancels. | Same single stage family. |
| sov_nuclear_bombs_breakaway_delivery_integration_mission | Breakaway custody crisis, delivery stage, selected site valid for the actor, and local delivery capability. | sov_nuclear_bombs_tuning.breakaway_delivery_integration_days | Complete and timeout use the shared operationalization resolver; crisis or site invalidation cancels. | Same single stage family; no generic duplicate remains. |
| sov_nuclear_bombs_joint_custody_transfer_mission | Active joint-custody mission and exact selected breakaway site valid. | sov_nuclear_bombs_duration.breakaway_transfer | Complete and timeout use sov_nuclear_bombs_complete_joint_custody_transfer; invalid actor or site cancels. | Separate from staged breakaway operationalization. |
| sov_nuclear_bombs_dismantlement_inspection_mission | Active dismantlement mission and exact selected site still has an assigned device. | sov_nuclear_bombs_duration.dismantlement_mission | Complete and timeout use sov_nuclear_bombs_complete_dismantlement; invalid actor or assigned device cancels. | One moratorium inspection family. |

## Cost and requirement clarity

The five shared cost profiles use two to four spendable types per action: command is political power plus command power; security is political power plus support equipment plus manpower; logistics is command power plus trains plus fuel; diplomatic is political power plus command power plus convoys; strategic is political power plus command power plus support equipment plus fuel.

The maximum is four distinct spendable cost types, and the audited cost localisation keys sov_nuclear_bombs_cost_command, sov_nuclear_bombs_cost_security, sov_nuclear_bombs_cost_logistics, sov_nuclear_bombs_cost_diplomatic, and sov_nuclear_bombs_cost_strategic use texticons for every spendable value without spelling out resource names.

Requirements are separated into custom trigger tooltips and spendable cost strings. Direct source coverage is 78 unique decision/mission name keys, 78 unique description keys, 13 custom trigger tooltip keys, and 5 custom cost text keys, with no missing direct localisation identifiers found.

The remaining strict-cost issue is in common/scripted_triggers/023_sov_nuclear_bombs_cost_triggers.txt, where the shared affordability checks use greater-than rather than equality-inclusive checks while the display shows the exact constant. That file is outside this audit ownership and was not changed.

## AI validity and route-lock notes

The decision source retains target-aware AI factors for capital, air-base, industrial, major-target, assigned-site, remote-site, transferred-custody, and crisis contexts. The new target guards fail closed for ordinary coercion against a major controller and do not alter the dedicated major-exchange route.

State-target selectors require the relevant actor, phase, active-project lock, and state validity helper. Selected test, collapse, breakaway, and command states are revalidated in the decision or mission cancel path. Major retaliation requires the separate world gate and a valid nuclear-major target.

The required chaosx_ai_probability_auditor was used. The installed MCP decision_ai_will_do adapter returned INTERNAL_ERROR and then PROBABILITY_SOURCE_DISCOVERED with zero decision candidates while redirecting to mission_ai_will_do, so a decision-weight conclusion is not valid.

The post-patch auditor compared the same named Event 23 scenarios. The fallback 43-scenario decision attempt returned PROBABILITY_ANALYZED_PARTIAL with 2,881 candidate rows, 310 unresolved rows, and comparisonChanges = 0, but it is explicitly not decision evidence. The focused three-decision attempt returned PROBABILITY_SURFACE_EMPTY.

The surviving breakaway family comparison used P23_COLLAPSE_NEGOTIATE_STABLE_BREAKAWAY, P23_COLLAPSE_RAID_IMMINENT_OPERATIONALIZATION, P23_COLLAPSE_TINY_UNSTABLE_BREAKAWAY, P23_COLLAPSE_OPERATIONAL_SUCCESS, and P23_LIMITED_USE_BREAKAWAY_SEVERE. It returned PROBABILITY_ANALYZED with 15 rows, zero unresolved rows, three diagnostics, and comparisonChanges = 0; all three stage missions were never eligible because their engine available blocks are intentionally always = no. This is score-only mission evidence, not normalized selection probability.

No AI numeric weight was changed, and no balance claim is made for the unavailable decision adapter. No complete stochastic cadence or sequence simulation was possible.

## Cleanup and exploit-risk notes

The owned source has no direct strike effect; strike authorization remains distinct from target selection and preparation. The read-only runtime review found exact target, war, stockpile, command, and world-gate rechecks before the shared nuclear action.

Stale actor, target, site, response, prepared-strike, breakaway-site, and assigned-device conditions now cancel the corresponding mission or close the corresponding decision path. The generic breakaway mission duplicate and the selector-after-selection exposure were removed.

The bounded source audit found no free strike path, free-device loop, war-goal spam path, core spam path, or cooldown bypass in the decision definitions. Broad route reachability, helper-level world scans, and shared payment semantics remain parent/runtime scope.

## Required MCP evidence

Event inspection for chaosx.nr23.1 used hoi4.event_inspect in lint mode after the bounded patches. It returned status ok and blockingDiagnostics = 0, with the large-workspace result marked partial because workspace-wide helper/lifecycle projections were deferred.

Event lint artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5ccdb2b159d75975151aef301dc6990c9a529c12aa17e65036a331dcd4f36c84/00f0bbbcb88b6a90561466412920200fea99c5b970d37b8be98b211ddf83e11b/event-lint-7ef39a19e520.json

Read-only event target render artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/27fa433df8f40e8f211e56cb6ed94095c7dc78b35e27c5210c798437cb0b4954/16ae329b17237ce0eba18eec210c7e3294883f602683684f37987b571ff42626/event-targets-7ef39a19e520-manifest.json

Read-only event state render artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ea91bdeaa2a1e07a211d82158b21548225d9c7840ef9e9e4dfa4b5936926b083/f53d386b10f4fc9513ae174ba1a22d7ad5bca72685852dce5798d4867c51160c/event-state-7ef39a19e520-manifest.json

The mandatory ordinary decision-tab hoi4.gui_inspect call returned GUI_INSPECTED with complete = true and no Event 23 scripted-GUI surface in the inspected source. The global GUI graph retained unrelated diagnostics and dropped additional diagnostics at its global budget.

GUI inspection artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/411301752efb2235e71787d0997f650648c2e05e4ffede34f4db4714755c7785/6a8d3aeb846486f65555066493371dec42d516b44af136a621869f4f613d5d90/gui-inspect.15644206d429222f.json

The mandatory hoi4.gui_render route was attempted for the normal decision-tab scenario at 1920x1080 and 1280x720, then retried with one resolution and one state. Both calls timed out after 180 seconds, so no production visual pass or GUI rewrite claim is made.

The post-patch probability artifacts are:

- Decision adapter inspection: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5cb6cced6cad4dfd1a3df6a8980d18381aabce5b12988f4e5541e7206542c65f/f0b4f0553fc466bb98018f4f627511f837924a83848f020e82a68fe10efe6280/probability-inspect-67372c687843.json
- Mission fallback inspection: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/db057615ae91734db97f9308afc3b1126895c5b1c3ed6fa7f9c89327dd99039d/fc9b97128901c5483d97c568f16ca480ce16b5a25c40497e9404b442c0f7511e/probability-inspect-67372c687843.json
- Breakaway-family comparison: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/654a749d8d415fb12f98467c0f3d1c38fd99c0edebf6fd1c2e0c25a5b1dda42a/a6ca2e3c099c0d1d40530715d2e3708b74e77e476cc6c8049a973f95eb2eb31c/probability-025f6a18f4a7409beae0d0de.json

## Validation limits and unresolved items

Source validation found balanced braces, 80 category entries, 13 mission timeouts, no generic duplicate mission definition, complete direct localisation coverage, and matching mission lifecycle fields.

No Event 23 localisation, event, runtime ledger, GFX, asset, workbook, or unrelated system file was changed.

The MCP event and GUI artifacts are partial or blocked by global analysis budgets, the decision probability adapter remains unavailable, the shared cost helper retains the strict equality edge, and no live Hearts of Iron IV session was run. These are the remaining limitations and are carried to the parent rather than treated as equivalent to full gameplay validation.

No simplification or unapproved fallback was introduced inside the owned decision/mission source. The absence of a GUI rewrite, localization patch, and helper patch is intentional and follows the stated ownership boundary.
