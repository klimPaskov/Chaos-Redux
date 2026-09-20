# Event 23 decision and mission audit

Audit date: 2026-09-19.

Disposition: INCOMPLETE.

This is a read-only audit of the current Event 23 source revision. The only file written by this audit is this handoff. No gameplay, workbook, asset, or localisation file was edited.

The source surface is not ready for completion review because it exceeds the visible-action contract, can randomly choose a breakaway site, and does not apply the common project lock to the three breakaway stage starters. Engine-level completion is also blocked by the unavailable decision-specific MCP route, the clipped generic production render, and the absence of a completed probability-auditor scenario artifact.

## Scope and evidence policy

I read AGENTS.md, the complete chaos-redux-decisions-missions, chaos-redux-events, chaos-redux-subagents, and chaos-redux-scripted-gui skills, all files under docs/specs/023_sov_nuclear_bombs_specs/, all current Event 23 plan and handoff files, and the older decision handoffs only to identify stale claims that must not be reused.

I read the current common/decisions/023_sov_nuclear_bombs_decisions.txt, common/decisions/categories/023_sov_nuclear_bombs_categories.txt, common/scripted_triggers/023_sov_nuclear_bombs_event_triggers.txt, common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt, common/scripted_effects/023_sov_nuclear_bombs_runtime_effects.txt, common/scripted_triggers/023_sov_nuclear_bombs_cost_triggers.txt, common/scripted_effects/023_sov_nuclear_bombs_cost_effects.txt, the Event 23 constants and scripted localisation, the Event 23 event file, localisation, interface registry, and referenced assets.

I consulted the required offline Paradox wiki pages for data structures, triggers, effects, modifiers, localisation, scopes, on actions, event modding, decision modding, idea modding, AI modding, interface modding, and scripted GUI modding, together with the installed vanilla documentation and vanilla decision/mission precedents under C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\.

The latest 2026-09-19 completion and documentation handoffs are treated as stale snapshots rather than current proof. Current findings below come from the source revision inspected in this audit and from fresh MCP calls.

The current decision file contains 81 top-level definitions inside sov_nuclear_bombs_command_category: 68 decision-like definitions and 13 mission definitions. The 13 mission identifiers begin at common/decisions/023_sov_nuclear_bombs_decisions.txt:1143 and continue through line 1373.

## Severity-ordered issue list

### High severity

1. The ordinary category can expose more than the six-primary-decision hard maximum.

common/decisions/023_sov_nuclear_bombs_decisions.txt:72 keeps sov_nuclear_bombs_operational_command visible across all normal phases and :91 keeps sov_nuclear_bombs_reform_custody_doctrine visible whenever its incident/evolution gate is true without a phase-specific presentation gate. :803 keeps sov_nuclear_bombs_enter_atomic_moratorium globally visible whenever its own available trigger can pass. In a valid production state with reactor entitlement, production capacity, a route, and a reform trigger, the visible set can include operational command, doctrine reform, reactor expansion (:248), device assembly (:266), delivery crews (:280), command exercise (:294), stronger authentication (:308), and atomic moratorium (:803), for as many as eight rows before any action is started. The custody state can similarly expose operational command, reform, audit, hardening, reserve dispersion, centralization, emergency retaliation delegation, and moratorium. Test and coercion states also reach or exceed the limit when their persistent controls and failure/response controls overlap.

This is a source finding, not an engine row-count result, because the installed MCP exposes no decision-specific inspector. The source directly violates the accepted three-to-five normally, six maximum contract in docs/specs/023_sov_nuclear_bombs_specs/023_sov_nuclear_bombs_decision_map.md:3-12.

Recommended fix: make the persistent command board a phase-specific summary or hide it once a phase action set is active, gate doctrine reform and moratorium presentation by the active phase/action group, and re-count every valid scenario until the category has no more than six visible primary actions.

2. Breakaway custody does not use player-selected site management.

sov_nuclear_bombs_breakaway_secure_custody at common/decisions/023_sov_nuclear_bombs_decisions.txt:1067 is not a state_target decision. Its effect sov_nuclear_bombs_breakaway_secure_local_custody at common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt:3028-3042 uses random_controlled_state and saves whichever eligible transferred site it finds as sov_nuclear_bombs_selected_state. The accepted decision map explicitly requires selected-site management for storage, test, and custody actions, and the same design rule forbids random redirection of an action to a different site.

