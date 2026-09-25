# CBRN theater decontamination motorized gate probability audit

Disposition: the owner applied the motorized archetype affordability-gate correction; this audit is read-only, and the exact matched-scenario comparison remains unresolved because the baseline artifact does not contain the complete scenario inputs.

## Audited surface and source

The weighted surface is decision `cbrn_assign_decontamination_corridor` in `common/decisions/cbrn_doctrine_decisions.txt`, analyzed through HOI4 MCP adapter `decision_ai_will_do`.

The source candidate pool is `cbrn_assign_decontamination_corridor`, `cbrn_choose_battlefield_authorization`, `cbrn_choose_retaliation_only`, and `cbrn_choose_unrestricted_authorization`; MCP discovery reported all four candidates and a complete pool at this source boundary.

The affordability gate is `cbrn_country_can_pay_theater_decontamination_assignment` in `common/scripted_triggers/cbrn_doctrine_triggers.txt`.

The parent changed the motorized stock check from `motorized_equipment_1 < constant:cbrn_doctrine_cleanup_assignment_cost.motorized_equipment` to `motorized_equipment < constant:cbrn_doctrine_cleanup_assignment_cost.motorized_equipment`.

The existing debit helper `cbrn_debit_motorized_stockpile_oldest_first` in `common/scripted_effects/chaosx_dynamic_effects.txt` consumes model 0 before model 1, while the required motorized cost is 2.

This correction aligns the source gate with the helper's archetype-wide, model-aware payment intent; engine aggregation of model variants is not proven by the probability adapter.

## Scenario evidence

The baseline scenario set id was `cbrn_theater_decontamination_baseline` and the four scenario ids were `cbrn_eng_theater_decon_motorized_1`, `cbrn_eng_theater_decon_motorized_2`, `cbrn_eng_theater_decon_motorized_3`, and `cbrn_eng_theater_decon_model0_only_2`.

The retained baseline request notes describe ENG with the theater-exploitation milestone, all other cost inputs set to 10000, model-1 stock at 1, 2, and 3 respectively, and a model-0-only row with model-0 stock 2 and model-1 stock 0; the target `FROM` scope was represented as `{id:"FROM",state:{}}`.

The request notes intended an active decontamination corridor and a contaminated target state, but neither the baseline artifact nor the retained request notes contain a complete typed representation of those conditions.

The corrected baseline evaluate artifact records scenario hash `ea260485951e035695b0ef0e0a437f82ddfed7077fb45739e1d18de741ed7452`.

The post-patch evaluation reused the four scenario ids and reconstructed the ENG, milestone, resource, and motorized values from the retained notes, but produced scenario hash `5a2013fdc827ade1e17c124e42f2eb0be88f561ef48200a73bbb7e4632d8ca9f`.

Because those hashes differ, the post-patch evaluation is a related score-only probe and is not an exact matched-scenario rerun.

## MCP evidence and findings

The installed game target was Operation Postern 1.19.2.0 (d245), and the adapter version was `hoi4-1.19.2.v1`.

Baseline `probability_inspect` reported source hash `10792628365baec1d0963795cb81bfe638bf15273e3ec8ff6ef60ece4ab65768`, source revision `7af216fba66cfda71ebc83fbbf7992afd7e79cae8542d2550bfbffe4b288d6aa`, four candidates, and a complete candidate pool.

The baseline adapter-specific inspect artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/da083e2d13013b7515eac747f11da18114916d950d779793cdf41ceba2052139/eb3efb1651133aa72f3f22cd30adc39ba21aab66e2890605a841bed5c699d484/probability-inspect-10792628365b.json`; the follow-up source-discovery inspect is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6e16cca41e3690e54ed62a53de2f2ac93293cefc0a224ea433f81c713e04f303/dd4dd2c8b2cbb6e9b43acc1fe8f29ee276c5d615a2d2f98fe749c0aac44b8ada/probability-inspect-10792628365b.json`.

The corrected baseline evaluate and sweep both reported source hash `10792628365baec1d0963795cb81bfe638bf15273e3ec8ff6ef60ece4ab65768`, source revision `d027ffe963d871b9fbf8c193e5fe5abcfcdde1479b8727cf59a81abfd6ce24be`, the same candidate-pool hash `564d255b3163468b2f377b4c95ac6f952f972cbda3683a5316d340738638a470`, and baseline scenario hash `ea260485951e035695b0ef0e0a437f82ddfed7077fb45739e1d18de741ed7452`.

Baseline evaluation completed as `PROBABILITY_ANALYZED_PARTIAL` with four scenarios, 16 candidate rows, 14 unresolved items, and two informational diagnostics.

