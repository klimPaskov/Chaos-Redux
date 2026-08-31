# Event 006 probability audit handoff — 2026-08-31

Status: read-only partial audit. No gameplay, AI, event, focus, decision, mission, or tuning files were changed.

## Scope and classification

The audited Event 006 surfaces are the automatic package allocator, regional package pools, formable Congress resolution, scenario registry, evolution MTTH, root and support event `ai_chance`, shared and package decision/mission `ai_will_do`, and the generic focus AI surface.

The only new scenario evaluation completed in this run was `E006_ALLOCATOR_EMPTY_FIXTURE_2026_08_31` with `CALM_EMPTY`, `GATHERING_EMPTY`, `RISING_EMPTY`, `TOTALEN_EMPTY`, and `WORLD_COLLAPSE_EMPTY` at a one-day horizon.

The retained named scenario contracts from the current Event 006 handoffs are `E6_ROOT_OPTION_MATRIX_2026_08_24` (`E6_CORE_EMPTY_CURRENT_2026_08_24`, `E6_SHARED_DECISION_EMERGENCY_2026_08_24`, `E6_SHARED_DECISION_PROVISIONAL_2026_08_24`), `E6_SHARED_DECISION_SCENARIOS_CURRENT_2026_08_06` (`E6_SHARED_OPEN_CALM`, `E6_SHARED_HOST_CRISIS`, `E6_SHARED_ROUTE_LOCKED`, `E6_SHARED_NO_VALID_TARGET`), `E6_SHARED_MISSION_SCENARIOS_CURRENT_2026_08_06` (`E6_SHARED_MISSION_OPEN`, `E6_SHARED_MISSION_HOST_CRISIS`, `E6_SHARED_MISSION_ROUTE_LOCKED`, `E6_SHARED_MISSION_NO_VALID_TARGET`), `E6_CRISIS_MISSION_SCENARIOS_CURRENT_2026_08_06` (`CRISIS_PRESSURE_OPEN`, `CRISIS_REQUESTER_LOST`, `CRISIS_RETRY_EXHAUSTED`, `CRISIS_NO_PRESSURE`), `E6_FOCUS_SCENARIOS_CURRENT_2026_08_06` (`FOCUS_OPEN_CALM`, `FOCUS_HOST_CRISIS`, `FOCUS_ROUTE_LOCKED`, `FOCUS_NO_VALID_ROUTE`), `E6_KUB_MISSION_MATRIX_2026_08_24` (`KUB_FRAGILE_PEACE`, `KUB_SEVERE_HOST_WAR`), and `E6_TAT_MISSION_MATRIX_2026_08_24` (`TAT_FRAGILE_PEACE`, `TAT_SEVERE_HOST_WAR`).

All results below are either exact MCP discovery metadata, bounded/partial MCP output, or source-only evidence. No exact campaign selection probability, timing distribution, dominance, starvation, or rank-reversal claim is made.

## Source surfaces and current workspace fingerprints

