# Event 029 seal safety postpatch review

Date: 2026-10-08.

Status: bounded read-only review complete for `decision_riches_found_gold_seal_depths` and `decision_riches_found_demons_permanent_seal`; the full seal-route acceptance remains open.

Acceptance basis: the user's current postpatch directions, Part 3's sealing actions, Part 4's Gold Disease and Demons Beneath the Mine routes, Achievement 7's The Last Shift conditions, and `docs/events/029_riches_found/seal_project_contract.md`.

No gameplay source, index, staging area, commit, game process, or child task was changed or started. This handoff is the only file created by this review. The unrelated `decision_riches_found_deny_mine` hunk in the shared decision file was left untouched.

The current physical SHA-256 of `common/decisions/029_riches_found_decisions.txt` is `88B2F6716F401657251BC79C8C144B081953D71725B81F693F630F28AEE36B8D`, matching the parent's reported current source identity.

## Findings by severity

### High: the accepted sealing routes are still incomplete

Part 3 requires control of shaft entrances and engineering capacity for `decision_riches_found_gold_seal_depths`, and requires control of entrances plus no active foreign or local force for permanent closure. Part 4 says Demons sealing success depends on evacuation, entrance control, sealed-depth integrity, and resistance from affected groups.

The existing composite affordability gates require two available civilian factories, 300 or 600 manpower, and 150 support equipment. Per the parent disposition, these are the concrete funded engineering-capacity inputs for the project; I do not report an absent engineering-capacity cost or propose an extra flag, supply/access cost, or fifth resource. Both decisions still lack the accepted entrance-control check. The Demons route also has no integrity-dependent success gate or affected-group resistance check. `riches_found_state_can_control_access` cannot be substituted directly because it requires an active mine and rejects closed or collapsed containment targets. No numeric integrity threshold is accepted by the cited design, so none is proposed here.

The missing entrance-control, integrity, and resistance checks remain blockers for claiming the complete sealing system, not regressions in the bounded terminal-gate, refund, and entombment repair. Keep them pending until route-compatible gates and player-facing blocked reasons are accepted and implemented. Native reservation of the two civilian factories after a stale click remains unproven.

### Medium: timed callbacks are not bound to a project generation

Both `remove_effect` blocks recheck the current payer, state registration, terminal status, route, and completion flags. They do not publish and consume a state/actor/family/generation receipt for the specific paid project, and `complete_effect` does not perform a second affordability and requirement preflight immediately before the debit.

If the state is controlled by another country when the timer resolves, `riches_found_mine_still_valid_for_payer` rejects completion and the decision refunds the original actor. If control leaves and later returns before the timer resolves, the final state checks can pass again because no generation receipt records the intervening transfer. This is source-only reasoning, not a demonstrated in-game exploit. The parent contract already records generation-safe callback identity and native factory reservation after a stale click as unresolved limits.

Recommended follow-up, if the parent accepts this lifecycle requirement: bind each start and delayed resolution to one actor, state, decision family, and generation receipt, then consume it once or refund the original actor. Keep the accepted Gold route and the explicitly harmful military-purge route available while doing so.

### Low: Gold late resolution does not treat a contract flag as route loss

`riches_found_gold_route_is_restricted` checks quarantine, district quarantine, controlled access, or temporary closure. It does not test `riches_found_contract_active` or `riches_found_occupation_active`. A new contract by itself therefore does not reject a Gold callback if the payer still controls the registered mine and the Gold layer and restricted-access route remain. A controller transfer away from the payer is rejected by the shared payer check.

Part 3 and the parent seal contract do not state that a newly opened contract must invalidate deep-section sealing, so this is recorded as current behavior and a design question, not as a defect. The demonic permanent seal explicitly blocks both active contracts and occupation at entry and again at delayed resolution.

No P1 source regression was confirmed in the two patched decision blocks. The open high-severity item above concerns full-route completeness.

## Current behavior and lifecycle

`decision_riches_found_gold_seal_depths` now hides terminal mines in `visible`, `available`, and `target_trigger`. At delayed resolution it rechecks that the original payer still controls the registered nonterminal mine, that the Gold layer and a restricted route remain, and that deep sections are not already sealed. Failure refunds exactly 300 manpower and 150 support equipment to the original decision actor. Success records both sealing flags, preserves the existing one-time partial-seal guard, and applies the existing pressure reductions.

