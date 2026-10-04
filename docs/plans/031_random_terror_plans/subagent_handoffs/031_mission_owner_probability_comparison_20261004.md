# Event 31 mission-owner AI/probability comparison

Status: the frozen-source read-only audit is complete, but the required numeric before/after comparison remains unresolved because the connected analyzer cannot recognize the immutable before snapshot as a weighted mission source.

No gameplay or localisation file was edited, no weight target was selected, no game was launched, no logs were requested or searched, and no Git operation was performed.

The parent confirmed the final freeze after adding the 24 callback-closure calls; the physical source hashes below match that frozen set.

After the MCP pass, the parent made one post-review correction to the unweighted Restore Services starter; the table below preserves the exact source set used by the prior MCP calls, and the current effects hash is recorded in the after-audit addendum at the end of this handoff.

The parent also reports that Restore Services now reserves slot 3, family, and target before its helper, and that country-recovery close rejects any occupied slot; these can affect eligibility, but the fixture does not bind the typed state needed to quantify their effect.

## Accepted scope and source files

The accepted design basis is `docs\specs\031_random_terror_specs\031_random_terror_decision_mission_matrix.md` and `docs\specs\031_random_terror_specs\031_random_terror_decision_mission_prompt.md`.

The baseline is `docs\plans\031_random_terror_plans\subagent_handoffs\031_mission_owner_probability_baseline_20261003.md`; its linked owner/progress contract was also read.

The baseline MCP inspect used source revision `e1a54a8fc0135b42af0c4355012499d6172dface7aedcf8da3b64f0e547d32bb` and analyzer source hash `15070be09547197f477201e0395367a5cc5c5323430e9529d80ea6e0f4f2b0f8`; its JSON artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fe20e6ff0a827c433b2949db1c650f76832493dbab4304acd3dd8a5211f35e88/e5568f8fc7b09dcd86c77d0cfee0d90f4adb81ee66c9e902698caca774736532/probability-inspect-15070be09547.json`.

The baseline evaluate artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5078537a298d6fae2b5c7a256591d27357a87a7d32c81e52e57502752e5323d1/24fa2a87f7c4ceae73f8384782abd6e3e0fe08174b1c872d0bf549ffae0b16fb/probability-0b8ba2b6dce3976b64c8b383.json`; its `analysisId` was `probability-0b8ba2b6dce3976b64c8b383` and its scenario hash was `11d242f0ff0b036d60c9f59bc21320c8d69fd43cf0728ee266f741f9a5d69edc`.

That baseline evaluation also had zero eligible candidates and 208 unresolved candidate rows; the final evaluation has zero eligible candidates and 208 excluded rows, so this change in analyzer disposition does not establish a score or probability improvement.

The audited surface is the eight Event 31 mission `ai_will_do` blocks in `common\decisions\031_random_terror_missions.txt`.

Supporting source reviewed for score inputs and scope writers: `common\decisions\031_random_terror_decisions.txt`, `common\scripted_effects\031_random_terror_effects.txt`, `common\scripted_triggers\031_random_terror_triggers.txt`, and `common\script_constants\031_random_terror_constants.txt`.

The final English source identity supplied by the parent and verified on disk is `localisation\english\031_terrorist_attack_l_english.yml`.

