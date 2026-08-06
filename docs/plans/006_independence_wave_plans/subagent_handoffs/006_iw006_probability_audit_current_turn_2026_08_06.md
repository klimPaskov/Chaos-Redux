# Event 006 weighted-logic audit, current turn

Date: 2026-08-06

Mode: read-only probability handoff. No gameplay, AI, event, focus, decision, mission, strategy, localisation, asset, spreadsheet, or runtime file was changed.

## Current authority and verdict

The current runtime authority is `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md`: 23 content-attested selectable packages across 22 reservation groups, 170 unattested selectable rows, 32 central adapters, and nine adapter-only fail-closed adapters. The active ordinary super-event identifiers are 23 and 24. Historical 6001/6002 labels are not used here.

Verdict: **HOLD / PARTIAL** for weighted-AI and probability completion.

The latest after-MAC MCP run used workspace `mod_chaos_redux_ea3b2d67c2c0`, source revision `73416e4cb8b3533fd51442cce1a6da08044932e01a694e17bb1a372c4996d3b6`, and target commit `56e72be08a00cd3b84c1170734624717855288cd`. It proves source discovery, parser diagnostics, and several complete source-level `random_list` pools. Named evaluations used empty state records or incomplete runtime candidate pools. They are bounded score/eligibility evidence only, not exact click probabilities, live AI rates, MTTH timing distributions, dominance, starvation, rank reversals, repetition rates, or exploit-safety proofs.

## Inspect-first MCP evidence

The current evidence consolidates the inspect-first calls recorded in `006_event6_final_ai_probability_audit_2026_08_06_after_mac.md` and the current capacity receipt. Representative inspect artifacts are preserved below.

