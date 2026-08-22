# Famine and Migration AI Probability Post-Audit

Audit date: 2026-08-22.

This is a read-only post-implementation audit of the shared famine and migration weighting surface. No gameplay, AI, event, decision, scripted-effect, scripted-trigger, constant, localisation, or runtime file was changed by this audit.

## Audited source surface

- `common/decisions/famine_migration_decisions.txt`: category `chaosx_famine_migration_category`, 26 weighted decision blocks, and three non-weighted mission blocks.
- `common/script_constants/famine_migration_constants.txt`: `famine_migration_decision_ai` bases and factors at lines 638-736, plus threshold and population constants.
- `common/scripted_triggers/chaosx_famine_migration_triggers.txt`: country, state, route, destination, border, return, blockade, and validity predicates.
- `common/scripted_effects/chaosx_famine_migration_effects.txt`: registries, cohort movement, reception accounting, cleanup, return, integration, and resettlement helpers.
- `common/scripted_effects/famine_migration_adapter_effects.txt`: adapter-facing setup and state helpers.
- `common/on_actions/chaosx_famine_migration_on_actions.txt`: bounded lifecycle callbacks and CXT registration hooks.

The package has no `ai_chance`, MTTH, `random_list`, AI-strategy factor, focus-selection, research-selection, technology, doctrine, or declared custom weighted-pool surface. The `random_country` startup hook is CXT test registration and is not a weighted candidate pool.

## MCP provenance

The first requested `decision_ai_will_do` inspection returned `PROBABILITY_SOURCE_DISCOVERED` with no matching decision adapter and suggested `mission_ai_will_do`.

- Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1ad8c0e72a2e05acc167aae15d056f924a71151272da7393ad4213359d8ea68f/a8874c96c61c91ce48820d28a3823589b734dea1b98f0a5bff98bdf8e476a9a1/probability-inspect-1db38e3d69f6.json`
- Source revision: `3fb9458c4a66cda9ee48414f476fbe5cee249136065a6fa3b4e9794c1a44219f`
- Source hash: `1db38e3d69f6be4b7c21e967c044b245fc5dd04dda26abafa22935e161fa6791`

A no-candidate-pool `mission_ai_will_do` retry timed out after 180 seconds. The explicit 26-candidate retry succeeded.

- Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2f1eea6ee84ee0fcbe91b0136def4f264f426b26117c7f8a75b1f4cc4dbde44e/e7b971832266a3a3aabfd14239fc2c0823034e8866b071ae5ebd2a84cc51a173/probability-inspect-1db38e3d69f6.json`
- Source revision: `883d9605a0e623714e3fb9f5739ad980df4c95a186531ccf112c8374702a5e8a`
- Source hash: `1db38e3d69f6be4b7c21e967c044b245fc5dd04dda26abafa22935e161fa6791`
- Result: `PROBABILITY_SOURCE_INSPECTED`, `poolComplete=true`, 26 candidates, 12 required inputs, zero inspect-unresolved inputs.

The final current inspection was also successful.

- Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e291df9e026a268d85629ad9ffbca80b1afdecdc2b1b941df247495bac8c73a8/789f4c520bc0d1427ed53e779d3e783483625cb0ef2229b8fe34e17a1969ef7c/probability-inspect-c874297e02df.json`
- Artifact SHA-256: `e291df9e026a268d85629ad9ffbca80b1afdecdc2b1b941df247495bac8c73a8`
- Source revision: `ffc3f6cec9e8add82503dd042c1340f02b1655f3c31a2cd96571fa019cd0f369`
- Source hash: `c874297e02df691eda7e9bea00a87d1352e3f9a60b5c747573d493d79ce8bb3d`
- Result: `PROBABILITY_SOURCE_INSPECTED`, `poolComplete=true`, 26 candidates, 12 required inputs, zero inspect-unresolved inputs.

The adapter is Operation Postern 1.19.2.0 (d245), with `rawScore=true`, `normalizedProbability=false`, `selectionRule=score_only`, and no time-distribution conversion. Mission scores are willingness scores and are not click probabilities.

For the linked resource inventory below, the first artifact path component is the artifact SHA-256 unless a separate SHA-256 is stated in the corresponding result block.

The one-scenario probe used before the full matrix was:

- JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/787be81c83a1721fe68a51d943bbd7264e42f1bfd09f3429ad498d7aac1ce3d3/6a11559ff68e5e6357e8ac501f1398ca9dd42cc9a7ac8433460f0ad3a98bb748/probability-57af9fd2bd8ee4a68fa43ae3.json`
- Ranking SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/03b9f5cf5b948dfae4c92a20b4c21ed0a1612b964e7498f0db08ffe7cd6a15f/574c92540b135a78849075938680cdbdbf7d3197aa8bdfc3f797ebfc447945f3/probability-probability-57af9fd2bd8ee4a68fa43ae3-ranking.svg`
- Matrix SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/26b98bfdd9ffdee32cae7052f69dccb4bcc9e98dfe49a063d9bf1a5c2df120b2/4c88618f18c92f9635e34ec7dca9fbe15bb9aeb1184502622d398eff34346ddd/probability-probability-57af9fd2bd8ee4a68fa43ae3-matrix.svg`
- Unresolved SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3bbf83b09de5fecbbc42c0505cf2d302239700fc8f4868ce800fa2a8e8f1b9f6/3bc505ab100fab1e8d62e8e0918134200fa71cd0c38182970eed6bd3d6d42174/probability-probability-57af9fd2bd8ee4a68fa43ae3-unresolved.svg`
- The probe also emitted PNG resources, but those long display names were truncated by the MCP response and were not used as authoritative evidence.

## Candidate identifiers and base values

The source-backed bases are the following `famine_migration_decision_ai` entries.

| Candidate | Base |
| --- | ---: |
| `fm_prepare_evacuation` | 5 |
| `fm_open_departure_routes` | 8 |
| `fm_restrict_departure` | 1 |
| `fm_close_border` | 1 |
| `fm_release_reserves` | 12 |
| `fm_emergency_imports` | 9 |
| `fm_repair_relief_route` | 14 |
| `fm_escorted_relief_convoy` | 16 |
| `fm_emergency_airlift` | 8 |
| `fm_invite_relief` | 7 |
| `fm_famine_evacuation` | 10 |
| `fm_evacuate_vulnerable` | 13 |
| `fm_evacuate_workers` | 8 |
| `fm_requisition_safer_state` | 5 |
| `fm_conceal_crisis` | 1 |
| `fm_maintain_extraction` | 2 |
| `fm_negotiate_corridor` | 12 |
| `fm_open_reception` | 10 |
| `fm_controlled_medical_reception` | 14 |
| `fm_distribute_arrivals` | 9 |
| `fm_transit_only` | 6 |
| `fm_enforce_closure` | 1 |
| `fm_local_integration` | 12 |
| `fm_third_country_resettlement` | 7 |
| `fm_voluntary_return` | 10 |
| `fm_forced_repatriation` | 0.2 |

The source uses factors for war, government ideology, famine pressure, displacement, reception load/capacity, exposure proof, evacuation preparation, blockade proof, and civilian-factory or air-experience gates. The analyzer reported that several factor branches were not active in any supplied fixture: `fm_close_border.factor_2`, `fm_conceal_crisis.factor_1/2`, `fm_controlled_medical_reception.factor_1/2/3`, `fm_enforce_closure.factor_1/2`, `fm_forced_repatriation.factor_1/2`, `fm_maintain_extraction.factor_2/3`, `fm_open_departure_routes.factor_2`, `fm_open_reception.factor_1`, `fm_restrict_departure.factor_2/3`, and `fm_voluntary_return.factor_3`.

## Twenty-scenario evaluation

`hoi4.probability_evaluate` completed as `PROBABILITY_ANALYZED_PARTIAL` for scenario set `FM_POSTIMPLEMENTATION_20_2026_08_22`.

- Analysis ID: `probability-27f3952bc314506bb9f685f5`
- JSON artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ad819f65fad7b1d96cf62ad5ec0bb8491aed28a1343178f0298c81067f308978/ff7122146a44b03e4defe5c2c5181ad4793eacb387192a62e2cb7738d153465a/probability-27f3952bc314506bb9f685f5.json`
- JSON artifact SHA-256: `ad819f65fad7b1d96cf62ad5ec0bb8491aed28a1343178f0298c81067f308978`
- Source revision: `532b9a2568183e805158fd8d777fcebb362c062bee26f470bc2ec3f5659f3245`
- Source hash: `c874297e02df691eda7e9bea00a87d1352e3f9a60b5c747573d493d79ce8bb3d`
- Scenario hash: `c72e02ef3aeaf7a48001c6d656e2898e18bab63387269eddbcb9f975275a6f67`
- Candidate pool hash: `90d337c26916e9db69c4e41327367942fd5139b29f25c52824e71858e04bfda9`
- Rows: 20 scenarios × 26 candidates = 520.
- Unresolved: 59.
- Diagnostics: 20.
- Every scenario contained 23 `unresolved` candidates and 3 explicit `false` outcomes; no scenario had a proven eligible candidate.

