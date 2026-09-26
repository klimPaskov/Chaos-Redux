# Event 006 IW-039/DON AI Probability Baseline - 2026-09-26

Disposition: Source and adapter baseline established. Quantitative selection conclusions remain unresolved. This is a read-only audit; no source, weight, spec, or matrix file was changed.

## Accepted scope and design context

The user-accepted policy is that state 245 (Millerovo) is IW-039/DON's unique Event 006 anchor and capital, state 238 (Volgodonsk) is an optional compact if available, and vanilla DON capital state 218 stays outside the Event 006 package.

Event 005 DHC and Event 006 IW-039 are mutually exclusive in both event orders, SOV state 219 is preserved, and reservation group RG-DON-KUBAN permits one package per wave.

The shared focus architecture remains root-level shared_focus. Imported-layout MCP proof remains blocked, with no direct-focus fallback.

IW-039 remains unadmitted. Its current package-specific runtime adapter, content attestation, setup, and cleanup are absent. The user authorized broad Event 006 work, but no DON AI weight or other weighted source was patched in this audit.

The accepted geography and event-order policy above is user-provided design context, not a campaign-state fixture or MCP probability evidence.

## Current source surfaces reviewed

- Region 04 allocator and package definitions: common/scripted_effects/006_independence_wave_package_region_effects_registry.txt.
- Shared package score function: common/scripted_effects/006_independence_wave_package_planner_effects.txt.
- Region 04 plan gates: common/scripted_triggers/006_independence_wave_package_region_triggers_registry.txt.
- Runtime adapter and content-attestation allowlists: common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt.
- Generic package readiness helpers: common/scripted_triggers/006_independence_wave_package_triggers.txt.
- Event 005/Event 006 DHC collision contract: common/scripted_triggers/005_006_liberations_collision_triggers.txt, with Event 005 calls in common/scripted_triggers/005_soviet_collapse_triggers.txt and common/scripted_effects/005_soviet_collapse_effects.txt.
- Shared allocation, AI willingness, and earliest-band values: common/script_constants/006_independence_wave_constants_registry.txt.
- Mounted force-profile predicate: common/scripted_triggers/006_independence_wave_triggers.txt.
- Event 006 shared tree: common/national_focus/006_independence_wave_focus.txt.
- Root-level shared-focus sources: common/national_focus/006_independence_wave_iw043_iw058_focus.txt and common/national_focus/006_independence_wave_iw093_iw098_focus.txt.
- Event 006 AI strategy registry: common/ai_strategy/006_independence_wave_ai_strategy_registry.txt.
- Generic and shared Event 006 decision/mission score sources: common/decisions/006_independence_wave_decisions.txt and common/decisions/006_independence_wave_shared_decisions.txt.
- Event option sources: events/006_independence_wave.txt and events/006_independence_wave_support_events.txt.
- Event 006 on-action registry checked for random-event scheduling: common/on_actions/006_independence_wave_on_actions_registry.txt.
- IW-039's static scenario-ranked package entry is common/scripted_effects/006_independence_wave_scenario_effects.txt:234. That array membership is a ranking input, not runtime admission or proof of a positive selectable weight.

The current consolidated Region 04 source is the registry path listed above. The older Region 04 path named in the 2026-08-10 preflight is not current.

## DHC/W039 exclusion update and baseline timing

The user reported during this audit that the accepted exclusion helper had been added to can_plan_independence_wave_package_iw_039, can_soviet_collapse_spawn_dhc, and the Event 005 force-all DHC branch. Current source review confirms is_don_dhc_cross_event_collision_clear at:

- common/scripted_triggers/006_independence_wave_package_region_triggers_registry.txt:350.
- common/scripted_triggers/005_soviet_collapse_triggers.txt:8196.
- common/scripted_effects/005_soviet_collapse_effects.txt:23514.

The first Region 04 probability inspection receipts were produced before the user's update and are retained as pre-gate receipts. The narrowed Region 04 receipt then had sourceRevision da8b9074ac9ef42bffa059864254abaa1f73188399293c4619f75491cc0270a and sourceHash 17e35c209602f859bd3e5b71bd6b394aa613d7d8686e0d07f1d8ee3b803585e6.

I reran probability_inspect with refresh=true after the update. The refreshed Region 04 result is classified current/post-gate: sourceRevision b3dcf501fa84ef47554bbbc5f3c767a744f1000bd28531ca6aba69edc44900ff, sourceHash 17e35c209602f859bd3e5b71bd6b394aa613d7d8686e0d07f1d8ee3b803585e6, poolComplete=true for the narrowed eight entries, availableCandidates=0, and requiredInputs=8. The refreshed planner inspect is also current/post-gate: sourceRevision 0c0dda49f7385df63c1f287c34a452cb684740bc036e2ead0ec82d260fd403bc and sourceHash 6aed5bf35bcea2f7a1571b149a0905ccd5466dba8cc4ac1a7f2648afd463ce95.

