# Event 23 test-accident probability baseline — 2026-09-26

Status: read-only baseline recorded; numerical probabilities remain unresolved. No gameplay or spec files were edited, no weights were tuned, and no commit was created.

## Decision and audited surface

The current user decision is that a test accident defaults to a no-yield high-explosive or preparation accident; true nuclear yield is permitted only after a rare catastrophic low-integrity physical severity gate. Evolution timing tuning is deferred and was not analyzed or recommended.

Audited surface: the four-entry `random_list` in `sov_nuclear_bombs_prepare_test_outcome` in `common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt` (pool at lines 798–802), with tuning in `common/script_constants/023_sov_nuclear_bombs_constants.txt`.

The test-outcome draw is conditional on the scripted effect’s test-action and nonce preconditions. This baseline does not estimate test preparation frequency, event timing, or whole-campaign accident incidence.

| MCP candidate ID | Outcome |
| --- | --- |
| `common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt:798.entry.1` | Success |
| `common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt:798.entry.2` | Partial yield/data |
| `common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt:798.entry.3` | Failed detonation |
| `common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt:798.entry.4` | Accident |

## Source identity

Local SHA-256: effects file `C3F3BA0ACA7C5FEFE0B5BE84704ACE1C292BB146E32BADDA896FC2FA35D3FEB5`; constants file `073BC77FB14B4FC6D2CCF0CE8EC46939E96EE62DC9EE201B12C1A04F50F097CE`.

Git blob IDs: effects `84c38e149b3732f10a4d03c2cc36e90ec0d5a6a9`; constants `6dc921190f569e4a90ff247d64d88601866a712c`. The repository HEAD was `3b1aae102fef476657df279bf00e4bc48d223294` during initial source capture and advanced to `7eda047012afb22f8d04d6438b50d9be9ba55d30` while this audit was in progress. The intervening commit changed neither audited source file; both blob IDs and local hashes remained the same. The current probability-scenario document gained a separate high-Chaos/Evolution-IV-absent first-use case; the two test scenarios below were unchanged.

MCP root `sourceHash` was `1c90f792579b83671ee5bc814853bf2bbfee7c055968701f0df86ab501b98242`; candidate provenance `sourceHash` was `c3f3ba0aca7c5fefe0b5be84704ace1c292bb146e32badda896fc2fa35d3feb5`, matching the local effects-file SHA-256. The MCP returned different `sourceRevision` tokens per operation; all are preserved below.

## MCP status and scenario results

Connected server namespace: `hoi4_agent_tools`. No separate server health/version tool was exposed, and its resource listing was empty; the artifact resource template was available. Tool calls were operational for inspect, evaluate, and sweep. The adapter reported `hoi4-1.19.2.v1`, targeting Operation Postern `1.19.2.0 (d245)`; observed game version was `Operation Postern v1.19.2.0.a729 (d245)`, verification status `workspace_verified`. The server-process version was not reported.

Live schemas confirmed these routes: `probability_inspect` accepts adapter/source/candidatePool; `probability_evaluate` accepts adapter/source/candidatePool/scenarioSet/metrics/outputs; `probability_sweep` adds `sweep.paths`, `steps`, `pairwise`, and `findRankReversals`; `probability_render` accepts analysisId/expectedScenarioHash/outputs; `probability_compare` accepts before/after sources and a scenarioSet. The scenarioSet used the connected adapter’s accepted shape: `{id, scenarios:[{id, actor, state, flags, scopes}]}`.

Scenario set ID: `P23_TEST_ACCIDENT_BASELINE_2026_09_26`. Scenario hash: `b7b6388fb60a553ab896bf71e3bf1f1db8e246b3d24a4c72b0bbb5feb7e37ef2`. Candidate-pool hash: `175a0c488ff4f2ea7ba5a7d7b64dbd62468b5399115863d6ee781665c600148c`.

| Exact scenario ID | Inputs supplied | Pool and external-factor completeness | MCP result |
| --- | --- | --- | --- |
| `P23_TEST_PROOF_SECURE` | Actor `SOV`; readiness 75; integrity 85; flags `sov_nuclear_bombs_test_instrumented`, `sov_nuclear_bombs_evacuation_plan_complete`. | Adapter reports all 4 random-list candidates and `poolComplete=true`; all four are implicitly eligible. The effect’s identified local flags and variables were declared, but derived numeric weights did not resolve. Peace, remote-site quality, and low exposure are not weight inputs in this effect. | `supportLevel=unsupported`; all four raw values, ranks, `conditionalProbability`, and `pathProbability` are null. Four `VALUE_UNRESOLVED` items. |
| `P23_TEST_CONCEALED_WEAK_COMMAND` | Actor `SOV`; readiness 50; integrity 35; flag `sov_nuclear_bombs_test_concealed`. | Adapter reports all 4 random-list candidates and `poolComplete=true`; all four are implicitly eligible. The effect’s identified local flags and variables were declared, but derived numeric weights did not resolve. Average-site condition and high foreign-intelligence pressure are not weight inputs in this effect; any separate observation rider is outside this four-entry draw. | `supportLevel=unsupported`; all four raw values, ranks, `conditionalProbability`, and `pathProbability` are null. Four `VALUE_UNRESOLVED` items. |