Gold sealing remains available for a localized Gold Disease route and is not emergency-only. The cited design does not authorize a new integrity number. Its two-factory commitment plus manpower and support-equipment costs are the accepted funded engineering-capacity package. The entrance-control requirement remains unimplemented, and the existing partial-seal helper does not establish it.

`decision_riches_found_demons_permanent_seal` now hides terminal mines at entry. At delayed resolution it rechecks original-payer control, registration and terminal status, the Demons layer, the cleared-district route, absence of an active contract or occupation, and absence of an already completed Demons seal. Failure refunds exactly 600 manpower and 150 support equipment to the original actor. Success sets the Demons seal receipt, calls `riches_found_record_entombment_harm`, and only then calls `riches_found_permanently_seal_mine` for generic cleanup.

The cleared-district helper intentionally accepts completed evacuation or military purge. A purge is not an evacuation. The permanent-seal tooltip aliases the ordinary seal consequence text and adds the explicit sentence that a military purge does not evacuate trapped crews.

For both decisions, the physical cost debits are top-level `complete_effect` effects, outside the targeted `FROM` state block. Failure refunds are likewise outside `FROM`, so the source layout places both debit and refund in the acting-country decision scope while successful mine effects execute inside the state target. The offline targeted-decision example uses `FROM` as the target inside `complete_effect`; this supports the source reading but does not prove engine callback ordering or player execution.

## Source-only edge cases

These are source traces, not gameplay or save observations.

| Case | Source result | Evidence class |
| --- | --- | --- |
| Controller differs when a delayed callback resolves | `riches_found_mine_still_valid_for_payer` fails its `is_controlled_by = ROOT` check; the action takes its failure branch and refunds its own manpower and support-equipment quote to the original actor. | Source-only |
| Controller changes away and back before expiry | The final state check can pass again if all current route flags match; there is no project-generation receipt. | Source-only limitation |
| New contract during Demons project | The delayed Demons gate rejects `riches_found_contract_active` and refunds the exact manpower and support-equipment debit. | Source-only |
| Occupation during Demons project | The delayed Demons gate rejects `riches_found_occupation_active`; a controller transfer also fails the payer-control check. | Source-only |
| New contract during Gold project | A contract flag alone does not remove the Gold route predicate; the Gold callback may still resolve while the original actor controls the state and the Gold restriction remains. No accepted source requirement makes this a failure case. | Source-only behavior, design remains open |
| Already sealed before delayed resolution | `riches_found_gold_depths_sealed` or `riches_found_demons_permanent_seal` blocks success, and the corresponding paid costs are refunded. | Source-only |
| Gold restriction lost before delayed resolution | The Gold callback re-evaluates `riches_found_gold_route_is_restricted`; if none of its four route flags remain, it refunds. | Source-only |
| Mine terminal before delayed resolution | The shared payer trigger rejects `riches_found_mine_terminal`; both decisions refund. Terminal entry is also hidden by the new decision gates. | Source-only |
| Workforce and district evacuation flags both set | `riches_found_seal_would_entomb_workforce` is false; either evacuation flag alone also prevents entombment harm. The dedicated Last Shift route still requires its mission receipts. | Source-only |
| Deposit exhausted without evacuation | The entombment predicate is false; the seal does not add entombment deaths, order loss, or legitimacy loss. | Source-only |
| Military purge with no evacuation | The purge satisfies `riches_found_demons_district_cleared`, so the permanent seal remains selectable. If a severe-collapse or supernatural crisis remains, the deposit is not exhausted, and neither evacuation flag is present, the conditional entombment helper records the trapped shift before cleanup. The purge's own harm and the Last Shift purge disqualifier remain independent. | Source-only |
| Entombment helper called again | `riches_found_entombment_harm_recorded` is checked before mutation and set before the harm transaction, so a repeated call does not repeat deaths, order loss, or legitimacy loss. | Source-only |
| Last Shift after unsafe sealing | The pre-cleanup helper sets `riches_found_workforce_entombed`; generic cleanup preserves achievement history; the timer refresh invalidates the route, and the achievement trigger independently rejects entombment, military purge, mass death, an account history, agreement/exploitation, or a reopened tunnel. | Source-only |

### Temporary-variable call path

`riches_found_record_entombment_harm` creates the `riches_found_harm_*` inputs in the state target and calls `riches_found_apply_harm_record` immediately. That helper creates its `state_civilian_population_loss_*` input and output storage before calling `apply_exact_state_civilian_population_loss`, then persists the applied result as a normal state variable. `riches_found_record_entombment_harm` does not consume a temporary output from a returning helper. No temporary-variable caller-lifetime defect was found in this source path.

