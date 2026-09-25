# Event 016 Mengele Teleportation AI Audit

Status: final-source post-patch audit, read-only. The owner applied the AI patch. This audit changed only this handoff; it did not edit gameplay, stage, or commit files.

## Scope and sources

- Weighted surface: four private stage decision wrappers in `common/decisions/016_mengele_teleportation_stage_decisions.txt`.
- Trigger source: `common/scripted_triggers/016_mengele_teleportation_stage_decision_triggers.txt`.
- Shared constants: `common/script_constants/016_brilliant_scientist_project_constants.txt`.
- Precedent reviewed: Kruger Teleportation stage decisions in `common/decisions/016_brilliant_scientist_directorate_project_board.txt`.
- Final decision source local SHA-256: `0D992F3D5BBB0A58D414090F12AF6D8C15A8A9C34E3A0905A528FED4974C0989`; final MCP source hash: `d44cf48710407a5ec8d768b22d9a52ddbc320692758770a0b9b26a4b20e7eeb2`; source revision: `a310d945c4e1c03cadc01ae6b897e0be33a3818183eed2fff69a3a9a3133497e`.
- Final trigger source local SHA-256: `73703DC378DE6F1BF9735CAEF49E97B6362C6674C2F855ADDCE591266B45ECBD`; constants local SHA-256: `A95301ED9CBC7BB8FCB751885165F62AE5AA8C6B315EADB0C5CDAF79350CE131`.
- The captured pre-patch decision source was untracked and had no retained immutable source path: local SHA-256 `C8E418A0B7D40EC771EAE3440ED36C348C266DD3B5FA5A81683DA8AF55A2FDB8`, MCP source hash `559b8ed88ba042b518e4d0096c1d4cfd11f2f05b25e13a19801ba57680fc6a4b`, baseline evaluation revision `ef3b87bffcb2782d78971cccc6c71082eb4fcf737755f1da00760971011f09ac`.
- Source review confirms base weights Theory/Deployment/Weaponization = `ai_medium` (5) and Prototype = `ai_high` (10); every wrapper retains `preferred_factor = 2` in wartime and adds `cautious_factor = 0.50` through its own private-provider trigger.
- The four factory quotes are Theory 2, Prototype 3, Deployment 6, and Weaponization 9. Each trigger is expressed as `NOT = { num_of_civilian_factories_available_for_projects > <stage quote> }`, so the source includes equality. The adapter did not resolve this comparison, so equality behavior is source-reviewed, not MCP-confirmed.
- The decision wrappers remain a candidate subset rather than the complete runtime category pool. No Kruger capacity value is used as a proxy for the private provider.

## MCP scenarios and final evaluation

The required `hoi4.probability_inspect` ran first on the final source using adapter `mission_ai_will_do`. It returned `PROBABILITY_SOURCE_INSPECTED`, four candidates, `poolComplete = false`, three required inputs, and zero inspect-level unresolved records. Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/59d79daf7a1c2e578a1e64cc4cb9637bfdd268c2b149b22476d04f6b41c4b8fa/9604f2f93b726b9352674bd64c9e4f23c7150a42f14988097ac23bdbcedfffdc/probability-inspect-d44cf4871040.json`.

The exact captured baseline set was reused: `event016_mengele_teleportation_baseline_2026-09-25`, scenario hash `36c6510294e1e5055f1756204237f66a6b13adb14297ec93879627cd77d374c6`.

| Scenario ID | Declared state |
| --- | --- |
| `mengele_teleportation_stage_peace` | GER, `has_war = false` |
| `mengele_teleportation_stage_war` | GER, `has_war = true` |
| `mengele_teleportation_stage_low_factory_capacity` | GER, `has_war = false`, private-provider margin = 2 |

The analyzed candidate IDs were `mengele_event016_teleportation_theory`, `mengele_event016_teleportation_prototype`, `mengele_event016_teleportation_deployment`, and `mengele_event016_teleportation_weaponization`. Eligibility/payment state and the complete decision pool were not declared, so these results are willingness scores, not click probabilities or a complete selection race.

Final-source `hoi4.probability_evaluate` returned `PROBABILITY_ANALYZED_PARTIAL`, analysis `probability-e9cf4db9d4440e1df0828659`, the final source hash/revision above, 3 scenarios, 12 candidate-scenario records, 12 unresolved records, zero diagnostics, and no top-level blockers.

| Scenario | Theory | Prototype | Deployment | Weaponization | Result class |
| --- | ---: | ---: | ---: | ---: | --- |
| Peace | 5 | 10 | 5 | 5 | Exact source-score trace before unresolved cautious triggers |
| War | 10 | 20 | 10 | 10 | Exact source-score trace with wartime factor ×2; cautious triggers unresolved |
| Private margin 2 | 5 | 10 | 5 | 5 | Base score trace only; cautious-trigger effects unresolved |

The adapter reported `Scenario does not declare trigger num_of_civilian_factories_available_for_projects` in peace/war and `Trigger num_of_civilian_factories_available_for_projects cannot compare the declared scenario value` in the low-margin scenario. Decision availability checks also remain unresolved at `custom_trigger_tooltip`. The 12 unresolved records cover candidate eligibility and stage trigger evaluation; no low-capacity factor application, live rank, or selection probability is established.

The captured baseline evaluation had peace scores 10/10/10/10 and war scores 20/20/20/20. Final-source medium-base stages now score 5 in peace and 10 in war, matching the reviewed Kruger medium stage bases; Prototype remains 10/20. This is a score comparison, not a probability comparison. Baseline evaluation artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6db135622a0fd81853372213138fb4e5af872878018c3333bf6771610244a443/b52d44ca259b675705ca6b613f9de6aa0cae875d3749e2d1b52b928f40febeec/probability-eca01ee959a4290dd4190473.json`.

