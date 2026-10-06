# Event 24 Emergency Restriction Prepatch Baseline

Audit date: 2026-10-03.

Workspace: C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux.

Status: incomplete, bounded source-only baseline. The required child probability-inspect route was attempted first but was not callable in this child registry. No request reached an MCP server. The parent has not relayed a valid inspect result for this emergency-restriction surface. There is no poolComplete result, scenario hash, analysis ID, render URI, or numerical balance signoff.

This baseline is separate from the 79-comparator comparison in handoff 14. It is bound to the parent-preserved 2026-10-03_pre_emergency_restriction snapshots, which include the current cleanup, civil-war, commander, and controlled-debrief state before the emergency-restriction patch. The 2026-10-03_post_exact_state snapshots remain unchanged and continue to define only the earlier 79-comparator comparison.

No gameplay, AI, event, decision, effect, trigger, constant, localisation, asset, or runtime file was edited by this auditor. No commit was made and the game was not launched.

## Accepted emergency-restriction intent

The accepted source is docs/specs/024_video_game_in_sweden_specs/024_video_game_in_sweden_spec_part_2_evolutions.md and docs/specs/024_video_game_in_sweden_specs/024_video_game_in_sweden_decision_map.md. They define Restrict Official and Public Use as the fastest and safest resolution when Sweden is collapsing or lacks the resources for a Reality Audit. The decision map calls political power optional.

The preserved scenario IDs are P24-C5 and P24-C7. No new IDs are introduced here.

The owner-defined patch target, recorded without endorsement or modification, is to quote the nominal 30 political power only when affordable and otherwise quote 0, quote Stability as the lesser of 4% and the available amount, quote War Support as the lesser of 3% and the available amount, show the quote with the existing political power, Stability, and War Support icons, and pay exactly that quote atomically. The owner states that nominal fees and AI weights remain unchanged. The owner also directs that the three reassessment options, four Evolution III initial choices, and 90-day restriction duration remain unchanged.

## Immutable prepatch source identities

The parent preserved these seven source copies before the owner patch. This auditor verified their current file hashes and read the frozen sources. These identities describe the current prepatch baseline, not the older post_exact_state comparison.

| Snapshot path | Bytes | SHA-256 |
| --- | ---: | --- |
| docs/plans/024_video_game_in_sweden_plans/probability_snapshots/2026-10-03_pre_emergency_restriction/024_hearts_of_iron.txt | 34,317 | 75e81ff4f8889a30957f23bc67a473f617fc4238b8dda07eca0a6edb8693798c |
| docs/plans/024_video_game_in_sweden_plans/probability_snapshots/2026-10-03_pre_emergency_restriction/024_video_game_in_sweden_effects.txt | 122,620 | 09cc1d0ebbf726289129cd831d6db4348ead725907e9a25a6f5d3316ef6920a2 |
| docs/plans/024_video_game_in_sweden_plans/probability_snapshots/2026-10-03_pre_emergency_restriction/024_video_game_in_sweden_triggers.txt | 29,557 | 97e110186baae1922fd837d57a8ad4f3f8e7655b94b0344b490aef7a273776ac |
| docs/plans/024_video_game_in_sweden_plans/probability_snapshots/2026-10-03_pre_emergency_restriction/024_video_game_in_sweden_decisions.txt | 38,595 | dc1ea5273d6f22cfe8361c8d8ba176d344fc4ba98865f62a2145455d694f7f30 |
| docs/plans/024_video_game_in_sweden_plans/probability_snapshots/2026-10-03_pre_emergency_restriction/024_video_game_in_sweden_constants.txt | 14,364 | 622621c00d24cf036cf3fec3f1f82949db6d92b3af4701af396bef4e132d632c |
| docs/plans/024_video_game_in_sweden_plans/probability_snapshots/2026-10-03_pre_emergency_restriction/024_video_game_in_sweden.txt | 12,209 | a0b0c2726ffa3adba7dbe40080e8b5b2b98bd35051eae351e773de1ba6723b08 |
| docs/plans/024_video_game_in_sweden_plans/probability_snapshots/2026-10-03_pre_emergency_restriction/024_hearts_of_iron_l_english.yml | 43,150 | 13eb7d9ba4a784068ed5c5ceadc55d3a59342b11e4ca61101e77f49e238797d7 |

