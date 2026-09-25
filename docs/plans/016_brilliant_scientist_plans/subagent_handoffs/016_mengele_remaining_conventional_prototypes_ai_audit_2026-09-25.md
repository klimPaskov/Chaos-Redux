# Event 016 conventional Prototype AI audit

**Disposition:** bounded read-only audit; no gameplay files changed. No concrete defect was found in the inspected AI weights or the parent’s no-DLC gate branches. MCP could not resolve candidate eligibility, so this is score evidence plus source review, not proof of campaign availability or selection. No score or rank here is a click probability.

## Scope and source identity

Repository HEAD at audit time: 752e25a6ff5509bcedb28af435c745f57889d176.

| Surface | Source | Local SHA-256 | MCP inspect revision / aggregate source hash |
|---|---|---|---|
| Three remaining conventional Prototypes | common/decisions/016_mengele_remaining_conventional_prototype_decisions.txt | 6851849676fb508c6de074f285f1db1868ff9605067eb134e34c8f65861d42b8 | 9edddbf9c7339d830ad0fc037764603d4779e0e599c259ca952c98044ba1089b / 424773a79edd29be9bfc3ffcd49b45f4421d2e21b7d6f9399788c368a171f53f |
| Existing conventional stage decisions | common/decisions/016_mengele_conventional_stage_decisions.txt | 48cd2dd6a7414320edd8c173b8ffaafa24d9a488c7b3e4fc24a3cfd65aa8a4303 | d0115631784e1dcf2731dac7800a6e506b24a34e375ecaaab32505d34b76b164 / 97f3a918d63122e548b8cc2405ddf09d7e083570cb88b9a212c709cfeb0020a0 |
| Parent later-stage requirement changes | common/scripted_triggers/016_mengele_conventional_stage_decision_triggers.txt | 1e361c5f85585c4eb51aa0ea7bb2345cc21287a2ea0c7858ce93263f737b2a38 | source-reviewed; not a weighted surface |
| New Prototype requirements | common/scripted_triggers/016_mengele_remaining_conventional_prototype_decision_triggers.txt | d482687f1139800d19c6ae7f6af53113211d74c16f4deb438e817320d7cd76fa | source-reviewed; not a weighted surface |
| Shared AI tuning constants | common/script_constants/016_brilliant_scientist_project_constants.txt | a95301ed9cbc7bb8fcb751885165f62ae5aa8c6b315eadb0c5cdaf79350ce131 | source-reviewed |

The new decision file is absent from HEAD. The exact Git result was: fatal: path 'common/decisions/016_mengele_remaining_conventional_prototype_decisions.txt' exists on disk, but not in 'HEAD'. These three candidates therefore have no historical before-source for a same-candidate probability_compare.

The existing decision source is in HEAD (blob 987de7c337cbc23b3646425adda6fbe5bd04fa98) and its AI weights are unchanged in the working tree. The parent changed eligibility in the separate scripted-trigger file; its prior HEAD blob is 6a2df3c707b7032f2c5d4e4d004919a4a5383671. No valid MCP before-overlay comparison was performed for that helper change.

## MCP scenarios and completeness

Used the mission_ai_will_do adapter. probability_inspect was called first for each weighted source. The initial Prototype inspect used the wrong input key source.relativePath and was rejected with: MCP error -32602: Input validation error: Invalid arguments for tool hoi4.probability_inspect: Unrecognized key: "relativePath" at source. Retrying with source.path succeeded.

The shared scenario set is e016_no_dlc_conventional_prototypes_2026-09-25, actor GER, hash be66eba906540f5ec4af6bbff78143dbb23214893f7db28c68bd65a367074ca5. The audit followed the repository’s subagent and decisions/missions skills, all 11 required offline core wiki pages plus AI/Decision Modding, and the relevant vanilla trigger documentation and timed-decision precedent.

| Scenario ID | has_war | has_dlc | available civilian factories |
|---|---:|---:|---:|
| peace | false | false | 99 |
| war | true | false | 99 |
| no_dlc_exact_factory_margin_electronics | false | false | 2 |
| no_dlc_exact_factory_margin_rocketry | false | false | 3 |
| no_dlc_exact_factory_margin_high_energy | false | false | 3 |
| dlc_native_gating | false | true | 99 |

All scenarios used empty flags and scopes, and supplied only the flat values shown. They are primitive-input probes, not complete campaign fixtures. The evaluator could not compare the declared value for num_of_civilian_factories_available_for_projects; the exact quote values did not resolve it. It also left custom_trigger_tooltip unresolved with “Scoped or compound trigger custom_trigger_tooltip is not declared by the scenario.” As the DLC and other compound requirements sit behind that wrapper, the DLC scenario does not prove either DLC gate outcome.

