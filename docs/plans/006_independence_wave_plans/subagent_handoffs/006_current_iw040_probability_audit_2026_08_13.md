# IW-040 Kuban current probability audit (2026-08-13)

## Scope and status

This is a read-only probability audit of the current IW-040 Kuban decision and mission surface in `common/decisions/006_independence_wave_kuban_decisions.txt`.

No gameplay, AI, event, localisation, or runtime source was edited, staged, or committed.

The decision surface is `independence_wave_kub_mounted_compact_category`, with eleven discovered `mission_ai_will_do` candidates.

The audit is partial and does not establish campaign balance because the MCP adapter reported `poolComplete = false` and `availableCandidates = 0` under the supplied fixtures.

## Source review

The source-level AI formulas are:

| Mission | Source base | Source modifier trace |
| --- | --- | --- |
| `independence_wave_kub_hold_mounted_compact_together` | `urgent` = 100 | none |
| `independence_wave_kub_secure_mounted_depots` | `high` = 25 | none |
| `independence_wave_kub_integrate_border_guards` | `high` = 25 | `factor = modifier_double` = 2 when `has_war = yes` |
| `independence_wave_kub_register_community_compacts` | `high` = 25 | none |
| `independence_wave_kub_settle_former_host_ledgers` | `standard` = 10 | `factor = modifier_double` = 2 when `NOT = { has_independence_wave_severe_host_threat = yes }` |
| `independence_wave_kub_ratify_constitutional_autonomy` | `high` = 25 | none |
| `independence_wave_kub_adopt_agrarian_compact` | `standard` = 10 | none |
| `independence_wave_kub_convene_socialist_councils` | `high` = 25 | none |
| `independence_wave_kub_establish_mounted_emergency_command` | `urgent` = 100 | `factor = modifier_double` = 2 when `has_war = yes` |
| `independence_wave_kub_codify_durable_sovereignty` | `high` = 25 | none |
| `independence_wave_kub_open_black_sea_steppe_network_corridor` | `standard` = 10 | none |

The constant definitions are in `common/script_constants/006_independence_wave_decision_constants.txt` (`standard = 10`, `high = 25`, `urgent = 100`, `modifier_double = 2`).

These are source score formulas, not click probabilities.

Every candidate also has visibility, availability, route, capital-control, cost, active-project, crisis, and lifecycle gates in the decision source; those gates are not represented by the empty state fixtures below.

## Required MCP evidence

### Initial mission adapter inspection

The mandatory first weighted-surface call was `hoi4.probability_inspect` with adapter `mission_ai_will_do` and source `{path: "common/decisions/006_independence_wave_kuban_decisions.txt"}`.

Result: `PROBABILITY_SOURCE_INSPECTED`, status `ok`, workspace `mod_chaos_redux_ea3b2d67c2c0`.