The random-list receipt's filesScanned contains only the Region 04 effects registry, and its sourceHash is the hash of that unchanged weighted source. It does not fingerprint the three separate gate call sites. The refreshed receipt is post-gate by run order and workspace sourceRevision; the helper call sites are independently verified by current source review and these current file hashes:

- common/scripted_triggers/006_independence_wave_package_region_triggers_registry.txt: SHA-256 4777C6EC621DB8D63BCE7307291577664A3D0CDDA74C0DA2374AFEA1B34D5E7A.
- common/scripted_triggers/005_soviet_collapse_triggers.txt: SHA-256 1255730AD012D1AA8A0364FEA6E2B22C2E4E72D749A2AE433753E0B427924B39.
- common/scripted_effects/005_soviet_collapse_effects.txt: SHA-256 2F813FD06F7F75EC54C7DABF81D512886B1C38D37718DA85C71BDA59B7E9C358.

The focus, shared-focus, decision, mission, event-option, MTTH, and strategy-factor inspection receipts below were captured before the user's gate update. Their listed source hashes identify those inspected weighted files; they are not used to certify the later gate call sites. The parent update changes eligibility, not the numeric weights in those surfaces.

The relevant refreshed probability artifacts are:

- Current/post-gate Region 04: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0653511b723e9f1251ea8a486a761efc08240418a073cad35dbeb910bbaf311e/ec63d4efbf28ef7b50b285fa3f92870626c21469c6803d13d69ef824c4f6abf5/probability-inspect-17e35c209602.json.
- Current/post-gate package planner: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b7789338e4bf28658c627fae37d4ca53c163c6a610b91f3b0beea05363d6bf3e/e1032163dcb808e739c39c116319a5e73dc4a5cb170db6ca791755c7b3ca9918/probability-inspect-6aed5bf35bce.json.

The guard changes affect eligibility and event-order exclusion. They do not modify numeric weights. No probability_compare was run, and no valid comparison claim is made without supported scenarios.

## MCP route, schema, and health record

Workspace: mod_chaos_redux_ea3b2d67c2c0. The connected probability artifact identifies tool version 3.0.7 and adapter version hoi4-1.19.2.v1. Game-version verification reads C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/launcher-settings.json and reports Operation Postern v1.19.2.0.a729 (d245), adapter target Operation Postern 1.19.2.0 (d245), status workspace_verified.

The exposed weighted routes are mcp__hoi4_agent_tools__hoi4_probability_inspect, probability_evaluate, probability_sweep, probability_simulate, probability_sequence, probability_compare, and probability_render. The matching structural routes used were hoi4.focus_inspect, hoi4.focus_render, hoi4.event_inspect, and hoi4.event_render.

With an adapter specified, probability_inspect requires a source object. The initial source-less call returned MCP error -32602: “An adapter requires a source; provide a source alone to discover compatible adapters.” Accepted calls used source = { path: "<mod-relative-path>" }. The evaluate route requires scenarioSet. The repository's connected-schema workflow confirms scenarios use actor, flat primitive state, flags, and scopes shaped as { id, state }; it does not accept typed scenario-variable declarations.

No helper_expansion, job, native task, or task-negotiation mode was used. No separate callable HOI4 health/version or client-task-negotiation endpoint was exposed; ordinary read-only inspect calls succeeded. A parallel batch briefly returned INTERNAL_ERROR for four inspectors; serial retries for those exact sources succeeded.

The adapter metadata cites docs/research/probability-adapter-evidence.md, but that path is absent in this checkout. The repository's 2026-09-20 Event 006 fixture-schema probe and live adapter artifacts were available.

## Probability inspection results

Every zero availableCandidates result below is an adapter/fixture-coverage observation only. It is not a real in-game probability or proof that every corresponding game choice is unavailable.

