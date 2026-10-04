# Soviet famine shortfall probability audit — 2026-10-03

## Audit status

Read-only before/after probability analysis is complete for the warning event, crisis event, and famine relief decision under the saved eleven-case scenario set.

The event option pools are complete when selected by their local event identifiers, but ordinary funding, shortfall, and target scenarios remain unresolved because the installed probability adapter cannot evaluate the source's compound equipment, mission, and variable-to-state-scope inputs.

No AI weight target is recommended, and no gameplay source was changed by this audit.

The MCP scenario model returns an exact conditional share of `1` for the warning and crisis relief-underway acknowledgements in the declared active-relief case.

The `invalid-GER` event result is contradictory and is classified as an analyzer anomaly rather than a valid selection probability.

## Scope and source identity

Audited weighted surfaces are `soviet_gulag.1` and `soviet_gulag.2` in `events/soviet_gulag.txt`, plus decision score `sov_emergency_famine_relief` in `common/decisions/camp_repression_major_country_decisions.txt`.

The installed direct HOI4 MCP server was version 3.6.0 with adapter `hoi4-1.19.2.v1`, target game version `Operation Postern 1.19.2.0 (d245)`, and workspace `camp_famine_oct3`.

Frozen baseline snapshots were read directly from the preserved files under [`mcp/soviet_famine_2026-10-03`](../mcp/soviet_famine_2026-10-03/).

Current production bytes were rehashed before the final comparisons and match the preserved after snapshots.

| Source | Frozen before SHA-256 | Frozen after/current SHA-256 |
|---|---|---|
| `events/soviet_gulag.txt` | `773c927aee19767055da26922c72b88aaa30335b751ec8b58423615081937a31` | `58cecddff96fb888fc95f3e11d10e30a066e9e967f419bc23525fc665af6d3ed` |
| `common/decisions/camp_repression_major_country_decisions.txt` | `0a5fe8c6b52f7137f037077c91804115cb07f6d4eae74c077a8d8fafda34a016` | `8580d4ff53b87e54cee3c833bbcecebdf2ca3653a50512ebd2c0160369230940` |
| `common/scripted_triggers/camp_repression_rework_triggers.txt` | `6af7825c80b16aecabca771064393d05d2389d31eb05f6ec986bd10b9b9381c1` | `5e21b40d7f864379fa132edc8c54955b8eadcaf68cbda58404cad0d9d9d2a57f` |
| `common/scripted_effects/camp_repression_action_dispatcher_effects.txt` | `690076509836afa0da14286f9fe5b00a5ca6e327cad4893c9fb07c196eff0161` | `4845da492fcfce7c01f8283df2cecb241406a8523479e8217db466d4a3121ce2` |
| `common/scripted_effects/camp_repression_major_country_effects.txt` | `feb1f4cb747763879197a168dcaf948d40a0c5148872221933f34b656fa794a` | `f06d70ba87eb101dc17c90cd71bece89ee6a928465100ff0e64bf55f7ce5220` |
| `common/script_constants/camp_repression_rework_constants.txt` | — | `4c55a56e61f436b449a625c69e2f4b9fed2c3bcf67411e4918347d38980360e8` |

The probability tool's `sourceHash` values below are analyzer hashes, not raw file SHA-256 values; source provenance within the retained JSON artifacts records the snapshot bytes.

The before/after probability calls pin the event and decision source text with `snapshotPath` and `expectedSourceHash`.

Shared helper resolution uses the indexed workspace; the pre-existing `camp_rework_soviet_relief_resources_ready` helper referenced by the old source was unchanged in the archived before/current helper text, while the added after-source helpers resolve from the current trigger file.

## Candidate pools

Every event option has no explicit `ai_chance` block, so the offline Event Modding reference and the MCP adapter treat each option's default raw weight as `1`; this is default weight behavior, not a missing custom weight.