This is a source-level scope and storage review. No runtime callback or helper execution was observed.

## Decision category, cognitive load, and mission quality

`riches_found_mine_management` is an ordinary decision category with a static category picture, no attached Event 029 scripted GUI, and `visible_when_empty = no`. It is visible while the country controls at least one registered mine. A controlled terminal mine remains registered, so the category stays visible for that sealed site and closes when the controller has no registered mine. The category predicate does not independently preserve visibility for a claim or short aftermath action after the country loses every registered mine; that broader category lifecycle was not changed in this bounded review.

The two in-scope sealing decisions contribute two visible actions. The total category action count and total simultaneous mission count were not audited because the task is restricted to the two named decisions and their direct Last Shift dependency. The two cost rows each show three values. Their tooltips state the timed factory commitment and the output consequence, and the decision descriptions are concise. Gold's visible pressure decrease is paired with a qualitative explanation that compulsion recedes and stable upper workings remain in production. The permanent seal explains the output loss and conditional human harm. No raw mechanic-variable dump or new player-facing meter was introduced.

| Mission | Owner | Category | Region | Requirement | Duration | Success | Failure/partial result | Duplicate risk |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `mission_riches_found_evacuate_workforce` | Current mine controller, through the country decision system | `riches_found_mine_management` | The controlled mine state carrying `riches_found_mission_evacuate_workforce_subject` | Evacuation authorization and route preparation; nonterminal mine; active evacuation route; rail or port route; deadline reached | 30-day preparation decision followed by a 270-day native mission timeout | Marks district and workforce evacuated, records the dedicated Last Shift evacuation receipts, lowers supernatural pressure, raises local order, and reduces development | Partial success if the route remains active at timeout; otherwise failure. Both timeout paths clear the live mission state and invalidate Last Shift. | Preparation/subject flags, active-route checks, and the shared mission-slot gate prevent a second setup for the same mine. |

The mission title and description are generic and do not name the mine state. The state-subject marker and selected-mine flow scope the route in source, but native mission-list presentation was not rendered, so the player's region-level disambiguation remains unverified when multiple mines are controlled.

## Cost, requirement, localisation, and AI audit

| Decision | Spendable costs | Timed commitment | Ongoing output loss | Count | Inline texticons |
| --- | --- | --- | --- | ---: | --- |
| `decision_riches_found_gold_seal_depths` | 300 manpower and 150 support equipment | 2 civilian factories for 60 days | Lower workings stay sealed and output is reduced | 4 | `£civ_factory`, `£manpower_texticon`, `£support_equipment_text_icon` |
| `decision_riches_found_demons_permanent_seal` | 600 manpower and 150 support equipment | 2 civilian factories for 90 days | Mine output ends permanently | 4 | `£civ_factory`, `£manpower_texticon`, `£support_equipment_text_icon` |

Each cost composite is shared between `available` and `custom_cost_trigger`. The civilian-factory predicate, `manpower_k` thresholds, and exact `support_equipment` inventory token agree with the displayed and debited values in source. The three inline getters select the matching available/blocked texticons. The base, blocked, and tooltip localisation keys exist for each decision. No fifth spendable cost is hidden in a tooltip or callback. Foregone output is included as the fourth cost type in this audit; conditional entombment is a consequence, not a spendable cost.

The civilian-factory, manpower, and support-equipment bundle is the accepted funded engineering-capacity investment. Do not add a separate engineering flag or another resource payment unless accepted design explicitly requires it. The native factory modifier and free-factory affordability gate are source-visible, but atomic reservation behavior remains unproven.

The affected localisation keys are `decision_riches_found_gold_seal_depths_tt`, `riches_found_cost_gold_seal_depths`, its blocked and tooltip aliases, `decision_riches_found_demons_permanent_seal_tt`, `riches_found_cost_demons_permanent_seal`, its blocked and tooltip aliases, and the shared `decision_riches_found_permanent_seal_tt`. The latter names up to 220 civilian deaths, Local Order loss, Revenue Legitimacy loss, public condemnation, and the no-loss evacuation/exhaustion cases. Requirement flags used by the decision are localized in `029_riches_found_requirement_flags_l_english.yml`.

The demonic AI block now has the same `riches_found_seal_would_entomb_workforce` low-willingness and democratic never-willingness conditions as the ordinary permanent seal. I checked only that the guards are present. Numeric willingness, candidate ranking, and `hoi4.probability_compare` belong to the parent's separate `chaosx_ai_probability_auditor` pass and are not validated here. The decision-inspection report carried an AI subartifact; I did not open or interpret it.