The following are bounded score-only rankings. They are not normalized probabilities and must not be read as executable AI selection outcomes while eligibility remains unresolved.

| Scenario | MCP status and bounded ranking |
| --- | --- |
| `prob_famine_relief_dense` | Partial, 23 unresolved/3 false; `fm_open_reception` 30 > `fm_controlled_medical_reception` 14 > `fm_open_departure_routes` 8 > `fm_restrict_departure` 1 > `fm_close_border` 0.2. |
| `prob_famine_relief_blocked_island` | Partial, 23 unresolved/3 false; `fm_open_departure_routes` 16 > `fm_controlled_medical_reception` 14 > `fm_open_reception` 6 > `fm_restrict_departure` 3 > `fm_close_border` 0.6. |
| `prob_soviet_extraction` | Partial, 23 unresolved/3 false; `fm_open_departure_routes` 16 > `fm_controlled_medical_reception` 14 > `fm_close_border` 3 = `fm_restrict_departure` 3 > `fm_open_reception` 2. |
| `prob_humanitarian_border` | Partial, 23 unresolved/3 false; `fm_open_reception` 30 > `fm_controlled_medical_reception` 14 > `fm_open_departure_routes` 8 > `fm_restrict_departure` 1 > `fm_close_border` 0.2. |
| `prob_capacity_exhausted_border` | Partial, 23 unresolved/3 false; same bounded ranking as `prob_humanitarian_border`. Capacity exhaustion was not resolved by the flat fixture. |
| `prob_outbreak_reception` | Partial, 23 unresolved/3 false; same bounded ranking as `prob_humanitarian_border`. Exposure and reception validity remained unresolved. |
| `prob_nuclear_evacuation` | Partial, 23 unresolved/3 false; same bounded ranking as `prob_famine_relief_blocked_island`. Fallout and return-route validity remained unresolved. |
| `prob_genocide_escape` | Partial, 23 unresolved/3 false; same bounded ranking as `prob_famine_relief_blocked_island`. Persecution and target ideology remained unresolved. |
| `prob_authoritarian_pushback` | Partial, 23 unresolved/3 false; `fm_open_departure_routes` 16 > `fm_controlled_medical_reception` 14 > `fm_close_border` 3 = `fm_restrict_departure` 3 > `fm_open_reception` 2. |
| `prob_destination_selection_internal` | Partial, 23 unresolved/3 false; same bounded ranking as `prob_humanitarian_border`. Internal destination safety was unresolved. |
| `prob_destination_selection_persecution` | Partial, 23 unresolved/3 false; same bounded ranking as `prob_famine_relief_blocked_island`. Destination persecution validity was unresolved. |
| `prob_corridor_acceptance` | Partial, 23 unresolved/3 false; same bounded ranking as `prob_famine_relief_blocked_island`. Corridor geometry, observers, and military cost were unresolved. |
| `prob_forced_return` | Partial, 23 unresolved/3 false; same bounded ranking as `prob_humanitarian_border`. Origin safety and return route were unresolved. |
| `prob_integration` | Partial, 23 unresolved/3 false; same bounded ranking as `prob_humanitarian_border`. Duration, host capacity, and terminal integration state were unresolved. |
| `prob_opposition_channel` | Partial, 23 unresolved/3 false; same bounded ranking as `prob_famine_relief_blocked_island`. Opposition ideology and movement validity were unresolved. |
| `prob_disaster_flight` | Partial, 23 unresolved/3 false; same bounded ranking as `prob_humanitarian_border`. Damage severity, route, cohort, and cooldown were unresolved. |
| `prob_bombing_exodus` | Partial, 23 unresolved/3 false; same bounded ranking as `prob_famine_relief_blocked_island`. Raid persistence, shelter mitigation, and active-cohort cooldown were unresolved. |
| `prob_requisition_donor` | Partial, 23 unresolved/3 false; same bounded ranking as `prob_humanitarian_border`. Donor safety, surplus, occupation, and famine protection were unresolved. |
| `prob_relief_donor` | Partial, 23 unresolved/3 false; same bounded ranking as `prob_humanitarian_border`. Reachability, stock, relations, and receiving capacity were unresolved. |
| `prob_cleanup` | Partial, 23 unresolved/3 false; same bounded ranking as `prob_famine_relief_blocked_island`. Registry cadence, removal, reset, reload, destination loss, and duplicate-debit state were unresolved. |

