# Startup probability repair handoff

Date: 2026-09-13.

Status: read-only audit complete for the bounded Event 031 projections and partial for the remaining source surfaces.

This handoff records MCP evidence gathered before and after the owner syntax repairs that were visible during the startup repair tranche.

No gameplay, AI, event, focus, decision, mission, technology, doctrine, scripted effect, scripted trigger, or runtime file was edited by this auditor.

No balance target was selected and no numeric weight was tuned.

The live startup owner completed two fresh clean main-menu launches, but those launches do not replace the probability analysis below.

## Required references and audit method

The required repository guidance was read from `AGENTS.md`, `.agents/skills/chaos-redux-subagents/SKILL.md`, `.agents/skills/chaos-redux-events/SKILL.md`, `.agents/skills/chaos-redux-mtth/SKILL.md`, and `.agents/skills/chaos-redux-debug-playtest/SKILL.md`.

The required offline wiki pages were consulted from `paradox_wiki/`, including Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, and AI modding.

The relevant installed vanilla references were consulted under `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/`, including script concepts, constants, triggers, effects, modifiers, event, decision, and AI documentation.

The MCP workspace was `mod_chaos_redux_ea3b2d67c2c0`.

Every weighted audit began with `hoi4.probability_inspect` and used `hoi4.probability_evaluate` and `hoi4.probability_compare` when the adapter could bind the declared source and pool.

The bounded Event 031 comparisons use inline Clausewitz fragments with the original and repaired random-list keys aligned to the same synthetic line and entry positions.

The repaired fragments expose the dynamic key values as flat state fields because the installed probability adapter resolves those fields and does not resolve the equivalent nested `variables`, `temp_variables`, or `values` objects.

The inline fragments are source-linked projections of the actual weight blocks for adapter comparison, not gameplay files and not a claim that the adapter has parsed every surrounding effect in the full source file.

## Completed Event 031 evidence

The source is `common/scripted_effects/031_random_terror_effects.txt`.

The preserved baseline is `docs/testing/live_qa/20260913_main_menu_startup/baseline/scripts/common/scripted_effects/031_random_terror_effects.txt`.

The current raw local hashes observed during the audit were baseline `830CBE5F7812DCADA0450CCC4AA86164F80975EDDCD14021C6D8E5BECD4A6149` and current `0FFB0B284B492AE08213A0E29565ECFB91ED0F2A34F5653736CF97061A224096`.

The current file contains unrelated repairs in addition to the weighted-key changes, so the inline comparisons below isolate the requested random-list contract and do not attribute unrelated file differences to the weight repair.

The original full-source inspect returned `PROBABILITY_SOURCE_INSPECTED` with source hash `7329213b82a73ac20648ddb28f237bdbf3d8cf86ee28287c415594d479f5bdba`, source revision `cd6fd5a3ddc855d910a134ea72cdad490b83cb3547905ca289c95b286b884a53`, 43 discovered candidates, zero available candidates, `poolComplete=false`, and unsupported `MULTIPLE_CATEGORICAL_POOLS`.

The full-source inspect artifact was `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bc0c6ab75accff7f66bc0121205c2ade0023fb45162a35a7ea513ad0d1c9d1ee/ad6b675e6cc9d012da85423032320bbbba738d73c1fdf1998f67f19ad5625e91/probability-inspect-7329213b82a7.json`.

The direct current-source inspect found the repaired incident pool at `common/scripted_effects/031_random_terror_effects.txt:431.entry.1` through `.24` with source hash `101a27aa2c7e02ce918492115b30437e730e3978d774b90da961728cb24a0e71`, source revision `a617dbc03d8d941305c217ae6ca6f109daa6f68718cf78f36f7e0c33e5af86bd`, 24 candidates, and `poolComplete=true`.

The direct current-source pattern inspect found `common/scripted_effects/031_random_terror_effects.txt:1084.entry.1` through `.4` with the same current source hash and `poolComplete=true`.

The direct current-source raid inspections found the high pool at line 2819, the low pool at line 2834, and the mid pool at line 2848.

Direct current-source evaluations of these repaired dynamic keys returned unresolved `VALUE_UNRESOLVED` rows when the flat runtime key fields were omitted.

That unresolved result is an adapter limitation for a full-source dynamic fixture and is not treated as a successful engine probability result.

### Incident pool

The named scenario set was `CR_STARTUP_031_INCIDENT_VARIABLE_BIND_2026_09_13` with `RT_INCIDENT_POOL_READY` and `RT_INCIDENT_POOL_READY_REPEAT`.

Both scenarios declared `pool=incident`, `all_entries_eligible=true`, and all 24 flat runtime key fields set to their source values, with the second scenario adding `repeat_probe`.

The synthetic candidate pool was `proposed/inline-probability-source.txt:50.entry.1` through `.24`.

