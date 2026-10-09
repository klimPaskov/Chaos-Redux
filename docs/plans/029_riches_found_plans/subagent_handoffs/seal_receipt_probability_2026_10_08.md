# Event 029 paid-seal receipt eligibility probability handoff

Status: exact pre-wiring bytes and the 13 named scenario fixtures are frozen; the post-patch compare returned partial analysis through the mission adapter, so the decision-score comparison remains unresolved under the HOI4 MCP 3.10.0 classifier defect.

This is a read-only probability audit. No gameplay file was edited, no Git or game command was run, no external package was changed, and no child was spawned.

## Scope and frozen before source

The only weighted surfaces are decision_riches_found_gold_seal_depths and decision_riches_found_demons_permanent_seal in common/decisions/029_riches_found_decisions.txt.

The exact current decision source was copied before the receipt-gate wiring patch to docs/plans/029_riches_found_plans/evidence/2026_10_08_seal_receipt_wiring_before/common__decisions__029_riches_found_decisions.txt. The 443,890-byte copy has SHA-256 88B2F6716F401657251BC79C8C144B081953D71725B81F693F630F28AEE36B8D and matches the live file byte-for-byte. It is the comparison baseline for the upcoming receipt-gate patch; it includes the earlier demonic entombment AI guards and is not the older pre-AI snapshot.

The three present but unwired receipt files were also copied and byte-verified:

| Logical source | Bytes | SHA-256 |
| --- | ---: | --- |
| common/scripted_effects/029_riches_found_seal_receipt_effects.txt | 10,160 | 0154EF86F38C47EBF9324252FFC4F662551CE6E819FB934EB40A07CF1649DC81 |
| common/scripted_triggers/029_riches_found_seal_receipt_triggers.txt | 10,260 | 9F8C3F10FD8A7F67652EA5D4D45BBA4CEFC9EB9E38DDB73F49287BFCF5AA5B0E |
| common/script_constants/029_riches_found_seal_receipt_constants.txt | 513 | 9C61E175915F607E991A962226D890EE4CF7A613B91D6E733534F08BE1B5DBC4 |

The frozen scenario input is docs/plans/029_riches_found_plans/evidence/2026_10_08_seal_receipt_wiring_before/seal_receipt_probability_inputs.json, 43,847 bytes, SHA-256 330C9467F3CA6EA83828BC623F2FD6979B77C0B2E2C43B377C253FE847D7F10C. It contains the exact declared two-ID candidate pool and 13 scenarios in scenario set event029_riches_found_seal_safety_20261008.

The fixture was derived from the prior typed fixture by retaining id, actor, date, flags, state, and scopes, preserving scope trees, omitting controls and closedFlags as in the earlier audit, and applying the seven derivations recorded in the copied seal_safety_scenario_fixture_manifest.json. The copied typed source is 968,232 bytes with SHA-256 EA66836933BCF34A929979E43B894ED7F6D61C88D2A545132B13FB1B6C46005E; the copied manifest is 3,422 bytes with SHA-256 CD6159A72BB1388132360B5CC5DB12878D65E207FE718B04139B6AE1ED4A8D14.

The 13 scenario IDs are RF_GOLD_01_STABLE_HIGH_LEGITIMACY, RF_GOLD_02_AUTHORITARIAN_WARTIME, RF_GOLD_03_COLLAPSE_IMMINENT, RF_DEMON_01_STABLE_DEMOCRACY_PEACE, RF_DEMON_02_COLLAPSING_AUTHORITARIAN_WAR, RF_DEMON_03_EVACUATION_COMPLETE, RF_DEMON_04_WORKFORCE_EVACUATED, RF_DEMON_05_DEPOSIT_EXHAUSTED_AFTER_PURGE, RF_DEMON_06_PURGE_NOT_EVACUATED, RF_DEMON_07_UNRESCUED_ECONOMIC, RF_DEMON_08_DEMOCRATIC_ENTOMBMENT, RF_DEMON_09_DEMOCRATIC_EVACUATED, and RF_DEMON_10_SEVERE_COLLAPSE_PURGE_NOT_EVACUATED.

## Live MCP health, schemas, and probability evidence

The live resource hoi4-agent://server/status reports the connected stdio server as version 3.10.0. Current PID 58972 appears as live in the resource’s server list, and the probability inspection call returned terminal status ok. Live tool declarations were available for probability_inspect, probability_evaluate, probability_sweep, probability_compare, and probability_render. The compare schema accepts adapter, before, after, candidatePool, outputs, refresh, and scenarioSet among its fields; the inspect and evaluate schemas accept a source object, and the installed source contract requires source.path.

The required first call was hoi4.probability_inspect with adapter decision_ai_will_do, source path common/decisions/029_riches_found_decisions.txt, the exact two-ID candidatePool, and refresh=true.