The physical before-source copies remain under `docs\plans\031_random_terror_plans\evidence\mission_owner_before_20261003\`.

| Source | Before SHA-256 | Final SHA-256 |
| --- | --- | --- |
| `common\decisions\031_random_terror_missions.txt` | `B24633FA4996FB2D25C44118C44A01F38B3C1C821DBCADF819FA71591813A71D` | `C775B7556270CFFAE07B33C1B8435D50B5990B1C8EA1383654E70C8458A71BD2` |
| `common\decisions\031_random_terror_decisions.txt` | `EC998C5B3355AAA8546EC73F0174F90F65A4665372C415DD2101315B2265F215` | `810E8EEC735E2AEDB35571609E1EA070443129C18E3B34ABC1F1F4A13C379236` |
| `common\scripted_effects\031_random_terror_effects.txt` | `0F673544C04424C84EF7DAFADAE1A01F01B075904A5B8C7F4AE52177704972A2` | `7BCE6DFA2B13CB3707D88B868F8393B73892CB914952C608565F0D499318F460` |
| `common\scripted_triggers\031_random_terror_triggers.txt` | `AEB0C8376214F1BF7BD498F8C266E9669284BC831984C21000287DCD2FAB0060` | `AEB0C8376214F1BF7BD498F8C266E9669284BC831984C21000287DCD2FAB0060` |
| `common\script_constants\031_random_terror_constants.txt` | `84AECCA5BE338433A9A9BF2BFBA5682BE8256D790A6940E1C5561D7705EA09B8` | `84AECCA5BE338433A9A9BF2BFBA5682BE8256D790A6940E1C5561D7705EA09B8` |

The English file SHA-256 is `94203E52F8701E92114EDEE5CD641E2C6D0EFFBAD664F340495FFBF1F20394F1`.

The MCP analyzer’s canonical `sourceHash` is distinct from the physical file SHA-256 and is recorded separately below.

## Probability MCP evidence

The connected workspace is `mod_chaos_redux_ea3b2d67c2c0`.

After the parent freeze, `hoi4.probability_inspect` used adapter `mission_ai_will_do`, the final mod-relative mission path, and the complete eight-ID candidate pool.

It returned `PROBABILITY_SOURCE_INSPECTED`, `poolComplete=true`, `candidates=8`, `availableCandidates=0`, `requiredInputs=0`, `requiredInputPaths=[]`, `sourceRevision=40288802c3c09c786854d4cfec600385c7f8b975b95596a63422e878a4656790`, and analyzer `sourceHash=e9f2adfc40a28293f7c0990e611eb114b080660d4ff8d1ee8c97e0d7062dfd22`.

The final inspect artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/dc2fb5d0e34e88f15729388c841db84f0da9e135e99926bd241394759799f19e/e9e68aceaf4a5e411913e05d381f6703995b51719ac27e9f12ad5e73712041c1/probability-inspect-e9f2adfc40a2.json`.

The baseline inspect had reported `scope.any_state` as a required input, while the final inspect returned no required input paths and the final evaluate still reported 18 unresolved scenario items; this adapter reporting difference does not prove that typed scope coverage was resolved.

`hoi4.probability_evaluate` received the exact parsed 26-scenario fixture object and all eight candidates with `metrics=["raw_value"]`.

It returned `PROBABILITY_ANALYZED_PARTIAL`, `analysisId=probability-e470e3943e9c2ca2d8d479f2`, `scenarioHash=11d242f0ff0b036d60c9f59bc21320c8d69fd43cf0728ee266f741f9a5d69edc`, 26 scenarios, 208 scenario-candidate rows, zero eligible candidates, 208 excluded candidates, 18 unresolved scenario items, and zero `unresolvedCandidates`.

Its analyzer `sourceRevision` is `40288802c3c09c786854d4cfec600385c7f8b975b95596a63422e878a4656790` and its `sourceHash` is `e9f2adfc40a28293f7c0990e611eb114b080660d4ff8d1ee8c97e0d7062dfd22`.

The analyzer emitted `PROBABILITY_OUTCOME_NEVER_ELIGIBLE` for each of the eight candidates across these supplied scenarios.

It also emitted `PROBABILITY_MODIFIER_UNSATISFIED_IN_SCENARIOS` for the corridor mission’s urgent factor and the hostage mission’s urgent factor in all 26 scenarios.

Those diagnostics describe this incomplete fixture evaluation and do not prove that the missions or those factors are impossible in a campaign.

`hoi4.probability_sweep` used the same exact parsed fixture and candidate pool, with five steps over `random_terror_pressure`, `random_terror_response_legitimacy`, and `global.random_terror_international_unity`, `findRankReversals=true`, and `pairwise=true`.

