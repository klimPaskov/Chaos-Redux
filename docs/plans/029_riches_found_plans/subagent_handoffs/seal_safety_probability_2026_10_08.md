# Event 029 seal-safety AI probability handoff

Status: baseline captured; parent AI guards applied; same-fixture probability comparison has no terminal MCP result and remains unresolved.
This is a read-only audit by the auditor; the parent applied the requested source change during this audit.
The auditor made no gameplay-source edit, launched no game, ran no Git command, and started no child agent.

## Scope and authoritative baseline

Audited IDs: `decision_riches_found_gold_seal_depths` and `decision_riches_found_demons_permanent_seal` in `common\decisions\029_riches_found_decisions.txt`.
The authoritative pre-AI source is the parent snapshot `docs\plans\029_riches_found_plans\evidence\2026_10_08_seal_safety_parent_before\common__decisions__029_riches_found_decisions.txt`, SHA-256 `AE8C42A480A71CCD41AB2553DC324815DAADF6496A406F8B530123B5E2ADE7B9` (442,525 bytes).
The audit copy at `docs\plans\029_riches_found_plans\evidence\2026_10_08_seal_safety_before\common__decisions__029_riches_found_decisions.txt` matches it byte-for-byte.
This parent snapshot is the `before` source for the attempted AI comparisons; the current shared decision file is not treated as the baseline.
At baseline capture, the shared decision file was SHA-256 `B9D2F4C7BB4EAE5DB1E2F3B1DE819C70FC6219238571A0E98AE52C99F5CE1B56` and contained the parent's neutral lifecycle-safety changes but no AI patch.
It was not used as the immutable before source.

## Probability MCP evidence

The first adapter-only call was rejected with `-32602`: `An adapter requires a source; provide a source alone to discover compatible adapters`.
A string source was also rejected because the live schema requires an object.
The valid source-specific inspect first used the retained snapshot path and exact target IDs.
That path returned status `ok`, code `PROBABILITY_SOURCE_DISCOVERED`, source hash `372671a7b8006895e6f52289ff4f4dc2dfa5e5b94aaf2ca9b66a69801f55e1db`, source revision `82208b36b02ccd357be07e0b16f0c4f2d6dc7f6a831ebdaeb30f58a7a7343438`, `availableAdapters: []`, `candidates: 0`, `requiredInputs: 0`, `unresolved: 0`, and `discoveryReason: no_weighted_surfaces`.
This was a path-specific result for the copied `docs` source and is not evidence that the decision adapter is absent for the logical game path.
Artifact URI: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f227b75d4ec84e91c12d6673b6cb600e9c4699f4a9fc58732ae197aa06e3301d/ba8989e718131eeb393ea616e159b70f3fa14e2bc94fcd05c1444639436aa8e9/probability-inspect-372671a7b800.json` (artifact SHA-256 `f227b75d4ec84e91c12d6673b6cb600e9c4699f4a9fc58732ae197aa06e3301d`).

A second read-only inspect pinned the same bytes through logical `path: "common/decisions/029_riches_found_decisions.txt"`, `snapshotPath` to the frozen copy, and lowercase `expectedSourceHash` `ae8c42a480a71ccd41ab2553dc324815daadf6496a406f8b530123b5e2ade7b9`.
The live schema rejected uppercase hex for `expectedSourceHash` and accepted the lowercase form.
This logical-path request returned `PROBABILITY_SOURCE_DISCOVERED`, the same source hash `372671a7b8006895e6f52289ff4f4dc2dfa5e5b94aaf2ca9b66a69801f55e1db`, source revision `26896910ab99f1d41c7d2aee20ad623be319d3e5beed909a4093045d3dcd0685`, three `decision_ai_will_do` candidates, 103 `mission_ai_will_do` candidates, and zero matches for both requested IDs.
The tool's artifact lists the examples `decision_riches_found_choose_partner`, `decision_riches_found_return_to_mine_list`, and `decision_riches_found_select_mine`; it scanned the snapshot file under the logical source request.
Artifact URI: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/88b063d2f7a2b235745cb27770b41c532d2c6620ebfff358fadabacfd366c555/359270c41bcc7a81019debe80b732bb0a15e9d51148e6749ae93f947ef0e2c60/probability-inspect-372671a7b800.json` (artifact SHA-256 `88b063d2f7a2b235745cb27770b41c532d2c6620ebfff358fadabacfd366c555`).
The adapter is present and discovers three other decision records, but neither target decision is exposed as a candidate; the target surface remains unresolved.