Inspection returned code PROBABILITY_SOURCE_DISCOVERED, requestedAdapter decision_ai_will_do, candidates=0, discoveryReason candidate_pool_not_found, and requiredInputPaths empty. Its sourceHash is 17e97cd4f4eeb35a26600f0246dbffbcf6c80a718b3fbf9784fbce38f4a17719 and sourceRevision is fbbc118877a57ef177c451a11bbd2d8690a9f537633dc6c62af422a38074e426. The inspection artifact is hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/29dbcc112121e52bf91b0a0e4741364506f0db9fc84cc7e23e7100acefe6e0fa/7f1081fdb6e49c4345144e4a9a8e1992767fa397650e3f2a59ca1771050132ff/probability-inspect-17e97cd4f4ee.json, artifact SHA-256 29dbcc112121e52bf91b0a0e4741364506f0db9fc84cc7e23e7100acefe6e0fa.

The adapter inventory reports three decision_ai_will_do candidates, zero matches for the declared two-ID pool, and 103 mission_ai_will_do candidates with one match. That mission bucket is not used as a fallback.

One named-scenario evaluation was made with the same two IDs, the frozen 13-scenario set, raw_value, and json/ranking/matrix/unresolved outputs. Although the request named decision_ai_will_do, the result silently selected adapterId mission_ai_will_do and returned PROBABILITY_ANALYZED_PARTIAL. Its scenarioHash is 2cc06fefa863e99e93b3357422d2ded67222435667a1e993072558d8153428e5, sourceRevision is 19e9a418902c5d3c2e703f3db4acfe894babcf5f8a7d8d129617bcdc9a6dc961, sourceHash is the same 17e97cd4f4eeb35a26600f0246dbffbcf6c80a718b3fbf9784fbce38f4a17719, and analysisId is probability-8bf0529659948eb357c541e2. The JSON artifact is hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9aa025d13bb585a1d2160f756fffc371b29711fe5318cd512fc456aec52009c7/72e133f7770060dafba1e471e18308c2ebabc948e75bbac00eedc771502ca87f/probability-8bf0529659948eb357c541e2.json.

The evaluation reports 26 candidates, zero eligible, 26 excluded, 18 unresolved, and three diagnostics. Its “never eligible” diagnostics and all its ranking/matrix resources belong to the misrouted mission analysis and are not accepted as decision evidence. The emitted diagnostic visualization URIs are retained only to preserve the failed route result:

- Ranking SVG: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d2bb31036cb444810f2a9bd992ff5f1ecc50e4985972d984ab914eb0cbf2f674/4531da831b2f20755ba54ccb5dbd55ffa024a780b0aae85e5c960bb077ff6189/probability-probability-8bf0529659948eb357c541e2-ranking.svg.
- Ranking PNG: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0af63c4515553d3ab7790075ce403ec8f225abe17914078f03da7f8a5cc4ef9a/5cf3f217409617c9e3f1342e7b11b81376accf7f8a1248029f95a9788d28b4dd/probability-probability-8bf0529659948eb357c541e2-ranking.png.
- Matrix SVG: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fecd9dc4a8cff516fb948a93d079765707ab2c7bf8e4a429078ddedaead29fad/706092191b56347e0dc262a8563507c417fe2614a484aaaa341d140cefb8ef92/probability-probability-8bf0529659948eb357c541e2-matrix.svg.
- Matrix PNG: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f741f08fdfbbfb1ce54fd96c557793c306c6d02ab18729e64f55389854acb6d3/37fe0d7121f760d27e43addb86bb2763128829476c5ca587fb58cc33aa359b5f/probability-probability-8bf0529659948eb357c541e2-matrix.png.
- Unresolved SVG: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8acac36da150add3e84a116d292fc48e6e911e7cd87fccd68072d76ec24a1bbb/1c0233743d20297dd0a64e916205254f700b8440d8ce280a8894066cbc443f7b/probability-probability-8bf0529659948eb357c541e2-unresolved.svg.
- Unresolved PNG: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1a93697bc2b847953bac6a93d803c01802452ab21ea328d4f6361ceed4a4d3ca/b77fff9bc41fbde30fd31f4b2d6b20d93112d43a0f9d5524fce79f5e9c6e8101/probability-probability-8bf0529659948eb357c541e2-unresolved.png.

No probability_render call was made against this out-of-scope mission analysis. No valid decision score, modifier trace, ranking, selection probability, comparison ID, or comparison scenario hash exists.

The active MCP 3.10.0 classifier defect is documented in the prior seal_safety_probability_2026_10_08.md: source-analysis.js lines 155-158 classifies every entry with days_remove as a mission. Both audited native decisions have days_remove, so the decision adapter omits them. The evaluation’s automatic mission_ai_will_do selection is consistent with that defect. Do not patch or route around the external package.