It returned `analysisId=probability-3ba8ab5ca2a2048f9849e1d9`, `scenarioHash=11d242f0ff0b036d60c9f59bc21320c8d69fd43cf0728ee266f741f9a5d69edc`, `sweepPoints=78`, zero eligible candidates, 208 excluded candidates, and 18 unresolved items.

Its analyzer `sourceRevision` is `bb8c4988cf38adc5aae825aff8f060a47f5f9c28ab89eb9655b7d4fe9f575863` and its `sourceHash` is `e9f2adfc40a28293f7c0990e611eb114b080660d4ff8d1ee8c97e0d7062dfd22`.

No valid rank reversal or sensitivity conclusion is available because the same effective candidates remained excluded from the adapter’s scenario model.

The evaluator’s matrix and unresolved SVGs are `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4e6bc12164df811098bd6c384fb316fb5002743176d0d34402b910ce3fa21263/7844732d4cf575ec7a422e24ab5f9239d5d74406d8ed50c4a3db15c6b82fdc28/probability-probability-e470e3943e9c2ca2d8d479f2-matrix.svg` and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2ce2cff38b3ad0a98f6329439d92c4bc25094817d2a2ee88987bfc28ca21802f/a632aeaa9b24d582ab0eabaeee3331d579368d15e96dad83247f475c64ae5a00/probability-probability-e470e3943e9c2ca2d8d479f2-unresolved.svg`.

The sweep’s sensitivity, threshold, and unresolved SVGs are `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cfd8afaba6bd3c71feec9a7d55974c13431dee17cbe827a4925d3990dda64268/970f3e1b1d68d2a455a32c9ef6506c784d7af5135b6bf83c0ad6f109399b4567/probability-probability-3ba8ab5ca2a2048f9849e1d9-sensitivity.svg`, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a6d32ffc270e06218fbe6e53b5f3d111d3f383d152a2e17fa057722f7cf35cc8/dc4600dbb9fe6b3a1657f018e166c8ba67b7363c16fac032160020f7a4d05ceb/probability-probability-3ba8ab5ca2a2048f9849e1d9-threshold.svg`, and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2ce2cff38b3ad0a98f6329439d92c4bc25094817d2a2ee88987bfc28ca21802f/b6d2ff94eec2262cdb872723b4658893f82e661840ec8d17c5e1eaa0101a6248/probability-probability-3ba8ab5ca2a2048f9849e1d9-unresolved.svg`.

The complete JSON, raster, SVG, SHA-256, and resource URI inventory is preserved in `docs\plans\031_random_terror_plans\evidence\mission_owner_comparison_20261004\mcp_evidence.json`.

## Before/after compare blocker

`hoi4.probability_compare` was called with adapter `mission_ai_will_do`, the full eight-candidate pool, the same parsed fixture object, before path `docs/plans/031_random_terror_plans/evidence/mission_owner_before_20261003/common/decisions/031_random_terror_missions.txt`, and after path `common/decisions/031_random_terror_missions.txt`.

The route returned `PROBABILITY_SURFACE_EMPTY` with `No weighted blocks matched this request` for the workspace-relative immutable snapshot path.

A separate `hoi4.probability_inspect` of that exact snapshot path returned `PROBABILITY_SOURCE_DISCOVERED`, `discoveryReason=no_weighted_surfaces`, `candidates=0`, and `availableCandidates=0`; it scanned the file as `mod:docs/plans/...` rather than as an active `common/decisions` weighted surface.

That snapshot probe reported `sourceRevision=77a94d3bad4b0e0a9e65220bcb3050311b6bc6fdd1bb5a3b6278171ed31ed44f` and analyzer `sourceHash=4a055ccf864c9893347a719c13c68625cd97cba08acd8cae8b3cae0c87ae6105`.

A retry using the absolute Windows path was rejected before analysis with `-32602`: `Path must be workspace-relative at before.path` and `Source path must be an exact workspace-relative file path at before.path`.

The first comparison did not time out, so the specified narrow transport/retake retry condition did not occur; a narrower pool would not correct the missing before-surface recognition.

No comparison ID, comparison artifact, or comparison scenario hash was returned.

The immutable snapshot bytes themselves are present and their SHA-256 matches the baseline handoff.

The allowed write scope does not include a temporary copy under runtime `common\decisions`, so this audit cannot remap the snapshot into the active source tree.

`hoi4.probability_render` was called for the evaluation and sweep IDs but returned `PROBABILITY_ANALYSIS_NOT_CACHED` for each.

The evaluate and sweep calls did return the linked visual resources listed above, but the explicit render route did not return additional artifacts.

A bounded 2,048-byte read of the final evaluation artifact returned `-32603: Artifact provenance manifest is unavailable`; the baseline handoff records the same error for its full and 6,000-byte artifact reads.

## Scenario and external-factor completeness

The unchanged fixture is `event31_mission_owner_baseline_20261003`, SHA-256 `CFD5FF35E35DE0553DE8CC0F07C282FFD4A4CBA6FF97D4675D0BAA02475FDD94`, with 26 scenarios.

The source definition pool is complete at 8/8 for every scenario listed below.

For every scenario, effective eligibility and external-factor completeness are unresolved because the fixture contains primitive state values and descriptive labels, not accepted typed bindings for receiver ROOT, target state, actor, owner, controller, nested CONTROLLER, mission slot, receiver-keyed receipt, or changing control.

The labels identify intended tests but do not bind those objects into the adapter.

The six score-context scenarios are `mission_ai_neutral_baseline`, `mission_ai_high_pressure_context`, `mission_ai_low_legitimacy_context`, `mission_ai_final_unity_context`, `mission_ai_capital_transport_target_priority`, and `mission_ai_retake_armed_state_priority`.

The cross-receiver and slot scenarios are `mission_a_b_same_mission_separate_states`, `mission_slot1_cross_family_conflict`, `mission_slot2_cross_family_conflict`, `mission_slot3_cross_family_conflict`, and `mission_same_state_distinct_receivers`.

The foreign or external target scenarios are `mission_transport_foreign_owned_root_controlled`, `mission_capital_foreign_owned_root_controlled`, `mission_restore_foreign_owned_root_controlled`, and `mission_retake_external_claimed_enemy_controlled`.

The nested receiver scenarios are `mission_hostage_state_owner_controller_distinct` and `mission_uprising_actor_owner_controller_distinct`.

The lifecycle scenarios are `mission_completion_owner_local_only`, `mission_cancellation_owner_local_only`, `mission_timeout_owner_local_only`, `mission_recovery_close_owner_local`, `mission_global_defeat_cleanup`, and `mission_capture_transfer_invalidation`.

The outcome criteria scenarios are `mission_all_eight_success_outcome_criteria`, `mission_all_eight_partial_outcome_criteria`, and `mission_all_eight_failure_outcome_criteria`.

Unavailable external inputs include the country’s actual war and major status, state owner/controller and capital status, family-specific active locks, route/evolution state, progress receipts, transfer timing, callback receiver identity, and event/action result state.

The after-inspect reported no required input paths, while its evaluate still reported 18 unresolved scenario items; this is an adapter reporting gap and is retained as unresolved rather than filled from fixture labels.

## Source weight inventory

The aliases in the final mission file are `@rt_mission_ai_low=1`, `@rt_mission_ai_medium=3`, `@rt_mission_ai_high=7`, `@rt_mission_ai_urgent=12`, `@rt_mission_ai_high_factor=2`, and `@rt_mission_ai_urgent_factor=4`.

`random_terror_value.low=25` and `random_terror_value.high=70` in `common\script_constants\031_random_terror_constants.txt` are unchanged.

| Mission | Base | Conditional modifiers in final source |
| --- | --- | --- |
| `random_terror_contain_attack_wave` | high `7` | urgent `×4` when Terror Pressure `>70`; high `×2` for `random_terror_failed_raid_recorded`; high `×2` at war |
| `random_terror_protect_transport_network` | high `7` | urgent `×4` when the receiver’s capital has its `random_terror_transport_mission_subject_@ROOT` receipt; high `×2` at war |
| `random_terror_break_cross_border_corridor` | high `7` | urgent `×4` when `random_terror_support_disrupted` is set; high `×2` at war |
| `random_terror_prevent_capital_seizure` | urgent `12` | urgent `×4` at war; high `×2` for a major country |
| `random_terror_retake_lost_state` | high `7` | urgent `×4` when an any-state target carries this receiver’s `random_terror_retake_mission_subject_@ROOT` receipt and armed-insurgency state; high `×2` at war |
| `random_terror_restore_civil_authority` | high `7` | urgent `×4` when Response Legitimacy `<25`; high `×2` at war |
| `random_terror_hostage_deadline` | urgent `12` | urgent `×4` when the receiving country has `random_terror_hostage_crisis_active`; high `×2` at war |
| `random_terror_stop_coordinated_uprising` | urgent `12` | urgent `×4` at war; high `×2` when global International Unity `>70` |

A balanced-brace source comparison of all eight before and final `ai_will_do` blocks found them equal after whitespace normalization and exactly two expected receipt-key changes: transport now checks `random_terror_transport_mission_subject_@ROOT`, and retake now checks `random_terror_retake_mission_subject_@ROOT`.

No base value, numeric factor, threshold, or other `ai_will_do` condition changed in those eight blocks.

The eight `days_mission_timeout` references are text-identical to the frozen before source; they remain native mission deadlines, and no separate event-MTTH timing distribution is claimed.

The mission file contains no `mtth:` entry reference for these missions; their `days_mission_timeout` values are separate objective deadlines, not event timing distributions.

The source weight inventory is classified `score-only`; the MCP evaluate and sweep are `unresolved`, with no valid raw score trace, ranking, selection probability, or timing result returned.

No bounded or sampled result was produced.

## Documentation and vanilla evidence

The offline `paradox_wiki\AI modding - Hearts of Iron 4 Wiki.md` `MTTH blocks` section, lines 26-37, revision `917cd261f7da51fe4d8687c5d7663e768a09c5c101ac130ce646bc64637aa818`, describes the `ai_will_do` score race and distinguishes event-option `ai_chance` sampling.

The offline `paradox_wiki\Decision modding - Hearts of Iron 4 Wiki.md` `AI` section, lines 357-374, and `Missions` section, lines 465-479, revision `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162`, cover decision willingness weights and mission activation/completion behavior.

The offline `paradox_wiki\Scopes - Hearts of Iron 4 Wiki.md` `Trigger scopes` lines 382-395 and `Effect scopes` lines 522-535, revision `18ef5249e4991f5427eca9ec4a2f66dd47f51e26a491c730adc622f1f5db1b49`, document global `any_state` and `every_state` versus country-limited alternatives.

The offline `paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md` `Flags` section, lines 102-126, revision `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`, documents country/state flag scopes and `@ROOT`-targeted country flags.

The offline `paradox_wiki\Effects - Hearts of Iron 4 Wiki.md` `Missions` section, lines 1908-1927, revision `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c`, documents `activate_mission` and related mission effects.

Installed `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\decisions\_documentation.md` lines 1-46, revision `5e7e686b5582f32c38d898d805e17171e88f3bfeee4a030deb1884f9726de019`, describes targeted decision scopes and their evaluation frequency.

Installed `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\effects_documentation.md` `activate_mission` lines 661-670, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`, confirms country scope and that activation ignores normal mission triggers.

