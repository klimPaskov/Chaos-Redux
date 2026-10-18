# Public Works populated WKS v2 probability evidence

Status: The bounded nine-case before/after probability comparison completed as partial native evidence; it is not a balance pass or a full Event 035 completion claim.

The owner reports source commit `19d3d0a59a4b3a14b45bec4d86b02dd3179e1ec0`, frozen source, and 87 source tests passing; this auditor did not run the test suite.

No gameplay, AI, event, localisation, asset, spreadsheet, test, or Git file was edited by this auditor.

## Frozen sources and current shared helpers

The immutable before decision snapshot is `docs/plans/035_great_depression_plans/audit_inputs/public_works_2026_10_07/before/decisions.txt`, SHA-256 `C99B4C5498494D187E3E81712756F20FE812E7DB7713D756A2FF6E9B25279067`.

The immutable final-owner after decision snapshot is `docs/plans/035_great_depression_plans/audit_inputs/public_works_2026_10_07/after_owner_final/decisions.txt`, SHA-256 `AA6357DB29620998A29C7FD666857D3F95106F362C2099F8673C754EC94DAB14`.

The immutable before surface-trigger snapshot is `docs/plans/035_great_depression_plans/audit_inputs/public_works_2026_10_07/before/surface_triggers.txt`, SHA-256 `27BC69FC602B9C553E6A9E95820595BF16D6F5CC251C1588D75311C2E7F201FA`.

The immutable final-owner after surface-trigger snapshot is `docs/plans/035_great_depression_plans/audit_inputs/public_works_2026_10_07/after_owner_final/surface_triggers.txt`, SHA-256 `80C139E893740963248DB726C264FBD36C682A2BDABF39ABACD0A1E7BC85255A`.

At audit closure, `common/decisions/035_great_depression_decisions.txt` still matched the final-owner decision snapshot and `common/scripted_triggers/035_great_depression_decision_surface_triggers.txt` still matched the final-owner surface snapshot.

The separate current helper `common/scripted_triggers/035_great_depression_public_works_triggers.txt` is now SHA-256 `6AECF24598D19608BF64C00479E674CCFF2B7CE5F9ECA25E058A60F52056CA80`; the previously reported `C204327CF9ADD639B31DD26997C8573EEF738E278E96125B9215E3472F2DEBA0` is historical.

The owner describes the intervening helper change as a pure type-proof guard with no AI-weight or target-eligibility change; it is current shared-source evidence, not a frozen before/after snapshot.

The current decision weights and numeric coefficients were not changed by the owner patch; the Public Works AI factor-zero predicate changed from the doomed classifier to Liquidated only, while other doomed consumers remain unchanged.

## Scenario fixture and grounding

The original empty nine-row scenario fixture remains immutable at `after_owner_final/wks_scenario_set_2026-10-08.json`, SHA-256 `ACD378F02CFDA3E9861148F08F30C54B68791560F907764413BEB9951A621BA4`.

The first populated fixture, written before the initial inspection/evaluation, is `wks_scenario_set_2026-10-08_v2.json`, SHA-256 `E0B5DBAB550FCBD7D1BB34F4B0BED81482F7136A2C33705FB3398CA7D4D5636`.

After the first one-case evaluation identified real missing scenario inputs, the final nine-row compare fixture was frozen as `wks_scenario_set_2026-10-08_v2_bound_r1.json`, SHA-256 `9C3123A32D3A52A19573A90FF600B710573A814189EB81CDADD1C223F2C0328C`.

The bound-r1 set preserves exactly these nine IDs: `WKS-DISTRESSED-NEED`, `WKS-IDLED-NEED`, `WKS-SHUTTERED-NEED`, `WKS-REOPENED-NEED`, `WKS-HEALTHY-NO-NEED`, `WKS-ACTIVE-PROJECT`, `WKS-FOREIGN-CONTROL`, `WKS-EPISODE-MISMATCH`, and `WKS-LEGACY-REPEAT`.

The separate Abandoned eligibility fixture is `wks_abandoned_conversion_2026-10-08_v2_bound_r1.json`, SHA-256 `86F0B71C75D8685753F8939DEFC87CF9AE38603AE0290012A48113138297FCDF`; it is not included in the nine-case comparison.

The separate in-memory source-runtime Abandoned proof record is `abandoned_conversion_source_runtime_2026-10-08.json`, SHA-256 `11CACCA8A65722656EF95F5BBD6D43B6EDD34634F0D787AB0094078539D9E504`.

The live HOI4 Agent Tools server reported version 3.10.0; the inspected probability scenario schema accepts numeric/boolean/string/scalar-array state values, typed `scopes`, and `controls`, while the probability scenario schema is strict and does not accept `closedFlags`.

