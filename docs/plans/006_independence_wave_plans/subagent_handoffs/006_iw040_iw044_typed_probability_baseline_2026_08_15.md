# IW-040 KUB / IW-044 TAT typed probability baseline handoff

Audit date: 2026-08-15.

## Disposition

This is a read-only evidence tranche for already-admitted IW-040 KUB and IW-044 TAT. No gameplay, AI, decision, trigger, central-admission, Join, localisation, or runtime file was edited. The typed-fixture route remains unresolved. The receipts below prove source discovery, adapter behavior, and fixture rejection only; they do not prove campaign ranking, dominance, starvation, repetition, timing, normalized selection probability, or balance.

## Read-only references

I read the repository `AGENTS.md`, `chaos-redux-subagents/SKILL.md`, `chaos-redux-decisions-missions/SKILL.md`, the admitted-package addendum `docs/plans/006_independence_wave_plans/006_admitted_package_ai_evidence_tranche_addendum_2026_08_13.md`, the current KUB/TAT probability handoffs, all required offline wiki core pages (Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, and AI modding), and every markdown file under `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/`.

## Audited source surfaces

| Surface | Current source files and identifiers |
| --- | --- |
| KUB mission AI | `common/decisions/006_independence_wave_kuban_decisions.txt`; category `independence_wave_kub_mounted_compact_category`; eleven mission IDs in the KUB pool below |
| TAT mission AI | `common/decisions/006_independence_wave_tatarstan_decisions.txt`; category `independence_wave_tat_river_compact_category`; eleven mission IDs in the TAT pool below |
| KUB package gates | `common/scripted_triggers/006_independence_wave_kuban_package_triggers.txt`; shared costs and decision gates in `common/scripted_triggers/006_independence_wave_decision_triggers.txt` |
| TAT package gates | `common/scripted_triggers/006_independence_wave_tatarstan_package_triggers.txt`; shared costs and decision gates in `common/scripted_triggers/006_independence_wave_decision_triggers.txt` |
| Shared score constants | `common/script_constants/006_independence_wave_decision_constants.txt` |

The worktree contains concurrent modifications to the decision and package-trigger files. This handoff does not attribute those edits to this audit and does not overwrite or stage them.

## Candidate pools

The KUB pool supplied to the adapter was complete relative to the eleven mission definitions discovered by source inspection:

`independence_wave_kub_hold_mounted_compact_together`, `independence_wave_kub_secure_mounted_depots`, `independence_wave_kub_integrate_border_guards`, `independence_wave_kub_register_community_compacts`, `independence_wave_kub_settle_former_host_ledgers`, `independence_wave_kub_ratify_constitutional_autonomy`, `independence_wave_kub_adopt_agrarian_compact`, `independence_wave_kub_convene_socialist_councils`, `independence_wave_kub_establish_mounted_emergency_command`, `independence_wave_kub_codify_durable_sovereignty`, `independence_wave_kub_open_black_sea_steppe_network_corridor`.

The TAT pool supplied to the adapter was complete relative to the eleven mission definitions discovered by source inspection:

`independence_wave_tat_hold_river_compact_together`, `independence_wave_tat_secure_river_depots`, `independence_wave_tat_integrate_border_guards`, `independence_wave_tat_register_community_compacts`, `independence_wave_tat_settle_former_host_ledgers`, `independence_wave_tat_ratify_constitutional_autonomy`, `independence_wave_tat_adopt_agrarian_compact`, `independence_wave_tat_convene_socialist_councils`, `independence_wave_tat_establish_river_emergency_command`, `independence_wave_tat_codify_durable_sovereignty`, `independence_wave_tat_open_volga_river_network_corridor`.

This source-relative completeness is not runtime-available-pool completeness. The adapter reported zero available candidates until a scenario can satisfy the country, scope, variables, flags, project, cost, and target gates.

## Fresh `hoi4.probability_inspect` receipts

The mandatory first calls used adapter `mission_ai_will_do`, `refresh = true`, and the corresponding decision source. Workspace: `mod_chaos_redux_ea3b2d67c2c0`.