The ranking SVG, matrix SVG, and unresolved SVG emitted by this evaluation are:

- `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/38a557b683d1c6bb7afe42b7beeac161fe64b9b193546a88c34ad997a2cf3a9d/3fa050b96e57417a6832301cd83e9a7719be0f11c5abfbcf29e6d1eda752c422/probability-probability-27f3952bc314506bb9f685f5-ranking.svg`
- `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/dead2b9c768aff284c69544b99bac3acf2e1a4747394607a23a54216c152cda5/615581ebb12c7fe397a35fbc8b93f2b64e508efb25a960562bf64ba6a8664fe8/probability-probability-27f3952bc314506bb9f685f5-ranking.png`
- `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2069718f73aea881d6c8ec6567c52534834bd3cdc2113a0545f1777976725bc2/3ce871be563d043010da042f343ce94673c07d0167971fb9c653ab6ed462a49e/probability-probability-27f3952bc314506bb9f685f5-matrix.svg`
- `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/20132371fa5951a0664a7f38b71d578c17a5eb7973c403d1510e0e637fcd86cb/00abaf9de4bd8926d73a124d0b8183f50d8e28744bec75985c880c9493d91ac3/probability-probability-27f3952bc314506bb9f685f5-matrix.png`
- `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/af2d224665dc6f88dab9f0bb64d2dcc55dfb674552990b9bd43c8db6c88d5127/3d0cce6e4bb1edb6ca27209bd119d531d1d27e57f76b55fffa1ba8748a695293/probability-probability-27f3952bc314506bb9f685f5-unresolved.svg`
- `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/86f3fcbe45ab8e3349681fef450d80b2ab101ec0c330270a4a3560c0f8d4e804/20263d7f0cd2f5b686b6bfca969ecb788bcc295c50d1a7437b3302375422ea84/probability-probability-27f3952bc314506bb9f685f5-unresolved.png`

## Sweep evidence

The successful sweep used the flat numeric path `famine_migration_food_pressure` over the same 20 scenario IDs and returned `PROBABILITY_ANALYZED_PARTIAL`.