The old 79-comparator comparison remains bound to its original post_exact_state copies. Those seven files were rehashed during this baseline and still match the identities recorded in handoff 14. No source drift was found in those immutable comparison inputs.

## Required probability inspect attempt and blocker

The first audit request was a read-only probability inspect for the complete local reassessment option pool against the frozen current prepatch event source:

- adapter: event_option_ai_chance
- source.path: docs/plans/024_video_game_in_sweden_plans/probability_snapshots/2026-10-03_pre_emergency_restriction/024_hearts_of_iron.txt
- candidatePool: chaosx.nr24.50.a, chaosx.nr24.50.b, chaosx.nr24.50.c
- refresh: true
- workspaceId: mod_chaos_redux_ea3b2d67c2c0

The child attempted mcp__hoi4_agent_tools__hoi4_probability_inspect with those arguments. It returned TypeError: mcp__hoi4_agent_tools__hoi4_probability_inspect is not present in this child tool registry. No request reached an MCP server. This records the exact child-route blocker and does not assert that the parent route is absent.

The matching child event_inspect trace and event_render options lookups for chaosx.nr24.50 were also unavailable in the child registry. They produced no structural artifact or render. The parent has not relayed a probability inspect result for this .50 pool. The prior .20 inspect status in handoff 14 is unrelated and does not establish .50 pool coverage.

No probability_evaluate, probability_sweep, probability_compare, or probability_render result is available for this prepatch baseline. No source revision, candidate eligibility trace, poolComplete field, unresolved-row artifact, scenario hash, analysis ID, comparison ID, or rendered URI was returned.

## Weighted surface and exact source pool

The event option pool is complete at the source-definition level. MCP poolComplete is unknown. ai_chance values below are raw source scores, not normalized selection probabilities.

| Option ID | Current source gate | Raw ai_chance base | Named raw modifiers |
| --- | --- | ---: | --- |
| chaosx.nr24.50.a Reality Audit | can_begin_reality_audit and can_pay_reality_audit | audit_crisis = 3.5 | supply-crisis factor 2.0, then route factors controlled 1.2, commercial 0.8, officer 1.0 |
| chaosx.nr24.50.b Dual-Track | can_use_dual_track and can_pay_dual_track | 2.0 | stability factor 1.6 when Stability exceeds 0.50, then route factors controlled 1.1, commercial 0.8, officer 1.4 |
| chaosx.nr24.50.c Restrict Use | can_restrict_use and can_pay_restriction | restrict_crisis = 4.0 | route factors controlled 1.1, commercial 1.0, officer 0.9 |

These values are score evidence only. No factors were multiplied by hand. An option contributes to an event selection only if its trigger passes. Exact conditional shares require a complete eligible pool and bound external state.

The normal decision video_game_restrict_use is a separate ai_will_do score race. Its source base is restrict_crisis = 4.0 with crisis, peace, and route modifiers. It calls the same affordability helper in available and custom_cost_trigger and declares ai_hint_pp_cost = 30. The decision score is not a click probability. No complete 18-decision adapter result was returned.

## Current affordability and payment contract

The frozen scripted trigger video_game_in_sweden_can_pay_restriction at common/scripted_triggers/024_video_game_in_sweden_triggers.txt:145-149 currently requires:

- at least 30 political power
- at least 0.04 Stability
- at least 0.04 War Support

The source constants are restriction_political_power = 30, restriction_stability_gate = 0.04, restriction_war_support_gate = 0.04, restriction_stability_loss = -0.04, restriction_war_support_loss = -0.03, and restriction_days = 90 in common/script_constants/024_video_game_in_sweden_constants.txt.

