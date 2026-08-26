# Event 014 probability refresh

Audit date: 2026-08-26.

Scope: current Event 014 opening-policy AI chance pool only. No gameplay, weight, model, GUI, or 3D source was changed.

## Current MCP inspection

`hoi4.probability_inspect` used adapter `event_option_ai_chance`, source `{path: "events/014_cannibalism.txt"}`, and the complete candidate pool `chaosx.nr14.2.a`, `chaosx.nr14.2.b`, and `chaosx.nr14.2.c`.

The call returned `PROBABILITY_SOURCE_INSPECTED` with `poolComplete = true`, three candidates, zero unresolved discovery inputs, source revision `29b9f4988065da535cba9877f28b8e4d996f74f22a2c8521a7263c2c5bde3f59`, and source hash `43741ef93efa26aaceb965a672987f3f567226716ae7e9b1382c30bbd71bf945`.

Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/33f2eda03d449184d3a383fbbdb9598e4e10a9296e27c7846b8459b7d99d38ae/7d478084b931bfbc5229d7b68b197c81e9d8c12a85b312e92c730eec83f36e29/probability-inspect-43741ef93efa.json`.

## Named evaluations

The empty baseline scenario set `E014_POLICY_BASELINE_2026_08_26` produced `PROBABILITY_ANALYZED_PARTIAL` with seven unresolved trigger rows. The adapter proved raw base scores of 55, 30, and 15 for `.2.a`, `.2.b`, and `.2.c`, but did not normalize effective probabilities while government, stability, and `check_variable` inputs were undeclared.

Baseline artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bdace8a904f60d64b66163df0d534f7d36245252bc8371411060c9771653da72/8555525fb2165237ec902b1be823627b543067d508c9f0740b6387ab46186c0b/probability-b06f21d7f686fb3f762e79bb.json`.

The democratic stable scenario set `E014_POLICY_DEMO_2026_08_26` supplied `has_government = democratic`, `has_stability = 0.70`, and `cannibalism_command_integrity = 0.80`. It produced `PROBABILITY_ANALYZED_PARTIAL` with four unresolved trigger rows, resolved the government and stability predicates where typed, and emitted two informational diagnostics that the authoritarian modifiers were not active in that scenario.

Democratic artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6dbeb005d6d33c23e9e9a5ea0bba8d7342d395c8ac4c3ef826fc0c77c2230a11/8d3e4452b321a169edb9e01d524e8c1bae670b30cddc55970daa0e067d4a07de/probability-d7b7f588160bc1a4aa1ab102.json`.

A second probe using the scalar `check_variable` fixture was accepted by the adapter and reproduced the same partial result under analysis id `probability-e4bf5293bc757d6d04c79807`; it did not establish numeric variable comparison semantics and is retained only as schema evidence.

## Current player-host safety refresh

`hoi4.probability_inspect` also inspected the complete player-host pool `chaosx.nr14.30.a` and `chaosx.nr14.30.b` in the same Event 014 source. It returned `PROBABILITY_SOURCE_INSPECTED` with `poolComplete = true`, two candidates, zero unresolved discovery inputs, the same source revision and source hash, and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bacc7181b435f9380ad77dedccbf5c5b35c52e86a4788245d267f39df1997de1/46d1e400ea8ceca4b32dfb251efd988aed707027d10e673aa407e6270b4d3429/probability-inspect-43741ef93efa.json`.

The named scenario set `E014_EVENT_30_PLAYER_SAFETY_CURRENT_2026_08_26` supplied `is_ai = true` for `AI_REMAINS` and `is_ai = false` for `PLAYER_COUNTRY`. `hoi4.probability_evaluate` returned `PROBABILITY_ANALYZED` with zero unresolved rows under analysis id `probability-e00ddb0961107eb5dddc9a55`; its JSON artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/22de3ab624e52f4a77acf7d224edd81cb3d47cac9fefd6b941e085a803331e77/d014f2e6ba3eddedf2bd6d67d66284ea30a7094fce4326213015ff23fce741f2/probability-e00ddb0961107eb5dddc9a55.json`.

The adapter reports the intended safety behavior: `.30.a` is the only AI-eligible outcome and is dominant in both scenarios, while `.30.b` is eligible-but-zero only in the human scenario because its source trigger requires `is_ai = no`. The dominance and starvation diagnostics are intentional route-protection warnings, not a balance patch request.

## Current revealed capture-outcome refresh

The complete four-option `chaosx.nr14.81` pool was inspected from the same event source and returned `PROBABILITY_SOURCE_INSPECTED` with zero discovery inputs unresolved. The inspect artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/53be38643ba412a521e72ae6e4482b35fd731a83ba4d94ac62543d0af7ea2d81/d1f7020627da30e6a65550c02ead3831ba145694781a0575e74cae1e5c238b68/probability-inspect-43741ef93efa.json`.

