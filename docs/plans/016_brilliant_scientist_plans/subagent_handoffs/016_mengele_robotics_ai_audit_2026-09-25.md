# Event 016 Mengele Robotics AI Baseline Audit

Date: 2026-09-25
Status: Baseline audit and owner-patch follow-up recorded; post-patch MCP evaluation partial; historical compare blocked.
Disposition: Read-only handoff for parent review. No gameplay changes or balance target applied.

## Parent decision summary (pre-patch baseline)

If the intended Robotics cautious proxy is stage-specific “no spare factory” headroom, the current global helper does not implement that policy. It marks Theory cautious with 2–7 available civilian factories although its quote is 1, and Prototype cautious with 4–7 although its quote is 3; both are one-spare scenarios at the lower boundary. It also marks Deployment cautious at 7 for a quote of 6. Conversely, Weaponization at exactly 8 factories has no spare at its quote of 8, but the current strict less-than-8 helper does not mark it cautious.

So, under the stage-margin interpretation, Theory and Prototype are structurally over-cautious, and Weaponization misses the equality boundary. This is a source-logic conclusion, not a verified selection-rate conclusion. Kruger is not a direct factory-margin control: its cautious helper checks the project-capacity ledger variable, not free factories. The parent should decide whether Mengele’s broad macro-capacity proxy is intentional or whether this stage-specific mismatch warrants a patch.

Do not interpret the returned matrix zeros as valid AI scores. The evaluator could not resolve required eligibility inputs, and this adapter reports raw scores only; it does not normalize decision scores into click probabilities.

## Audited sources and hashes

- Mengele weights: common/decisions/016_mengele_robotics_stage_decisions.txt; local SHA-256 F7D230A012B7D902F30857A80285E416DD82B6F6DE87200ABC9A6738B0F5C586; MCP canonical sourceHash 7d4a777af50963d186b5ad32e99c12a99f3340f609f2269358b8f9ebc8435e77.
- Mengele cautious trigger: common/scripted_triggers/016_mengele_robotics_stage_decision_triggers.txt, brilliant_scientist_mengele_robotics_decision_capacity_is_low.
- Shared tuning: common/script_constants/016_brilliant_scientist_project_constants.txt; ai_high = 10, preferred_factor = 2, cautious_factor = 0.50; Robotics stage civilian-factory quotes are Theory 1, no-DLC Prototype 3, Deployment 6, Weaponization 8.
- Kruger comparison: common/decisions/016_brilliant_scientist_directorate_project_board.txt; local SHA-256 EE129E541E275A4C48CF6FE375E8AE2833D85529E6CE5EF74B6707282B405293; MCP canonical sourceHash 62f2b563c5e777f22c3cff66a3206821a6d2d9a7b74aff0017e13cad552aa562.
- Kruger cautious input: common/scripted_triggers/016_brilliant_scientist_triggers.txt, brilliant_scientist_has_low_project_capacity; this compares brilliant_scientist_project_capacity against brilliant_scientist_measure.band_low. The capacity value is the project portfolio ledger, not num_of_civilian_factories_available_for_projects.

The four Mengele identifiers inspected were mengele_event016_robotics_theory, mengele_event016_robotics_prototype, mengele_event016_robotics_deployment, and mengele_event016_robotics_weaponization. Each uses base constant:brilliant_scientist_project_board.ai_high, a war modifier with preferred_factor when has_war is yes, and cautious_factor when the global low-capacity helper is true.

The exact Kruger comparison identifiers were brilliant_scientist_advance_robotics_theory, brilliant_scientist_fallback_robotics_prototype, brilliant_scientist_advance_robotics_deployment, and brilliant_scientist_advance_robotics_weaponization. Their base and war/cautious factors match the Mengele values; their cautious predicate differs as described above.

The Mengele helper compares available civilian factories strictly below the Weaponization quote of 8 for every stage. The no-DLC Prototype is a paid fallback only when Götterdämmerung is absent; with that DLC, the native prototype project path is authoritative. These decisions are sequentially gated, so the four candidates do not form a simultaneous in-game decision race.

## HOI4 probability MCP evidence