This can secure a different depot from the one the player intended and changes the later technical, command, delivery, recovery, and return chain without a player choice.

Recommended fix: expose a state-target selector for the first breakaway custody action and pass that exact selected state through every stage, with no random fallback. If no state is selectable, keep the decision hidden and explain the blocked reason.

3. The three breakaway stage starters omit the shared active-project guard.

The visible and available blocks for sov_nuclear_bombs_breakaway_attempt_technical_access, sov_nuclear_bombs_breakaway_form_command, and sov_nuclear_bombs_breakaway_integrate_delivery at common/decisions/023_sov_nuclear_bombs_decisions.txt:1081-1119 only reject their shared breakaway mission flag. Their effect helpers at common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt:2866-2932 likewise check stage custody and the shared breakaway flag but never call sov_nuclear_bombs_event_no_active_project.

The current sov_nuclear_bombs_event_no_active_project contract at common/scripted_triggers/023_sov_nuclear_bombs_event_triggers.txt:894-921 does list the breakaway mission, but that list is not enough when the breakaway starters do not use it. A technical, command-formation, or delivery-integration mission can therefore start while another project or mission such as an ultimatum response, rail security, joint custody, or dismantlement flow is active. The shared flag still serializes the three breakaway stages with each other, but the global three-active-mission limit is not enforced by one common guard.

Recommended fix: require sov_nuclear_bombs_event_no_active_project = yes in all three decision availability blocks and all three start-effect limits, and retain the selected-state validity check at activation and completion.

4. The delivery route gate proves platform capacity but not the trained delivery chain, and its engine equivalence is unresolved.

sov_nuclear_bombs_event_has_delivery_route at common/scripted_triggers/023_sov_nuclear_bombs_event_triggers.txt:73-98 checks atomic technology, bomber technology, deployed bombers, fuel, and an owned controlled airbase. The exact endpoint helper at :102-120 uses an event distance ceiling rather than a native air-wing range query. The route helper never requires sov_nuclear_bombs_delivery_crews_ready or sov_nuclear_bombs_delivery_crews_certified; those flags are only set by the delivery-crews mission at common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt:2138-2139 and are not referenced by the test, demonstration, limited-strike, or retaliation route gates. The current source therefore allows the preparation mission to be optional even though its localisation says it establishes the verified bomber route.

This is a route-lock source finding and a specification-integration question if the crew mission is intended as a bonus rather than a prerequisite. Separately, the runtime launch/callback path is only source evidence: sov_nuclear_bombs_execute_shared_action calls the native launch effect and the Event 23 callback confirms the request, but no installed MCP route in this audit proved a live wing-range, native queue, or save/load callback transaction.

Recommended fix: decide and document whether delivery-crews certification is mandatory for every detonation route. If mandatory, add it to the shared route predicate or to the exact action authorization predicates, and replace the distance proxy with the strongest supported native route validation available. Preserve the callback nonce and exact endpoint re-check.

5. The category's production visual evidence is currently a clipping failure, and no Event 23-specific decision window is registered.

The source category is an ordinary category with one static picture at common/decisions/categories/023_sov_nuclear_bombs_categories.txt and the picture/icon definitions in interface/023_sov_nuclear_bombs.gfx; there is no Event 23 scripted GUI to route to chaosx_event_ui_worker. Fresh hoi4.gui_inspect and hoi4.gui_render calls were nevertheless run against the native countrydecisionview at 1920x1080 to satisfy the decision-surface visual evidence requirement. The production inspector reported GUI_ACCIDENTAL_CLIPPING for a 550x1080 window clipped to 0x0, along with zero-size production elements and a partial Lua sprite representation. The full production PNG was a blank dark view, so this cannot be dismissed as a renderer difference.

An attempted inspect of sov_nuclear_bombs_command_category returned GUI_WINDOW_MISSING, inspectedElementCount: 0, and validation false with truncated graph/validation diagnostics, confirming that this is not a registered custom Event 23 window. The current evidence cannot prove Event 23 row alignment, overflow, click regions, disabled states, or static-picture placement in production.

Recommended fix: first obtain a working native decision-category render or record an exact engine-service blocker. Then inspect matching Event 23 scenarios for normal, locked, active-mission, long-text, missing-localisation, hover, selected, disabled, warning, empty-list, and full-list states. Do not add a new scripted GUI solely to work around this audit.