`hoi4.probability_evaluate` was then called for the two named decisions with the official six `RF_GOLD_*` and `RF_DEMON_*` scenarios.
It returned `PROBABILITY_SURFACE_EMPTY`, zero artifacts, empty data, and no scenario hash.
A second baseline evaluation used the 13-case set in the fixture manifest below and returned `PROBABILITY_SURFACE_EMPTY` for the two-target candidate pool.
It produced no base score, modifier trace, ranking, scenario hash, or comparison ID.
These conclusions are unresolved; no willingness score or click probability is claimed.
The final scenario fixture manifest is `evidence\2026_10_08_seal_safety_before\seal_safety_scenario_fixture_manifest.json`, SHA-256 `CD6159A72BB1388132360B5CC5DB12878D65E207FE718B04139B6AE1ED4A8D14`.
The 13-case request used candidate pool `["decision_riches_found_gold_seal_depths", "decision_riches_found_demons_permanent_seal"]` and scenario set `event029_riches_found_seal_safety_20261008`.
The exact retained fixture, selected IDs, normalization, and seven derived cases are recorded in `evidence\2026_10_08_seal_safety_before\seal_safety_scenario_fixture_manifest.json`.
The source fixture SHA-256 is `EA66836933BCF34A929979E43B894ED7F6D61C88D2A545132B13FB1B6C46005E`; the scenario specification SHA-256 is `CD0BE227B9354274B355626DD02E3FC71A3ABCBE703BC15341CE1F92DB860BBD`.
Because the adapter returned no analysis, there is no MCP scenario hash to preserve.
An additional attempt to use a unique scenario-set ID did not return a terminal result after about 93 seconds and was terminated.
A one-decision, one-scenario `hoi4.decision_inspect` underload retry also did not return a terminal result after about 93 seconds and was terminated.
Neither retry produced evidence.
A pre-AI inspect of the logical shared decision file is diagnostic only, not baseline bytes.
It returned source hash `7c8d84a0d20d38d279e438bb54cbe58eda44ece57f2cde831ab7676827994b79`, source revision `29317100617c277a3dc5c6c8a7110c85c4bae2a3db50839592530c162009f8f6`, three `decision_ai_will_do` candidates, and zero matches for the two target IDs.
Its artifact URI is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4f43a8668b0b09c9b6c5302fb16f4928074abd5e736fb9fb8b7d9f2262bbc987/9c301901fa52f09f50e72853537397adce831046f572c50f887b57d5cf51deb7/probability-inspect-7c8d84a0d20d.json` (artifact SHA-256 `4f43a8668b0b09c9b6c5302fb16f4928074abd5e736fb9fb8b7d9f2262bbc987`).
Its source-only inventory artifact URI is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b17e546ea7060a0cd97f21dda45a4fcd8a11927781dd2d80db6fc8005a9561b9/0b4e4908c978b5c28944ec8459179e7257a97c980c6f654a3f89c11b57b136ac/probability-inspect-7c8d84a0d20d.json`.
References read through the local HOI4 reference tools: offline `Decision modding - Hearts of Iron 4 Wiki.md`, AI section, lines 357-374, revision `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162`; offline `AI modding - Hearts of Iron 4 Wiki.md`, MTTH blocks, lines 26-37, revision `917cd261f7da51fe4d8687c5d7663e768a09c5c101ac130ce646bc64637aa818`; installed `common\decisions\_documentation.md`, Country Decisions, lines 1-46, revision `5e7e686b5582f32c38d898d805e17171e88f3bfeee4a030deb1884f9726de019`.
The initial decision context omitted several unrelated sections; targeted reads completed the relevant decision-AI, MTTH, and decision-gate coverage.
No baseline sweep was run because inspect exposed no target candidate or supported numeric sensitivity path.
No render was attempted because evaluation returned no analysis artifact or `analysisId`.
No probability simulation was run because no explicitly uncertain input was declared.
No probability sequence was run because no complete custom pool with cadence and state transitions was declared.