Inspection artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7ac61a2498fcf2916b4ca1b36a30b91f8b566776aeccacde82e309bb53b0db0d/f53b6f785d6e64e32c1ffc17629ad8146882e0d56fa7575af0c0ea74c64c880/probability-inspect-de8e919c4eae.json`.

Inspection artifact SHA-256: `7ac61a2498fcf2916b4ca1b36a30b91f8b566776aeccacde82e309bb53b0db0d`.

Inspection source revision: `8a65689a54fa0b3f29389307df0e38a4966dd5fdeb79c8613e668646940d3bb5`.

Inspection source hash: `de8e919c4eae46c9abbb6fdb38703ccc0e59039dbd43c6eeeb120e3fe911a093`.

Inspection reported 11 adapters, 11 discovered candidates, 0 available candidates, 15 required inputs, 0 unresolved inputs, and `poolComplete = false`.

### Named scenario evaluation

The evaluation used adapter `mission_ai_will_do`, the complete source-enumerated candidate list above, raw score output, ranking output, and unresolved output.

Scenario-set id: `iw040-kub-current`.

Scenario ids: `KUB_FOUNDING`, `KUB_PROJECT_READY_PEACE`, `KUB_PROJECT_READY_WAR`, `KUB_HOST_LOSS_FALLBACK`, `KUB_ROUTE_LOCKS`, and `KUB_NETWORK_READY`.

Each scenario supplied `state = {}` because typed campaign fixture fields were not accepted by the recovered route.

The candidate list was complete relative to the eleven mission IDs discovered in the current file, but it was not a complete engine-available selection pool: the adapter still reported zero available candidates and `poolComplete = false`.

Result: `PROBABILITY_ANALYZED_PARTIAL`, status `ok`, analysis id `probability-a03ca1ed802dbb497cc57422`.

Scenario hash: `0652c4cc5f95699e8f09ab0167d20b60e4d5214911f5a1423096b47a02452dbb`.

The evaluation reused source revision `8a65689a54fa0b3f29389307df0e38a4966dd5fdeb79c8613e668646940d3bb5` and source hash `de8e919c4eae46c9abbb6fdb38703ccc0e59039dbd43c6eeeb120e3fe911a093`.

The adapter analyzed 66 candidate/scenario rows and returned `unresolved = 116`, `diagnostics = 11`, and `analysisStatus = partial`.

All eleven candidates were diagnosed as `PROBABILITY_OUTCOME_NEVER_ELIGIBLE` across the six empty-state scenarios.

This never-eligible result is exact for the supplied fixture evaluation but is not evidence that the missions are permanently impossible in live campaign state.

The 11 diagnostics are conditional fixture results for `hold_mounted_compact_together`, `secure_mounted_depots`, `integrate_border_guards`, `register_community_compacts`, `settle_former_host_ledgers`, `ratify_constitutional_autonomy`, `adopt_agrarian_compact`, `convene_socialist_councils`, `establish_mounted_emergency_command`, `codify_durable_sovereignty`, and `open_black_sea_steppe_network_corridor`.

Rendered evaluation evidence:

- Ranking SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5ea14e824135fbe36abd0e238a0d29580b36381121a56a2c9318e07cf6511b4d/c0232f61bd2d3207fd995cb743bcb16b2d8da4c193d61a5633ad7217b7199d9d/probability-probability-a03ca1ed802dbb497cc57422-ranking.svg`.
- Ranking PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8787fd7c36875c9e59859307b48ffe2fa667c27db2ae3e770298bce374b016dd/aa059db36fed946ef31420838075d249c857f68ea3bd38dc2e745603548d36ea/probability-probability-a03ca1ed802dbb497cc57422-ranking.png`.
- Unresolved SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c2422e28e8b758734cf2728610718afd55e081893032c6f84152a1c8c5d7becd/0cd533517c6b6dea952875032383ee29a3893f2925cc25af97b74159c7257d1a/probability-probability-a03ca1ed802dbb497cc57422-unresolved.svg`.
- Unresolved PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/74c80fe64038d09259cd1ff645f55d1ecb21bc7355be6884e4e44e9ba7418b11/68ed326d158dcb299cb12f468aeee92aa61831aeb8880d4aec80a8fcbb3320d3/probability-probability-a03ca1ed802dbb497cc57422-unresolved.png`.

### Current/current comparison

`hoi4.probability_compare` was run with the same adapter, candidate list, scenario set, and current source on both sides.

Result: `PROBABILITY_ANALYZED_PARTIAL`, status `ok`, analysis id `probability-0ed2aec879bf4ce061bc5ca6`.

The comparison reused scenario hash `0652c4cc5f95699e8f09ab0167d20b60e4d5214911f5a1423096b47a02452dbb`, source revision `8a65689a54fa0b3f29389307df0e38a4966dd5fdeb79c8613e668646940d3bb5`, and source hash `de8e919c4eae46c9abbb6fdb38703ccc0e59039dbd43c6eeeb120e3fe911a093`.

Comparison result: `comparisonChanges = 0`, `unresolved = 116`, `diagnostics = 11`, and `analysisStatus = partial`.

This is a capability/current-current receipt only; it does not prove a before/after balance change.

Rendered comparison evidence:

- Comparison JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/43666cf1a3a64e1f31a16aaf1b276667784b0f4f90162f662f9a6a6d1bc172a4/9e3bc3839dd1cba8701f0b8e227c33d2210c7927e0dbd3457f4c19e5051ba3de/probability-0ed2aec879bf4ce061bc5ca6.json`.
- Ranking SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f2e33c7e39889c8746a9fc4c4fa6dad16f3a37dfeb12b029c2179e56a5f87d84/41e20c3a0426d4701c6ec8d815aab2afb7efc0254bad40e8e8978b07ff804e8c/probability-probability-0ed2aec879bf4ce061bc5ca6-ranking.svg`.
- Ranking PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c2c0a1cc88c7b5907efd41b916865d606222cb654d6c63fae6be940828bbc58d/9052651ad69258996c1f8bc516cb2ac35ff7bc9add9bf2fd0f78fbff706d935c/probability-probability-0ed2aec879bf4ce061bc5ca6-ranking.png`.
- Comparison SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2450d67f32f665574260ffbd84f57cc7db1a9cf58aca09b66d13c1108a27cc49/5069a1c539c9946132536c6a8a64aef4cd94ff6a53fedd70034494a73fa3687f/probability-probability-0ed2aec879bf4ce061bc5ca6-comparison.svg`.
- Comparison PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a1fd8e11d21dd2414c85f7412d454fa53b5b857ed9fb09593caa20f6277f498f/2771644f602e030e079572dbe0b3f127361c034d9226a40119fa1762776212da/probability-probability-0ed2aec879bf4ce061bc5ca6-comparison.png`.
- Unresolved SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c2422e28e8b758734cf2728610718afd55e081893032c6f84152a1c8c5d7becd/aee016b52a11080e1a44922302523f460478e8c522f44e60367275294ddd94c9/probability-probability-0ed2aec879bf4ce061bc5ca6-unresolved.svg`.
- Unresolved PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/74c80fe64038d09259cd1ff645f55d1ecb21bc7355be6884e4e44e9ba7418b11/8c7c4c92f0246a9a5252d144a34c9b990df51084099e5e1839a9ef65430b9065/probability-probability-0ed2aec879bf4ce061bc5ca6-unresolved.png`.