The inspect adapter reports rawScore=true, normalizedProbability=false, and poolComplete=false. The three-Prototypes source pool and the 15 candidates in the stage source are not the complete mengele_clone_army_category pool; candidates also live in other decision files. External trigger state is incomplete for every scenario.

## Three Prototype decision scores

Evaluated mengele_event016_electronics_prototype, mengele_event016_rocketry_prototype, and mengele_event016_high_energy_prototype across the six named scenarios: 18 candidate-scenario observations. Result PROBABILITY_ANALYZED_PARTIAL; analysis ID probability-4690e318daa2b21f2f4e6934; evaluation source revision 81fdb6191a8b85de048e42d4e8b19eb6a6d967567083748c539b34a686092c55; aggregate source hash 424773a79edd29be9bfc3ffcd49b45f4421d2e21b7d6f9399788c368a171f53f; scenario hash as above. Eligibility remains unresolved for all 18 observations.

- Each decision uses constant:brilliant_scientist_project_board.ai_high = 10.
- In war, constant:brilliant_scientist_project_ai.preferred_factor = 2 applies, tracing 10 to 20; in peace it does not apply.
- Each decision has the cautious factor 0.50 behind its low-factory-margin helper. That comparator remains unresolved at ordinary and exact-margin values, so the final combined score is unresolved where this branch matters. The war value 20 is only the trace before that unresolved branch.
- The three decisions share this pre-caution policy. Compared with the Kruger fallback policy recorded in the parent handoff, the traced policy uses the same ai_high base, preferred-war factor, and cautious low-margin factor. Capacity, receipt, and complete route-state parity against Kruger were not evaluated in these primitive scenarios. This audit selects no replacement tuning value.

The source helpers visibly check no Götterdämmerung, provider/project state, and resources. The low-margin helper negates “available factories greater than quoted factories,” so source intent includes equality at the quoted margin; MCP did not establish runtime truth at equality.

## Existing Deployment and Weaponization candidates

The inspected stage source contains 15 Theory, Deployment, and Weaponization candidates across Biomedical, Electronics, Materials, Rocketry, and High Energy. The affected set is mengele_event016_biomedical_deployment, mengele_event016_biomedical_weaponization, mengele_event016_electronics_deployment, mengele_event016_electronics_weaponization, mengele_event016_materials_deployment, mengele_event016_materials_weaponization, mengele_event016_rocketry_deployment, mengele_event016_rocketry_weaponization, mengele_event016_high_energy_deployment, and mengele_event016_high_energy_weaponization. Evaluation covered the 15 candidates × six scenarios (90 observations): result PROBABILITY_ANALYZED_PARTIAL; analysis ID probability-5743ff2bcc25b9aff0eec677; evaluation source revision 770e0c95ab5eeef1f4ff5104a63eed159b4feedb00aebdcbf62d8bc8a48aed2e; aggregate source hash 97f3a918d63122e548b8cc2405ddf09d7e083570cb88b9a212c709cfeb0020a0; same scenario hash. Eligibility for the ten later-stage candidates remains unresolved because their compound tooltip requirements are not represented.

Within the supplied source candidates, Biomedical, Electronics, Materials, and Rocketry Deployment/Weaponization use ai_high = 10; High Energy Deployment/Weaponization use ai_medium = 5. The preferred-war factor is false in peace and doubles the traced values in war to 20 and 10. These are score-only traces in an incomplete pool; they do not establish candidate availability, actual choice, or selection odds.

Source review of the parent’s trigger patch finds the no-DLC alternatives for Electronics Deployment and Weaponization, Rocketry Deployment, and High Energy Deployment. Their DLC branches retain the corresponding technology and special-project requirements. The other later-stage gates were not changed in the reviewed diff, and the weighted decision definitions are unchanged. This is source evidence only; MCP did not resolve these compound gates.

## Defects, risks, and limits

No concrete source defect was found in the reviewed score blocks or no-DLC alternatives. This audit does not recommend changing weights. Candidate eligibility is unresolved and the category pool is incomplete, so the evidence cannot establish positive weight on an impossible choice, rank reversal, dominance, starvation, repetition rate, or exploitability. No cadence or campaign-state transitions were modeled. The adapter is score-only and does not calculate normalized selection probability.