### Medium severity

6. The initial breakaway security gate accepts one division but does not check supply or a held rail corridor.

sov_nuclear_bombs_event_selected_breakaway_site_has_security_force at common/scripted_triggers/023_sov_nuclear_bombs_event_triggers.txt:985-995 requires the selected state to be controlled by the actor and divisions_in_state.size > 0, because the file-local floor is zero. The recovery route separately requires infrastructure and railway, but no supply status, rail connection continuity, or corridor control is checked. This is weaker than the decision-map requirement for adequate guards and a secured route and makes security force mean one division even when the operation cannot be supplied.

Recommended fix: centralize a tunable minimum guard/supply/corridor predicate and use it in selection, activation, cancellation, and completion of recall, rail security, raid, and joint-custody actions.

7. Dynamic phase, site, target, and deadline localisation exists but is not wired into the ordinary category description.

The category description at localisation/english/023_soviet_nukes_l_english.yml:89 displays only operational devices, readiness, integrity, and posture/knowledge. common/scripted_localisation/023_sov_nuclear_bombs_scripted_localisation.txt defines GetSovietNuclearBombsPhaseName, GetSovietNuclearBombsCategorySiteName, GetSovietNuclearBombsCategoryTargetName, and GetSovietNuclearBombsCategoryDeadlineName, but a repository search found no category description or interface consumer using these helpers. The deadline strings show fixed total durations such as “120 days,” not remaining mission time.

The four visible values have real gameplay significance, but the header does not explain the current phase, selected site/target, active mission deadline, or the immediate response to a low threshold. This forces the player to infer state from a long list of rows and tooltips.

Recommended fix: wire a concise phase/site-or-target/deadline summary into the existing ordinary category description, or remove unused dynamic helpers after confirming another consumer. Use actual remaining time rather than a static duration label.

8. Requirement tooltips do not match the current predicates in two important places.

localisation/english/023_soviet_nukes_l_english.yml:167 says a target must be a valid registered state, but sov_nuclear_bombs_event_state_is_valid_command_target at common/scripted_triggers/023_sov_nuclear_bombs_event_triggers.txt:141-175 checks impassability, existence, custody flags, ownership/control or war, and valid coercion actors without requiring sov_nuclear_bombs_state_is_registered. The tooltip therefore describes a stricter requirement than the operational, coercion, redirect, and command target triggers actually enforce.

The registered-site tooltip at localisation/english/023_soviet_nukes_l_english.yml:169 says “Dismantlement requires at least two assigned devices,” while the current selector at common/decisions/023_sov_nuclear_bombs_decisions.txt:971-987 and the shared predicates at common/scripted_triggers/023_sov_nuclear_bombs_event_triggers.txt:614-625 use greater_than_or_equals one-device checks. The current one-device threshold is source-correct; the player-facing text is not.

The doctrine-reform tooltip at localisation line 193 describes a generic “major war-state change,” while the current trigger at common/scripted_triggers/023_sov_nuclear_bombs_event_triggers.txt:28-46 requires one of specific test-failure, accident, confirmed-enemy-use, capital-threat, or Evolution-I-plus-war conditions. It also says “active operation” while the implementation uses the broader event_no_active_project helper.

Recommended fix: align these tooltips with the exact current trigger predicates and keep spendable costs separate from non-consumed target/site requirements.

9. Partial test outcome exists in the source pool but is not presented as a distinct player-facing outcome.

The current test pool at common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt:752-806 and common/script_constants/023_sov_nuclear_bombs_constants.txt:301-317 uses base weights 60 success, 20 partial, 12 failure, and 8 accident, with preparation/readiness/integrity modifiers and minimum-one clamps. This is current evidence; older handoffs claiming a 70/20/10 three-entry pool are stale.

Only failure is marked non-detonating in prepare_test_outcome; partial, success, and accident use the same native delivery route. Partial sets sov_nuclear_bombs_test_partial_yield and applies its integrity delta, but the normal test report at localisation/english/023_soviet_nukes_l_english.yml:27 mentions success, failure, and accident while omitting partial yield. The accident report at line 30 says the device remains accounted for even though native delivery/ledger consumption needs engine confirmation.

Recommended fix: give partial yield a precise report/status line and confirm its intended device and native-detonation consequence. Keep the current four-entry source pool only if all four outcomes are represented consistently in event text, logs, ledger receipts, and follow-up decisions.

