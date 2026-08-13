# Event 018 probability and AI bounded-closure audit

Date: 2026-08-10. Scope: current Event 018 Resources Found weighted surfaces after the field workboard change. This is a read-only MCP/source audit. No gameplay, AI, event, focus, decision, or runtime source was changed.

## Verdict

The authored pools inspected here do not show a confirmed balance, dominance, starvation, rank-reversal, repetition, or exploit defect. The user's no-unresolved-AI-evidence gate cannot honestly close. Several authored pools are complete at inspection but their score evaluation remains bounded because the installed adapter cannot type the full campaign predicates, and the event-wide option pool remains incomplete. Direct random rolls, scripted MTTH variables, mission applicability, and fixed AI-strategy blocks are adapter-only limitations rather than source defects, but they are still not engine evidence.

The strongest current conclusion is therefore: **no confirmed weighted-logic defect; bounded static/source evidence is positive; complete normalized AI/probability closure is not proven.**

## Evidence boundary and required references

I read `AGENTS.md`, `.agents/skills/chaos-redux-subagents/SKILL.md`, `.agents/skills/chaos-redux-events/SKILL.md`, `.agents/skills/chaos-redux-focus-trees/SKILL.md`, and `.agents/skills/chaos-redux-decisions-missions/SKILL.md` before source review. I read the complete `docs/specs/018_resources_found_specs/` package, the prior dated probability/focus/decision handoffs, the current workboard changes, the offline Paradox wiki core pages, and the required vanilla documentation.

Current weighted source files are `common/national_focus/018_resources_found_cave_focus_tree.txt`, `events/018_random_resource.txt`, `common/decisions/018_resources_found_decisions.txt`, `common/scripted_effects/018_resources_found_prefire_effects.txt`, `common/scripted_effects/018_resources_found_cave_effects.txt`, `common/scripted_effects/018_resources_found_effects.txt`, `common/scripted_effects/018_resources_found_decision_effects.txt`, `common/ai_strategy/018_resources_found_ai_strategy.txt`, and the Event 018 scripted-trigger/effect files consumed by those sources.

All MCP calls were read-only. Every weighted source started with `hoi4.probability_inspect`; supported pools then used `hoi4.probability_evaluate` with declared scenario IDs and rendered ranking/matrix/unresolved artifacts. No exact selection probability is claimed where a complete candidate pool or typed external state is absent.

## Surface summary

| Surface | Current inspect result | Evaluation result | Classification |
| --- | --- | --- | --- |
| Focus hierarchy | Complete three-candidate named pool | Partial score race, 6 rows, 11 unresolved | Bounded score-only; no defect proven |
| Focus doctrine | Complete three-candidate named pool | Partial score race, 6 rows, 6 unresolved | Bounded score-only; no defect proven |
| Focus adaptation | Complete six-candidate named pool | Partial score race, 12 rows, 6 unresolved | Bounded score-only; empty-state warnings expected |
| Focus continental | Complete eight-candidate named pool | Partial score race, 16 rows, 20 unresolved | Bounded score-only; late-route fixtures absent |
| Focus world-end | Complete four-candidate named pool | Partial score race, 8 rows, 30 unresolved | Bounded score-only; terminal-route fixtures absent |
| Event options, whole file | 204 candidates, poolComplete=false, 18 required inputs, 1 unresolved | No honest whole-file normalization | Incomplete heterogeneous pool |
| Event `.1` options | Exact four-candidate pool complete | Partial, 8 rows, 4 unresolved | Bounded score-only |
| Selected-field decisions | Exact 29-candidate pool complete, 8 required inputs, 0 inspect unresolved | Partial, 87 rows, 296 unresolved | Bounded score-only; AI page bypass confirmed |
| Prefire random lists | Six authored entries discovered, poolComplete=false, 4 required inputs | Partial, 12 rows, 7 unresolved | Dynamic state-bound random list |
| Cave brood random list | Five authored entries complete, 5 required inputs | Partial, 15 rows, 5 unresolved | Dynamic route-bound random list |
| Six-way resource roll/evolution roll counts | `direct_random` reports no weighted surfaces | Not available through adapter | Adapter-only limitation |
| Event MTTH | No direct event MTTH surface | Not applicable for direct event timing | Scripted MTTH variables are adapter-only |
| Mission applicability | Mission adapter empty; decision adapter suggested | Not available as mission score | Adapter-only limitation |
| AI strategy factors | Fixed Event 018 strategy source reports no weighted surfaces | Not available | Adapter-only limitation |

## Focus selection pools

The focus tree source contains 67 focuses. The following five named pools were supplied exactly as bounded selection races.

### Hierarchy pool

Candidates: `DHO_one_maw`, `DHO_many_chambers`, `DHO_hoard_the_veins`.