| Surface | Source and adapter | Inspect result | Evidence |
| --- | --- | --- | --- |
| Central allocator | `common/scripted_effects/006_independence_wave_package_allocator_effects.txt`, `random_list` | 14/14 candidates, 14 required inputs, `poolComplete=true`, 0 unresolved, source hash `bc6f7ff8598df33b610442e6ada24c28d7d82167fe135474deb18094b3b6cf83` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/08f50bac1050db701611403e27a03701966f02f8925fedefcc05329410b2c5c8/f1cd3d8b89abae49c00cf359846f8bdc0bcc0576525a192440acb7c40102fd61/probability-inspect-bc6f7ff8598d.json` |
| Region allocators | `common/scripted_effects/006_independence_wave_packages_region_01_effects.txt` through `_region_14_effects.txt`, `random_list` | Complete source pools: 9/9, 9/9, 8/8, 8/8, 12/12, 12/12, 5/5, 3/3, 7/7, 7/7, 5/5, 13/13, 19/19, 9/9. Region 03 includes IW-026 MAC and excludes IW-025. | Region 03 artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a9666c7277e29d0b7679d2e023983df6fc9d9e900024adfd850cef2d36df35da/b0d81feab2e6138ca1f9b11a21bb330bca6f743ab87fd7e43c5aaedb45863aba/probability-inspect-ff114c943bad.json` |
| Custom-pool probe | Central allocator and Region 04, `custom_weighted_pool` | 0 candidates and `poolComplete=false`. Current source is not exposed as a custom-pool surface by the installed adapter. | Exact result recorded in the final audit. Treating this source as a normalized custom pool is unsupported. |
| Shared decisions | `common/decisions/006_independence_wave_decisions.txt`, `decision_ai_will_do` | 10 decision candidates, 61 required inputs, 0 source diagnostics, `poolComplete=false`. | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b89cde389fbe5258215278312a740c9d59c96bf546cb7c255b5e949fb8d9272e/cc307c272b6c3dd1bec83caf0c1dc33632b7dfcff828b9454fdc4e1a0a5aca8c/probability-inspect-f84a0e082f6a.json` |
| Shared missions | Same source, `mission_ai_will_do` | 54 mission candidates, 38 required inputs, 0 source diagnostics, `poolComplete=false`. | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b6d072cfc356bdb7096c61d56741b8c4cb996969ae7ab73fca8abe3b342b1b80/948e3df8d8651f7f64baf60b5939df7ace35c5f64f5265089efed317138d5a6b/probability-inspect-f84a0e082f6a.json` |
| Generic focus AI | `common/national_focus/006_independence_wave_focus.txt`, `national_focus_ai_will_do` | 184 focus candidates, 15 required inputs, 0 source diagnostics, `poolComplete=false`. | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fb19d588a83287edb3746eda8e9aeeea659abe33c1ef2f22009c2ba86249d755/24573ee47ccf5123d0076bc1505101f96ec6b87e4daa4f273a1e6dd394ecf931/probability-inspect-cea5fad03a09.json` |
| SCN-008 controls | `common/decisions/006_independence_wave_scenario_decisions.txt`, `decision_ai_will_do` | 3 navigation decisions, 1 required input, `poolComplete=false`. These are deterministic previous/next controls, not a probability-proportional selection pool. | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/112f4b1e449388b0b457049e4f82e099da86f079a7d2d41370a54a831303f7b0/add964af81e64495a31d33c8cbfa952e9405ea62b424321a48414937b2df8d20/probability-inspect-fcd8a24fbe89.json` |
| Crisis mission | `common/decisions/006_independence_wave_crisis_decisions.txt`, `mission_ai_will_do` | 1 candidate, 7 required inputs, `poolComplete=false`. The decision adapter is unavailable because the file has no decision AI block. | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b01652711ed678f07435e0742b9ecc8c7e675be643fa56784cd05b37cc15850c/f61695a16175aaf98b7d6d2971609db498a37245f38194c1bfcf441451f6babf/probability-inspect-da54a4d80e28.json` |

## Named scenarios and result classification

All named evaluations below declared scenario IDs and hashes but supplied `state = {}`. Candidate completeness and external factors are therefore incomplete unless noted otherwise.

### Allocator and capacity

- `E6_ALLOCATOR_REQUIRED_SCENARIOS_CURRENT_MAC_2026_08_06`: `R03_MAC_OPEN`, `R04_ALL_OPEN`, `R04_KAR_BLOCKED`, `R04_CRI_BLOCKED`, `CAPACITY_20_WITNESS`. Analysis `probability-d5a09cc4bf4283756461eefa`, scenario hash `30697835b662c8c36f3a9c5e49c2649b2a50304b67c96528fe6dfeee44f4baea`, 5 scenarios, 70 rows, 14 unresolved, 0 diagnostics. Result is bounded/partial, not normalized probability.
- `E6_R03_ALLOCATOR_SCENARIOS_CURRENT_MAC_2026_08_06`: `MAC_OPEN`, `MAC_LIVING_FORMER_HOST`, `MAC_HOST_WAR`, `MAC_LOW_CAPACITY`. Analysis `probability-1058ddcf50884afda456b1ee`, 4 scenarios, 32 rows, 8 unresolved. The unresolved render is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e1d40f65380ad92e4f6c3d9b34b9af29cffe6f7e013ece98661e15f60b6d9ead/e1063142603681b65ec045bcbc13904a96e216b1964e655ee7d778e8da9c0565/probability-probability-1058ddcf50884afda456b1ee-unresolved.svg`.
- `E6_R04_ALLOCATOR_SCENARIOS_CURRENT_MAC_2026_08_06`: `R04_ALL_OPEN`, `R04_KAR_BLOCKED`, `R04_CRI_BLOCKED`, `R04_BOTH_OPEN_LOW_CAPACITY`, `CAPACITY_20_WITNESS`. Analysis `probability-1da57bc3ccc5291ae92003d2`, 5 scenarios, 40 rows, 8 unresolved. Ranking render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2b3e79e146e8c1ada7e5ca3a14f74f651637261be71e2419258e01740ea3f34f/4ec6451be9a0b10de22df99c2671e6159aaf91fbb0cc8cc48e8298d14b9bf495/probability-probability-1da57bc3ccc5291ae92003d2-ranking.svg`.
- The current capacity expansion set `E6_CAPACITY_EXPANSION_SCENARIOS_CURRENT_2026_08_06` covers `IW012_ICE_READY`, `IW026_MAC_YUG_READY`, `IW029_BOS_YUG_READY`, `IW070_ARM_EVENT5_SHARED`, `IW071_GEO_EVENT5_SHARED`, `IW072_AZR_EVENT5_SHARED`, `IW173_HAW_READY`, and `TARGET_REACHED_AND_HOST_RISK`. The custom-pool adapter returned zero candidates and `PROBABILITY_CANDIDATE_POOL_INCOMPLETE`, so no exact capacity probability is proven. The outer `random_list` set `E6_CAPACITY_EXPANSION_OUTER_SCENARIOS_CURRENT_2026_08_06` and its sweep over `chaos_band`, `target_count`, and `capacity` returned 70 rows with 14 unresolved. Analysis IDs were `probability-deb60a5c5afdf33dff80e189` and `probability-df2db183c71e54c4cd42114e`. The sweep is bounded sensitivity evidence only.

### Decisions, missions, and focus

- `E6_SHARED_DECISION_SCENARIOS_CURRENT_2026_08_06`: `E6_SHARED_OPEN_CALM`, `E6_SHARED_HOST_CRISIS`, `E6_SHARED_ROUTE_LOCKED`, `E6_SHARED_NO_VALID_TARGET`. Analysis `probability-9f13e191d036a7047654e3ec`, 40 rows, 1,990 unresolved, 8 diagnostics. Classification: bounded score-only.
- `E6_SHARED_MISSION_SCENARIOS_CURRENT_2026_08_06`: `E6_SHARED_MISSION_OPEN`, `E6_SHARED_MISSION_HOST_CRISIS`, `E6_SHARED_MISSION_ROUTE_LOCKED`, `E6_SHARED_MISSION_NO_VALID_TARGET`. Analysis `probability-8950045661d66cea9adf4cf6`, 216 rows, 486 unresolved, 20 diagnostics. Classification: bounded score-only.
- `E6_CRISIS_MISSION_SCENARIOS_CURRENT_2026_08_06`: `CRISIS_PRESSURE_OPEN`, `CRISIS_REQUESTER_LOST`, `CRISIS_RETRY_EXHAUSTED`, `CRISIS_NO_PRESSURE`. Analysis `probability-adfb7e57ec7ba9495504a95e`, 4 rows, 7 unresolved, 0 diagnostics. Classification: bounded score-only.
- `E6_FOCUS_SCENARIOS_CURRENT_2026_08_06`: `FOCUS_OPEN_CALM`, `FOCUS_HOST_CRISIS`, `FOCUS_ROUTE_LOCKED`, `FOCUS_NO_VALID_ROUTE`. Analysis `probability-a409c793623379895e9836f0`, 736 rows, 1,033 unresolved, 226 diagnostics, incomplete 184-focus pool. Classification: bounded score-only. Structural `hoi4.focus_inspect` separately resolves 184 focuses and 193 connectors with no Event 006 crossings or node intersections. Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2b4c6222e5fb6bbad277c6a60917cf7f25bb483880abf67abf9805d1ebf7fbcf/8d127eada28690038ee5c796cef7acb803beadf4ce18340ac97e8d018435b73a/focus-inspect.546c98db483766b3.json`; render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/99315e3b89510ee95475cdcaa004b6120834db4ffe96f9ca9e101b1bae25ff3e/404ca2cba18bab163a954d97be67d1b697b9db76e3387814fcbb74cadbf1566d/independence_wave_focus_tree.focus.svg`.

### Event options, MTTH, and evolution timing

`ai_chance` source inspection/evaluation remained partial for `events/006_independence_wave.txt`, `events/006_independence_wave_evolution_incidents.txt`, `events/006_independence_wave_form01_02_04.txt`, `events/006_independence_wave_form05.txt`, `events/006_independence_wave_iw043_iw058.txt`, `events/006_independence_wave_iw093_iw098.txt`, `events/006_independence_wave_mediterranean.txt`, `events/006_independence_wave_rhineland_bavaria.txt`, and `events/006_independence_wave_wallonia_frisia.txt`. Representative analyses were root `probability-b1341db7e86f8447c22c5434`, evolution `probability-774a9f1a4ecd36f126814267`, form01/02/04 `probability-8a6c039b53b99bb3fd1e031d`, form05 `probability-e6999b95b1dde63a4fdce591`, and IW043/IW058 `probability-ac629d6245a32753bfc68a8f`. Pools were incomplete and state records empty, so no option click probability is claimed.

The `event_mean_time_to_happen` adapter returned `PROBABILITY_SURFACE_EMPTY` with exact blocker `No weighted blocks matched this request` for `common/mtth/006_independence_wave_evolution_mtth.txt` and `common/scripted_effects/006_independence_wave_evolution_effects.txt`. Evolution timing is unresolved. No MTTH timing distribution, sweep, or sequence result is available.

SCN-008 source `common/scripted_effects/006_independence_wave_scenario_effects.txt` returned the same `PROBABILITY_SURFACE_EMPTY` blocker for both `direct_random` and `random_list`. The source-driven matrix remains eight player-facing modes by four intensities, 32 cells. This is deterministic navigation, not probability-proportional sampling.

## Current package-specific surfaces

| Package | Weighted source surface | Current MCP/evidence status | Safe conclusion |
| --- | --- | --- | --- |
| IW-013 NAV | `common/ai_strategy/006_independence_wave_iberian.txt`; `common/decisions/006_independence_wave_iberian_decisions.txt` | Source-level additive strategy and decision/mission weights exist. The package remains adapter-only and central execution fail-closed. No package-specific typed MCP pool is complete. | No NAV AI ranking, timing, or package probability claim. |
| IW-015 GLC | Same Iberian strategy/decision files | Same as NAV. GLC remains adapter-only and central execution fail-closed. | No GLC AI ranking, timing, or package probability claim. |
| IW-030 MNT | `common/ai_strategy/006_independence_wave_montenegro.txt`; `common/decisions/006_independence_wave_montenegro_decisions.txt` | Source repair preserved gates, but MNT remains adapter-only and fail-closed for typed AI, release, host, cleanup, and runtime evidence. No package-specific complete MCP pool. | No MNT AI ranking, timing, or package probability claim. |
| IW-014 CAT | `common/ai_strategy/006_independence_wave_catalonia.txt`; `common/decisions/006_independence_wave_catalonia_decisions.txt` | CAT is admitted as a standalone vanilla carrier. Its package-specific decisions use shared AI constants, but no complete typed MCP package scenario is recorded. FORM-07 remains fail-closed separately. | Source admission does not prove CAT AI balance or click probability. |
| IW-026 MAC | `common/ai_strategy/006_independence_wave_macedonia.txt`; `common/decisions/006_independence_wave_macedonia_decisions.txt` | Decision inspect 1 candidate/10 inputs, mission inspect 11/13, both incomplete. `ai_strategy_factor` exact blocker `PROBABILITY_SURFACE_EMPTY`. `E6_MAC_DECISION_SCENARIOS_CURRENT_2026_08_06` analysis `probability-50e16d24fb12038cf17559db`; `E6_MAC_MISSION_SCENARIOS_CURRENT_2026_08_06` analysis `probability-910da7cbe88f2d4a9f74d4c1`; empty-state diagnostics include never-eligible route actions. | Bounded source/eligibility evidence only. No quantitative MAC AI claim. |
| IW-029 BOS | `common/ai_strategy/006_independence_wave_bosnia.txt`; `common/decisions/006_independence_wave_bosnia_decisions.txt` | Package is admitted, but `ai_strategy_factor` returns `PROBABILITY_SURFACE_EMPTY` for the Bosnia strategy source. | No quantitative BOS AI claim. |
| IW-033 KAR / IW-041 CRI | `common/ai_strategy/006_independence_wave_karelia_crimea.txt`; `common/decisions/006_independence_wave_karelia_crimea_decisions.txt` | Inspect 2 decision candidates/12 inputs and 20 mission candidates/14 inputs, pools incomplete. Strategy adapter exact blocker `PROBABILITY_SURFACE_EMPTY`. Existing same-path compare returned `comparisonChanges=0` only as capability evidence. | No KAR/CRI ranking, dominance, starvation, or before/after claim. |

For NAV, GLC, MNT, CAT, MAC, BOS, KAR, and CRI, package admission or source presence is not probability evidence. The central authority continues to fail closed wherever the source-of-truth map says the package is adapter-only or lacks independent identity/runtime proof.

## Compare, sweep, simulation, sequence, and renders

- `hoi4.probability_compare` same-path current/current probes on MAC and KAR/CRI returned `comparisonChanges=0`. This is a capability receipt, not a before/after result. The route rejects `revision`, cached `analysisId`, artifact/source-hash references, and hash-qualified source paths with `PROBABILITY_SOURCE_NOT_FOUND`.
- A bounded allocator sweep exists for `E6_CAPACITY_EXPANSION_OUTER_SCENARIOS_CURRENT_2026_08_06`, but unresolved candidate rows remain. It does not establish a threshold or rank-reversal claim.
- No `probability_simulate` run was valid because no uncertain input distribution and seed were declared.
- No `probability_sequence` run was valid because the custom transaction lacks a complete declared cadence, cooldown, recovery, cap, removal/reset, timer, and terminal-state manifest.
- Ranking, matrix, sensitivity, and unresolved views were rendered where useful. Rendered artifacts are listed above and in the current final audit handoff. Structural event evidence is separate and partial. No whole-event completion claim follows.

## Findings and owner recommendations

1. Keep the weighted-AI gate at HOLD/PARTIAL. Do not convert score traces into click probabilities. In HOI4, `ai_will_do` is a score race, while event `ai_chance` is proportional sampling over the complete visible option pool.
2. Add a typed MCP-supported fixture or custom-pool manifest for all 23 attested transaction candidates, including package readiness, host and anchor reservations, Event 005 collision state, temporary-array mutation, transaction order, prior selection, and target-capacity state. Re-run `E6_ALLOCATOR_REQUIRED_SCENARIOS_CURRENT_MAC_2026_08_06` and the capacity sets with complete state.
3. Add an MCP-recognizable strategy projection or explicit state bridge for `common/ai_strategy/006_independence_wave_generic.txt`, `common/ai_strategy/006_independence_wave_karelia_crimea.txt`, `common/ai_strategy/006_independence_wave_macedonia.txt`, and `common/ai_strategy/006_independence_wave_bosnia.txt`. Do not tune numeric factors before the adapter exposes them.
4. Populate the shared, package, focus, event, and SCN-008 scenario records with route flags, package identity, targets, ledgers, costs, cooldowns, war state, host/former-host state, and external strategy factors. Empty state records cannot prove eligibility, starvation, or dominance.
5. Preserve a pre-patch source path before future AI changes. The installed compare route cannot consume cached analysis IDs or a `revision` field, so a true before/after comparison is otherwise blocked.
6. Keep NAV/GLC/MNT and the other adapter-only packages fail closed. Do not add a generic package fallback to obtain a larger probability pool.

## Skipped analyses, blockers, and uncertainty

- Event evolution MTTH and scenario random adapters: exact blocker `PROBABILITY_SURFACE_EMPTY` / `No weighted blocks matched this request`.
- Generic, MAC, BOS, and KAR/CRI `ai_strategy_factor`: exact blocker `PROBABILITY_SURFACE_EMPTY` / `No weighted blocks matched this request`.
- Crisis decision adapter: no decision AI block in the source. Crisis mission adapter is the only supported surface.
- Custom-pool central allocator: 0 candidates and `poolComplete=false`; source-level random-list evidence remains separate.
- No exact normalized package probability, option probability, focus-click probability, timing distribution, rank reversal, dominance, starvation, repetition, exploit, live-runtime, save/load, or whole-event completion claim is supported.

No gameplay files were changed by this audit.