The vanilla precedent is `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\decisions\PRC.txt`, `PRC_assaulting_guyuan` beginning at line 6592, SHA-256 `19B5776BF0E91A419946BEDAF3AA5E052EC09165AE8BDBCB0F1800CD081A01DF`; its exact-state mission target is structural precedent only.

## AI validity and risk findings

The two receiver-key changes bind the transport-capital and retake-armed-state AI modifiers to the mission receiver’s receipt.

The hostage mission’s corrected cancel guard is country-scoped, and its state flag tests remain inside state scopes; the current source no longer has the state-scope `has_country_flag` placement described in the parent correction.

`random_terror_failed_raid_recorded` remains a concrete source-level scope mismatch: mission AI at `common\decisions\031_random_terror_missions.txt:115` tests a country flag, while the only repository `common\*.txt` writers found at `common\scripted_effects\031_random_terror_effects.txt:562` and `:2914` use `set_state_flag`.

No matching country-flag writer was found in the repository-wide `common\*.txt` search, so the containment high-factor appears unable to activate through the current Event 31 writers.

The same identifier also has country-scope consumers in `common\decisions\031_random_terror_decisions.txt:98`, `:1734`, `:1746`, and `:1766`, alongside a state-scope consumer at `:562`; reconcile the intended receiver/state receipt contract across those consumers and both state writers.