10. Two collapse selectors present the same action before any depot is chosen.

sov_nuclear_bombs_collapse_command at common/decisions/023_sov_nuclear_bombs_decisions.txt:117 and sov_nuclear_bombs_select_disputed_depot at :818 use the same collapse-active, no-site-selected presentation and the same collapse-site target predicate. This creates two near-duplicate primary rows for one selection task before the later recall, rail, raid, disable, and restore actions become relevant.

Recommended fix: retain one selector identifier and make the other a hidden compatibility alias or phase-specific action only if it has a distinct effect and tooltip.

11. AI weights are present but not sufficiently centralized or engine-verified.

The source gives all 81 definitions an ai_will_do block, and many target selectors use capital, airbase, industrial, major-power, custody, or remote-site factors. The major first-use gate is conservatively source-gated through Evolution IV, Chaos, war, strategic losses, capital threat, front collapse, reserve exhaustion, enemy-use or launch-preparation evidence, readiness/integrity floors, delivery route, and a nuclear-major target. Retaliation additionally requires Evolution III, a confirmed exchange, a selected major target, an unreserved device, route, readiness, integrity, and centralized/delegated authority.

However, many decision bases and threshold factors remain literal values in the decision file, and the installed probability adapter did not return a complete normalized selection pool. Balance cannot be claimed from source weights alone.

Recommended fix: route the named probability scenarios through a completed chaosx_ai_probability_auditor pass after the decision adapter and mission pool are available, centralize repeated AI tuning values, and compare the same scenarios before and after any balance patch.

### Low severity and follow-up risks

12. sov_nuclear_bombs_breakaway_operationalization_paused is set by sov_nuclear_bombs_cancel_breakaway_operationalization at common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt:2687-2693 but is not read or cleared anywhere in the current source search. It is currently inert, but it is a stale state flag and should either become a documented player-facing pause state or be removed from the cancellation path.

13. The hotline automatically chooses a partner with random_country in sov_nuclear_bombs_select_standdown_partner rather than exposing a player-selected opposing major. The event plan allows direct or mediated communication, so this is a lower-confidence agency concern rather than a confirmed contract violation, but the selected partner should be shown before the player commits the diplomatic cost.

14. The category has a valid static picture and icon source registration, but no fresh Event 23-specific visual artifact demonstrates that the supplied asset is aligned, unclipped, or readable in the ordinary decision-category consumer. The generic production render blocker prevents treating source wiring as visual acceptance.

## Decision-category lifecycle notes

The opening event chaosx.nr23.1 and follow-up events establish the Event 23 actor, ledger, doctrine choice, evolution flags, and the ordinary category. The four initial custody choices are mutually exclusive, after which the category exposes custody, production, test, coercion, authorization, retaliation, collapse, and moratorium actions in one static ordinary category.

Targetable decisions save selected states as global event targets. The operational command, coercion, retaliation, collapse, breakaway, and dismantlement actions then pass those pointers into the Event 23 event effects and the shared runtime action contract.

Timed decision rows set pending flags and resolve on removal, timeout, cancellation, or actor invalidation. The 13 timed mission definitions at common/decisions/023_sov_nuclear_bombs_decisions.txt:1143-1373 all use activation, available = { always = no }, a dynamic constant duration, a completion path, a cancel trigger/effect, a timeout effect, and an AI score.

The test lifecycle is survey, reserve one assigned device, prepare one of three test profiles, optionally improve evacuation, resolve the four-entry outcome pool, confirm or reject the native route, record the receipt, and return to custody. The coercion lifecycle is select a state, derive a valid country target and demand, send an ultimatum, record the target response, apply or verify settlement terms, or clear the response window. The breakaway lifecycle is physical custody, technical access, command formation, delivery integration, and only then operationalization or return.

The lifecycle is generally event-driven and does not add a new whole-world periodic loop in the inspected Event 23 decision/effect surface. The main lifecycle failure is that the breakaway stage entry path is not serialized against the other active projects and that the first custody site is random rather than selected.

## Cognitive-load audit

The category contains 68 decision-like definitions and 13 mission definitions, but the player should only see a small phase-specific subset. The current presentation logic can show up to eight primary rows in a valid production/custody state, seven in a coercion or test state, and duplicate collapse selectors before site selection.

