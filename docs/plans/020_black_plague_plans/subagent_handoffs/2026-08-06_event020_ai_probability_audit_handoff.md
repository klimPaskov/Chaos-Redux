# Event 020 AI and Probability Audit Handoff

Audit date: 2026-08-06. Scope is read-only weighted logic and probability evidence for Event 020 Black Plague. No gameplay, AI, event, focus, decision, or constant files were edited.

## MCP provenance

The mandatory `hoi4.probability_inspect` adapter discovery completed in workspace `mod_chaos_redux_ea3b2d67c2c0`; the installed adapter target is Operation Postern 1.19.2.0 (d245). All probability conclusions below are separated into exact, score-only, bounded, and unresolved evidence. The full event source query and the full weaponization event source query each timed out after 180 seconds; the narrow source/candidate queries below completed.

## Audited surfaces

### Event option `chaosx.nr20.46`

Source: `events/020_black_death.txt`.

Adapter: `event_option_ai_chance`, `hoi4.probability_inspect` with candidate pool `{chaosx.nr20.46.a, chaosx.nr20.46.b}` and the six `chaosx.nr20.80.a.*` options. Source revision `a0a064679f1bdf4b2970537e10a663c4ee817eff0a37d3fb1de754c1e86d62ba`; source hash `7923851ea457a0d42da7beb20cd621de5a302c42e1fdc8a19cc4b38b4297177f`. The inspect artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/caad13ed6baf41fdbd4787ef5b757c00d538db1e959d2a71c4613e95b3524eef/5201428899804e61cf4b1e2da5a56ad2627b57742a21af7591979e2a46c1838c/probability-inspect-7923851ea457.json`.

`hoi4.probability_evaluate` used complete candidate pool `{chaosx.nr20.46.a, chaosx.nr20.46.b}` under scenario set `NR20_HUNGER_RESOLUTION_MATRIX_2026_08_06`, scenarios `HUNGER_COHERENCE_LOW_MASS_LOW` and `HUNGER_COHERENCE_HIGH_MASS_HIGH`, scenario hash `603162fda0f62ccedd2a8f58aff506f32484fe2b9db07e96abd47d8690848e88`. Analysis id `probability-bcc57001e9dc66e921c160cd`; JSON artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/103d17626b61239accc36c363cf105f626b04aff4fd00391e8ecca76fc2a5a9a/7314177640bae155bfc6e59f19211b41140fcec1561025dd914350de44661d59/probability-bcc57001e9dc66e921c160cd.json`; ranking and unresolved render artifacts were also emitted by the tool.

The engine-supported base scores are exact and score-only: option `.46.a` has factor 75 and `.46.b` has factor 25. The conditional factor 2 on `.46.a` requires `has_variable black_plague_rat_coherence` plus a numeric coherence trigger; the conditional factor 2 on `.46.b` requires numeric `black_plague_rat_brood_mass` at the dominance gate. The declared scenario state fields did not satisfy the adapter's typed trigger-input contract, so all effective modifiers and normalized categorical probabilities remain unresolved. Do not report 75%/25% as effective selection probabilities. The adapter also detected two categorical pools when `.80` was included (`MULTIPLE_CATEGORICAL_POOLS`); `.80` is an eligibility-gated target-continent choice set with no `ai_chance` weight block, not one normalized six-way chance pool.

Classification: base factors exact; effective chance unresolved; `.80` eligibility-only/score-free; no rank or probability claim.

### Rat decisions

Source: `common/decisions/020_black_plague_rat_decisions.txt`.