`random_terror_support_disrupted` is written as a country flag by `random_terror_decision_disrupt_support` in `common\scripted_effects\031_random_terror_effects.txt:2151`, matching the corridor AI predicate’s scope form.

`random_terror_hostage_crisis_active` is set under the target state’s `CONTROLLER` at `common\scripted_effects\031_random_terror_effects.txt:601`, matching the nested controller as the accepted hostage mission receiver.

All eight source blocks have a positive base, but positive bases do not prove mission activation, scenario validity, or a selection share.

The MCP’s `PROBABILITY_OUTCOME_NEVER_ELIGIBLE` warnings cannot establish that any definition is dead or impossible because all eight rows were evaluated without typed target and receiver bindings.

Dominance and starvation remain unresolved because no valid candidate ranking was returned.

The requested sweep produced 78 points but no valid rank-reversal result because all 208 rows were excluded and 18 scenario items remained unresolved.

Repetition and exploit risk are not quantified by this native mission-weight audit; the parent-reported family locks and callback closures are not a declared custom pool with a cadence/transition manifest, and no runtime observations were authorized.

## Weight semantics

The offline AI Modding reference describes `ai_will_do` as an AI score race: in most cases the game draws a value between zero and each entry’s score and selects the entry with the highest draw.

That is not probability-proportional-to-size sampling and does not make an `ai_will_do` score a normalized click probability.