The category header is compact rather than a wall of prose, and the four displayed values are meaningful: usable devices represent ledger stock less reservation, readiness represents delivery/technical usability, integrity represents authorization/accounting reliability, and posture/knowledge summarize strategic identity and foreign awareness. Their thresholds, causes, consequences, and player response are not explained in the header, and phase, selected site/target, and active deadline are absent.

The active mission design intends one to three visible missions, and ordinary decision starters mostly use sov_nuclear_bombs_event_no_active_project. The breakaway starters are the exception, so the cap is not enforceable as a single invariant. The impossible mission availability blocks are appropriate for explicit activation, but they make the probability adapter report score-only mission surfaces rather than real selection probabilities.

Most individual decision descriptions are short and consequence-oriented. The main text-density defects are the long static row set, the unused contextual localisation helpers, the mismatch between exact requirements and tooltip prose, and the omission of partial test yield from the report.

## Mission quality notes

| Mission | Owner and region | Requirement and duration | Success/failure and cleanup | Duplicate/overlap risk |
| --- | --- | --- | --- | --- |
| sov_nuclear_bombs_device_assembly_mission | Current Event 23 actor, production/country | Production capacity and atomic technology, 120 days | Completes production or cancels when the actor becomes invalid; flags are cleared by the paired effects | Low through the normal decision, but the helper itself does not repeat the full shared project guard |
| sov_nuclear_bombs_delivery_crews_mission | Current actor, production/delivery route | Delivery route, 90 days | Sets ready/certified flags and readiness on success; invalid actor cancels | Low for duplicate activation because the decision and effect use a mission flag; its certification is not used by action gates |
| sov_nuclear_bombs_command_exercise_mission | Current actor, production/command chain | Delivery route, 60 days | Sets exercise completion and readiness/integrity changes; invalid actor cancels | Low for duplicate activation; completion is optional and does not gate release |
| sov_nuclear_bombs_proof_test_mission | Current actor, selected test state | Valid registered site, one assigned device, exact selected route, 120 days | Resolves success, partial, failure, or accident; invalid site/actor cancels and releases through the action-context rules | Low under normal flow; native pending cleanup remains engine-unverified |
| sov_nuclear_bombs_ultimatum_response_mission | Current actor plus selected target country/state, coercion | Valid target response window, 45 days | Applies full/partial settlement, records alternate responses, or clears the target on cancel/timeout | Low under normal start; target invalidation and delayed response cleanup are source-covered but not live-verified |
| sov_nuclear_bombs_strike_preparation_mission | Current actor, selected limited-strike state | Reserved device and valid limited-strike target, 7 days | Completes preparation or aborts and recovers the device | Low under normal start; native route and queue proof are missing |
| sov_nuclear_bombs_retaliation_window_mission | Current actor, exchange target or hotline | Confirmed exchange/valid target or hotline, 30 days | Resolves hotline or executes/cancels the response and clears the window | Low for ordinary decisions, but exact native callback ordering is unverified |
| sov_nuclear_bombs_rail_corridor_security_mission | Current actor, selected breakaway state/rail region | Valid collapse site, infrastructure, railway, and one division, 120 days | Recall, secure, or raid completes only after current route/security checks; cancel clears operation and selection | Medium because one division is the entire security threshold and no supply/corridor check exists |
| sov_nuclear_bombs_breakaway_technical_access_mission | Breakaway/current actor, selected transferred depot | Physical custody, selected valid site, stage 1, 180 days | Grants technical-access flag or records failure and clears shared stage | High because its starter has no global no-project guard |
| sov_nuclear_bombs_breakaway_command_formation_mission | Breakaway/current actor, selected transferred depot | Technical access, selected valid site, stage 2, 240 days | Grants command-formed flag or records failure and clears shared stage | High because its starter has no global no-project guard |
| sov_nuclear_bombs_breakaway_delivery_integration_mission | Breakaway/current actor, selected transferred depot/route | Command formed, exact delivery capability, stage 3, 180 days | Operationalizes the site only after capability and custody checks; otherwise records failure and clears stage | High because its starter has no global no-project guard and the first site selection is random |
| sov_nuclear_bombs_joint_custody_transfer_mission | Current actor, selected transferred breakaway site | Valid collapse site, recovery route, security force, 120 days | Requires a currently registered transferred site, marks joint custody on success, records failure otherwise, and clears selection | Low for normal activation; it is still exposed to overlap from breakaway stage starters |
| sov_nuclear_bombs_dismantlement_inspection_mission | Current actor, selected Soviet registered site | At least one assigned device, moratorium, 180 days | Executes one-device dismantlement and clears the mission; cancellation clears action context and selection | Low for activation; tooltip says two devices while code uses one |

