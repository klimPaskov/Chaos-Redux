# Event 006 current weighted-logic audit — 2026-08-13

Status: **PARTIAL / UNRESOLVED.** This is a read-only probability handoff for the current Event 006 source boundary. No gameplay files were changed, no weights were patched, and no commit was made.

## Authority and scope

The audit used the current authority files `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md` and `docs/plans/006_independence_wave_plans/006_independence_wave_resume_packet.md`. Their compile-time boundary is 31 content-attested selectable packages, 28 compatible reservation groups, 162 unattested selectable rows out of 193 non-overlay rows, and 39 runtime package adapters. The active automatic ladder is 3/4/5/7/10 and World Collapse also targets 10. The current deterministic Join order is `IW-001, IW-002, IW-004, IW-006, IW-007, IW-008, IW-009, IW-010, IW-012, IW-014, IW-017, IW-018, IW-019, IW-023, IW-024, IW-026, IW-027, IW-028, IW-029, IW-030, IW-031, IW-038, IW-040, IW-044, IW-033, IW-041, IW-070, IW-071, IW-072, IW-173, IW-184`.

The weighted scope covered the core Event 006 event-option AI chance and evolution MTTH surfaces, the allocator random-list/direct-random/custom-pool surfaces, shared decisions and missions, admitted package decisions/missions for IW-038 Ruthenia, IW-040 Kuban, and IW-044 Tatarstan, the shared focus AI race, generic and package AI strategy factors, scenario decision surfaces, and Join event/effect surfaces.

## Required references consulted

I read `AGENTS.md`, `.agents/skills/chaos-redux-subagents/SKILL.md`, `.agents/skills/chaos-redux-events/SKILL.md`, `.agents/skills/chaos-redux-mtth/SKILL.md`, `.agents/skills/chaos-redux-focus-trees/SKILL.md`, and `.agents/skills/chaos-redux-decisions-missions/SKILL.md` before analysis.

I consulted the offline wiki pages `Data structures`, `Triggers`, `Effects`, `Modifiers`, `Localisation`, `Scopes`, `On actions`, `Event modding`, `Decision modding`, `Idea modding`, `AI modding`, and `National focus modding` under `paradox_wiki/`. I also read the vanilla documentation `script_concept_documentation.md`, `script_collection_input.md`, `script_collection_operator.md`, and the relevant `effects_documentation.md` and `triggers_documentation.md` sections under `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/`.

The reference semantics used here are that Event `ai_chance` is proportional-to-weight sampling, MTTH is daily timing after trigger validity, decisions and missions use willingness scores rather than normalized click probabilities, focus `ai_will_do` is a highest-score race over the complete available focus pool, `random_list` is weight-proportional effect selection, and `direct_random` is a percentage chance rather than a candidate race.

## MCP evidence

Every surface listed below was first sent through `hoi4.probability_inspect` or, where the installed transport failed, the inspect attempt and exact failure are recorded. The workspace supplied to successful calls was `mod_chaos_redux_ea3b2d67c2c0`.

### Core Event 006 event-option AI chance

Source: `events/006_independence_wave.txt`.