Inspect: `poolComplete=true`, candidates=3, requiredInputs=6, unresolved=0, sourceHash `5ff8349e0c8301714c3d721c172141d7e5aef70e60ac0d640e7189e06329dfd8`, sourceRevision `01e568d4f1ccdc5e4b0dc52074b9de7ddad2b7b2b970cf00d455a9b5441c5d72`, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/40751f207a2896e8dc87c59a781e6871e1f548bae5d270b0ed66144afb31d2fb/b1d91c71b004ee6a35e33bd5918f1e74f17fd3a5afb19a1119750a26245070b5/probability-inspect-5ff8349e0c83.json`.

Scenarios: `FOCUS_HIERARCHY_VALID_BASELINE` with empty state and `FOCUS_HIERARCHY_WAR` with `has_war=true`. Evaluate analysis `probability-f86138e0d204a7c0762c86b9`, scenarioHash `3f4b4d3861d7c189625b74c50453d9b0a6ca7a42db20994f94739fc89f568f35`, candidates=6, unresolved=11, diagnostic count=1. MCP returned JSON, ranking, matrix, and unresolved resources for this analysis; the analysis ID and scenario hash are the stable lookup keys, while the source inspect artifact above is the exact retained inspect URI.

The only diagnostic was the expected unsatisfied `@cave_ai_disabled` factor for `DHO_one_maw` in the empty fixture. This is not a live route ranking or starvation proof.

### Doctrine pool

Candidates: `DHO_stone_phalanx`, `DHO_burrow_war`, `DHO_scree_tide`.

Inspect: `poolComplete=true`, candidates=3, requiredInputs=3, unresolved=0, sourceHash `5ff8349e0c8301714c3d721c172141d7e5aef70e60ac0d640e7189e06329dfd8`, sourceRevision `01e568d4f1ccdc5e4b0dc52074b9de7ddad2b7b2b970cf00d455a9b5441c5d72`, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6633ae0ee12d5df636f3d0c1d31b1156ca864d9b77180fa4df8a54a3c03aad5d/5bfdd8c89273c3d70889e08c12346f2883da92d8ad6276af31595587b292d283/probability-inspect-5ff8349e0c83.json`.

Scenarios: `FOCUS_DOCTRINE_VALID_BASELINE` with empty state and `FOCUS_DOCTRINE_WAR` with `has_war=true`. Evaluate analysis `probability-fbb193c7884327c35922c074`, scenarioHash `79d8f28d792f749c41fde13a187acbf77be14716e139f76346941c454f2fe931`, candidates=6, unresolved=6, diagnostic count=1. MCP returned JSON, ranking, matrix, and unresolved resources for this analysis; the analysis ID and scenario hash are the stable lookup keys, while the source inspect artifact above is the exact retained inspect URI.

The sole diagnostic was the expected unsatisfied cave-AI factor for `DHO_scree_tide` in an empty fixture.

### Adaptation pool

Candidates: `DHO_study_broken_weapons`, `DHO_grow_denser_plates`, `DHO_open_the_joints`, `DHO_surface_senses`, `DHO_harden_against_the_sky`, `DHO_choose_the_final_adaptation`.

Inspect: `poolComplete=true`, candidates=6, requiredInputs=1, unresolved=0, sourceHash `5ff8349e0c8301714c3d721c172141d7e5aef70e60ac0d640e7189e06329dfd8`, sourceRevision `afd94a86de094d8ca1b488ad5b1baaacd0893df5f0705370a7579332db1bf427`, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/72a6890cbd1392efd59c33c21451360ec9dec15c5ceec2a5ad2c80c8ea366ded/9b9436fa7c8202d8d7b0e888a306e7a4ef7814db42a1626f80d1d9c706a04328/probability-inspect-5ff8349e0c83.json`.

Scenarios: `FOCUS_ADAPTATION_VALID_BASELINE` with empty state and `FOCUS_ADAPTATION_WAR` with `has_war=true`. Evaluate analysis `probability-dd9e09688c72e016a2ca1267`, scenarioHash `8a303d18b9bbbe196676e5e1cc891f5e40520e5eda42afb41ba3cdf7802399fa`, candidates=12, unresolved=6, diagnostic count=4. MCP returned JSON, ranking, matrix, and unresolved resources for this analysis; the analysis ID and scenario hash are the stable lookup keys, while the source inspect artifact above is the exact retained inspect URI.

The warnings that `DHO_study_broken_weapons` and `DHO_grow_denser_plates` are never eligible are expected under empty route/equipment fixtures. No starvation conclusion is valid without a typed adaptation-state scenario.

### Continental pool

Candidates: `DHO_mark_the_richest_route`, `DHO_break_the_first_ring`, `DHO_consume_an_industrial_belt`, `DHO_take_the_continental_capitals`, `DHO_seal_the_coast`, `DHO_break_continental_coalitions`, `DHO_consume_the_last_resistance`, `DHO_continent_consumed`.

Inspect: `poolComplete=true`, candidates=8, requiredInputs=5, unresolved=0, sourceHash `5ff8349e0c8301714c3d721c172141d7e5aef70e60ac0d640e7189e06329dfd8`, sourceRevision `de8eb594d9c200851041a1e5d43e65d79cb86ba856a838a3bd6014d7ff60e914`, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/dbd63257ba8284596cf4cef7701452e8dc45e4d83bd6d51e55d2023626bc9fe9/c3183ac7c44a82edb783647299cc2db1be10f004e723bd9c74c82c37b4360ba5/probability-inspect-5ff8349e0c83.json`.