video_game_in_sweden_pay_restriction in common/scripted_effects/024_video_game_in_sweden_effects.txt:751-765 contains separate conditional payment blocks. Political power is subtracted when its threshold passes. Stability and War Support are then changed independently when their respective gates pass. This source path is not an atomic quote and payment transaction.

The normal decision cost text in localisation/english/024_hearts_of_iron_l_english.yml:222-224 displays political power, Stability, and War Support using their three existing texticons. It shows 30 political power, 4% Stability, and 3% War Support. The tooltip lists 4% minimum reserves for both Stability and War Support, then a further 3% Stability loss from enforcement through backlash_stability_display = 3. The source effect is backlash_stability = -0.03. The decision source uses the same affordability helper and a 30-point ai_hint_pp_cost.

## Declared audit scenarios and unresolved inputs

The scenario facts below are audit assumptions supplied for P24-C5 and P24-C7. Numeric values are not confirmed native campaign state. Scope and currency binding remain unresolved.

| Scenario ID | Declared fact values | Additional state assumptions | Unresolved native inputs |
| --- | --- | --- | --- |
| P24-C5, Evolution III after supply failure | phase 4, route 1, current_incident 0, last_incident 2, political power 0, Stability 0.02, War Support 0.01, fuel 0, trains 0, support equipment 0, army experience 0, command power 0 | Valid Swedish host, no active mission, prior supply-family incident, supply failure and lost core | ROOT and Swedish host scope binding, actual country and state ownership/controller facts, Evolution III active and enabled flags, current supply gap versus historical supply-crisis flag, has_war, resource fact mapping, available civilian project factories, event targets |
| P24-C7, near capitulation | phase 4, route 1, current_incident 0, last_incident 0, political power 0, Stability 0.02, War Support 0.01, fuel 0, trains 0, support equipment 0, army experience 0, command power 0, surrender progress 0.9 | Valid Swedish host, no active mission, near capitulation | ROOT and Swedish host scope binding, ownership/controller facts, Evolution III active and enabled flags, surrender-progress variable mapping, resource fact mapping, available civilian project factories, event targets |

The generic custom-pool envelope shape identified earlier is schemaVersion 1.0 with id and scenarios, where each scenario has id, label, and state containing named facts. It was found in docs/testing/runtime_repairs/20260913_cxt_history_followup/facility_probability_corrected/scenarios.json. That file proves custom-pool envelope shape only. It is not an accepted native Event24 scenario contract and does not prove native variable, ROOT-scope, host, flag, or currency mapping. No new scenario IDs, numeric array indices, or separate JSON fixture were created for this baseline.

## Bounded source result

Under the declared numeric assumptions, and only if they bind to the native country scope:

- P24-C5 and P24-C7 fail the current restriction affordability trigger because political power 0 is below 30, Stability 0.02 is below 0.04, and War Support 0.01 is below 0.04.
- Reality Audit fails its source affordability checks at zero Army Experience, support equipment, fuel, and trains. Its costs are 12 Army Experience, 100 support equipment, 750 fuel, and 8 trains. It also requires the field-start package and completed logistics and red-team flags.
- Dual-Track fails its payment checks at zero Army Experience and command power. Its source costs are 10 Army Experience, 20 command power, and one available civilian project factory. The factory input was not specified.

These are bounded source-gate findings, not adapter-confirmed eligibility. If the declared resource facts bind, the current three-option reassessment pool has no option that passes its source availability and affordability gates in either scenario. MCP poolComplete and engine scope binding are unresolved, so no normalized probability, option ranking, or exact starvation claim is made.

The source AI bases and modifiers are unchanged under the planned patch according to the owner. The current normal restriction decision remains a score-only source result. Future timing and reliance-driven decision choices remain unbalanced and unvalidated. The proposed affordability repair is not applied or evaluated in this handoff.

## Owner-defined patch scope, not an auditor target