| Pool | Frozen before options | After options | Pool coverage |
|---|---|---|---|
| `soviet_gulag.1` | `.1.a`, `.1.c`, `.1.b` | `.1.a`, `.1.c`, `.1.relief_underway`, `.1.famine_eased`, `.1.b` | Complete local pool in each selected inspect/evaluate call. |
| `soviet_gulag.2` | `.2.a`, `.2.d`, `.2.b`, `.2.c` | `.2.a`, `.2.shortfall`, `.2.relief_underway`, `.2.famine_eased`, `.2.b`, `.2.c` | Complete local pool in each selected inspect/evaluate call. |

The semantic mapping for the renamed shortfall option is frozen `.2.d` → current `.2.shortfall`; the compare output counts one old identifier removal and one new identifier addition, but the shortfall outcome remains represented.

The current crisis pool also adds `.2.relief_underway` and `.2.famine_eased`; the warning pool adds the corresponding `.1` acknowledgements.

The whole event file has multiple categorical pools, so its aggregate inspect is not a single complete normalization pool; every event result below selects `soviet_gulag.1` or `soviet_gulag.2` and passes the complete local candidate list.

`probability_inspect` reports only `sov_emergency_famine_relief` for the decision query, which is complete relative to that single identifier but incomplete as an AI decision-choice pool.

The decision belongs to category `gulag_and_mass_repression_system`, which also contains Soviet choices including `sov_transfer_prisoners_to_industrial_camps`, `sov_reinforce_nkvd_authority`, `sov_reduce_paranoia_through_party_review`, `sov_release_prisoners_for_military_service`, `sov_dismantle_overextended_gulags`, `sov_conceal_famine_mortality`, `sov_admit_local_administrative_collapse`, and `sov_authorize_extreme_periphery_repression`.

Several of those decisions also use `constant:camp_rework_ai_weight.soviet_relief`; the one-decision score query cannot establish a category-wide rank, selection probability, dominance, or starvation result.

Mission `sov_emergency_famine_relief_mission` has no AI weight and `allowed = { always = no }`, so it is a mission-state gate rather than a weighted candidate.

## Named scenario set

The exact fixture is [`soviet_famine_shortfall_scenario_set_2026-10-03.json`](soviet_famine_shortfall_scenario_set_2026-10-03.json), SHA-256 `3442d0ee048981f7bf5a913bdb019c89254208b45d9da508551f56cf76e04aa`.

All eleven cases use date `1942.7.1` and political power `30`; the MCP-normalized scenario hash is `45f23eb01dea706865a912c047a20f133b3b3cab61a618e0b8f29b4440b6d210`.

| Scenario ID | Declared state |
|---|---|
| `SOV-funded-exact` | SOV, famine pressure `80`, stocks `120 motorized / 18 trains / 180 support`, crisis flag, responsible controlled target state `219`, controls `219=SOV`. |
| `SOV-motorized-short` | Same SOV crisis and target state, stocks `119 / 18 / 180`. |
| `SOV-train-short` | Same SOV crisis and target state, stocks `120 / 17 / 180`. |
| `SOV-support-short` | Same SOV crisis and target state, stocks `120 / 18 / 179`. |
| `SOV-short-no-target` | SOV crisis, stocks `119 / 18 / 180`, and no control map or `from` state. |
| `SOV-funded-no-target` | SOV crisis, stocks `120 / 18 / 180`, and no control map or `from` state. |
| `SOV-concealed-target` | SOV crisis and responsible controlled target `219`; target is a famine pressure site with records concealed and site undiscovered. |
| `SOV-discovered-target` | SOV crisis and responsible controlled target `219`; target is a famine pressure site with records not concealed and site discovered. |
| `SOV-active-relief` | SOV, famine pressure `80`, zero stocks, crisis and relief-active flags, and active mission `sov_emergency_famine_relief_mission`. |
| `SOV-stale-resolved` | SOV, famine pressure `0`, zero stocks, no flags, no active mission, and no target. |
| `invalid-GER` | GER actor and `original_tag`, famine pressure `80`, exact stocks `120 / 18 / 180`, and no SOV flags or target. |

