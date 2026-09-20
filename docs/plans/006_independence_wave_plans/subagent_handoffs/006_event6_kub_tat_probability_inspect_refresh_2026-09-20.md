# Event 006 KUB/TAT probability inspection refresh (2026-09-20)

## Disposition

`UNRESOLVED / read-only MCP evidence refresh`.

This refresh covers only the admitted IW-040 KUB and IW-044 TAT mission AI surfaces and does not change source weights, triggers, decisions, missions, package admission, or Join.

## Current source inspection

The KUB source is `common/decisions/006_independence_wave_frontier_decisions.txt`. An unfiltered `hoi4.probability_inspect` retry completed with source revision `4f556e318df91385dd9a438d09ce37335aef0c60daaca785a8d0f989753d0d41`, source hash `6ae0124991b3742ae8b7a856c8207ea9d755335dac9a79cbe848ac8fc88785c1`, `poolComplete = false`, 23 aggregate source candidates, 19 required inputs, zero unresolved inspect inputs, and zero available candidates; its artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/01b08a8e41ed061b7e466d07857372f63b17b1c8085ba5f0e6844bc552586b0c/44e7d1e4dea26a96ad59c4abaae9baca4d1d973811c710348df086fc7313c8e4/probability-inspect-6ae0124991b3.json`.

The exact KUB package pool was then inspected with its 11 named candidates and completed with `poolComplete = true`, 11 candidates, 17 required inputs, zero unresolved inspect inputs, and zero available candidates. Its filtered artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/50e4e627c6d50b8a24653cb1992bc26c3169f26107c784b4267b57e68eb3616c/c8c77dc5341a70d9b0eb81bdd8e4125302c9a76a48c7aedd5780ce0c76a0e3ef/probability-inspect-6ae0124991b3.json`.

The TAT source is `common/decisions/006_independence_wave_siberian_decisions.txt`. An unfiltered `hoi4.probability_inspect` completed with source revision `a75a1042cb2587a57381c591a24de74797668eb32e36045aa1f800c03d170553`, source hash `10a83c3b7f4c6700eebce87393a8ee357f96ece5ca06966eb944f84b44749200`, `poolComplete = false`, 88 aggregate source candidates, 19 required inputs, zero unresolved inspect inputs, and zero available candidates; its artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a8623872a69c51966c9921a70dc4321f57f660e13e21f69b372665eaabba4950/62816c7053f586371fd706ce5a8a957bda90efabdebc3fd112c7e9bf2f322d57/probability-inspect-10a83c3b7f4c.json`.

The exact TAT package pool was then inspected with its 11 named candidates and completed with `poolComplete = true`, 11 candidates, 18 required inputs, zero unresolved inspect inputs, and zero available candidates. Its filtered artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ec1b1e377d08ea0e5c748136c084b2b7ebfd9c6e7324dfb7c910b4f7c2c347a3/7ced2351350ec37c736cd6d951ca9403362db3a6a0ee8066ced36d1205abf6f4/probability-inspect-10a83c3b7f4c.json`.

The unfiltered 23/88 counts are aggregate candidates across merged source files, not the package-specific pools. The current exact KUB and TAT package pools remain complete at 11/11; neither count represents package admission or probability outcomes.

## Bounded empty-state evaluation

The exact historical 11-row TAT candidate pool was evaluated under `E006_TAT_EMPTY_SOURCE_RELATIVE_REFRESH_2026_09_20` with one empty-state scenario and no invented package values. The result was `PROBABILITY_ANALYZED_PARTIAL` with analysis id `probability-bc5bbff0deae5ef6838f6691`, one scenario, 11 candidates, 308 unresolved items, and 11 diagnostics; the JSON artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/92e4f09d2663e612e0d7754363b027b0d7a07acb9b894bb2ae76630488533669/bf16dcf0f672e7d8d3a7c40472a805ec4191c5f539c624fc1175e656e7b0754e/probability-bc5bbff0deae5ef6838f6691.json`.

The matching KUB evaluation used its exact 11-row candidate pool under `E006_KUB_EMPTY_FILTERED_RETRY_2026_09_20` with one empty-state scenario. It returned `PROBABILITY_ANALYZED_PARTIAL` with analysis id `probability-f61dc2f0f7abcf8bd906272b`, one scenario, 11 candidates, 307 unresolved items, and 11 diagnostics; the JSON artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/44728a494f244926551a3e19b0fd4ae6bb236b367046491f7e1becabb8d73c54/da2c6f113db68fc93acc1eaf17597741bea51422863d7cf90c2c475068d4b1ba/probability-f61dc2f0f7abcf8bd906272b.json`.

## Evidence boundary

The ten accepted KUB/TAT scenarios remain unexecuted as typed package-state fixtures. The existing blocker receipt `subagent_handoffs/006_event6_kub_tat_probability_retry_2026-09-20.md` remains authoritative for the rejected unsupported state fields and the missing actor, event-target, variable, ledger, route, resource, and former-host state contract.

No `probability_compare`, complete sweep, simulation, sequence, normalized probability, dominance, starvation, rank-reversal, or numeric balance conclusion is valid from this refresh. No AI, decision, mission, focus, strategy-factor, admission, or Join source was edited.

The Event 006 boundary remains 32 content-attested packages, 29 compatible reservation groups, 40 runtime adapters, 161 unattested selectable rows, and the exact `3/4/5/7/10` automatic ladder with World Collapse at `10`.