## Required comparison and blocker

One final-source `hoi4.probability_compare` call was made with the same candidate IDs and named scenario set, using the captured baseline evaluation as `beforeManifest` and the final current source as `after`. The route rejected the input during schema validation; no comparison artifact or comparison ID was produced. Exact error:

`MCP error -32602: Input validation error: Invalid arguments for tool hoi4.probability_compare: Invalid input: expected string, received undefined at beforeManifest.id; Invalid input: expected object, received undefined at beforeManifest.selection; Invalid input: expected array, received undefined at beforeManifest.candidates; Invalid input: expected array, received undefined at beforeManifest.transitions; Unrecognized keys: "adapter", "analysisId", "diagnostics", "metadata", "operation", "resources", "scenarios", "status", "unresolved" at beforeManifest`.

The baseline evaluation artifact is not a schema-valid compare manifest, and the pre-patch source was untracked with no immutable historical path. This is a compare-input/schema blocker, not a timeout. No further compare retry was made.

No final-source sweep was run: the owner replaced the former single global cutoff with four stage-specific thresholds, and the final evaluator could not resolve the numeric factory trigger. The earlier interim-source sweep on the global threshold is superseded and does not validate the final 2/3/6/9 stage boundaries.

## Final-source artifacts

- Inspect JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/59d79daf7a1c2e578a1e64cc4cb9637bfdd268c2b149b22476d04f6b41c4b8fa/9604f2f93b726b9352674bd64c9e4f23c7150a42f14988097ac23bdbcedfffdc/probability-inspect-d44cf4871040.json`.
- Evaluate JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4e8702ee7cfe3058a3581f567d6b02a3ca2555244aad7cb554c237b3d5d992a1/452e6183d6959b3994bc79727898f68fc1a457c9e90a1a817327cdc18a09c344/probability-e9cf4db9d4440e1df0828659.json`.
- Ranking render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1913079d12762fa07d76a1f45a41140eba3e1a8494f35f13fb3d146b165b124c/a3572babdc54a728fd2b259ff738ea882f9f91b63478eaa4f9e294e32f640990/probability-probability-e9cf4db9d4440e1df0828659-ranking.png`.
- Modifier waterfall render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3374c031b99ba518b439e89538f5d2639cec3bc86480bb5c9de093260aeee0b4/f0b339f8d2251d7483d1f3f8fc72dc5f5dc028e9059f75868d65778fbe7776a2/probability-probability-e9cf4db9d4440e1df0828659-waterfall.png`.
- Unresolved render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c62c7a78931fcd4d061be7682bb163cb97af605dbabfba1b331abb3506a8fd2d/25f9174a4071d015257df64e6f38d934db04381244d7263ba69e47cfb2d37970/probability-probability-e9cf4db9d4440e1df0828659-unresolved.png`.

## Findings and limits

The final source has the requested stage-specific base values, wartime preference, and private-provider cautious triggers at quotes 2/3/6/9 with equality included by source logic. No additional weight change is recommended by this audit. MCP confirms the base and wartime score traces but cannot confirm the factory gates or factor application.

Dominance, starvation, rank reversal, repetition, and exploit risk remain unresolved because the candidate pool and eligibility state are incomplete and this adapter reports scores rather than decision-selection probabilities. Parent can use the exact score traces above for review; a probability-level before/after claim requires a schema-valid retained baseline manifest or immutable baseline source plus an analyzer route that accepts it and resolves the private factory trigger.

Required references were reviewed before Chaos source inspection: root `AGENTS.md`; all eleven core offline Paradox wiki pages; `.agents/skills/chaos-redux-subagents/SKILL.md`; `.agents/skills/chaos-redux-decisions-missions/SKILL.md`; relevant vanilla documentation under `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation`; and vanilla/Chaos decision precedent. No gameplay, stage, or commit change was made.
