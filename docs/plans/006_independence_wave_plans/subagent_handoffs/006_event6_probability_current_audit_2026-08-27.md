# Event 006 current probability audit

Status: bounded, read-only audit on 2026-08-27. No gameplay, AI, event, focus, decision, mission, strategy, source-map, spec, workbook, or export files were edited.

## Scope and references

Audited current Event 006 weighted surfaces against `006_source_of_truth_map.md`, `006_independence_wave_resume_packet.md`, `006_event6_probability_audit_round_2026_08_24.md`, and `006_event6_first_footprint_admission_improvement_addendum_2026_08_26.md`.

Read `AGENTS.md`, `chaos-redux-events`, `chaos-redux-subagents`, and `chaos-redux-mtth`, the required offline Paradox wiki pages, and the relevant vanilla documentation under `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation`.

HOI4 MCP workspace: `mod_chaos_redux_ea3b2d67c2c0`. Adapter game target: Operation Postern 1.19.2.0 (d245).

## Successful current MCP evidence

### Root event option `ai_chance`

Source: `events/006_independence_wave.txt`.

`hoi4.probability_inspect`, adapter `event_option_ai_chance`, returned `PROBABILITY_SOURCE_INSPECTED`, source revision `69c8a8272a3833a9d2572014de194a973be3ebf64ec9bfeb989faed10f025df6`, source hash `a08206c27f0e0da5cfd56e3e6e985b067d7b528ba1f6e4b3898369346b238cd2`, 22 discovered candidates, 13 required inputs, and `poolComplete=false`.

Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f7fe874b36f58c12c4800313e9205f0f3729069edc140ee5fdd1823264db7eaf/6665d56de258cb0f6e0dce33d3d186440150dad083c398cb815ecbb4e304ec74/probability-inspect-a08206c27f0e0.json`.

The 22 candidates are the 20 root IDs `chaosx.nr6.2.a`, `chaosx.nr6.300.a`, `chaosx.nr6.301.a`, `chaosx.nr6.301.b`, `chaosx.nr6.301.c`, `chaosx.nr6.302.a`, `chaosx.nr6.302.b`, `chaosx.nr6.302.c`, `chaosx.nr6.303.a`, `chaosx.nr6.303.b`, `chaosx.nr6.304.a`, `chaosx.nr6.304.b`, `chaosx.nr6.304.c`, `chaosx.nr6.305.a`, `chaosx.nr6.306.a`, `chaosx.nr6.307.a`, `chaosx.nr6.308.a`, `chaosx.nr6.311.a`, `chaosx.nr6.311.b`, `chaosx.nr6.35.a`, plus `chaosx.triggerable_scenarios.80.a` and `chaosx.triggerable_scenarios.80.b`.

`hoi4.probability_evaluate`, scenario set `E6_ROOT_OPTION_MATRIX_2026_08_24`, scenarios `E6_CORE_EMPTY_CURRENT_2026_08_24`, `E6_SHARED_DECISION_EMERGENCY_2026_08_24`, and `E6_SHARED_DECISION_PROVISIONAL_2026_08_24`, returned `PROBABILITY_ANALYZED_PARTIAL`, analysis `probability-21ecef2ef00a9848c2101687`, scenario hash `509f3bf047bf951e9ca0c5d5cad28068e9f8be60440685cc2df06baacb70fa30`, 60 scenario-candidates, and 19 unresolved items.

Artifacts: JSON `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/41672d50cc42614955ad64eb5ed280867f51e7d65da58dff9f6762e7cbb6d13b/c3db11608f627df722ff00347396812d7829f2ca074f227e0282602c0a9f3d16/probability-21ecef2ef00a9848c2101687.json`; ranking SVG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4a9bd51a40fff8263f9188ebc4ba1dd50359064d7a6c07d866905cddfa7a80ce/920444f64f80360abdca21b596dd0c335498d2af727d919dfa282cf844f64bb2/probability-probability-21ecef2ef00a9848c2101687-ranking.svg`; unresolved SVG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/38838b1831e77eb6343d8d1a2b7fa7eb9fbff4fbab74749fe362f780278f481a/d5def5068eaaabccb219b9d18ebc7790c4be54789371456ef23cb8e4de1ccdc5/probability-probability-21ecef2ef00a9848c2101687-unresolved.svg`.

Result classification: bounded score-only, not a click probability. MCP explicitly withheld normalization because the candidate pool is incomplete and reported `.301.a`'s `independence_wave_decision_ai.modifier_major` inactive in all three fixtures.

### Merged support-event `ai_chance`

Source: `events/006_independence_wave_support_events.txt`.

`hoi4.probability_inspect`, adapter `event_option_ai_chance`, returned `PROBABILITY_SOURCE_INSPECTED`, source revision `69c8a8272a3833a9d2572014de194a973be3ebf64ec9bfeb989faed10f025df6`, source hash `4d7ed5adb1d7c26803d1771ba98d4a3c9149fb2e2661d3ff0e770edbcf613437`, 154 candidates, 44 required inputs, and `poolComplete=false`.

Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/aba0028d7282146d4040f42955447ffdb36f3df3243379106cc65342b96fc314/4b85b0b25461498a050b0131609916d0736943ec339cd4c26e874ca99ac3bc1a/probability-inspect-4d7ed5adb1d7.json`.

