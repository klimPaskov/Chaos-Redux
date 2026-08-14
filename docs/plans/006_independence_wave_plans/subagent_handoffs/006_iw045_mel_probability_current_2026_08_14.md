# Event 006 IW-045 BSK and IW-047 MEL probability audit

Date: 2026-08-14

Status: **PARTIAL / FAIL-CLOSED for quantitative balance**. This is a read-only current-source audit after IW-045 Bashkiria central admission and the current IW-047 Mari El package-local tranches. No gameplay, AI, central registry, Join, asset, workbook, or runtime files were changed.

## Scope and current admission boundary

Audited weighted surfaces:

- IW-045 Bashkiria (`BSK`) mission and decision scores in `common/decisions/006_independence_wave_bashkiria_decisions.txt`.
- IW-045 `ai_strategy_factor` source in `common/ai_strategy/006_independence_wave_bashkiria.txt`.
- IW-047 Mari El (`MEL`) mission and decision scores in `common/decisions/006_independence_wave_mari_decisions.txt`.
- IW-047 `ai_strategy_factor` source in `common/ai_strategy/006_independence_wave_mari.txt`.
- Event 006 core event-option `ai_chance` in `events/006_independence_wave.txt` as the shared event context.
- Event 006 outer allocator `random_list` in `common/scripted_effects/006_independence_wave_package_allocator_effects.txt` as the shared package-selection context.
- Event 006 evolution incident options in `events/006_independence_wave_evolution_incidents.txt` and evolution MTTH definitions in `common/mtth/006_independence_wave_evolution_mtth.txt`.

Current source-of-truth evidence says IW-045 is centrally content-attested and admitted to deterministic Join after IW-044. `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt` contains the IW-045 adapter, attestation, normal preflight, and SCN-008 preflight branches. `common/scripted_effects/006_independence_wave_join_effects.txt:240` probes IW-045 after IW-044 and before IW-033. IW-047 remains package-local. Its package effects, decisions, focus hooks, and AI file exist, but the current dispatch adapter, content-attestation branch, scenario preflight, and Join probe have no IW-047 branch. The current authority therefore remains BSK admitted and MEL fail-closed.

## Required references

I read `AGENTS.md`, `.agents/skills/chaos-redux-subagents/SKILL.md`, `.agents/skills/chaos-redux-events/SKILL.md`, and `.agents/skills/chaos-redux-mtth/SKILL.md`. I consulted the offline wiki pages `Data structures`, `Triggers`, `Effects`, `Modifiers`, `Localisation`, `Scopes`, `On actions`, `Event modding`, `Decision modding`, `Idea modding`, and `AI modding` under `paradox_wiki/`. I also read the installed vanilla documentation `script_concept_documentation.md`, `effects_documentation.md`, `triggers_documentation.md`, and `modifiers_documentation.md`.

The semantic distinction used here is that decision and mission `ai_will_do` values are willingness scores, focus values are score races, event `ai_chance` and `random_list` are proportional sampling surfaces, and MTTH is a timing distribution. None of the BSK or MEL decision score values below is a click probability.

## MCP workspace and source revisions

Workspace: `mod_chaos_redux_ea3b2d67c2c0`.

All current inspections reported source revision `7cb6cc94900a8e7b2b757e673eb8d540e862282fd47c0c7c5679a4f55d3f571f` for this worktree snapshot.