Inspect status: `ok`, code `PROBABILITY_SOURCE_INSPECTED`; adapter `random_list`; discovered `candidateCount=4`, `poolComplete=true`, `availableCandidates=0` before scenarios, and no unresolved inspect diagnostics. Inspect `sourceRevision`: `4aeab1c2dd327eecb9be0e26ef7b94432bc3bf64ab3244dfbce99ca2b481c526`.

Evaluate status: `ok`, code `PROBABILITY_ANALYZED_PARTIAL`, `analysisStatus=partial`; analysis ID `probability-a007e605ce18a906fa0b4741`; 2 scenarios, 8 candidate-scenario rows, 4 unresolved weight expressions, 0 diagnostics, no blockers. Evaluate `sourceRevision`: `17e962e063e39912c64e4b9cd5a09a7989eec70e99ff8fcc3b2a3571d16bf92c`.

Exact unresolved paths and messages were `var:sov_nuclear_bombs_test_success_weight`, `var:sov_nuclear_bombs_test_partial_weight`, `var:sov_nuclear_bombs_test_failure_weight`, and `var:sov_nuclear_bombs_test_accident_weight`; each returned `VALUE_UNRESOLVED` with “Scenario or source definitions do not resolve numeric expression [path].” No normalized probability mass or usable ranking can be reported. The report’s fallback `topOutcomes` fields are not rankings: every candidate has `rank=null` and `supportLevel=unsupported`.

Sweep status: `ok`, code `PROBABILITY_ANALYZED_PARTIAL`; analysis ID `probability-c242947ffbacffc6dad0697a`; same scenario hash; 4 unresolved expressions. The requested integrity/readiness sweep returned only 2 original scenario points, no breakpoints, elasticities, pairwise interactions, or rank reversals. These empty results do not establish absence of sensitivity or reversals. Sweep `sourceRevision`: `5938ede19c7d587a0ea9e74ee19d9562a289c949c5d2f368268b336328359016`.

## Source trace and findings

Base weights are success 60, partial 20, failure 12, accident 8. Source-order modifiers are: instrumented test adds 15 success and subtracts 5 accident; concealed test adds 6 failure and 5 accident; completed evacuation adds 5 success; integrity below 40 subtracts 10 success and adds 5 each to partial and accident; readiness at least 75 adds 8 success and subtracts 4 partial. Each resulting temporary weight is clamped to a minimum of 1 before the draw.

These are exact source values and condition traces, not evaluated final weights. The secure scenario’s readiness of 75 meets the `>= 75` branch; its integrity 85 does not meet `< 40`. The concealed scenario’s integrity 35 meets `< 40`; readiness 50 does not meet `>= 75`. The adapter could not evaluate the effect-derived temporary expressions, so available weight mass, normalized weights, dominance, and rank reversal remain unresolved. Source code applies a minimum-one clamp to every candidate, but the analyzer did not validate the resulting runtime values; no analyzer-confirmed negative or zero weights are available.

The source assigns `non_detonating` only to the failed-detonation outcome and assigns `detonation_required` to every other result, including accident. This is a source-level consequence-path mismatch with the current user decision; it is not a probability finding. The scenario document expects accidents to rise in the concealed/weak-command case and remain rare in the secure case, but this MCP run proved neither expectation.

No AI score race, repetition sequence, event timing, or target-validity claim is made. Dominance, starvation, rank reversal, repetition, and exploit frequency are unresolved. The source clamp is the only source-level evidence against complete candidate starvation. No evolution timing tuning is proposed.

Recommended parent-owned follow-up: in `sov_nuclear_bombs_prepare_test_outcome` and its action consequence dispatch, make accident consequences default to the no-yield high-explosive/preparation path and permit a true nuclear yield only through the accepted rare catastrophic low-integrity physical severity gate. Keep all four weights and evolution timing unchanged. This recommendation records the explicit user decision and does not choose or tune a weight target.

## Artifacts and route blockers

Inspect JSON (SHA-256 `4f9e2bae75e10606c5b78e091894ace1dea71d6af0600095ec48bcfb20147656`): `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4f9e2bae75e10606c5b78e091894ace1dea71d6af0600095ec48bcfb20147656/552114625c97535d25260f8c97c8c5c5b1a2397b9c260450a4cb7fdaef41a574/probability-inspect-1c90f792579b.json`.

Evaluate JSON (SHA-256 `6c3eab3c532595976265c29081a6f383a1383edcfe65c7b93f1f1bcd68ab2ab1`): `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6c3eab3c532595976265c29081a6f383a1383edcfe65c7b93f1f1bcd68ab2ab1/0321713bc4990a0014bf30d25836ddff4d94f028f4cb54e1bf01110b7482bd01/probability-a007e605ce18a906fa0b4741.json`.