The source weights in entry order were `16, 12, 10, 8, 7, 7, 12, 10, 8, 6, 6, 5, 5, 5, 4, 4, 5, 4, 5, 4, 5, 4, 4, 2`.

The declared total was 158 tickets.

The baseline inspect returned `PROBABILITY_SOURCE_INSPECTED`, source hash `cee4f097b06f8cbf0415d850d25aac84255ce7bdd451e199a85ebed2dc3ad203`, source revision `278707a3b98d0dade182d71887282177136d47746f54cded33d1ac5612321642`, and a complete 24-candidate pool.

The baseline inspect artifact was `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2aa61282192357134d0d2065099bd1a3dc48a2a92aa7997bddc9e69aef8d12ca/f97def6310c3a9816d56149db80c3789228fe4e53fc317b7e5fd84c10957fcd9/probability-inspect-cee4f097b06f.json`.

The baseline evaluation was `probability-dfbe6a950dab84ea554d0e26` with scenario hash `8f06f4bf8c735b976af009ec4169e4ad1dd1d431b9a99334ecfc6c28785e7ec7` and JSON artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bcd5a613c7af3703a70dbefeb152da5eae5a39f29ecaee5e32ad576ed3af1c2c/10a77f6a9e905e3a924933f3eb7bf935b3890816d96c9236ab3a904db4563dfe/probability-dfbe6a950dab84ea554d0e26.json`.

The repaired inspect returned source hash `b33928add7b095cba521a902f9f6348583fc2fef45839b638ae535001aa4ec9d` and a complete 24-candidate pool.

The repaired inspect artifact was `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b327cb15c60d673625143e65b927dbde0cbecc08d332f292af4fe4de8f507067/26cc6361461511a7720d8b414246f7863b1efefe57ece45a2c3ec5c9cc499f53/probability-inspect-b33928add7b0.json`.

The repaired evaluation was `probability-6891a56e30420a2e858bd25f` with the same scenario hash and JSON artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/425cf82a5ebbe32e0fa6002255404e5d133d68f9f068a7e24eb31d74bc4d0903/da3a3c41a0efbcda958652adb9e493b9d7dc713b5322a2d9c0974ece194212ca/probability-6891a56e30420a2e858bd25f.json`.

The same-scenario compare returned `PROBABILITY_ANALYZED` as `probability-e9eb7eb422bb3e5e7abb2577` with the same scenario hash, zero unresolved rows, zero diagnostics, and `comparisonChanges=0`.

The compare JSON artifact was `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/72539948a77022baa6ffaeeb4625ffa04781d187b4b5c43c39eba780d79d3110/ad6bf88395004b44d61c88a1c19a7a16d2d726048731484ee20aab21db169c3b/probability-e9eb7eb422bb3e5e7abb2577.json`.

The rendered compare evidence was ranking `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f202592e520341de2567bb4c60d2afe5f9cd115cb32a6b4c3179d3ec1ed8b083/c70da2f7f050a9f3ebbf48f5752bf09887f36e22693460be552d620dbc8f862b/probability-probability-e9eb7eb422bb3e5e7abb2577-ranking.svg`, matrix `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c7183e2d0a25b3f56415b5915ba673ac4b528eb72d615b91617a14ee94a2f8b8/b98848da652d9dd3aef6802c9cdea744fb3e14689e4daa69bd93e744b8802610/probability-probability-e9eb7eb422bb3e5e7abb2577-matrix.svg`, comparison `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2450d67f32f665574260ffbd84f57cc7db1a9cf58aca09b66d13c1108a27cc49/2ab1d9e159c02ab248a44446b455bda82d46a0f7f22ee386d31202bf7f8482dc/probability-probability-e9eb7eb422bb3e5e7abb2577-comparison.svg`, and unresolved `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d6cc34de4a6f32afd16a90b09c5631e732e81cfd45199abec74fe2209cf8029b/1fb77ea6927d19d95378206990e23e17252fc90f3a8f1a815c0d1b832e91223f/probability-probability-e9eb7eb422bb3e5e7abb2577-unresolved.svg`.

The compare retained exact normalized values for the declared pool, including 16/158 = 8/79, 12/158 = 6/79, and 2/158 = 1/79 for the largest, next, and smallest source weights.

Classification: exact for the declared 24-entry inline pool and its flat runtime bindings, with no rank or probability change; unresolved for full live-source evaluation without those bindings.

### Scenario-pattern pool

The named scenario set was `CR_STARTUP_031_SCENARIO_PATTERN_VARIABLE_BIND_2026_09_13` with `RT_PATTERN_RANDOM_INPUT` and `RT_PATTERN_RANDOM_INPUT_REPEAT`.

Both scenarios declared `scenario_input_type=random_pattern`, `all_entries_eligible=true`, and `random_terror_draw_runtime_scenario_pattern=25`, with the second adding `repeat_probe`.