The same offline reference distinguishes event-option `ai_chance`, which uses probability-proportional sampling; no Event 31 mission `ai_chance` surface is in this audit.

No `mtth:` entry is used by these eight mission definitions, so no event MTTH timing distribution or cumulative timing claim is made.

## Recommended follow-up

1. Reconcile `random_terror_failed_raid_recorded` at the cited decision, mission, and effect paths so the country AI modifier and its writer share an explicit receiver-aware scope contract.

2. Restore MCP comparison coverage for immutable evidence snapshots, or provide a separately indexed read-only before workspace, then rerun the full eight-candidate comparison using the same parsed fixture object.

3. Once the connected schema supports typed scope bindings, rerun the same 26 scenarios with explicit receiver, state, owner, controller, active-slot, and receipt inputs; keep the fixture labels descriptive until such bindings are returned.

4. Keep the numeric weights unchanged until the MCP returns comparable eligible candidates and score traces; this audit selects no balance target.

## Skipped analyses and remaining uncertainty

`hoi4.probability_simulate` was not used because no uncertain-input distribution or seed contract was declared.

`hoi4.probability_sequence` was not used because these are native mission definitions rather than a complete declared custom weighted pool with cadence and state transitions.

No narrower comparison retry was run because the full-pool request failed with `PROBABILITY_SURFACE_EMPTY`, not a load timeout.

The explicit `hoi4.probability_render` calls failed with `PROBABILITY_ANALYSIS_NOT_CACHED`; visual artifacts returned by evaluate and sweep remain linked in the evidence bundle.

Artifact range reads failed with `-32603: Artifact provenance manifest is unavailable`, so the linked JSON content could not be independently expanded.