For targeted cases the fixture provides root and `from` state `219`, control ownership, responsibility, and `scope.var:sov_famine_warning_state_id` / `scope.var:sov_famine_crisis_state_id` values; the analyzer still fails to bind the variable-to-state trigger references.

The fixture declares mission state as an empty mission-ID list in ordinary cases and the specific mission-ID list in `SOV-active-relief`; the analyzer still reports that it cannot compare `has_active_mission` with the declared value.

## Probability evidence

The immutable baseline event inspect artifact is `hoi4-agent://workspace/camp_famine_oct3/artifact/0229c355486f99bd22c5250241dfb881b41d4ec0ad0eed8762971c03ea1c4f56/0d6af2aae818cfa728d71cc3bef2a82c55815569dafdc2d2fc002cc1e68d9411/probability-inspect-723ebe829eb3.json` (`sourceRevision` `a818f615fdd437fc7b49f9c31f6d486364887cd08c5754ab3b4e1d61e3fcb753`).

Baseline event inspect found eleven option definitions across five pools and correctly reported the unqualified whole-file pool as incomplete; selected baseline pools were `.1` with three candidates and `.2` with four.

Current selected inspect artifacts are `.1` `hoi4-agent://workspace/camp_famine_oct3/artifact/b6785b8acd7d9ffa67bf47520334249239dad0ef67cae18b4400ce6c4b7ea1ae/87b6a1d9902dd89ee49628e608cc7290a19f62553713b556e6731f78a87a8fe4/probability-inspect-d7ae9a59d6ae.json` (`sourceRevision` `538cbca5392810050aa5b65eeb268c23077b48927a708080067c0d0b87b19e40`) and `.2` `hoi4-agent://workspace/camp_famine_oct3/artifact/392aa08a599ae287db87ac983348776a2f08aaebcf5372e912d6a4a9374db66c/1d472722005980ba1eafc7037232ca0f484e4650923dff0d707f405b86e7cea7/probability-inspect-d7ae9a59d6ae.json` (`sourceRevision` `93cbf7bec26d9f142a1a96b07b66b9ab045fa00a2d2d5ce392df96e054c347d9`).

Both current event pools inspect as complete locally, with five warning options and six crisis options; their event source is identified by analyzer source hash `d7ae9a59d6ae50fe1937083f3ef40b41a479ff0dfecd64a585918869553087fd` and provenance raw hash `58cecddff96fb888fc95f3e11d10e30a066e9e967f419bc23525fc665af6d3ed`.

| Surface and pass | MCP analysis ID | Scenario hash | Source revision | Rows and result coverage |
|---|---|---|---|---|
| Baseline warning evaluate | `probability-52f9cfe7e2d9a3cc205b7082` | `45f23eb01dea706865a912c047a20f133b3b3cab61a618e0b8f29b4440b6d210` | `533b7e19e121afd55506e195df3b12c79f182660267a450a66a5feb46ea6f59a` | 11 cases / 33 rows; 0 eligible, 5 excluded, 28 unresolved. |
| Current warning evaluate | `probability-6ab185d55ae98ef283fc8114` | `45f23eb01dea706865a912c047a20f133b3b3cab61a618e0b8f29b4440b6d210` | `8e8650737ee97f29aeb9f083d13b8aa853e6fb73bf03f16abc1282b3aa27df4b` | 11 cases / 55 rows; 1 eligible, 22 excluded, 32 unresolved. |
| Warning before/after compare | `probability-11c76d618f6a9b5f312960d7` | `45f23eb01dea706865a912c047a20f133b3b3cab61a618e0b8f29b4440b6d210` | `af02cf257ff0409c134b248a7685b5871b06dfdb005f0549fae198b8667c5ff7` | Partial; 55 current rows, 46 source/candidate changes, 1 eligible, 32 unresolved. |
| Baseline crisis evaluate | `probability-53cd23f26aba2de700c38ec1` | `45f23eb01dea706865a912c047a20f133b3b3cab61a618e0b8f29b4440b6d210` | `98fa2e02b9634e072e7067dfd9b3d671df68f3f682b342f13478573c6df4939a` | Partial; 11 cases / 44 rows; 0 eligible, 10 excluded, 34 unresolved. |
| Current crisis evaluate | `probability-9b0e0f33256751d8118e0c23` | `45f23eb01dea706865a912c047a20f133b3b3cab61a618e0b8f29b4440b6d210` | `bd912e29dac563b693eefe53cd0ee8eaa87c8028e16d3417bc2def04a270b09c` | Partial; 11 cases / 66 rows; 1 eligible, 27 excluded, 38 unresolved. |
| Crisis before/after compare | `probability-270e99fae717ed858f44f9d8` | `45f23eb01dea706865a912c047a20f133b3b3cab61a618e0b8f29b4440b6d210` | `cc77e61c6c01e507fff34655df8d2404091b4844819f18b43e4e78e1c9a5a062` | Partial; 66 current rows, 59 source/candidate changes, 1 eligible, 38 unresolved. |