| Surface | Source and identifiers | Static pool or block evidence |
|---|---|---|
| Outer automatic allocator | `common/scripted_effects/006_independence_wave_effects.txt`; `independence_wave_select_one_automatic_package`, `independence_wave_allocate_automatic_packages` | One outer `random_list` with fourteen regional entries; selection is repeated until target, attempt cap, or `independence_wave_plan_pool_exhausted`. |
| Regional package allocator | `common/scripted_effects/006_independence_wave_package_region_effects_registry.txt`; `independence_wave_select_region_01_automatic_package` through `_14_automatic_package` | Fourteen regional lists and 126 package weight entries. The complete runtime candidate set still depends on country, anchor, host, reservation, package, route, and attestation state. |
| Allocator modifier computation | `common/scripted_effects/006_independence_wave_package_planner_effects.txt` | Source constants expose base 100, sponsored candidate +100, registered tag +25, new region +30, new host +20, prior package −80, prior region −25, prior host −20, low-chaos signature −35, high-chaos +45, and minimum floor 1. World-collapse rarity is 1.35. These are source traces, not normalized probabilities. |
| Formable Congress | `common/scripted_effects/006_independence_wave_formable_registry_effects.txt`; `independence_wave_formable_resolve_congress` | Two random-list entries, success and failure. Failure risk is tier-based with source bases 15/25/40/55, opposed +15, observer +5, controlled-anchor relief −10, surplus-consent relief −5, military method +10, hidden high-chaos method +15, and a 5–85 clamp. |
| Scenario selection | `common/scripted_effects/006_independence_wave_scenario_effects.txt`; `independence_wave_scenario_rebuild_ranked_registry` | 138 deterministic ranked registry additions; this is a deterministic navigation/ranking surface, not a probability-proportional pool. |
| Evolution timing | `common/mtth/chaosx_mtth_variables.txt`; `independence_wave_evolution_interval`, called by `independence_wave_schedule_next_evolution_check` in `common/scripted_effects/006_independence_wave_evolution_effects.txt` | Base 300 days, clamp 90–720 days, factors Gathering Storm 1.15, Rising 1, Chaos Tier 0.85, Totalen Chaos 0.7, World Collapse 0.55, thin network 1.25, dense network 0.8. |
| Root event options | `events/006_independence_wave.txt`; root `chaosx.nr6.1` and downstream `chaosx.nr6.*` options | Static scan has 11 `ai_chance` blocks; the adapter discovered 22 candidates but could not establish a complete visible pool. |
| Support event options | `events/006_independence_wave_support_events.txt`; support `chaosx.nr6.*` options | Static scan has 136 `ai_chance` blocks; the adapter discovered 154 candidates but could not establish a complete visible pool. |
| Shared decisions | `common/decisions/006_independence_wave_shared_decisions.txt` | Static scan has 14 `ai_will_do` blocks; the adapter discovered two candidates, six required inputs, and no unresolved parser item, but no active-state candidates were available. |
| Main decisions | `common/decisions/006_independence_wave_decisions.txt` | Static scan has 77 `ai_will_do` blocks; the adapter discovered 13 candidates and 86 required inputs, with no available active candidates. |
| Package missions | `common/decisions/006_independence_wave_frontier_decisions.txt` and `common/decisions/006_independence_wave_siberian_decisions.txt` | Static scan has 23 and 88 `ai_will_do` blocks respectively. The frontier retry was blocked by the MCP transport outage before a discovery artifact could be produced. |
| Generic focus AI | `common/national_focus/006_independence_wave_focus.txt`; `independence_wave_focus_tree` | Static scan has 228 focus identifiers and 227 explicit `ai_will_do` blocks. No new focus probability run completed after the transport outage. |

Current local SHA-256 fingerprints at handoff time are:

| File | SHA-256 |
|---|---|
| `common/scripted_effects/006_independence_wave_effects.txt` | `3D91D28F4288B0D9F1CD864A918DEF89CC7AE24102632A2FC94C4523816ECDC3` |
| `common/scripted_effects/006_independence_wave_package_region_effects_registry.txt` | `2C309B2400D987B93C45159699A1A936FD4FECF7D3E883978E288E854A941728` |
| `common/scripted_effects/006_independence_wave_formable_registry_effects.txt` | `94490D9B158A36F7868F3EB600432461E033381EC4A223B0B293CA218A8B13B3` |
| `common/scripted_effects/006_independence_wave_scenario_effects.txt` | `130BCFCDA62A0C3C439936038E0EDC77038415A853A6EA9E96B600D24AE56067` |
| `common/scripted_effects/006_independence_wave_evolution_effects.txt` | `CC75B8B6BC4EB2BA834610C1A43E15D405ACF0289280A62263C1C5AADCDAC142` |
| `common/mtth/chaosx_mtth_variables.txt` | `91988D433884C49DC4E8D98F3F7CBF0E9ECAE218E3EC147539425466CCA4BA33` |
| `common/decisions/006_independence_wave_shared_decisions.txt` | `1F5787C3C2BB3A92E9C914CF1148270A0BD7E96556FF49DC7EC6C3A8BC8F682C` |
| `common/decisions/006_independence_wave_decisions.txt` | `A89058CE2499F6B8EA84398EF40198B00FCFEDF5B1C8F6238BA528636392FF68` |
| `common/decisions/006_independence_wave_frontier_decisions.txt` | `936F3F392A8F534DD8ED78456BAC8FD6308193BF8B2A2E53334585F0DBE9D336` |
| `common/decisions/006_independence_wave_siberian_decisions.txt` | `F52B3A783BCB9B445A0C53C419B60862D03FBD7BFB6A34485C328F9453E08A2E` |
| `common/national_focus/006_independence_wave_focus.txt` | `100332118BFBF8ED1688F01524D3FA3EB10A6CC20039F9D2A18387ADC88A21B4` |
| `events/006_independence_wave.txt` | `9C89405800DFAA484FECBE4E08DE108B5F8E028E1D2973FCBEAA3B3A8BCF5368` |
| `events/006_independence_wave_support_events.txt` | `F8DB738666DC14003DC3240DD027DA3DDD8EC3F67EE85465B9C8F580B4265021` |