| Source | Result | Source revision | Source hash | Adapter result | Artifact |
| --- | --- | --- | --- | --- | --- |
| KUB | `PROBABILITY_SOURCE_INSPECTED` | `92952da17137a1b57721cd2592ecf62322318d69a2a49b4b5203ca00a8333a1e` | `87ba7c79b4c87b980b378f0a6c08cd27051363bea3b9b44eaec4a7ee49a4f25c` | 11 candidates, 15 required inputs, 0 available, `poolComplete=false`, 0 unresolved inspect items | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/998c34794d73f6ec2c0219172a14b9b6597beb3b2402fc97e4d2ecac50ff5ab3/05ad36c4beef42ee185da9995746ed989fe9bcaec12bd1e5e44d4f51c1ffc33a/probability-inspect-87ba7c79b4c8.json` (artifact SHA `998c34794d73f6ec2c0219172a14b9b6597beb3b2402fc97e4d2ecac50ff5ab3`)
| TAT | `PROBABILITY_SOURCE_INSPECTED` | `92952da17137a1b57721cd2592ecf62322318d69a2a49b4b5203ca00a8333a1e` | `2e84e8d3ea2432956071806401bea769ed0d2b53e4cd64e9d738138ade3c1dae` | 11 candidates, 15 required inputs, 0 available, `poolComplete=false`, 0 unresolved inspect items | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b35e5c2377a4a2b6a383896bd124c5cf5d8390027f41ac27c8dfd8ba049afba7/8ce289527d1027153415d5af7be08096befcdc04a5688740080e5be4d5f0da7a/probability-inspect-2e84e8d3ea24.json` (artifact SHA `b35e5c2377a4a2b6a383896bd124c5cf5d8390027f41ac27c8dfd8ba049afba7`)

The adapter declares `selectionRule = score_only`, `rawScore = true`, `normalizedProbability = false`, `sequence = false`, and `timeDistribution = false`. It explicitly says not to invent a categorical denominator for mission `ai_will_do` scores. The declared required inputs are `capital_scope`, `check_variable`, `command_power`, `exists`, `has_army_experience`, `has_decision`, `has_equipment`, `has_manpower`, `has_stability`, `has_variable`, `has_war`, `has_war_support`, `num_of_civilian_factories_available_for_projects`, `original_tag`, and `var:independence_wave_former_host`.

