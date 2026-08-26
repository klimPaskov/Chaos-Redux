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

## Disposition

This refresh strengthens current source-revision evidence for the opening-policy weights but does not certify normalized campaign probabilities, route dominance, or dynamic host selection.

No balance patch is justified. Any future weight or trigger change must rerun source-qualified inspection and the same named scenario evaluations, then use `hoi4.probability_compare` with identical pools and scenarios.
