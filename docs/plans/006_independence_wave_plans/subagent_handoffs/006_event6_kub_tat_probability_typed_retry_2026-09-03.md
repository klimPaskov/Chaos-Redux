# Event 006 KUB/TAT typed probability retry handoff

Date: 2026-09-03.

Status: read-only retry completed; evidence remains partial and blocked on typed scenario state.

Owner: chaosx_ai_probability_auditor.

Scope: the IW-040 Kuban and IW-044 Tatarstan decision and mission AI willingness surfaces only.

No gameplay, AI, trigger, decision, strategy, or tuning source was edited by this audit.

## Authority boundary

This retry preserves the admitted package boundary of 32 content-attested selectable packages, 29 compatible reservation groups, 161 unattested selectable rows, and 40 runtime package adapters.

The accepted addendum is docs/plans/006_independence_wave_plans/006_admitted_package_ai_evidence_tranche_addendum_2026_08_13.md.

The addendum's scenario contract requires real package setup, anchor ownership and control, active-project state, costs, former-host scope, route availability and government, founding and crisis state, both ledgers, Network and League state, and sovereignty state. The retry did not invent any of those values or weaken any trigger to make a pool appear eligible.

## Audited surfaces and source provenance

The historical per-package paths named by the addendum are no longer present in the current workspace. KUB is merged into common/decisions/006_independence_wave_frontier_decisions.txt under the marker for common/decisions/006_independence_wave_kuban_decisions.txt, and TAT is merged into common/decisions/006_independence_wave_siberian_decisions.txt under the marker for common/decisions/006_independence_wave_tatarstan_decisions.txt.

The first fresh inspect against common/decisions/006_independence_wave_kuban_decisions.txt returned PROBABILITY_SOURCE_NOT_FOUND with the exact blocker “Probability source path was not found”. The current merged paths were therefore used for all subsequent calls.

| Surface | Current source and captured source identity | Adapter result |
| --- | --- | --- |
| KUB mission/decision pool | common/decisions/006_independence_wave_frontier_decisions.txt, KUB block lines 614-1175, source revision a50db66e589b56461649b0899dd8cd2a6746b2363e10f3126a47dd1062a3f14f, source hash ccbb75a16ead7ab72ea77e90cf562971f8ede81bba9993e9769c047510eb6c9f | mission_ai_will_do inspect succeeded; decision_ai_will_do was discovered as empty and redirected to mission_ai_will_do |
| TAT mission/decision pool | common/decisions/006_independence_wave_siberian_decisions.txt, TAT block lines 2801-3372, source revision 5e041b74252d33777eb98a1823440b7ed5ce1d4caf5830a4913c1328e55fe172, source hash 9fe87c1b20f9b999fc6e5732ab5d1dee87a8a7b9ed90de0cd31ddd4e7928a5e1 | mission_ai_will_do inspect succeeded; decision_ai_will_do was discovered as empty and redirected to mission_ai_will_do |
| KUB/TAT strategy factors | common/ai_strategy/006_independence_wave_ai_strategy_registry.txt, KUB lines 1696-1748 and TAT lines 3046-3098, captured source revision 838b999c26847acf0a0aac2f431f24707723e140e0ad766a5b8fc0e4c301a595 and hash 9fa2ceabcceb79e6d2240ceac219e1c3304c6c4ca2ae42003958452ecad10ae7 | ai_strategy_factor inspect returned PROBABILITY_SOURCE_DISCOVERED with discoveryReason no_weighted_surfaces; no strategy probability evaluation was supported |

The exact source-relative candidate pools supplied to each mission inspect and evaluate call were complete at 11/11.

KUB pool: independence_wave_kub_hold_mounted_compact_together, independence_wave_kub_secure_mounted_depots, independence_wave_kub_integrate_border_guards, independence_wave_kub_register_community_compacts, independence_wave_kub_settle_former_host_ledgers, independence_wave_kub_ratify_constitutional_autonomy, independence_wave_kub_adopt_agrarian_compact, independence_wave_kub_convene_socialist_councils, independence_wave_kub_establish_mounted_emergency_command, independence_wave_kub_codify_durable_sovereignty, independence_wave_kub_open_black_sea_steppe_network_corridor.

