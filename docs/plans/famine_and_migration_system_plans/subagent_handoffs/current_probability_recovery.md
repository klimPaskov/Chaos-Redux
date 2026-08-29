# Current probability recovery audit: famine and migration

Date: 2026-08-25

Scope: read-only recovery audit of the separate famine and migration systems. No gameplay, AI, event, decision, mission, trigger, effect, constant, localisation, or documentation source outside this handoff was edited. No famine or migration incident events were found or introduced; the specifications require that no such incident event layer exist.

## Completion verdict

The recovery audit is incomplete and remains unresolved for balance certification. The current decision source pools are discoverable when the complete ten- and eighteen-entry candidate lists are supplied, but the installed adapter exposes no available candidates and cannot resolve the required runtime scopes and triggers. The adapter reports score-only semantics, not normalized selection probabilities. The three dynamic custom pools remain incomplete at the adapter boundary: destination selection reports zero candidates with five unresolved entries, opposition reports zero candidates with seven unresolved entries, and relief-donor selection reports zero candidates with three unresolved entries after the explicit manifest probe.

The rendered rankings and matrices show `0.00000` or a `0.000–1.000e-12` sensitivity axis because unresolved gates collapse the analyzable rows. Those values are not proof of zero eligibility, starvation, dominance, or a zero click probability. No exact selection probability, timing distribution, rank ordering, repetition rate, or balance claim is certified.

## Required references read

The audit followed `AGENTS.md`, `.agents/skills/chaos-redux-subagents/SKILL.md`, `.agents/skills/chaos-redux-decisions-missions/SKILL.md`, `.agents/skills/chaos-redux-event-planning/SKILL.md`, and `.agents/skills/chaos-redux-mtth/SKILL.md`.

The binding specification and plan material read were `docs/specs/famine_and_migration_system_specs/README.md`, `docs/specs/famine_and_migration_system_specs/famine_and_migration_system_implementation_surface_map.md`, `docs/specs/famine_and_migration_system_specs/famine_and_migration_system_probability_scenarios.csv`, `docs/plans/famine_and_migration_system_plans/ai_probability_current.md`, and `docs/plans/famine_and_migration_system_plans/completion_report.md`.

The offline Paradox wiki reference set consulted was `Data structures`, `Triggers`, `Effects`, `Modifiers`, `Localisation`, `Scopes`, `On actions`, `Event modding`, `Decision modding`, `Idea modding`, and `AI modding` under `paradox_wiki/`. The relevant vanilla documentation reference set was under `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/`, including `triggers_documentation.md`, `effects_documentation.md`, `script_concept_documentation.md`, `modifiers_documentation.md`, and `dynamic_variables_documentation.md`.

## Audited source surfaces

Decision AI surfaces:

- `common/decisions/famine_decisions.txt`: `famine_release_reserves`, `famine_emergency_imports`, `famine_repair_relief_route`, `famine_escorted_relief_convoy`, `famine_emergency_airlift`, `famine_invite_relief`, `famine_evacuation`, `famine_requisition_safer_state`, `famine_conceal_crisis`, and `famine_maintain_extraction`. Their `ai_will_do` blocks begin at source lines 223, 372, 493, 597, 759, 889, 988, 1215, 1334, and 1398.
- `common/decisions/migration_decisions.txt`: `migration_prepare_evacuation`, `migration_open_departure_routes`, `migration_restrict_departure`, `migration_close_border`, `migration_evacuate_vulnerable`, `migration_evacuate_workers`, `migration_negotiate_corridor`, `migration_accept_corridor_offer`, `migration_reject_corridor_offer`, `migration_open_reception`, `migration_controlled_medical_reception`, `migration_distribute_arrivals`, `migration_transit_only`, `migration_enforce_closure`, `migration_local_integration`, `migration_third_country_resettlement`, `migration_voluntary_return`, and `migration_forced_repatriation`. Their `ai_will_do` blocks begin at source lines 517, 573, 623, 689, 758, 955, 1161, 1199, 1221, 1308, 1394, 1528, 1714, 1828, 1972, 2125, 2231, and 2443.