The final scenario binds root actor GER, typed `scopes.FROM = { id: "64", type: "state", flags, state }`, and `controls["64"] = "GER"`; the target scope intentionally omits its optional `actor` field so its scope identity remains state ID `64` for center-array membership.

The state-array binding is `array.ROOT.great_depression_center_state_ids = ["64"]`, script variables use `variable.<name>`, and native trigger inputs use `trigger.<name>`; no `candidateOverrides`, synthetic `scope.*` values, or derived eligibility helper keys were inserted.

The final fixture declares the requested hypothetical actor inputs: active crisis, episode 35, severity 45, peak 55, evolution 0, phase 1, Emergency Public Works doctrine, Relief Coalition AI profile enum 1, selected center 64, current registry array/index, PP 500, manpower 500,000, fuel 5,000, trains 500, support equipment 500, convoys 500, available project civs 20, peacetime, and no active project/action lock.

The source cost refresh executed by `.tools/test_event035_public_works.py::PublicWorksTests.prepared` returned factor 1.0, civilian 1, PP 25, manpower 500, fuel 500, trains 2, convoys 3, support equipment 10, stability 0.03, and war support 0.02 for 20 available project civs.

The reopened WKS target declares state 64 as owned and controlled by GER, capital/inland, industry 3, arms factory 1, infrastructure 2, population 8,000k, and zero measured infrastructure/rail/port/anti-air building damage; these are explicit hypothetical overrides, not claims about a live campaign.

The installed vanilla map source `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\history\states\64-Brandenburg.txt` has SHA-256 `3BD06F88BA34DD9E81927820768FD3E90EC4532E3928552A34FF8B80B4666B6F` and records state 64 as Brandenburg, owner/core GER (also core PRE), with Berlin at victory-point province 6521, state category megalopolis, and the listed 16 state provinces; its default 1936 building levels and manpower are not the user-requested hypothetical values.

The bounded map lookup returned `MAP_LOOKUP_COMPLETED`, one state inspected, map revision `7ef63472bc500f0e00ec9fe8d8a38488a45b3654b4209aa53e598719116cc819`, and artifact URI `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bb77e13294bc1d10d0b31fcd1a84dca1d4dd41e674da3dc77a2f7eb076a74c2e/b443b65b100fff03e6cc6b6dd09107fe6a90b0ea82953d30bb78b2310a172a29/map-lookup.7ef63472bc500f0e.8d030eb3664782be.json`; a subsequent bounded resource read reported that its provenance manifest was unavailable, so the local vanilla state file is retained as the directly read shape evidence.

