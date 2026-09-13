# Event 021 building comparison proposal

Disposition: accepted in principle and queued for parent release after review of this exact proposal.
Acceptance basis: the parent authorized this bounded read-only investigation and subsequently accepted the intended correction in principle from the documented vanilla factory tokens.
No gameplay source was written during this review.

## Exact proposed edits

Every comparison retains its current state scope, strict greater-than operator, and `constant:random_civil_war_value.zero` threshold.
No score constant, selector, array, cap, route, cost, or surrounding condition changes.

| File and line | Existing expression | Exact replacement | Classification |
| --- | --- | --- | --- |
| `common/scripted_triggers/021_random_civil_war_parent_triggers.txt:778` | `building_level@arms_factory > constant:random_civil_war_value.zero` | `check_variable = { building_level@arms_factory > constant:random_civil_war_value.zero }` | Missing variable wrapper only. |
| `common/scripted_effects/021_random_civil_war_parent_effects.txt:1163` | `building_level@civilian_factory > constant:random_civil_war_value.zero` | `check_variable = { building_level@industrial_complex > constant:random_civil_war_value.zero }` | Missing wrapper and wrong building-type token. |
| `common/scripted_effects/021_random_civil_war_parent_effects.txt:1164` | `building_level@military_factory > constant:random_civil_war_value.zero` | `check_variable = { building_level@arms_factory > constant:random_civil_war_value.zero }` | Missing wrapper and wrong building-type token. |
| `common/scripted_effects/021_random_civil_war_parent_effects.txt:3336` | `building_level@arms_factory > constant:random_civil_war_value.zero` | `check_variable = { building_level@arms_factory > constant:random_civil_war_value.zero }` | Missing variable wrapper only. |
| `common/scripted_effects/021_random_civil_war_parent_effects.txt:3376` | `building_level@arms_factory > constant:random_civil_war_value.zero` | `check_variable = { building_level@arms_factory > constant:random_civil_war_value.zero }` | Missing variable wrapper only. |

The score keys `constant:event021_anchor_weight.civilian_factory` and `constant:event021_anchor_weight.military_factory` are valid tuning names and must remain unchanged.
Only the two building-type arguments to `building_level@...` change.
Wrapping the current incorrect factory tokens alone would leave those checks aimed at building types absent from the inspected game and mod building definitions.

## Syntax and token evidence

- Installed vanilla `documentation/dynamic_variables_documentation.md:1096` introduces state dynamic variables, and line 1101 defines `building_level` with a building-type target and the example `building_level@arms_factory`.
- Installed vanilla `documentation/triggers_documentation.md:2110` documents `check_variable` and its short greater-than form.
- Installed vanilla `common/buildings/00_buildings.txt:55` defines `arms_factory` with `military_production = 1`, and line 70 defines `industrial_complex` with `general_production = 1`.
- Installed vanilla `localisation/english/buildings_l_english.yml:5` names `arms_factory` as Military Factory, and line 26 names `industrial_complex` as Civilian Factory.
- A definition search across installed vanilla and Chaos Redux `common/buildings` found no `civilian_factory` or `military_factory` building definitions.
- Installed vanilla `common/decisions/INS.txt:2009` uses `check_variable = { building_level@industrial_complex > INS_civs_pre_investment }` inside a state-scoped decision condition.
- Installed vanilla `common/decisions/GER.txt:293`–295 checks state factory variables inside `check_variable` and uses `building_level@dockyard` in the same form.
- Offline `paradox_wiki/Building modding - Hearts of Iron 4 Wiki.md` documents building identifiers declared under `buildings = { ... }`, while the required Data structures and Triggers pages document game variables and their comparison form.

No separate documentation file was found in the inspected vanilla or mod `common/buildings` directories.
The installed dynamic-variable documentation, building definitions, localisation, and decision precedents jointly establish the proposed tokens and access form.

## Complete helper and caller review

`event021_priority_front_depot_target_valid` checks the state stored in `random_civil_war_priority_front_state`.
It requires ROOT ownership and control, membership in ROOT's opening-core array, and either a supply node or a military factory.
The factory check remains inside that OR branch.
`event021_seize_depot` consumes this predicate for availability at decisions line 135, its guarded completion and cost effects at line 156, and its AI zero-factor exclusion at line 166.
The proposed wrapper therefore touches a real AI eligibility gate even though no numeric AI factor changes.

`event021_parent_score_anchor_state` is called in state scope from `event021_parent_select_connected_anchor` at parent-effects line 1183.
Its factory conditions award the existing civilian score of 8 and military score of 10 before the unchanged clamp and rounding.
The caller selects the highest score with `find_highest_in_array` from aligned arrays and preserves its existing tie/index handling.
Correcting the two building tokens restores the intended factory checks, which can change state rankings relative to broken checks.
It does not redefine the weights or convert the deterministic selection into a random pool.