`hoi4.probability_inspect` returned `PROBABILITY_SOURCE_INSPECTED` with source revision `e27639e1cb1241b3a8ad25ac9316191768991d19b0df72de287fee7fa3cf402c`, source hash `b97c0de3de07618f183b5ffde387a2776b65735ad75a48e7f7c88a71783791e3`, 20 discovered candidates, 0 available candidates, `poolComplete=false`, 13 required inputs, and 1 unresolved item. Inspect JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ebf6bff0e3403d6f2f586014cf2126a1ed52e88573098538c6a78b6391a1a989/a99789fe32cde798d4b4a63ccadc6a3ab12bb43017f6af6d223142d01f936d6b/probability-inspect-b97c0de3de07.json`.

Named scenario set: `E6_CORE_EMPTY_CURRENT_2026_08_13`, containing `CORE_EMPTY` with an intentionally empty state fixture. This is a source-discovery and adapter-capability scenario, not a complete campaign fixture; host, carrier, package identity, route, ledger, resource, capital, war, and event-target factors were not silently assumed.

`hoi4.probability_evaluate` returned `PROBABILITY_ANALYZED_PARTIAL` with analysis ID `probability-7b8d41ba0b9d22d0b3b5fd32`, source revision/hash matching the inspect, scenario hash `8034753966613b5e97c825478b2c5fec4c55145c2b9f86bcb4d75975aa2cd7b3`, 1 scenario, 20 candidates, 23 unresolved items, and 2 diagnostics. JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/277ec09ca12decbfeee6223d6c102ed73f92207141baafcb3ddedd9d69244efd/ea11d7f445cde9fb863bbbd96878c59c6ae2b52e13ce72f8e6942de7e69c4ecf/probability-7b8d41ba0b9d22d0b3b5fd32.json`. Ranking SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0484067f7b31ab2047e51caeba6f78ab9c546d434f1ed6e63d2a950b65048610/3fa09041f2233a3c66fa6540ec47b72520c6dc82a0175d95113bbc2f70998d7e/probability-probability-7b8d41ba0b9d22d0b3b5fd32-ranking.svg`. Ranking PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ba1d093c60cebb7eba419ae18e9d2c45f33135df114d8b9e43cdc23f911755db/366cfe30ed67f6da142818daf0f2834c2ea48821d6c0d6ebfc8ee192a4f9e371/probability-probability-7b8d41ba0b9d22d0b3b5fd32-ranking.png`. Unresolved SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7ad5d073b237292581809720b08d0393bb941f1674bf62a21e34f7190bb9daa9/2f03c234b7da7542c1d53edaac322ca2a1be709598a4da7a55343132837ae9db/probability-probability-7b8d41ba0b9d22d0b3b5fd32-unresolved.svg`. Unresolved PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8a345d31c42fc5435252b3cd26e9c916a386f6887f556fb78119236141464201/b44ec6cad9cb05138dba547f2fbb59f3170a053bec945ec44fdf68309b6a5b47/probability-probability-7b8d41ba0b9d22d0b3b5fd32-unresolved.png`.

The two diagnostics were `PROBABILITY_CANDIDATE_POOL_INCOMPLETE` with normalized probabilities withheld and `PROBABILITY_MODIFIER_UNSATISFIED_IN_SCENARIOS` for `chaosx.nr6.301.a`'s `constant:independence_wave_decision_ai.modifier_major` factor, inactive in the empty fixture. Classification is **bounded/score-only and unresolved for normalized option probability**. The source has 11 `ai_chance` blocks by static scan, but this call does not prove which options are available or their campaign probabilities.

An explicit `hoi4.probability_render` retry was not possible after the transport failure below. The evaluate response itself contains the ranking and unresolved rendered resources above; no additional current render claim is made.

### Automatic package allocator

Source: `common/scripted_effects/006_independence_wave_package_allocator_effects.txt`.

`random_list` inspect returned `PROBABILITY_SOURCE_INSPECTED`, source revision `e27639e1cb1241b3a8ad25ac9316191768991d19b0df72de287fee7fa3cf402c`, source hash `bc6f7ff8598df33b610442e6ada24c28d7d82167fe135474deb18094b3b6cf83`, 14 candidates, `poolComplete=true`, 0 available candidates, 14 required inputs, and 0 unresolved items. Inspect JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/67f51637c58748a683f37bcb6a7246318c44d909bda907fe2a914215ecdc39e2/5d0f8ae36933aafc0a421e2f23431f94187d5c7eaca5dccbcf1d4eaa69db2b55/probability-inspect-bc6f7ff8598d.json`.

The 14 entries are the region-level random-list draw at source lines 57–72, weighted by the recomputed `independence_wave_region_01_total_weight` through `independence_wave_region_14_total_weight` variables. The static allocator contract prepares each region, sums all 14 weights, draws only while the total is greater than zero, and marks the pool exhausted otherwise. It then loops until the selected count reaches the target or the attempt cap is reached, and fails closed if exact-count or metadata-array alignment checks fail.

`direct_random` inspect returned `PROBABILITY_SOURCE_DISCOVERED` with the same source revision/hash, `requested_adapter_empty`, 0 direct-random candidates, 14 available `random_list` candidates, and suggested adapter `random_list`. Inspect JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2fc19e1fa638dc1b6d64f69ac01f26a0bdfb18c7fd60d8c0944e20166a05eb0b/8902bf23a7102a0689eb3c1986ce322b0fe6ea3556e1517e07407e5acec84721/probability-inspect-bc6f7ff8598d.json`.