The after warning evaluate artifact is `hoi4-agent://workspace/camp_famine_oct3/artifact/aea6f2bc286d5aa7f9ead7c01dafaff16babecde5b0307eee4a561560926dda4/a0ba36ac8a2922a6d12f6d897fe4e3034570f3a71ed68fb90124e29690c28c72/probability-6ab185d55ae98ef283fc8114.json`; its retained result and ranking, matrix, waterfall, and unresolved visuals are recorded in [`after-final-event-warning-evaluate-recovered-result.json`](../mcp/soviet_famine_2026-10-03/after-final-event-warning-evaluate-recovered-result.json).

The before/after warning comparison artifact is `hoi4-agent://workspace/camp_famine_oct3/artifact/16f39ce3e04f0e64d36c5b8d503c26be35b198e4bf6d0b99c51fbb5aae8b04a9/38e254c7a52f6efbfdcd69ae71f57ea1eaf825798243b7a67d45f34fe43ad757/probability-11c76d618f6a9b5f312960d7.json` with comparison SVG `hoi4-agent://workspace/camp_famine_oct3/artifact/01baadc17fd7c91a20add87909c82fddc62089ae241080ee87c6775bfaf0dadc/4f66b252e0ac9fe097b2308bb24532e8e92cbbc787d9698f76b4b7e89b932295/probability-probability-11c76d618f6a9b5f312960d7-comparison.svg` and PNG `hoi4-agent://workspace/camp_famine_oct3/artifact/cc282678c7925b1b0b7bbf1f5bd897074bff53bc230ac324bfa9475e3cbd42e8/c78d93d423bf87655269f471405075a465214385632110f109c0d69ada59540d/probability-probability-11c76d618f6a9b5f312960d7-comparison.png`.

The after crisis evaluate artifact is `hoi4-agent://workspace/camp_famine_oct3/artifact/ffcf5121210db9f065cedd096280ec98c1e2b57f3dab3b0558d43c97faddc48b/476eefceaef7503703058007767101cf71d9e0d475dd67154ca271db1e6c46b0/probability-9b0e0f33256751d8118e0c23.json` and the crisis comparison artifact is `hoi4-agent://workspace/camp_famine_oct3/artifact/bfd40f7753d908ea7079cfd6540a2d536188d41b463ff8131dba6c8fc6f20d0a/11f1ab038c40436e3cedfcb118fbacfddaeebd8496a214f4f4b212aab20f5e5f/probability-270e99fae717ed858f44f9d8.json`.

The crisis comparison SVG is `hoi4-agent://workspace/camp_famine_oct3/artifact/0d3aa823ced74b2249134ce5fc1ec53c5f80f2fba1663650d54e37099f05c398/01e0cb5a53d597e5d9489fdc8a50f347781d913c2ef47e133f8ed8accd34a4ca/probability-probability-270e99fae717ed858f44f9d8-comparison.svg` and PNG is `hoi4-agent://workspace/camp_famine_oct3/artifact/072aa5d6a4200c3bce4e2f80f62fd6229a1c8e5cc4f8a24918fd2ff81ebc688a/90c0e32a3a6ae09f5e18135060a2b8a9505c09b54d45c4ab9bcce0901d936de2/probability-probability-270e99fae717ed858f44f9d8-comparison.png`.