- Analysis ID: `probability-e5e77d07e1a716315c92d64f`
- JSON artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7c2a9053de6f798e2de04a4b3e997039a7571e1ae8db5c8213446b9e8ea5d463/42f3802fc1348b348f870d86252a363a629ee9711c2afbd4fd713ebd2325574f/probability-e5e77d07e1a716315c92d64f.json`
- JSON artifact SHA-256: `7c2a9053de6f798e2de04a4b3e997039a7571e1ae8db5c8213446b9e8ea5d463`
- Source revision: `bacd07510bce5d9133e56306cdf60cdeccc13998aa92670486deb4a898f0879a`
- Source hash: `c874297e02df691eda7e9bea00a87d1352e3f9a60b5c747573d493d79ce8bb3d`
- Scenario hash: `9dd7c6d8127e54f2c84459cfee92c2fffe664355248d19e55b9985e520ea8335`
- Sweep points: 20.
- Unresolved: 59.
- Breakpoints: none.
- Rank reversals: none reported.

Sweep render resources:

- Ranking SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7f709bb0a443d0c2a08bc10b2644e744242e2dad92f077baf25650fa28217a73/fdbff947e0e29419096e965d6feb200e3851f9679835a1860d3b1c73a91c756f/probability-probability-e5e77d07e1a716315c92d64f-ranking.svg`
- Ranking PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/027d3bfa9ac378327b3a9801586abf9e005d186bff94e62f23a1211fa44faf5c/fe3a7f3ce168b992fcb20ca3d18325eaf69b77579479448989a2c12cb1870207/probability-probability-e5e77d07e1a716315c92d64f-ranking.png`
- Sensitivity SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fdf655b29cae1e02a8de4e2afa6cf39af31ae6f42d9490cd371aa1053f369b58/504127eedcd175f78d67a6bb102b674d286b1b203c0275734d6b439c98b8401c/probability-probability-e5e77d07e1a716315c92d64f-sensitivity.svg`
- Sensitivity PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/64a7b6aa956f526d69280b0c8b416f12bd1ef9e6ed9f09e5d736fc9a0859f7ab/c1cdd71aea8782b9b32305ac1549c393f292e958d99e2f03357a22b73861fe75/probability-probability-e5e77d07e1a716315c92d64f-sensitivity.png`
- Threshold SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a6d32ffc270e06218fbe6e53b5f3d111d3f383d152a2e17fa057722f7cf35cc8/590cb367d5cd73d5fae4a9a3ab98909182ca3a4cdfd35f1ce7527ccf0d9ebbe1/probability-probability-e5e77d07e1a716315c92d64f-threshold.svg`
- Threshold PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b76acd470fd70e5eba53e1c69e5403c466b9e86517ed6cf501771449c31db8ae/f79d242e65a0415c7fafad0bdf85ee8c5ad4b1fed8991974d7ce3140faac1424/probability-probability-e5e77d07e1a716315c92d64f-threshold.png`
- Unresolved SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/af2d224665dc6f88dab9f0bb64d2dcc55dfb674552990b9bd43c8db6c88d5127/c4b60a5c2810bc4ed9da9d4a8daff5dd966c550f6a3aa25e9272b35348e369a8/probability-probability-e5e77d07e1a716315c92d64f-unresolved.svg`
- Unresolved PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/86f3fcbe45ab8e3349681fef450d80b2ab101ec0c330270a4a3560c0f8d4e804/c0d1861c1820d9988ddff2670d0ca14da97988bd6a9966e50a9d7de9347c4650/probability-probability-e5e77d07e1a716315c92d64f-unresolved.png`

The first sweep attempt failed exactly with `PROBABILITY_SWEEP_RANGE_REQUIRED` for `state.num_of_civilian_factories` in `prob_famine_relief_dense`. The successful flat-path sweep does not prove threshold behavior because the adapter accepted one supplied value per scenario rather than a complete declared range.

## Current/current comparison

The exact same fixture and scenario hash were compared against the current source path on both sides.

- Analysis ID: `probability-e7b9a0a14bc5741afdc6f63e`
- JSON artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6fa6b0695f2e8e83553b8266831a2c46babfd452c1534dcd728029a55c7f0f8c/a7fe0003e1dff35960086c0d13c6d5c683ae8592794ca98ee4ca007090328b51/probability-e7b9a0a14bc5741afdc6f63e.json`
- JSON artifact SHA-256: `6fa6b0695f2e8e83553b8266831a2c46babfd452c1534dcd728029a55c7f0f8c`
- Source revision: `88f8b8bd7a2219c9a4bcdeb4f70cffcfc0269391e6aa127bccadca56deecb41b`
- Source hash: `c874297e02df691eda7e9bea00a87d1352e3f9a60b5c747573d493d79ce8bb3d`
- Scenario hash: `c72e02ef3aeaf7a48001c6d656e2898e18bab63387269eddbcb9f975275a6f67`
- Rows: 520.
- Unresolved: 59.
- `comparisonChanges`: 0.