## Post-patch comparison attempt

The parent applied exactly two additional modifiers to `decision_riches_found_demons_permanent_seal.ai_will_do`: the existing `low_factor` when `riches_found_seal_would_entomb_workforce` is true, and the existing `never_factor` when democratic government and that helper are both true.
The parent reported no other AI coefficient edits.
The post-AI whole decision file is 443,890 bytes with SHA-256 `88B2F6716F401657251BC79C8C144B081953D71725B81F693F630F28AEE36B8D`.
The exact after bytes are retained at `docs\plans\029_riches_found_plans\evidence\2026_10_08_seal_safety_after_ai\common__decisions__029_riches_found_decisions.txt` and match the live source hash.
The after file includes the earlier parent lifecycle-safety edits as well as the two AI guards; the before/after pair therefore does not isolate all non-AI source differences.

Five `hoi4.probability_compare` requests were submitted with the same scenario set `event029_riches_found_seal_safety_20261008`, all 13 exact scenario IDs, and the frozen before SHA `AE8C42A480A71CCD41AB2553DC324815DAADF6496A406F8B530123B5E2ADE7B9` versus after SHA `88B2F6716F401657251BC79C8C144B081953D71725B81F693F630F28AEE36B8D`.
The requests covered both target IDs with logical source paths plus the before snapshot path and expected hashes, the demonic decision alone with the same fixture, direct snapshot-before plus logical after paths, a no-refresh retry, and finally logical paths pinned to before and after snapshots.
Every compare call remained nonterminal for about 93 to 124 seconds and was terminated without structured content, code, artifact, scenario hash, or comparison ID.
No `PROBABILITY_SURFACE_EMPTY` compare result was returned, so the compare is blocked and no comparison pass is claimed.

A post-patch `hoi4.probability_inspect` was also submitted for the logical current source with expected hash `88b2f6716f401657251bc79c8c144b081953d71725b81f693f630f28aee36b8d` and the two target IDs.
It did not return a terminal result after about 93 seconds and was terminated.
The logical-path inspect pinned to the before snapshot did return three non-target candidates, but it does not establish post-patch candidate coverage.

The installed classifier source now explains the inventory split: its `days_remove` predicate places the timed target decisions in the mission bucket.
The direct `candidatePoolMatches` fields for the two requested IDs were still zero, and no score trace or comparison result was returned.
The installed offline `Decision modding` AI section explicitly permits either `factor = 10` or `base = 10` in native `ai_will_do` MTTH blocks, so the target's valid `base = constant:riches_found_decision_ai.medium` form must not be rewritten for analyzer convenience.
The three recognized examples are decision selectors using `base = constant:riches_found_value.zero` at `common\decisions\029_riches_found_decisions.txt:9061`, `:9111`, and `:9135`; the target blocks use `base = constant:riches_found_decision_ai.medium` with standard modifier blocks.
This observed distinction does not prove why the adapter excludes the target blocks, and the installed documentation confirms both `base` and `factor` are valid native MTTH initializers.
The parent reports that a lexical brace/declaration scan found all 97 decision and mission declarations at depth 1 inside their category and final depth 0, with `claim_free` closed at line 307 and no misnesting.
The discovery gap is therefore unresolved at the adapter/source-matching level, not attributed to malformed source.

## Source review: score, validity, and harm conditions