Scenarios: `FOCUS_CONTINENTAL_VALID_BASELINE` with empty state and `FOCUS_CONTINENTAL_WAR` with `has_war=true`. Evaluate analysis `probability-21596478fb49e739e462c30c`, scenarioHash `42ec28219f223aeb964d5fe6c9b66c9d39166339b1eae22aa766136b066cd0b0`, candidates=16, unresolved=20, diagnostic count=3. MCP returned JSON, ranking, matrix, and unresolved resources for this analysis; the analysis ID and scenario hash are the stable lookup keys, while the source inspect artifact above is the exact retained inspect URI.

The warnings for `DHO_take_the_continental_capitals`, `DHO_consume_the_last_resistance`, and `DHO_continent_consumed` are expected late-route fixture omissions.

### World-end pool

Candidates: `DHO_deepen_the_continental_heart`, `DHO_listen_beneath_distant_shores`, `DHO_choose_the_first_rupture`, `DHO_the_world_opens_below`.

Inspect: `poolComplete=true`, candidates=4, requiredInputs=7, unresolved=0, sourceHash `5ff8349e0c8301714c3d721c172141d7e5aef70e60ac0d640e7189e06329dfd8`, sourceRevision `08d5c8181eda0db624ba7b7c50bc2ac3c154dc4ce458ffb8b44c729b03913a60`, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/32829eba41eddb504892199ebc13d8e844232433778c0a1f0c91de6e4d529f15/b86c538864f4c4822fa348be28734ee0c14adf3d673b060ebcc3974e247d13f8/probability-inspect-5ff8349e0c83.json`.

Scenarios: `FOCUS_WORLD_END_VALID_BASELINE` with empty state and `FOCUS_WORLD_END_WAR` with `has_war=true`. Evaluate analysis `probability-c9b2015c0d9c78c0a6f5fe08`, scenarioHash `c7a951ef465d5ed77489d7716caf7bbf57c4e0ec04278a28ffb781123fc49fb4`, candidates=8, unresolved=30, diagnostic count=2. MCP returned JSON, ranking, matrix, and unresolved resources for this analysis; the analysis ID and scenario hash are the stable lookup keys, while the source inspect artifact above is the exact retained inspect URI.

The warnings for `DHO_deepen_the_continental_heart` and `DHO_the_world_opens_below` are expected terminal-route fixture omissions.

All five focus pools are complete candidate manifests. Their evaluations remain score-only bounded evidence, not focus click probabilities. No dominance or starvation claim is supported by the empty/war fixtures.

## Event option pools

The current `event_option_ai_chance` inspect on `events/018_random_resource.txt` found sourceHash `6999853c6a9dfcefaa69fcfcb77f77e070b56a9eb7ca91cc6f936701a9681b7c`, sourceRevision `5bf4a8f899157f8ac337dd9d2a964229b0182b51d968c867157fecc568269ff5`, 204 candidates, 18 required inputs, `poolComplete=false`, and one unresolved item. Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7b198c0906023291206607c09d856c5187645d22a8146a8acf6edee461d8dd9b/4bf89639a36f12728e8f51306030080796c6210343e901dd318942d63058cdcd/probability-inspect-6999853c6a9d.json`.

The source was segmented into exact event-ID pools as follows. The letters are the complete authored `ai_chance` option candidates for each event.