## Evidence and validation limits

`hoi4.decision_inspect` live schema revision was read from the connected `mcp__hoi4_agent_tools__hoi4_decision_inspect` tool. One bounded scenario, `gold_at_cost_floor`, used a typed `FROM` state scope, a typed controller binding, `controls = { "1" = GER }`, and cost inputs of 2 available civilian factories, 0.3k manpower, and 150 support equipment.

That call returned `DECISION_ANALYZED_PARTIAL`, `complete = false`, 100 unresolved definitions, and a source revision of `ca6ddb815d70394ce8b27aeb1c14cf580f90603b348ed00cdcf5c272c9556275`. The three Gold affordability predicates resolved true at the supplied cost floor. Overall availability and category visibility remained unresolved because the adapter did not resolve `is_controlled_by`, `CONTROLLER.exists`, the selected-mine state pointer versus `PREV`, or the category's `any_controlled_state` scan. Its custom-cost amount was null and its direct `paymentEffects` list was empty, so the analyzer did not model the manual debit or refund even though those effects are present in source.

The linked decision artifact was assembled from seven contiguous byte-range reads. The returned byte count was 83,751 and its SHA-256 matched `e6de389f1300e3ef29ed5f6e22962c6282dc511e0581be0ef015907842a4fc89`. Artifact URI: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e6de389f1300e3ef29ed5f6e22962c6282dc511e0581be0ef015907842a4fc89/9313dc9379dbc21643a476b40453bca854117f021e6ef00f006e2f4755b45913/decision-6e333514cf4794a00a69dd54.json`.

A second typed decision-inspection request for `decision_riches_found_demons_permanent_seal` used the 2-factory, 0.6k-manpower, 150-support quote and a purge-only `FROM` state. It did not return after several minutes and was stopped; there is no Demons MCP scenario result. Source-level case traces above remain explicitly source-only.

The category file contains only the ordinary category icon, static picture, and visibility triggers. It has no Event 029 `.gui` or `scripted_gui` window. `hoi4.gui_inspect` and `hoi4.gui_render` were each attempted with `windowName = riches_found_mine_management`; neither returned within approximately 60 seconds and both reads were stopped. There is no render artifact or visual evidence for native cost-row fit, clipping, or the generic evacuation mission's displayed region. This visual gate remains open; no renderer discrepancy is inferred.

No probability evaluator, sweep, or compare was run because the parent assigned the AI audit separately. No gameplay test, source test, save inspection, or game launch was performed. No source-only result is represented as live-game proof.

### Documentation and precedent references

- `docs/specs/029_riches_found_specs/029_riches_found_spec_part_3_decisions_missions_foreign_interference.md:556-595` covers the deep-section seal and permanent seal requirements, tradeoffs, and AI direction.
- `docs/specs/029_riches_found_specs/029_riches_found_spec_part_4_evolutions.md:871-895` covers the Demons permanent seal, evacuation, military purge, and human-cost rules.
- `docs/specs/029_riches_found_specs/029_riches_found_spec_part_6_assets_localisation_achievements.md:746-774` and `docs/specs/029_riches_found_specs/029_riches_found_achievement_prompt.md:285-322` define Achievement 7, its required evacuation/assistance/seal route, and its disqualifiers.
- `docs/events/029_riches_found/seal_project_contract.md` records the accepted bounded costs and the still-pending full-route requirements.
- Prior audit: `docs/plans/029_riches_found_plans/subagent_handoffs/seal_cost_audit_2026_10_07.md`.
- Offline `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md:284-356`, revision `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162`, documents custom cost display/payment and timed decision completion/removal behavior. Its targeted-decision example at lines 550-575 shows `FROM` as the target within `complete_effect`; `hoi4.reference_read(id=0499304c418c2c6245632e09df7aef24ea7bdf1c6e3c9b0adf9374c06451a81a, startLine=550, maxLines=26)` did not return after roughly 60 seconds, so the bounded local section was read directly.
- Installed `common/decisions/_documentation.md:1-46`, revision `5e7e686b5582f32c38d898d805e17171e88f3bfeee4a030deb1884f9726de019`, documents targeted-decision trigger scopes and frequency.
- Installed `documentation/dynamic_variables_documentation.md:469-471`, `557-559`, and `592-595`, revision `538525747f0c285062c9ce8db14b4e07c3cf6bac1013115fa4f57291cb4ebdda`, documents `manpower_k`, `num_equipment`, and `num_of_available_civilian_factories`.
- Installed `documentation/modifiers_documentation.md:2202-2206`, revision `00a0eca6d2b3a70ce4b8a0d38997dd609aa0c9349ddcd04c8cac92849425be7e`, lists `civilian_factory_use` as a country/war-production modifier.
- Vanilla `game:common/decisions/AST.txt:2-42`, `AST_union_strike`, uses `days_remove`, `modifier = { civilian_factory_use = 1 }`, and a delayed `remove_effect`. `hoi4.source_lookup` workspace-index revision: `ca6ddb815d70394ce8b27aeb1c14cf580f90603b348ed00cdcf5c272c9556275`.
- Offline `paradox_wiki/On actions - Hearts of Iron 4 Wiki.md:450`, local SHA-256 `6822ADC85A374A1C1364F2DEF6F32C6D66DA9FB0280319DDD6AF4B84B33D882A`, documents `on_state_control_changed` with new controller `ROOT`, old controller `FROM`, and state `FROM.FROM`. The local file hash was verified directly.
- `hoi4.source_lookup` returned the full `riches_found_record_entombment_harm` definition at `common/scripted_effects/029_riches_found_harm_effects.txt:193-210`, helper revision `2a3c080a629399d79a344a72d771a43495a6e91c3638ed0aa7e689cee4d4907d`.

## Handoff summary

Files changed by this review: only `docs/plans/029_riches_found_plans/subagent_handoffs/seal_safety_review_2026_10_08.md`.

Gameplay ids reviewed: `decision_riches_found_gold_seal_depths`, `decision_riches_found_demons_permanent_seal`, `mission_riches_found_evacuate_workforce`, `riches_found_record_entombment_harm`, and `riches_found_achievement_last_shift_route`.

The bounded source changes preserve the intended four-cost profiles, terminal gates, delayed matching-route checks, exact manpower/support-equipment refunds, conditional entombment receipt before cleanup, the military-purge route, and Last Shift disqualifiers. The complete route remains incomplete, GUI visual evidence is unavailable, the second decision-inspection result is unresolved, and AI numeric validation remains parent-owned.

No separate plan was written. The requested handoff is this file.

## Follow-up finding and disposition: Gold sealing pressure tooltip

The earlier `decision_riches_found_gold_seal_depths_tt` reported the explicit eighteen-point Extraction Pressure reduction without the conditional pressure increase that can happen first. In `common/decisions/029_riches_found_decisions.txt:7018-7028`, the delayed effect calls `riches_found_begin_partial_seal` only when the mine has no existing partial seal and `riches_found_mine_can_begin_temporary_closure` is true, then applies the explicit negative-eighteen effect. The helper at `common/scripted_effects/029_riches_found_effects.txt:2513-2524` adds `constant:riches_found_scaling.partial_seal_pressure_add`, whose current value is twelve at `common/script_constants/029_riches_found_constants.txt:827`.

When that guarded branch creates a partial seal, the ordered pressure effects are plus twelve followed by minus eighteen, with the existing meter boundaries applied by the helper and final refresh.
Away from those boundaries, this produces six points of net relief; it is not a universal six-point change at the meter's limits.
If the mine already has a partial seal or cannot begin that closure step, this decision does not add the twelve-point strain and applies only the explicit eighteen-point relief, subject to the existing lower bound.

Disposition: implemented in the current shared worktree, with this review update recording the implementation evidence and limits. The parent changed only `decision_riches_found_gold_seal_depths_tt` in `localisation/english/029_riches_found_decisions_l_english.yml` to disclose the conditional strain before the relief, and added two matching explanatory sentences to `docs/events/029_riches_found/seal_project_contract.md`. No gameplay effect, AI coefficient, cost, or probability changed. The tooltip correction is pending its own commit.

The bounded English value was checked as decoded from the current UTF-8-with-BOM file. Its two color pairs contain eight marker characters across `§G`, `§!`, `§R`, and `§!`, represented by four actual U+00A7 section signs. No U+00A3 texticon or Unicode escape sequence is expected or present in this effect tooltip. The authored escaped line break remains intact in the localisation value.

No MCP or probability query was repeated for this copy correction. The earlier no-P1 finding and all prior source-only edge cases remain unchanged.

Parent publication: the tooltip correction and its two contract sentences are committed as `92ce42facc32e03af11ecfe04dc756492d1bdc16`.
This supersedes only the earlier pending-commit statement; the source and engine-evidence limits remain unchanged.