## Source values, gates, and result classification

The current source weights are unchanged by the planned receipt wiring and are source values only:

- Gold seal base is constant:riches_found_decision_ai.medium=3. Its modifiers are 2.5 for public policy, 2 for the Gold next-step pressure value, and 4 for deep-mine status.
- Demons permanent seal base is constant:riches_found_decision_ai.medium=3. Its modifiers are 2.5 for public policy, 4 for democratic government, 2 for supernatural crisis, 0.50 when riches_found_seal_would_entomb_workforce is true, and 0 for democratic government with that helper true.

The source constants are in common/script_constants/029_riches_found_constants.txt. These are raw source coefficients, not evaluated base or final AI scores. Native decision ai_will_do is willingness scoring and does not produce a click probability.

Before wiring, the Gold decision’s available and custom_cost_trigger blocks use the existing gold affordability gate; the Demons decision uses its existing demonic affordability and route gates. Neither target decision calls rf_gold_seal_can_start_manual or rf_demons_seal_can_start_manual yet. The new trigger wrappers are at lines 196-203 of common/scripted_triggers/029_riches_found_seal_receipt_triggers.txt.

The new manual-start helper checks the coherent family quote, absence of a receipt, current route/controller/registration, valid non-exhausted state counters, pending-count capacity, manpower, and support equipment. It deliberately excludes native civilian-factory reservation, which remains handled by the existing two-factory decision gates; native reservation ordering and rejected-entry behavior remain unproven. The existing helpers also encode saved-quote refund and state-controller epoch handling, but these are not yet called by the two target decisions or the control-change hook.

Conclusion classifications:

- Current AI formula and constants: score-only source evidence.
- MCP candidate inventory counts and artifact metadata: exact reported tool output, with adapter semantics defective for these two decisions.
- Receipt helper behavior: bounded source evidence only; the parent’s prior 23 source cases were not rerun here and do not prove native reservation or callback ordering.
- Scores, eligible rankings, selection probabilities, dominance, starvation, rank reversals, repetition rates, and exploit probabilities: unresolved.

Candidate-pool and scenario completeness are not sufficient for a numeric decision comparison. The requested pool is exactly the two scoped IDs, but MCP candidate coverage is 0/2. The fixture is synthetic and its gate inputs are partial: the Gold base scenarios omit explicit Gold layer/route predicates; RF_DEMON_02 lacks the cleared-district flag; RF_DEMON_03 is already sealed; all six original scenarios omit num_of_available_civilian_factories; only RF_DEMON_07 supplies that field, as a cost-ineligible case. The previous audit also omitted controls and closedFlags. No saved scenario represents the new pending receipt, a clean no-pending contrast, or an epoch mismatch. Those three derived source cases were not added or evaluated because the live probability route did not expose either target as a decision candidate and did not establish how it represents the receipt helper’s dynamic owner variables. No invented receipt flags or variable keys were submitted.

## AI validity and risk findings

No measured dominance, starvation, rank reversal, repetition, or snowball outcome is claimed. The current source has a positive base score for both decisions; separate availability and custom-cost gates decide eligibility. The planned receipt gate therefore changes eligibility, not the declared AI coefficients. The source-level demonic entombment modifiers reduce or zero willingness under the named harm condition, but their evaluated effect remains unresolved.

The identified integration risk is a missing receipt eligibility check before parent wiring: current decision availability does not yet call the new manual-start helper. Parent integration should preserve the two-factory gate, revalidate and store the quote before debit, resolve/refund using the stored quote at the native removal boundary, refund on native cancellation, allocate the caller temporaries, and bump the controller epoch before existing reconciliation. These are recommendations from the supplied integration plan; this audit applied none of them.

## Compare plan, skips, and remaining uncertainty

After parent notification that the source patch is complete, run one hoi4.probability_compare with the same 13-scenario fixture, the exact two candidate IDs, before.path and after.path set to the logical decision source, before.snapshotPath set to the frozen decision copy, and before.expectedSourceHash set to lowercase 88b2f6716f401657251bc79c8c144b081953d71725b81f693f630f28aee36b8d. Do not use mission_ai_will_do if the classifier repeats. Allow one narrow retry only if the comparison load times out. A returned empty or misrouted result remains unresolved and is not a passing comparison.

Skipped analyses:

- No probability_sweep was run because the correct decision adapter exposed no target candidates or supported sensitivity path.
- No probability_simulate was run because no uncertain inputs were declared.
- No probability_sequence was run because this is not a complete declared custom pool with cadence and state transitions.
- No valid probability_render was run because there was no in-scope analysis artifact; the evaluator’s auto-emitted mission views are preserved as invalid-route diagnostics.
- No source-derived pending/noPending/epochMismatch scenarios were submitted because the evaluator did not prove target or dynamic receipt-state coverage.
- No comparison was run before the parent patch, per the requested ordering.