`hoi4.probability_inspect` with `decision_ai_will_do` succeeded only for two active indexed candidates (`black_plague_rat_record_the_dead`, line 472, and `black_plague_rat_resolve_brood_succession`, line 373). Source revision `4ff09633f211c0565e6dacbb6490d6e49d7418001f0600b997255728ce1bc943`; source hash `ef74839ba8036e09649bd6c433fa039aeddcb0b2ed8b6812632f809dc46d6f2e`; artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bbf863bdc6f19d714c5469431985a6f8c4c097678f6e691af6a058db443682ae/051d0918eaf3a372ebccf1407cff528557376a1d7811b363a8122bba022c0e42/probability-inspect-ef74839ba8036e09649bd6c433fa039aeddcb0b2ed8b6812632f809dc46d6f2e.json`.

The adapter reports `selectionRule = score_only`, `rawScore = true`, `normalizedProbability = false`, `poolComplete = false`, and required scenario input `check_variable`. The shared index explicitly discovers only active, unshadowed decision blocks, so Crown Strike, royal-node, crown-the-continent, and terminal decision blocks were not available to this adapter. Repeating with candidate overrides and `mission_ai_will_do` produced the same exact blocker: `PROBABILITY_SURFACE_EMPTY` / “No weighted blocks matched this request” for the source. This is an adapter coverage blocker, not evidence that those source `ai_will_do` blocks are absent.

### Response, shared-response, and weaponization decisions

Sources: `common/decisions/020_black_plague_response_decisions.txt`, `common/decisions/020_black_plague_shared_response_decisions.txt`, and `common/decisions/020_black_plague_weaponization_decisions.txt`.

`decision_ai_will_do` inspection returned `PROBABILITY_SURFACE_EMPTY` for all three sources, including explicit candidate pools for `black_plague_shared_strike_royal_node`, `black_plague_shared_strike_the_crown`, `black_plague_shared_seal_royal_burrows`, and the weaponization decisions. No artifact was produced. These surfaces remain unproven by MCP; source-only constants or static scans must not be described as AI selection probabilities. Crown Strike/royal-node audit is therefore unresolved pending an adapter route that can index the nested/targeted decision blocks.

### Rat focus trees

Sources: `common/national_focus/020_black_plague_rat_focus_tree.txt` and `common/national_focus/020_black_plague_rat_king_focus_tree.txt`.

`national_focus_ai_will_do` inspection succeeded. The rat tree contains 52 discovered focus candidates (`poolComplete = false`, required inputs `check_variable`, `focus.external_factors_complete`, `has_completed_focus`, `has_variable`, `num_of_controlled_states`); inspect artifact from the latest refresh: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/731adc86d92171e376ab6736cb916979e44aac3cd4c87b79a43d26869e1a2b53/d7a82204eb8212f5c15e57c59e34ab46bb5e8e302e37110dd300759db2b99e70/probability-inspect-8bcde52ff27f.json`, source revision `8125b25ac62d0533c1d41f603fd6fd93e4c216aeaa542b7ab1de9a3c9653a01a`, source hash `8bcde52ff27fa128052fa498ae2e767c1b38974a546ffc83f83fa66b535bf57c`.

The Rat King tree contains 71 discovered candidates (`poolComplete = false`, six required input classes); its inspect artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b6b9dcbf7dba82a5984c04e42aaeaf42fae6a1caa7ba3083dbbc8e9590e4e055/48525d9f488ef5e17cce8b302d3f79e3182476eddda6bd9e8738ae42e568c7d6/probability-inspect-5cd85432168e.json`, source revision `aa644a8c1d668620aaa3e1e5557bc0902d72322b04818f757ce6124694485e39`, source hash `5cd85432168e8150b1c83d0607409a19a15cc51ce868a76ddf1906a64104024e`.

Because neither focus pool is complete and external focus factors/prerequisite completion are undeclared, no normalized focus-choice probabilities, dominance, starvation, or rank-reversal claim is valid. The adapter warns that ordered AI strategy plans can override the score race.

### Spread random lists

Source: `common/scripted_effects/020_black_plague_spread_effects.txt`.

`random_list` inspection found 12 entries in six distinct complete two-entry pools at lines 526, 541, 550, 559, 582, and 605. Inspect source revision `e8f304138941a5e10b915648e545ec33282a7a655a8d62fb013d4caf0af1d243`, source hash `a4ad50a7855dcb04739d005c78f63919d1982b0b28f0c2403bc42039909c1345`, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ef9f89876c4970c9c85dba7e0feea1e0a2c32b73a7447740f1bd4fefc52a263e/c4eb56fb6f1cc83e00426e293182ff9de2e302ff2ef0b73acafcb86f73d7d80d/probability-inspect-a4ad50a7855d.json`.