The decision_ai_will_do inspect did not discover these timed stage choices and suggested mission_ai_will_do. I then used mission_ai_will_do with the explicit four-ID candidate pool. Its selectionRule is score_only, normalizedProbability is false, and the documented limitation is that mission scores are not normalized without a documented complete selection rule.

| Operation | Source and result | Revision or scenario hash | Artifact |
|---|---|---|---|
| Mengele decision adapter discovery | SourceHash 7d4a777af50963d186b5ad32e99c12a99f3340f609f2269358b8f9ebc8435e77; 0 matching decision candidates; suggested mission adapter. | sourceRevision 879fb88d08f1d1bacf948d9860414beee8981df00ee306616c6fbca22ccca67e | hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c2279a52f9e3a702336be9a83e4bbf2c5a8601b95bea9fc0f8e30ecb05869b47/4f3cc85aad46efd68f314fccf421bbba8a5c97c9d1f9b7f1392350a443592f2f/probability-inspect-7d4a777af509.json |
| Mengele mission adapter inspect | Four explicitly requested candidates; poolComplete true for that declared pool; required inputs include custom_trigger_tooltip, has_war, and num_of_civilian_factories_available_for_projects; unresolved 0 at static inspect. | sourceRevision ac9e12ce708122ade6ad32e99f8b300c719a42b2693e8e31ddac308dbce20d04 | hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/66d5e9facfad2a52b0e1206419cfc3aae52376b2055a353f96b6d335015bcf0a/aebb3cc7d0f24456e1c2248d07b385044459d7874b9942eb0701f03f756db0e9/probability-inspect-7d4a777af509.json |
| Kruger decision adapter discovery | Stage choices not discovered by decision adapter; three unrelated manage actions were found. | sourceRevision ddbc1e94a457cd6ae9972ef73dd315795febe8259f432256644bb79d70d81c28 | hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9dfd2e8759c6c05fba6eb91eb6ae9c7c75c37b27205169a692cc5bbdfa477aff/c2642c91117f717a59c7540e34764eee405b8dd423c60ebf1445b6d2d0033122/probability-inspect-62f2b563c5e7.json |
| Kruger mission adapter inspect | Four explicitly requested candidates; poolComplete true for that declared pool; required inputs include check_variable, custom_trigger_tooltip, and has_war; unresolved 0 at static inspect. | sourceRevision 34744ecc1240ce498fb3a612e395d3b716c3cb98db9081a87ec4b0e40c72dfec | hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fbac9b9fccc3c4171b476a1cffed37812e625b3c7a0e30f09c521aff9225d08e/5ad0a0b001db460dbb85603e52d335ba4a088550d0fbae009d9826a299c990ed/probability-inspect-62f2b563c5e7.json |

### Named scenario evaluation

Scenario set: E016_ROBOTICS_PEACE_WAR_FACTORY_MARGIN_2026_09_25. The actor was the placeholder ABC, flags were empty, and no country/target scopes were declared. State inputs set has_war, available civilian factories, project capacity 100, and a false has_dlc:Gotterdammerung value. The explicit candidate pool was the four Mengele identifiers above. Project capacity 100 isolates the difference between the factory-margin input and Kruger’s portfolio-ledger input.

| Scenario id | State purpose |
|---|---|
| robotics_peace_margin_10 | Peace; 10 available factories; ample-margin control. |
| robotics_war_margin_10 | War; 10 available factories; preferred-factor control. |
| robotics_peace_low_margin_theory_2 | Peace; 2 factories, one above Theory’s quote of 1. |
| robotics_peace_low_margin_prototype_4 | Peace; 4 factories, one above Prototype’s quote of 3. |
| robotics_peace_low_margin_deployment_7 | Peace; 7 factories, one above Deployment’s quote of 6. |
| robotics_peace_low_margin_weaponization_8 | Peace; exactly 8 factories, equal to Weaponization’s quote. |

The pre-patch baseline Mengele evaluation returned PROBABILITY_ANALYZED_PARTIAL, analysisId probability-79c6739f317ccda6c8b4a318, sourceRevision 0c192d95124248cbea32686856acfd744f8305999279290b94bb2f4f0c9605a6, canonical sourceHash 7d4a777af50963d186b5ad32e99c12a99f3340f609f2269358b8f9ebc8435e77, and scenarioHash 231a923899686a828a02b3e6a23cc712a7bc133f30f7a8e7cdf2e9a7977475ea. It evaluated 24 candidate/scenario rows and reported 8 unresolved outcomes with no diagnostics.