## Cost and requirement clarity

The five cost profiles are command, security, logistics, diplomatic, and strategic. The per-action spendable-type counts are command 2, security 3, logistics 3, diplomatic 3, and strategic 4, so no profile exceeds the four-type limit in the current source scan.

The cost triggers and payment effects are paired in common/scripted_triggers/023_sov_nuclear_bombs_cost_triggers.txt and common/scripted_effects/023_sov_nuclear_bombs_cost_effects.txt. They use political power, command power, support equipment, manpower, trains, fuel, and convoys as context-appropriate resources instead of a flat political-power exchange.

All five visible cost strings in localisation/english/023_soviet_nukes_l_english.yml:155-166 use texticons: £pol_power, £command_power, £support_equipment_text_icon, £manpower_texticon, £GFX_train_texticon, £GFX_fuel_texticon, and £convoy_texticon. The source scan found no fifth hidden spendable cost in decision effects, confirmation paths, or the paired cost helpers.

The cost text is separated from non-consumed requirements through custom cost triggers, custom cost text, and custom trigger tooltips. The remaining clarity defects are the target registration mismatch, the dismantlement one-versus-two mismatch, and the lack of a category-level display for the active state/site/deadline context. The actual custom-cost rendering could not be validated in the clipped generic production view.

## AI validity and route-lock notes

Source-level AI is present on every current decision and mission definition. Target selectors use explicit state target triggers and generally reject impassable, missing, dismantled, capitulated, subject, or invalid-country targets. Major strike selection requires a nuclear major at war, and coercion rejects a major controller. Current one-device predicates use greater_than_or_equals one in the selected storage, selected test, transferred, and unreserved-device helpers.

The severe first-use gate and major-exchange gates are source-conservative. Major exchange requires reciprocal major receipts rather than a single detonation, and first use requires Evolution IV plus the severe Chaos/war/loss/capital-threat/front-collapse/reserve/external-use conditions. These source findings are not probability evidence.

The exact delivery route is still a numeric platform/distance proxy rather than native wing availability. Breakaway delivery capability reuses that proxy for the holder and the selected endpoint. Breakaway security is one division with no supply test. Reactor and native queue completion, native bomb-stockpile deltas, and callback/save-load identity remain source-only concerns because no live game or native queue evidence was run by this auditor.

## Localisation and tooltip gaps

The ordinary category name, picture/icon names, decision names, mission names, cost strings, and most custom trigger tooltips are present. The category picture is registered as GFX_decision_category_sov_nuclear_command_picture and the icon as GFX_decision_category_sov_nuclear_command_icon.

The category description does not expose current phase, selected site, selected country/target, or remaining deadline even though the scripted-localisation helpers exist. The partial outcome is omitted from the normal test report, the accident report wording is ambiguous about device accounting, the target tooltip overstates registration, the site tooltip overstates dismantlement quantity, and the doctrine reform tooltip describes broader conditions than the trigger accepts.

No missing localisation key was used as a reason to dismiss a source or visual issue. The current source and localisation were audited as-is; no localisation was changed.

## Cleanup, cancellation, timeout, and exploit-risk notes

Positive source findings are that every timed mission has a cancellation path and timeout path, sov_nuclear_bombs_event_no_active_project enumerates the main project flags, the action context avoids refunding a still-pending native delivery, and annex cleanup clears the Event 23 pointers, projects, missions, and pending reactor state. Joint custody completion now checks a registered selected site with at least one transferred device before setting success. Retaliation completion revalidates the current target/route before executing, and coercion response resolution applies or verifies concrete settlement terms instead of treating a response flag alone as compliance.

The main remaining risks are the random breakaway-site assignment, the missing global breakaway project lock, the optional delivery-crew/certification gate, and the absence of live native callback/queue proof. sov_nuclear_bombs_breakaway_operationalization_paused is written but never consumed or cleared. The current source does not show a free repeated one-device loop in ordinary dismantlement; each completed dismantlement finalizes one device and the selected-site predicates require a remaining assigned device. The current source also does not show a flat-cost or free war-goal loop in this decision surface.

## Mandatory MCP evidence

