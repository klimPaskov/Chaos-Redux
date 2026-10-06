# Event 001 Final Fresh Probability Audit, 2026-10-06

Disposition: bounded Event 001 probability checks completed; the spread, rare-variant, and option-pool results are scenario-specific, while the uninspected pools and world-wide Event 091 share remain unresolved.

This is a read-only audit handoff for parent review.

No gameplay source, balance target, asset, index, spreadsheet, CSV, runtime, desktop, or game file was edited.

## Sources and MCP version

The current event source is events/001_communism_spread.txt, raw SHA-256 37B7B2E533842DB23F150A3378DA7015672540D59B381F14A21BAEA1AC45FD99.

The frozen event source is docs/plans/001_communism_spread_plans/probability_before_20261005/001_communism_spread.txt, raw SHA-256 12359309CC86ACD67477A91D737C9A7CE6B15820D8021A059C8DCEDACBB8FB46.

The current effects source is common/scripted_effects/001_communism_spread_effects.txt, raw SHA-256 D9536AF3327785BE46836448C62E341016A1E537B06C335B26FE1044B8A20D1B.

The frozen effects source is docs/plans/001_communism_spread_plans/probability_before_20261005/001_communism_spread_effects.txt, raw SHA-256 1D5E107D0A62416D6748B39152188E148B45196F7E54E609D4C13D171B20509B.

The current trigger source is common/scripted_triggers/001_communism_spread_triggers.txt, raw SHA-256 08B23B4621736380D468D4856C42860DEA1DD5047DA1143F288A60D1AE7EA81F.

The current tuning source is common/script_constants/001_communism_spread_constants.txt, raw SHA-256 8E011B438B57EF5CB6EA46B96BAA805D9A2CC515463255143BF9D9C27DC0C46E.

The focused Event 001 option inspection and all successful probability artifacts report source hash 15110c8758dc313916732e8b6597f7bf48460cceaaeb840aef076b124c7cc984 for the current event file, source hash b29e05701ccdd70a90710d6af919c28f6590e9e4fb8dbb3f3aa5eac7096d5bb6 for the current effects file, and adapter version hoi4-1.19.2.v1 for Operation Postern 1.19.2.0 (d245).

The live tool inventory exposed probability inspect, evaluate, sweep, compare, simulate, sequence, and render schemas, but no separate MCP server version or health tool.

The retained Event 001 offline wiki, installed documentation, and structural event-inspect/render evidence are cited in probability_release_20261005.md and integration_release_20261005.md; those structural routes were not repeated in this probability-only turn.

## Weighted surfaces and results

| Surface | Candidate pool and external inputs | Result classification |
| --- | --- | --- |
| chaosx.nr1.2.a and chaosx.nr1.2.b event options | The focused inspector found the complete two-option pool and required command_power; the compare scenarios declared command_power 9/10/11, global.black_friday_price_cp_10 = 10, has_war false/true/true, and has_stability 0.6/0.6/0.2. | Exact conditional event-option shares, conditional on the event being presented. |
| Spread roll at effects line 1414 | The complete two-entry pool takes the supplied raw weights 18/82 and 95/5; upstream campaign chance construction is outside this local pool. | Exact conditional local random-list shares; bounded with respect to the preceding campaign formula and invocation cadence. |
| Sabotage/no-sabotage roll at effects line 1699 | The complete two-entry pool was found, but the calculated sabotage chance and its complement were not declared for the named scenarios. | Pool inspection exact; evaluation unresolved because external weight inputs are incomplete. |
| Industry/strike incident type at effects line 1713 | The focused inspection timed out before returning pool completeness; report receipt flags affect the type weights. | Unresolved. |
| Surprise variants at effects line 2826 | Complete three-entry pool with the named none/some/all receipt states and raw weights 40/30/30, then 0/30/30, then 0/0/0. | Exact conditional local shares for none and some; all-zero case has no normalized selection probability and is expected to be skipped by the caller gate. |
| Ritual variants at effects line 2853 | Complete four-entry pool with raw weights 30/25/25/20, then 0/25/25/20, then 0/0/0/0. | Exact conditional local shares for none and some; all-zero case has no normalized selection probability and is expected to be skipped by the caller gate. |
| Whisper variants at effects line 2872 | Focused inspection timed out; four receipt-sensitive entries are present in source. | Unresolved. |
| Evolution-family selector in try_communism_evolution_incident | Complete four-entry pool; its surprise, ritual, whisper, and no-incident weights depend on family unlocks, remaining variants, and a computed complement not declared as a complete scenario. | Pool inspection exact; no family share or timing result. |
| Neighbor/remote spread route at effects line 1463 | Focused inspection timed out; eligible state targets and route weights are not fully declared. | Unresolved. |
| Event 091 weight nudge and global event selection | The helper adds a source-defined increment to Event 091, but the full global.all_events candidate set, host state, filter results, cadence, caps, and terminal transitions are not supplied. | Global Event 091 share and sequence remain unresolved; no local-pool result is presented as a global share. |