The rendered matrix displays 0 for every cell. Treat those zeros as unusable placeholders: the unresolved records include “Trigger num_of_civilian_factories_available_for_projects cannot compare the declared scenario value” and “Scoped or compound trigger custom_trigger_tooltip is not declared by the scenario.” A first probe put custom_trigger_tooltip=true in flat state and remained partial; the adapter contract says flat primitives may not bind compound triggers. Do not invent a gameplay flag or claim that the evaluator proved 0, 10, or 20 as a score.

The matching Kruger evaluation returned PROBABILITY_ANALYZED_PARTIAL, analysisId probability-8a0f5233361798e190205860, sourceRevision 24b49a3ceb7b221b5b1682e379384f51ce8d618285a3c59a5299013eac1f1b0b, canonical sourceHash 62f2b563c5e777f22c3cff66a3206821a6d2d9a7b74aff0017e13cad552aa562, and scenarioHash 7741d1f61bef90c8ebbabd549e8a425ec92b19abfeba7ff4001cc2c71a4affa5. The supplied 11-scenario run produced 44 rows and 8 unresolved outcomes. It included high and low project-capacity controls and the stage-margin factory counts; it does not provide a complete in-game decision pool or prove a normalized outcome.

Primary Mengele evaluation JSON: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/aeb1f02a45c66720124865214b1c941a36fc475645605fa7ad3a336ece15fd43/8f269f850b1f87bea0d3bf7d479b1344f3a504f878946bfd07f768e8bfddcd2e/probability-79c6739f317ccda6c8b4a318.json

Rendered Mengele matrix SVG: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/681b8d8d1cff69828484b17c3f8b868415139a8d7aa401cbc1527022f39cecae/d6217063a7ede6f50c01af482dec7457174dc072e0088ea41b66194dd29cbc4a/probability-probability-79c6739f317ccda6c8b4a318-matrix.svg

Rendered Mengele unresolved SVG: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/692a7f8c74384c81b6229e1d9302a178e871a9f9cd836166170696622aab3f28/ab7212638c0286eaf6aea33a366c65b662ee22e1ac603b2bf8a5b4ded7054f85/probability-probability-79c6739f317ccda6c8b4a318-unresolved.svg

Kruger evaluation JSON: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d2f43baa1b554cd6549f9247c497fca99f710f902c7c772d20c8a232e8326dd7/45a8dd0fb75afdf05e72beae406fa2775da7136039bd840b786a6faff992059a/probability-8a0f5233361798e190205860.json

Kruger rendered matrix SVG: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/98d1060c791e839f404ec23345dc0c7485bff1c2b01e3862fad4cb4bff81ceb7/ff06bde72c8d169d3de384fb0e8001f8cdb2ed372bb03ad6cfb25490333f8463/probability-probability-8a0f5233361798e190205860-matrix.svg

## Findings and limits

- Score inputs match across the four compared blocks: base 10, war-preferred factor 2, cautious factor 0.50. This is a willingness score expression, not a probability; the MCP adapter also expressly disables normalized probability.
- The named margin scenarios isolate the global threshold’s source behavior. They do not prove full decision eligibility, execution, stage timing, or campaign-level factory availability.
- The four requested symbols are a complete declared comparison subset only. The full category/global decision pool is incomplete, and stages are sequentially gated rather than simultaneously selectable.
- No exact ranking, selection probability, timing, starvation, or repetition result is established. No exploitable route or positive-weight impossible-choice finding is established by this partial run.
- At baseline, a historical pre-change source path was unavailable. The post-patch compare attempt and its exact validation rejection are recorded in the follow-up below; do not treat a self-comparison or empty before path as evidence.
- probability_sweep did not complete and produced no result artifact. The sweep call was interrupted before it returned; this handoff reports no sweep breakpoint or sensitivity conclusion.
- A first parallel Mengele evaluate attempt returned INTERNAL_ERROR; a serial narrow rerun completed as partial. The partial rerun does not clear the eligibility blocker.
- No probability_simulate or probability_sequence was run because no uncertain-input distribution or complete custom weighted pool with cadence/transitions was declared.