The synthetic candidate pool was `proposed/inline-probability-source.txt:3.entry.1` through `.4`.

The four source weights were 25 each, for a 100-ticket pool and a 25 percent normalized probability for every entry.

The baseline inspect returned `PROBABILITY_SOURCE_INSPECTED`, source hash `3c5ac3d6dc0933316d87eff0b1943472a3d653c32290358da1eaf6172b671dbd`, source revision `6ea7d2ad7b83565627b1c8f5009d0b49d48d3d30012e3c4946bc77e7bbbf07c4`, and a complete four-candidate pool.

The baseline inspect artifact was `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/372bff76ea46bdc1545ff8843906c3dffcd6e78e7103dfa92ce19584591e8665/f897f4cc7f4e51cb2443aaf7778f7e1e055c058d8c554b29cd924ccac55ed9b6/probability-inspect-3c5ac3d6dc09.json`.

The baseline evaluation was `probability-b58205af822597ff1a701b78` with scenario hash `b2b658809e347ebfd4127b5adb241efcc88d9100b3f50b18113de61a9282ea31` and JSON artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3211b4a9da53936e3acaaafebb44c44a08d7570a168949c6dd5d3d8e93cf9380/23eaa521c751dd6609f4b47f44784afc837d4d6523ec5f0e37cc88d9f82eaa16/probability-b58205af822597ff1a701b78.json`.

The repaired inspect returned source hash `67ccb62cf92d851397d3f28d9ac84a9156fff561e15cb56d0c561ea50d9468b3` and a complete four-candidate pool.

The repaired inspect artifact was `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5b36a6386a59e7c885af34ae29bd142231a70ca74baa39b51958107d03bdf8b7/64ea8f7e4c680b04b142f6281eaf9e47860f9f298e1ad151a47af1e5b829552a/probability-inspect-67ccb62cf92d.json`.

The repaired evaluation was `probability-a489ccb4068d9cc0da809de1` with the same scenario hash and JSON artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d53d9010f1d05bb93a355e6622128cecf31a8a5aafb60c28cf1174281dcdddb9/fa1a85a31faa0d0c779b2f49b43352d3856fbe734294c6c6957160c881ba7e5a/probability-a489ccb4068d9cc0da809de1.json`.

The same-scenario compare returned `PROBABILITY_ANALYZED` as `probability-7caf4cf652a4e36c80370dc2` with scenario hash `7c6254403101d05a707bf2a71a19884b615f5ab3a7bcdd35834d78e308881bf5`, eight candidate rows, zero unresolved rows, zero diagnostics, and `comparisonChanges=0`.

The compare JSON artifact was `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/76917b0704c68ef707d3547b22a6adf3906e5723d4a02c9c9bf1e95e6d6ad7dd/44b0497bc9df65d38721831796678f66f310eaba862f8c9bfc30eb9ed70c97bf/probability-7caf4cf652a4e36c80370dc2.json`.

The rendered compare evidence was ranking `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/81d6d22ed0be347a92061300d05a81592afc9ed994242cbf8b9dce5cb18cf82a/e1798910c9ba73c28acb81606979a632254b3885dd2c2b4072d2de3f60fd3e93/probability-probability-7caf4cf652a4e36c80370dc2-ranking.svg`, matrix `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5ffec0afdaa07a73242a03fbab2286ab4036b5ea2e7e281d4f95e3790c73fff9/7849cd683cee03ea02922b4c50542fca85ea95e9b00d9414396aceb19c8e31f9/probability-probability-7caf4cf652a4e36c80370dc2-matrix.svg`, comparison `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2450d67f32f665574260ffbd84f57cc7db1a9cf58aca09b66d13c1108a27cc49/14386995248c084f4de7320adec26f98f2d8200cb35c6d397e1b39edb1129130/probability-probability-7caf4cf652a4e36c80370dc2-comparison.svg`, and unresolved `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d6cc34de4a6f32afd16a90b09c5631e732e81cfd45199abec74fe2209cf8029b/763e28dd43079a7a0727ec597505526f5dfd7eeb5a1e7d16d3c4db9c1251a540/probability-probability-7caf4cf652a4e36c80370dc2-unresolved.svg`.

Classification: exact for the declared four-entry inline pool and flat runtime binding, with unchanged 25 percent values and rank order; unresolved for full live-source evaluation without the binding fixture.

### Raid high pool

The named scenario set was `CR_STARTUP_031_RAID_HIGH_VARIABLE_BIND_2026_09_13` with the two same-scenario probes `RT_RAID_HIGH_READY` and `RT_RAID_HIGH_READY_REPEAT`.

The declared high-band weights were 65, 20, 10, 4, and 1 out of 100 tickets.