| Surface and source | Adapter result | Source revision and source hash | Artifact |
| --- | --- | --- | --- |
| Region 04 source-wide registry inventory, common/scripted_effects/006_independence_wave_package_region_effects_registry.txt | 126 entry candidates across distinct random-list pools; poolComplete=false; availableCandidates=0; requiredInputs=126; unresolved=1; unsupported MULTIPLE_CATEGORICAL_POOLS. The whole registry is not one distribution. | Pre-gate receipt: revision 5179cc549a8371bf7bcd4ffeedc3687faddcfa951df1138865ede4f04c4f2425; hash 17e35c209602f859bd3e5b71bd6b394aa613d7d8686e0d07f1d8ee3b803585e6. | hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5168314632ac5e9aa411f24cb467dc02b6bbf9c180d3e4fc4ca03db86a152732/7950dc528eb52512cb723f588419eeb2661ff96880043864956f06c659cf25ae/probability-inspect-17e35c209602.json |
| Region 04 allocator narrowed to its eight source IDs | poolComplete=true; candidates=8; availableCandidates=0; requiredInputs=8; unresolved=0. Exact for source pool shape only. | Pre-gate receipt: revision da8b9074ac9ef42bffa059864254abaa1f73188399293c4619f75491cc0270a7; hash 17e35c209602f859bd3e5b71bd6b394aa613d7d8686e0d07f1d8ee3b803585e6. Current/post-gate refresh: revision b3dcf501fa84ef47554bbbc5f3c767a744f1000bd28531ca6aba69edc44900ff; same weighted-file hash. | Current/post-gate artifact above. |
| Shared package planner, common/scripted_effects/006_independence_wave_package_planner_effects.txt | custom_weighted_pool; candidates=0; poolComplete=false; availableCandidates=0; requiredInputs=0. This scripted helper is not a declared custom-pool manifest; empty output is adapter coverage, not an empty in-game pool. | Pre-gate receipt: revision da8b9074ac9ef42bffa059864254abaa1f73188399293c4619f75491cc0270a7; hash 6aed5bf35bcea2f7a1571b149a0905ccd5466dba8cc4ac1a7f2648afd463ce95. Current/post-gate refresh: revision 0c0dda49f7385df63c1f287c34a452cb684740bc036e2ead0ec82d260fd403bc; same weighted-file hash. | Current/post-gate artifact above. |
| Main focus-tree file, common/national_focus/006_independence_wave_focus.txt | national_focus_ai_will_do; candidates=184; poolComplete=false; availableCandidates=0; requiredInputs=17; unresolved=0. Adapter selection rule is uniform_score_race, requires a complete eligible pool, and is not weight divided by the sum. | revision 2c1fcdbac7036c4ddf6d03f623fa223376981876cab633c6c2f3d9ca1010adcc; hash 146460765accaaccab080cdca0308a185938ff2163e0eea15885ceef97325e7d | hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4b5a067a78e1613da08157faab0a9c53ea70fdb861d6ab49c27d8b6966d1bd61/06fba18715c7cc6a810fc9e35f5c82d1f7dc22ad6632eb5d42874e8ea307fe14/probability-inspect-146460765acc.json |
| Shared focuses, common/national_focus/006_independence_wave_iw043_iw058_focus.txt | no_weighted_surfaces; candidates=0. This is adapter coverage for shared_focus source blocks, not proof of zero engine influence. | revision 1a3d465a8223cf3c99e20d6c510b4961729a2b53a843271c068e503d5735d0da; hash ee2154a71b8a24489f631c41d7b62a85b7cd8b3f4dec22f233fcaac5c815d7c0 | hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/875945b618c9abcda8285c8a41e8c0c036289b6d5248391e968abed1d468f5a3/4cfa08435c8be77c5767250d9c0653fde3e204cda4b6d374e4bb9a643e765240/probability-inspect-ee2154a71b8a.json |
| Shared focuses, common/national_focus/006_independence_wave_iw093_iw098_focus.txt | no_weighted_surfaces; candidates=0. Same adapter limitation. | revision 0f28d86377cf0c7b946d45c178b381c453efe105aac464041367172cc78c80f0; hash 3cdd90abed902e7132cceaf0e9846e6a8008bb14995b489af825ad86b1bfd4c9 | hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/65b926e80a2af52fd26533f3830910d20320456c38dbdc1e7cbebc44bd02c5dd/4f22d0493edd5b4bd2eba9b3f847959f42bd9bade5e12aa6495b561d343184d5/probability-inspect-3cdd90abed90.json |
| Generic Event 006 decisions, common/decisions/006_independence_wave_decisions.txt | decision_ai_will_do; candidates=13; poolComplete=false; availableCandidates=0; requiredInputs=89; unresolved=0. Willingness-score inventory, not click probability. | revision b956c37a811a2ad8531bbfe00935c71a1ab3fcab2bfe50ffbdf89bcb0e701fd5; hash 15158a10e7e7f2e6fe132e7bca5b4525ba1347161f1fcd504c5634bc1f34a25e | hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/413608cfa9b39750c17d8b5f1823542afc59ab94edfa33ffefe23f8716369c34/1aa5bd039b91877537422b36c7f7105bf691bb2fc140f05572abbaf1524f197f/probability-inspect-15158a10e7e7.json |
| Generic Event 006 missions in the same source | mission_ai_will_do; candidates=72; poolComplete=false; availableCandidates=0; requiredInputs=54; unresolved=0. | revision b956c37a811a2ad8531bbfe00935c71a1ab3fcab2bfe50ffbdf89bcb0e701fd5; hash 15158a10e7e7f2e6fe132e7bca5b4525ba1347161f1fcd504c5634bc1f34a25e | hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c1a66edf281e133ee006f5a7917db28052b8c57249b29398a8f717acd72517aa/caa3f7e3bf705416d8983a15ca4cabf5a2a05db456a8f58da5925b1e1d26a30d/probability-inspect-15158a10e7e7.json |
| Shared Event 006 decisions, common/decisions/006_independence_wave_shared_decisions.txt | decision_ai_will_do; candidates=2; poolComplete=false; availableCandidates=0; requiredInputs=6; unresolved=0. | revision b275bf9061010755d6acb1c4e13f97b5f9a2a92f7bc29c3cf1232928848d3583; hash 2fdde2bc8ff09bbefbe09f896cfecc8018097e4b46f1d020a768506a18149b6f | hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3375c75564eb337c108f9c67e2b84f862a4627be04e9d073f40ef3e3d6a78a48/c53ef7ff99e3c73db95d11754ce238a681e219a785fa87eb74d0259ff85170e2/probability-inspect-2fdde2bc8ff0.json |
| Shared Event 006 missions in the same source | mission_ai_will_do; candidates=12; poolComplete=false; availableCandidates=0; requiredInputs=15; unresolved=0. | revision b275bf9061010755d6acb1c4e13f97b5f9a2a92f7bc29c3cf1232928848d3583; hash 2fdde2bc8ff09bbefbe09f896cfecc8018097e4b46f1d020a768506a18149b6f | hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/15f462db6a915be96bb5562b2a1d2ab0ebea47a8e976e7c99cb91b3fdd882a34/e70106bff25f098d4d2f2af3d8a19cc88c0eb6244dfd29f568f0b22fb6090357/probability-inspect-2fdde2bc8ff0.json |
| Event 006 root-event option weights, events/006_independence_wave.txt | event_option_ai_chance; candidates=21; poolComplete=false; availableCandidates=0; requiredInputs=13; unresolved=1. Multiple event-option pools were not normalized together. | revision 7e5a84b6781498a2968fc3f98b331e0c1a0e0a7262b7718cdf6622252fd32956; hash e97272f91cfc0839a63ea4646170cbd57382d446d107869a2ceb2c9145ab76f8 | hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5e40be3877eba1ee8e9401738df0418fefef61ab116e504c16e418bfe27d89b2/1809a7bd5c77c953c833e4ada108b9764e5c7b80f12e6734e9ef38a9fcfcacb4/probability-inspect-e97272f91cfc.json |
| Event 006 support-event option weights, events/006_independence_wave_support_events.txt | event_option_ai_chance; candidates=154; poolComplete=false; availableCandidates=0; requiredInputs=46; unresolved=1. Multiple event-option pools were not normalized together. | revision bf104d1394f8eef1664ded46d34635e1d5bbe5a19eaa1ecbb54797c8c2892a35; hash 4d7ed5adb1d7c26803d1771ba98d4a3c9149fb2e2661d3ff0e770edbcf613437 | hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/59567a31e9790fb08e66e8571990e95f3af2f99a750ef77bbc64ddecd3d1e079/ca67215c23af90eebed5be3b7f4bc455f8df6f67c97d38d568ff77827f483d7a/probability-inspect-4d7ed5adb1d7.json |
| MTTH, events/006_independence_wave.txt | requested_adapter_empty; candidates=0; no timing surface. | revision bcae6aad5876e9a3102780062d6bc4b896cd0509c5abb1995912bf2f93ef58f6; hash e97272f91cfc0839a63ea4646170cbd57382d446d107869a2ceb2c9145ab76f8 | hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/edc58e671c0270cb16088aa01388339b3c5cb9eb02b966f574c55882d3b97f8f/95ab3a63e97931bb315252dba9ad980a343fd732fad038c313cdccef723ef0d7/probability-inspect-e97272f91cfc.json |
| MTTH, events/006_independence_wave_support_events.txt | requested_adapter_empty; candidates=0; no timing surface. | revision 67925e174efecd25620ac972591a463542f32890523d9588f1d2ed271958dfeb; hash 4d7ed5adb1d7c26803d1771ba98d4a3c9149fb2e2661d3ff0e770edbcf613437 | hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ab20b369dd2a92725867b97c557c1156c99ec90eae24615c10e018c648362131/6d22c601f15f9cc3d175bf64f05828720509b98693b5d355cc285ed91aaba734/probability-inspect-4d7ed5adb1d7.json |
| Event 006 AI strategy factor, common/ai_strategy/006_independence_wave_ai_strategy_registry.txt | ai_strategy_factor returned no_weighted_surfaces; candidates=0. The source still contains ai_strategy records, so this is an adapter limit rather than proof of no strategy influence. | revision 24ee3013a548051c8664fc6345674cf0cb5807ef6891709ba59ab61592140dcf; hash b84ee2ca17f45793196641dd0d383779fb2e36ab29da6a1ee2d90912ec82deb6 | hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6ee0c9930851b66c13e0b6650041c50710889bb218c6dbbaf0b8329f7f8db520/d5078e74d45c7866b001a24578fd28af1c7170acaf6e8efc59c9b6803d0e95e3/probability-inspect-b84ee2ca17f4.json |