Dynamic weighted pools:

- Famine relief donor pool: `common/scripted_effects/famine_relief_effects.txt`, especially `famine_relief_donor_candidate_weight` at line 112, `famine_relief_select_donor` at line 250, and `famine_relief_select_and_create_contract` at line 367, with gates in `common/scripted_triggers/famine_relief_triggers.txt` and constants in `common/script_constants/famine_relief_constants.txt`.
- Migration destination pool: `common/scripted_effects/migration_destination_selection_effects.txt`, the matching gates in `common/scripted_triggers/migration_destination_selection_triggers.txt`, and `common/script_constants/migration_destination_selection_constants.txt`. The declared selection entry points supplied to MCP were `migration_select_general_safe_evacuation_destination`, `migration_select_internal_safe_route_destination`, `migration_select_foreign_transit_destination`, `migration_select_third_country_resettlement_destination`, and `migration_select_safe_food_reserve_donor`.
- Famine opposition pool: `common/scripted_effects/famine_opposition_effects.txt`, `common/scripted_triggers/famine_opposition_triggers.txt`, and `common/script_constants/famine_opposition_constants.txt`. The complete declared channel manifest supplied to MCP was `famine_opposition_party_democratic`, `famine_opposition_party_communism`, `famine_opposition_party_fascism`, `famine_opposition_party_neutrality`, `famine_opposition_local_resistance`, `famine_opposition_national_autonomy`, and `famine_opposition_project_movement`.
- Humanitarian corridor response is wired through `common/decisions/migration_decisions.txt`, `common/scripted_effects/humanitarian_corridor_effects.txt`, `common/scripted_triggers/humanitarian_corridor_triggers.txt`, and `common/script_constants/humanitarian_corridor_constants.txt`. The accept/reject decision entries were included in the migration AI pool and are separately noted below because their corridor factors were not active in any supplied fixture.

No famine/migration event file or incident event identifier was audited because the source/specification boundary explicitly excludes that layer.

## Current source provenance and inspect evidence

All current decision evaluations and sweeps below report MCP source revision `ed226da4d1fc71a16cd31365b853d1d249e44cd05c68be4f99932b326404b110`.