Current/current comparison render resources:

- Ranking SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c90b3a25aa37df615425ef55cb49b8755e21d4fb3130061ca354571a5ac47715/f2e5441020008302b310e74dc2c6f7197b06e6851ee2af5649674216d0a725d0/probability-probability-e7b9a0a14bc5741afdc6f63e-ranking.svg`
- Ranking PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/81ef7cd672cd3a8303303fccbbdde718979d1d407c3417534922e3c790d7df88/1bb8f74b4a7c661e26ddf88f39caa32a86b2fe9154939eb4b55526cdf6af06d3/probability-probability-e7b9a0a14bc5741afdc6f63e-ranking.png`
- Matrix SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2069718f73aea881d6c8ec6567c52534834bd3cdc2113a0545f1777976725bc2/00b254fa2c8778c3f7eb9fe7ff957490e9829aafdb22103298930614410b362f/probability-probability-e7b9a0a14bc5741afdc6f63e-matrix.svg`
- Matrix PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/20132371fa5951a0664a7f38b71d578c17a5eb7973c403d1510e0e637fcd86cb/8d3e2e302f9a360dd25a32240bf345069f4fe17fadcc96262738c517ab0b035f/probability-probability-e7b9a0a14bc5741afdc6f63e-matrix.png`
- Waterfall SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/49d5d8ea9e0fa5e5649370fd779cd116223d1a724f0ea1c8f3e68e6dab862c0b/b88b8c70336f5498df8c7d694f6b6c5ac591859f7d8f316cec21dfc25a0ff73c/probability-probability-e7b9a0a14bc5741afdc6f63e-waterfall.svg`
- Waterfall PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4d323f0de6f0d2e3a9ea92caf9095f370eec81069ba85325cd55c2e26341204d/5598db8ff3aecf57223b2b9e8785b319589bf4874375576c82341e23aca65df4/probability-probability-e7b9a0a14bc5741afdc6f63e-waterfall.png`
- Comparison SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2450d67f32f665574260ffbd84f57cc7db1a9cf58aca09b66d13c1108a27cc49/cda27c64e3ac00a6412c40959debef0b79891276935be31bbf2dada763eeb635/probability-probability-e7b9a0a14bc5741afdc6f63e-comparison.svg`
- Comparison PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a1fd8e11d21dd2414c85f7412d454fa53b5b857ed9fb09593caa20f6277f498f/037b34f05243dfaf140f935851ad43d3e8ff1caf3e9bfcf41630c49ee1f96baf/probability-probability-e7b9a0a14bc5741afdc6f63e-comparison.png`
- Unresolved SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/af2d224665dc6f88dab9f0bb64d2dcc55dfb674552990b9bd43c8db6c88d5127/5d8ea0399b7fb3008f74d0e07c80308d197e15ed2c04daebd4022b82354c86dc/probability-probability-e7b9a0a14bc5741afdc6f63e-unresolved.svg`
- Unresolved PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/86f3fcbe45ab8e3349681fef450d80b2ab101ec0c330270a4a3560c0f8d4e804/50c1cc3a4e5310fd983da37d7003d6f540e4bfb26aaf48233812dcda42781396/probability-probability-e7b9a0a14bc5741afdc6f63e-unresolved.png`

This is a capability receipt only. The pre-implementation baseline explicitly has no famine/migration source or artifact, so no genuine before/after balance comparison exists. The comparison ranking, matrix, waterfall, comparison, and unresolved artifacts are linked from the JSON result.

The source hash remained `c874297e02df691eda7e9bea00a87d1352e3f9a60b5c747573d493d79ce8bb3d`, while MCP recorded different workspace revisions for inspect (`ffc3f6...`), evaluate (`532b9a...`), sweep (`bacd075...`), and compare (`88f8b8...`). The artifacts retain these revision-specific provenance values; no cross-revision numeric claim is made beyond the stable source hash.