TAT pool: independence_wave_tat_hold_river_compact_together, independence_wave_tat_secure_river_depots, independence_wave_tat_integrate_border_guards, independence_wave_tat_register_community_compacts, independence_wave_tat_settle_former_host_ledgers, independence_wave_tat_ratify_constitutional_autonomy, independence_wave_tat_adopt_agrarian_compact, independence_wave_tat_convene_socialist_councils, independence_wave_tat_establish_river_emergency_command, independence_wave_tat_codify_durable_sovereignty, independence_wave_tat_open_volga_river_network_corridor.

The source-relative pools are complete, but the adapter's empty fixture reported 0 runtime-eligible candidates for both packages. This is not evidence that the choices are dead because the fixture omitted the required package state.

## Source score trace

The merged KUB and TAT blocks use the shared constants in common/script_constants/006_independence_wave_constants_registry.txt at the independence_wave_decision_ai block around line 1251: blocked 0, standard 10, high 25, urgent 100, modifier_double 2.

The captured source bases are exact score values, not selection probabilities.

Founding missions and emergency commands use urgent 100.

Depots, border guards, community compacts, constitutional autonomy, socialist councils, and durable sovereignty use high 25.

Former-host settlement, agrarian compacts, and Network corridor projects use standard 10.

The border-guard and emergency-command scores have factor 2 when has_war is yes.

Former-host settlement has factor 2 when the severe-host-threat trigger is false.

The KUB pressure constants are in the same registry around lines 6332-6365: start ledgers 34 and 41, stable threshold 60, and founding crisis duration 600 days.

The TAT pressure constants are around lines 8827-8860: start ledgers 38 and 44, stable threshold 60, and founding crisis duration 600 days.

The package scripted triggers are common/scripted_triggers/006_independence_wave_kuban_package_triggers.txt and common/scripted_triggers/006_independence_wave_tatarstan_package_triggers.txt. They define package identity, project readiness, cost checks, stable-ledger checks, active-project exclusion, route-government matching, anchor state 234 or 249, former-host event-target scope, and complete setup requirements.

## MCP inspect evidence

All weighted calls began with hoi4.probability_inspect as required.

KUB mission inspect: artifact hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9b5e8804f52ff605aaab55d8576e5dd8a1a1c0266c5a71df90db8c89dee54b93/6d058c52d83c4bee40e7b7001217178e90eb3f0bdeb5bca4cf4e6992a1c0052f/probability-inspect-ccbb75a16ead.json.

TAT mission inspect: artifact hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c0179664804089e46879fcf8e44438d216dd646df2cc804ab25fb61157ba9ea2/0b8c64bde035494af07104f36872cc3cb3c74412b1d428760181a3ee50647859/probability-inspect-9fe87c1b20f9b999fc6e5732ab5d1dee87a8a7b9ed90de0cd31ddd4e7928a5e1.json.

Both inspect artifacts report poolComplete true, 11 candidates, and 0 available candidates for the supplied empty fixture.

The requested decision_ai_will_do adapter was not a separate recognized surface in this source. KUB discovery artifact is hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8c390e4ab819a07149e3574b6e02abd2eebac3274d88a4aa2caeac99a57ea4a2/813dd79d1cda12d6c36fffa0e1e50f985538a171289b096d3496b19cddf3ab01/probability-inspect-ccbb75a16ead.json, and TAT discovery artifact is hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/78f8909b0d1611418521117026752596c9d22b72867fd2c48604bb1aeb2c7ca4/c059e1066280afc0d4e2cbc1553050aca86cf681aeaa00c5ec6c240345e67821/probability-inspect-9fe87c1b20f9b999fc6e5732ab5d1dee87a8a7b9ed90de0cd31ddd4e7928a5e1.json.