For evt001_industry_report_cp_below, the analyzer marks chaosx.nr1.2.b ineligible, leaving chaosx.nr1.2.a at conditional probability 1.0.

For evt001_industry_report_cp_exact, both options are eligible; chaosx.nr1.2.a has raw score 65 and conditional share 0.5416667, while chaosx.nr1.2.b has raw score 55 and share 0.4583333.

For evt001_industry_report_cp_above, both options are eligible; chaosx.nr1.2.a has raw score 65 and conditional share 0.7027027, while chaosx.nr1.2.b has raw score 27.5 and share 0.2972973.

The final Event 001 compare is exact for its complete local pool and declared scenario inputs, with scenario hash c17c2b38fe8a3f70fe47fc25f822dfb4a34fcfc24e3c78e6fd55d00b9fe6eac2 and analysis id probability-55c07539fd10f9c9e5000dbd.

The compare maps chaosx.nr1.2.b from eligible before the gate to ineligible only in the CP9 scenario; the inclusive CP10 boundary keeps it eligible at the exact quote.

The CP9 result triggers PROBABILITY_DOMINANT_OUTCOME because the remaining option has the entire conditional share; no rank reversal occurs in the three declared option scenarios.

For evt001_spread_small_stable, entry 1 spread has raw weight 18 and share 0.18, while entry 2 no-spread has raw weight 82 and share 0.82.

For evt001_spread_large_wartime_nonai_pressure, entry 1 spread has raw weight 95 and share 0.95, while entry 2 no-spread has raw weight 5 and share 0.05.

The spread ranking reverses between the two named scenarios, and the 95 percent stress outcome triggers PROBABILITY_DOMINANT_OUTCOME.

The spread evaluate has scenario hash 69b530c2a92816efc3d9dba5cab7c882118a457885b7bb3e8988e3d9ebeb4c40 and analysis id probability-80e1aa42cd134ac40d5123e6.

The matched frozen/current spread compare used the actual source lines 1385 before and 1414 after, with scenario hash 69b530c2a92816efc3d9dba5cab7c882118a457885b7bb3e8988e3d9ebeb4c40 and analysis id probability-bca0f531c661aa1b7e28aad9.

That compare reports the before line-based entry ids as removed and the current line-based ids as added, with zero unresolved deltas; it does not emit a numeric old-versus-new probability delta, so no such delta is claimed.

For evt001_surprise_none, the three variant shares are 0.40, 0.30, and 0.30 in source order.

For evt001_surprise_some, after the .14 variant receipt, the remaining two variants each receive 0.50 and the reported variant has probability 0.

For evt001_surprise_all, all supplied weights are zero; the analyzer returns null conditional probabilities and warns that adapter fallback behavior controls the forced all-zero case.

For evt001_ritual_none, the four variant shares are 0.30, 0.25, 0.25, and 0.20 in source order.

For evt001_ritual_some, after the .15 variant receipt, the remaining shares are 0.3571429, 0.3571429, and 0.2857143; the reported variant has probability 0.

For evt001_ritual_all, all supplied weights are zero; the analyzer returns null conditional probabilities and warns that adapter fallback behavior controls the forced all-zero case.

The surprise and ritual variant evaluations do not model the parent family gate or live callback order, so the all-zero cases are not interpreted as selectable in normal event execution.

Source review shows each selected surprise or ritual variant sets its matching communist_reported_nr1 receipt before queuing the report event; this supports the once-per-crisis design at source level, while the probability adapter does not prove native callback delivery or runtime repetition.

The zero weight for a reported variant is intentional starvation of that consumed variant; the remaining unseen variants retain nonzero local shares until the family is exhausted.

## Artifact evidence