## Region 04 source score trace (score-only, not a probability)

The current Region 04 random list is independence_wave_select_region_04_automatic_package at common/scripted_effects/006_independence_wave_package_region_effects_registry.txt:974-984. Its complete narrowed source pool contains IW-033, IW-036, IW-037, IW-038, IW-039, IW-040, IW-041, and IW-042. The exact MCP entry IDs are the same path at line 975, entry.1 through entry.8, respectively. Their inputs are the eight independence_wave_weight_iw_* variables named above.

IW-039 is entry.5. Its loader sets package id iw_039, reservation group rg_don_kuban, region eastern_europe_western_russia, depth regional, archetype mountain_or_frontier, disposition automatic_if_not_living, registered-tag use selected, target tag DON, anchor state 245, and primary host from the anchor owner. The reservation effect uses state 245 as the anchor and tries state 238 as an optional compact. It does not reserve state 218 as a package state.

The plan gate can_plan_independence_wave_package_iw_039 requires an open liberation release plan, a free plan slot, package and reservation-group uniqueness, the DHC collision gate, an available DON candidate tag, and an available state 245 anchor. The generic candidate-tag predicate also requires independence_wave_package_content_ready. The shared host/anchor predicate requires an existing owner that controls the anchor and rejects Soviet-collapse origins and reserved/protected states.