The native civilian-factory reservation order, callback identity/exclusivity, saved-game state, and actual game selection behavior remain outside this MCP evidence. Do not claim a baseline pass or any balance conclusion until the after-source comparison returns a terminal, correctly routed decision result.

## Post-patch comparison result (2026-10-08)

The parent-reported post-patch decision source hash was independently verified at the logical path: common/decisions/029_riches_found_decisions.txt is 453,086 bytes with SHA-256 6CC508136D8E3B94443204603F16506EC4CB10760E1DEAEB665B57DD69DF4107. The before snapshot remains 443,890 bytes with SHA-256 88B2F6716F401657251BC79C8C144B081953D71725B81F693F630F28AEE36B8D.

Both audited ai_will_do blocks were extracted from before and after source and compared line-for-line. The blocks are identical: decision_riches_found_gold_seal_depths has normalized extracted-block SHA-256 1DCE6A0F644ED907A13DD25687599CDBFBA073F40146E9B44CC0E70AFB6ED17A, and decision_riches_found_demons_permanent_seal has normalized extracted-block SHA-256 2A065167BB73A834BA09A8FE4F0815E69B2BA354BCBA80A4BED801543DE52BF5. This is source-text evidence that the AI willingness definitions did not change; it is not an MCP score comparison.

One hoi4.probability_compare call used adapter decision_ai_will_do, the exact two-ID candidate pool, the same saved 13 scenarios, before.path and after.path set to the logical decision path, before.snapshotPath set to the frozen 88B2… copy, and lowercase before.expectedSourceHash 88b2f6716f401657251bc79c8c144b081953d71725b81f693f630f28aee36b8d. The call returned terminal status ok in 35.7 seconds, but code PROBABILITY_ANALYZED_PARTIAL and adapterId mission_ai_will_do. It reported 26 candidates, 0 eligible, 26 excluded, 104 unresolved, comparisonChanges=26, 13 scenarios, and scenarioHash 2cc06fefa863e99e93b3357422d2ded67222435667a1e993072558d8153428e5. The sourceHash is 037b33dcadd453270347e1f82f9c9c602ccf1a6d5745772e7c46f984a87b50fe and sourceRevision is db62c145159d727d7b476fde28a00ac227c5be1cce1c1effaf1aef6c4c47679f.

The result did not include a comparisonId. Its scenarioHash and comparisonChanges are retained as misrouted tool output, not accepted decision evidence. No numeric score delta, decision ranking, candidate eligibility result, selection probability, or comparison pass is claimed. Because the call returned rather than timing out, the timeout-only narrow retry was not used.

The five returned artifacts are all attached to the wrong mission-adapter analysis and are retained only to document the route failure:

- JSON: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/35117d207d880100e3aec2bb4a97936fe81fa8d50eba5c3cf5e19d706f9f1b92/4f84d6180c1a332b6be67dacd3bb5a8da4e8916a1111f90f7d36d7460d485146/probability-0993efc250018770818191ed.json.
- Comparison SVG: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/79f1b3eb81968c403c9107fd9423b8d6e98748dca620916c4e0f860fd5a15289/0e1a8201cca51d14cf93d8bf3de9d3f591c34b966b5b5819ed6df67bf412d2de/probability-probability-0993efc250018770818191ed-comparison.svg.
- Comparison PNG: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/560f1f50c9a4c9f8d479e5592025a22580e7344430b4fb19664f7b77d946d094/5e4ee6d4ea8721fcaae4956797cda909ad6b58782c1969f77d5f71ad5de76460/probability-probability-0993efc250018770818191ed-comparison.png.
- Unresolved SVG: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/da1e0f6f96faea4786d4c53fcb77746f35010bb6b21b7606f03bb94d1da41ee9/a52624d73b4f745be3c6c033ae03c5cc54cc0e290d5a80d215c3165fb092ff50/probability-probability-0993efc250018770818191ed-unresolved.svg.
- Unresolved PNG: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4ae0dbc2ac1197c68ca3e6b53f36346de6967a5877bb14053384e3fe4ba6ebd2/c7df3836b71b14ac0dd3362df184842a00b822f55996b995777ff2770f99aa15/probability-probability-0993efc250018770818191ed-unresolved.png.

No explicit probability_render call was made against the mission analysis. The compare response already emitted comparison and unresolved views, but they are not valid evidence for the scoped decision surface.

The final decision AI validity, dominance, starvation, rank-reversal, repetition, and exploit findings remain unresolved by MCP. The source-text equality confirms unchanged willingness blocks only; it does not prove the new manual gates are engine-valid, that either target is eligible in the supplied scenarios, or that AI will select them.