Evaluation was attempted with `E6_SCENARIO_MODE_2026_08_24` and `E6_JOIN_RETRY_2026_08_24`, but failed with `ARTIFACT_MANIFEST_INTEGRITY_FAILED`.

### Automatic allocator outer region pool

Source: `common/scripted_effects/006_independence_wave_effects.txt`, `independence_wave_select_one_automatic_package`, random list at line 3297.

`hoi4.probability_inspect`, adapter `random_list`, returned `PROBABILITY_SOURCE_INSPECTED`, source revision `2375381d0e0468efccef10c185078eeba27ce904e1052220b39cef5d8758f447`, source hash `5b551b7eed1e6c673d519870075f8cb057e0c521e5bb3b28585df8506f71c29a`, 14 candidates, `poolComplete=true`, and 14 required inputs `independence_wave_region_01_total_weight` through `_14_total_weight`.

Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/daee059af43c24af47f40bf108fcdd1c32d3d799ad8d36c5e633a4633ad18679/654f3990ddc34c4a8c72313a6a16dc6929151a867992c70589da2a34763fc48b/probability-inspect-5b551b7eed1e.json`.

`hoi4.probability_evaluate` was attempted under the required `E6_ALLOCATOR_LADDER_2026_08_24` scenarios `ALLOC_UNIFORM_COMPLETE`, `ALLOC_CALM_3`, and `ALLOC_RISING_5` with complete 14-entry fixtures, first using entry names and then source entry IDs. The route returned `PROBABILITY_SURFACE_EMPTY` for the first form and `ARTIFACT_MANIFEST_INTEGRITY_FAILED` for the latter and for the no-pool retry. `hoi4.probability_sweep` on the same named ladder and three paths (`_01`, `_02`, `_14`) also returned `ARTIFACT_MANIFEST_INTEGRITY_FAILED`.

Therefore the old 2026-08-24 ladder percentages are not re-certified as current. No current rank-reversal, dominance, starvation, or timing claim is made from the failed route.

### Formable congress success/failure random list

Source: `common/scripted_effects/006_independence_wave_formable_registry_effects.txt`, `independence_wave_formable_resolve_congress`, random list at line 2485.

`hoi4.probability_inspect`, adapter `random_list`, returned `PROBABILITY_SOURCE_INSPECTED`, source revision `2375381d0e0468efccef10c185078eeba27ce904e1052220b39cef5d8758f447`, source hash `355bf8134c4151ef3265293666e291f16461997ad73bebb53053dbaab01ac05d`, two candidates, `poolComplete=true`, and two required inputs.

Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a50d304bd304a621e064e7a785dd7372ec427113d1afd4adbf1462314e73aa80/c50a5735e1d07b32de3f027023d08eddad4bf51ca6ebb1f5da104c93cce8ebd1/probability-inspect-355bf8134c41.json`.

Evaluation under named scenario `E6_SCENARIO_MODE_2026_08_24`, with explicit declared fixture values of 1 for both `independence_wave_formable_success_weight` and `independence_wave_formable_failure_weight`, returned complete exact analysis `probability-96ce0b313e1c5d9bec8312c7`, scenario hash `93d7db3a8e9c997b1911313f31f58e42db3107b885dfedfd00d1bd62ab3ebaa3`, and exact 1/2 versus 1/2 conditional probabilities.

JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e008c643c96364e99cff12f03ed2c13e655a64aae2572f3d0409004c4cda423b/5fb39ba0f9609847d65ba88c9003fd077b8f4ae147d98fdf60a574cad5b560cc/probability-96ce0b313e1c5d9bec8312c7.json`.

The exact result is only for the declared two-entry synthetic fixture and does not establish campaign congress odds.

### AI strategy factor source

Source: `common/ai_strategy/006_independence_wave_ai_strategy_registry.txt`.

`hoi4.probability_inspect`, adapter `ai_strategy_factor`, returned `PROBABILITY_SOURCE_DISCOVERED`, source revision `2375381d0e0468efccef10c185078eeba27ce904e1052220b39cef5d8758f447`, source hash `a35190937fed7a0e7a3e156244ad0dbac468bdc2c0c05366da6cce0d3d482396`, and `discoveryReason=no_weighted_surfaces`, with zero candidates and zero required inputs.

Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/43aca06d5c3833b9f939906398346c2a889590e3dc29e17960490801716e3551/291a9b75f2871d660f965be5d2ef5c375ffc8163306f21ce0171a43ada1de3c1/probability-inspect-a35190937fed.json`.