`event021_parent_score_same_tag_node` is invoked from `capital_scope`, a stored anchor-state scope, and `every_owned_state` at lines 3353, 3360, and 3379.
Those actual callers establish state evaluation despite the nearby introductory country-scope comment for the broader same-tag system.
The factory branch adds the existing `constant:event021_same_tag_tuning.depot_node` value of 8 to the temporary node score.

`event021_parent_initialize_same_tag_contest` stores government and claimant node/score arrays and adds bounded owned and controlled claimant states with at least one supply-node, naval-base, infrastructure, or military-factory feature.
The line 3376 correction preserves that OR gate and the existing count cap.
Its entry point is the committed same-tag takeover at line 3403.
No scoring, leverage, membership cap, node selector, or registration logic is proposed for alteration.

No new helper, input, output, default, side effect, constant, event target, cleanup, or call-site migration is needed.
The existing dynamic helper registry and owner documentation were consulted, and extracting a new helper for these simple comparisons would expand this parser task unnecessarily.

## MCP evidence and limits

The Event 021 root trace/render evidence from `event21_infrastructure19_handoff.md` is reused as linked-chain context.
It is partial at revision `410c82bea077b36a7e01b4ed11eb4927d40357359aad54622f2b2adf58fea5cb`, with workspace-wide helper/lifecycle projections deferred.
It does not validate these proposed edits or the actual building-dependent gates.

The read-only probability auditor performed fresh narrow inspection for these helpers.
The priority-front depot trigger, same-tag scoring helper, and same-tag initializer returned `INTERNAL_ERROR` without artifacts.
The anchor scoring helper matched zero candidates, while the source inventory exposed only the separate random-list entries.
Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5e3517473cb6908c3d3f99f49be1b0ce8395b7f986997de8ce1c2d1d6d422bdd/95a5bd1e965ade1a971f591be41a0778dbfbbd3cc0e2eca6fd1b07f1f1b58ee9/probability-inspect-d3c0977c47cd.json`.

The explicit `decision_ai_will_do` inspection for `event021_seize_depot` returned `PROBABILITY_SOURCE_INSPECTED`, one decision surface, four required inputs, and `poolComplete: false`.
Source revision: `a48a7dedff6913c5ff45dfb5668db52dd6b77391dc53ece92d34e0a1441c66b6`.
Source hash: `f737e27647ca83d358f7878de14c5df11f9dae729264b141706b069051609385`.
Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e0689347b6947708cc93f61c9339f04ca735804660c172fdb84cd474216347b1/1cc8681c670495d7ea452a5ebe9b9a0cf82e0aecd737a9756c5d0b3feec38d1d/probability-inspect-f737e27647ca.json`.
Discovery does not project the nested depot predicate or supply a complete competing-decision pool.
No manual Boolean overrides, invented candidate pools, normalized probabilities, campaign ranking claims, or fixture-based gate proof were used.
No before-and-after comparison was run because this phase is read-only and no building correction was applied.
After release and application, the owning patch phase must request the matching probability comparison and retain any unsupported projection as unresolved.

## Release and validation notes

Observed source hashes remained `7F47BA3F4DCA0D1BFE1B7BF6C586CCECF41E16E112985A97222901911D7BAFD6` for parent triggers and `E84C38F6A64EE5C83E81E65AC4D5ED7768BBACBF43C28B4C6EBA0C0CBE6068F6` for parent effects.
These are the preceding infrastructure repair hashes, not building20 post-edit hashes.
The parent reported launch 19 ended with its tracked sources stable and the preceding seven infrastructure diagnostics absent.
That acceptance does not cover these unapplied building comparisons.

Before any implementation, create immediate full-byte backups and guard both current file hashes.
An inverse check must restore the exact five original expressions, including the two original factory aliases, and recover both original file hashes.
Meaningful source scenarios for subsequent review are civilian-factory-only, military-factory-only, both-factory, and neither-factory states, plus depot states admitted by the unchanged supply-node alternative.
Under the proposed conditions, the existing factory contributions are respectively 8, 10, 18, and 0 before clamping.
These are intended source-level consequences, not measured runtime results.

No gameplay simplification or fallback is proposed.
Implementation and native parser acceptance remain queued for the parent's release.
Actual nested-gate evaluation, deterministic campaign ranking, and decision AI probability remain unresolved by the available MCP projections.
Only this handoff file was created during the review.
No game launch, source write, or commit was performed.
Skills used: events, decisions/missions, and subagents, with the offline building-modding reference added for token verification.
No skills were created or changed.