In both current event comparisons, `SOV-active-relief` is exact: only `.1.relief_underway` or `.2.relief_underway` is eligible and its conditional share is `1` under that declared scenario.

Normal exact-funding, each one-unit-short stock case, target-free cases, target-state cases, and stale-resolved cases do not yield exact shares.

For those cases, the adapter reports `has_equipment` as undeclared despite the fixture's three typed stock counts, `has_active_mission` as incomparable despite its mission-ID lists, and `var:sov_famine_warning_state_id` / `var:sov_famine_crisis_state_id` as undeclared despite the explicit state `219` aliases.

The crisis comparison reports 44 `UNRESOLVED_ANALYSIS_INTRODUCED` regressions, all attached to those newly analyzed gate expressions; this is an analyzer-coverage regression signal and does not prove that engine eligibility regressed.

Both event comparisons emit `EVENT_OPTION_FALLBACK_NOT_PROVEN` because all discovered options are gated.

Both comparisons also report a dominant outcome in `SOV-active-relief`, which is the exact relief-underway acknowledgement, and in `invalid-GER`.

In `invalid-GER`, the analyzer assigns conditional probability `1` to `.1.a` and `.2.a` while also reporting that each candidate has eligibility `false` and raw weight `0`; this contradiction is an adapter anomaly and is not a valid AI selection result.

## Decision score

The before decision inspect artifact is `hoi4-agent://workspace/camp_famine_oct3/artifact/d62b502a89e231741bcceae589cde893775812710468f3cf426c6a465ce9ea8b/5254cf6232b4a052c96f9c5e17376443883649c8365d111ba65949c7a394af4b/probability-inspect-8f12812be499.json` (`sourceRevision` `efadc3f0a4f32207e9883da42ca9e0d716a3bbea3fba342d7ecb6f11ddddffd3`).

The after decision inspect artifact is `hoi4-agent://workspace/camp_famine_oct3/artifact/44b5b7a5907b5b8d699f314cf1d696c777f581252ce16d27a9f7db57700bf622/f533672c3e6bfde1c9d6f1630c9f6c694e03fa8f803a0f7811e7c71d6831dd71/probability-inspect-8bb161884b4d.json` (`sourceRevision` `c0c9dc5b9dfd7ee4a647b141c95d8cae6f5373a3e2eeb484b6631ff2ff44b5b4`).

Both inspect one candidate and require `has_active_mission` and `scope.has_equipment` inputs.

The score source is `ai_will_do = { base = constant:camp_rework_ai_weight.soviet_relief }`; that constant remains `40.00` in `common/script_constants/camp_repression_rework_constants.txt`.

The final before/after decision comparison is `probability-e7f2f0199c3448e9935c1303`, scenario hash `45f23eb01dea706865a912c047a20f133b3b3cab61a618e0b8f29b4440b6d210`, and source revision `e8197e556b86184a82dcd13e0cbd0f9840df8d4693c18b3c58c4f7e7eca3ec10`.

It reports zero score changes across eleven scenarios; all non-active rows retain raw value `40`, and the active relief row is excluded with raw value `0`.

Every row is classified `score_only`; conditional selection probability is null because this is one candidate within a larger category and the availability inputs remain unresolved.