| Surface | Adapter | Source hash | Inspect result | Artifact |
|---|---|---|---|---|
| BSK decisions and mission | `mission_ai_will_do` | `b7b031d727e03702aabc0decda0612f29957d2a01bfcb3565b1e30f06be54844` | `PROBABILITY_SOURCE_INSPECTED`, 11 candidates, pool incomplete, 15 required inputs, zero available under empty fixture | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/40d576077c7b00e5072d9e2a5a39092392922d9de8121bae2c13499077fb62b4/40cface296626f5dde67154477b5348bf71ccc9ff2e72a3bdc8a6050f2f9936d/probability-inspect-b7b031d727e0.json` |
| BSK decisions requested as `decision_ai_will_do` | `decision_ai_will_do` | same source hash | `PROBABILITY_SOURCE_DISCOVERED`, requested adapter empty, suggested adapter `mission_ai_will_do`, 11 matching candidates | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f01be22b3f7ea976dfc9d76aeec4c6cedc6c7cd46ce38dd935b9eeae5cc30942/8e41bd1e45b3e4b934661f7c85f097424b60b80dde438078b836915b004e47b5/probability-inspect-b7b031d727e0.json` |
| BSK strategy | `ai_strategy_factor` | `38b83abe93f18b1a122521e57bbab27885bd648caca37949a755c8c26ac745fc` | `PROBABILITY_SOURCE_DISCOVERED`, `no_weighted_surfaces`, zero candidates | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8da348e678d7faeb86448b4d91f12e4bb090c23385d9a8d7bd209260049bc15f/6169118b5cc63678b4d0e794bacf4e55a93dcb0da57a0a27a6b2f81fe8dc49b2/probability-inspect-38b83abe93f1.json` |
| MEL decisions and mission | `mission_ai_will_do` | `fe28dbeb18d645410397c80926c8d4d620d3072d856ba0b6749bf03b1c9b7fe5` | `PROBABILITY_SOURCE_INSPECTED`, 11 candidates, pool incomplete, 15 required inputs, zero available under empty fixture | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/dcc7011f56631ded95c26903524fd953801f735c7993e5180a4059edb8f2a1f6/bd0acee350837904a9f890592aa889e40a55db826fe481bc4a1f67c4484f15dc/probability-inspect-fe28dbeb18d6.json` |
| MEL strategy | `ai_strategy_factor` | `1ebebf8cc5f53ba2f3fa1e8a615f5c6413557179b9baafe4f8b7ec63fb5392bd` | `PROBABILITY_SOURCE_DISCOVERED`, `no_weighted_surfaces`, zero candidates | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7f1d5b2fbad586fb6886bcb6e40473dac76a7070db9127a909f2b081662fc40f/a4a2d8d6a1297ace2223e738e5e84e295844291af321f3fed3469fb24e3fda62/probability-inspect-1ebebf8cc5f5.json` |
| Core Event 006 event options | `event_option_ai_chance` | `d0e57da75a6e98b333e6b95dea7db084e18778909656f1a66724801ad6889482` | `PROBABILITY_SOURCE_INSPECTED`, 20 candidates, pool incomplete, 13 required inputs, one unresolved | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0caac458826d51c13b7e2fbe0b82cc82c78762ca439ceb4e5c326906883e5edf/d8f336620aae6e00b8af30d5d24472b2a40e853c8629fd9b57a82fc1f9555cd9/probability-inspect-d0e57da75a6e.json` |
| Outer package allocator | `random_list` | `bc6f7ff8598df33b610442e6ada24c28d7d82167fe135474deb18094b3b6cf83` | `PROBABILITY_SOURCE_INSPECTED`, 14 region candidates, source-entry pool complete, 14 required inputs, zero unresolved | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/104ab7ddb9ba91e09f7c61721365d6a29d0977dced0f09971beb63f93e81ae9e/1a336afd4e2574b7a7bf6f19b0692256af5eefe72cf3dff5a123b67032e9c7e4/probability-inspect-bc6f7ff8598d.json` |
| Allocator requested as `direct_random` | `direct_random` | same allocator hash | `PROBABILITY_SOURCE_DISCOVERED`, requested adapter empty, suggested adapter `random_list`, 14 matching entries | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/163435dadb1e873ea73490e79f947da96743c0020dbc65aac195a391bafdcdfe/78e1c81b9cf99a9383448f80a5ae7385823d46494d7b1fa78969e36d43e39390/probability-inspect-bc6f7ff8598d.json` |
| Allocator requested as `custom_weighted_pool` | `custom_weighted_pool` | same allocator hash | `PROBABILITY_SOURCE_INSPECTED`, zero candidates, pool incomplete | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e18e72950642e480b75bab1efddc2f65550178ed59b42f15ade6e8e10f59e58a/e447db122d82cbc12ed8c4c628123c2936f9c09bf7b7b42554917d694c55d322/probability-inspect-bc6f7ff8598d.json` |
| Evolution MTTH file | `event_mean_time_to_happen` | `8632297cf059164892a537ff3a987cddd0406c020e98234331014d42b4b8f8a2` | `PROBABILITY_SOURCE_DISCOVERED`, `no_weighted_surfaces`, zero candidates | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e10733202eca0715ec2d500e3fbade8b44acce1b92d26e58fefc893a29570cee/70e8e5a4a0de25bda41411efa9a37f10b4bfa4064be21194c0a8c8f507dd0d8f/probability-inspect-8632297cf059.json` |
| Evolution incident options | `event_option_ai_chance` | `b455e753546a59f103f8aa3a1b8d3525160cf9d8aad13552a1e81a7e54b55826` | `PROBABILITY_SOURCE_INSPECTED`, 10 candidates, pool incomplete, one unresolved | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8e27b72adbec49ca6843b403fb00cd20900d51002622f69b63d31879da1aa45c/50258b235575c67bebc315467770158e3b0db93025a28ab21cb8636f3f154615/probability-inspect-b455e753546a.json` |

## BSK and MEL score surfaces

Both package decision files expose the same 11-candidate shape. Candidate-pool completeness is source-level complete for the named 11 IDs, but runtime availability is incomplete because the adapter requires 15 campaign inputs and the submitted typed state could not be represented. The candidate IDs supplied to evaluation were:

- BSK: `independence_wave_bsk_hold_frontier_congress`, `independence_wave_bsk_secure_frontier_depots`, `independence_wave_bsk_integrate_frontier_guards`, `independence_wave_bsk_register_bashkir_communities`, `independence_wave_bsk_settle_former_host_ledgers`, `independence_wave_bsk_ratify_constitutional_autonomy`, `independence_wave_bsk_adopt_agrarian_compact`, `independence_wave_bsk_convene_socialist_councils`, `independence_wave_bsk_establish_frontier_emergency_command`, `independence_wave_bsk_codify_durable_sovereignty`, and `independence_wave_bsk_open_ural_network_corridor`.
- MEL: `independence_wave_mel_hold_forest_congress`, `independence_wave_mel_secure_forest_depots`, `independence_wave_mel_integrate_woodland_guards`, `independence_wave_mel_register_mari_communities`, `independence_wave_mel_settle_former_host_ledgers`, `independence_wave_mel_ratify_constitutional_autonomy`, `independence_wave_mel_adopt_forest_land_compact`, `independence_wave_mel_convene_woodland_councils`, `independence_wave_mel_establish_forest_emergency_command`, `independence_wave_mel_codify_durable_sovereignty`, and `independence_wave_mel_open_volga_finnic_corridor`.

Shared AI score constants are in `common/script_constants/006_independence_wave_decision_constants.txt:264-278`: blocked `0`, very low `2`, low `5`, standard `10`, high `25`, urgent `100`, double modifier `2`, major modifier `5`.

Static source score traces, classified as **exact source facts and score-only**, are:

| Package | Candidate class | Base | Conditional modifier |
|---|---|---:|---|
| BSK | founding mission | urgent `100` | `available = always = no`, so it is a passive timed mission and not a click race |
| BSK | ordinary security, administration, route projects | high `25` or standard `10` | integrate guards and emergency command multiply by `2` while `has_war = yes`; former-host settlement multiplies by `2` when no severe host threat |
| BSK | emergency route | urgent `100` | wartime multiplier `2` |
| BSK | settled compact, sovereignty, network | high `25` or standard `10` | gated by route, settlement, compact, network, League, capital-control, active-project, and cost triggers |
| MEL | founding mission | urgent `100` | `available = always = no`, so it is a passive timed mission and not a click race |
| MEL | ordinary security, administration, route projects | high `25` or standard `10` | integrate guards and emergency command multiply by `2` while `has_war = yes`; former-host settlement multiplies by `2` when no severe host threat |
| MEL | emergency route | urgent `100` | wartime multiplier `2` |
| MEL | settled compact, sovereignty, network | high `25` or standard `10` | gated by route, settlement, compact, network, League, capital-control, active-project, force-generation, and cost triggers |

The source values do not normalize across the 11 entries and do not establish a selection probability. The founding mission's passive `always = no` availability is not evidence of starvation.

## Named evaluations

### BSK missions and projects

Scenario set: `IW045_BSK_MISSION_CURRENT_2026_08_14`, with `BSK_FOUNDING`, `BSK_READY_PEACE`, `BSK_READY_WAR`, `BSK_HOST_LOSS`, `BSK_ROUTE_LOCKS`, and `BSK_NETWORK_READY`. Each scenario explicitly supplied `state = {}` because the adapter rejected typed package fixtures. Horizon was 600 days and metric was `raw_value`.

`hoi4.probability_evaluate` returned `PROBABILITY_ANALYZED_PARTIAL`, analysis ID `probability-bd0247702958c4f8880311b3`, scenario hash `829438909cc6991fc280c688ed51f267ab482d8ff7f2cf8f9808c2681fa8dc6e`, 66 candidate-scenario rows, 136 unresolved items, and 11 diagnostics. JSON artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/137ee4723ddc792ad83f9585ca03cddaf179fe823b7341b58639bdc9f1336998/8e1364db5ac2fcea1c4e87e20e40e095a8319900910a40ffc9a096b907749e7e/probability-bd0247702958c4f8880311b3/probability-bd0247702958c4f8880311b3.json`.