## MCP discovery artifacts

The workspace id returned by the probability server was `mod_chaos_redux_ea3b2d67c2c0`.

| Adapter and source | MCP result | Revision, source hash, pool metadata, and artifact |
|---|---|---|
| `random_list`; `common/scripted_effects/006_independence_wave_effects.txt` | `PROBABILITY_SOURCE_INSPECTED` | Revision `751c90fd258459ae7474e69ed7449871f11bbfc407d88bb25b3c3347bac4560a`; source hash `c61c82d488128673852d6ec8b579b77b258899a3415cec967ec3a0b369c815dc`; 14 candidates, 14 required, 0 available, `poolComplete=true`, 0 unresolved. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e0369f2f9300cfc64c3917e00c944fad3f7217eaf031b25691635be7a6003761/5a41df8fddc9436141cd1d53e9be715ff3876d01900b421f694a76c3e4a77ae7/probability-inspect-c61c82d48812.json`. |
| `random_list`; `common/scripted_effects/006_independence_wave_package_region_effects_registry.txt` | `PROBABILITY_SOURCE_INSPECTED` | Revision `751c90fd258459ae7474e69ed7449871f11bbfc407d88bb25b3c3347bac4560a`; source hash `42743e6ccb4adb96ec3e3031e2f0057cd89fc11999d8efffa887795575d6b96b`; 126 candidates, 126 required, 0 available, `poolComplete=false`, 1 unresolved. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/dc9d08bcdebee3ee9ada00ca5639c6a125eaa95c62599b9a5e19695d17a13e96/6b305277c7880ec0d1f211b991a38c5e184223c242479fd20ae49c33e78f2661/probability-inspect-42743e6ccb4a.json`. |
| `event_option_ai_chance`; `events/006_independence_wave.txt` | `PROBABILITY_SOURCE_INSPECTED` | Revision `1050effb6582c018049f41e2df3bdb4b37ae1d4ef533235b6c08c3cb89eca811`; source hash `1257ea0e633018078f75a4b22931bd46666d1ed8e72d22f6708262b9ffe5d961`; 22 candidates, 13 required inputs, 0 available, `poolComplete=false`, 1 unresolved. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/332e243ecf641977e3825af6ab3e459e85d1309a70fabd1c488f94fe4c214e37/a66dcb0371cd8f8b82ed7c2bb912d51babfebd3bb98581fa96b1c3a56a7211db/probability-inspect-1257ea0e6330.json`. |
| `event_option_ai_chance`; `events/006_independence_wave_support_events.txt` | `PROBABILITY_SOURCE_INSPECTED` | Revision `53cc486e9ca4f5f5fc7869c71a2d69d57cf620295d6fe163047f90665095600a`; source hash `4d7ed5adb1d7c26803d1771ba98d4a3c9149fb2e2661d3ff0e770edbcf613437`; 154 candidates, 44 required inputs, 0 available, `poolComplete=false`, 1 unresolved. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5248ac98313030fd45d53b2f6ed7b6440c79822483caf2e501cb207134e8a26b/381bcd57a8ce3d1f1ce4b4e3e22a58fdb783b4c92cb16b337b5d9dd02113a294/probability-inspect-4d7ed5adb1d7.json`. |
| `decision_ai_will_do`; `common/decisions/006_independence_wave_shared_decisions.txt` | `PROBABILITY_SOURCE_INSPECTED` | Revision `ffb4453f573a540ac3f1a59632ccbb6d8ff9a0c017a96e5c7fdf6830e8b7ed7c`; source hash `527ab5a84e3b12986f9c175e6d479a1db1afa9382606a2cb87964e4d7b6ede5b`; 2 candidates, 6 required inputs, 0 available, `poolComplete=false`, 0 unresolved. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bfa1219401a9882c89ec6874c5ddc618509b21db125d101c83fb5013c479a0b0/6544118fb9100a1cc82a730ce970b6a0fe86723dea6edfc420bfe260aa43c40b/probability-inspect-527ab5a84e3b.json`. |
| `decision_ai_will_do`; `common/decisions/006_independence_wave_decisions.txt` | `PROBABILITY_SOURCE_INSPECTED` | Revision `8d74e26dcefa65fb24070fffc9d831ef9681b7e93411fd885ec6c9e9d86384b7`; source hash `136529687018fb7e43e2a9344675c916e030c4b367d4858565a236179c8fe686`; 13 candidates, 86 required inputs, 0 available, `poolComplete=false`, 0 unresolved. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/dfe2e96609b7e45fbc8c8e9ca86c3d280b61df84155d27466e7a78ed85660f9b/cd7e44014af2c267f6fb80c0c6de724a9ff13fff1da1b04203cd51edba87c6bf/probability-inspect-136529687018.json`. |
| `mission_ai_will_do`; `common/decisions/006_independence_wave_decisions.txt` | `PROBABILITY_SOURCE_INSPECTED` | Revision `fd5e4fb2e591da1836dcb5f680852fc07e41ea678320f57a94fe658a7ac2168c`; source hash `136529687018fb7e43e2a9344675c916e030c4b367d4858565a236179c8fe686`; 64 candidates, 50 required inputs, 0 available, `poolComplete=false`, 0 unresolved. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/abd3aeecea50cad0b2bdd1961a727693ac4ae3323a5a047bd62201c7c491c9fb/a0e8afc6ee52c3e0f48fc7e55d51587d642fd83920e1296ee5a1f13bb03ad7e0/probability-inspect-136529687018.json`. |

## Bounded evaluation and rendered evidence

`hoi4.probability_evaluate` ran for `random_list` on `common/scripted_effects/006_independence_wave_effects.txt` under `E006_ALLOCATOR_EMPTY_FIXTURE_2026_08_31` with the five named empty-fixture scenarios, one day, and `raw_value` plus `conditional_probability` metrics.

The result was `PROBABILITY_ANALYZED_PARTIAL`, analysis id `probability-c6d3d5048186aff0b92078fa`, source revision `751c90fd258459ae7474e69ed7449871f11bbfc407d88bb25b3c3347bac4560a`, source hash `c61c82d488128673852d6ec8b579b77b258899a3415cec967ec3a0b369c815dc`, scenario hash `86e494bc102fdde5e3cdb28bef7812a6b9e2fda36a10e8d7ba05707ba4ba0ca6`, five scenarios, 70 rows, 14 unresolved values, 0 diagnostics, and four visual resources.

The JSON artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c3d3216a959ff39aae12833a3855e6300b0f60ad57a8e359332562e3604a68bc/9b8eaa939dd9d43f6971c251c90df7e0d4f2da2cf330b6f193b4259cfa09a109/probability-c6d3d5048186aff0b92078fa.json`.