An explicit eleven-entry candidate override was also inspected. TAT returned `poolComplete=true` with the same zero available candidates and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bb6bcc230d6ac59577d8f6fc7d9c0bb42a227cb10b66fe34bc69d02b79ccc6a7/9d30b82901062d4ca29941427a85568d8e422af004da5b81a0d2e44a2e6335ef/probability-inspect-2e84e8d3ea24.json`. The analogous KUB override returned the exact `INTERNAL_ERROR` / `Unexpected internal error` with no artifact. This is an adapter receipt, not a source conclusion.

## Named scenario contract and completeness

The addendum names these ten scenarios: `KUB_FRAGILE_PEACE`, `KUB_SEVERE_HOST_WAR`, `KUB_STABLE_ROUTE_LOCK`, `KUB_NETWORK_READY`, `TAT_FRAGILE_PEACE`, `TAT_SEVERE_HOST_WAR`, `TAT_STABLE_ROUTE_LOCK`, `TAT_NETWORK_READY`, `BOTH_RESOURCE_STARVED`, and `BOTH_IMPOSSIBLE_AMBITION`.

The required external factors are package identity and setup, anchor/state ownership and control (KUB state 234; TAT state 249), capital scope, phase/crisis flags, both package ledgers, active-project and completion flags, route availability and matching government, cost and reserve affordability, `has_war` and severe former-host threat, former-host existence/war relation, founding settlement, Network and League state, and formable/member validity where applicable. None of these factors was inferred from scenario prose.

| Scenario | MCP submission | Candidate pool | External factors | Classification |
| --- | --- | --- | --- | --- |
| `KUB_FRAGILE_PEACE` | Submitted once as `state = {}` and once as primitive schema probe | Source-relative 11/11; runtime availability 0 | Incomplete; no actor/target/compound fixture | Partial, unresolved; no live claim |
| `KUB_SEVERE_HOST_WAR` | Not submitted after fixture rejection | 11/11 source-relative only | Incomplete | Unresolved |
| `KUB_STABLE_ROUTE_LOCK` | Not submitted after fixture rejection | 11/11 source-relative only | Incomplete | Unresolved |
| `KUB_NETWORK_READY` | Not submitted after fixture rejection | 11/11 source-relative only | Incomplete | Unresolved |
| `TAT_FRAGILE_PEACE` | Submitted once as `state = {}` | Source-relative 11/11; runtime availability 0 | Incomplete; no actor/target/compound fixture | Partial, unresolved; no live claim |
| `TAT_SEVERE_HOST_WAR` | Not submitted after fixture rejection | 11/11 source-relative only | Incomplete | Unresolved |
| `TAT_STABLE_ROUTE_LOCK` | Not submitted after fixture rejection | 11/11 source-relative only | Incomplete | Unresolved |
| `TAT_NETWORK_READY` | Not submitted after fixture rejection | 11/11 source-relative only | Incomplete | Unresolved |
| `BOTH_RESOURCE_STARVED` | Not submitted after fixture rejection | 11/11 source-relative only for each package | Incomplete; reserve floor and complete shared pool absent | Unresolved |
| `BOTH_IMPOSSIBLE_AMBITION` | Not submitted after fixture rejection | 11/11 source-relative only for each package | Incomplete; member/formable target state absent | Unresolved |

The four non-empty package states per side and both cross-package states remain named contracts, not executed live-state results.

## Typed-fixture attempts and exact limits

1. The accepted empty shape was `scenarioSet = { id, scenarios: [{ id, state: {} }] }`. It is syntactically valid but declares no actor, scope, variable, flag, target, or resource state.
2. A nested-object fixture attempt was rejected before analysis with the exact MCP validation error: `MCP error -32602: Input validation error: Invalid arguments for tool hoi4.probability_evaluate: Invalid input at scenarioSet.scenarios[0].state.has_equipment; Invalid input at scenarioSet.scenarios[0].state.has_variable; Invalid input at scenarioSet.scenarios[0].state.check_variable; Invalid input at scenarioSet.scenarios[0].state.capital_scope; Invalid input at scenarioSet.scenarios[0].state.var:independence_wave_former_host; Invalid input at scenarioSet.scenarios[0].state.flags`.
3. A primitive-only probe was accepted syntactically with direct values for `original_tag`, `exists`, `has_war`, command power, manpower, stability, war support, army experience, civilian factories, `has_equipment`, `has_decision`, `has_variable`, `capital_scope`, `check_variable`, former-host variable, and package variables/flags. The resulting artifact still reports unresolved actor/compound/numeric trigger inputs. In particular, the trace includes `Scenario does not declare actor for original_tag`, `Scoped or compound trigger capital_scope is not declared by the scenario`, `Scoped or compound trigger has_equipment is not declared by the scenario`, `Scoped or compound trigger var:independence_wave_former_host is not declared by the scenario`, `check_variable requires declared var and value`, and `Trigger command_power cannot compare the declared scenario value`. Therefore primitive JSON acceptance is not typed campaign-fixture support.
4. No actor/target schema was invented after this exact boundary. The owner or tool provider must supply the documented adapter fixture shape for country actor scope, capital/anchor scope, former-host target, flags, variables, active decisions, and numeric comparison values.

## Evaluation receipts

### KUB empty named baseline

`hoi4.probability_evaluate` used the full 11-ID pool, scenario set `IW040_TYPED_BASELINE_2026_08_15`, scenario `KUB_FRAGILE_PEACE`, `state = {}`, raw-value metric, and a 600-day horizon. Result: `PROBABILITY_ANALYZED_PARTIAL`, analysis ID `probability-412fd7a39a6e3b136d279bb0`, source hash `87ba7c79b4c87b980b378f0a6c08cd27051363bea3b9b44eaec4a7ee49a4f25c`, source revision `195cb49476f19998939bd98a0c742fe774ff7ebac866b687a2eeb4e4569af31d`, scenario hash `ebf13c339deecd0d6fa9c762a9ab70013d84e32c637009a4d0e215c66a900178`, 11 rows, 116 unresolved items, and 11 `PROBABILITY_OUTCOME_NEVER_ELIGIBLE` diagnostics. This is exact only for the supplied empty fixture and does not prove a dead mission.

Key rendered artifacts were emitted by the same call: ranking `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3785fec13450c6efda1d9176f6ec87820a73e72d9eacc435b1428b7b2de19b1f/92d01bc473c5a0af9e29736e5b46bc18a154e49d05c314c1f859848de33e8f4a/probability-probability-412fd7a39a6e3b136d279bb0-ranking.svg`, matrix `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e2c0554742723d5267ae087c37ae5b8415270c7150550235b4e86916af3294cf/c2f27f44637a32be80c5ec6b11a679bf0fa7eb5aeadbc5bd74bcb160eee014ed/probability-probability-412fd7a39a6e3b136d279bb0-matrix.svg`, and unresolved `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c2422e28e8b758734cf2728610718afd55e081893032c6f84152a1c8c5d7becd/1635b28c86135e4506321aafea860283700fe7c24885cfd264f86bd502971f61/probability-probability-412fd7a39a6e3b136d279bb0-unresolved.svg`.

### KUB primitive schema probe

The primitive-only probe used scenario set `IW040_TYPED_PRIMITIVE_PROBE_2026_08_15`, scenario `KUB_TYPED_PRIMITIVE_PROBE`, and the same complete pool. Result: `PROBABILITY_ANALYZED_PARTIAL`, analysis ID `probability-5781775f3ca1a1a1369c4bec`, source revision `3dcd170efd4db5c81fa5d85d1994f779ce5e06e77a46d8cf135b11c13f1bb7ee`, source hash `87ba7c79b4c87b980b378f0a6c08cd27051363bea3b9b44eaec4a7ee49a4f25c`, scenario hash `69074618e39219eeea7eff3aa74c1fb1a9069402f7d8cc2029f9e8fb97ea27ce`, 11 rows, 101 unresolved items, and 13 diagnostics. The reduction from 116 to 101 is not typed eligibility: all candidates still reported never eligible, while two war multipliers were merely reported inactive. JSON artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8b4e3e40441a1d7e957a9c45176d861247a850fddc5653fa9d627df6f79e6978/81267907c93851de23777037e0c985d954bc034b0e3138156f977d8fcce207f7/probability-5781775f3ca1a1a1369c4bec.json`; ranking `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bb92ec066e4dddffa6732919ed1ca068d9050d2d3193aa7096568d6720f754c/2237c11f6afef46972bb2a16132522148766933833843cf3b5f8c2ba26c8ff1c/probability-probability-5781775f3ca1a1a1369c4bec-ranking.svg`; matrix `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4da33184f948f498c834d434219401e3bd7b55baac0b0348299e35e68a0baa45/4618bf8e9e36fff3f012f7c99b11e47fdcc9863d779e2abaf358ce1b2bcda746/probability-probability-5781775f3ca1a1a1369c4bec-matrix.svg`; unresolved `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bf3a1050f97e04b0567469db4fc286200fcbf01c7a95e71384a501c9c26064a5/9eace193aa212d0ab97b570302e585af0c09ca4768fa6cb1ca3ca150bc3ccd41/probability-probability-5781775f3ca1a1a1369c4bec-unresolved.svg`.