In each baseline row, the assignment base score was exactly 40, while availability remained unresolved at `custom_trigger_tooltip`; the serious factor 2 and severe factor 1.5 had unresolved conditions, and rank and conditional probability were null.

The baseline sweep evaluated four declared stock configurations, but it returned no breakpoints, elasticities, pairwise interactions, or rank reversals because eligibility and ranks were unresolved; the empty reversal list is not evidence that no rank reversal exists.

Post-patch `probability_inspect` reported source hash `10792628365baec1d0963795cb81bfe638bf15273e3ec8ff6ef60ece4ab65768`, source revision `431b906bdff95c3bcb489a0b1d04e8469aba81816f81d1010f5631ddb237fd97`, and the same four-candidate pool.

Post-patch evaluation completed as `PROBABILITY_ANALYZED_PARTIAL` with four scenarios, 16 candidate rows, 15 unresolved items, and one informational diagnostic under reconstructed scenario hash `5a2013fdc827ade1e17c124e42f2eb0be88f561ef48200a73bbb7e4632d8ca9f`.

In each post-patch assignment row, the base score remained exactly 40, the same two factors remained unresolved, availability remained unresolved at `custom_trigger_tooltip`, and rank and conditional probability remained null.

The post-patch evaluator source revision was `423441c025091ed84e58ea65b028615d7351ee4453830556c321438e24662dea`; its source hash remains the decision-file hash and therefore does not identify the changed scripted-trigger bytes.

These decision scores are willingness scores, not click probabilities; the adapter reports `selectionRule = score_only`, does not normalize scores, and has no timing distribution.

The MCP evidence therefore proves the unchanged base score and exposes unresolved eligibility; it does not prove affordability at 1, 2, or 3 trucks, whether the model-0-only row is eligible, or how the game aggregates model variants for generic `motorized_equipment`.

## Comparison and rendered evidence

No valid same-scenario `probability_compare` was produced.

The exact baseline scenario inputs were not recoverable from the complete evaluation artifact, which contains results and hashes but not the original input rows; the reconstructed post-patch hash differs from the baseline hash.

The comparison route was present, but attempts to use the saved baseline artifact as `before` were rejected because the tool requires a source object and rejects the artifact URI and analysis-id object forms tried; per parent direction, no mismatched-scenario comparison was substituted.

Baseline evaluation JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ccd0290359ea3e798e18fd4e1ac2845926e1d884f3db691216bbd4a7dd4c2593/468e95d8f0c411035f92d223c5fbcaaa3f55468292e1a9541a8369abba67de0f/probability-8df9a8be7f0bf0669d562d69.json`.

Baseline evaluation ranking, waterfall, and unresolved renderings: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/31a4739ba7ed709fe8b3c9aa04d3795c950925f7af4e4e36495204fe9ed4773a/06a513447b7e57c1b7ec746bcae427997e576a51e104384cb958b6be85c4aaee/probability-probability-8df9a8be7f0bf0669d562d69-ranking.svg`, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1997f672a43152af75f44661a5147a417a0e4a6e6ccb57a56f8ba30aec8b11bf/3c3d29d5db6f583354f82df53d89a743c7ec33db1bbd076a0b8c26c9fc584bd0/probability-probability-8df9a8be7f0bf0669d562d69-waterfall.svg`, and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9970c22dfa83cf49c1b8c80cd06fa4c40e291561bcec77d7c89f24718c040429/40a9a0a4ffe450bfccc5e79ee6aa72b15ce534b4b63fdd7c2039a6e236ca405e/probability-probability-8df9a8be7f0bf0669d562d69-unresolved.svg`.