Those discovery results have requestedAdapter decision_ai_will_do, discoveryReason requested_adapter_empty, and suggestedAdapter mission_ai_will_do. The effective HOI4 surface is therefore the mission adapter for these decision-category entries.

The strategy inspect artifact is hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/faffdf75b92759cfc9c1e62947b0d95038d6f941121a0e1b05e70a2a1acad76f/6694a2b1b791f5f2aeea4b64f2385da64cd7ea4dcf2fc6aaeab799ceff736fa4/probability-inspect-9fa2ceabcceb.json.

## Named scenario retry results

Each exact named scenario below was submitted in the all-ten evaluation sets for both current package sources. The candidate pool was complete at 11/11, but the state supplied to the adapter was the empty object because the typed actor and scoped-state schema was not available. Thus every result is partial, score-only, and unresolved rather than an exact scenario result.

| Scenario ID | Intended contract from the addendum | KUB source result | TAT source result |
| --- | --- | --- | --- |
| KUB_FRAGILE_PEACE | KUB active, state 234 secure, both ledgers below stable, no war or active project, recovery projects preferred, no route settlement or corridor bypass | poolComplete true; 11 rows; 0 eligible; raw scores 0; unresolved | poolComplete true; 11 rows; 0 eligible; raw scores 0; unresolved |
| KUB_SEVERE_HOST_WAR | KUB active, severe former-host threat or war, capital secure, readiness below stable, emergency security and border guard lane only when gates are valid | poolComplete true; 11 rows; 0 eligible; raw scores 0; unresolved | poolComplete true; 11 rows; 0 eligible; raw scores 0; unresolved |
| KUB_STABLE_ROUTE_LOCK | stable KUB ledgers, one shared route open, no government installed, only the matching government project valid | poolComplete true; 11 rows; 0 eligible; raw scores 0; unresolved | poolComplete true; 11 rows; 0 eligible; raw scores 0; unresolved |
| KUB_NETWORK_READY | founding and crisis resolved, stable KUB state, Network and League route active, durable sovereignty and corridor gates valid | poolComplete true; 11 rows; 0 eligible; raw scores 0; unresolved | poolComplete true; 11 rows; 0 eligible; raw scores 0; unresolved |
| TAT_FRAGILE_PEACE | TAT active, state 249 secure, both ledgers below stable, no war or active project, river recovery projects preferred | poolComplete true; 11 rows; 0 eligible; raw scores 0; unresolved | poolComplete true; 11 rows; 0 eligible; raw scores 0; unresolved |
| TAT_SEVERE_HOST_WAR | TAT active, severe former-host threat or war, capital secure, river readiness below stable, emergency security and border guard lane only when gates are valid | poolComplete true; 11 rows; 0 eligible; raw scores 0; unresolved | poolComplete true; 11 rows; 0 eligible; raw scores 0; unresolved |
| TAT_STABLE_ROUTE_LOCK | stable TAT ledgers, one shared route open, no government installed, only the matching constitutional, agrarian, socialist, or emergency project valid | poolComplete true; 11 rows; 0 eligible; raw scores 0; unresolved | poolComplete true; 11 rows; 0 eligible; raw scores 0; unresolved |
| TAT_NETWORK_READY | founding and crisis resolved, stable TAT state, Network and League route active, durable sovereignty and Volga corridor gates valid | poolComplete true; 11 rows; 0 eligible; raw scores 0; unresolved | poolComplete true; 11 rows; 0 eligible; raw scores 0; unresolved |
| BOTH_RESOURCE_STARVED | post-spend reserves below the shared safe floor, only reserve-preserving actions valid, prestige, corridor, and major-security actions suppressed | poolComplete true; 11 rows; 0 eligible; raw scores 0; unresolved | poolComplete true; 11 rows; 0 eligible; raw scores 0; unresolved |
| BOTH_IMPOSSIBLE_AMBITION | no ready formable family, valid members, or ordinary regional ambition, so ambition/formable choices fail closed | poolComplete true; 11 rows; 0 eligible; raw scores 0; unresolved | poolComplete true; 11 rows; 0 eligible; raw scores 0; unresolved |