The same-scenario compare was `probability-0273bccf4f1b69eb0e34aa09` with ten candidate rows, zero unresolved rows, two unchanged `PROBABILITY_STARVED_OUTCOME` diagnostics for the raw-1 entry, and `comparisonChanges=0`.

The compare JSON artifact was `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/797bf381ddecb715dd6b97ff60ad0c51a3c3bd0a3343cb5811891b40970b4e2c/82f4de0eb5b640a81e1c2b469500526064e7fdada7467919f0b6cf50de32dabd/probability-0273bccf4f1b69eb0e34aa09.json`.

The comparison render was `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2450d67f32f665574260ffbd84f57cc7db1a9cf58aca09b66d13c1108a27cc49/fae43fd280a4f256bd933a3097cddc5948479469f4bf7c18f4c65ffdd5011bbb/probability-probability-0273bccf4f1b69eb0e34aa09-comparison.svg`.

The unchanged distribution is 65 percent, 20 percent, 10 percent, 4 percent, and 1 percent in source order.

The raw-1 starvation warning is an existing declared-pool diagnostic shared by both sides and is not a syntax-repair regression.

Classification: exact for the declared five-entry high-band projection, with a retained starvation warning.

### Raid low pool

The named scenario set was `CR_STARTUP_031_RAID_LOW_VARIABLE_BIND_2026_09_13` with `RT_RAID_LOW_READY` and `RT_RAID_LOW_READY_REPEAT`.

Both scenarios declared `raid_band=low`, `all_entries_eligible=true`, and flat runtime fields `random_terror_draw_runtime_raid_low_clean=10`, `costly=15`, `partial=25`, `failure=35`, and `abusive=15`, with the second adding `repeat_probe`.

The synthetic candidate pool was `proposed/inline-probability-source.txt:12.entry.1` through `.5`.

The baseline inspect returned `PROBABILITY_SOURCE_DISCOVERED` with source hash `a5cdb7535cec79fc135a5244548cadb905d13ceeaedc171109e8c21710b7c4be` and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9c2538588ec9bb02b910709152d5db6101c3145775500a8c32e4a1fd0ea448fd/fe1bc37748e9d6e1f1fab45cbfc728c17d3101917f4d213c66796f977d5edf4a/probability-inspect-a5cdb7535cec.json`.

The repaired inspect returned `PROBABILITY_SOURCE_DISCOVERED` with source hash `bed0aa2f6a11e575e15dccc21fa6f14c7456cb5e25b15d68c1f8704dbc092b99` and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f9f71537129c8225475b1aa5fbdb56ed2c012f65dec8c7bbcb2615299744bfcc/bffae4262c74b850e0c55a0bc7404ef909ee68a6ae407a877ad2af778d41ce03/probability-inspect-bed0aa2f6a11.json`.

The baseline evaluation returned `PROBABILITY_ANALYZED` as `probability-5ac13e18f62bc67c70a9bc32` with scenario hash `d62d860ab764df5e4307602cf2321eef2fab5bd5f2174e1195c5c8303a91c2d4` and JSON artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e91dbed2348d479909bb5d23770e5bc9060ff63df4cd419e4ff9880df26d099c/19d492cd8c395c716e5867ad315e497473787c6249d05e39d227269c587b1774/probability-5ac13e18f62bc67c70a9bc32.json`.

The repaired evaluation returned `PROBABILITY_ANALYZED` as `probability-729ba3f59da34b9ef3a369aa` with the same scenario hash and JSON artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/643689dc3367f9525f7fba966c05472cd975ca0b52a117a9164d697f0dd64b07/160aa3cc892cf0de9e4a0298783010703471a66be7e50257207f52b179464ba8/probability-729ba3f59da34b9ef3a369aa.json`.