## Baseline recommendation (superseded by owner patch)

If the intended policy is “apply caution only when available factories do not exceed the current stage quote,” make the helper stage-aware and preserve the owner-selected equality semantics. Re-evaluate all four candidates with the same named scenarios after the parent decides whether this is the desired policy. If the shared global threshold is an intentional broad macro-capacity heuristic, document that intent and do not describe it as stage-margin behavior. This report does not select between those design choices and applies no patch.

The audit used chaos-redux-subagents and chaos-redux-decisions-missions. It consulted the required 11 offline core wiki pages, relevant decision/AI material, vanilla trigger documentation, and a vanilla Soviet design-bureau decision precedent. Process deviation: the exact Chaos source files were opened before the vanilla documentation/precedent review was completed; the vanilla review was completed afterward. No live game was launched, no gameplay file was changed, and no commit was created.

## Owner-patch follow-up (2026-09-25)

The parent reported that the owner patch gives each Robotics stage a cautious factory-margin trigger at its exact stage quote, with equality included. The following source review and MCP run are read-only; they do not alter or commit the patch.

### Source delta

The pre-patch decision source SHA-256 was F7D230A012B7D902F30857A80285E416DD82B6F6DE87200ABC9A6738B0F5C586 and used brilliant_scientist_mengele_robotics_decision_capacity_is_low, one global comparison against the Weaponization quote of 8, for all four ai_will_do blocks.

The current decision source SHA-256 is 8B974AC810C6A74E068146C91168DDEE988ED600E46C45DD166D4569BC9D2BD5. The current trigger source SHA-256 is 064CC387D3E89830C6B5A3926F542226A052EDE2881B5CF3460DDD6136149B69. Both source files are untracked in Git in this worktree, so no prior committed file version is available at HEAD.

Each current low-margin trigger uses NOT { num_of_civilian_factories_available_for_projects > stage_quote }, which implements the requested inclusive boundary. Each ai_will_do now references its corresponding trigger. The base remains ai_high = 10, the war-preferred factor remains 2, and the cautious factor remains 0.50.

| Named scenario and corresponding stage | Baseline global helper | Owner-patch stage helper | Source-logic delta |
|---|---|---|---|
| robotics_peace_low_margin_theory_2; Theory quote 1, available 2 | Cautious at < 8 | Not cautious at <= 1 | The one-spare Theory case no longer receives the cautious factor. |
| robotics_peace_low_margin_prototype_4; no-DLC Prototype quote 3, available 4 | Cautious at < 8 | Not cautious at <= 3 | The one-spare Prototype case no longer receives the cautious factor. |
| robotics_peace_low_margin_deployment_7; Deployment quote 6, available 7 | Cautious at < 8 | Not cautious at <= 6 | The one-spare Deployment case no longer receives the cautious factor. |
| robotics_peace_low_margin_weaponization_8; Weaponization quote 8, available 8 | Not cautious at < 8 | Cautious at <= 8 | The exact-cost Weaponization case now receives the cautious factor. |

At 10 available factories, the peace scenario has no cautious modifier; the war scenario has the preferred modifier and no cautious modifier. These are exact source-predicate results for the corresponding stage candidates. They do not establish a game-wide candidate ranking or click probability.

### Current MCP inspect

The required post-patch mission_ai_will_do inspect returned PROBABILITY_SOURCE_INSPECTED with sourceHash 547f244eb196b2d49ab9bf9af1ab8a4dc429cf139cd7f87fd7aa9816e5cdbe24, sourceRevision 4a9a207472c81935c3a4059e7d1ed884749d7c81f2f0202bb7da2b377e1798fd, poolComplete true for the explicitly supplied four candidate IDs, candidates 4, requiredInputs 3, and unresolved 0 at static inspect. This declared subset is not the complete global decision pool.

Post-patch inspect artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7e475f06872b36b9253dafb45140088007b9896de85d3e56ffbe43f0e98d1a5c/fe3de60380364e617a43a11196f5dd9c6975ad04cb01893f34634c1d5da85d77/probability-inspect-547f244eb196.json

### Required same-scenario compare attempt