The KUB all-ten evaluate-and-render call used scenario set E006_KUB_RENDER_RETRY_2026_09_03, analysis probability-f284108884992cdf27499602, scenario hash 1d1a116f6678b92faec8a2097de35eb0691efb7ce5876424f032c35199a7d91e, 10 scenarios, 110 candidates, 310 unresolved entries, and 11 never-eligible diagnostics.

KUB evaluation JSON: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c0466c16ecc1f792b33aafd2aa5f0d1e6c4944055ad6eb5651318155ce8675cd/cdc7fab29f249b9beced35ec3d9f2a20119f5611b3edfce0c7da141aae1821c2/probability-f284108884992cdf27499602.json.

KUB rendered ranking: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a9ad362969d26060b74e93b4080213aa91ea5a01051050beb73ae84351484094/a9a1e3d786f5b9d2f91d4cf9633bc0fd5fd60cb91e1d076a8e7e6b81919d6674/probability-probability-f284108884992cdf27499602-ranking.svg.

KUB rendered matrix: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/11efad837080ab75e007616194443cf76492ff0ff12b357df249ae61e0f689a4/61fc41cca576466fccaf60c492db68fef940359b04977d2d6ca5dcb3a1c12205/probability-probability-f284108884992cdf27499602-matrix.svg.

KUB rendered unresolved view: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e86cbc5ec81631228af20fcfdf737556af35be471d9e21953467f74cad2260e8/ff4eabf1a2c7fdf3d927ab7a973b7f4074d18f61f71dacaa54e3936a52fc46c7/probability-probability-f284108884992cdf27499602-unresolved.svg.

The TAT all-ten evaluate-and-render call used scenario set E006_TAT_RENDER_RETRY_2026_09_03, analysis probability-357d275561c6e7672ef536cb, scenario hash 4154a33f831ca57dac1360508f1900f3ff6ce092b53a6e8c71ef5b7cf190f331, 10 scenarios, 110 candidates, 311 unresolved entries, and 11 never-eligible diagnostics.

TAT evaluation JSON: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/111b1873d5a9e94bafa8868319d6211b7194b45170a6bd726f8b0f46421fb43c/bf939e15a4b25cd7cfa2c7b0d7bdda1a04847f52e35c3802402203dd61eaeef9/probability-357d275561c6e7672ef536cb.json.

TAT rendered ranking: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/faa07a3da9efcfefad55dd625c174f5187d23ee35de10f10db03f6219f842195/256beb10e8e84bd55bb050dc243e55f7cfcc458da73766f54392cb3dbf763835/probability-probability-357d275561c6e7672ef536cb-ranking.svg.

TAT rendered matrix: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4d56d4dee7f79a0e35f6fa373d0662abc445fe830271f29418ff655a76b73ee5/3eab7ddb9d6a686b34058a0638c6a774e80ebeb91cf98241375581d6bc330755/probability-probability-357d275561c6e7672ef536cb-matrix.svg.

TAT rendered unresolved view: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3fadbccb7181fc89f985fd2269f0e2b8132c94d87f2fea1fc2fcfaabca854bea/6f3440c52a774f92666232b5393513f608d4ae5a8253cdb29644474bfa1ccb4b/probability-probability-357d275561c6e7672ef536cb-unresolved.svg.

The render calls were made in the same server process as their evaluate calls. An earlier separate-process render returned PROBABILITY_ANALYSIS_NOT_CACHED with the exact message “Render requires an analysis ID produced by this server process”; the same-invocation retry above is the authoritative rendered evidence.

## Typed primitive probes and exact schema blockers