The owner has refined the political-power quote to the continuous amount min(nominal 30, available positive political power), avoiding a 29-versus-30 waiver cliff. The quote for Stability is min(nominal 4%, available Stability), and the quote for War Support is min(nominal 3%, available War Support). The displayed fees must be the actual clamped quote, use the same three existing texticons, and be paid atomically from a fresh quote. The owner intends no affordability floor gate, so the emergency choice remains financially answerable. This is the owner's choice within the accepted emergency-safety and optional-political-power direction, not an auditor-selected target.

At the declared zero political-power value in P24-C5 and P24-C7, both the earlier zero-or-30 proposal and the refined continuous quote produce zero political-power payment. The scenario IDs and all other baseline facts remain unchanged. The nominal fee caps and AI weights are unchanged by the owner's plan.

The owner states that all three .50 reassessment choices, all four Evolution III initial choices, and the 90-day restriction timer remain unchanged. This baseline does not validate those presentation or lifecycle claims after patch.

## Required AFTER inspect and compare after the owner patch

The immutable BEFORE event source for a later comparison is docs/plans/024_video_game_in_sweden_plans/probability_snapshots/2026-10-03_pre_emergency_restriction/024_hearts_of_iron.txt. The owner must preserve an immutable AFTER source and its related scripted-effect, trigger, decision, constant, scripted-localisation, and localisation files after the patch. The AFTER paths must be returned before the comparison.

Use the parent probability_inspect route first for adapter event_option_ai_chance and the complete chaosx.nr24.50.a, chaosx.nr24.50.b, chaosx.nr24.50.c pool. Then use probability_compare with the frozen BEFORE path and a new immutable AFTER path, never the same source on both sides, the same P24-C5 and P24-C7 named scenarios, and the same three-option pool. The custom-pool envelope is only a possible serialization reference if the parent confirms that the native compare route accepts it. Preserve the declared named facts, add no new scenario IDs or numeric array indices, and leave native binding unresolved. If native binding or pool completeness remains unresolved, report a bounded or unresolved comparison without a rank claim. The child-local probability route failure recorded above is distinct from parent-route availability.

## Installed dynamic-variable documentation

C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/dynamic_variables_documentation.md has SHA-256 538525747f0c285062c9ce8db14b4e07c3cf6bac1013115fa4f57291cb4ebdda. Lines 435-438 document has_stability as an availability trigger. Lines 439-442 document has_war_support as an availability trigger. Line 785 documents the stability dynamic variable. A targeted search found no standalone raw war_support dynamic-variable entry. Use the documented has_war_support trigger to test or quote available War Support. This documentation confirms token availability and range descriptions, not ROOT-scope or adapter field binding.

## Skipped analyses, blockers, and handoff status

- probability_inspect was attempted first through the child route and failed before dispatch with the exact TypeError above.
- The parent reports that probability_inspect for the frozen BEFORE .50 three-option pool was dispatched in cell79 and is awaiting a result. No parent inspect artifact or result has been relayed to this child.
- Parent-side evaluate, sweep, compare, and render results for this .50 baseline have not been relayed to this child.
- event_inspect and event_render child routes were also unavailable. The parent must relay any structural result separately.
- The complete source option list is three entries, but adapter poolComplete is unknown.
- Root scope, host identity, state control, native currency binding, crisis flags, event targets, and unlisted external state remain unresolved.
- No numerical selection probability, score normalization, ranking, starvation measurement, rank reversal, or balance signoff is reported.
- The current 79-comparator comparison remains separate and frozen to post_exact_state. No file under that folder was rewritten or used as this baseline.
- No tests, game launch, or runtime validation were performed.

Handoff status: source-only prepatch baseline recorded with the exact child inspect blocker. The parent BEFORE inspect is pending in cell79. The owner patch has not changed the preserved BEFORE source facts. A fresh AFTER snapshot and parent-side inspect/compare are required after patch. The 79-comparator AFTER set remains separate and unchanged. No gameplay changes or commit were made by this auditor.