The scenario set `E014_EVENT_81_CAPTURE_OUTCOMES_CURRENT_2026_08_26` evaluated fascist, democratic, and neutrality government states with `PROBABILITY_ANALYZED`, zero unresolved rows, and zero diagnostics under analysis id `probability-e94c3a2b6a55df0b0d2adf88`. The JSON artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/75c6823eee4213d07cf98ef6b1b6c2e0eac3b6ae21702386c25cb740c97bbd9c/4f783b828e926648ca36c3ad635e8e3435f05fbbd7a910259572445f725c26c6/probability-e94c3a2b6a55df0b0d2adf88.json`.

The conditional results are exact and source-intended: fascist weights 60/30/25/30 normalize to 12/29, 6/29, 5/29, and 6/29; democratic weights 150/30/10/30 normalize to 15/22, 3/22, 1/22, and 3/22; neutrality weights 60/30/10/30 normalize to 6/13, 3/13, 1/13, and 3/13. These are conditional outcomes after the reveal and captured-Hannibal target gates, not campaign-wide route frequencies.

## Current random-list identity refresh

`hoi4.probability_inspect` used adapter `random_list` against `common/scripted_effects/014_cannibalism_effects.txt` and discovered 42 entries across the seven regional name pools, the six-personality pool, and three outcome pools. The source revision was `7378fff1bc4a086c1027c2fe8810e0117aaf860950140fed3177d9a69a16946c`, the source hash was `bcfa8fcbd35017d04d195b81f465da45a62469578246ff437f6ac3b8ab54a45c`, and the complete-source discovery artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3d36481815c811a4a9c0089d6ee253725829521dd29194691d2a9528277172ca/ac4a82158d4323bbc38558cc1ec615ec203616908d89e2265b3dc1de5ef3faac/probability-inspect-bcfa8fcbd350.json`. The aggregate discovery remains `poolComplete = false` because the adapter treats the separate source blocks as one unresolved aggregate surface.

The European regional name block at source line 4648 was evaluated as a complete four-candidate pool under `E014_WARLORD_REGIONAL_NAMES_CURRENT_2026_08_26`. `hoi4.probability_evaluate` returned `PROBABILITY_ANALYZED` with `analysisId = probability-70d9e4d318b9b89efc0e3618`, four candidates, zero unresolved inputs, zero diagnostics, and exact conditional probability 1/4 per candidate. The JSON artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a112addbdcb6933444505be8893a6c63dbdc652ce1cd355073ff355139bef1b8/863a2044139da7ff22587b27982693973ea26e5823965d0a1e3177fa26345f50/probability-70d9e4d318b9b89efc0e3618.json`.

The six-personality block at source line 4711 was evaluated as a complete six-candidate pool under `E014_WARLORD_PERSONALITIES_CURRENT_2026_08_26_RETRY`. `hoi4.probability_evaluate` returned `PROBABILITY_ANALYZED` with `analysisId = probability-0b60164f800cc68bea44b098`, six candidates, zero unresolved inputs, zero diagnostics, and exact conditional probability 1/6 per personality. The JSON artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f4b87489a04fbf314495815561ce009e18591a9c6658d59b88e7bdceb20b2d94/73f7644d5ab6d826b2c3088f90b9f64eec8d0fb64691396b989c6c2a47421dd8/probability-0b60164f800cc68bea44b098.json`.

## Disposition

This refresh strengthens current source-revision evidence for the opening-policy weights but does not certify normalized campaign probabilities, route dominance, or dynamic host selection.

The random-list refresh strengthens two identity sub-pools, but it does not certify the aggregate seven-region selector, dynamic region assignment, or the three outcome blocks because those remain separate or variable-derived surfaces.

No balance patch is justified. Any future weight or trigger change must rerun source-qualified inspection and the same named scenario evaluations, then use `hoi4.probability_compare` with identical pools and scenarios.