The Region 04 weight wrapper initializes independence_wave_weight_iw_039 to allocation_factor.zero, then calls the score helper only if can_plan_independence_wave_package_iw_039 passes. The shared score helper itself initializes independence_wave_candidate_weight to zero. Its positive branch requires has_independence_wave_runtime_package_content_attestation_for_execution_id and the package earliest-chaos-band gate. IW-039 is absent from both has_independence_wave_runtime_package_adapter_for_execution_id and has_independence_wave_runtime_package_content_attestation_for_execution_id in common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt. The shared preflight requires both. This is an exact current-source score-only conclusion: IW-039's calculated allocation weight stays at zero while the attestation remains absent. This is not a normalized selection probability.

The declared shared allocation score constants are base=100, sponsored_candidate=100, registered_tag=25, new_region=30, new_host=20, prior_package_penalty=80, prior_region_penalty=25, prior_host_penalty=20, signature_low_chaos_penalty=35, high_chaos_bonus=45, and minimum=1. The minimum floor is inside the content-attested positive branch. World-collapse rarity is 1.35 in independence_wave_allocation_factor, applied only under its world-collapse/earliest-band condition.

The score helper additionally applies plan-phase and history modifiers for replicable-independence confidence, dormant nations, armed birth, sovereign congress, open sovereignty, prior-wave packages/regions/hosts, sponsorship, registered tags, and high-chaos state. Their applicability and order for a DON campaign were not supplied as a scenario. The source earliest-band constant p39 is 2.

The package archetype is mountain_or_frontier; a separate shared force-profile predicate includes mounted_mobile. Their intended mapping remains unresolved.

The DHC collision trigger requires DHC not to exist, DON not to be reserved/pending/prepared/committed/active, and Event 005 not to have reserved states 218 or 238. The Event 005 call site and IW-039 plan gate both use the shared contract. The RG-DON-KUBAN uniqueness check is present in the plan gate. This is source evidence only; no event-order or state-transfer runtime scenario was evaluated.

## Focus, decision, mission, event-option, and strategy interpretation

