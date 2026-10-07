# Event 012 Gods activation and settlement probability final handoff

Date: 2026-10-07.

Status: partial. The source and scope review is complete, but final after-score evaluation and same-scenario comparison are unresolved because the HOI4 probability calls timed out.

This was a read-only audit. No gameplay files were edited, no Git mutation was made, and Hearts of Iron IV was not launched.

## Audited surfaces

The weighted surface is the decision_ai_will_do adapter over common\decisions\012_africa_gods_decisions.txt. The comparable candidate list remains exactly the eight IDs in the 2026-10-06 handoff:

- gods_of_africa_comply_demand
- gods_of_africa_substitute_demand
- gods_of_africa_negotiate_demand
- gods_of_africa_refuse_demand
- gods_of_africa_permanent_defiance
- gods_of_africa_choose_reciprocal_covenant
- gods_of_africa_choose_sovereign_exaction
- gods_of_africa_choose_strategic_ambiguity

This list combines five participant response decisions with three host doctrine decisions. Those are separate decision contexts and do not form one selection race. The adapter reports willingness scores, not click probabilities. No normalized denominator or exact selection probability is available.

The unweighted activation gate is gods_of_africa_continent_is_secured in common\scripted_triggers\012_africa_gods_epoch_binding_triggers.txt:54-66. Its current logic has two branches:

1. The Scramble phase is settled and africa_scramble_response_defeat is absent.
2. africa_triggerable_scenario_applied is set, africa_triggerable_scenario_type exists, and that type equals world_is_one.

The explicit has_variable check guards the type comparison against an absent input. The initial continental-settlement receipt alone does not satisfy this secured-continent trigger.

The SCN-011 Africa Is One opening in common\scripted_effects\012_africa_triggerable_scenario_effects.txt:228-243 seeds africa_first_proof_succeeded only if africa_focus_first_proof_satisfied is false, clears africa_first_proof_pending, records africa_evolution_i_logged, and calls africa_gods_of_africa_begin_consolidation. It does not replay the proof reward package. The World Is One opening follows its own terminal-campaign setup and does not call that initializer.

The normal Evolution I route calls the same owner-local initializer from common\scripted_effects\012_africa_evolution_effects.txt:51. The final continental milestone also retries it at common\scripted_effects\012_africa_focus_route_effects.txt:2317-2319, covering the case where Evolution I preceded formation. The initializer remains gated by current-host identity, the Africa Is One and Evolution I receipts, physical return, generation identity, and the existing consolidation lifecycle.

The settlement decision gods_of_africa_commit_settlement changed from target-array rows over gods_of_africa_participants to one host-wide row in common\decisions\012_africa_gods_decisions.txt:1636-1662. The current visible and available gates require a valid active host and a secured continent. Its completion effect calls gods_of_africa_commit_final_settlement. That effect rechecks current host identity, current epoch permission, active or pending state, the secured-continent gate, and the one-use final-settlement receipt before freezing and applying the settlement.

## Source identities and hashes

These SHA-256 values are hashes of local file bytes. The before copies are under docs\plans\012_africa_plans\subagent_handoffs\takeover_activation_probability_2026-10-06_evidence.

| Source | Before snapshot SHA-256 | Current SHA-256 |
| --- | --- | --- |
| common\scripted_triggers\012_africa_gods_epoch_binding_triggers.txt | 5afb48b7e53e2d1aa2f47fde96742add41f85c7203c94842093bdf674effb67e | 63ba5fa62d2ca8c2bd5562abde0cdf1c1cc53fd599f64efb8d36df4181e553e7 |
| common\scripted_effects\012_africa_triggerable_scenario_effects.txt | f6554dece95c091db2e7ed60f0fef647853b46107ca473f62a187d2878258197 | 3c515a4d0b17947e9d89709e49ef2b1260f2223ff1c87ace46fdf190030c0bd2 |
| common\scripted_effects\012_africa_focus_route_effects.txt | 8f57e66cb69a5768a25a2d8ca044a628fe45abf7dfd709f9395552bf1e29859f | dc220b4c80eb5c9150518a325dc3c810b1f5b80dfaed9e23c2245ce31d36c838 |
| common\decisions\012_africa_gods_decisions.txt | 03e124a014d54d59539db8e4bdf4693d3f071df79207d50f05751978fa715fd5 | 5515165dea18746734df2d50c7005d1a9c163b3afe015b2dce00967b3e4a7d45 |
| common\scripted_triggers\012_africa_gods_recovery_triggers.txt | 3664ab41fa1bfc62eca631c5e1618cfa94e3e3dda7568d0c749c816e5e34369c | c9f9073f3969b3c18a9a1d17048512a332723722ec5e509fbee85b583b01ecd1 |