The analyzer marked all 11 BSK candidates never eligible across the intentionally empty fixtures. This is a fixture limitation, not a gameplay reachability result. Unresolved inputs include package and setup identity, state 651 ownership/control, capital control, former-host existence and war, both compact ledgers, route flags, active project and cooldown state, resource and factory affordability, founding settlement, crisis resolution, network membership, and cleanup state.

Rendered evidence from `hoi4.probability_render` using the same analysis and scenario hash:

- ranking: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7ae245af12ad663858f06ff6db90338b8a760fcc1061112e15b1e3b33c7137e6/0962a85202688ebc77b96dd04b46c7631143f8626d11f3ee5250a2eac56554bb/probability-probability-bd0247702958c4f8880311b3-ranking.svg`
- matrix: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ed5568bb13cf548e6c380f12d71c3b6bf4bec35986d2f8579ca25174d3bccffc/f2a318d2682d806588fbb77369d72b1f68c5d5c3c932b1f98ea44f92a95c64a2/probability-probability-bd0247702958c4f8880311b3-matrix.svg`
- unresolved: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/eea5c3d7edcd6904b351d760bf1bb01734b90b0971f3115fcb737d547b374c08/ce4f46d60a535b805089c8340b1321c4115d290d8c8210e831008bf7161ddc2c/probability-probability-bd0247702958c4f8880311b3-unresolved.svg`

### MEL missions and projects

Scenario set: `IW047_MEL_MISSION_CURRENT_2026_08_14`, with `MEL_FOUNDING`, `MEL_READY_PEACE`, `MEL_READY_WAR`, `MEL_HOST_LOSS`, `MEL_ROUTE_LOCKS`, and `MEL_NETWORK_READY`. Each scenario explicitly supplied `state = {}` because the adapter rejected typed package fixtures. Horizon was 600 days and metric was `raw_value`.

`hoi4.probability_evaluate` returned `PROBABILITY_ANALYZED_PARTIAL`, analysis ID `probability-23ee9ef12d977ee90b83ebe4`, scenario hash `1bb0305e9f454a499b56323411d62984c7943a1c8613303fdbcc937957cffb0f`, 66 candidate-scenario rows, 136 unresolved items, and 11 diagnostics. JSON artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ca88c762b0d371b844b67fb9820a5d1c82e1b25e548bddde90bde0691c89737b/373216f965e475537232cd276cfebdb81c39296de8c78339e033cca25cd3109b/probability-23ee9ef12d977ee90b83ebe4.json`.