The main focus adapter records 17 required inputs: BEL, HOL, LUX, capital_scope, check_variable, custom_trigger_tooltip, event_target:independence_wave_setup_anchor_state, event_target:independence_wave_setup_former_host, exists, focus.external_factors_complete, has_completed_focus, has_cosmetic_tag, has_variable, has_war, is_in_array, original_tag, and var:independence_wave_former_host. Its adapter metadata says ordered AI strategy plans can override weighted focus selection; prerequisites, bypasses, the prerequisite-completion multiplier, and external focus factors need scenario inputs.

The main focus file contains 184 ordinary focus definitions, root-level shared_focus content, and shared_focus references. The two other Event 006 shared-focus source files return no_weighted_surfaces when inspected individually by national_focus_ai_will_do. The probability adapter therefore does not establish an import-complete DON focus-selection pool. The source has 130 shared_focus references; the main file contains 73 shared_focus definitions, and the two separate focus files contain 48 and 43 shared_focus definitions. The 184 probability candidates match the ordinary focus definitions in the main file. Keep the accepted imported-layout proof blocked; the source-scoped focus result must not be promoted to a full shared-focus race.

The structural focus pass used treeId independence_wave_focus_tree and relativePath common/national_focus/006_independence_wave_focus.txt. hoi4.focus_inspect returned FOCUS_INSPECTED, 184 focus nodes, 196 connectors, zero crossings, zero node intersections, one long connector, and no blocking diagnostics. Its inline inventory was truncated at 64 of 92 paths. The warnings were a 10-column connector at focus lines 801-819 and missing vanilla localisation for continuous_restrict_freedom_desc. hoi4.focus_render showed the same 184-node view and layoutHash a4d2d61f7c8f879a7e98ea8e6befc1b6c561138f0373355b91508b4056ad03e7. These are structural artifacts, not probability evidence, and they do not clear the imported-focus baseline blocker.

The decision constants in common/script_constants/006_independence_wave_constants_registry.txt are blocked=0, very_low=2, low=5, standard=10, high=25, urgent=100, modifier_half=0.5, modifier_double=2, and modifier_major=5. These are willingness-score inputs. They do not normalize into decision or mission click probabilities. The generic and shared candidate counts are incomplete adapter inventories with missing state, not ranks. No DON-specific decision or mission source is attached to an admitted IW-039 package.

Event option ai_chance is probability-proportional-to-size sampling, distinct from the focus score race and decision/mission willingness scores. The event-option inspectors found multiple separate option groups in each source and returned incomplete pools; the 21 and 154 counts must not be normalized as one event choice. Example discovered option IDs include chaosx.nr6.2.a and chaosx.nr6.300.a in the root event source and chaosx.nr006.4301.a and chaosx.nr006.4302.a in support events.

Event MTTH inspection returned no timing candidates for either named Event 006 event file. No direct random effect or random_events entry was found in the two Event 006 event files or its on-action registry. The shared region registry contains 14 random_list blocks; only the Region 04 IW-039 pool was narrowed and analyzed. Other region lists were outside this package-specific audit.

The ai_strategy_factor adapter found no compatible weighted surfaces in the consolidated Event 006 AI strategy registry. The source contains regular ai_strategy records with value fields, but no IW-039/DON identifier and no focus_factors declaration was found in the named focus/strategy sources. Do not interpret no_weighted_surfaces as proof of no strategy behavior; the present ai_strategy records are outside this adapter result.

## Scenario completeness and result classification

No scenarioSet, named scenario ID, scenario hash, seed, uncertainty distribution, scheduled state change, cadence, or terminal-state contract was provided. No scenario was created because accepted geography and source scripts do not define the current DON campaign state.

| Surface | Candidate-pool completeness | External-factor completeness | Classification |
| --- | --- | --- | --- |
| Region 04 random list | Complete source shape for eight entries after narrowing. | Incomplete: eight computed weight variables and all campaign gates/history are unbound. | Exact source-pool shape; score-only exact zero for IW-039 under the current missing-attestation gate; normalized probabilities unresolved. |
| Shared package planner | No declared custom-pool manifest; zero adapter candidates. | No cadence/state-transition fixture or runtime input map. | Unresolved adapter coverage, not an empty in-game pool. |
| Generic focus selection | 184 direct candidates only; shared_focus candidates omitted. | Incomplete: 17 adapter inputs, ordered strategy plan, prerequisites, bypasses, and external factors. | Unresolved; no rank or selection probability. |
| Generic and shared decisions/missions | Incomplete adapter inventories. | Incomplete: required inputs range from 6 to 89, depending on source/adapter. | Willingness-score only; ranks and operational likelihood unresolved. |
| Event option AI chance | Incomplete; separate event-option pools were not selected. | Incomplete: 13 root-source inputs and 46 support-source inputs, with one unresolved diagnostic per source. | Unresolved; no option probability. |
| Event MTTH | No MTTH candidates in the two checked sources. | Not applicable to those files. | Exact source-level absence for the checked event files; no timing result. |
| Event 006 AI strategy factor | Adapter found no compatible surface. | Source strategy values and live plan state are not represented by that adapter result. | Unresolved adapter coverage; not proof of no strategy behavior. |