The same-scenario compare returned `PROBABILITY_ANALYZED` as `probability-b1182ebb543933d100f3c25b` with the same scenario hash and compare artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/892d4845e7ee97b3da43570a0c6a242dea77dbd790b358cc78c37976311d4564/7edf5461b50a103348f3cb066e622b067815afc1474d8ea8f61a0c51c425dd83/probability-b1182ebb543933d100f3c25b.json`.

The compact compare response returned no error, while its `comparisonChanges` field was not exposed in the retained short response and was not promoted to a numeric claim here.

The rendered compare artifacts were ranking `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/eeaf592266c5ae4508c5cee544f842803a977044d08386f7c8d0995a8cf3dae1/2180d7e6ae461167d30c31842494bcb763a9a7e32eb1676e37fc9f8e3fa0442a/probability-probability-b1182ebb543933d100f3c25b-ranking.svg`, matrix `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3d105ccdffc9526fe4e52b5581a0f9d52a13b5a1bfa6551b83dc2a3c1c39f75f/c292557be7fb59bc36d23d574cf32e138b1eb4012378b92928921723b481958d/probability-probability-b1182ebb543933d100f3c25b-matrix.svg`, comparison `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2450d67f32f665574260ffbd84f57cc7db1a9cf58aca09b66d13c1108a27cc49/dbe7f9b463195505dbf74b1983a82a4bea0700805900d5ec52209e1e81599a48/probability-probability-b1182ebb543933d100f3c25b-comparison.svg`, and unresolved `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d6cc34de4a6f32afd16a90b09c5631e732e81cfd45199abec74fe2209cf8029b/bb312499b62ee68683a8bead9f91af679d4d194e9b62a3838de8e1b49c65aa38/probability-probability-b1182ebb543933d100f3c25b-unresolved.svg`.

Classification: bounded source-contract comparison returned by MCP with the exact 100-ticket inputs, but the unextracted comparison field remains unresolved in this handoff.

### Raid mid pool

The named scenario set was `CR_STARTUP_031_RAID_MID_VARIABLE_BIND_2026_09_13` with `RT_RAID_MID_READY` and `RT_RAID_MID_READY_REPEAT`.

Both scenarios declared `raid_band=mid`, `all_entries_eligible=true`, and flat runtime fields `random_terror_draw_runtime_raid_mid_clean=35`, `costly=30`, `partial=22`, `failure=10`, and `abusive=3`, with the second adding `repeat_probe`.

The synthetic candidate pool was `proposed/inline-probability-source.txt:12.entry.1` through `.5`.

The baseline inspect returned `PROBABILITY_SOURCE_INSPECTED` with source hash `53d8a41ab40c8da5f4ed75ecefd921471ba1d16f51087b551a194a090a31a725` and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f1d83b49e36d0b904b4472708ad5f4b9233371e2d66102a930bae9372c3f7ba4/1f23011c414065e761511346db83962c6e0a859d4954fbd32e11624836519fea/probability-inspect-53d8a41ab40c.json`.

The repaired inspect returned `PROBABILITY_SOURCE_INSPECTED` with source hash `ba15a448adc7896770b44fff3703623954d3132137d28ea9699cdd60a2a6b1bf` and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/334db4c5360252a1d810ca2612cb59787b2b50a84192ac9f9f37c89aca3e5759/2906ecffc0da052563d4679957134986b71501e9a8e6d407225a2f6a99cbf560/probability-inspect-ba15a448adc7.json`.

The baseline evaluation returned `PROBABILITY_ANALYZED` as `probability-67a6a443f2b96daf59c6e09a` with scenario hash `d96918fd88359c841939e26f3129b4979a119f94139043f8256444abef8a42e3` and JSON artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b73563a9a8fc230c25a7d3dcdcbf6fdbebd39811b4658194672663fd0709db62/a2da4e21460f190d002a1b067a67d13bac1bf0987f1b912875ea27637f1d4d55/probability-67a6a443f2b96daf59c6e09a.json`.

The repaired evaluation returned `PROBABILITY_ANALYZED` as `probability-af4ec719c4b1c5963356d5bf` with the same scenario hash and JSON artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a84d760e44668d2b57292f01d61b0f5926f902b19c712982364444dee33e9d12/b92a403e0472f359060f9cc94c12e55a4bd1a32fa519777c90aa95c0a2b676ae/probability-af4ec719c4b1c5963356d5bf.json`.

The same-scenario compare returned `PROBABILITY_ANALYZED` as `probability-796b8f9bf5d999d47f3e2d50` with the same scenario hash and compare artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2d56ae95ac6c2830c71026346f8559e0844a4fce8149a234f73aecdbf83acd53/962132d90a8bbd336123c3435f22487020b7036f65f52fe6ea6d1c67cc2f4412/probability-796b8f9bf5d999d47f3e2d50.json`.

The compact compare response returned no error, while its `comparisonChanges` field was not exposed in the retained short response and was not promoted to a numeric claim here.

The rendered compare artifacts were ranking `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b60bc29ae28778eaab851c7e058771b69d7d7de4b890dca50e9df16234e4b23d/962ac27246b44baff5361553d3490bafe2b2ceb720ad87172432dec2ffaedc37/probability-probability-796b8f9bf5d999d47f3e2d50-ranking.svg`, matrix `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/dc6600df6d91cefd967ddcebb0c4e77b3a4775824b04163bed0a6f7e6cdb7252/39d4e31deb973e03379726bb5429cf7d93912945fb5e1f5e3f3bc1bb078ec869/probability-probability-796b8f9bf5d999d47f3e2d50-matrix.svg`, comparison `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2450d67f32f665574260ffbd84f57cc7db1a9cf58aca09b66d13c1108a27cc49/3b78dc14374476c7b4a7658e03d71ee6596692465138252fca1abfdd1e2fefaa/probability-probability-796b8f9bf5d999d47f3e2d50-comparison.svg`, and unresolved `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d6cc34de4a6f32afd16a90b09c5631e732e81cfd45199abec74fe2209cf8029b/56e06659fbb1b8348c7e00eba6043fae1e2ea9b929f7d48f9fcc3241b7a41931/probability-probability-796b8f9bf5d999d47f3e2d50-unresolved.svg`.