In the frozen baseline, `gold_seal_depths` has `base = constant:riches_found_decision_ai.medium` and source modifiers for favored public policy, the gold-pressure next step, and deep-mine urgency.
`demons_permanent_seal` has the same medium base and source modifiers for favored public policy, democratic urgency, and the supernatural-crisis factor.
The source constants are `medium = 3`, `policy_favored_factor = 2.5`, `urgent_factor = 4`, `high_factor = 2`, `low_factor = 0.50`, and `never_factor = 0`; these are source values, not MCP-measured results.
Neither target AI block contains the entombment `low_factor` or democratic `never_factor` seen on the separate existing `decision_riches_found_permanent_seal` template.
That template uses `low_factor = 0.50` when `FROM = { riches_found_seal_would_entomb_workforce = yes }` and `never_factor = 0` when that condition and democratic government are both true.
The helper `riches_found_seal_would_entomb_workforce` at `common\scripted_triggers\029_riches_found_triggers.txt:572` is true for severe collapse or supernatural crisis, unless the deposit is exhausted, the workforce is evacuated, or the demonic district is evacuated.
The helper does not exclude a completed military purge.
The source-only implication is that purge does not count as evacuation for this harm guard; the explicit purge-not-evacuated variants preserve that distinction.
This is not an MCP-measured score result.
The frozen demonic decision's visibility/target gates require the demonic layer, a cleared district, no active contract or occupation, and no prior permanent seal.
The cleared-district helper accepts evacuation, workforce evacuation, or military purge.
The frozen gold decision requires the gold layer, a restricted gold route, and unsealed depths.
The source fixture does not fully bind these gates: the original `RF_DEMON_02` has no cleared-district flag; `RF_DEMON_03` is already sealed; and the Gold scenarios omit the layer/route predicates.
Its `manpower_k = 500` means 500,000 manpower, which is ample against the 600 raw manpower cost (0.6k).
All six original cases omit `num_of_available_civilian_factories`.
Therefore the named set does not establish a complete available candidate pool or complete external-factor coverage.
The supplied cost context is retained but not re-audited here: gold sealing reserves two civilian factories for 60 days and consumes 300 raw manpower (0.3k) plus 150 support equipment before reducing lower-workings output; demonic permanent sealing reserves two civilian factories for 90 days and consumes 600 raw manpower (0.6k) plus 150 support equipment before ending ordinary mine output.
Cost availability, factory reservation timing, and refunds are not probability-adapter evidence.

Parent-reported decision-audit evidence is separate from this probability pass: no P1 regression was found, and the three gold affordability predicates resolved true for a typed `FROM` case with two civilian factories, 300 raw manpower (0.3k), and 150 support equipment.
That review still leaves the overall control/helper/payment model unresolved and reports route entrance, integrity, resistance, and callback-identity gaps.

## Scenario fixture used for the requested follow-up

The base six scenarios are copied unchanged from the retained typed fixture after keeping `id`, `actor`, `date`, `flags`, `state`, and `scopes`; the country/state scope trees are preserved. `controls` and `closedFlags` were omitted because the probability request accepts the typed scenario fields used by the previous bounded audit, not those auxiliary fixture fields.
The seven added scenarios are deterministic copies of the named base cases.
`RF_DEMON_04_WORKFORCE_EVACUATED` adds `riches_found_supernatural_crisis` and `riches_found_workforce_evacuated` to the `FROM` flags of `_02`.
`RF_DEMON_05_DEPOSIT_EXHAUSTED_AFTER_PURGE` adds `riches_found_severe_collapse`, `riches_found_demons_military_purge`, and `riches_found_deposit_exhausted` to `_02`.
`RF_DEMON_06_PURGE_NOT_EVACUATED` adds `riches_found_supernatural_crisis` and `riches_found_demons_military_purge` to `_02`.
`RF_DEMON_07_UNRESCUED_ECONOMIC` adds those same two flags to `_02` and sets root and controller `num_of_available_civilian_factories = 1`, `manpower_k = 500`, and `support_equipment = 100`; it is cost-ineligible because civilian factories and support equipment are below the declared recipe.
The unchanged `manpower_k = 500` is 500,000 manpower and is ample against the 600 raw manpower cost (0.6k).
This case does not establish that no economic rescue alternative exists.
`RF_DEMON_08_DEMOCRATIC_ENTOMBMENT` adds `riches_found_severe_collapse` and `riches_found_demons_military_purge` to `_01`.
`RF_DEMON_09_DEMOCRATIC_EVACUATED` adds `riches_found_severe_collapse` and `riches_found_workforce_evacuated` to `_01`.
`RF_DEMON_10_SEVERE_COLLAPSE_PURGE_NOT_EVACUATED` adds `riches_found_severe_collapse` and `riches_found_demons_military_purge` to `_02`.
The exact 13 IDs are `RF_GOLD_01_STABLE_HIGH_LEGITIMACY`, `RF_GOLD_02_AUTHORITARIAN_WARTIME`, `RF_GOLD_03_COLLAPSE_IMMINENT`, `RF_DEMON_01_STABLE_DEMOCRACY_PEACE`, `RF_DEMON_02_COLLAPSING_AUTHORITARIAN_WAR`, `RF_DEMON_03_EVACUATION_COMPLETE`, `RF_DEMON_04_WORKFORCE_EVACUATED`, `RF_DEMON_05_DEPOSIT_EXHAUSTED_AFTER_PURGE`, `RF_DEMON_06_PURGE_NOT_EVACUATED`, `RF_DEMON_07_UNRESCUED_ECONOMIC`, `RF_DEMON_08_DEMOCRATIC_ENTOMBMENT`, `RF_DEMON_09_DEMOCRATIC_EVACUATED`, and `RF_DEMON_10_SEVERE_COLLAPSE_PURGE_NOT_EVACUATED`.