To test whether direct scalar declarations were accepted without changing source, two separate one-scenario probes were run using the IDs KUB_FRAGILE_PEACE_PRIMITIVE_RETRY and TAT_FRAGILE_PEACE_PRIMITIVE_RETRY. The probes declared direct primitive values for original_tag, exists, has_war, command_power, has_manpower, has_stability, has_war_support, has_army_experience, num_of_civilian_factories_available_for_projects, has_equipment, has_decision, has_variable, capital_scope, check_variable, and var:independence_wave_former_host.

Both probes returned PROBABILITY_ANALYZED_PARTIAL with poolComplete true, 11 rows, all eligibility false, raw values 0, and score_only support.

KUB primitive analysis: probability-c1dc5ff6a8fcdf8ac5be3457, scenario hash ecf879662d5eea30d888153d8a9bc3f62ea633eae15f8b8779dc447f6709a51f, 243 unresolved entries, 13 diagnostics. JSON artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/380a4dea816471a55b1a4f1a0fd6a4ca85c1095bb1d351d416e3ddb52e253cf3/2c4988b7798426c7bab61eeeee859ae03f79ad748f7d3db1007e13236b452a44/probability-c1dc5ff6a8fcdf8ac5be3457.json.

TAT primitive analysis: probability-d15a002bba037b009ece2d2f, scenario hash 989535e9d19e029bcee55a34c7e3d26a4ff5fb1892b430e1d975352d35d2d517, 244 unresolved entries, 13 diagnostics. JSON artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7a3208a17fa601eaacdbf977507b66657f837e192cd1215e4c278d6869f2e750/98367226f5a2278eba7871821c723f75a8be0c8b1aca1796a349eee762053a3b/probability-d15a002bba037b009ece2d2f.json.

The exact unresolved trigger categories in both probes were:

- The scenario does not declare an actor for original_tag.

- check_variable requires a declared variable and value.

- event_target:independence_wave_setup_former_host and event_target:independence_wave_setup_anchor_state are not declared by the scenario.

- Numeric setup variables are not declared: independence_wave_setup_package_id, independence_wave_setup_region, independence_wave_setup_depth, independence_wave_setup_territory_level, independence_wave_setup_force_level, independence_wave_setup_chaos_band, and independence_wave_setup_archetype.

- Scoped or compound triggers cannot be evaluated: has_equipment, capital_scope, and var:independence_wave_former_host.

- The declared scenario booleans could not be compared by has_variable or has_decision, and the declared scalar values could not be compared by command_power, num_of_civilian_factories_available_for_projects, has_stability, has_manpower, and has_army_experience.

- KUB ledger variables independence_wave_kub_rada_cohesion and independence_wave_kub_mounted_readiness were not declared, and TAT ledger variables independence_wave_tat_rada_cohesion and independence_wave_tat_river_readiness were not declared.

- TAT also could not compare has_war_support.

- independence_wave_reconquest_fear was not declared.

The 13 diagnostics per primitive probe consist of 11 PROBABILITY_OUTCOME_NEVER_ELIGIBLE diagnostics, one for every source candidate, plus two PROBABILITY_MODIFIER_UNSATISFIED_IN_SCENARIOS diagnostics for the has_war factor on border guards and emergency command. The latter factor was correctly not active in the fragile-peace probe with has_war false.

The primitive trace still exposed the exact source bases: urgent 100 for founding and emergency, high 25 for depots, guards, communities, constitutional, socialist, and durable sovereignty, and standard 10 for former-host, agrarian, and corridor. In the no-war primitive probe the former-host no-severe-threat factor resolved true and produced 20 from the standard base, while the war factors remained unsatisfied. This is score evidence only; no candidate became selectable.

## Sweep, comparison, and other workflow results

The required probability_sweep route was attempted for KUB and TAT with findRankReversals true, pairwise true, paths state.command_power and state.has_war, and three steps.

Each sweep returned PROBABILITY_SWEEP_RANGE_REQUIRED with the exact message “Every sweep path requires a scenario range, numeric alternatives, or numeric state value”. The KUB empty-set blocker identified scenario KUB_FRAGILE_PEACE and path state.command_power. The TAT primitive blocker identified scenario TAT_FRAGILE_PEACE_PRIMITIVE_RETRY and path state.command_power. No threshold, sensitivity, or rank-reversal artifact exists.