The complete Region 04 source pool does not make its external factors complete. For that pool, the required input names are the eight independence_wave_weight_iw_* variables listed above. The focus artifact retains its exact required-input list. Decision, mission, and event-option artifacts retain their source-linked unresolved input records.

## AI validity, dominance, starvation, reversals, timing, and repetition

The decisive score-only finding is that IW-039's current calculated allocation weight remains zero while its content-attestation gate is absent. Its random-list entry is present, but that does not mean IW-039 is admitted, executable, positive-weighted, or selected.

Dominance, starvation among the other seven Region 04 packages, rank reversals across chaos bands or plan phases, decision/mission ranking, focus-route starvation, repeated package selection, timing drift, and snowball/exploit risk remain unresolved. The planner has previous-wave penalties and conditional phase modifiers, but there is no supported sequence manifest or declared campaign trajectory with which to quantify them.

Zero availableCandidates in the inspectors is adapter/fixture coverage, not real game eligibility. No exact or bounded selection probability, timing estimate, ranking, sampled estimate, sensitivity, or balance claim is made.

## Required follow-up before a weighted patch

No numeric AI weight or balance target is recommended by this audit. Any such suggestion remains unresolved pending user-accepted design and scenario-specific evidence.

Before an owner patch or weight adjustment, the parent should review the IW-039 admission gap: runtime adapter, content attestation, setup, cleanup, and package-content-ready state are absent. Keep the accepted geography and DHC exclusion policy in force, and resolve the mountain_or_frontier versus mounted_mobile mapping without adding a direct-focus fallback.

For a future probability pass, provide named source-grounded fixtures with the complete Region 04 eight-entry pool and real state for the release plan, remaining slots, package/group history, DON identity/readiness, anchor owner/controller and availability, state 218/238 conflict state, DHC collision state, host selection, sponsorship, chaos band, prior-wave history, package adapter/attestation state, and applicable Event 006 phase flags. Focus fixtures need the complete imported shared_focus pool and prerequisite, bypass, ordered-plan, and external strategy factors. Decision, mission, and event-option cases need their own valid candidate pools and availability/target/route inputs.

After an owner-approved source change, use the same named scenarios for probability_compare. Until then, compare has no before/after source pair, and no comparison ID exists.

## Skipped analyses and exact blockers

- probability_evaluate and probability_sweep were not run because there is no valid named DON runtime scenario or complete external-state input set. Supplying only accepted geography would invent campaign state.
- probability_simulate was not run because no uncertain input distributions were explicitly declared.
- probability_sequence was not run because the planner has no complete declared custom-pool manifest, cadence, transitions, cooldown/recovery, cap, removal/reset, timer, or terminal-state contract.
- probability_compare was not run because this is a baseline pass and no source was patched.
- probability_render was not run because no probability analysis ID exists. The unresolved probability view cannot be rendered without an analysis receipt; structural focus and event renders are preserved separately.
- Other random_list pools in the registry were not analyzed because the request names the Region 04 IW-039 pool; the broad inspection correctly marked the registry as multiple categorical pools.
- No IW-039-specific decision/mission score or AI strategy factor is available for an admitted country package because IW-039 is not admitted.
- Event 006 event-chain structural inspection was partial at workspace scale and is not used as package probability evidence.
- No tests or live-game launch were performed, as requested.

## MCP and rendered evidence

All MCP calls were read-only in workspace mod_chaos_redux_ea3b2d67c2c0.

The narrowed Region 04 probability artifact metadata identifies schema probability-inspection.v2, toolVersion 3.0.7, artifact SHA 60d35c4564d162b854b102d8054f821dd6d0eab0fcbec6bd6f7e44d388692a64, and size 11,291 bytes. The 1,048,316-byte main focus-probability artifact was reconstructed and JSON-validated from 53 verified ranges: offsets 0 through 1,039,896 in 19,998-byte chunks, followed by an 8,420-byte final range.