| Event ID | Options | Event ID | Options | Event ID | Options |
| --- | --- | --- | --- | --- | --- |
| `chaosx.nr18.1` | a,b,c,e | `.2` | a,b | `.3` | a,b,c |
| `.4` | a,b,c | `.5` | a,b,c | `.6` | a |
| `.7` | a,b,c | `.8` | a,b,c | `.9` | a |
| `.10` | a,b,c | `.11` | a,b,c | `.12` | a,b,c,e |
| `.13` | a,b,c | `.14` | a,b,c,f,e | `.15` | a |
| `.20` | a,b,c,e | `.21` | a,b,c | `.22` | a,b,c,e |
| `.23` | a | `.24` | a,b,c | `.25` | a |
| `.26` | a,b,c | `.27` | a | `.28` | a,b,c |
| `.29` | a,b,c | `.30` | a | `.31` | a,b,c |
| `.32` | a,b | `.40` | a,b,c,e | `.41` | a,b,c |
| `.42` | a,b | `.43` | a,b,c | `.44` | a,b,c |
| `.50` | a,b,c,e | `.51` | a,b,c,e | `.52` | a,b,c,e |
| `.53` | a,b,c,e | `.54` | a,b,c,e | `.55` | a,b |
| `.56` | a,b,c,e | `.57` | a,b,c,e | `.58` | a,b,c,e |
| `.59` | a,b | `.60` | a,b,c | `.61` | a,b,c,e |
| `.62` | a,b,c | `.63` | a,b,c,e | `.64` | a,b,c |
| `.65` | a,b,c,e | `.66` | a,b | `.67` | a,b,c |
| `.68` | a | `.69` | a,b | `.70` | a,b |
| `.71` | a | `.72` | a,b | `.73` | a,b,c |
| `.80` | a,b,c | `.81` | a,b,c | `.82` | a,b,c,e |
| `.83` | a,b,c,e | `.84` | a | `.85` | a,b,c |
| `.86` | a,b,c | `.87` | a,b,c | `.88` | a |
| `.89` | a,b,c | `.90` | a | `.91` | a |
| `.92` | a | `.93` | a,b | `.94` | a |
| `.95` | a | `.96` | a,b | `.97` | a |
| `.98` | a | `.99` | a,b,c |  |  |

Single-option events are deterministic within their option family but still require their event-level eligibility state. They are not treated as 100% campaign probabilities.

The exact `.1` pool was inspected with candidates `chaosx.nr18.1.a`, `chaosx.nr18.1.b`, `chaosx.nr18.1.c`, and `chaosx.nr18.1.e`; `poolComplete=true`, candidates=4, requiredInputs=2, unresolved=0, and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/afc658dfbd14d485883fed6d0fed46df632f33e5f95ed127d77ae172af8fc122/eeb09c8431801f5d9720043c61b8595805ec154691f632f14e53baf959f9d18b/probability-inspect-6999853c6a9d.json`.

`.1` evaluation used scenario set `E018_EVENT_OPTIONS_1_CURRENT_2026_08_10` with `E018_EVENT_1_VALID_BASELINE` state `{}` and `E018_EVENT_1_INVALID_NO_FIELD` state `{has_war:true}`. Analysis `probability-24faf58a4b15679e53c33b90`, sourceRevision `5bf4a8f899157f8ac337dd9d2a964229b0182b51d968c867157fecc568269ff5`, sourceHash `6999853c6a9dfcefaa69fcfcb77f77e070b56a9eb7ca91cc6f936701a9681b7c`, scenarioHash `42ea3240e720e71d4e3101010ce9760c1c6030840b8d57e43832721444f00b16`, candidates=8, unresolved=4, diagnostics=0. JSON artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c3a5ed86f7964defbec37b8032066db2246d841a16c35e25ecbb6b3e225d2b1b/b9156d03ffb9c5a180f5525bbc8f0771c905a9d71a4ccb3768747fd836684fd7/probability-24faf58a4b15679e53c33b90.json`; MCP also returned ranking, matrix, and unresolved resources for this analysis.

The remaining event-ID families were statically enumerated but not each independently evaluated in this closure turn. The whole-file adapter explicitly withholds normalized odds because the heterogeneous 204-candidate pool and typed event predicates are incomplete. This is an evidence omission/adapter limitation, not a source defect claim.

## Decision score pool and presentation-page bypass

The current selected-field bounded decision pool is exactly these 29 candidates:

`resources_found_cycle_field_workboard`, `resources_found_refresh_field_project_estimates`, `resources_found_cycle_selected_field`, `resources_found_refresh_evolution_clocks`, `resources_found_establish_national_authority`, `resources_found_charter_domestic_operators`, `resources_found_place_field_in_strategic_reserve`, `resources_found_commission_geological_appraisal`, `resources_found_drill_deeper_test`, `resources_found_map_surrounding_basin`, `resources_found_open_primary_works`, `resources_found_extend_rail_road_corridor`, `resources_found_install_heavy_machinery`, `resources_found_build_local_processing`, `resources_found_expand_worker_settlement`, `resources_found_build_integrated_processing_corridor`, `resources_found_unify_compound_authority`, `resources_found_split_resource_concessions`, `resources_found_recruit_regional_labor`, `resources_found_shorten_shifts_rotate_crews`, `resources_found_reinforce_shafts_ventilation`, `resources_found_establish_field_hospital`, `resources_found_compensate_affected_families`, `resources_found_conceal_casualty_reports`, `resources_found_regulated_output`, `resources_found_maximum_shifts`, `resources_found_wartime_requisition`, `resources_found_emergency_suspension`, and `resources_found_reactivate_suspended_field`.