Current supporting source hashes:

| Source | Current SHA-256 |
| --- | --- |
| common\scripted_effects\012_africa_gods_effects.txt | f9fcb0d37264eb6e10e64ca8b774226c17804170fae194bf616f4155aa00d51 |
| common\scripted_effects\012_africa_gods_recovery_effects.txt | 14affd56c1200bd1289b00973ba151158b686065e42b13421b8ecbd2dae562a2 |
| common\scripted_triggers\012_africa_gods_triggers.txt | 5f8e6ff91f20ab804d6f6900120defee82a99f85ac04a734b8f5939e260e687b |
| common\scripted_triggers\012_africa_world_order_triggers.txt | 51a995d3b83109798862216b475124e328b28e304b6934ee677de3e5facd7a23 |
| common\scripted_effects\012_africa_world_order_effects.txt | 2035e3f7c33f3cfe4b265712cae708d18706d74724dc76ee8cbdf92efac5e41c |
| common\scripted_effects\012_africa_evolution_effects.txt | 81a3be56dc3b931588cb11b246777b0971851fc994bffb00a9cc72bf04da7c4e |
| common\script_constants\chaosx_triggerable_scenarios_constants.txt | 2780386117cf4cbf608374fcd83ca0bb7ef49eab687ad4ca9534acc207c96889 |
| common\script_constants\012_africa_world_order_constants.txt | c902dd4d8a10f4de871d6b5e4db5fd784d947f34f942d77cd67e199c792ed6ed |
| common\script_constants\012_africa_gods_constants.txt | be9f4d3cd489b86d6dca14b213d8d02fd48b42020228dd209f0f8098a14d563e |
| common\script_constants\chaos_meter_constants.txt | 3afc88033de79f3abb0d173c82aaef6130fbf0846cd012a575ca00b73bde1b4a |
| events\012_african_union.txt | c3e0390e6a5a6193d6fc04defdccb6e0267b36c66734e78d5221de7eceee288d |
| events\012_africa_evolutions.txt | 07dc1a8c148294e9f653dc3f7b56b1f6e8435efdc075d25c91c3ae64aab593a7 |

The final epoch-binding trigger hash is 63ba5fa6…e553e7. The older takeover_activation_gate_evidence_2026-10-06.json records 87395b637f64f75cffc7da3e2e8890dbaaa7e32588cd0ee0da6f32556e8113df as that file's after hash, so that metadata is stale. The current recovery-trigger file differs from its before snapshot only in a comment describing the secured-continent witness; its executable lines match the snapshot.

The MCP source-lookup revisions were 3f911766206b8ad0177db44392c529887916357cc3a5cfeef135fa6b643d78ed for the secured-continent trigger, c9f0c03902e82d6565ad7dba435bd484c839d8bbe242da14edf4839877219c68 for the final-settlement effect, 4b4092c94a3a94b8330429b6c7a1d9f6ada3e6b062f89200d201d24f8930e149 for the milestone helper, and 923e002b903fa4cc90fb4a4f07fd1835795f3d325dd68397b9aa4aa40c319b35 for the current settlement decision block.

## Probability evidence