`custom_weighted_pool` inspect returned `PROBABILITY_SOURCE_INSPECTED` with the same source revision/hash, 0 candidates, `poolComplete=false`, and no unresolved items. Inspect JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9c4bb4bdc2dda0e04e5d7e2ff2af92dc4a247bbc68a4840a3ef9bf8f3b397943/59505a5b9671fd0dd72de0d0505ab38da71b6068c52eeee17aac10a245c34bfc/probability-inspect-bc6f7ff8598d.json`.

No current allocator `probability_evaluate`, `probability_sweep`, `probability_render`, `probability_sequence`, or `probability_simulate` result was obtained because the MCP transport closed immediately after the inspect pass. Therefore no exact region or package probability, normalized ranking, rank reversal, dominance, starvation, repetition rate, cadence distribution, or terminal-state proof is claimed. The inspect's `poolComplete=true` means only that the 14 source-level region entries were found; it does not establish that the runtime package candidates inside those regions are complete or available under the 31/28/39 authority boundary.

### Evolution MTTH

Sources: `common/mtth/006_independence_wave_evolution_mtth.txt` and `common/scripted_effects/006_independence_wave_evolution_effects.txt`.

`event_mean_time_to_happen` inspect on the MTTH file returned `PROBABILITY_SOURCE_DISCOVERED`, discovery reason `no_weighted_surfaces`, source revision `e27639e1cb1241b3a8ad25ac9316191768991d19b0df72de287fee7fa3cf402c`, source hash `8632297cf059164892a537ff3a987cddd0406c020e98234331014d42b4b8f8a2`, 0 candidates, 0 required inputs, and 0 unresolved items. Inspect JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/74b46ca4503138a17c94c38ecb55ee0a2ed8895523550f6fa5a1703012ca9c19/4e9cf623dfc2b88f5daf50fe0d42700b761e3658f9ce27f824930793de7e3f31/probability-inspect-8632297cf059.json`.