The comparison JSON is `hoi4-agent://workspace/camp_famine_oct3/artifact/49f230cad45e93990c9ca7853aa00c37433b4c55320a851ec8e417cddaab4d13/10fac871f2ceba5dfd66074639008ca31817d4b238d5a382bae3795733d62a44/probability-e7f2f0199c3448e9935c1303.json`; its comparison SVG is `hoi4-agent://workspace/camp_famine_oct3/artifact/2450d67f32f665574260ffbd84f57cc7db1a9cf58aca09b66d13c1108a27cc49/50efbbd8df2a40b8f58252c596b20cb6daa647e41874fc1a79c32d595e1e920f/probability-probability-e7f2f0199c3448e9935c1303-comparison.svg` and PNG is `hoi4-agent://workspace/camp_famine_oct3/artifact/a1fd8e11d21dd2414c85f7412d454fa53b5b857ed9fb09593caa20f6277f498f/9c4d114cec7b51855b060a79fb14c79998d6b4209e249ed8fbfeb55fa5e3037d/probability-probability-e7f2f0199c3448e9935c1303-comparison.png`.

The adapter does not establish decision availability or a click probability, and the one-candidate result cannot answer whether another Soviet decision outranks relief in the shared category.

The relief mission itself has no AI score and is `allowed = { always = no }`.

No claim is made about an actual 30 PP debit; this probability pass evaluates the decision AI score and source gates, not live engine payment behavior.

## Sweep and render evidence

The current warning sweep is `probability-a05fc4416474843feae081cc`, scenario hash `5fd0c25b88a5162bb96e90420641358e5a7232645eaa6cdc0bb18075cd949e2d`, source revision `9a51a8066e102994619cb0c6a1360031a5d0c6ef09eaf2f0a2b40815dba68db2`, and 25 points.

It sweeps `variable.famine_pressure` and the compound `scope.has_equipment`, both over declared `0..1` ranges with five steps; this is a coarse gate sensitivity, not a stock-specific sweep or a full famine-pressure scale.

The sweep returns no breakpoints, no local elasticities, and no rank reversals; three of five outcomes remain unresolved and no conditional probability is produced.

The result is classified `partial` with `poolComplete = true` for the selected five-option warning pool, but its gates remain unresolved.

The sweep's `PROBABILITY_OUTCOME_NEVER_ELIGIBLE` warnings for `.1.b` and `.1.famine_eased` are limited to that one gate-boundary sensitivity scenario and do not establish that either option is unreachable in the full eleven-case set.

The sweep result JSON is `hoi4-agent://workspace/camp_famine_oct3/artifact/b263dd009acc6ba1d68ede36f1ac014fb25d13987dff58918da712210457c569/623f11c66c989682bae7bcf05c52ec8ae918c07cdbd48b053d1cad95f6f7e6c6/probability-a05fc4416474843feae081cc.json`; sensitivity SVG is `hoi4-agent://workspace/camp_famine_oct3/artifact/3296ed01f59314ad043e1d9052bd6366e47a8947ecf98d90251f106c52c5e5ae/5116d90ea3b97ba11c71a281305a42d548bee902a2d4c77176f84734da25594e/probability-probability-a05fc4416474843feae081cc-sensitivity.svg` and threshold SVG is `hoi4-agent://workspace/camp_famine_oct3/artifact/a6d32ffc270e06218fbe6e53b5f3d111d3f383d152a2e17fa057722f7cf35cc8/29b42b69daa470e6e45afe9bca0235e95d70b5d2471f793a85c74ee307d75e22/probability-probability-a05fc4416474843feae081cc-threshold.svg`.

Current crisis sweeps with the full two-path set and a narrower `variable.famine_pressure`-only sweep both terminated with `INTERNAL_ERROR` and produced no artifacts.

Current decision sweeps with the full two-path set and a narrower pressure-only sweep also terminated with `INTERNAL_ERROR` and produced no artifacts.