## Frozen evidence files

The directory `docs\plans\029_riches_found_plans\evidence\2026_10_08_seal_safety_before\` retains the parent-before decision snapshot, the typed scenario fixture and spec, the cost/localisation snapshot from the parent-before folder, and source helper copies captured from the shared workspace at baseline time.
The helpers are supporting source snapshots, not substitutes for the parent's authoritative whole-decision baseline.

| Evidence file | Bytes | SHA-256 |
| --- | ---: | --- |
| `common__decisions__029_riches_found_decisions.txt` | 442525 | `AE8C42A480A71CCD41AB2553DC324815DAADF6496A406F8B530123B5E2ADE7B9` |
| `common__scripted_triggers__029_riches_found_triggers.txt` | 68722 | `8930B26A5A928301A5063D34A463E78A26BE09F6BC4DBE2B75B37186BF1CDA5F` |
| `common__scripted_triggers__029_riches_found_cost_triggers.txt` | 25461 | `C53B2A587EA192B7247E3A70F6D878681AAA94D77C44A6286F6FAC8E41B80C96` |
| `common__scripted_effects__029_riches_found_effects.txt` | 195103 | `0F603E0ABB9854441CE62AE69DC41CE845D21A55E2F592D5E49F02A355836D54` |
| `common__scripted_effects__029_riches_found_harm_effects.txt` | 31224 | `C4992785962BAD71235AC964E4BCE75B49B72978F5B60785BF0452D132B8FD1A` |
| `common__scripted_effects__029_riches_found_aggregate_stage_effects.txt` | 11632 | `65DA4EA17D88BFEB76FA2862224AF23A27AEAA3B72C952D06065C0BB57729182` |
| `common__script_constants__029_riches_found_constants.txt` | 38749 | `53D8DDF3BB195FF49FBAD9A1EA00CC1351FEED80C4E48A66F2DD04DA44ED6DA7` |
| `localisation__english__029_riches_found_decisions_l_english.yml` | 114952 | `0B5E5495AB2D7878EA5FCEAA674DC2B7CFBDB3682DC454225D8B7A5BF97D6CAD` |
| `2026_10_03_typed_scenarios.json` | 968232 | `EA66836933BCF34A929979E43B894ED7F6D61C88D2A545132B13FB1B6C46005E` |
| `029_riches_found_ai_probability_scenarios.md` | 18628 | `CD0BE227B9354274B355626DD02E3FC71A3ABCBE703BC15341CE1F92DB860BBD` |
| `seal_safety_scenario_fixture_manifest.json` | 3422 | `CD6159A72BB1388132360B5CC5DB12878D65E207FE718B04139B6AE1ED4A8D14` |

The frozen post-AI whole-decision copy is `docs\plans\029_riches_found_plans\evidence\2026_10_08_seal_safety_after_ai\common__decisions__029_riches_found_decisions.txt`, 443,890 bytes, SHA-256 `88B2F6716F401657251BC79C8C144B081953D71725B81F693F630F28AEE36B8D`.
It matches the live source at the time of capture.

## Findings, limits, and next step

No baseline or post-patch AI score, modifier trace, candidate ranking, selection probability, dominance result, starvation result, rank reversal, repetition rate, or exploit probability was produced by MCP.
Source review confirms the base values and entombment guard predicates only.
The decision adapter exists, but the returned candidate inventory omits both target decisions; the unrelated `mission_ai_will_do` inventory was not substituted.
The parent-applied demonic modifiers match the existing `decision_riches_found_permanent_seal` guard pattern.
Five same-fixture comparison requests were submitted, but all ended without a terminal MCP result, so no comparison pass is claimed.
No numeric sweep path was exposed for the helper's Boolean eligibility; no sensitivity sweep or render result is claimed.
The baseline inspection artifacts and exact compare inputs are retained above; no compare ID, comparison scenario hash, or render URI exists.
This audit recommends no new gold-seal tuning target; the current comparison gap prevents measured confirmation that its AI score is unchanged.
Skills read and applied: `chaos-redux-subagents`, `chaos-redux-decisions-missions`, and `chaos-redux-mtth`.
No skill was edited.

## Installed MCP classifier investigation (read-only append, 2026-10-08)

This follow-up resolves the earlier unexplained adapter/source-matching gap and makes no further probability-compare request.

### Configured server and installed package

The live resource `hoi4-agent://server/status` reported current server PID `1908`, transport `stdio`, version `3.10.0`, and start time `2026-10-08T06:48:48.024Z`.
PID `1908` is `node.exe` at `C:\Program Files\nodejs\node.exe`; its running script resolves to `C:\Users\klimp\AppData\Local\npm-cache\_npx\e5002410e5b7105a\node_modules\hoi4-agent-tools\dist\bin\stdio.js`.
The installed package root is `C:\Users\klimp\AppData\Local\npm-cache\_npx\e5002410e5b7105a\node_modules\hoi4-agent-tools`.
Its `package.json` at lines 2 and 4 identifies `hoi4-agent-tools` version `3.10.0`, SHA-256 `86017F941A2FA6D3F35A2D39E3B29EBF68DD7AC4553493988DCD325E23B2BCBC`.