The declared normalized source contract is 35 percent, 30 percent, 22 percent, 10 percent, and 3 percent in source order.

Classification: bounded source-contract comparison returned by MCP with the exact 100-ticket inputs, but the unextracted comparison field remains unresolved in this handoff.

## Other requested surfaces and exact limits

The following rows preserve the required source paths, scenario names, and MCP results without claiming successful normalized runtime probabilities where the adapter or source baseline was incomplete.

| Surface | Source and intended repair | Named scenario contract | MCP result and classification |
|---|---|---|---|
| Event 024 friendly opinion gates | `events/024_hearts_of_iron.txt`, identifier `chaosx.nr24.40`, owner used `meta_trigger` with literal threshold 50 and preserved factors. | `024_FRIENDLY_OPINION_ABOVE_50`, `024_FRIENDLY_OPINION_AT_50`, `024_FRIENDLY_OPINION_BELOW_50`, with the same event-option candidate pool. | Baseline `event_option_ai_chance` inspect was complete with five candidates and `poolComplete=true`; source hash `7bda391f8ce7809f64ab4e0ae33445ce0d09c4d10f50e77bf07813422379b898`; artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/419fd1188a401821f89fd071cb3e4663186b51c6ae1713f7c4d46a025e6edf3b/.../probability-inspect-7bda391f8ce7.json`. A same-scenario compare was not produced in this final documentation-only pass, so the repaired threshold remains source-preserved and probability-unresolved. |
| Event 029 concession threshold | `events/029_riches_found.txt`, identifier `nr29.1`, owner corrected the category to `riches_found_foreign_interest_threshold.weak_factory_count`, retaining value 20. | `029_WEAK_FACTORY_COUNT_19`, `029_WEAK_FACTORY_COUNT_20`, and `029_WEAK_FACTORY_COUNT_21` with the same five event-option candidates. | Baseline `event_option_ai_chance` inspect was complete with five candidates, `poolComplete=true`, source hash `c52a5fe30db8b0a8048f115d897dd734559e73c6804d67f0025070d08ea4df6c`, and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ccccb463366eafa8f268db842fa6d61f4d5b16eed839c377f9d49c8d06764e56/.../probability-inspect-c52a5fe30db8.json`. A same-scenario compare was not produced in this final documentation-only pass, so the unchanged threshold is source-evidenced and probability-unresolved. |
| Event 030 stale target readiness | `common/scripted_effects/030_time_traveler_effects.txt`; the owner resets existing `time_traveler_prefire_ready` to zero and sets it to one only after successful weighted selection. | `030_VALID_TARGET`, `030_EMPTY_CANDIDATE_POOL`, and `030_STALE_TARGET`; retain existing load tickets. | Baseline helper inspect returned `no_weighted_surfaces`, source hash `3e6e478e82162e1738086d18d71d9cc71308f3c04b661c8eee0bc1d759e544c8`, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/25659d1abee20750425944f484ca17cb88b3cee3c5831126a0434c932b8214d4/.../probability-inspect-3e6e478e8216.json`. This is a state-flow guard, not a normalized probability surface. |
| Holy Realm refuge host | `common/scripted_effects/003_holy_realm_effects.txt`; restored canonical Tibet-first selection, then native random choice among eligible Bhutan/Nepal hosts. | `003_TIB_CAN_HOST`, `003_TIB_EXISTS_REFUSED`, `003_TIB_GONE_BHU_NEP`, `003_TIB_GONE_ONE_ADMITTED`, and `003_NO_ADMITTED_HOST`, with candidate manifest `TIB`, `BHU`, `NEP`. | The pre-repair helper was undefined and the prior probability inspect returned `INTERNAL_ERROR`; no before engine distribution exists. Historical contract is TIB-only 1, TIB gone with both native hosts 0.5 each, one admitted host 1, and no host 0 with no stale dispatch. The current compare remains unresolved because the before adapter could not bind the missing helper. See `holy_realm_helper_recovery.md`. |
| Event 021 decision exposure | `common/decisions/021_random_civil_war_decisions.txt` and the two `021_random_civil_war` trigger files; exposure viability uses any current country ruler existential predicates. | `021_CURRENT_RULER_EXISTS`, `021_NO_CURRENT_RULER`, `021_NESTED_NONRULER_SCOPE`, and the same 18 decision candidates. | `decision_ai_will_do` inspect returned 18 candidates, `poolComplete=false`, zero available candidates, and 12 required inputs; source hash `ffe0c7fe9093ea2e125ea0ef6eaac03cf66e91395d057cd5682e694233e6f89a`; artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3349aeec1806b6c85c3ce21645805824bf1ad2a1ea74641994a8a574fe1d621b/6f66a7076b80d505785cd149140edb69be2bc931796320856eb72e74f20095bc/probability-inspect-ffe0c7fe9093.json`. The route is score-only with unresolved hidden country state and no normalized probability claim. |
| Event 027 terrain gates | `common/scripted_effects/027_doctrine_research_ai_effects.txt` and `common/scripted_effects/027_doctrine_research_effects.txt`; five invalid state-scoped `has_terrain` uses were replaced by native `any_state_of` arrays with `is_controlled_by=PREV`. | `027_TERRAIN_CONTROLLED_FOREST`, `027_TERRAIN_CONTROLLED_MOUNTAIN`, `027_TERRAIN_CONTROLLED_PLAINS`, `027_OWNERSHIP_ONLY_NO_TERRAIN`, and `027_NO_CONTROLLED_TERRAIN`; include nested `THIS != ROOT` while preserving the calling country as `PREV`. | Baseline terrain effect inspect returned exact MCP `INTERNAL_ERROR` for the archived baseline fragment, so no before evaluation or compare can be claimed. Current full AI-effect inspect returned `PROBABILITY_SOURCE_INSPECTED`, source hash `de235c1d5ba79fe964763b2ac93f41dfb69d0f8421a670c10c8dc230b2a2507c`, `poolComplete=false`, 143 required inputs, and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/dc368fbd9616997440340dfda06530df4148a17d4bbcfe9e981f06b71ab5de57/234370ec4e7cefe6b914ed398e702a2c5ff378e7a67a22bf62efccf3b4f91e66/probability-inspect-de235c1d5ba7.json`. This is score-only and unresolved. |
| Event 027 AI spellings and bare comparisons | `common/scripted_effects/027_doctrine_research_ai_effects.txt`; preserve all existing score additions while repairing missing `ai_` helper spellings and bare comparisons. | `027_NAVY_OWNER_READY`, `027_AIR_OWNER_READY`, `027_GRAND_FOUND`, `027_TRACK_FOUND`, `027_SUBDOCTRINE_FOUND`, and `027_TRANSACTION_SUCCESS`. | Baseline random-list discovery returned 143 candidates, source hash `cbf30e6c9ce4e64721b69dac436017e7c4c856b8b855e2ac27c12040567bb550`, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/878b3f3e83a49d05cf1f6fd82c4fa625ad7cb9adc122d88cc6a8faba241bee93/9943f51fb85dbc1d7e8b73a620bf61ce525e28fc78a27201b856809daba15668/probability-inspect-cbf30e6c9ce4.json`. The hidden score inputs were not typed into a complete scenario, so normalized output and compare remain unresolved. |
| Event 028 victory-point predicates | `common/scripted_effects/028_asteroid_incoming_runtime_effects.txt`; preserve the existing score predicates while repairing invalid `victory_points` syntax. | `028_VP_BELOW_THRESHOLD`, `028_VP_AT_THRESHOLD`, and `028_VP_ABOVE_THRESHOLD` with the same outer candidate gates. | Inspect returned `no_weighted_surfaces`, source hash `7c665739efa3d9ad40f6cd87458875c51a4b747ae20d241a9ee118420cdb74c3`, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/46e2d477a12f90ce934660a9624ae430a5db360b731cd82b46ee9c3fdd6b66cf/7041cb3f642e832c71092b5d87f883723b2e35180a1d659a1eee349ff8ad088e/probability-inspect-7c665739efa3.json`. The predicates are score gates and no normalized probability result is available. |
| Event 035 imported-resource floor | `common/scripted_effects/035_great_depression_effects.txt`; preserve the imported-resource floor predicate. | `035_IMPORTED_RESOURCE_BELOW_FLOOR`, `035_IMPORTED_RESOURCE_AT_FLOOR`, and `035_IMPORTED_RESOURCE_ABOVE_FLOOR`. | Inspect returned `no_weighted_surfaces`, source hash `254f272ff5672a8a57b361be2374cba3811813885b09685051f01b06eaddafe0`, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3a3032e441a9373c88d48cfd94c23fbec1f3e9e1c3140357795b3e91c0c8232a/b9505759f5d454c2830c1139d2b6a45a25fff95bfdba31d411669ce087ecb9d4/probability-inspect-254f272ff567.json`. This is a score or eligibility predicate, not a normalized pool. |
| Event 035 incident due-clock initializer | `common/scripted_effects/035_great_depression_incident_effects.txt`; move the due-clock initializer out of the trigger while preserving timing values. | `035_DUE_CLOCK_READY`, `035_DUE_CLOCK_NOT_READY`, and the same declared incident candidate pool. | Source-only inspect discovered 63 candidate positions with source hash `8758482d2a491a6953d0d7fc5fb3d8667b0cb702ebc91b59eb9426fa8d281928`, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2bc715f8195820046fb57b5276cff88b4d0120de91ceae2ca3f3680f783d3f9e/fe71177c83ec1fcf97f9571c71b70fc9f72c89273b9b0656c737960276952eae/probability-inspect-8758482d2a49.json`, but direct `random_list` inspection returned exact MCP `INTERNAL_ERROR` at the due-clock initializer in the trigger around lines 1031-1033. No baseline normalized probability or compare is claimed. |
| Event 039 technology factor gates | `common/scripted_effects/039_murder_mystery_integration_effects.txt`; repair `has_tech encryption_1` to `installed basic_encryption` and `radar` to `radio_detection` while retaining factor arithmetic. | `039_BASIC_ENCRYPTION_PRESENT`, `039_BASIC_ENCRYPTION_ABSENT`, `039_RADIO_DETECTION_PRESENT`, and `039_RADIO_DETECTION_ABSENT`. | This handoff records the exact source contract and owner boundary, but no durable probability artifact was produced for the technology factor adapter in this documentation-only pass. The conclusion remains unresolved pending a typed factor fixture and same-scenario compare. |

The Event 035 source reachability review also found that all three current callers of `classify_worldwide_pressure` at `common/scripted_effects/035_great_depression_incident_effects.txt:5359`, `:5372`, and `:5473` gate `great_depression_is_valid_worldwide_pressure_target`, which excludes `great_depression_active` at the corresponding trigger definition around line 165.

The repaired `any_other_country` faction exposure therefore preserves the reachable original member-flag condition, while the caller's own active flag is unreachable at every current callsite.

This is source and trigger reachability evidence only and does not establish a normalized probability result.

## Source receipts and limits

The Event 027 terrain source receipt is `startup_terrain_repair_receipt.json`.

Its before and after hashes are `76919a4f84de2c15dbf4387cddd0ff869c4bab6dcb00fe22fc196bb4d970e749` to `51bfc294cfcbc08d5b0d4d28a5a2672d3cb3f897d6ec79de6bd60f99ceeb9f3f` for the AI effect and `4d0fa0d2bd1bdf17611f043adb0e3253ccc087c253ca7ac6779e1254b7afa333` to `93db1942926261a20e9d8a000a1acb8812898cf3c899641646f3ba2e7aee2341` for the doctrine effect.

The map-derived terrain arrays are documented in `startup_terrain_research.md` and `startup_terrain_state_sets.json`.

The terrain map join covers 1,081 state files, 13,414 province definitions, and 10,272 memberships, with 454 forest states, 459 mountain states, and 675 plains states.

The terrain arrays are map classifications and are not balance values.

The 031 `@` declarations are file-local, so the dynamic-key projection explicitly binds every 031 runtime field to the original numeric value before evaluating the random list.

The probability adapter did not resolve nested runtime-variable objects and did not provide a complete typed full-source fixture for the surrounding scripted-effect call graph.

The full 031 source contains multiple categorical random pools, so an unrestricted inspection cannot certify one normalized pool; each bounded comparison therefore declares the complete pool it evaluates.

The Event 003 before helper was absent, the Event 035 baseline trigger contained a due-clock initializer in an unsupported position, and the Event 027 terrain baseline archive returned `INTERNAL_ERROR` before evaluation.

Score races and eligibility predicates are not click probabilities.

No `probability_sweep` was run because no tuning range or rank-reversal question was authorized.

No `probability_simulate` was run because no uncertain input distribution or seed contract was declared.

No `probability_sequence` was run because no complete cadence, cooldown, state-transition, and terminal-state manifest was declared.

The completed 031 evidence is exact only for the declared bounded pools and input bindings.

The remaining rows are source-preservation evidence, score-only evidence, or unresolved adapter routes and must not be presented as full runtime balance certification.

## Recommended owner follow-up

Retain every existing 031, 024, 029, 030, 003, 027, 028, 035, and 039 numeric value and rerun the exact named scenarios after any further source change.

For 031, keep the complete incident 158-ticket pool and each unchanged 100-ticket pattern or raid pool intact while preserving the flat runtime bindings required by the analyzer fixture.

For 027 terrain, rerun a typed score fixture covering controlled forest, controlled mountain, controlled plains, ownership without matching terrain, no controlled terrain, and nested `THIS != ROOT` scope.

For 003, provide a before-side helper or accepted canonical baseline manifest before claiming a true before-and-after comparison.

For 024, 029, and 039, run the same named threshold or technology presence scenarios through the corresponding typed adapter and retain both source inspect artifacts.

For 021, 028, and 035, keep conclusions score-only until the adapter exposes complete candidate validity and external state.

No simplification was applied to gameplay source by this auditor; the only audit simplification is the explicitly labeled inline MCP projection for the bounded Event 031 comparisons.