| Sweep request | Durable job handle | Result |
|---|---|---|
| Current warning, 25 points | `camp_famine_oct3:job_6b58d0350a1f7508cc677c4ed66812a1e8c012d1ca0676ea39a04b7d99bb7deb` | Completed partial. |
| Current crisis, full two-path grid | `camp_famine_oct3:job_43e86a94c54d361b5351075782abe5e4f9672de6528c417f785d788b32f11826` | Terminal `INTERNAL_ERROR`, no artifacts. |
| Current crisis, pressure-only grid | `camp_famine_oct3:job_e4f458ba69a4c1549d2ab72c51e738ec804334b3656167f4e02dc30324680528` | Terminal `INTERNAL_ERROR`, no artifacts. |
| Relief decision, full two-path grid | `camp_famine_oct3:job_99e43c175b28b46693c5ec931c15cb8356128969d387d20bd44839e81839031d` | Terminal `INTERNAL_ERROR`, no artifacts. |
| Relief decision, pressure-only grid | `camp_famine_oct3:job_63b7d7b622e6b3e4afff8e6dd6ff02c7951494b3b3e6b20536be1c2bbe8944e4` | Terminal `INTERNAL_ERROR`, no artifacts. |

The exact requests and terminal responses are retained in [`final-event-warning-probability-sweep-task.json`](../mcp/soviet_famine_2026-10-03/final-event-warning-probability-sweep-task.json), [`final-event-crisis-probability-sweep-task.json`](../mcp/soviet_famine_2026-10-03/final-event-crisis-probability-sweep-task.json), [`final-event-crisis-probability-sweep-famine-only-task.json`](../mcp/soviet_famine_2026-10-03/final-event-crisis-probability-sweep-famine-only-task.json), [`final-decision-score-probability-sweep-task.json`](../mcp/soviet_famine_2026-10-03/final-decision-score-probability-sweep-task.json), and [`final-decision-score-probability-sweep-famine-only-task.json`](../mcp/soviet_famine_2026-10-03/final-decision-score-probability-sweep-famine-only-task.json).

Those four terminal results are saved as [`final-event-crisis-probability-sweep.json`](../mcp/soviet_famine_2026-10-03/final-event-crisis-probability-sweep.json), [`final-event-crisis-probability-sweep-famine-only.json`](../mcp/soviet_famine_2026-10-03/final-event-crisis-probability-sweep-famine-only.json), [`final-decision-score-probability-sweep.json`](../mcp/soviet_famine_2026-10-03/final-decision-score-probability-sweep.json), and [`final-decision-score-probability-sweep-famine-only.json`](../mcp/soviet_famine_2026-10-03/final-decision-score-probability-sweep-famine-only.json).

The explicit `probability_render` request for the warning comparison returned `PROBABILITY_ANALYSIS_STALE` with zero visual resources; the crisis comparison render request timed out with MCP `-32001 Request timed out`.

The compare tools themselves returned the comparison SVG/PNG artifacts listed above, and the warning sweep returned its own sensitivity, threshold, ranking, matrix, and unresolved SVG/PNG artifacts.

Structural `event_inspect` and `event_render` calls ran in focused mode without helper expansion; they retained revisions `01fa0f1bc4c157c7879f95717aa33f00e7b0b10fff65f26404cc9c59a117e7a9` and `810ac1e3a8972e394810c2d2a6fee3d6aa9d53e4b3257d8b351256e964f2bb17`, each with zero expanded helpers and 8,958 unresolved nodes.

The warning options render is `hoi4-agent://workspace/camp_famine_oct3/artifact/2eb556e16f6ef6c5a7967d52ef4e8307306895c60e1dcb67242734023dbf9637/e4842fe97e86c4bf4c9d8a31fb320f3c1b2487031da22fa08d1772f4ee152c92/event-options-01fa0f1bc4c1.svg` with PNG `hoi4-agent://workspace/camp_famine_oct3/artifact/c2f4ff46e3f96f94b859823ba32255a92604a04206bb53fa1e631e8fd9382380/5b7987c0607362a6416d3ab5c76da626c0738384e7c5e3c823339d6fe9afea70/event-options-01fa0f1bc4c1.png`.

The crisis options render is `hoi4-agent://workspace/camp_famine_oct3/artifact/acf041acde5baa9f453c9467f798e3ed978f3f1bea0e644a843aacccf060b5a2/2501ce16aca1b64bea2a987dedfaaba079c46ea7debaf3c64a84f3acbdfb0fa9/event-options-810ac1e3a897.svg` with PNG `hoi4-agent://workspace/camp_famine_oct3/artifact/a38fe950a2452e897b24e568d0f7efdc7e567d3b796783978466526f75cee2c9/371b05e0da6da344b3a363702f0104a3de35c0235b7224be84b5a31f244c994d/event-options-810ac1e3a897.png`.