### TAT empty named baseline

`hoi4.probability_evaluate` used the full 11-ID pool, scenario set `IW044_TYPED_BASELINE_2026_08_15`, scenario `TAT_FRAGILE_PEACE`, `state = {}`, raw-value metric, and a 600-day horizon. Result: `PROBABILITY_ANALYZED_PARTIAL`, analysis ID `probability-1a90a53a126a4de9d5d9aca2`, source revision `3dcd170efd4db5c81fa5d85d1994f779ce5e06e77a46d8cf135b11c13f1bb7ee`, source hash `2e84e8d3ea2432956071806401bea769ed0d2b53e4cd64e9d738138ade3c1dae`, scenario hash `01713324cd973c44a4ad271ff957deef45f7a4673b1d648a5b341e5d3813b8b0`, 11 rows, 116 unresolved items, and 11 never-eligible diagnostics. Key artifacts: JSON `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9adb27675b8dc2f14d0a40474daad352da244b10db0599f227bbe4c13e2c564a/360420631d30601e65509e1fbd723497b1a1021bef03edb70787d01b24b8329e/probability-1a90a53a126a4de9d5d9aca2.json`; ranking `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/eaf860cb8805772357b754ce4c5add5a281a7fb8ed33d597c127985395a76c13/f3656ba214dd3ab48ffe52e0a8d7a9fcd99383a33e2849a0465cdb015ed5a3dd/probability-probability-1a90a53a126a4de9d5d9aca2-ranking.svg`; matrix `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2536effc775880c41086e96b83e08a79a96ff2f654e9c1836e0d33e6b70aa4ae/0a86ea0d45ae81fac8eca515015465b4f26b81f97223c97d441de3bcba503dd1/probability-probability-1a90a53a126a4de9d5d9aca2-matrix.svg`; unresolved `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9e28d4193507909a10c518c8509aacc9034d96ef0d442caf490d422235c5801a/fe922c34458a1f20c3a6c9757ce3b0062405808c9db10c0b30cebace46b6c352/probability-probability-1a90a53a126a4de9d5d9aca2-unresolved.svg`.