The source visibly contains ordinary `ai_strategy` factors and host/patron/league gates, but this adapter did not expose them as a normalized selection pool. Their influence remains score-only or unresolved for this audit.

### Evolution MTTH

Source: `common/mtth/006_independence_wave_evolution_mtth.txt`.

`hoi4.probability_inspect`, adapter `event_mean_time_to_happen`, returned `PROBABILITY_SOURCE_DISCOVERED`, source revision `69c8a8272a3833a9d2572014de194a973be3ebf64ec9bfeb989faed10f025df6`, source hash `8632297cf059164892a537ff3a987cddd0406c020e98234331014d42b4b8f8a2`, zero weighted surfaces, and zero candidates.

Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/071073d01b60814f26e86ca47ef4bd080930003201a2f651549dd23a59f7ca0b/5ee9b942aef03481620662115738fb396355122bd4dbe37a9d3501a003f40c30/probability-inspect-8632297cf059.json`.

Evaluation under `E6_EVOLUTION_MTTH_MATRIX_2026_08_24` with `E6_EVOLUTION_MTTH_EMPTY_CURRENT_2026_08_24` and `E6_EVOLUTION_MTTH_DENSE_NETWORK_2026_08_24` failed `PROBABILITY_SURFACE_EMPTY` with `No weighted blocks matched this request`; no timing distribution is proven.

## Current routes blocked

The following mandatory inspect/evaluate routes were attempted against current sources and returned `ARTIFACT_MANIFEST_INTEGRITY_FAILED` with the exact message `Artifact provenance manifest does not match its immutable address`: inner allocator `common/scripted_effects/006_independence_wave_package_region_effects_registry.txt` (`random_list`), shared decisions `common/decisions/006_independence_wave_decisions.txt` (`decision_ai_will_do`), Form 03 decisions `common/decisions/006_independence_wave_form03_decisions.txt` (`mission_ai_will_do`), shared focus `common/national_focus/006_independence_wave_focus.txt` (`national_focus_ai_will_do`), SCN-008 `common/scripted_effects/006_independence_wave_scenario_effects.txt` (`custom_weighted_pool`), merged root/support event structural inspect, allocator sweep, and probability render retry.

The same error blocked the final merged support-event evaluation under `E6_SCENARIO_MODE_2026_08_24` and `E6_JOIN_RETRY_2026_08_24`.

Earlier dated handoffs retain structural focus evidence at revision `56ae382...` and older decision/mission partial discovery, but those artifacts are not treated as current probability evidence after the current merged-worktree revision drift.

No `probability_compare` was run because no valid current before/after owner patch exists; comparing the same current source would not establish a change result.

## IW-095 first-footprint admission

The queued IW-095/Dahomey package remains plan-only and adds no executable package-owned weighted surface in the current worktree.

Current source has generic planner bindings `independence_wave_prepare_weight_iw_095`, `independence_wave_load_package_iw_095`, and `independence_wave_reserve_package_iw_095` in `common/scripted_effects/006_independence_wave_package_region_effects_registry.txt`, plus `can_plan_independence_wave_package_iw_095` in `common/scripted_triggers/006_independence_wave_package_region_triggers_registry.txt`, but the readiness chain still requires `is_independence_wave_candidate_tag_available`, including `independence_wave_package_content_ready`; no IW-095 package source sets that readiness flag.

The current outer allocator is a complete 14-region pool, but the inner package pool, candidate eligibility, host/league/patron state, decision/mission scores, focus callback ordering, anti-repeat behavior, and custom SCN-008 pool are not currently MCP-proven because of the route failures above.

Central admission therefore cannot be supported by current evidence. The strongest current conclusion is fail-closed: keep IW-095 out of executable admission until its package identity, runtime 776 binding, content readiness, AI strategy, complete candidate-pool evidence, and same-scenario `probability_compare` are available.

## Findings and recommended follow-up

No positive-weight impossible-choice, dominance, starvation, rank-reversal, repetition, or snowball conclusion is asserted for current Event 006 because the required complete-pool scenario traces are unavailable.

Recommended owner follow-up is to repair MCP artifact provenance for the current merged files, then re-run the named root, support, allocator ladder, first-footprint, decision/mission, focus, host/league/patron, and SCN-008 scenarios with complete pools and preserve `probability_compare` evidence before any admission or tuning decision.

Completion status: audit evidence is delivered, but the Event 006 probability audit is unresolved for all affected large merged surfaces because of the exact MCP artifact-integrity blocker above.