| Evidence | Artifact URI |
| --- | --- |
| Whole-file random-list discovery | hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d3759e409d1ef576a8d85c3da39b77d41b8201b2cd8cfbbba99a6ea0b91fccb5/b9a05a4775bf23c68b0d85dc2b51c633194183367013363e69946c7366cff021/probability-inspect-b29e05701ccd.json |
| Focused CP option pool | hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8586fa8954af19c2a08e56bc5212e4474125d912a457950f1a75ccd28986d790/31a6897e72ef48ca64b43961fe1ab442600fbc98fd94046c6d3a67a1a07563d2/probability-inspect-15110c8758dc.json |
| Focused spread pool | hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/12fa31ed47ce2a8bf247cc82be60e3108023d4dbc489cd5ba4f333742c1dca82/e70e31824e3a630415ff2049f34d5b6984dc66e085a7bdd1d7836c77cce9c279/probability-inspect-b29e05701ccd.json |
| Focused escalation pool | hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/53bede50fa84712c4e205469eca52cd35d47782a56f9c6176dc06b592fb54d62/dbbd266ea0c69498aeb9c6fbbd2a04d7ffa5acf52c5875ce121f7c8c2ad1bfb9/probability-inspect-b29e05701ccd.json |
| Focused sabotage chance pool | hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c22505b21efd3004e192ddbbfec2e24e997620ab0dfba45fb27efbbab9ae4cf2/3eb5f6e3a566ff975175cc44eccfa23295062df7df32fa8ba47ef902b382b13a/probability-inspect-b29e05701ccd.json |
| Focused surprise variant pool | hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f5c500db14ffcc50226161eaacf2b9c1c03dc55bedbe4fae95a0b6db5435e446/62d4e13ad7c730d4bbb0539b8c8375051aedec38311b48c716ccb0e0f71e699f/probability-inspect-b29e05701ccd.json |
| Focused ritual variant pool | hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3b02c49c07254288bf2c6994abe6a29a12cd5c134ec35ff80ea40a3ebaa65810/4ebbd03355dbbcd928cbff7d944adbb1111e52b6f2570e251bb60ca44589d941/probability-inspect-b29e05701ccd.json |
| Focused evolution-family pool | hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cb6503262940b45a0c24d7b6956e6f401abb252de9403fcf7672c3823136aec1/787c00de5ccf46102cc82810deee574422d8f39ead5e8a677eb2c8bf0a520990/probability-inspect-b29e05701ccd.json |
| Final CP compare JSON | hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/49a5cbacdc9ea6f4eacf527fe136fb1f7e109b003203a2d4571590ddecc99005/75851a578d974ea07e2bf2fe0e0152348a697a627adcf5376919a2f37fa1e647/probability-55c07539fd10f9c9e5000dbd.json |
| Final CP comparison PNG | hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b8de1ff1422ae2e0e4b20bdade1a7898d5061cb4ed28abdbefcabcc230c9fbe8/7ec6152be3c1a2119744e2ab3bfc7e6c8f484577cc78379d375abd967695e3dd/probability-probability-55c07539fd10f9c9e5000dbd-comparison.png |
| CP unresolved PNG | hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/741e9e9423642ce8eb7607dbaccbbceeec8fa1c4ab1c760262892070e72be88c/1d7fd9664cf88405d69fb5000d17cd5c2da39366698684c8b917f037bddd2757/probability-probability-55c07539fd10f9c9e5000dbd-unresolved.png |
| Spread evaluate JSON | hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4c2ba5288e955b144eef174f7bc1dbc59462eb0d2359eccb0a5ad1ded3633a07/87b40a6eaaeaf3dee9c55a8507e76d0ea095bfd0f5e01ce71b1d4f1228cb5cf9/probability-80e1aa42cd134ac40d5123e6.json |
| Spread compare JSON | hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bca839518db65d6ada4058a510e5917026f4a9ab68d4aadd74953ddd0de68620/2d216e33642240f6ca5f12c7e9df831ca3f6f1cebc815b8cd50c03431ca5c58f/probability-bca0f531c661aa1b7e28aad9.json |
| Spread comparison PNG | hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5f5a7f532ba71c86175f1708162f7937e0e016d24b22e61f91df4aa735ebbf73/1d59cd638f5f918d6008d678513a41c2b1c30363fbe0b43eb25a0d64d6112856/probability-probability-bca0f531c661aa1b7e28aad9-comparison.png |
| Surprise evaluate JSON | hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cda027e0689003fbb277edbb8d959a88b73b48f6ab331f54a3f61555f2e6ee68/b7120df20f362854b4e4ab055f9048280515d09bf040515c7bf25c96d25fc2be/probability-afbfe1631c5c579a97afe999.json |
| Surprise matrix PNG | hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5fc414ba1e8c0a182dc9e0344568ecc081f4b7c1c742f334cf7615a7a786574f/71582a682eab97455b40981ff8041617ec2cbc00d4caa70653459f53b931b90c/probability-probability-afbfe1631c5c579a97afe999-matrix.png |
| Ritual evaluate JSON | hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/701be0913adddb9209862e7289094d0b21d85357d8e99c85240a950bdf82e593/d72db49faa4ed2382ce5f7da6939aa8d660366064596eacd5c8efa3edcdff779/probability-8187ac31af1b7baeb981f104.json |
| Ritual matrix PNG | hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e7057c249e680900175083ce6a9c193db4c48abbfaf3efcb1f4891e55fba2350/739cb1c678b6a294debc23c67b4ae276d2d8d5e7818fba615195e5c84dcd9bc4/probability-probability-8187ac31af1b7baeb981f104-matrix.png |

