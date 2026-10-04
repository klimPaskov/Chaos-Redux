# German exact-transfer availability probability comparison

Disposition: matched read-only MCP comparison completed; decision eligibility and click probability remain unresolved in the adapter.

The audited candidate is `germany_transfer_prisoners_to_experiment_site` in `common/decisions/genocide_crisis_decisions.txt`, with the same 29-ID same-file decision pool and six scenario IDs from [the earlier baseline](transfer_decision_baseline_2026-09-26.md).
The six-scenario hash stayed `41e48088659f4bbaf7fbd84b1974491d9d9004e028b1fe399fa081df13516c94`.
The frozen before decision and trigger raw SHA-256 values are `e06525307514bb1f66b923f824a3d9ac00937202dc0194fc7ce53fab7633c0f2` and `bb0238c5a601c90f2093253cccd9b1b0143c65e091e082913fafe5971eb2724c`.
The after values are `610117369787dad95b345632a7120a67823b35cfd9384f28fb87663db133fef2` and `a22382d8b2db75d365318d0882fae9e4e2b0917252ce51f71de8ff38514bc5bd`.
The after inspect found the complete declared pool at MCP source revision `1190490b115bfcb4e1982cd61a9e7ac8761dd059e7c2d1fe0a36aba772d36feb`, source hash `d53c4b53216e8782160a888b9b8a3d8a0743b6285d56939be1600a6aacce10b9`, and [inspect artifact](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/95201edae699f3c6aaa6ed6ab07100f53801b0908cccb2ab3adc7394e32cf8e7/d306cd400462a40f162cd1379036bc3e5bd40554edfd1575cf52ec60c2fd2bbc/probability-inspect-d53c4b53216e.json).

The required `probability_inspect` preceded six-scenario evaluation on the frozen source.
That evaluation returned `PROBABILITY_ANALYZED_PARTIAL`, 174 candidate-scenario rows, 545 unresolved items and 68 unresolved candidates; its analysis ID is `probability-3360d0fb0bb4ce999df13252` and its [JSON artifact](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a9e52a8bc0d004ded9f6928c26f789e92e076e96b1bc09b73f8354bf5860d986/f9af18b02f09352d1b719fefc399529d49220d390b176d8301bd5f29ecdb107c/probability-3360d0fb0bb4ce999df13252.json) has rendered ranking, matrix, waterfall and unresolved companions.
The adapter's `NEVER_ELIGIBLE` warning for that frozen candidate is not live-game proof because its flat fixtures lack typed source-row, state-88 capacity and payment bindings.

The post-edit [matched compare JSON](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c5c9cd4c65fb66bf854eac8f7058cb97f1f19ad3f4db915a76e641076ce89eb2/696e69eb700cdf3fd662e98b2dd143f6dcf619282be52c67f73882a79ae7e9b8/probability-afd83a35548da9ff9d442e28.json) used exact frozen and after bodies embedded with `inlineClausewitz`, the unchanged 55-point AI constant, the same 29 candidates and the identical scenario set.
It returned `PROBABILITY_ANALYZED_PARTIAL`, analysis `probability-afd83a35548da9ff9d442e28`, 174 rows, 11 comparison changes and 658 unresolved items/69 unresolved candidates; its [comparison](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/03a63331ee612d854bc16120f48fb9b17c54785949de64f5f8e09f62590e6f18/eacf765ad89ebb1e0232bde6617175209ac9784a86b39f1017005923663a5f68/probability-probability-afd83a35548da9ff9d442e28-comparison.svg) and [unresolved](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/185da5005cb4f0151d8616bd4a6357c45291ee20f066b6549629bffec49b9f8d/d86f030b91e4974593ddd628cb2349a219a91b67ab1aad4bc516271c2418e15f/probability-probability-afd83a35548da9ff9d442e28-unresolved.svg) views were rendered.
The candidate's actual source willingness remains 55 on both sides.
Its `GER_post_administration_invalid` row changed from false to unresolved eligibility and reports `rawDelta=55` solely because a candidate became score-visible to the adapter; that is not an AI weight increase.
The other five candidate rows report raw delta zero, while five noncandidate rank deltas with raw delta zero were attributed to source or scenario metadata and are not established gameplay rank reversals.
The adapter reports `selectionRule=score_only` and `normalizedProbability=false`; it cannot establish current native eligibility, a full game-wide competing pool or click probability.
No sensitivity sweep was run because this patch changed an availability gate, not an AI weight or declared numeric sweep target.