The user-level config `C:\Users\klimp\.codex\config.toml` lines 126-133, SHA-256 `689DE022A149C4282DA76324F4D51D6BD22FB3EFBC20D80EADEB5E288F9259B9`, launches `npx.cmd --yes --prefer-online hoi4-agent-tools@latest` and sets `HOI4_AGENT_CONFIG` to `C:\Users\klimp\AppData\Roaming\hoi4-agent-tools\config.json`.
The repository config `.codex\config.toml` lines 12-18, SHA-256 `8B410F652ACD6C6BDFBC985139839CA8B2166F70DC70DEBC521D6FFE27777012`, names the same package and working directory.
The resolved `HOI4_AGENT_CONFIG` file has SHA-256 `7F5579FD68182E9DEE173AAC98A74E67A33785491259573C12D4B93F62DBD9CC`; its `modRoots` and `gameRoot` point to the supplied Chaos Redux mod root and installed HOI4 root.
The configured tag is mutable `@latest`, but the active process path and package manifest both identify the actually installed version as `3.10.0` in the `_npx\e5002410e5b7105a` cache.

### Installed classifier and domain contract

The primary installed classifier is `C:\Users\klimp\AppData\Local\npm-cache\_npx\e5002410e5b7105a\node_modules\hoi4-agent-tools\dist\hoi4_agent_tools\probability\source-analysis.js`, SHA-256 `E0116D2961139D556F09C477D43A55167222D6BA98188008109046EA218D6B11`.
Its `decisionCandidates` function accepts direct decision-category children with `ancestors.length === 1` at lines 132-153.
At lines 155-158 it sets `mission = true` for any entry with `is_mission = yes`, a `days_mission_timeout` field, or a `days_remove` field, then excludes the entry from `decision_ai_will_do` whenever that predicate is true.
At lines 160-167 it reads the native `ai_will_do` block and emits the candidate kind from that same `mission` boolean.