## Source score trace (score-only)

The shared constants are exact source evidence: `urgent = 100`, `high = 25`, `standard = 10`, and `modifier_double = 2`. KUB and TAT use urgent 100 for the passive founding mission and emergency command, high 25 for depots, border guards, community compacts, constitutional autonomy, socialist councils, and durable sovereignty, and standard 10 for former-host settlement, agrarian compact, and the network corridor. War doubles border-guard and emergency-command scores. Former-host settlement doubles when the severe-host-threat trigger is absent. These are willingness scores, not click probabilities. The founding mission has `available = { always = no }` and must not be interpreted as AI starvation.

## Sweep receipts and skipped comparisons

The KUB sweep used the complete 11-ID pool, `KUB_FRAGILE_PEACE`, path `state.has_war`, three steps, pairwise sensitivity, and rank-reversal search. It returned exact `INTERNAL_ERROR` / `Unexpected internal error` with no artifact.

The TAT sweep used the complete 11-ID pool, `TAT_FRAGILE_PEACE`, path `state.has_war`, three steps, pairwise sensitivity, and rank-reversal search. It returned exact `PROBABILITY_SWEEP_RANGE_REQUIRED` with blocker message `Every sweep path requires a scenario range, numeric alternatives, or numeric state value`, details `scenarioId = TAT_FRAGILE_PEACE`, `path = state.has_war`. No threshold, sensitivity, or rank-reversal conclusion is made.

`hoi4.probability_compare` was not run in this tranche because no owner-applied source change or valid historical before/after source snapshot exists. A current/current receipt would be capability evidence only and cannot close the typed-fixture gap. Simulation was skipped because no uncertain input distribution or seed contract was declared. Sequence was skipped because these ordinary mission pools are not a manifest-declared custom weighted pool with cadence, recovery, cooldown, removal, reset, and terminal-state declarations. Strategy-factor inspection/evaluation was not widened in this bounded mission-only pass; prior current handoffs record no weighted strategy surface.

## Findings and recommendation

- Source-relative candidate pools are complete at 11/11 for each admitted package, but runtime pool and external-factor completeness are unresolved.
- The adapter is score-only and intentionally withholds normalized selection probabilities. No exact probability can be stated.
- Empty fixtures produce 11 never-eligible diagnostics per evaluated package; this is exact only for `state = {}` and is not evidence of dead projects.
- The primitive probe proves that direct scalar JSON is not enough to resolve actor and compound scopes. The nested object form needed to describe those scopes is rejected by tool input validation.
- No validity, dominance, starvation, repetition, rank-reversal, exploit, or balance conclusion is supported by this tranche.

Recommended next step: the probability-tool owner should provide a documented typed fixture schema that exposes country actor scope, capital/anchor scope, former-host target scope, country flags, named variables and comparison values, active decisions, resource values, and target validity. Re-run the same ten scenario IDs with the same 11-entry pools, then run sweep/compare under an accepted numeric range and a true before/after source pair. Do not patch weights, central admission, or Join based on these partial receipts.

## Simplifications, omissions, and blockers

No gameplay simplification or fallback was applied. The ten scenario contracts were not all executed because the adapter rejected the required compound fixture representation; no balance claim is made. The exact MCP blockers are the nested-state `-32602` validation errors, KUB sweep `INTERNAL_ERROR`, and TAT sweep `PROBABILITY_SWEEP_RANGE_REQUIRED`. No source file was edited, staged, or committed by this audit.