| Surface | Adapter and pool | Current source hash | Inspect result and artifact |
| --- | --- | --- | --- |
| Famine decisions | `mission_ai_will_do`, complete 10-ID pool | `c271593ac497ddf01b152db36959768afdbd54d0271cc47095fcff1c572fe6dc` | `PROBABILITY_SOURCE_INSPECTED`; `poolComplete=true`, `candidates=10`, `availableCandidates=0`, `requiredInputs=6`, `unresolved=0`. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7c25954e5f37bc9aa1866a5817598344e98c9ac0722d8d26067696009bb1e3d6/3e9649e49dd13a80170a529fb8396634a3841de9020bd178c065e2ff0f9dff74/probability-inspect-c271593ac497.json` |
| Migration decisions | `mission_ai_will_do`, complete 18-ID pool | `df2d56d23fcc32905584e0bfe6ff8ac800cd7eb044d73d58b78867746ef36104` | `PROBABILITY_SOURCE_INSPECTED`; `poolComplete=true`, `candidates=18`, `availableCandidates=0`, `requiredInputs=11`, `unresolved=0`. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6d9214ef5521ff205ac11cbb7c9d3b0a4dc69ea722622c5409d660e0194e44d4/771c9ceab0569f1ffdfdd15a592f88539cbfc55e342d834f074928b3143be32e/probability-inspect-df2d56d23fcc.json` |
| Migration decision adapter probe | requested `decision_ai_will_do` | `df2d56d23fcc32905584e0bfe6ff8ac800cd7eb044d73d58b78867746ef36104` | `PROBABILITY_SOURCE_DISCOVERED`; requested adapter was empty, suggested adapter was `mission_ai_will_do`, with `availableCandidates=18`, `identifierMatches=18`, and `candidatePoolMatches=18`. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d6db89ec29358ac9ab80581b963124737bacdb19aa6d15a25ad7ce029658274b/b0e8b9044d87fcf23e9b9a0ca9da68e9faaf6d91a8b5ed57c66c7d8e5c6f5a85/probability-inspect-df2d56d23fcc.json` |
| Destination custom pool | `custom_weighted_pool`, five-entry manifest | `454c73ffc47b4d76a69d5c8298ea2d19623b23a982a685a69d3831ebbfb8c374` | Source revision `7978ccf8f71024f0112b313b3361fe33362746bb8da845b087f784b28cc8de76`; `poolComplete=false`, `candidates=0`, `availableCandidates=0`, `requiredInputs=0`, `unresolved=5`. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c18e01a78991b1420f5a869b0c02892e2185bf9e31c33df9e4be3ca80bd96383/8c92cfe74cb72f6a633f0d28768d46f7bed1e418b31d278f7ac96befc79b11ac/probability-inspect-454c73ffc47b.json` |
| Opposition custom pool | `custom_weighted_pool`, seven-channel manifest | `4040a2f554f24521026236dad3316f209169a510b184103f4b81b1b437f1f22e` | Source revision `7978ccf8f71024f0112b313b3361fe33362746bb8da845b087f784b28cc8de76`; `poolComplete=false`, `candidates=0`, `availableCandidates=0`, `requiredInputs=0`, `unresolved=7`. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2ef55164e8eb5740fd931ba518c5d38d8fb3d00ef09fa27c62763279ce681f4a/db028bda80253d039ae5977d01e273004ad6fee0f89922044fde069d622b07e9/probability-inspect-4040a2f554f2.json` |
| Relief donor custom pool, source discovery | `custom_weighted_pool`, source only | `3fb98f4792277e87b5f58a05644b083b0795a912fb577ed49847f7b4fadabfb8` | Source revision `ed226da4d1fc71a16cd31365b853d1d249e44cd05c68be4f99932b326404b110`; `poolComplete=false`, `candidates=0`, `availableCandidates=0`, `requiredInputs=0`, `unresolved=0`. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/13b128273e665a555583c6f937b0ccc3c02048e030ca3736c190505595c461c7/8e2f58795eae515349633e6a3db693d0a39feb297fc705610dfdb53f888e7eab/probability-inspect-3fb98f479227.json` |
| Relief donor custom pool, explicit three-token manifest | `custom_weighted_pool`, three-token manifest | `3fb98f4792277e87b5f58a05644b083b0795a912fb577ed49847f7b4fadabfb8` | Same source revision; `poolComplete=false`, `candidates=0`, `availableCandidates=0`, `requiredInputs=0`, `unresolved=3`. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a77d4a6f6ffc600f73f4cbb607c92c4bf7fe51e310f732de776d605e5fe885cf/30ab15c3270db7b3475c00c477f1771ae8523ba5a445604d8319e0be6c330abb/probability-inspect-3fb98f479227.json` |

The decision adapter capability reported in the current inspect resources is `rawScore=true`, `normalizedProbability=false`, `timeDistribution=false`, `selectionRule=score_only`. The source-level complete pool flag does not make the runtime candidate set complete and does not convert willingness scores into click probabilities.

## Named scenario analyses

### Famine decision AI

The matrix evaluation used scenario set `current_famine_probability_matrix` with `prob_famine_relief_dense`, `prob_famine_relief_blocked_island`, and `prob_soviet_extraction`, the complete ten-entry famine pool, flat scenario state fields, and no seed because this is a score evaluation rather than a simulation.

MCP returned `PROBABILITY_ANALYZED_PARTIAL`, analysis id `probability-03bd691e2fc0a70e7f3bf9b8`, source hash `c271593ac497ddf01b152db36959768afdbd54d0271cc47095fcff1c572fe6dc`, source revision `ed226da4d1fc71a16cd31365b853d1d249e44cd05c68be4f99932b326404b110`, scenario hash `960f7fc09e6172e804a350b9855a8d4453db6b3b3044fdb8f46d0ef420970e8b`, three scenarios, thirty candidate rows, twenty-three unresolved items, zero diagnostics, and six visual resources. Classification: score-only, partial, unresolved external state; not exact or bounded selection probability.

The rendered JSON, ranking, matrix, and unresolved evidence are:

- JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b1eb0394dd76eb9954593e89614346361ff3768d2c829c8c80591a81282bb4c8/4c88c27dd6ceb44e51255c135afd134311233a806741c7395275335d309dfd78/probability-03bd691e2fc0a70e7f3bf9b8.json`.
- Ranking SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/19e497adfbd04b4471b4b434042887a1603205c31f12bd17888716b113387c6c/f8307222396af48a97b46310400d714a1daa6496bb2fafa659a254699705875c/probability-probability-03bd691e2fc0a70e7f3bf9b8-ranking.svg`.
- Matrix SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/36e09f4edf3c5326dd2591e6e89896f8943ed60993451c2f0bf33c04e8b0619a/6b1bb501c5a25bccee6e8133f2220b409c9047c8dab2a8ec143e8564cc3fb76a/probability-probability-03bd691e2fc0a70e7f3bf9b8-matrix.svg`.
- Unresolved SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/32a3e106ece0ceb2b209022b68987069b40a0ceea96f873928c77b4603a69186/25f3f6ebc9e6f76a9031b90d4a9c04c44936e50d3290db20929aeb8000be5431/probability-probability-03bd691e2fc0a70e7f3bf9b8-unresolved.svg`.

The ranking and matrix render every candidate at `0.00000`. The unresolved view identifies missing `FROM`, `has_government`, `custom_trigger_tooltip`, `has_equipment`, `has_air_experience`, and `has_war` declarations among the twenty-three unresolved rows. Therefore the expected relief ordering, blocked-island ordering, and early Soviet extraction ordering remain unresolved rather than disproven.

A one-scenario flat-state probe for `prob_famine_relief_dense` used scenario set `current_famine_flat_state_probe`, scenario hash `c27c9c03a27084a917a26b08dbe11f97d1d4fd78990ef2473196199928ecb3b9`, analysis id `probability-597fd2bd02e2649c58058f05`, and returned the same score-only partial shape with ten candidates and twenty-three unresolved rows. This probe established that flat primitive state fields are accepted, but it does not establish typed scope binding.

### Migration and corridor decision AI

The matrix evaluation used scenario set `current_migration_probability_matrix` with the eleven named ids `prob_humanitarian_border`, `prob_capacity_exhausted_border`, `prob_outbreak_reception`, `prob_nuclear_evacuation`, `prob_genocide_escape`, `prob_authoritarian_pushback`, `prob_corridor_acceptance`, `prob_forced_return`, `prob_integration`, `prob_disaster_flight`, and `prob_bombing_exodus`, the complete eighteen-entry migration pool, flat state fields, and no seed.

MCP returned `PROBABILITY_ANALYZED_PARTIAL`, analysis id `probability-7e26d24f734ca77b97891362`, source hash `df2d56d23fcc32905584e0bfe6ff8ac800cd7eb044d73d58b78867746ef36104`, source revision `ed226da4d1fc71a16cd31365b853d1d249e44cd05c68be4f99932b326404b110`, scenario hash `a513d993b2f7c562d6b237682df3e0679926b8dbe6ffcf39cf35ee646b800b91`, eleven scenarios, 198 candidate rows, 77 unresolved items, six diagnostics, and six visual resources. Classification: score-only, partial, unresolved external state; not exact or bounded selection probability.

The rendered JSON, ranking, matrix, and unresolved evidence are:

- JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a8eb73e14414bbd54f77887c462edcd3205ee4937bc38603aa78e7b5f51667ab/702292e3e6693b6c68f63b165ac271aa75f529dfc954ee7f00ba8a36aef08152/probability-7e26d24f734ca77b97891362.json`.
- Ranking SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/004b092e621311f1910bc868758386cea889817caa45717d9254d6d82cbd4bc0/90e51ea33e48612d2a8d560a805f702473ea3c943091b7a7fa99e060eda8c0a5/probability-probability-7e26d24f734ca77b97891362-ranking.svg`.
- Matrix SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9d2db4705985d32d39fc01680e9d33348630aa8898118e82f7694475d62ef5d8/fe5a653f20928939b5346dc351444899915c401566be5c7eb1a036b5acb5a91d/probability-probability-7e26d24f734ca77b97891362-matrix.svg`.
- Unresolved SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c42731ecbed27ed526a3acc4866ea177183e35315f4aa5c46e6a75429d63d1c0/d3532b7ca0637b2d117bf1876e67cf08176ab6b0a8183a63d96085125d24b8f5/probability-probability-7e26d24f734ca77b97891362-unresolved.svg`.

The ranking and matrix render every candidate at `0.00000`. The unresolved view includes `hidden_trigger`, `FROM`, `has_variable`, `has_government`, `has_war`, `has_equipment`, `any_owned_state`, `num_of_civilian_factories`, `migration_reception_policy`, `migration_active_mission_count`, `migration_reception_load`, `migration_departure_policy`, and `var:humanitarian_corridor_offer_requester_country_id`. The corridor accept/reject paths are consequently not proven to rank in `prob_corridor_acceptance`.

The six MCP diagnostics were explicit: `migration_accept_corridor_offer` factor `constant:humanitarian_corridor_ai.accept_humanitarian_factor`, `migration_controlled_medical_reception` factor `constant:migration_decision_ai.controlled_medical_reception_factor_1`, `migration_open_departure_routes` factor `constant:migration_decision_ai.open_departure_factor_2`, `migration_open_reception` factor `constant:migration_decision_ai.open_reception_factor_1`, `migration_reject_corridor_offer` factor `constant:humanitarian_corridor_ai.reject_humanitarian_factor`, and `migration_voluntary_return` factor `constant:migration_decision_ai.voluntary_return_factor_3` were not active in any of the eleven supplied scenarios.

`prob_disaster_flight` and `prob_bombing_exodus` were included to preserve the exact matrix ids, but their source surface is deterministic movement pressure rather than a categorical `ai_will_do` selection pool. Their zero matrix cells therefore cannot be interpreted as movement probabilities.

## Threshold and sensitivity sweeps

The first famine sweep attempt used `current_famine_threshold_sweep` with paths `famine_severity`, `famine_reserves`, `mortality`, `visibility`, `republic_pressure`, and `war_need`. MCP returned the exact error `PROBABILITY_SWEEP_RANGE_REQUIRED` with blocker details `scenarioId=prob_famine_relief_dense`, `path=famine_reserves`, and message `Every sweep path requires a scenario range, numeric alternatives, or numeric state value`. No artifact or threshold conclusion came from that attempt.

A corrected numeric-variable probe used `current_famine_numeric_threshold_probe`, paths `famine_food_pressure`, `famine_food_reserve_amount`, `famine_profile_extraction`, and `famine_profile_concealment`, three steps, pairwise comparison, and rank-reversal search. MCP returned `PROBABILITY_ANALYZED_PARTIAL`, analysis id `probability-fe53babd001dd439fcf8af57`, source hash `c271593ac497ddf01b152db36959768afdbd54d0271cc47095fcff1c572fe6dc`, source revision `ed226da4d1fc71a16cd31365b853d1d249e44cd05c68be4f99932b326404b110`, scenario hash `07b639bf238d786de58516c508f8ab8381eb34b3918d614c6fa0a0682c05fdee`, three scenarios, thirty candidate rows, eighteen unresolved rows, two diagnostics, and eighteen sweep points. Rendered evidence:

- JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ff89a9b47a658a060069555895d961c2c1e2ae6ce2c67b06c95fa3c9508cb73a/23c402d33c0fa2953ae3a87ac53321c91246233c85bad1f61dc98bb3016ebfa2/probability-fe53babd001dd439fcf8af57.json`.
- Sensitivity SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9b6ecda9a92d2ee223aa6fa53c8862a9733f8b713af95fa4e1a159624609abf0/b34536285011f1450366cf58866c743c0998f5183297650f1ecabfa9a7e1ed72/probability-probability-fe53babd001dd439fcf8af57-sensitivity.svg`.
- Threshold SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a6d32ffc270e06218fbe6e53b5f3d111d3f383d152a2e17fa057722f7cf35cc8/865ea5fb9dbacf6da5b341f379a3dd57deb4c6296e9331de1320a52dbc295cd5/probability-probability-fe53babd001dd439fcf8af57-threshold.svg`.
- Unresolved SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1a4babde35c2c5997218beb133a2ab6f5c58b4e25a3c3a83c4dbe8eae1944e90/68bedf2487f28619ac7f66d785de4dd0c0127da3bc39153c3a196fa9525c3845/probability-probability-fe53babd001dd439fcf8af57-unresolved.svg`.

The sensitivity render reports a `0.000–1.000e-12` y-axis, and the threshold render reports `0 rank reversals and 0 threshold observations`. Because the rows remain unresolved and effectively zero, this is an unresolved partial sweep, not evidence that no rank reversal exists.

The migration sweep used `current_migration_capacity_threshold_probe`, paths `migration_reception_load`, `migration_reception_policy`, `capacity`, and `aid`, three steps, pairwise comparison, and rank-reversal search. MCP returned `PROBABILITY_ANALYZED_PARTIAL`, analysis id `probability-e2a872459b26e27014c8a478`, source hash `df2d56d23fcc32905584e0bfe6ff8ac800cd7eb044d73d58b78867746ef36104`, source revision `ed226da4d1fc71a16cd31365b853d1d249e44cd05c68be4f99932b326404b110`, scenario hash `92208d51b584d831136baefb89ae3d9afac45ea89e42d807ade28788e4d936d1`, one scenario, eighteen candidate rows, 77 unresolved rows, six diagnostics, and six sweep points. Rendered evidence:

- JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e4b71e84bb1eb098fc39e156a2f0ff597f2ee49247d50701061cb4965147e3d9/5fb8950ff1071802e9976d1e3f50729fa6ff0d88689f413c5d44d615b9845bfe/probability-e2a872459b26e27014c8a478.json`.
- Sensitivity SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7f3625a1b12f223ccaa653c08f6f5046f9009b53ba816bac69fe063b078def08/313ff227b2ad46564a1f309fceca35aa70f15be307dbed3ee252cfd2bbf6ec86/probability-probability-e2a872459b26e27014c8a478-sensitivity.svg`.
- Threshold SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a6d32ffc270e06218fbe6e53b5f3d111d3f383d152a2e17fa057722f7cf35cc8/0c4f69c106f9ed0a026894baaf39817a8fd2afc8e95a106eb4b1d4c240329234/probability-probability-e2a872459b26e27014c8a478-threshold.svg`.
- Unresolved SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c42731ecbed27ed526a3acc4866ea177183e35315f4aa5c46e6a75429d63d1c0/96368bf9f24e563f507e90a93dbcb34b952bb43f8c7f24b27bfb166f3f4080e7/probability-probability-e2a872459b26e27014c8a478-unresolved.svg`.

This sensitivity render also has a `0.000–1.000e-12` y-axis and zero reported reversals/observations while 77 trigger/variable rows remain unresolved. No migration capacity or aid threshold is certified.

## Typed-scope and adapter errors

The first scenario schema probe returned this exact validation error: `MCP error -32602: Input validation error: Invalid input: expected string, received undefined at scenarioSet.id; Invalid input: expected record, received undefined at scenarioSet.scenarios[0].state; Invalid input: expected array, received object at scenarioSet.scenarios[0].flags; Unrecognized keys: "setup", "scopes", "variables", "externalFactors", "seed", "cadence", "terminalState" at scenarioSet.scenarios[0]`.

The typed nested-scope probe then returned: `MCP error -32602: Input validation error: Invalid input at scenarioSet.scenarios[0].state.scopes; Invalid input at scenarioSet.scenarios[0].state.variables; Invalid input at scenarioSet.scenarios[0].state.externalFactors`. Flat primitive state fields are accepted, but typed nested scopes and nested variable/external-factor records are not accepted by the current scenario schema. This is the reason the evaluations cannot bind `FROM`, requester/destination states, government, war, equipment, and compound triggers.

The requested `decision_ai_will_do` inspection for famine returned an exact MCP result with `artifactCount=0`, `code=INTERNAL_ERROR`, `status=error`, and blocker `INTERNAL_ERROR: Unexpected internal error`. The migration request did not fail silently: it returned `PROBABILITY_SOURCE_DISCOVERED`, `requestedAdapter=decision_ai_will_do`, `suggestedAdapter=mission_ai_will_do`, and eighteen matching candidates. All current decision evidence above therefore uses the suggested `mission_ai_will_do` adapter and is explicitly labelled score-only.

## Validity, ranking, and risk findings

- Candidate-pool completeness: complete only at the declared source-level decision-list boundary (`10/10` famine and `18/18` migration). Runtime eligibility is not complete because the adapter reports zero available candidates and unresolved trigger inputs.
- Custom-pool completeness: incomplete for destination (`0` candidates, `5` unresolved), opposition (`0`, `7`), and relief donor (`0`, `3` on the explicit token probe). No custom pool can be normalized or sampled from this evidence.
- Base values and modifier traces: rendered decision rows are `0.00000` under unresolved state. The migration diagnostics identify six factors inactive across all eleven fixtures; the famine numeric sweep identifies inactive `famine_decision_ai.escorted_relief_convoy_factor_2` and `famine_decision_ai.repair_relief_route_factor_2`. These are analyzer diagnostics, not balance targets.
- Willingness versus probability: every decision `ai_will_do` result is a willingness score. The MCP adapter explicitly reports `normalizedProbability=false`; no value in this handoff is a click probability.
- Dominance and starvation: unresolved. Zero rendered rows cannot distinguish invalid candidates from unresolved triggers, and the custom candidate pools are absent at runtime.
- Rank reversal: unresolved. The two threshold renders report zero observations only because no resolved score variation was available.
- Repetition, timing drift, cooldown, recovery, cap, reset, removal, and terminal-state safety: unresolved. The decision adapter has no time distribution, and no complete custom-pool cadence/state-transition manifest was available.
- Invalid/dead/hidden targets and exploit risk: unresolved by MCP. Source helpers appear to intend strict gates and fail-closed total-weight handling, but source-only inspection is not accepted as engine proof under this audit contract.

## Comparison status

No owner-applied source patch occurred during this read-only audit, so there is no valid current before/after source pair. The recorded baseline in `ai_probability_current.md` consists of incomplete inspection artifacts from earlier source revisions and does not provide a comparable before source object, complete candidate pool, or comparison id. `hoi4.probability_compare` was therefore not run; the exact comparison blocker is `no usable before/after source revision pair or owner-applied patch`, not a balance conclusion. A current-vs-current comparison would not be a before/after audit.

For traceability, the plan records older incomplete inspection hashes and artifacts: famine old hash `d9f1ea3470dc...` with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/699620.../85ea5c.../probability-inspect-d9f1ea3470dc.json`, migration old hash `d7e79ad53855...` with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b5549e.../b726d.../probability-inspect-d7e79ad53855.json`, and historical custom hashes `454c73ffc47b...` and `4040a2f554f...`. Those records remain incomplete and are not comparison evidence.

## Skipped analyses and blockers

- No callable `chaosx_ai_probability_auditor` route is exposed in this runtime. The direct HOI4 MCP routes were used instead, and this handoff preserves their artifacts and errors.
- Custom-pool evaluation was not completed after the parent stopped further MCP calls. The combined destination/opposition/donor evaluation request was aborted before any result was returned, so it has no artifact, scenario hash, or conclusion.
- `hoi4.probability_simulate` was not run. The matrix mentions convoy and donor uncertainty, but no explicit input distributions, correlations, approved seeds, or complete candidate pools were declared.
- `hoi4.probability_sequence` was not run. No complete custom-pool manifest declared cadence, recovery, cooldown, cap, removal, reset, timers, and terminal states.
- No event inspect/render route was run because the separate famine/migration systems contain no incident event chain and the specifications explicitly prohibit adding one.
- No live HOI4 launch or gameplay validation was performed.

## Recommended next fixes, without applying them

1. Add an analyzer-compatible typed scenario contract for the decision sources, including `FROM`/requester/destination scopes and the unresolved government, war, equipment, air-experience, `hidden_trigger`, `custom_trigger_tooltip`, `any_owned_state`, `num_of_civilian_factories`, `has_variable`, and numeric migration variable inputs observed in `common/decisions/famine_decisions.txt` and `common/decisions/migration_decisions.txt`.
2. Publish a complete manifest for the dynamic destination pool in `common/scripted_effects/migration_destination_selection_effects.txt` and `common/scripted_triggers/migration_destination_selection_triggers.txt`, listing every runtime candidate state, validity gate, route geometry, history exclusion, capacity/load modifier, total-weight accumulator, and zero-total behavior.
3. Publish the seven-channel runtime manifest for `common/scripted_effects/famine_opposition_effects.txt` and `common/scripted_triggers/famine_opposition_triggers.txt`, including absent-ideology zeroing, local resistance/autonomy gates, visible blame, and terminal selection state.
4. Publish the registered donor-state manifest for `common/scripted_effects/famine_relief_effects.txt` and `common/scripted_triggers/famine_relief_triggers.txt`, including route modes, donor stock/headroom ranges, relation modifiers, persecution/war-corridor overrides, protected/famine-state exclusions, and selection cadence.
5. After fixtures and manifests exist, rerun the same named scenario ids and complete candidate pools, then rerun the numeric sweeps with declared ranges and retain the unresolved renders until every required input is resolved. Do not convert the scores to click probabilities.
6. After any owner-applied weight, gate, pool, or tuning change, run a same-scenario `hoi4.probability_compare` against a valid before artifact and preserve its comparison id. Keep the famine and migration namespaces separate and do not add incident events.

## Final handoff state

Completed: mandatory current `probability_inspect` pass for famine decisions, migration decisions, destination pool, opposition pool, and relief donor pool; named decision scenario evaluations; numeric famine and migration sweeps; rendered ranking/matrix/sensitivity/threshold/unresolved evidence; source hashes, source revisions, scenario hashes, candidate manifests, exact adapter/schema errors, and uncertainty classification.

Blocked: exact engine eligibility, normalized probability, timing, custom-pool ranking, donor/destination/opposition selection, comparison, and balance certification.

Uncertainty: all unresolved items and adapter limitations listed above remain active. No weight target or gameplay patch was chosen or applied.