The installed adapter contract is `C:\Users\klimp\AppData\Local\npm-cache\_npx\e5002410e5b7105a\node_modules\hoi4-agent-tools\dist\hoi4_agent_tools\probability\adapters.js`, SHA-256 `8EC6A390C5EC1280E083A8CBDABA19F0F7E72BA0D62BF8AA4AC5C70041D4B4D4`.
At lines 57-78, `decision_ai_will_do` declares source block type `decision ai_will_do`, accepts country and target scopes, supports `base/add/factor`, modifiers, script constants, and scripted triggers, and is `score_only` with no normalized probability.
At lines 80-100, the distinct mission adapter declares source block type `mission ai_will_do`.
The installed `decision/ai.js` at `C:\Users\klimp\AppData\Local\npm-cache\_npx\e5002410e5b7105a\node_modules\hoi4-agent-tools\dist\hoi4_agent_tools\decision\ai.js`, SHA-256 `0737B3AD97ADAEEDC3A584DF244FDBB445773DE1A978FB0554F113082E120ED7`, chooses the adapter from `subject.kind` at line 37, so the classifier's `days_remove` result also routes decision inspection through the mission adapter.

Native references confirm the classifier predicate is wrong for `days_remove`.
The offline `Decision modding` Wiki section “Timer upon selection” at lines 337-356, revision `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162`, defines `days_remove` as the timer on a decision after selection and ties its expiry to the decision's `remove_effect`.
The installed `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\effects_documentation.md` section `add_days_remove` at lines 1066-1080, revision and SHA-256 `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`, explicitly calls `days_remove` the value of a decision.
The same offline Wiki's Decision modding AI section at lines 357-374 documents both `factor` and `base` as valid native `ai_will_do` initializers.
Therefore the target blocks' `base = constant:riches_found_decision_ai.medium` syntax is valid and must not be rewritten to accommodate the adapter.

### Corrected native counts and exact misclassification

Brace-aware read-only scans of both pinned decision files agree: the frozen before file (`AE8C42A480A71CCD41AB2553DC324815DAADF6496A406F8B530123B5E2ADE7B9`) and the after file (`88B2F6716F401657251BC79C8C144B081953D71725B81F693F630F28AEE36B8D`) each contain 97 `decision_` declarations plus 9 `mission_` declarations, 106 total.
The file has 95 `state_target` fields, 94 `days_remove` fields, 9 `days_mission_timeout` fields, and no `is_mission = yes` fields.
In these exact files, all 95 `state_target` fields belong to native decision declarations and none belong to the nine mission declarations.
Of the native decisions, 94 are state-targeted and have `days_remove`; `decision_riches_found_select_mine` is state-targeted but has no `days_remove`; two decisions have neither field.
This corrects the parent-provided partition that assigned one `state_target` to a mission and described three selectors as lacking the field: `select_mine` is a native decision with `state_target = any_controlled_state` at frozen-before lines 9047-9049 and after lines 9066-9068.

The logical-path probability inventory's 3 decision examples are `decision_riches_found_choose_partner`, `decision_riches_found_select_mine`, and `decision_riches_found_return_to_mine_list`.
In the after file, `choose_partner` at lines 9029-9064 and `return_to_mine_list` at lines 9116-9136 lack `state_target` and `days_remove`; `select_mine` at lines 9066-9114 has `state_target` but no `days_remove`.
The other 94 native decisions with `days_remove` satisfy the installed classifier's `mission` predicate, while the 9 actual missions satisfy it through `days_mission_timeout`.
That yields exactly 3 decision candidates and 103 mission-like candidates, matching the live MCP inventory.

This is a confirmed native-versus-adapter misclassification, not a source nesting defect and not a base-versus-factor parser limitation.
The parent's lexical scan also confirms all declarations are at the expected category depth and `claim_free` closes at line 307.
The `mission_ai_will_do` bucket is not an acceptable substitute because 94 of its records are native decisions under the installed source classifier.
No external package, dependency, repository gameplay file, or live configuration was modified.

The attempt to read the earlier probability-inspect artifact through the advertised byte-range resource template failed with `-32603: Artifact provenance manifest is unavailable`.
The artifact inventory details remain limited to the structured counts/examples already returned, but the installed classifier source, adapter contract, native file counts, configured process, and documentation were directly verified.