The installed hoi4-agent-tools server did not expose hoi4.decision_inspect or a decision-specific render route. The exact absence of that route is an engine-evidence blocker; source row analysis is not equivalent to an engine decision-row inspection.

Fresh hoi4.event_inspect was run with selector { kind: event, eventId: chaosx.nr23.1 }, downstream direction, helper expansion, depth 3, and refresh. It returned status: ok, code EVENT_INSPECTED_PARTIAL, workspace mod_chaos_redux_ea3b2d67c2c0, revision 5157ad1bfa6f2172c93e6c740eeb9f6398e124f1bd1ab17777a3065783f0c6ea2, graph hash b6613a4ac5d285114b2066cbca625fd687d2aca12297caf6b4bdf6abe5c50372, zero blocking diagnostics, and a structural artifact at hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6bcb1c21663ef7555f430fc14e3e8400e807fef8480bd9cee6075b87b148ec07/4e67bf8dc4a61fe149781c353d277ff76cabbee8e60410bf57a4b0c0711faaef/event-lint-5157ad1bfa6f.json. The route is partial because workspace-wide helper and lifecycle projections were deferred, so it is structural evidence only.

Fresh hoi4.event_render for the same selector returned status: ok, code EVENT_RENDERED_PARTIAL, the same revision, and these artifacts: manifest hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/555c6d352f1ec9ee2ab6aca48339befe6bf4c7d53ebb4f61869217aa1da64b0/a599309fe8abd791aa9bc0461fb8800315c15a9ba8d54d126654297251136146/event-overview-5157ad1bfa6f-manifest.json, JSON hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3909186f960c51939237455e8c6dcdc173c68e5ad4c85386a2988d7b965fe20e/e300070059ad2314c24e3a676798411ea253bf6cf195b41fe4b02ae36cfef37c/event-overview-5157ad1bfa6f.json, SVG hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8b27bdee93452e1dabcc974588613cdebaa397c0b5374bc612d5c0544456a67f/73d1e889f4b9b7b0481a1650c3ef80ae65c3883e2467a9fd80bff41dda7ab833/event-overview-5157ad1bfa6f.svg, and PNG hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6faeba86ae4508bba608be4c9973f2ca003f7fc170b9c307e930c516d897bb40/555273d3a224d65c4e2c04a7bf7e411ccb4173dad10bcb56a9fff3590aa4d215/event-overview-5157ad1bfa6f.png. The render selected only ten nodes from a much larger graph and remains partial.

Fresh hoi4.gui_inspect of native countrydecisionview at scenario evt23-decision-category-current-20260919, 1920x1080, UI scale 1, returned status: ok, code GUI_INSPECTED, complete source validation, zero skipped sources, and artifact hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/95943919b3ffc67495025d4d4254691ec0d7e83fc8237eba27f8fe5c58028c41/b8ceb71bfbf75e4bf07d4e855ccb98dd5860c5550f6ffe9760a18fd1e994491c/gui-inspect.85ed88240b03161c.json. Its source graph was complete, but diagnostics included GUI_ACCIDENTAL_CLIPPING to 0x0, zero-size production elements, unsupported texture/scroll fields, and a partial Lua sprite representation.

Fresh hoi4.gui_render of the same native window returned status: ok, code GUI_RENDERED, source revision 85ed88240b03161cde8608388fd68fb7c904e6841793b00e0debe23b2a143e1c, and full PNG hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/397d44367a8a781890ca2bc55c286a9b4f1f5d87c380f87d08bbe82d9d756820/af8e65046aba48a1c5501e40fbe037a3453c67075e65b31a0f45ddd871e32a72/countrydecisionview-full.png. The production image was a blank dark 1920x1080 view caused by the reported clipping/zero-size layout. The render did not cover hover, selected, disabled, warning, active, completed, empty-list, full-list, minimum-value, or maximum-value states.

A fresh hoi4.gui_inspect attempt using window name sov_nuclear_bombs_command_category returned artifact hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a0fffc9fa9d379cdd257e4ec6dc851ee942f89078b0400dc18ef2ccd7ad4aba8/8000c45e6264535fe52fc7f3320061dd58fdfc0c9a49beb2e18328030c8ea414/gui-inspect.19f45441f12fbb95.json, inspectedElementCount: 0, GUI_WINDOW_MISSING, and validation false due truncated global graph/validation diagnostics. This is evidence that the ordinary category is not a custom scripted-GUI window, not evidence that its in-game category layout is acceptable.