probability_compare was not run because there is no owner-provided before/after patch and no complete typed baseline. The addendum forbids inventing a candidate patch or claiming a balance defect from the empty fixture, so no comparison is applicable.

probability_simulate was skipped because no declared uncertain input distribution was complete.

probability_sequence was skipped because no complete custom weighted pool with cadence, cooldown, state transitions, and terminal states was declared for KUB or TAT.

Event, focus, GUI, and technology structural analyses were outside this decision/mission weighted tranche; no event-option, focus-selection, GUI-linked choice, technology, or doctrine candidate was included in the requested KUB/TAT pool.

## Findings and balance conclusion

The adapter proves that these entries are score-only AI willingness surfaces. Its capability report has selectionRule score_only, rawScore true, normalizedProbability false, sequence false, and timeDistribution false. Therefore an ai_will_do value such as 100, 25, or 10 is not a click probability and cannot be normalized into one from this evidence.

The source-relative candidate pools are complete at 11/11 for both packages, but the runtime scenario state is incomplete. All ten named scenarios on each package source therefore returned all-false, raw-zero rows because every candidate's eligibility depended on unresolved package state or scoped triggers.

No exact dominance, starvation, rank reversal, repetition, timing drift, or exploit/snowball conclusion is supported. No impossible-positive-weight defect is proven because the adapter could not establish the corresponding availability gates. In particular, the empty result for BOTH_IMPOSSIBLE_AMBITION does not prove fail-closed ambition behavior, and the empty result for BOTH_RESOURCE_STARVED does not prove reserve-preserving behavior.

The only exact balance-relevant evidence is the source score ladder and its conditional modifier traces described above. A complete same-scenario comparison is required before any source-safe weight patch can be proposed. This retry provides no such proof; no patch is recommended and no source change is authorized.

## Remaining blocker and next safe action

The blocker is the missing typed scenario schema for HOI4 actor scopes, event targets, flags, `check_variable` and scoped trigger values, numeric package/setup variables, ledger values, route/government state, and target validity. The adapter accepts a candidatePool override and reports it complete, but it does not accept the nested typed fixture shape previously attempted, and direct primitive declarations still produce the exact unresolved categories above.

The next audit may proceed only after the probability adapter documents or accepts a complete typed fixture for the addendum's package state, or after an authoritative MCP fixture manifest supplies those values. Once that exists, rerun all ten exact scenario IDs with the unchanged 11/11 pools, then run sweep and same-scenario compare only if a complete before/after baseline exists.

Conclusion: KUB/TAT typed probability retry is evidence-blocked, not a source-balance approval. No gameplay files were changed.

## References consulted

Relevant prior handoffs consulted were docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw040_iw044_typed_probability_baseline_2026-08-15.md, docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_probability_mcp_recovery_2026-09-02.md, docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw044_tatarstan_ai_mirror_repair_2026-08-14.md, and docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_ai_probability_baseline_2026-09-03.md.

Before the MCP calls, the offline Paradox wiki pages paradox_wiki/AI modding - Hearts of Iron 4 Wiki.md, paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md, paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md, paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md, paradox_wiki/Effects - Hearts of Iron 4 Wiki.md, paradox_wiki/Modifiers - Hearts of Iron 4 Wiki.md, paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md, paradox_wiki/Event modding - Hearts of Iron 4 Wiki.md, paradox_wiki/Localisation - Hearts of Iron 4 Wiki.md, paradox_wiki/On actions - Hearts of Iron 4 Wiki.md, and paradox_wiki/Idea modding - Hearts of Iron 4 Wiki.md were consulted.

The installed vanilla documentation consulted for the weighted decision and mission surfaces was C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\script_concept_documentation.md, C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\triggers_documentation.md, C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\effects_documentation.md, and C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\modifiers_documentation.md.