The returned ranking renders are `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/594233ff20e0e21f9a848274e08579d9961524ac88d1a21081496e618e226036/9f8daa4d52db4482afd8af98e1f847a268e841a836d0cf4f332ffd3aa8d60656/probability-probability-c6d3d5048186aff0b92078fa-ranking.svg` and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/dcea2d695d67ad79ee4cf26865b81489bcffc2a388d71c04d0acb9daf3a166d7/2b92f489c8654a4a276b3ca1c0c584fe7bd372688fb7e175385d7e7c1f82ed55/probability-probability-c6d3d5048186aff0b92078fa-ranking.png`.

The unresolved render is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b376452dd35a669b20b3ba5787e6af6347617460240eb4e6e0da2f2ae9a45962/52d57fba034933d9b2353b765ba43c89f517d50ecce15b7e14754a2f7c38d70b/probability-probability-c6d3d5048186aff0b92078fa-unresolved.svg`, with PNG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/443748d25cfe2d3c7c73f1357d1647f95e14a3a02a6d877b89d4c6a07af3fc50/4a435d458b8d2010ca5aaa67eb3fdc2572d66c39e8aac93c327432fd2e647dc6/probability-probability-c6d3d5048186aff0b92078fa-unresolved.png`.

The 14 unresolved rows are consistent with missing campaign fixture state, not evidence that the 14 outer region entries are syntactically invalid. Because all five states were empty, no normalized package or region selection probability is established.

## Adapter blocker

After the successful discovery artifacts and outer evaluation, the HOI4 MCP adapter became unavailable. The route reported `INTERNAL_ERROR`; the underlying tool response was `Transport closed`.

The exact blocked calls were a retry of `hoi4.probability_inspect` for `mission_ai_will_do` on `common/decisions/006_independence_wave_frontier_decisions.txt`, `hoi4.event_inspect` for `chaosx.nr6.1`, a regional allocator `hoi4.probability_evaluate`, and the requested allocator `hoi4.probability_sweep` for `wave_chaos_band`, `target_count`, and `capacity` with pairwise/rank-reversal output. No artifacts were returned for those calls.

Consequently, event structural inspection/rendering, new root/support option evaluations, decision/mission score traces, focus route evaluation, MTTH timing evaluation, sensitivity sweeps, rank-reversal checks, and post-change comparison remain unresolved for this run.

## Validity, balance, and exploit-risk findings

The outer allocator has an MCP-discovered complete 14-entry structural pool, but the empty fixtures expose zero available entries; the adapter therefore proves pool declaration only, not campaign eligibility or normalized selection.

The nested regional registry exposes 126 candidate entries with one unresolved adapter item, so the inner pool is incomplete for probability claims even before campaign gates are supplied.

The root and support event surfaces are `ai_chance` option surfaces, and their adapter candidate pools are incomplete; source constants and modifiers cannot be converted into exact option probabilities without visible-option, trigger, route, government, host-war, and external-factor state.

The decision and mission surfaces are willingness score races, not click probabilities. Their discovered candidates and required-input metadata are insufficient to rank active choices because availability, target validity, costs, cooldowns, route flags, host state, and AI strategy context are absent.

The formable Congress two-entry random list and its state-dependent risk modifiers are source evidence only. No success/failure probability is claimed.

The scenario registry is deterministic and should not be reported as a weighted selection pool. Its 138 rank writes require structural inspection for route validity, but no rank dominance or starvation conclusion is proven here.

The evolution MTTH source is bounded by explicit base/minimum/maximum constants and state modifiers, but no timing distribution or repetition rate is proven without active-incident, chaos-tier, active-country-count, and terminal-state fixtures.

Dominance, starvation, rank reversal, repetition, unsafe snowballing, and invalid-route positive weight remain unresolved. The source visibly contains prior package/region/host penalties, a minimum weight floor, an attempt cap, pool-exhaustion handling, and cleanup, but these safeguards were not engine-traced under typed scenarios in this run.

## Recommended follow-up fixes or checks (not applied)

Restore the HOI4 MCP probability and structural adapters, then rerun the exact named scenario sets above with typed campaign fixtures and the same source revisions.

For the allocator, provide the full 126-entry inner candidate manifest plus country/anchor/host existence and control, reservation groups, package attestation, prior package/region/host arrays, opening confidence, chaos band, target count, capacity, Event 005 collision state, and terminal/pool-exhaustion state.

For root/support events, provide complete visible-option pools and trigger state for route, government, war, host, target, and external modifier context before asserting any `ai_chance` probability.

For decisions/missions/focuses, provide complete active candidate pools, availability and bypass state, target validity, dynamic costs, cooldown/repetition state, route gates, and strategy factors; report score races separately from probabilities.

For MTTH, evaluate base, chaos-tier, thin-network, and dense-network fixtures with active incident state and terminal suppression, then sweep the named factors for timing drift and threshold reversals.

Run `hoi4.probability_compare` only after an owner-applied source patch or a clearly identified before/after revision, using the same scenario IDs, complete pool, and external-factor manifest.

## Skipped analyses and remaining uncertainty

`hoi4.probability_sweep` was attempted but blocked by `INTERNAL_ERROR`/`Transport closed`; no sensitivity or rank-reversal claim is available.

`hoi4.probability_compare` was not run because no owner-applied before/after patch exists in this read-only audit; a same-source comparison would not be a meaningful balance comparison.

`hoi4.probability_simulate` was skipped because no explicit uncertainty distributions, correlations, or seed were declared.

`hoi4.probability_sequence` was skipped because no complete custom-pool cadence, cooldown, recovery, cap, removal, reset, or terminal-state manifest was available.

No live HOI4 execution was performed. The audit is incomplete until the MCP transport is restored and the missing typed fixtures and complete pools are supplied.