The final read-only probability_inspect used adapter decision_ai_will_do, source common\decisions\012_africa_gods_decisions.txt, and the exact eight IDs above. It returned PROBABILITY_SOURCE_INSPECTED in workspace mod_chaos_redux_ea3b2d67c2c0, source hash 5e5c14392d42ceb3c7f6419dbf7637284c0502725362fa4fca0b46387ebbf6e6, and source revision 6dd57587d9948c0ab62f080b08bd273c98f001bf8a712317f2d384b8eccd18a8. It reported eight requested candidates, poolComplete=true for that supplied list, required inputs has_war, scope.any_of_scopes, and variable.global.chaos_meter_value, and zero unresolved inspect entries. This source inventory does not establish scenario eligibility or a complete live decision pool.

The current inspect artifact is hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/86c712d08cb3f2b884bfde1d5c844ebc4572068daf88840fdcf14411cce3fe7c/dadad3567d68de227b0d349b16629aa7dae5a95a518aeed474fe5c1925265dce/probability-inspect-5e5c14392d42.json.

Source-defined base inputs for the requested decisions are visible even though no final scenario trace returned:

| Decision | Source-defined base |
| --- | --- |
| gods_of_africa_comply_demand | gods_of_africa_ai_response.comply_base = 50 |
| gods_of_africa_substitute_demand | 0; the source labels this as a player shortcut while AI uses separate substitute-slot decisions |
| gods_of_africa_negotiate_demand | gods_of_africa_ai_response.negotiate_base = 20 |
| gods_of_africa_refuse_demand | gods_of_africa_ai_response.refuse_base = 5 |
| gods_of_africa_permanent_defiance | gods_of_africa_ai_response.defiance_base = 2 |
| Each of the three doctrine decisions | gods_of_africa_ai.doctrine_base = 10 |

The source-defined doctrine modifiers are reciprocal peace 3 and cooperation 1.5, exaction war 3 and occupation 2, and high-Chaos ambiguity 4. These are source constants, not evaluated composite scores. The final adapter returned no numeric modifier trace or ranking.

The comparable scenario set in the prior handoff is 012-GODS-ACTIVATION-ELIGIBILITY-2026-10-06 with hash 2ded6efe59930a96a50f2a69aabc8b1b61fdd18706dfdaafc0cc100035d91e96. Its named scenarios are INITIAL_UNIFICATION_UNSETTLED, FINAL_SUCCESS, FINAL_DEFEAT, and LOST_CAPITAL. The recorded fixture uses actor AFR, has_war=false, chaos_meter_value=0, and the Africa Is One and Evolution I receipts. The scenario definitions leave participant and host scopes, the africa_host event target, authority variables, and active-decision context unbound. LOST_CAPITAL also lacks the capital state ID, owner, and controller.

I submitted those same four scenario IDs with the reported values and the same eight candidate IDs. The raw originally saved scenario payload is not present in the handoff or before-source snapshot directory, and neither final evaluation returned a scenario hash, so exact input-hash equivalence to 2ded6efe…d91e96 could not be confirmed.

Both final probability_evaluate calls timed out at the MCP's 600-second limit. The first requested raw values, ranking, matrix, and unresolved output. The single retry kept the same source, scenarios, and candidate IDs while reducing output to JSON and unresolved traces, and it also timed out. Neither call returned an analysis ID, score traces, rankings, unresolved counts, scenario hash, or artifact.

Both same-scenario probability_compare calls also timed out at the 600-second limit. They compared the exact before snapshot of common\decisions\012_africa_gods_decisions.txt against the current source with the same four scenario IDs and eight candidate IDs. The retry requested only comparison and unresolved outputs. Neither returned a comparison ID, numeric delta, or artifact.

There is no final after-analysis ID to pass to probability_render. The prior baseline and intermediate artifacts are retained for context only, and the intermediate results are superseded by the current epoch-trigger hash:

- Baseline inspect: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b00803d589c054c3de18b68aa7e29d4ef9b27cfc1fe92f331ff52dcde5d5c27d/40bdffc70c687a350233daffac657b13facdda2f6e2feabea5badde1059ee0e9/probability-inspect-bab09cc57f21.json
- Baseline evaluation, analysis probability-e8e4c7c626fb350f6c52e89c, source revision 5534074a3d8661c478e5484bb3ff6273a5c825fcce3882e92c186730020c8a2d, scenario hash 2ded6efe59930a96a50f2a69aabc8b1b61fdd18706dfdaafc0cc100035d91e96: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5bdba4d9b2ff62622df6f5d36275d89f5799161404cda677ab67367201eaa5e5/5348d064432378c988a0b13fd03ee888a583b2c5f069d100e776e48755544f9d/probability-e8e4c7c626fb350f6c52e89c.json
- Baseline ranking render: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a4bd854679cbe273db2999f63b7f6ff4042f955d73f2e314c33dbff8f6537da1/1c83b266d7b1530890e218c8defe86e772875cab08a023c26cc98598b9c14c11/probability-probability-e8e4c7c626fb350f6c52e89c-ranking.svg
- Baseline unresolved render: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/27f7513f6f8fa75d8df80e0f2b9e05c8c8222fee23a61f0f564fe1c419a2fb51/6c513843b325b7ee2a154683a5dcfdd28f5ea207946007c85c30340bca4ce690/probability-probability-e8e4c7c626fb350f6c52e89c-unresolved.svg
- Superseded intermediate evaluation, analysis probability-cf4e80b5aa53760d66d0d8ab: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9cd9be4ceb7c05a2d0ec8fec83a8967d4929f3254539a72425d0bffc49f1a072/abdac7019f416db28fdf099f8aacd27fc77b6849b34e7898ee5cd476d041132b/probability-cf4e80b5aa53760d66d0d8ab.json
- Superseded intermediate ranking render: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3e338a3ff9c22af58580e649e8fa45413474d35f46faa24b64c56c6a6076ee0d/1a6937f0ed78609f40d5b1fcde2298f151ecb820059fa0e55dd5c7ff6b6436ae/probability-probability-cf4e80b5aa53760d66d0d8ab-ranking.svg
- Superseded intermediate unresolved render: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/27f7513f6f8fa75d8df80e0f2b9e05c8c8222fee23a61f0f564fe1c419a2fb51/74fddf756712bc52271922b6be74c919511b9692fdc523774f5dbb8ce58b05e9/probability-probability-cf4e80b5aa53760d66d0d8ab-unresolved.svg

The prior baseline evaluation reported 32 indexed candidates, 12 eligible, 20 excluded, 716 unresolved trace records, and zero unresolved candidates. It returned no normalized probability or complete live race. Its compact report did not include numeric base and modifier traces for all eight requested choices. The prior fixture made the exaction war modifier and high-Chaos ambiguity modifier false because has_war was false and chaos_meter_value was zero. Those are baseline fixture observations, not campaign starvation or dominance findings.

The inspected list is not the complete live pool for any one decision category. The five response choices and three doctrine choices are separate surfaces, and participant target context remains absent. The actual selection denominator is therefore not available. Equal aggregate counts in the intermediate evaluation do not prove a zero delta.

Per the parent source review, no AI base or factor was changed. Source inspection shows gods_of_africa_commit_settlement currently has ai_will_do base=1, but that identifier was not in the prior eight-candidate probability model. No numeric before/after score or click probability is claimed for the host-wide settlement action.

## Classification and risk findings

Evidence classification: current source identities and trigger expressions are exact. The activation and settlement interpretations are bounded source evidence under the declared fixtures. The prior AI result is partial and score-only. Final after evaluation and numeric comparison are unresolved. No sampled result was produced.

The secured-continent branch logic is bounded source evidence, not observed campaign state. Successful-settlement classification depends on the settled Scramble phase and absence of the defeat flag. The World Is One branch depends on both the applied receipt and the typed scenario variable, with the existence guard preventing an absent value from matching.

The SCN-011 first-proof seed and normal milestone retry are bounded source evidence. The seed preserves chronology without replaying rewards, and both ordinary ordering paths call the same idempotent initializer. The 180-day consolidation clock is a date-based source mechanic, not an MTTH distribution analyzed here.

The settlement decision's change from participant-target rows to one host-wide action is exact in the current source. The current effect keeps one-use and current-epoch guards. Its AI ranking remains score-only and unmeasured against a complete host-category pool.