`hoi4.source_lookup` returned zero definitions and references for the three queried flag/receipt symbols, `referencesComplete=false`, and `unresolvedReferenceCount=18450`; the underlying source was therefore reviewed directly, but the index did not improve indexed coverage.

Event-chain, focus, technology, doctrine, GUI, and map structural routes were not applicable to this bounded mission `ai_will_do` surface.

The concrete design/accounting limits, tool outputs, artifact hashes and URIs, fixture object, and per-call inputs are preserved in `docs\plans\031_random_terror_plans\evidence\mission_owner_comparison_20261004\mcp_evidence.json`.

Skills used: `chaos-redux-subagents`, `chaos-redux-decisions-missions`, and `chaos-redux-mtth`.

No skills were created or updated.

## After-audit unweighted effect correction (2026-10-04)

The current SHA-256 of `common\scripted_effects\031_random_terror_effects.txt` is `41DF95B5C1F72D5F464E2A650921B32C3787EA1F250FAFAE56D00877D498CB35`; the effects hash in the preceding MCP source table, `7BCE6DFA2B13CB3707D88B868F8393B73892CB914952C608565F0D499318F460`, identifies the source used during the earlier inspect/evaluate/sweep calls.

The parent reports that the only effect-file change since that source set is removal of the generic `random_terror_civil_authority_restored` state-flag write from `random_terror_decision_restore_services`; this is an unweighted post-review correction and no probability tool was rerun for it.

The correction follows `docs\specs\031_random_terror_specs\031_random_terror_achievement_prompt.md`, lines 187-194, SHA-256 `D39ED37C0B9BEA17357382B796E17F0C1A04A16631BEF3B95FF9CF6B353E4540`, whose achievement condition requires every recaptured state to complete Restore Civil Authority.

The corresponding accepted section in `docs\specs\031_random_terror_specs\031_random_terror_spec_part_12_achievements.md`, lines 194-201, has SHA-256 `2D0F9407D805AF5BD875F66748F490058CD81002DCEEAECC0EA21DC5853716F3`.

Current source shows the starter retains only `random_terror_civil_authority_restored_@ROOT` at `common\scripted_effects\031_random_terror_effects.txt:2279`; its caller clears that keyed transient flag at `common\decisions\031_random_terror_decisions.txt:1714` before `activate_mission`.

The timed mission's successful resolver is the sole current writer of generic `random_terror_civil_authority_restored`, at `common\scripted_effects\031_random_terror_effects.txt:3870`.

The achievement consumer reads that generic fact at `common\scripted_effects\031_random_terror_achievement_effects.txt:653`; a repository-wide `common` search found no AI consumer of the generic flag.

This removes the starter-time achievement credit while preserving the keyed transient progress contract that the mission clears before activation.

The other current hashes remain `common\decisions\031_random_terror_missions.txt` `C775B7556270CFFAE07B33C1B8435D50B5990B1C8EA1383654E70C8458A71BD2`, `common\decisions\031_random_terror_decisions.txt` `810E8EEC735E2AEDB35571609E1EA070443129C18E3B34ABC1F1F4A13C379236`, `common\scripted_triggers\031_random_terror_triggers.txt` `AEB0C8376214F1BF7BD498F8C266E9669284BC831984C21000287DCD2FAB0060`, `common\script_constants\031_random_terror_constants.txt` `84AECCA5BE338433A9A9BF2BFBA5682BE8256D790A6940E1C5561D7705EA09B8`, and English localisation `94203E52F8701E92114EDEE5CD641E2C6D0EFFBAD664F340495FFBF1F20394F1`.

The original fixture remains SHA-256 `CFD5FF35E35DE0553DE8CC0F07C282FFD4A4CBA6FF97D4675D0BAA02475FDD94`.

The earlier MCP source revision, scenario hash, render artifacts, and `PROBABILITY_SURFACE_EMPTY` compare blocker remain exactly as recorded above; this addendum creates no new MCP analysis or comparison result.

The auditor made no gameplay patch for this correction.