Sweep JSON (SHA-256 `57afaf72b222e281ed717bd2416b25c1d094c13a87244ba47d0c1cdbb4f6707a`): `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/57afaf72b222e281ed717bd2416b25c1d094c13a87244ba47d0c1cdbb4f6707a/c2f18bffa0671b3f11775d4c795160976d480c89186a04e2a075ad811a199393/probability-c242947ffbacffc6dad0697a.json`.

Evaluate visual resources returned with the analysis (URI; SHA-256):

- Ranking: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9aa7ee1779d3d1cc939dbbb38f1c1c1d002efbd39e1561492e5271faa98c4837/8d43029d7146c3a5282c562c3d76586ecc6137ba93f65706a7c4202f49801422/probability-probability-a007e605ce18a906fa0b4741-ranking.svg`; `9aa7ee1779d3d1cc939dbbb38f1c1c1d002efbd39e1561492e5271faa98c4837`.
- Matrix: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/adde5cfb64b32907e9f05337db69fe6b2753faed14b7e1ea0ec60e2ad8705885/49a547f1fe12dc0576222ed5440a4b20156d674c7771b9c4ea060de33b32f1c0/probability-probability-a007e605ce18a906fa0b4741-matrix.svg`; `adde5cfb64b32907e9f05337db69fe6b2753faed14b7e1ea0ec60e2ad8705885`.
- Waterfall: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/294c042c76a605651b040e53b3b46e34bcbcf76a73c016a614f89c6bc5e61a36/beed71d5fc505922485a0e648e3e7920fd2c919a60726cae650c5107171159de/probability-probability-a007e605ce18a906fa0b4741-waterfall.svg`; `294c042c76a605651b040e53b3b46e34bcbcf76a73c016a614f89c6bc5e61a36`.
- Unresolved: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/42ddc597e635f062174c57623bf4fa79f78ac1a36caeb3d6df40aa2f28f64018/41c0eb666ad5d1058266449207f0f7e2030f9820b3f36f08790eef5616606592/probability-probability-a007e605ce18a906fa0b4741-unresolved.svg`; `42ddc597e635f062174c57623bf4fa79f78ac1a36caeb3d6df40aa2f28f64018`.

Sweep visual resources returned with the analysis (URI; SHA-256):

- Sensitivity: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7f5f0919ece296d84a6d541c2b0f4a0724bee8cc274edde1a636093b0ad70321/4cf99e1075b84c0a05f3f60dbb25b1996f9d1e1a8943e4939316ae6679093a76/probability-probability-c242947ffbacffc6dad0697a-sensitivity.svg`; `7f5f0919ece296d84a6d541c2b0f4a0724bee8cc274edde1a636093b0ad70321`.
- Threshold: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a6d32ffc270e06218fbe6e53b5f3d111d3f383d152a2e17fa057722f7cf35cc8/9ee96c7db272b5355dc913a3a003a12bbe68117057d4d652b45e5b4ca722265b/probability-probability-c242947ffbacffc6dad0697a-threshold.svg`; `a6d32ffc270e06218fbe6e53b5f3d111d3f383d152a2e17fa057722f7cf35cc8`.
- Ranking: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8678f25d13b69e2a2160f444a5935697e7c7a7919f92dd97c97773aea6bc9b67/3267ffa85c9b7ef426047fc9eb36e8ddba83e31f824b138308aa5e8cffc72f68/probability-probability-c242947ffbacffc6dad0697a-ranking.svg`; `8678f25d13b69e2a2160f444a5935697e7c7a7919f92dd97c97773aea6bc9b67`.
- Unresolved: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/42ddc597e635f062174c57623bf4fa79f78ac1a36caeb3d6df40aa2f28f64018/76942102fd645f7e6a79e2c77812049143fd48901bce314e2c958b3d33ddb3ba/probability-probability-c242947ffbacffc6dad0697a-unresolved.svg`; `42ddc597e635f062174c57623bf4fa79f78ac1a36caeb3d6df40aa2f28f64018`.

Matching PNG resources were also returned by the analyses. These are analyzer-emitted views; the explicit render route did not succeed.

`probability_render` was attempted for both analysis IDs with the matching scenario hash. Both returned status `error`, code `PROBABILITY_ANALYSIS_NOT_CACHED`, blocker message “Render requires an analysis ID produced by this server process.” No retry was made. `probability_compare` was not called because no post-patch source exists and comparing the current source to itself is invalid; there is no comparison ID. Preserve a byte-exact pre-edit source copy before the parent patch because an analysis artifact is not a replacement source for `probability_compare`.

`probability_simulate` was skipped because the named inputs are deterministic and no uncertain distributions were declared. `probability_sequence` was skipped because this is a single native `random_list` draw, not a declared custom pool with cadence and transitions. The matching event structural inspect/render routes were not run before this handoff was closed; event-chain structure beyond the audited effect remains unverified.

## References reviewed

Read the current repository instructions, `chaos-redux-mtth` and `chaos-redux-subagents` skills, Event 23 Parts 3, 9, and 10, coding prompt, and probability-scenario document. Relevant offline references were the Paradox wiki Data Structures, Effects, Event modding, and AI modding pages, plus vanilla `effects_documentation.md`, `triggers_documentation.md`, `script_concept_documentation.md`, and `common/script_constants/documentation.md`.