I attempted hoi4.probability_compare with adapter mission_ai_will_do, the same four candidate IDs, and the exact six-scenario set E016_ROBOTICS_PEACE_WAR_FACTORY_MARGIN_2026_09_25. The baseline reference supplied the recorded pre-patch path, canonical sourceHash 7d4a777af50963d186b5ad32e99c12a99f3340f609f2269358b8f9ebc8435e77, and sourceRevision 0c192d95124248cbea32686856acfd744f8305999279290b94bb2f4f0c9605a6; the after reference supplied the current path, canonical sourceHash 547f244eb196b2d49ab9bf9af1ab8a4dc429cf139cd7f87fd7aa9816e5cdbe24, and inspect revision 4a9a207472c81935c3a4059e7d1ed884749d7c81f2f0202bb7da2b377e1798fd.

The compare route rejected those historical identity fields before analysis with this exact error:

MCP error -32602: Input validation error: Invalid arguments for tool hoi4.probability_compare: Unrecognized keys: "sourceHash", "sourceRevision" at before
Unrecognized keys: "sourceHash", "sourceRevision" at after

No comparison ID or comparison artifact was produced. Git reports both current source files as untracked; the previous audit/MCP evidence retains the baseline hashes and artifacts, but the pre-patch file is not available at a distinct mod-relative before path. The installed compare contract requires before.path and after.path; using the live path for both sides would compare the patched file to itself, so I did not do that. The historical before/after comparison remains blocked pending an accessible pre-patch source path or a compare route that accepts the stored baseline artifact/revision.

### Post-patch narrow evaluation and render

The current mission_ai_will_do evaluation reused the exact six named scenarios and four candidate IDs from the baseline. Its scenarioHash is 231a923899686a828a02b3e6a23cc712a7bc133f30f7a8e7cdf2e9a7977475ea, identical to the baseline evaluation. It returned PROBABILITY_ANALYZED_PARTIAL with analysisId probability-b5aea44306531957089f7fc2, sourceHash 547f244eb196b2d49ab9bf9af1ab8a4dc429cf139cd7f87fd7aa9816e5cdbe24, sourceRevision 12a7e23fd34101021aae52bd78a3ae83e1ba7d5b00b2a1160f6f47799b25a021, 6 scenarios, 24 rows, 8 unresolved outcomes, and no diagnostics.

The rendered current matrix shows 0 in all 24 cells, as did the pre-patch rendering. These zero cells are not valid raw-score deltas because eligibility remains unresolved. The current unresolved artifact reports both “Scoped or compound trigger custom_trigger_tooltip is not declared by the scenario” and “Trigger num_of_civilian_factories_available_for_projects cannot compare the declared scenario value.” The adapter therefore did not prove the source-logic changes as numeric scores or rankings.

Post-patch evaluation JSON: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f43c87fc9991bc2383a9dffc5bfd6127f46c324774c423b91a31a8ed4a6511de/5d011d93a82da3eabe7584f161979c5b9413d161c87fdbc131d4c8b2d1506110/probability-b5aea44306531957089f7fc2.json

Post-patch rendered matrix SVG: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/681b8d8d1cff69828484b17c3f8b868415139a8d7aa401cbc1527022f39cecae/d0e6d4d0d2f1b9b1966d812f6f2e4789d2b34fdc3836760e7f799454d6aa423a/probability-probability-b5aea44306531957089f7fc2-matrix.svg

Post-patch unresolved SVG: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/692a7f8c74384c81b6229e1d9302a178e871a9f9cd836166170696622aab3f28/8c98a4a3e7444e2fa253e2011059986027ca80af616fb0d3ee317745660b632b/probability-probability-b5aea44306531957089f7fc2-unresolved.svg

This adapter remains score_only with normalizedProbability false. Actor ABC, no scopes, and flat primitive trigger inputs leave the scenario fixture incomplete for actual decision eligibility; the four requested entries remain a subset, and the decisions are sequentially gated. No exact score ranking, selection probability, campaign timing, starvation, or repetition conclusion is supported. I did not run a post-patch sweep because the requested follow-up was the same-scenario compare plus narrow inspect/evaluate; compare validation failed before analysis.

The source-logic delta is positive and matches the owner’s stated target at each stage quote, including equality. Numeric MCP confirmation and formal before/after comparison remain unresolved for the reasons above. No gameplay source was edited by this audit, no commit was created, and HOI4 was not launched.