The added normal-country source inputs were `num_of_factories = 4` (the declared target has three industrial and one military factory), `infantry_spawn_derivative_family_id = 0` (the source enum's `none` value), zero contagion-source count, zero inactive worldwide episode/stage sentinels, zero current/failed project authorization IDs when no project exists, and native state identity `trigger.state = "64"`.

The installed evaluator does not support nested `has_equipment` blocks or enumerate `any_controlled_state`, `any_owned_state`, `any_neighbor_state`, or `has_railway_connection` from a single typed target binding; the declared equipment stocks do not override those unsupported compound constructs.

## MCP evidence

`hoi4.probability_inspect` ran first for adapter `decision_ai_will_do` and candidate `great_depression_launch_regional_works_program` against the live logical decision source, whose source hash was `bdfd85b4be5fb2cbf15aa58e6f1e0c35554877365461b823d6cbf3a427e0a23c` and source revision was `549bd731bef0cfa7b3e525b4a703445a5424a4aea3496177ba71b63c3c250e27`.

The inspect returned `PROBABILITY_SOURCE_INSPECTED`, one filtered candidate, `poolComplete = true` only for that singleton filter, no available candidate without scenario input, zero discovered required-input paths, and zero source unresolved entries; the empty required-input list did not prove scenario completeness.

The probability-inspect artifact SHA is `539825d12fe05eaa9040b38d27994e3c0ba92ae0526ac0747b72b567f2020298`, size 69,864 bytes, URI `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/539825d12fe05eaa9040b38d27994e3c0ba92ae0526ac0747b72b567f2020298/70fe5ef5208eb14d4c1daff6ddde9854f269bfc941a6b4b4bd5972ce47f413c5/probability-inspect-bdfd85b4be5f.json`.

The requested single-case `decision_inspect` used `id = great_depression_launch_regional_works_program`, one `WKS-REOPENED-NEED` scenario with actor GER, numeric/native root state, `controls["64"] = "GER"`, and typed `FROM` state ID 64 with stage flags and target state values; it was accepted rather than rejected.

That decision inspection returned `DECISION_ANALYZED_PARTIAL`, scenario count 1, `complete = false`, 8,316 decisions, 2,070 categories, 100 unresolved definitions, report hash `5961f48f404cdf490f83a3117aba296ea5119d183bcc59e80032ab1bb55693a9`, and source revision `be3e6efd130e607a1525897241e5e27f79fd408911fcc160f1220d0d0d95cae8`.

The decision-inspect report artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5be8284a170a8479f4bd9d3d48c2329b6f5ae404380e53fbe248d0927e9f3a63/78013228d6b37795725c635261104b058944976b96e311c22cd183aa20bb8f0e/decision-5961f48f404cdf490f83a311.json`, SHA-256 `5be8284a170a8479f4bd9d3d48c2329b6f5ae404380e53fbe248d0927e9f3a63`, size 1,638,913 bytes.

A first decision-report resource request declared a 1,048,576-byte range but returned only 35,196 decoded bytes, so the chunk failed required byte-range verification; the narrowed 32,768-byte retry returned `MCP error -32603: Artifact provenance manifest is unavailable`, and no contents from that report are used as evidence.

The initial populated one-case evaluate over `WKS-REOPENED-NEED` reduced the unbound-input report from 56 in the prior empty-map case to 20, but still left eligible/excluded status unresolved; it was superseded by the bound-r1 one-case evaluation below.

The final bound-r1 `WKS-REOPENED-NEED` evaluation returned `PROBABILITY_ANALYZED_PARTIAL`, one candidate, zero eligible and zero excluded, seven unresolved, `eligibility = unresolved`, `conditionalProbability = null`, and no verified `rawValue`.

The reopened evaluate analysis ID is `probability-0f41cc48b24e50302b442a8d`, scenario hash `f9a6a16e81e489c1ba1f323720ca8b6a229497162e19c17a05ed848cd8e490b2`, source revision `1ef67fade664809bbd3fd0713f677894402e33c63e417b4af5da5ae9f915bffd`, source hash `bdfd85b4be5fb2cbf15aa58e6f1e0c35554877365461b823d6cbf3a427e0a23c`, and artifact SHA `1038dbd24ed4e5023499c08db3d33fcf4a22880086d7498c52f443e8e3ff6c37` (168,702 bytes).

The reopened evaluate JSON URI is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1038dbd24ed4e5023499c08db3d33fcf4a22880086d7498c52f443e8e3ff6c37/f35658d4a1f48db6886dd504571f328f995ae127e7beae32f043b3a30033da72/probability-0f41cc48b24e50302b442a8d.json`.

The mandatory compare used the exact same bound-r1 nine-scenario object for both sources, one candidate decision, `refresh = false`, and frozen before/after decision snapshots with their expected SHA-256 values.

The compare returned `PROBABILITY_ANALYZED_PARTIAL`, nine scenarios, one candidate per scenario, five excluded candidates, zero eligible candidates, four unresolved candidates, seven unresolved input classes, and zero comparison changes; `conditionalProbability` was null for all candidates.

The compare analysis ID is `probability-06f8ab56f5d2d45ea1b8613f`, scenario hash `fe057cacc3486d00b0df4c513d1c5678dfdf05d571006da66e08adefdd2414ec`, analyzer source hash `4d061168307dd413daa2aa08c1792828d1537cb79de29ce076097b5737ff08a8`, and source revision `d56b3d1a9da1fc6dec08e10a1739951e6d7e113881502590f4cf98de154ff6db`.

The compare JSON artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/38f1306c99dc50b8220feefea76bc1e203da4793d7e65075f74cf5ea4912895c/f0dfe302071876e60c3be8e7c0b115e2955c869d480c6f0a4a3a987e290c4/probability-06f8ab56f5d2d45ea1b8613f.json`, SHA-256 `38f1306c99dc50b8220feefea76bc1e203da4793d7e65075f74cf5ea4912895c`, size 1,444,213 bytes; it was assembled from gap-free 32,768-byte ranges and its final byte count and SHA matched.

The compare tool emitted comparison SVG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2450d67f32f665574260ffbd84f57cc7db1a9cf58aca09b66d13c1108a27cc49/e6592b688814cb7df6943d2d0cb01de8b1fe15f198a652c17f6be8724b4dae14/probability-probability-06f8ab56f5d2d45ea1b8613f-comparison.svg` and PNG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a1fd8e11d21dd2414c85f7412d454fa53b5b857ed9fb09593caa20f6277f498f/6d4ccd9c6f7c66fbf4caf65db7d2f07079511370141cf5915c47524ba36edfeb/probability-probability-06f8ab56f5d2d45ea1b8613f-comparison.png`.

The compare tool also emitted unresolved SVG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c43b2f3bf79384327bef50958240c37a5bda78b88729cee00737037f709a1940/e72c951710690ede1f0768f94e5a2ed8a488b6db426fe6e0db34dcfa4b9a5413/probability-probability-06f8ab56f5d2d45ea1b8613f-unresolved.svg` and PNG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8e6861a6cd8c1ed13fdc7f02d52d4e77f5c7ee9601d26746acf02d4509a741c7/df89365df1da6412adb5efccb54f384dde5f90b602810e5974a2ff5c97e19d7a/probability-probability-06f8ab56f5d2d45ea1b8613f-unresolved.png`.

The scenario rows are:
| Scenario | MCP eligibility | Numeric interpretation |
| --- | --- | --- |
| `WKS-DISTRESSED-NEED` | unresolved | No raw score; conditional probability null. |
| `WKS-IDLED-NEED` | unresolved | No raw score; conditional probability null. |
| `WKS-SHUTTERED-NEED` | unresolved | No raw score; conditional probability null. |
| `WKS-REOPENED-NEED` | unresolved | No raw score; conditional probability null. |
| `WKS-HEALTHY-NO-NEED` | false | Reported raw zero is an exclusion placeholder, not an AI score. |
| `WKS-ACTIVE-PROJECT` | false | Reported raw zero is an exclusion placeholder, not an AI score. |
| `WKS-FOREIGN-CONTROL` | false | Reported raw zero is an exclusion placeholder, not an AI score. |
| `WKS-EPISODE-MISMATCH` | false | Reported raw zero is an exclusion placeholder, not an AI score. |
| `WKS-LEGACY-REPEAT` | false | Reported raw zero is an exclusion placeholder, not an AI score. |

The unresolved scope paths are `scope.any_controlled_state`, `scope.any_owned_state`, `scope.any_neighbor_state`, `scope.has_railway_connection`, and `scope.has_equipment`; the last repeats for multiple actual equipment consumers.

The four need scenarios are not confirmed eligible because the evaluator cannot model the remaining target/pool scope constructs; the five exclusions correspond to the explicit no-need, active-project, foreign-control, stale-registration-episode, and completed-receipt guards.

The separate after-only `WKS-ABANDONED-CONVERSION` evaluation returned `PROBABILITY_ANALYZED_PARTIAL`, one unresolved candidate, zero eligible and zero excluded, seven unresolved inputs, no raw score, and null conditional probability.

The Abandoned evaluation analysis ID is `probability-17f3e7f587d7bc5f025d428e`, scenario hash `bd732069ac6e8acba9244b933439494dee6f313d64bac279f02afc8ff44d5879`, source revision `e1ebc78d3a3023f40d62ad143533dc6110fda70ff6ec11583ca18799e5ae22e2`, artifact SHA `6b75e0258efd46e3f79f4965b3b955f12ae6ebc2d2ce0e60de25c5a445e202c5`, size 170,194 bytes, and JSON URI `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6b75e0258efd46e3f79f4965b3b955f12ae6ebc2d2ce0e60de25c5a445e202c5/06544c3e7aa698625e24cd19c46013a30ace21071c6f915bcb4464cf54de53dd/probability-17f3e7f587d7bc5f025d428e.json`.

The separate source runtime produced Abandoned plan kind 9, local-demand baseline 4 before payment, and a persistent `great_depression_public_works_abandoned_conversion_proven` receipt after local demand fell to -1 and the center reopened; the runtime fixture was AAA/state 121 and is source-only, not a native GER/state-64 observation.

## Classification, limits, and completion

The AI adapter reports a willingness score, not a click probability; the four unresolved candidates have no verified raw numeric score and none has a conditional selection probability.

The scenario candidate pool is complete only for the singleton decision filter in each scenario; the 96-child decision category and full state-target selection race were not supplied, so no normalization, ranking, dominance, starvation, or click probability is claimed.

No coefficient sweep was run because the owner changed no numeric coefficient or threshold and the full target pool remains incomplete; no simulation or sequence was run because no uncertain-input distribution or cadence manifest was declared.

An explicit `hoi4.probability_render` call for the comparison returned `PROBABILITY_ANALYSIS_NOT_CACHED`; the compare and evaluate calls themselves emitted the comparison and unresolved SVG/PNG artifacts retained above.

The baseline source recommendations remain source-level only: Public Works need and stage cases behave according to the frozen owner patch, but this bounded comparison does not certify full AI balance or Event 035 completion.

No source patch, coefficient change, WKS fixture simplification, full 96-child pool trace, HOI4 launch, log request, or native campaign claim was made by this auditor.