New-candidate compare limitation: there is no before decision source in HEAD. Existing-candidate compare limitation: the decision source is unchanged while the parent changed its helper trigger source; a meaningful comparison needs the prior helper source as a supported before-overlay. No compare call was made, so whether the live compare schema accepts such an overlay remains unknown.

## MCP artifacts

Prototype inspect: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/32db8a6d3fad09c186f69164c716676f5cf74cc2b1b1a8aa59d7db6c8b64184c/20de37203b81726e881aa8d2af7d0904cb16bccf3c12408ab2089b6862ca4750/probability-inspect-424773a79edd.json

Stage inspect: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/629b6142fe0a95aa1d3c4f0e9cc3146f4ff57412b98374fb0ce6964e6a236907/27ec3a98bed7b8277bee47010dfad797562b900f9781c0575baf3ec33c1cf853/probability-inspect-97f3a918d631.json

Prototype evaluation: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8b0d722889d1369119f5ff58893eaa12ff79f055798c65a8555a8d9e00aec23b/71d7fdf96f64aec39f12b47147e3c75a6c5508470d892711eca91f3614a86e6c/probability-4690e318daa2b21f2f4e6934.json

Stage evaluation: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/80b799527b3dad332c3ee2d67e3937aa6ebddf0e510b33ca808c0faae027e9f2/00654b07764d90ea9f318988745e48cec173af6ab50e9b08a79906ce77a64dc0/probability-5743ff2bcc25b9aff0eec677.json

No continuation URI was returned with the completed inspect/evaluate artifacts.

Prototype generated ranking, matrix, and unresolved views:
- hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ea6fa7ccc5cd6c1c22996d3f2da69645ac00add68f8f3aee19ed2e9f90e842bb/aa4a0fe816e2694aa481f522243442dbc1125fe7852bd22fc7b022a9e5226e3e/probability-probability-4690e318daa2b21f2f4e6934-ranking.svg
- hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7490e72962373186be1e1d31724d2c901d4482eebd833702f1741038c2b4f0c1/1bef8ae0d5c73a961c8049e57d81562857dbb582e1bad85f0634b0ee9e9ab1ec/probability-probability-4690e318daa2b21f2f4e6934-matrix.svg
- hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1b30e05bcfe11eec97e2b86d9837715ff1bd530378cc1326b128d4547568ff20/6bc8718d123d16c4cc0efce88b7acec50f3a3c207830d2852e18c5a5bc22fee3/probability-probability-4690e318daa2b21f2f4e6934-unresolved.svg

Stage generated ranking, matrix, and unresolved views:
- hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/355d8ec56770db1f3986e5c456045ca4d70362bcd9cfa7ae4ef4663ff6620332/acbf2d69f298f1feb9f3b74ff0e5b970c19c17438f6532bfeea5b0dc0ee7e4e1/probability-probability-5743ff2bcc25b9aff0eec677-ranking.svg
- hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9154ae9add1d9f368699ece6daaf3f728f88e61cfff99e4e224133f67505b0a4/3938b2706b1216da00f687ea50c702a0d333d6ec2291d4851787d92dccfbd6d9/probability-probability-5743ff2bcc25b9aff0eec677-matrix.svg
- hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7b9d4d1b6cb1a0016658cbcfb41a85a95dc297f51f6c16b3e804370f8638025e/dee7de1ce853412f080dee55f1208e403fb9ec44664193d70a8443dfb7dd1edd/probability-probability-5743ff2bcc25b9aff0eec677-unresolved.svg

## Unperformed work and handoff

probability_sweep, probability_compare, and a separate probability_render call were not run after the user explicitly requested an immediate bounded handoff and no further MCP calls. This was a user-directed stop, not an adapter stall or a tool validation failure. Evaluations returned generated ranking, matrix, and unresolved render artifacts above. The exact MCP limits observed are the unresolved custom_trigger_tooltip and numeric factory comparison; the missing HEAD baseline for the new decisions is the exact compare limit. A supported before-overlay for the changed helper source and scenarios capable of binding the tooltip/compound triggers and factory comparator remain necessary to close the other evidence gaps.

Action for the parent: current evidence found no AI-weight defect requiring a value change before committing the three no-DLC Prototype decisions. Keep the accepted Kruger-parity policy absent separate balance evidence; this audit chooses no new target. Preserve the reviewed no-DLC alternatives and DLC-native requirements in the parent trigger file. Record availability, exact-margin behavior, ranking, and campaign risk as unresolved pending an adapter-supported fixture and, for the existing stage patch, a real HEAD before-overlay using the same scenario IDs.