The matching effects-file inspect also returned `no_weighted_surfaces`, source hash `4632b46c85507e33aebecedde8c423cdffa88506f790698b71f9396369a1a617`, 0 candidates, and 0 unresolved items. Inspect JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/acf15d3e8abf3c10eedd5831854ba3cf37f038e611d752a6b26dc25ad09ad81d/052c7384f73769690300cc1d5be57627038eb6dd299ede9436a3f44629f1de85/probability-inspect-4632b46c8550.json`.

The named scenario set reserved for a follow-up was `E6_EVOLUTION_MTTH_EMPTY_CURRENT_2026_08_13` with `EVOLUTION_EMPTY` and an empty state. Its evaluate call returned the exact transport blocker `tool call failed for hoi4_agent_tools/hoi4.probability_evaluate: Transport closed`, so no MTTH timing, effective days, median, or cumulative chance is proven. Classification is **unresolved adapter surface** rather than zero timing.

## Surfaces blocked by the MCP transport

After the successful core and allocator calls, a concurrent inspect batch caused the installed `hoi4-agent-tools` transport to close. Sequential retries returned the same exact `Transport closed` error for probability and structural tools. The following inspect-first attempts were made and are unresolved for this current revision:

| Surface | Current source | Required adapter | Inspect result | Static/source context |
|---|---|---|---|---|
| Shared decisions | `common/decisions/006_independence_wave_decisions.txt` | `decision_ai_will_do` | Initial inspect succeeded before the outage: 10 candidates, 0 available, `poolComplete=false`, 79 required inputs, 0 unresolved; current evaluate/sweep/render unavailable after outage | 64 `ai_will_do` blocks; bases include urgent/high/standard and war/route/capacity/severe-host modifiers |
| Shared missions | `common/decisions/006_independence_wave_decisions.txt` | `mission_ai_will_do` | Inspect retry returned exact `Transport closed` | 37 `days_remove` entries in this shared file; founding deadline is passive (`available = { always = no }`) where specified and must not be treated as AI starvation without a typed fixture |
| IW-038 Ruthenia decisions/missions | `common/decisions/006_independence_wave_ruthenia_decisions.txt` | `decision_ai_will_do`, `mission_ai_will_do` | Inspect attempt returned exact `Transport closed` | 11 `ai_will_do` blocks and 10 timed project entries; package gates include setup, capital control, active-project exclusion, ledgers, resources, former-host, and route government |
| IW-040 Kuban decisions/missions | `common/decisions/006_independence_wave_kuban_decisions.txt` | `decision_ai_will_do`, `mission_ai_will_do` | Inspect attempt returned exact `Transport closed` | 11 `ai_will_do` blocks and 10 timed project entries; package gates include setup, capital control, active-project exclusion, ledgers, resources, former-host, and route government |
| IW-044 Tatarstan decisions/missions | `common/decisions/006_independence_wave_tatarstan_decisions.txt` | `decision_ai_will_do`, `mission_ai_will_do` | Inspect attempt returned exact `Transport closed` | 11 `ai_will_do` blocks and 10 timed project entries; package gates include setup, capital control, active-project exclusion, ledgers, resources, former-host, and route government |
| Shared focus race | `common/national_focus/006_independence_wave_focus.txt` | `national_focus_ai_will_do` | Inspect attempt and retry returned exact `Transport closed` | 207 `ai_will_do` blocks by static scan; the focus is a score race, not a normalized probability. Full available pool, prerequisites, bypasses, mutual exclusions, and package hooks remain required inputs |
| Generic strategy | `common/ai_strategy/006_independence_wave_generic.txt` | `ai_strategy_factor` | Inspect attempt returned exact `Transport closed` | Three gated profiles with additive values for army, infantry, support, artillery, industry, infrastructure, defense, trains, and war restraint |
| IW-038 strategy | `common/ai_strategy/006_independence_wave_ruthenia.txt` | `ai_strategy_factor` | Inspect attempt returned exact `Transport closed` | Four gated layers; source values include army 86, infantry 40, support 50, artillery 24, infrastructure 70, defense 82, emergency army 118, and founding/settled restraint −260/−430 |
| IW-040 strategy | `common/ai_strategy/006_independence_wave_kuban.txt` | `ai_strategy_factor` | Inspect attempt returned exact `Transport closed` | Four gated layers with the same current numeric ladder as RUT and KUB-specific trigger identities |
| IW-044 strategy | `common/ai_strategy/006_independence_wave_tatarstan.txt` | `ai_strategy_factor` | Inspect attempt returned exact `Transport closed` | Four gated layers with the same current numeric ladder as RUT/KUB and TAT-specific trigger identities |
| Scenario decisions | `common/decisions/006_independence_wave_scenario_decisions.txt` | `decision_ai_will_do` | Inspect attempt returned exact `Transport closed` | Three AI-will-do blocks; scenario mode/phase, setup, package identity, and ledger gates must be typed before numeric claims |
| Join event options | `events/006_independence_wave_join.txt` | `event_option_ai_chance` | Inspect attempt returned exact `Transport closed` | Source-level Join disposition is deterministic first-success, not a weighted package draw; the current event-option candidate pool remains unverified in this pass |
| Join effects | `common/scripted_effects/006_independence_wave_join_effects.txt` | `random_list`, `custom_weighted_pool`, `direct_random` | Inspect attempts returned exact `Transport closed` | Source review finds no weighted selector; retry queue `chaosx.nr6.40` and `independence_wave_join_retry_pending` are single-flight timing state, not weighted choices |

The first shared-decision inspect receipt above is current evidence from this run. The other rows are unresolved because a successful current inspect was not emitted after the transport outage; historical handoffs must not be substituted for current proof.

## Scenario and candidate-pool discipline

The only named current evaluate scenario completed here is `E6_CORE_EMPTY_CURRENT_2026_08_13 / CORE_EMPTY`, with an explicitly empty state fixture and scenario hash `8034753966613b5e97c825478b2c5fec4c55145c2b9f86bcb4d75975aa2cd7b3`. Its candidate pool was not complete because the adapter reported 20 discovered candidates but 0 available candidates and 13 required inputs. No external factor was inferred.

The allocator inspect proves 14 source-level region candidates but 0 runtime-available rows and 14 required inputs. The current 31 admitted IDs, reservation collisions, package attestation, anchor ownership/control, host survival, target count, wave phase, prior-wave state, temporary arrays, retry/attempt cap, and cleanup terminal state therefore remain incomplete for any exact allocator scenario.

The decision, mission, focus, strategy, scenario, and Join surfaces have no current typed scenario hash or current analysis artifact after the transport outage. Historical scenario sets and artifacts in older handoffs remain dated capability evidence and are not re-labelled as current.

## Findings

1. The core event-option adapter recognizes 20 source options but cannot establish the complete available pool or resolve 13 required inputs, so no exact accept/decline or branch probability is valid. The observed `chaosx.nr6.301.a` major modifier is not active under the empty fixture; this is a fixture-coverage finding, not a dead-option proof.
2. The allocator's outer `random_list` is structurally complete at the 14-region source-entry level, while runtime availability is empty and inner package candidates are not exposed by the adapter. No region or package dominance, starvation, rank reversal, repetition, or wave-ladder timing conclusion is valid.
3. `direct_random` and `custom_weighted_pool` are not the active allocator adapters for the current source. The former redirects to `random_list`; the latter discovers no surface. This is an exact adapter-capability result, not proof that scripted temporary-array selection is absent from runtime.
4. Evolution MTTH files are not recognized as weighted surfaces by the installed adapter. Their timing remains unresolved rather than zero or constant.
5. Decisions, missions, and focuses must be reported as score races or eligibility results, not normalized click probabilities. Their complete available pools and external gates remain unproven for current shared and admitted-package fixtures.
6. Static source shows the same numeric strategy ladder for RUT, KUB, and TAT (86 army, 40 infantry, 50 support, 24 artillery, 70 infrastructure, 82 defense, 118 emergency army, and −260/−430 founding/settled restraint), but the `ai_strategy_factor` adapter outage prevents any claim about effective overlap, activation, dominance, or war-avoidance behavior.
7. Join currently uses deterministic first-success package disposition plus a single-flight retry marker and hidden retry event. No weighted Join package probability is claimed; the current event-option adapter proof is blocked.
8. No safe conclusion about starvation, dominance, repeated package selection, unsafe snowball, or exploit risk can be made for the 31/28/39 runtime boundary from this partial MCP pass.

## Recommended next weighted tranche (not applied)

1. Repair or restart the HOI4 MCP transport and rerun `hoi4.probability_inspect` sequentially for every unresolved adapter before any new evaluate or sweep call.
2. Build one typed scenario matrix covering `E6_SHARED_DECISION_EMERGENCY`, `E6_SHARED_DECISION_PROVISIONAL`, `E6_RUT_PROJECT_READY`, `E6_KUB_PROJECT_READY`, `E6_TAT_PROJECT_READY`, `E6_FOCUS_ROUTE_RACE`, `E6_SCENARIO_MODE`, and `E6_JOIN_RETRY`. Each scenario must declare phase, package identity/setup, capital ownership/control, route/government flags, ledgers, resource and civilian-factory affordability, active project and cooldown state, former-host existence/war, severe-host-threat state, event-target/temporary-array state, network/League state, and target validity.
3. For the allocator, provide the complete 31-ID admitted pool plus the 14 region-entry pool and the current reservation-group/host/collision state, then evaluate the active ladder points 3/4/5/7/10 and World Collapse 10. Use `probability_sweep` only with declared numeric paths such as target count, capacity, chaos band, or attempt cap; retain any range-required blocker.
4. Re-run `probability_render` for ranking, matrix, timing, sensitivity, and unresolved views after each successful analysis and preserve the returned URIs and scenario hashes.
5. Do not run `probability_compare` until an owner-applied source revision and a valid pre-change baseline are explicitly identified. Same-source comparisons are capability receipts only.
6. Keep the shared focus surface separate from package-specific focus hooks; a focus race claim requires the complete route-aware available focus pool, not the 207 source block count.

## Skipped analyses and exact blockers

- Shared mission, focus, generic strategy, RUT/KUB/TAT strategy, scenario decision, Join event, and Join effect inspections were attempted after the first successful pass and returned the exact MCP error `tool call failed for hoi4_agent_tools/hoi4.probability_inspect: Transport closed`.
- Evolution MTTH evaluate returned the exact MCP error `tool call failed for hoi4_agent_tools/hoi4.probability_evaluate: Transport closed` after a successful no-surface inspect.
- Allocator evaluate, sweep, render, simulation, and sequence were skipped after inspect because the same transport outage made their receipts unavailable; no hand-calculated substitutes were used.
- No `probability_sweep` result is claimed because no current numeric scenario ranges survived the transport outage.
- No `probability_simulate` result is claimed because no uncertain-input distributions and seed were declared.
- No `probability_sequence` result is claimed because the adapter did not receive a complete custom-pool manifest with cadence, cooldown/recovery, removal/reset, cap, timer, and terminal states.
- No `probability_compare` result was run because no identifiable before/after source revision exists for this current audit.
- Required structural Event/Focus MCP inspection and rendering for unresolved surfaces were not completed after the same exact `Transport closed` failure; source-only review is not presented as structural engine evidence.

No simplification or gameplay fallback was applied. This handoff is intentionally incomplete until the required MCP adapters and typed scenario fixtures become available.