Focus structural revision: af53c4deaa1a0898e81aaff231828f7b0d822008646c86900b5800426c8a8496.
Focus layout hash: a4d2d61f7c8f879a7e98ea8e6befc1b6c561138f0373355b91508b4056ad03e7.
Focus inspect: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bcea56e1e8c21ffa350a922369aeb7aef9143dcac41a6cd5a771607ba92a4680/c7ce4edc41767ce239ed65d2920c2c6ac0928a66e820d1bf58084a865e3c82b5/focus-inspect.af53c4deaa1a0898.json.
Focus render HTML: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/11ec2175bda4262c6a28c70f299fd7eee6e24f3dc9b4d706a65da261bd3f79bf/531f17d67670c5c05fb8179b4af001915878c89885036e27fbcb949333f4f962/independence_wave_focus_tree.focus.html.
Focus render SVG: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5086d880824847a69a40978a74727d27f869e94a735828bcfccb315258f70109/818a708579db553da71aeba59ed578e5e9af6f3f34601b93f091b74e88c0ed38/independence_wave_focus_tree.focus.svg.
Focus render JSON: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/aef8f0c7c0d7584eee5c28f033e560f1327b5eb82bf10865d3f71bde107b6a0c/53e70aed3f24e05bffa0cbc7eb4a7699ff49501fe8004e22828b8accc53d40e6/independence_wave_focus_tree.focus.json.
Focus source map: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/daa5c3e1457a46dbb03e9d992babfcb0d1b47942b4ffe0e1bfe3d52d4d04b664/8633d5d5a5f7ce70fa91b515e043d0c2e0f12357c947fec87c2cd4960055bd3c/independence_wave_focus_tree.focus.source-map.json.
Focus planning manifest: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/58249fcc8452d8d90e60a81edb8790cf2129eb88522da0aac3003525d9203149/4c2f338e2ecde5f14b107bfceb269a4bfe3beb0b12945110c58dc4ccdd17866c/independence_wave_focus_tree.focus.plan.json.

Event structural trace revision: 02aadd003a66d42965ee451ee17108816105638af9ec6f0a31e9ffaa4138eafb.
Event graph hash: 65d862ddd1a7893bfede856be54280246099dc7c95c67203da75673e889a9695.
After the gate update, hoi4.event_inspect and hoi4.event_render were refreshed for chaosx.nr6.1 and returned this same revision, graph hash, and layout hash. The focused event route reads event and on-action sources and does not include the changed scripted-trigger/effect call sites, so these structural receipts do not validate the gate changes.
Event inspect: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c63877ed3aab43735882da6ce28cfdc0d7662ab6b81752da2d48fa7504d06014/0f379b4191a3dd5c8496fe6396f7857514d5f73290abef19827fff19042ae14a/event-trace-02aadd003a66.json.
Event render layout hash: 3ba5f18a64912a9ece6fe76dde07333dd05321a92381135e629786aae491844d.
Event overview manifest: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bc813a760fa2cce693f43f9a39588953546e5e38a2e3f320a6baa4570dca2178/49cd4c236fb169e189f8000dfdedd7b480dbb69e07136a615990a9b6afefed0d/event-overview-02aadd003a66-manifest.json.
Event overview JSON: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/dca8a5dec072a280cb9a1e3f0bdbf776cf5a50b8160151ed5fab3b4c2e5f2fbc/2cec447ee1765dbdfc2448ac12f41eb896a9f831605278fbcbfda55e0752b081/event-overview-02aadd003a66.json.
Event overview SVG: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e8164551830218b24776d59e5839a974314698586a60bd701dcbdc9b032211d6/bdadb74daf02fe49c709f1713830c3300f60f5a418e406a392c9f31b985ab486/event-overview-02aadd003a66.svg.
Event overview PNG: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/61fe55dd7d118d104a2b29fff217f06d7b38418cd42c3d1c09af34a99654eda3/a1b18151f3721690c5445da7d0fe60fdf34a9127a30b4660da638b682b44cf13/event-overview-02aadd003a66.png.

## Handoff status

The current baseline reflects the post-gate cross-event exclusion at the Region 04 pool and planner inspection layer. Numeric rankings, selection probabilities, timing conclusions, balance targets, dominance, starvation, rank reversals, repeated-selection risks, and exploit-risk conclusions remain unresolved for lack of valid runtime fixtures and incomplete imported-focus/strategy-adapter coverage. The parent owns final review and any future source edit.

Skills used: chaos-redux-subagents, chaos-redux-mtth, chaos-redux-events, chaos-redux-focus-trees, and chaos-redux-decisions-missions. No skill was created or modified.