Current inspect: `poolComplete=true`, candidates=29, requiredInputs=8, unresolved=0, sourceHash `dd2e5ef3aa158a6a1f175f17cee63246dc3692e2b50016059a3cc72213b9361f`, current inspect revision `b0644cccbc94a4f77df61a435e56a5fb95c469d49f071389d39608cd0f0eb9db`, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8bd746e7784d47f47c1ab390afadef5e6cb83d84415edc94fa95ea6a406d32ec/c67f6abad53661614f75f7dd21be7b6a7ed8df3f734df0c7d9d9da51a3f35f24/probability-inspect-dd2e5ef3aa15.json`. The parent also retains a post-workboard inspect at revision `65977b1a30fdc9b258aa2606a58936e45e8cc3d43c5a81fdbea9d8804060af89` and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8a205eeded51bf7653fb51f73b4b98e22fda39ef19cc1777b3050a2011780302/8448b525fc55e2bd08176187552c7292883a5aef637b8b48080ad31a4576a37f/probability-inspect-dd2e5ef3aa15.json`.

Evaluation scenario set `E018_DECISIONS_SELECTED_FIELD_CURRENT_2026_08_10` contains `DECISION_AI_PRESENTATION_BYPASS_BASELINE` with empty state, `DECISION_AI_PRESENTATION_BYPASS_WAR` with `has_war=true`, and `DECISION_AI_PRESENTATION_BYPASS_MAJOR_WAR` with `{has_war:true,is_major:true}`. Analysis `probability-f3c46d006373f96d2da4fe16`, sourceRevision `1e24d33aafd6c9d0853bacb6291bcbef89a6e1bbb7999280acff445419961fad`, scenarioHash `c064789f72a90dad4a4801c74a132797cd557b331ee254c1f1c07560b2559669`, candidates=87, unresolved=296, diagnostics=25. JSON artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c72074177f4763bbaf051b750d02cfd806e70bf8aa2f0a649a71c1e46f0d0b18/ab1991673ea4f37453e2dfb779e4cf6cc0bbcb8ad3e3abc0c0a55acd7219a4d3/probability-f3c46d006373f96d2da4fe16.json`; ranking `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/09ab14cb519049a31060d1d21d30c3ee06f4c4af7ddba35ff0d4bd19632637a4/476557d72fd1e015ef04dd8912066367c659050f0541dd030f2fec350b2acf0c/probability-probability-f3c46d006373f96d2da4fe16-ranking.svg`; matrix `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e1067acf279b4957b4bd0dd34fa03e780f336765f2f8afae27d46758ccce781c/21a0105107289b704288ccdd9709b3762ad009280aa67d5bffcdc74588293362/probability-probability-f3c46d006373f96d2da4fe16-matrix.svg`; unresolved `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/36f45addf2d9097f9534e156ddf0f60398bb7487ed6e869d0634ee234d49f3ec/f2b24b65138738d72d8d2e6c9d55b673e69963f3e01c5548af5fecedf07ecd43/probability-probability-f3c46d006373f96d2da4fe16-unresolved.svg`.

The 25 warnings are mostly `PROBABILITY_OUTCOME_NEVER_ELIGIBLE` under the empty field/route fixture, including local processing, integrated processing corridor, charter, appraisal, reserve, drilling, transport, machinery, labour, hospital, casualty, operations, suspension, and reactivation. They are not live-world starvation findings. The source's `resources_found_cycle_field_workboard` is `NOT = { is_ai = yes }`, and page navigation/actions are human presentation only. AI bypasses the page layer and evaluates ordinary decision/effect routes. This confirms the requested AI presentation-page bypass.

This decision result is a score race, not a click probability. The complete 29-candidate inspect pool is a strong bounded input proof, but the 8 typed external inputs remain unresolved in evaluated scenarios.

## Random-list and direct-random surfaces

### Prefire random lists

`common/scripted_effects/018_resources_found_prefire_effects.txt` contains exactly three `random_list` blocks and six authored entries:

1. `common/scripted_effects/018_resources_found_prefire_effects.txt:150.entry.1` and `:150.entry.2` choose fresh field versus enrichment field.
2. `common/scripted_effects/018_resources_found_prefire_effects.txt:39.entry.1` and `:39.entry.2` choose preferred versus ordinary state inside a fresh-field selection.
3. `common/scripted_effects/018_resources_found_prefire_effects.txt:76.entry.1` and `:76.entry.2` choose preferred versus ordinary state inside an enrichment selection.

The source constants are `new_field_base=60`, `enrichment_base=40`, `enrichment_investment_bonus=20`, `enrichment_transport_bonus=15`, `enrichment_survey_bonus=15`, `enrichment_international_bonus=10`, `evolution_i_bonus=15`, `evolution_ii_bonus=20`, `evolution_iii_bonus=25`, and preferred/ordinary bucket weights `70/30`.

Inspect sourceHash `7674b88a5e7f22ad34e643f889509a56d7a9db0c76654d084e49130e7e421861`, sourceRevision `0f558e6bd7712ed6477cfe53c44cf7425841f5d1dd3aec33315953c1124d55df`, candidates=6, `poolComplete=false`, requiredInputs=4, unresolved=1, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/79be91385ae9d6335c70cd75bc05e1f8be7ba2266762befe753dbc52d1b871a1/345f465cf82c6f7acc912a61145af586e52173e7b32c3c05e704af5dc0db88bf/probability-inspect-7674b88a5e7f.json`.