Complete-pool `hoi4.probability_evaluate` calls used one declared empty external state per pool. The land analysis is fully parsed and exact: analysis id `probability-4e4074262b86bf73f0396f51`, scenario `E020_ROUTE_LAND_BASE_2026_08_06`, scenario hash `778217dbe0440d5053b49e23b4ccfe8de3763f90673e15900d1c7bd898716f5a`, JSON artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/61df63c586bf11fa8d1a02966fab363bec04a830f6f2205e33d920346c521b5c/1d0bf21554ba8a2bd2b9885632cdfca99c5ea53abf04f48dfdeec1a5a5783935/probability-4e4074262b86bf73f0396f51.json`. It proves land success 28/100 and failure 72/100, with exact support and no unresolved inputs.

The corresponding complete-pool analyses returned exact, zero-unresolved results for troop, refugee, local-port, internal-transport, and overseas pools. Their analysis ids were `probability-48b81c63bca08493c185df45`, `probability-9a49fc45562a71bfbf25e0f0`, `probability-0792a673c75bd24742ee4d96`, `probability-8a79069d2b4e631161dfb1a0`, and `probability-0757496b09cde04c5dadd0c2`, respectively. Source constants independently identify the exact weights: troop 24/76, refugee 22/78, local port 20/80, internal transport 18/82, and overseas jump 6/94. The overseas run emitted `PROBABILITY_DOMINANT_OUTCOME` at 0.94; this is an explicit dominance warning, not a bug by itself. The adapter is `proportional_categorical`; each pool must be evaluated separately and cannot be merged into one global spread probability.

### Weaponization random lists, MTTH, strategy factors, and weighted origin

`random_list` inspection of `common/scripted_effects/020_black_plague_weaponization_effects.txt` succeeded with four discovered entries and one unresolved item; inspect artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cbc8056b63aa5d04954ffb5abf0594b889361a82a822cde0b89007d9d8cb1f53/213f139e1be100659d08fa6618db31f7b72eb0d52b64733a32a45cc309f4de1e/probability-inspect-362254a8e39a.json`, source revision `cbc65305dd105ea880ae23d3b2091bbf6dcc06f1b38daef57237d3185bea13e8`, source hash `362254a8e39aced96810b689738eb78b6539ee9f153dad6f2dc62446167f4eba`. The two source pools are the 18/82 accident check (line 64) and 2/98 stockpile failure check (line 275). Dynamic effect-derived conditions were not evaluated; preserve as unresolved until a complete pool and cadence scenario is supplied.

`event_mean_time_to_happen` inspection of `common/mtth/020_black_plague_rat_mtth.txt` returned `PROBABILITY_SURFACE_EMPTY`; no timing distribution was proven. `ai_strategy_factor` inspection of `common/ai_strategy/020_black_plague_rat_ai_strategy.txt` returned the same exact empty-surface blocker. The weighted mainland origin path in `common/scripted_effects/020_black_plague_effects.txt` is a dynamic `random_scope_in_array` ticket pool assembled from every valid state and per-state population/industry/route modifiers; no direct MCP probability adapter result was available for this custom pool. Do not claim a global origin probability without a declared state candidate array and all external modifiers.

## Findings and recommendations (no patches applied)

- Keep `.46` base factors documented as score inputs only; provide typed `has_variable` and numeric variable declarations before claiming effective hunger-resolution chances, then rerun `probability_compare` on the same two scenarios.
- Obtain an MCP adapter route for nested/targeted decision blocks before balancing Crown Strike, royal-node, terminal campaigns, or response decisions. Until then, all AI-race conclusions for those files are unresolved.
- Treat focus trees as incomplete candidate pools; run named route scenarios with prerequisite history, variables, and ordered strategy plans before making dominance/starvation claims.
- Preserve separate two-entry spread pools. The exact route odds above are conditional on the route pool being entered; they are not world-level spread probabilities. Review the 94% overseas no-jump warning against the intended Evolution II pacing.
- Evaluate weaponization and weighted-origin systems with explicit custom-pool/cadence adapters once the dynamic array and state inputs can be declared. Include cooldown, terminal, reset, and removal state in any sequence scenario.

## Remaining blockers and skipped analyses

Skipped or unresolved: full event-source probability inspection (180-second timeout); full weaponization event-source inspection (180-second timeout); response/shared-response/weaponization decision AI (adapter `PROBABILITY_SURFACE_EMPTY`); Rat King terminal decision/mission candidate indexing (same adapter limitation); Rat MTTH timing (`PROBABILITY_SURFACE_EMPTY`); AI strategy factors (`PROBABILITY_SURFACE_EMPTY`); weighted mainland origin custom pool (no supported direct adapter route); effective `.46` conditional factors (scenario variable typing unresolved). No exact normalized probability is asserted for any incomplete pool.