The event renders are partial graph views with thousands of unrelated graph diagnostics, so they document the selected option neighborhood only and do not establish full event-chain lifecycle coverage.

## Interpretation and recommended follow-up

The current event option raw weights remain equal at the engine default `1`; there is no probability evidence for changing them.

The relief decision remains at score `40` before and after, as authorized; this is a score comparison, not a normalized click probability.

Do not treat the analyzer's `invalid-GER` probability `1` as a valid outcome; the same row explicitly says the option is ineligible and has raw weight `0`.

For exact funding and shortfall conclusions, the analyzer needs typed `has_equipment` inputs that map to all three equipment rows, mission-ID state it can compare, and a supported binding for the saved state-variable target references.

For a decision-choice comparison, the candidate pool must include the other currently available decisions in `gulag_and_mass_repression_system` with their own scenario gates; this audit deliberately reports only the relief score.

The `EVENT_OPTION_FALLBACK_NOT_PROVEN` warning warrants checking the actual full trigger partition when engine-model coverage is improved; the available adapter results do not prove that a production popup is stranded.

No simulation was run because no probability distributions or sampled uncertain inputs were declared, and no sequence analysis was run because these surfaces do not define a custom weighted pool with cadence and terminal transitions.

Both famine events are `is_triggered_only = yes`; no event MTTH weight or timing distribution is in scope.

## Reference and route notes

Offline Event Modding, options and `ai_chance` default behavior, `paradox_wiki/Event modding - Hearts of Iron 4 Wiki.md` lines 153–179, revision `96327b896298420d84058394a44ed08be7eb518726b8f207b392fea71f05d43d`.

Offline AI Modding, MTTH score interpretation, `paradox_wiki/AI modding - Hearts of Iron 4 Wiki.md` lines 26–37, revision `917cd261f7da51fe4d8687c5d7663e768a09c5c101ac130ce646bc64637aa818`.

Offline Decision Modding, `ai_will_do` selection scores and defaults, `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md` lines 357–374, revision `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162`.

Offline Decision Modding, native and custom costs, the same page lines 284–336 and revision above; this reference does not prove a live PP debit for the current mixed-cost decision.

Offline Triggers, `has_equipment`, `paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md` lines 1509–1583, revision `abc51ad18a2c46e46d47baa795c5a840ebaf7c4ae3e777426c64a9f4c0c0ce06`.

Installed decision documentation, `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/decisions/_documentation.md` lines 1–46, revision `5e7e686b5582f32c38d898d805e17171e88f3bfeee4a030deb1884f9726de019`.

Installed trigger documentation, `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/triggers_documentation.md` lines 3835–3843, revision `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29`.

Vanilla precedent was read locally from `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/decisions/AFG.txt`, decision `AFG_recruit_turkestan_legion`; it manually consumes custom-cost equipment, but does not establish payment behavior for this famine decision.

The direct `hoi4.source_lookup` request for that bounded vanilla decision timed out with MCP `-32001 Request timed out`; the parent also observed the broader request timing out, so the local vanilla file read is retained as the reference and the source-lookup route gap remains recorded.

## Remaining uncertainty

The standalone final after-decision evaluation task `camp_famine_oct3:job_5724fe05dade4de4b413042b5b7f2004e51b76bb507ecb725843804209bc70e8` and structural event comparison task `camp_famine_oct3:job_936962176c3676bb98cf97200648c809a352d22a485547ced2c07cb270d6a690` both ended `INTERNAL_ERROR` without artifacts; the decision before/after compare itself completed successfully.

No game session or game logs were used, and the MCP results model source scenarios rather than observed engine execution.

The event option, equipment, mission, and target-state questions listed above remain unresolved until a supported adapter input path can represent the source conditions.