The exact six-entry evaluation used scenario set `E018_PREFIRE_RANDOM_LIST_CURRENT_2026_08_10` with `PREFIRE_EMPTY_BASELINE` state `{}` and `PREFIRE_ENRICHED_EVOLUTION_III` with declared preference/transport/survey/international/evolution flags. Analysis `probability-192e59eaaeb7a107e9597acc`, scenarioHash `f810c63a92c8098cec380f316e53d41fbb28836741c08c79dd4752050016a071`, candidates=12, unresolved=7, diagnostic `PROBABILITY_CANDIDATE_POOL_INCOMPLETE`, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ece32f4af84f6a68c60ed46de26b143d5b6d44c4c0b0670d0fda417889335dae/3897faebc25e579f51c245cfe662c49c16a9814f0d230fe77d3232ebab775cca/probability-192e59eaaeb7a107e9597acc.json`, ranking `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8aab1e9f970b44e1a853dd3614a3b0f215df5ecdd4a2d79631b90168758d3a1e/632090c715e286977ab7c175d0db79a451a00b5ebc3592a3d696aeef2f60e627/probability-probability-192e59eaaeb7a107e9597acc-ranking.svg`, matrix `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/17bb12570f442652708b4789acce8c0aa3ff8a9cc21f297412d99267e6f4359d/980bd6ad710644892f0a5e1fb3dd2dc565e8c22b23c034a72328d55aa22d5b28/probability-probability-192e59eaaeb7a107e9597acc-matrix.svg`, unresolved `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d9624ab0479b71cdfca8dc9c7daec53e60f9490255bd80d82f7353cc9b69d859/93e1df9087bc09571abc88929cbad1b41c608cdc5870f425d5962edc6a823cb2/probability-probability-192e59eaaeb7a107e9597acc-unresolved.svg`.

No fresh-vs-enrichment normalized probability is claimed from this run because the adapter withheld normalization when the source has nested state-selection entries and unresolved eligibility inputs. The authored base values remain 60/40 and the enrichment bonuses are source-visible tuning, not proved live odds.

### Cave brood random list

`common/scripted_effects/018_resources_found_cave_effects.txt:229` contains exactly five entries: `:229.entry.1` default war brood, `:229.entry.2` Stone brood, `:229.entry.3` Burrow brood, `:229.entry.4` Scree brood, and `:229.entry.5` Guard brood. Source constants are `default_brood=50`, `doctrine_brood=15`, and `guard_brood=5`. Doctrine entries are enabled only for their route flags; guard is enabled only after `cave_feeding_chamber_guards_unlocked`.

Inspect sourceHash `ae4058423879d8e98e81c4d19c0366b50b428a0259e9f9ecfa07d2d5a7396d9e`, sourceRevision `7a4a94a3e6ee67672c55df63d5058970b8e3cb7f97d75377084553ddc4dfb9c7`, candidates=5, `poolComplete=true`, requiredInputs=5, unresolved=0, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/93209066df8b2a60bb36ba046aaae97a4c5985f3ec854af9d64601652ef0df39/fa28f370804495e3a71f39b867c904fcdb048ba81ff7ef49f3448da7fb64b323/probability-inspect-ae4058423879.json`.