Fresh hoi4.probability_inspect with adapter decision_ai_will_do and source path common/decisions/023_sov_nuclear_bombs_decisions.txt returned status: ok, code PROBABILITY_SOURCE_DISCOVERED, source revision 206a070b3e7ecdb733fd8f1093acfc467b8ad80a176d88c9deee241fe629d4df, source hash f85397565290163e432048a5034a0dd604bcaeb918a1f94232dff24c04517e1d, zero candidates for the requested adapter, and a suggestion to use mission_ai_will_do with 81 available candidates. Artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/da2b8215acfd9d535b5c5cdee5804f45967a57d281f52c16af2d66b26df76d4f/d2db07ae928d829d024f167efb01e67ba47a1b6becd6d99c04afd9daf7267e5f/probability-inspect-f85397565290.json.

Fresh hoi4.probability_inspect with adapter mission_ai_will_do and the same source returned status: ok, code PROBABILITY_SOURCE_INSPECTED, source revision 206a070b3e7ecdb733fd8f1093acfc467b8ad80a176d88c9deee241fe629d4df, poolComplete: false, 81 candidates, zero available candidates, 19 required inputs, and zero unresolved inputs. The adapter documents score-only analysis, raw scores without normalized selection probabilities, and available = { always = no } mission surfaces. Artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d532e6fc83ed7eb3175f65c00cb5095fcbc2d344394d101f71362ab2834df549/63bc46f8075d4eb1a6a9569ee660e43d24c68def3c7900d5d149fc86db84a95c/probability-inspect-f85397565290.json.

The required chaosx_ai_probability_auditor specialist was invoked read-only and was instructed to run the Event 23 scenario workflow. Its MCP scenario pass remained running and was shut down before returning a final scenario artifact. Therefore no scenario-specific probability, sweep, or comparison result is claimed here. The exact blocker is incomplete specialist output, not a fabricated balance conclusion.

No hoi4.gui_rewrite or other write-capable MCP route was used because this task is explicitly read-only.

## Validation performed and skipped

Meaningful checks completed were current source reading, exact decision/mission counting, source predicate and effect cross-checks, cost-profile and texticon audit, current localisation/tooltips review, fresh event inspect/render, fresh native decision-window GUI inspect/render, attempted Event 23 window inspection, and probability-source inspection.

Skipped meaningful validation includes live gameplay, native nuclear delivery, aircraft-wing range/queue behavior, reactor completion/cancellation identity, save/load persistence, exact in-game decision-row count, and a completed scenario probability compare. The agent must not launch Hearts of Iron IV, and the installed MCP did not provide the missing decision route or a completed specialist probability artifact.

## Recommended implementation order

1. Enforce the six-visible-primary limit and remove the duplicate collapse selector before further balance work.

2. Replace random breakaway custody selection with a player-selected state target and add sov_nuclear_bombs_event_no_active_project to all breakaway decision and effect entry guards.

3. Decide whether delivery-crews certification is a hard route prerequisite, then align the shared route predicate, target tooltips, and mission descriptions.

4. Add the missing security/supply/corridor gates or explicitly document the one-division threshold as accepted design.

5. Wire phase/site/target/remaining-deadline context into the existing ordinary category description and correct the one-device, target-registration, doctrine-reform, and partial-outcome localisation.

6. Re-run the Event 23 probability scenarios through chaosx_ai_probability_auditor with complete decision/mission candidate pools and retain before/after artifacts before claiming AI balance.

7. Repeat native GUI inspection/rendering after the production decision view is no longer clipped, and validate matching Event 23 scenarios across all required states.

## Changed files and identifiers

Changed file: docs/plans/023_sov_nuclear_bombs_plans/subagent_handoffs/023_decision_mission_auditor_final_2026-09-19.md.

No gameplay, workbook, asset, or localisation file was changed by this audit. No decision, mission, scripted GUI, or localisation identifier was added or renamed.

Plan handoff path: this audit handoff is the only handoff written; no additional plan file was created.

Final disposition: INCOMPLETE.

The source audit is actionable, but completion is blocked by the unresolved six-row and breakaway-stage issues, the random site selection, the missing decision-specific MCP route, the clipped production render, and the incomplete probability-auditor scenario result. These blockers must remain explicit until the owning implementation pass and parent review resolve them.
