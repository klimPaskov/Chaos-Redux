# Event 012 W5 receipt trace and owner handoff

Status: blocked and intentionally read-only. No gameplay source, readiness flag, receipt, tag, map binding, asset, model, or fallback was added in this trace.

## Scope and evidence

The trace covered `common/scripted_triggers/012_africa_world_order_triggers.txt`, `common/scripted_effects/012_africa_world_order_effects.txt`, `common/decisions/012_africa_decisions.txt`, `events/012_africa_world_order.txt`, the six world-package focus files, `common/ideas/012_africa_world_order_ideas.txt`, the world AI profile and route-plan files, the Event 012 world-order specification, the W0-W4 handoffs, and the W5 atomic-certification addenda.

A refreshed read-only `hoi4.event_inspect` trace for `africa_world_order.110` returned `EVENT_INSPECTED_PARTIAL` with no source changes and a workspace-wide projection containing 17 blocking diagnostics. The linked artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7e4af70be155b1c52e893099719d884198d80946967becabba1892e6a5e8acec/eea8f60c58279d06c88eef90870c30c97fa2c23121bf7c9f58f81b751d373c61/event-trace-54c80fc8baf0.json`.

The MCP projection is structural evidence only and is not used to claim a certification pass. Direct source inspection is decisive for the readiness writer and receipt-contract finding.

## Current gate and writer trace

| Surface | Current owner and evidence | W5 consequence |
| --- | --- | --- |
| Candidate admission | `africa_world_register_current_candidate` in `common/scripted_effects/012_africa_world_order_effects.txt:17` accepts a live non-subject, non-African, non-special-chaos country with a controlled capital and generic or explicitly approved focus surface, then sets `africa_world_package_candidate`, `africa_world_continent_id`, status, and starting metrics. | This is nomination evidence only; it is not a complete package receipt. |
| Frozen roster | `africa_world_nominate_missing_package_candidates` calls `africa_world_finalize_package_roster` at `common/scripted_effects/012_africa_world_order_effects.txt:125`; the finalizer records one disposition for each constant `africa_world_continent.middle_east` through `.oceania`, updates the host arrays and counters, and sets documented/partial/incomplete/complete roster flags. | The roster is the safest future certification boundary, but the finalizer currently does not certify readiness. |
| Existing readiness writer | `africa_world_commit_package_successor` sets `africa_world_package_implementation_ready` at `common/scripted_effects/012_africa_world_order_effects.txt:1781` while transferring an already installed package to a valid successor. | This is successor continuity and must remain separate from initial W5 certification. |
| Action 85 target and installer | `africa_select_world_package_candidate_target` requires `has_country_flag = africa_world_package_implementation_ready` at `common/decisions/012_africa_decisions.txt:1719`; `africa_world_install_current_package` repeats that gate at `common/scripted_effects/012_africa_world_order_effects.txt:1945`. | Certification must only unlock Action 85; it must not install or mutate package state. |
| AI and sponsorship consumers | Action 85 AI target checks the same flag at `common/scripted_triggers/012_africa_ai_profile_triggers.txt:791`; the AI/action and sponsorship paths read it at `common/scripted_effects/012_africa_ai_profile_effects.txt:2717`, `common/scripted_effects/012_africa_action_effects.txt:3782`, and `common/scripted_triggers/012_africa_world_sponsorship_triggers.txt:36`. | No AI-only or sponsorship-only readiness setter is safe. |
| Africa-only closure | `africa_scramble_can_close_continental_docket` vetoes a candidate carrying the readiness flag at `common/scripted_triggers/012_africa_world_order_triggers.txt:769`. | Partial promotion would create the exact closure deadlock that the atomic rule is intended to prevent. |
| Terminal presentation | `africa_terminal_world_identity_can_commit` requires the separate global `africa_the_world_super_event_package_ready` at `common/scripted_triggers/012_africa_world_order_triggers.txt:829`; the identity effect repeats the gate at `common/scripted_effects/012_africa_world_order_effects.txt:3275`. | W5 must leave the super-event flag and terminal presentation closed. |

The current runtime therefore has eight references to `africa_world_package_implementation_ready`, one of which is the successor-only writer and seven of which are reads. There is no initial all-six writer. There is no `set_global_flag = africa_the_world_super_event_package_ready` in `common/` or `events/`.

Event `africa_world_order.110` at `events/012_africa_world_order.txt:353-367` only acknowledges the deferred docket by setting `africa_world_package_roster_review_noted`. It is not a W0-W4 implementation review receipt and cannot substitute for one.

## Exact six-package input trace

The shared registry defines six required slots in `common/script_constants/012_africa_world_order_constants.txt:23-35` and `required_package_count = 6` at `:149`. The eventual trigger must receive one valid candidate and one authoritative receipt bundle for each slot.

| Slot | Candidate/package identity and authored surfaces | Existing post-install proof that was traced | Missing pre-install receipt inputs |
| --- | --- | --- | --- |
| Middle East (`constant:africa_world_continent.middle_east`) | Package flag `africa_world_middle_east_package`, focus tree `africa_middle_east_world_focus_tree`, AI profile `africa_ai_profile_world_middle_east_is_active`, and six authored idea pictures such as `africa_world_middle_east_federal_compact`. | `africa_world_package_route_is_grounded` accepts `africa_crossroads_command_settlement_ratified` or an `africa_middle_east_*_route` flag; shared lanes require `africa_crossroads_command_settlement_ratified`, `africa_crossroads_red_sea_nile_treaty_ratified`, and `africa_crossroads_settlement_congress_complete`. | No route-registration receipt, constituent-protocol receipt, AI/external-plan receipt, focus-tree receipt, idea-sprite receipt, identity/flag receipt, or shared review receipt exists before installation. |
| Europe (`constant:africa_world_continent.europe`) | Package flag `africa_world_europe_package`, focus tree `africa_europe_world_focus_tree`, AI profile `africa_ai_profile_world_europe_is_active`, and package ideas in `common/ideas/012_africa_world_order_ideas.txt`. | Route proof accepts `africa_europe_common_defence_ratified` or an `africa_europe_*_route` flag; shared lanes require `africa_europe_common_defence_ratified` and `africa_europe_post_colonial_treaty_ratified`. | The same seven pre-install receipt classes are absent. Existing route, shared-lane, idea, and identity flags are installed-actor outputs. |
| Asia (`constant:africa_world_continent.asia`) | Package flag `africa_world_asia_package`, focus tree `africa_asia_world_focus_tree`, AI profile `africa_ai_profile_world_asia_is_active`, and package ideas in `common/ideas/012_africa_world_order_ideas.txt`. | Route proof accepts `africa_asia_food_river_board_ratified` or an `africa_asia_*_route` flag; shared lanes require `africa_asia_food_river_board_ratified`, `africa_asia_corridor_settlement_ratified`, and `africa_asia_indian_ocean_partnership_ratified`. | The same seven pre-install receipt classes are absent. `africa_world_package_ratification_is_proven` cannot help because it requires installation. |
| North America (`constant:africa_world_continent.north_america`) | Package flag `africa_world_north_america_package`, focus tree `africa_north_america_world_focus_tree`, AI profile `africa_ai_profile_world_north_america_is_active`, and package ideas in `common/ideas/012_africa_world_order_ideas.txt`. | Route proof accepts `africa_north_america_two_ocean_defence_ratified` or an `africa_north_america_*_route` flag; shared lanes require `africa_north_america_two_ocean_defence_ratified`, `africa_north_america_islands_settlement_ratified`, and `africa_north_america_africa_diaspora_treaty_ready`. | The same seven pre-install receipt classes are absent. The four voluntary-diaspora flags are runtime play-loop outputs, not certification receipts. |
| South America (`constant:africa_world_continent.south_america`) | Package flag `africa_world_south_america_package`, focus tree `africa_south_america_world_focus_tree`, AI profile `africa_ai_profile_world_south_america_is_active`, and package ideas in `common/ideas/012_africa_world_order_ideas.txt`. | Route proof accepts `africa_south_america_resource_debt_law_ratified` or an `africa_south_america_*_route` flag; shared lanes require `africa_south_america_resource_debt_law_ratified`, `africa_south_america_continental_defence_settled`, and `africa_south_america_south_atlantic_partnership_ratified`. | The same seven pre-install receipt classes are absent. The three-region balance trigger is explicitly installed-actor scope. |
| Oceania (`constant:africa_world_continent.oceania`) | Package flag `africa_world_oceania_package`, focus tree `africa_oceania_world_focus_tree`, AI profile `africa_ai_profile_world_oceania_is_active`, and package ideas in `common/ideas/012_africa_world_order_ideas.txt`. | Route proof accepts `africa_oceania_pacific_reserve_ratified` or an `africa_oceania_*_route` flag; shared lanes require `africa_oceania_pacific_reserve_ratified` and `africa_oceania_africa_sea_treaty_ratified`. | The same seven pre-install receipt classes are absent. The Australia continent token is mapped to the Oceania slot only by the existing candidate/profile predicates. |

For each of the six rows, the exact pre-install receipt contract still needs authoritative identifiers for these six package-local inputs:

1. Grounded route registration.
2. Constituent protocol registration.
3. AI eligibility or external-route-plan registration.
4. Focus-tree registration beyond generic/replacement candidate admission.
5. Idea-sprite registration.
6. Identity/flag registration.

The shared contract also needs a localisation/asset/documentation acceptance receipt and one global W0-W4 review acceptance receipt. Static source existence, focus visibility, an AI plan name, an idea `picture`, a cosmetic tag, or a high-chaos review flag cannot stand in for those receipts. Script cannot prove human visual, localisation, documentation, or named-audit review through a numeric variable.

The six `africa_*_high_chaos_package_reviewed` global flags are route-specific focus/AI gates in `common/ai_strategy_plans/012_africa_focus_plans.txt`; they are explicitly deferred high-chaos controls and are not grounded package receipts.

## Safest future owner map and callsite

No narrow gameplay patch is safe until the receipt owners publish the missing identifiers. Once those receipts exist, the smallest owner map is:

| Helper | Scope and inputs | Output and side effects | Safe callsite |
| --- | --- | --- | --- |
| `africa_world_all_package_runtime_surfaces_are_certified` | Pure trigger in `common/scripted_triggers/012_africa_world_order_triggers.txt`; host scope, frozen `africa_world_package_candidates` array and counters, six candidate scopes, the six constant continent IDs, and the exact receipt identifiers. | Boolean all-six result only. Require exactly six distinct live candidates, one per slot, valid candidate/base checks, controlled non-African capitals, no absent/resolved/installed entries, no successor/exile/breakup/terminal/pending state, no partial/high-chaos substitution, and every runtime receipt. | Recheck immediately after the reviewed `africa_world_finalize_package_roster` freeze in `africa_world_nominate_missing_package_candidates`, before Action 85 is available. |
| `africa_world_certify_all_package_runtime_surfaces` | Host effect in `common/scripted_effects/012_africa_world_order_effects.txt`; re-evaluate the trigger and iterate only the frozen candidate array with a bounded `for_each_scope_loop`. | Set `africa_world_package_implementation_ready` on all six current candidates or on none. Do not install, transfer territory, load a focus tree, complete a focus, set a route, grant sovereign proof, create a tag, or touch terminal flags. | The reviewed post-freeze callsite above, with the effect itself repeating the trigger as an atomic guard. |

`africa_world_install_current_package` remains the only initial installation lifecycle, `africa_world_commit_package_successor` remains the only continuity transfer, and Action 90 remains behind the independent terminal presentation gate. No event target or global receipt target is needed while the host-owned candidate array is the durable bounded roster, and no recurring world scan is authorized.

## Why no patch was applied

The candidate path currently exposes only nomination facts: a valid country, continent ID, controlled capital, generic or replacement-approved focus surface, and host roster membership. `africa_world_package_route_is_grounded`, `africa_world_package_shared_lanes_are_proven`, and `africa_world_package_ratification_is_proven` each require `africa_world_package_is_installed = yes`. The polity foundation and constituent registration helpers likewise start only after installation. The six focus capstones also require installed actor proof before recording package ratification and final identity.

Adding the proposed trigger now would either infer certification from static files or invent unowned flags, and calling the successor writer would incorrectly model initial certification as continuity. Both violate the accepted W5 atomic rule. The current install source does remove an installed candidate from `africa_world_package_candidates` at `common/scripted_effects/012_africa_world_order_effects.txt:1981`; an older completion-delta handoff reports that as stale, but the current source was rechecked and no repair is requested here.

## Validation and remaining work

Read-only searches confirmed one successor-only implementation-ready writer, seven runtime reads, no initial certification helper, and no super-event readiness setter. Source trace confirmed the six continent constants, the six roster slots, the Action 85 gate, the separate terminal gate, and the installed-only boundaries of route, lane, ratification, polity, and identity proof. The refreshed MCP event trace is partial and workspace-bounded, so it does not change the source conclusion.

The blocker is the absence of authoritative pre-install identifiers for grounded route, constituent protocol, AI/external plan, focus, idea, identity, localisation/asset/documentation acceptance, and global W0-W4 review. The parent must accept those receipts in their owning systems before adding the pure trigger, atomic setter, and reviewed post-freeze callsite. No fallback, partial promotion, terminal flag, or gameplay edit is justified in this tranche.