Evaluation scenario set `E018_CAVE_BROOD_RANDOM_CURRENT_2026_08_10` used `CAVE_DEFAULT_ONLY` state `{}`, `CAVE_STONE_GUARD_UNLOCKED` with Stone doctrine and guard flags, and `CAVE_BURROW_SCREE_UNLOCKED` with Burrow and Scree flags. Analysis `probability-29446e167665233c470f3d9a`, scenarioHash `ff2e8b470353679bbb1cbefe61234337146dade9caa4172f59f8c18e214dd125`, candidates=15, unresolved=5, diagnostics=0, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/737c83ee742aeffeb712305cf319b0c58d87186f632d68a5ae9c0d396db06887/065408bca137e00150ab523de14e54f5068cb790c41900fdbb8394a1ec474846/probability-29446e167665233c470f3d9a.json`, ranking `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/58d053326b126c4566b280360e0034d3c1576b8258d38e5f0d4af5fbf8026bed/4baadd7c4c4cdaf8749476eb84cf11a92b4dd7fb124fbcb4ce7944e733f48812/probability-probability-29446e167665233c470f3d9a-ranking.svg`, matrix `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d3dcbf657e0b2a6b153dc6dd654a8598b9923af35bbb2ac0e892e5e1d7074577/ee471409c7fce7c87aa65620a6b7122a90b9a937210142668edd4692f73ba77e/probability-probability-29446e167665233c470f3d9a-matrix.svg`, unresolved `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/505cfd88351fe68f23442e4f4113736e3e742560a1004e12fe8452f4de9373dd/cf72a0184ce7481ebb33b3d493341c6ecab32d33b3654052961a6631fc4a8c70/probability-probability-29446e167665233c470f3d9a-unresolved.svg`.

The complete five-entry manifest and zero inspect unresolved support the authored pool. Evaluation unresolved items are route-state typing limits, not a confirmed weighting error. In an eligible doctrine/guard fixture, the source intent is default 50 plus each unlocked doctrine 15 and guard 5; no exact normalized live distribution is claimed from this partial run.

### Six-way standard-resource roll and evolution deposits

`common/scripted_effects/018_resources_found_effects.txt:484-498` performs a uniform integer roll from 1 through 6 using `resources_found_resource.max_exclusive=7`, mapping to oil, aluminium, rubber, tungsten, steel, and chromium. The adapter's `direct_random` inspect on this source returned `PROBABILITY_SOURCE_DISCOVERED`, `discoveryReason=no_weighted_surfaces`, candidates=0, requiredInputs=0, sourceHash `0a90b52cea410ece4e2ce405bd73999c1c451b021a94bb8f6c5420b207e6e75e`, sourceRevision `d4c8413f7ad1ac6495585e812388f236c06cc3244cb98eb0fae46bc4af5e23da`, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/00a6d4ab3d529b2de1597c309ff987437ebf49a6c40048840570a2d396505c30/a42eef9e3963204ac1fc65053ccc5a79dcd749585423cd85e6e17479c97474f4/probability-inspect-0a90b52cea41.json`.

This adapter result means the six-way roll and all `set_temp_variable_to_random` amount/count rolls are not represented in MCP probability evidence. Source review found no weighted-list defect: the six resource types are selected by the documented 1..6 range, and duplicate eligibility is deliberate because each independent roll can select the same resource and stack it.

Current package surfaces are:

- Baseline: one independent 80..120 roll.
- Evolution I prefire: two to four independent 80..120 rolls.
- Evolution I active repeat: one to three independent 80..120 rolls.
- Evolution II prefire: three to five independent 90..140 rolls.
- Evolution II active repeat: one to three independent 90..140 rolls.
- Evolution III: one independent 120..200 roll for each of all six resource types, with duplicates impossible only because the resource type is explicitly assigned once per type.

These are direct random ranges and duplicate-eligibility semantics, not `random_list` pools. No exact distribution, expected amount, or balance claim is made because the direct-random adapter reports no surface.

## MTTH, mission, strategy, and structural adapters

`event_mean_time_to_happen` inspect on `events/018_random_resource.txt` returned `PROBABILITY_SOURCE_DISCOVERED`, `requested_adapter_empty`, suggested adapter `event_option_ai_chance`, sourceHash `6999853c6a9dfcefaa69fcfcb77f77e070b56a9eb7ca91cc6f936701a9681b7c`, candidates=0, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/acb0365269d59db813d9befeec959c0267c58076fc25db16488ddacd2746f163/19f41beda5ad755e3719adb2af71d31ccf18caf9a5891c771dd8c82e008e52e3/probability-inspect-6999853c6a9d.json`. A second inspect on `common/scripted_effects/018_resources_found_decision_effects.txt` returned `no_weighted_surfaces`, sourceHash `23f692fa4e2bbb4c7114bdf3d9115134d554ad083c45c07e37e331600ea7eaba`, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4259f60f47532c671a37230bbc1c3bfcca8707a011d8fea6fc40e3151b3256e6/79a6b5c614b5377764af8971d36a5891d6c3723a4e3257d971fb0cd053276a5f/probability-inspect-23f692fa4e2b.json`. Event 018 has no direct event MTTH block; scripted MTTH variables and rescheduler effects are outside this adapter.