No final dominance, starvation, rank reversal, repetition rate, snowball, or exploit probability is established. The current AI evaluation and comparison did not return. Source guards support one-use final settlement, but they are not a runtime repetition measurement.

## Structural and validation evidence

Focused event inspection for selector event chaosx.nr12.1 returned JOB_WORKER_EXIT on both the trace and narrower retry, with no graph artifact. The one overview render request for that event produced no response or artifact within about 93 seconds, so I stopped waiting. No event graph comparison was attempted because the event source file is unchanged and no graph-bearing inspect artifact was returned.

script_validate on the full epoch-binding trigger file returned SCRIPT_CHECK_PARTIAL with valid=null, 44 commands checked, 10 argument blocks unchecked, six unknown-scope roots, and zero findings. An explicit country-scope snippet request returned SCRIPT_CHECK_PARTIAL with valid=null because the validator treated the top-level scripted trigger name as an undocumented native command and checked zero commands. Neither result is a full engine validation.

The final source hashes were independently rechecked after the parent reported the stable epoch-trigger hash. No gameplay or Git changes were made during this audit.

## Documentation references

| Source | Section and lines | Revision |
| --- | --- | --- |
| Offline AI modding wiki | MTTH blocks, 26-37 | 917cd261f7da51fe4d8687c5d7663e768a09c5c101ac130ce646bc64637aa818 |
| Offline Decision modding wiki | AI, 357-374 | 7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162 |
| Offline Decision modding wiki | Target checks, 519-530 | 7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162 |
| Installed common\decisions\_documentation.md | Country Decisions, 1-46 | 5e7e686b5582f32c38d898d805e17171e88f3bfeee4a030deb1884f9726de019 |
| Offline Triggers wiki | has_variable and check_variable, 570-571 | abc51ad18a2c46e46d47baa795c5a840ebaf7c4ae3e777426c64a9f4c0c0ce06 |
| Installed documentation\triggers_documentation.md | check_variable, 2110-2134; has_variable, 5006-5014 | 7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29 |
| Offline Data structures wiki | Event targets, 263-269 | 62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4 |
| Installed documentation\effects_documentation.md | save_event_target_as, 6496-6504 | 2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af |

These sources distinguish AI score races from probability-proportional event-option sampling, describe target scope for the old decision rows, and document the variable-presence guard used by the current trigger.

## Recommendations and remaining blockers

1. Preserve the has_variable guard and exact world_is_one type check in gods_of_africa_continent_is_secured. Do not treat africa_continental_settlement_complete alone as final security.
2. Preserve the conditional SCN-011 first-proof seed and the normal milestone retry to africa_gods_of_africa_begin_consolidation. Keep the physical-capital and current-host checks in the canonical initializer.
3. Keep gods_of_africa_commit_settlement as one host-wide finalization action guarded by gods_of_africa_continent_is_secured, and retain the one-use checks in gods_of_africa_commit_final_settlement.
4. If the host settlement AI score is intended to be tuned, centralize its literal base in common\script_constants\012_africa_gods_constants.txt and evaluate it only against a declared complete host-category pool. This audit does not select a new numeric target.
5. Refresh the after hash recorded in docs\plans\012_africa_plans\takeover_activation_gate_evidence_2026-10-06.json when the owner updates that evidence file.
6. Once the probability route responds, rerun evaluation, comparison, and rendering with the saved raw scenario payload, the same four IDs, and the same eight candidate IDs. Record the returned scenario hash before treating it as an exact reproduction.

Skipped: probability_sweep because this repair changes eligibility and call scope, no AI threshold or numeric factor was declared for tuning, and no sweep range was supplied. probability_simulate was skipped because no uncertain-input distribution was declared. probability_sequence was skipped because this is not a declared custom weighted pool. Final after rendering was blocked because no final analysis ID was returned. The event graph compare was skipped because the event source itself was unchanged and structural inspect/render supplied no graph artifact.

Skills used: chaos-redux-subagents, chaos-redux-events, chaos-redux-decisions-missions, and chaos-redux-event-planning. No skill was created or updated.