The explicit render call returned `PROBABILITY_ANALYSIS_STALE` with no new visual resources because the cached comparison was stale against the current workspace revision.

- Stale render artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0ffb8e31a3eceb4ed1ad9b62604595ba15b32686dac5fe7516930883f321114a/ef4a1fb1099b0125813d615b216faa9a9e8e2a9ba1dfdb9a943fc2a77f35cee2/probability-e7b9a0a14bc5741afdc6f63e.json`
- Stale render SHA-256: `0ffb8e31a3eceb4ed1ad9b62604595ba15b32686dac5fe7516930883f321114a`

## Event 149 and structural evidence

Local source review found no `events/149_immigrations.txt` and no famine/migration event chain to analyze. `hoi4.event_inspect` was run with a file selector and returned a partial workspace scan rather than a package event graph.

- Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8e091118337ec89bb2b673a415889731255de41515d47fe52a99e6514ba9cc11/2d569599cb0ce91a7c3bd27c88633f04ab6a783a1234abefa156fce2332a8f4f/event-scan-b98e7381a4c7.json`
- Artifact SHA-256: `8e091118337ec89bb2b673a415889731255de41515d47fe52a99e6514ba9cc11`
- Result: `EVENT_INSPECTED_PARTIAL`, revision `b98e7381a4c7db9af46cdd5bb023a2c6eea74810796e264fb775944e1b0f3138`, graph hash `ffe1cde28d833202b56283760f404da68ac6591c57e3edac9d9e0a06f0c23c81`.
- The scan reported 9,513 workspace events and 8,287 unresolved nodes, which is not evidence that Event 149 exists.
- `hoi4.event_render` was not run because no package event chain was present to render.

## Skipped analyses

`hoi4.probability_sequence` was skipped because no complete famine/migration registry or cohort manifest declares cadence, cooldown, cap, recovery, removal, reset, destination-loss handling, annexation handling, reload behavior, duplicate-debit protection, and terminal states.

`hoi4.probability_simulate` was skipped because no uncertain input distributions, correlations, samples, or seed were explicitly declared.

No focus, research, technology, doctrine, GUI, AI-strategy, MTTH, `ai_chance`, or random-list route was applicable to this package.

## Findings and classification

### Required before completion

- Provide an MCP-supported typed fixture for country, state, `FROM`, target, neighbor, and other-country scopes. The schema rejected nested `FROM` and `target` objects, leaving route, destination, donor, cost, capacity, ideology, exposure, stockpile, cooldown, and prerequisite state unresolved.
- Re-run the exact 20 scenario IDs with complete availability, target validity, route geometry, cost affordability, external modifiers, and terminal-state fixtures.
- Re-run sweep with explicit accepted numeric ranges and a real rank-reversal search.
- Produce a true baseline/current comparison after a baseline source artifact exists; current/current `comparisonChanges=0` is not post-patch evidence.
- Resolve whether the MCP diagnostics for `fm_conceal_crisis`, `fm_enforce_closure`, and `fm_forced_repatriation` represent unreachable implementation branches or only unsupported scoped fixtures.
- Declare and analyze the cleanup/custom-pool manifest before claiming cadence, recovery, cooldown, reset, removal, or terminal-state safety.

### Optional future

- Add seeded simulation only after uncertain external inputs are explicitly defined.
- Add sensitivity paths for capacity, air experience, factories, route cost, shelter mitigation, and cooldown once the adapter accepts ranges and scoped state.
- Render a fresh comparison after the source revision and scenario fixture are stable.

### Rejected by specification

- Exact selection percentages or normalized click probabilities for these `ai_will_do` scores.
- Treating score ranks as probabilities, timing distributions, or campaign frequencies.
- Treating source-only inspection or hand arithmetic as balance proof.
- Treating unrelated Event 078 `ai_chance` as famine/migration evidence.

No new balance targets were selected and no tuning values were changed.