The analyzer marked all 11 MEL candidates never eligible across the intentionally empty fixtures. This is a fixture limitation, not a gameplay reachability result. MEL adds the package force-generation gate to project cancellation and availability. Unresolved inputs otherwise match BSK, with MEL package identity, state 833 anchor, current-generation force proof, former-host relation, forest ledgers, route flags, network, and cleanup state also required.

Rendered evidence from `hoi4.probability_render` using the same analysis and scenario hash:

- ranking: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/869b9472bc17515ab6c8f1a2b67f2a1efda7a5bcd023f9c5876826cab01a3f7e/398c95221cf98fdf50cdb32738e2b76b47710a477c8a4c5f9ee29b984f08177a/probability-probability-23ee9ef12d977ee90b83ebe4-ranking.svg`
- matrix: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8e4053708e549d3c50145aec155837989edc6b2b43cf20255cc2b1499676eef8/a173618d9eec1debbc73a1ced64b2ad7600e93805ebc8f691673a2f81ae2eec3/probability-probability-23ee9ef12d977ee90b83ebe4-matrix.svg`
- unresolved: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/721119d4183e3c4fb898cc078c8bf4aacfb5822c3a79a42749c9640bc0d90074/dfb217f056882c1ef4e33b6579f1010b7880737b00aeab40bdcbe50da62c8034/probability-probability-23ee9ef12d977ee90b83ebe4-unresolved.svg`

### Strategy factors

Both BSK and MEL strategy inspections returned `no_weighted_surfaces` with zero candidates. Named empty-state evaluations were run as `IW045_BSK_STRATEGY_EMPTY_CURRENT_2026_08_14 / BSK_STRATEGY_EMPTY` and `IW047_MEL_STRATEGY_EMPTY_CURRENT_2026_08_14 / MEL_STRATEGY_EMPTY`. Both returned the exact blocker `PROBABILITY_SURFACE_EMPTY: No weighted blocks matched this request` for adapter `ai_strategy_factor`. No analysis ID, scenario hash, ranking, or rendered strategy artifact exists.

Static strategy values remain source-only:

- BSK frontier survival: army `90`, infantry production `42`, artillery production `24`, support production `48`, infrastructure `78`, bunker `86`.
- BSK founding restraint: `avoid_starting_wars = -260` while a living former host exists and its ledger is unsettled.
- BSK settled frontier: army `90`, infrastructure `78`, `avoid_starting_wars = -430` after compact stabilization.
- BSK emergency guard: army `120`, bunker `86` under emergency government.
- MEL forest survival: army `74`, infantry production `34`, artillery production `18`, support production `52`, infrastructure `66`, bunker `78`.
- MEL founding restraint: `avoid_starting_wars = -245` while a living former host exists and its ledger is unsettled.
- MEL settled compact: army `74`, infrastructure `66`, `avoid_starting_wars = -405` after compact stabilization.
- MEL emergency guard: army `108`, bunker `78` under forest emergency government.

These values are additive strategy factors and are not normalized probabilities. The adapter limitation prevents any claim about overlap, effective accumulation, dominance, starvation, repetition, rank reversal, or war-restraint behavior.

## Shared Event 006 probability context

The core event-option inspect found 20 candidates with an incomplete available pool, 13 required inputs, and one unresolved input. No current exact branch probability is valid. The outer allocator inspect found all 14 region-level `random_list` entries and marked that source-entry pool complete, but runtime candidate availability and package-level pool completeness remain unresolved. `direct_random` redirected to `random_list`, and `custom_weighted_pool` found no surface. The evolution MTTH file returned `no_weighted_surfaces`. The ten evolution incident options were discovered but their pool was incomplete with one unresolved input.

The event structural pass used `hoi4.event_inspect` with selector `chaosx.nr6.350`, state-flow mode, revision `d21fdfa2723e4a624054076fb1104ba638c4fbb1f733358a99b24aac1839ace2`, and graph hash `4223118f94e6920016241a8b9cd25da3e9dd5fd0103899eb9fd36238159df415`. It returned `EVENT_INSPECTED_PARTIAL`, zero blocking diagnostics, 2,127 deferred workspace diagnostics, and 8,266 unresolved nodes. The corresponding `hoi4.event_render` state artifacts are revision-matched and partial. State render JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a7855865d0925a13f37006af8746fe0c161f12f87d2232fb158bb6d75834835f/425d783cef74ba6addc346b342d81d7c57aaed2acb4f26f04aa233dddbb64b5b/event-state-d21fdfa2723e.json`. SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b221ba88360f39b5b3485aae88637d83299d88a520372905c772acdff23fe5d6/df44452f6d5328cb6529fac1a6ac34e9bd43f757d13dcb61852c6a3493673451/event-state-d21fdfa2723e.svg`.

## Sweep and compare status

I attempted `hoi4.probability_sweep` for both BSK and MEL mission pools using the six named scenarios, complete 11-ID pools, `state.has_war`, `state.has_independence_wave_severe_host_threat`, three steps, pairwise sensitivity, and rank-reversal search. Both calls returned the exact blocker `PROBABILITY_SWEEP_RANGE_REQUIRED`: every sweep path needs a scenario range, numeric alternatives, or numeric state value, with the first blocker at `BSK_FOUNDING / state.has_war` and `MEL_FOUNDING / state.has_war`. No sensitivity, threshold, rank-reversal, or sweep artifact exists.

`hoi4.probability_compare` was not run. There is no owner-applied before/after source revision in this tranche, and a same-source comparison would only be a capability receipt rather than a balance comparison. `probability_simulate` was not run because no uncertain-input distributions or seed were declared. `probability_sequence` was not run because neither package is a declared custom weighted pool with cadence, cooldown/recovery, removals, resets, caps, timers, and terminal states.

## Findings and risk classification

1. **Exact source structure, unresolved runtime probability.** BSK has central adapter, attestation, preflight, and deterministic Join presence. MEL has package-local score and strategy sources but no central execution admission. This is source and registry evidence, not a probability claim.
2. **Score-only.** BSK and MEL project values are 10, 25, or 100 with declared war and host-threat factors. They are willingness scores. They cannot be converted to click probabilities without the complete available decision or mission pool and external factors.
3. **Fixture-blocked.** Both package evaluations supplied an explicit empty state. All 11 candidates were reported never eligible in both sets. Those diagnostics must not be interpreted as dead content.
4. **Adapter-blocked strategy.** The `ai_strategy_factor` adapter exposes zero candidates for both strategy files. It does not prove that the authored `ai_strategy` entries are ignored by the game.
5. **No dominance or starvation proof.** There is no valid candidate ranking across complete typed BSK or MEL states. Dominance, starvation, repetition, rank reversal, unsafe snowball, and exploit risk remain unresolved.
6. **Shared event remains incomplete.** The core event-option pool, allocator runtime candidate pool, evolution timing, and evolution incident availability remain incomplete or adapter-unresolved. The current whole-event probability boundary therefore remains HOLD / PARTIAL even though BSK is centrally admitted.

## Recommended owner fixes, not applied

1. Preserve BSK's current central admission and Join order. Do not claim quantitative AI acceptance from the partial BSK evidence.
2. Keep MEL fail-closed until its route-flag and portrait gates, central adapter and attestation, normal/scenario preflight, and deterministic Join entry are independently complete.
3. Extend or repair the MCP `ai_strategy_factor` adapter so package strategy layers and their activation gates are exposed. Until then, do not tune the BSK or MEL strategy constants from these receipts.
4. Supply typed fixtures for BSK and MEL at minimum for setup, ready peace, ready war, living former host with unsettled ledgers, host-loss fallback, each route government, compact stabilization, network readiness, state/capital ownership, resource affordability, active-project exclusion, generation/origin guards, and cleanup.
5. Re-run the same six scenario IDs with complete external factors. Then run `probability_sweep` on declared numeric alternatives for war and severe-host-threat gates, target/capacity values where relevant, and route-state thresholds. Preserve scenario hashes and rendered ranking, matrix, sensitivity, threshold, and unresolved artifacts.
6. After an owner-applied source change, run `probability_compare` against a real pre-change source with the same complete scenario IDs. Do not treat same-source comparisons as balance proof.

## Skipped analyses and blockers

- No exact or bounded BSK/MEL runtime selection probability is proven because both mission evaluations had 136 unresolved rows and incomplete campaign fixtures.
- No BSK/MEL strategy-factor ranking is proven because `ai_strategy_factor` returned `no_weighted_surfaces` and evaluation returned `PROBABILITY_SURFACE_EMPTY`.
- Both probability sweeps were blocked by `PROBABILITY_SWEEP_RANGE_REQUIRED` because boolean state paths had no declared numeric alternatives or ranges.
- No compare was run because no owner patch and valid before revision were supplied.
- No simulation or sequence analysis was run because their declared input contracts were not met.
- Structural Event MCP evidence is partial with deferred workspace-wide helper/lifecycle projections. No live HOI4 session or save/load run was performed.

No simplification or fallback was applied.