`mission_ai_will_do` inspect on `common/decisions/018_resources_found_decisions.txt` returned `requested_adapter_empty`, suggested adapter `decision_ai_will_do`, candidates=0, sourceHash `dd2e5ef3aa158a6a1f175f17cee63246dc3692e2b50016059a3cc72213b9361f`, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a2aa2f250e98c1281500b94c4883febff939585b858edfe64003b6dd2140bf5a/7f55265c08e4621191511ff4b68fce9647a3b95d869aa2db78d4340106fd1db8/probability-inspect-dd2e5ef3aa15.json`. Event 018 mission applicability is present in source but not analyzable as a mission score by the installed adapter.

`ai_strategy_factor` inspect on `common/ai_strategy/018_resources_found_ai_strategy.txt` returned `no_weighted_surfaces`, candidates=0, sourceHash `d65af6c3961b9581ba6ff0d59eb953c1c36f4c7c46fcc8ad405969274897a6ba`, sourceRevision `911cb6f2a4c5fa5dc20e004d276615e7d6c00dae2bb1fe1998010c1f75020b0b`, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/04f8bdf5f919c5f95bd15cc281f3a5acf36c0b49708a28f01c793f4425f23760/86d9e21015be86aeb249c0bbaf7664ec22eeb6f8cdd3aebe66b393babf6a7b32/probability-inspect-d65af6c3961b.json`. The source contains fixed strategy blocks and factors, but no adapter-backed candidate pool or factor race was available.

Fresh structural MCP evidence: `hoi4.event_inspect` scan returned `EVENT_INSPECTED_PARTIAL` at revision `53a767c5012bf86517e556e90f78047efea681342277a5d2813f07ffef0c5f15`, graphHash `cf99bd44a1d512f1e2dae932df4620b38cc19524bac01092fe94a54ca70231a9`, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d969ad2260b877584dca240a1a41eaf5e08cf1a42b30467bc19e6db5c4d64f93/dfc3d6d5e1c091dcda5de94e7856b3aaa756bf4e8668e75ea555853524bd8e14/event-scan-53a767c5012b.json`. It is a workspace-wide partial projection with no blocking diagnostics, not a focused Event 018 lifecycle proof.

Fresh `hoi4.focus_inspect` returned `FOCUS_INSPECTED`, tree `018_resources_found_cave_focus_tree`, focusCount=67, layoutHash `776a29503fc0a2697f7421e085d3174fbe6fab691b7ac3966e6dd994fe8c3bdd`, tree-local diagnosticCount=0, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/71a8559fa59e3fca61062702590cd92491d90089ba8801ddfa7954029e8ee225/31b1808b6b27ec520b03fc11f6d271bd1a2014cff4fac85aabeb56ac141c3d52/focus-inspect.f15049544f64a86b.json`. `hoi4.focus_render` returned `FOCUS_RENDERED`, SVG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1bbe413dc31ffc8000592b4d838f820e76b0f98253601d7bc68473317ef6a7a7/d17c0d2f5095ce5a7c6b584e33538b060472ae6258eb65fec45c51aad779b4d0/018_resources_found_cave_focus_tree.focus.svg`, JSON `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/412491dfc68147653a6373f7a2c7d4400b007b05e8e219992bf32fceea320ec4/acc5122187deb00fef0fb28426cd495b23f6d9380a2340096230b522147b9b5d/018_resources_found_cave_focus_tree.focus.json`. The renderer also reports 14 unrelated global missing continuous-focus icons; none belongs to the Event 018 tree, whose own diagnosticCount is zero.

## Findings and closure gate

- No authored complete bounded pool produced a confirmed positive-weight impossible candidate, dominance defect, starvation defect, rank reversal, unsafe repetition, or exploit loop.
- Focus pools are complete manifests but score evaluations are partial because route, cave, adaptation, continental, and terminal predicates are not fully typed in the supplied fixtures.
- The selected-field decision pool is complete at 29 candidates and confirms the AI presentation-page bypass, but its score evaluation remains partial and is not a normalized click probability.
- The cave brood pool is complete at inspection and its source constants are internally coherent; evaluation remains route-state bounded.
- Prefire fresh/enrichment and nested state-bucket random lists are discovered but not normalizable with current dynamic inputs.
- The event-wide 204-option pool is explicitly incomplete; only `.1` received a fresh exact-pool evaluation in this turn. All event IDs/options were enumerated statically, but that enumeration is not a substitute for MCP evaluation of every typed event family.
- Six-way resource selection, evolution count/amount rolls, scripted MTTH timing, mission applicability, and fixed AI strategy factors have no usable adapter surfaces. These are irreducible adapter-only limitations for this audit.

Therefore the no-unresolved-AI-evidence gate remains **OPEN**. It may close only after the adapter can type the remaining event/focus/decision predicates and represent direct random, scripted MTTH, mission, and strategy surfaces, or after an approved engine-backed evidence route is supplied. No gameplay patch is recommended from this audit; any future tuning change requires a same-scenario baseline/compare pass.

## Simplifications, omissions, and blockers

No source simplification or fallback was applied. The remaining omissions are evidence-side: no per-ID MCP evaluation for every event option family, no direct-random adapter representation, no direct event MTTH block, no mission score adapter, no AI-strategy-factor adapter, and no typed campaign fixtures for complete normalized focus/decision/random evaluation. These omissions are explicitly not converted into source defects or balance claims.