Baseline sweep JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9202b76cc9b53fee573d8587a4884166661468d25f3c2250a07a506afc23e501/9818b58c91fa2c642caee66cd09689ff9648342d1e23df3e2926b6c986fa432b/probability-e8081965a010485a651e862d.json`.

Baseline sweep ranking, sensitivity, threshold, and unresolved renderings: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a8e7fedb54ce6245d4661c1caa3d34e63fa06d7f0502c6b6defbee6af7620f77/9d064a1712b23f4c6f264424711d736597e00c8c4573e34e03bc467a567ad8e5/probability-probability-e8081965a010485a651e862d-ranking.svg`, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7f5078d0050c7bb998abbde09e20f0ed392d16ec0e54152b3eebda0ddac8573d/2a5e9e7b9d8ea0335df1d398cb688bfbf5e70a68ee6da46f1572a66368d7f21d/probability-probability-e8081965a010485a651e862d-sensitivity.svg`, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a6d32ffc270e06218fbe6e53b5f3d111d3f383d152a2e17fa057722f7cf35cc8/acbb9d550cfbc17471f14926a5ac12f8e0abb5610257c94fb0715d89e269480a/probability-probability-e8081965a010485a651e862d-threshold.svg`, and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9970c22dfa83cf49c1b8c80cd06fa4c40e291561bcec77d7c89f24718c040429/6db22de22e58c7ef37eeef070e64e7a9a8f4963a09d6508100517f61f93d6fb8/probability-probability-e8081965a010485a651e862d-unresolved.svg`.

Post-patch inspection JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/87476f20c936dbbb2dc06d224ecba09c9f158395c11c23bf76c265c3f3dd3c3c/53d3c4c3b5af5a27fc98ab59c076eba91d0d3107407522f40c009d34946c837e/probability-inspect-10792628365b.json`.

Post-patch evaluation JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ab21aac0c8d1fc99443474fed711d668bbdcf5b75115825c55e069fb240750e1/9573a6010772bc00343c3a7e46d873194b8fa14f71adc06044056e0676242307/probability-213ef0d110667551f1dffeb3.json`.

Post-patch evaluation ranking, matrix, waterfall, and unresolved renderings: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/215924b6c923f0e9475dcb7252ff7e7458419a6673709a427eded465720eb223/e34f0ea463b10ef3774397db677d17a82ef30f602c91b7c6772e782a8798229c/probability-probability-213ef0d110667551f1dffeb3-ranking.svg`, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/542c3d1659aba0f2f347f276d52e0cb4ccc6f823df97afd2a9601fa9eb5d8e14/68a280b63cc9de2e5ee3317d17e4710727ec200248c00603fd34d37f0bf5ee54/probability-probability-213ef0d110667551f1dffeb3-matrix.svg`, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1997f672a43152af75f44661a5147a417a0e4a6e6ccb57a56f8ba30aec8b11bf/a40858a6dabed72e343dff8d7c210a7ef21c1b895e1e9c4ad638dd29e4c0411f/probability-probability-213ef0d110667551f1dffeb3-waterfall.svg`, and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/329d08ca916b3c3d22dc145cf5fb2bb8dc34470d73e86e84bfebc745888c1370/70a7dc5230c289222a559eb1e3b6bf4dd4380cb8107b9794252ab4232ae89424/probability-probability-213ef0d110667551f1dffeb3-unresolved.svg`.

A separate baseline `probability_render` attempt returned `PROBABILITY_ANALYSIS_NOT_CACHED` with message `Render requires an analysis ID produced by this server process`; the inspect, evaluate, and sweep calls supplied their own rendered evidence links above.

## AI behavior, limits, and recommendations

The assignment has a positive base weight of 40, but its actual eligibility and modifier-adjusted score remain unresolved; no ranking, dominance, starvation, or rank-reversal conclusion is justified.

The adapter models decision AI as a score race without a normalized selection denominator, so no score is a click probability.

The adapter has no timing or sequence model for this decision; repetition, cooldown, and timing behavior were not analyzed.

The full four-candidate source pool is declared, but candidate availability is unresolved, so no candidate is proven impossible or guaranteed to win under these fixtures.

Keep the `motorized_equipment` gate and model-0-first debit aligned to the same cost constant, and retain all four candidate ids if a later exact scenario compare is rerun.

For a decisive eligibility comparison, preserve the original baseline scenario JSON or repeat the baseline with a complete adapter-supported binding for the `FROM` state, `custom_trigger_tooltip`, active-corridor helper, contamination helper, and cost inputs; do not infer generic archetype aggregation from this score-only pass.

No probability retuning is recommended because this patch changes only affordability eligibility and the evaluated base score remains 40.

## Skipped work, skills, and references

No exact `probability_compare` was run because the recovered baseline artifact omits its scenario input rows and the reconstructed scenario hash does not match; no mismatched comparison was substituted.

No post-patch sweep, simulation, or sequence analysis was run because the exact baseline scenario object was unavailable, no uncertain distribution or seed was declared, and this adapter does not model timing or sequence behavior.

No gameplay source, AI weight, helper, localization, spreadsheet, or runtime file was edited by this auditor, and no commit was created.

Skills used: `.agents/skills/chaos-redux-subagents/SKILL.md` and `.agents/skills/chaos-redux-decisions-missions/SKILL.md`.

Offline wiki references consulted: Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, and AI modding; vanilla decision, AI, trigger, and effect documentation was also reviewed.

No live game was launched.