The JSON artifacts for the spread, surprise, ritual, Event 001 CP compare, and Event 001 spread compare were retrieved through byte-range resources and checksum-verified against their artifact URIs.

## Incomplete analyses and source limits

The 1463 neighbor/remote spread pool, 1713 industry/strike report-type pool, and 2872 whisper-variant pool each returned the exact blocker tool call error: tool call failed for hoi4_agent_tools/hoi4.probability_inspect; caused by timed out awaiting tools/call after 600s.

No further inspect or evaluate retry was made for those three timed-out pools.

The spread route, sabotage type, and whisper variant conclusions remain unresolved.

The sabotage/no-sabotage local pool and evolution-family selector were inspected completely, but their scenario inputs do not supply every computed chance, unlock, receipt, or complement required for evaluation.

The full global Event 091 pool, its candidate filters, and its cadence/cap/removal/reset transitions were not declared, so neither a global Event 091 share nor sequence result is claimed.

No probability simulation was run because no uncertain input distribution was declared.

No probability sequence was run because the custom Event 091 pool manifest and state transitions are incomplete.

No MTTH-backed surface was found in the named Event 001 sources.

The five Event 001 decision AI scores, PP hints, and emergency-cost selectors were not part of this parent-bounded final recheck; their previous unresolved score audit remains in probability_release_20261005.md.

No separate sweep was run because this parent task bounded the fresh recheck to the named evaluate/compare scenarios, and the CP9/10/11 compare resolved the declared boundary cases directly.

Fresh probability_render calls returned PROBABILITY_ANALYSIS_STALE because the workspace revision changed after the analyses; the evaluate and compare calls themselves produced the ranking, matrix, comparison, waterfall, and unresolved artifacts linked above.

The current Event 001 structural chain remains covered only by the previous partial event-inspect/render evidence cited in the earlier handoffs, not by a fresh structural pass in this turn.

## Recommendations

Keep the inclusive CP10 gate in events/001_communism_spread.txt for chaosx.nr1.2.b; the exact boundary comparison shows it is false at CP9 and true at CP10 and CP11 against a declared quote of 10.

No ai_chance weight target is recommended from these results; the final conditional option shares are already complete for the declared pool and named contexts.

Keep the per-variant receipt weighting and the has_unreported_communist_surprise_revolt_variant, has_unreported_communist_worker_ritual_variant, and has_unreported_communist_world_revolution_whisper_variant caller gates aligned so exhausted all-zero subpools are not selected.

Review the 95/5 spread stress case only if the owner intends a different conditional dominance target; no patch was applied.

Do not claim or tune an Event 091 global selection share from the local +200 helper; provide a complete eligible global.all_events manifest and declared state transitions before such an analysis.

## Skills and work boundary

Read and applied .agents/skills/chaos-redux-subagents/SKILL.md, .agents/skills/chaos-redux-events/SKILL.md, .agents/skills/chaos-redux-decisions-missions/SKILL.md, and .agents/skills/chaos-redux-mtth/SKILL.md as relevant.

No skills were changed, no tests or game launch were performed, and no commit was created.