### AI strategy adapter inspection

Because the mission adapter had no available candidates, `hoi4.probability_inspect` was also run with adapter `ai_strategy_factor` against `common/ai_strategy/006_independence_wave_kuban.txt`.

Result: `PROBABILITY_SOURCE_DISCOVERED`, status `ok`, with `discoveryReason = no_weighted_surfaces`, 0 candidates, 0 available candidates, 0 required inputs, and 0 unresolved inputs.

AI-strategy inspection artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1e1f8bb52d1d56cd9314b43d6e9e5961dfcd4e8486fc9f3af02bed1ea0ec9b92/cecf181cc3998763c949e9315f9400f4130396a727ecfcbd71bbffbd2a14463a/probability-inspect-e4407e6b4829.json`.

AI-strategy source hash: `e4407e6b4829fb90a50f76e0766a883e1663896c931c829ab15fe9a8b2341d9c`.

The source contains four static KUB strategy blocks for mounted survival, former-host restraint, settled compact, and emergency guard, but the requested `ai_strategy_factor` adapter exposes no analyzable weighted surface for them.

## Findings

No candidate ranking, dominance, starvation, rank reversal, repetition, or exploit-risk conclusion is valid for live campaign behavior from this run because the engine fixture made all candidates unavailable and the normalized pool was incomplete.

The source score ladder is intentionally non-flat (`urgent` 100, `high` 25, `standard` 10), with conditional doubling for war-sensitive military actions and for former-host settlement when severe host threat is absent.

The current source therefore has a score race in principle, but this run did not prove which actions win once route, cost, capital, crisis, host, network, and state-control gates are populated.

The empty fixtures also prevent verification of AI validity for `is_independence_wave_kub_project_ready`, `capital_scope = { is_controlled_by = ROOT }`, costs, active-project serialization, route government, former-host validity, state 234 ownership/control, and network membership.

## Recommended follow-up (do not apply in this audit)

Provide typed fixture values or a supported state adapter for the six named scenarios, including package/setup flags, compact pressure ledgers, route flags and government, state-234 ownership/control, capital control, available civilian-factory/cost gates, active-project status, former-host existence and war state, severe-host-threat flag, founding-settlement completion, network membership, league-route availability, durable-sovereignty flag, and `has_war`.

Rerun `hoi4.probability_evaluate` with the same six scenario IDs and complete available candidate pool after fixtures resolve.

Rerun `hoi4.probability_sweep` for `has_war` and `has_independence_wave_severe_host_threat` with explicit boolean/numeric alternatives; the attempted sweep was blocked with `PROBABILITY_SWEEP_RANGE_REQUIRED` because every sweep path lacked a scenario range or numeric alternatives.

Use the same scenario hash and candidate list for any owner-applied AI patch, then run a true before/after `hoi4.probability_compare` rather than another current/current capability comparison.

## Skipped or blocked analyses

The sweep was not analyzed because the MCP returned `PROBABILITY_SWEEP_RANGE_REQUIRED` for scenario `KUB_FOUNDING`, path `state.has_war`; no range, numeric alternatives, or numeric state value was supplied.

No seeded simulation was run because no uncertain inputs were explicitly declared and the candidate pool was unavailable.

No custom-pool sequence was run because this is a mission score race, not a declared custom weighted pool with cadence, cooldown, recovery, removals, resets, and terminal states.

No additional AI-strategy evaluation was run because the AI-strategy adapter discovered no weighted surfaces.

## Classification

Source formulas and constant substitutions are exact source evidence.

The six-fixture eligibility results are exact for the supplied empty-state fixtures but bounded to those fixtures.

The all-never-eligible, ranking, and unresolved outputs are partial MCP evidence and must not be generalized to live campaign probability or balance.

No exact selection probability is claimed.

