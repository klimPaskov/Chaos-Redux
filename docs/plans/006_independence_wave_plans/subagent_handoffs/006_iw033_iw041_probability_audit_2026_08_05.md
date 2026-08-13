# IW-033 / IW-041 probability and weighted-logic audit

Evidence date: 2026-08-05.

Audit owner: `chaosx_ai_probability_auditor`.

Verdict: read-only evidence is partial and remains unresolved for runtime selection probabilities, normalized package ranks, rank reversals, and live 21/20 capacity success because the typed HOI4 MCP scenarios cannot represent the package planner's event targets, dynamic trigger scopes, attestation helpers, evolution flags, or prior-wave arrays. The source-level automatic pools are structurally complete for the supported `random_list` adapters, and the allocator is fail-closed on exact-count or aligned-array failure.

## Scope and source surfaces

The audit covers the promoted IW-033 Karelia and IW-041 Crimean Tatar package wrappers in Region 04, the outer automatic allocator, the package allocation-weight helper, the package dispatch attestation list, the package decision mission scores and cancellation gates, and the package AI strategy file.

Exact source surfaces audited:

- `common/scripted_effects/006_independence_wave_packages_region_04_effects.txt:119-163` defines the Region-04 package wrappers, the automatic eight-package preparation list, and the inner `random_list`.
- `common/scripted_effects/006_independence_wave_package_allocator_effects.txt:15-133` recomputes all region totals, draws one region/package, loops toward the target, and fails closed on pool exhaustion, stale phase, exact-count failure, or misaligned metadata arrays.
- `common/scripted_effects/006_independence_wave_package_planner_effects.txt:507-696` defines the runtime candidate gates and allocation-weight modifiers.
- `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:44-45,117-118` includes IW-033 and IW-041 in the runtime adapter and content-attestation OR-lists.
- `common/decisions/006_independence_wave_karelia_crimea_decisions.txt:9-365` defines the two passive founding missions, eight government route choices, durable sovereignty choices, former-host action, and regional network mission.
- `common/scripted_triggers/006_independence_wave_karelia_crimea_package_triggers.txt:162-210` defines active-project exclusion, capital-loss invalidation, and the custom live-league phase trigger.
- `common/ai_strategy/006_independence_wave_karelia_crimea.txt:27-88` defines KAR/CRI army, production, infrastructure, bunker, dockyard, and war-avoidance factors.
- `common/script_constants/006_independence_wave_constants.txt`, `common/script_constants/006_independence_wave_package_constants.txt`, and `common/script_constants/006_independence_wave_evolution_constants.txt` centralize bands, count ladder, attempt cap, base modifiers, and evolution modifiers.

The current post-promotion static attestation set is 21 selectable packages across 20 compatible reservation groups: IW-001, IW-002, IW-004, IW-006, IW-007, IW-008, IW-009, IW-010, IW-012, IW-014, IW-017, IW-018, IW-019, IW-023, IW-033, IW-041, IW-070, IW-071, IW-072, IW-173, and IW-184. The 21/20 state is an input witness only; it does not prove that 20 live releases can be frozen.

## Required references consulted

Before source review I read `AGENTS.md`, `.agents/skills/chaos-redux-subagents/SKILL.md`, `.agents/skills/chaos-redux-events/SKILL.md`, `.agents/skills/chaos-redux-mtth/SKILL.md`, and `.agents/skills/chaos-redux-event-planning/SKILL.md`. I also consulted the offline Paradox wiki pages for Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, and AI modding, plus the applicable vanilla documentation under `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/`, including `script_concept_documentation.md`, `effects_documentation.md`, `triggers_documentation.md`, and AI/decision/event references.

## MCP inspection evidence

The mandatory read-only `hoi4.probability_inspect` calls used workspace `mod_chaos_redux_ea3b2d67c2c0`.

### Region-04 package pool

Adapter: `random_list`.

Source revision: `829ca80edf9b0342786874c3484c9c0479f8ef55d3088fa078916b8f7b90f11e`.

Source hash: `e8f1792fa6b12a426551789a259fb67b570cb5194059ccc17e433ade122af2eb`.

The inspector found a complete eight-entry pool with eight required inputs and zero unresolved expressions. The pool is IW-033, IW-036, IW-037, IW-038, IW-039, IW-040, IW-041, and IW-042. IW-034 and IW-035 are intentionally absent from the automatic Region-04 draw because they are open-sovereignty route-only packages.

Inspection artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f3bc6c29192012b4ec24ff4f4bc0606118f243007451e6e0d2567dcc6af956b7/144436b7a8795157e87eda2696f5587ce3f256530b4166ada8ca8c422a3c9c3b/probability-inspect-e8f1792fa6b1.json`.

### Global outer allocator pool

Adapter: `random_list`.

Source revision: `829ca80edf9b0342786874c3484c9c0479f8ef55d3088fa078916b8f7b90f11e`.

Source hash: `bc6f7ff8598df33b610442e6ada24c28d7d82167fe135474deb18094b3b6cf83`.

The inspector found a complete 14-entry region pool with 14 required inputs and zero unresolved expressions. This proves only that the outer region `random_list` is discoverable; it does not resolve each region's dynamic package total.

Inspection artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e612c9a4efaad5d3d8412a4fbe1d7878180ba6e432a3916d0ed32823efc9af45/cfae9900846717f2dc513571a9681e25f03f90b23a2ff170bd043fab291309be/probability-inspect-bc6f7ff8598d.json`.

### Decision mission surface

Adapter: `mission_ai_will_do`.

Source revision: `829ca80edf9b0342786874c3484c9c0479f8ef55d3088fa078916b8f7b90f11e`.

Source hash: `0ade9f81b363914d5de020c39be0b0d84a4607d32801dc147919dd3b5080c500`.

The inspector discovered 20 candidate missions and 13 required inputs, but marked the runtime pool incomplete. This is the useful adapter for the file; the `decision_ai_will_do` parser did not expose the full category as a complete candidate pool.

Inspection artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0c255e89aff2196d7f1c6f82b303957ab8f5bdc0ee6bfedf684f90c1857fab6f/9f3fdf91f090205f73747adc689db40f51174883c8be91e4f62c50ff7d309ab1/probability-inspect-0ade9f81b363.json`.

### Unsupported adapters and blockers

The `custom_weighted_pool` inspection of `common/scripted_effects/006_independence_wave_package_allocator_effects.txt` returned `poolComplete=false`, zero discovered candidates, and zero required inputs because the installed adapter does not recognize this helper as a declared custom pool. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f7fdbe9397c1bf9966186ffa6e47b937e78dedb5490ed7278dc7e081d5607815/135a03cf97599af47e14f37d11917d7075c7a7c38b2f9eaa753d9337afaa4e63/probability-inspect-bc6f7ff8598d.json`.

The `ai_strategy_factor` inspection of `common/ai_strategy/006_independence_wave_karelia_crimea.txt` returned `PROBABILITY_SURFACE_EMPTY` with the exact blocker `No weighted blocks matched this request`; no MCP artifact or engine-level strategy ranking exists for this source.

## Region-04 required scenarios

Scenario set `R04_REGION04_ALLOCATOR_REQUIRED_SCENARIOS_CURRENT` supplied the complete eight-entry adapter pool and explicitly named the following states:

- `R04_ALL_OPEN`: all eight candidates declared eligible, open sovereignty, chaos band 3, target 1, attempt cap 206, capacity 20.
- `R04_KAR_BLOCKED`: IW-033 declared blocked and the other seven Region-04 candidates supplied.
- `R04_CRI_BLOCKED`: IW-041 declared blocked and the other seven Region-04 candidates supplied.
- `R04_BOTH_OPEN_LOW_CAPACITY`: both promoted packages open with capacity witness 20.
- `EVENT5_SOVIET_CONFLICT`: both promoted packages open with an explicit Event-005/Soviet-conflict marker.
- `CAPACITY_20_WITNESS`: all eight candidates supplied with target count 20, capacity 20, and attempt cap 206.

The candidate arrays, blocked IDs, chaos band, target, capacity, and conflict marker are complete as declared scenario inputs. The scenarios are not complete runtime world states because typed state cannot provide `can_plan_independence_wave_package_*` trigger scopes, anchor owners, primary hosts, runtime attestation helper results, opening-confidence variables, evolution flags, or prior-wave package/region/host arrays.

### Required-scenario evaluation

Adapter: `random_list`; analysis ID: `probability-25b3957d1521f759cc226dac`; source revision: `829ca80edf9b0342786874c3484c9c0479f8ef55d3088fa078916b8f7b90f11e`; scenario hash: `ac987aa606befdad128af2eec192bce7f5dd243c794db9b530a089f833ebd675`; six scenarios, 48 candidate rows, eight unresolved items, and zero diagnostics.

Evaluation artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8d6208844b5e1473dcfd02f18acbbce5acb3590feacd02f3ac574f6a7ddaf7f6/37bd0882147eed363e979493d4dd54bc7c3c66f3a7466ad311bf076fa75c2d2c/probability-25b3957d1521f759cc226dac.json`.

Classification: partial and unresolved, not exact probability. No normalized IW-033 or IW-041 percentage can be stated because the dynamic candidate weights remain unresolved even though the eight-entry candidate pool is complete.

Rendered ranking: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d93b3acd544a1ef903264741d5d1697458071c48c93e38e1542be7928e22eaa0/38ee02e5f1b839d58e582f09da949586245e70e16ff8a0fb42408847141fbbb3/probability-probability-25b3957d1521f759cc226dac-ranking.svg`.

Rendered matrix: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a56ce082013c78bdd177ea3ea5c0eca575860738b615bdbb8c74dd48457fc69b/83dc857efc1f3acd219c5be81bf52c4556d960415d22aed1150f83398124e8a8/probability-probability-25b3957d1521f759cc226dac-matrix.svg`.

Rendered unresolved view: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f70435e64441089d5ce25d1933bad39ef19e4abb89089446fe2883f1554c0b51/2c2bec7dd690efbfaf5d7ef03605db85e7c4b5520570273868f0ee53db3c553e/probability-probability-25b3957d1521f759cc226dac-unresolved.svg`.

### Region-04 sensitivity and rank-reversal sweep

Sweep set `R04_REGION04_ALLOCATOR_SWEEP_CURRENT` varied `wave_chaos_band`, `capacity`, and `target_count` with five steps, pairwise sensitivity, and rank-reversal search. Analysis ID: `probability-0d10df11b3c80b0cda81eae1`; source revision: `829ca80edf9b0342786874c3484c9c0479f8ef55d3088fa078916b8f7b90f11e`; scenario hash: `7256ac311e718c21570b25b55d41f46c738c3df2c968a59b0714ea22745f7f5b`; six scenarios, 48 candidate rows, 18 sweep points, eight unresolved items, and zero diagnostics.

Sweep JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fd80b30ad2fc36f0f3ba711ae224a0697773ea1884434dba8b044206102aa83b/05dbc1d7a551b982ea9893a85318771292399d21c27f501b98d85b113d0ed1fe/probability-0d10df11b3c80b0cda81eae1.json`.

Rendered sensitivity: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2ea944f307538f0364103d40d8ccb1bb984df13f665ff4c980e99bc321186813/9a2d438b51012c450d762fadde5e572ab3616bb9b58b662b8025a0c6a682d55e/probability-probability-0d10df11b3c80b0cda81eae1-sensitivity.svg`.

Rendered threshold: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a6d32ffc270e06218fbe6e53b5f3d111d3f383d152a2e17fa057722f7cf35cc8/3bdf53cf73a75ddafded62730cdea482a00506ebe90e56c8bd9225062b9afd20/probability-probability-0d10df11b3c80b0cda81eae1-threshold.svg`.

Rendered ranking: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/745aeee454ad27a92273831b1b338786057a84ab3c44c33a373a2cfea5ab1e34/f297666db1a77fc287f379e8d24f9b124060eb674a02a90446db9ea984679630/probability-probability-0d10df11b3c80b0cda81eae1-ranking.svg`.

Rendered matrix: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a56ce082013c78bdd177ea3ea5c0eca575860738b615bdbb8c74dd48457fc69b/e9b67312ddb00fd0333e6bf673b3b72c89c01457eae30b432c341469bc65438f/probability-probability-0d10df11b3c80b0cda81eae1-matrix.svg`.

Rendered unresolved view: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f70435e64441089d5ce25d1933bad39ef19e4abb89089446fe2883f1554c0b51/61938b9373dd984a5ba03cd97741d47ed0e4983f28c06ad4c977a403be3b2de9/probability-probability-0d10df11b3c80b0cda81eae1-unresolved.svg`.

Classification: partial and unresolved. The sweep found no provable rank reversal or dominance result because every candidate trace still depends on unresolved runtime gates; the rendered ranking is evidence of unresolved analysis, not a probability claim.

## Global 21/20 post-promotion allocator scenarios

The static post-promotion state was supplied explicitly as 21 attested package IDs, 20 compatible groups, target count 20, capacity 20, and maximum attempts 206. The global outer adapter sees 14 region entries; package-level eligibility remains dynamic inside each region.

Scenario set `GLOBAL_ALLOCATOR_21_20_POSTPROMOTION` evaluated `POSTPROMOTION_21_20_WORLD_COLLAPSE` at chaos band 5, `POSTPROMOTION_21_20_TOTALEN` at band 4, `POSTPROMOTION_21_20_KAR_CRI_REGION04_OPEN` at band 3 with all eight Region-04 IDs, and `POSTPROMOTION_21_20_KAR_BLOCKED` at band 3 with IW-033 blocked.

Evaluation analysis ID: `probability-67847a3609e44b3763efb75e`; source revision: `829ca80edf9b0342786874c3484c9c0479f8ef55d3088fa078916b8f7b90f11e`; scenario hash: `2b5c8281612b52a65be786fb3b377a5a5ccd6bc03764760ff3f5ae1d599d875d`; four scenarios, 56 candidate rows, 14 unresolved items, and zero diagnostics.

Evaluation artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cc09d87d3abd5f3a78f22f875ce3ca6097274370559253ab3350b50829d13943/5fd78d242bfc2afc60d5f3a432f602139598622355c6bb82468010edb09547cb/probability-67847a3609e44b3763efb75e.json`.

The 21/20 sweep `GLOBAL_ALLOCATOR_21_20_POSTPROMOTION_SWEEP` varied the same three numeric paths with five steps, pairwise sensitivity, and rank-reversal search. Analysis ID: `probability-3c86faa8135942a21b98614f`; source revision: `829ca80edf9b0342786874c3484c9c0479f8ef55d3088fa078916b8f7b90f11e`; scenario hash: `db812d0a10c536b55cf722de0b076303411b59cad0ffe489344bbbe6fda94543`; four scenarios, 56 candidate rows, 12 sweep points, 14 unresolved items, and zero diagnostics.

Sweep JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/87cdd0babdfe0042fe793fbb25623909465ae811c2c75340b1527fbbce61a9dd/e28ccc07a486b42bc23d98b8ae70d4182007e1c71d386dd7e8062e8c70736d07/probability-3c86faa8135942a21b98614f.json`.

Rendered sensitivity: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/506fa8621c9c3e3b23224c0c0d34c7aabe94b680abc6e94518ff8e007b527c45/94d942d241b417d92ae49d45c27434fce8eb1266a167489f533a175466cd80c2/probability-probability-3c86faa8135942a21b98614f-sensitivity.svg`.

Rendered threshold: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a6d32ffc270e06218fbe6e53b5f3d111d3f383d152a2e17fa057722f7cf35cc8/bd5433800274c41e5cc85b1c66533fea0f9c6077d1b880cbb362f843c3e6bc17/probability-probability-3c86faa8135942a21b98614f-threshold.svg`.

Rendered ranking: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f362b867673ae53cb49b24f3d3cac7c22cce68f0c92978d4b3e0a01464cc5db5/8868907d202f5b379bb9be8258b4ed34daa2c57f42fc33f7827f00a4efdaf018/probability-probability-3c86faa8135942a21b98614f-ranking.svg`.

Rendered matrix: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/87f035ce8a58e9e97b05291f2ae016f9909c8918626021202e06f96b5ad21462/f123e4904cb50c778ba659cd9096da8ad79959b2670f578a16f78f5dd66e3c2e/probability-probability-3c86faa8135942a21b98614f-matrix.svg`.

Rendered unresolved view: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b376452dd35a669b20b3ba5787e6af6347617460240eb4e6e0da2f2ae9a45962/bae51827a01ca9ace2b93980918d90d59034de74cfa1ecd57f1add3bf65cfe5f/probability-probability-3c86faa8135942a21b98614f-unresolved.svg`.

Classification: partial and unresolved. The MCP pass does not prove that 21 attested packages can satisfy a 20-release wave, nor that 20 compatible groups survive all anchor, host, capital, Event-005, and reservation checks.

## Decision mission scenarios and compare

The current mission evaluation set `IW033_IW041_MISSION_STATES_CURRENT` contains nine named states: `PACKAGE_KAR_FOUNDING`, `PACKAGE_CRI_FOUNDING`, `PACKAGE_KAR_GOVERNMENT_ROUTE`, `PACKAGE_CRI_GOVERNMENT_ROUTE`, `PACKAGE_KAR_CAPITAL_LOST`, `PACKAGE_CRI_LOW_RESOURCES`, `PACKAGE_KAR_NETWORK_NOT_LIVE`, `PACKAGE_CRI_NETWORK_LIVE`, and `NO_PACKAGE`.

Mission evaluation analysis ID: `probability-ffaa0d8ab584da07cc31ba7d`; source revision: `829ca80edf9b0342786874c3484c9c0479f8ef55d3088fa078916b8f7b90f11e`; scenario hash: `544b7f23fc33dcd76a5dc097df95f286c56dcb25ad1d40c55cb6165386d25a18`; nine scenarios, 180 candidate rows, 104 unresolved items, and three design diagnostics.

Mission evaluation artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b45656c8c88990b0c40cfbc6180aeeb5a206db9e0d8b267c59d30d6118afe4be/fc5b2d340479c9f9101e7255d6250f1699393b3e7f0f3410f34df8d9aa31a788/probability-ffaa0d8ab584da07cc31ba7d.json`.

The three warnings are the two passive founding missions and the network mission. The founding missions intentionally use `available = { always = no }` because they are activation-backed passive timers, so the warning is not evidence that a selectable AI action is starved. The network warning is not a source conclusion because the custom global live-league phase trigger cannot be represented by the typed scenario state.

The true before/after compare uses adapter `mission_ai_will_do`, the current decision source after owner changes, and an in-memory baseline with the earlier founding cancel predicates, without the eight capital-loss cancellation pairs, and without the live-league availability conjunct. Named scenarios are `PACKAGE_KAR_FOUNDING`, `PACKAGE_CRI_FOUNDING`, `PACKAGE_KAR_WAR`, and `PACKAGE_CRI_SETTLED`.

Compare analysis ID: `probability-dbc42b020c2684cb6900bff8`; source revision: `829ca80edf9b0342786874c3484c9c0479f8ef55d3088fa078916b8f7b90f11e`; scenario hash: `8e8a9836a34b1c158311e14c54a5ebf81ec0daafb816ff4d7c185b44ea0e9ebe`; four scenarios, 80 candidate rows, 131 unresolved items, three diagnostics, and four comparison changes.

Compare artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4065277e6daf30e5705b96582afc40a1fbb8fde7debebcd317ee0f071061b1b9/618d621d8114928d7c900400d943ad441f8d2300f2c6193e4cc18e63702b089a/probability-dbc42b020c2684cb6900bff8.json`.

Rendered comparison: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d93d12f7d8a7a2c5704e13aae3e4263bd1ee74963dd8a9b44185efdd62b2d20f/80f62065ecff07fab0fcd2ab7eebaadb63ffb7c635fa2588200ba6f79a4da959/probability-probability-dbc42b020c2684cb6900bff8-comparison.svg`.

Classification: partial compare. The decision-source changes are visible to the adapter, but trigger/effect changes in the package trigger and package-effect files are outside this decision-only compare and require a future full-graph manifest or a supported typed trigger fixture.

## Source-level score and modifier trace

The planner starts each runtime-attested candidate at base 100 and floors a positive candidate at minimum 1 after modifiers. The centralized baseline is `common/script_constants/006_independence_wave_constants.txt:94-104`.

The score-only modifiers are sponsored candidate +100, registered tag +25, new region +30, new host +20, prior package -80, prior region -25, prior host -20, signature below high-chaos band -35, and high-chaos-only +45. Opening-confidence adds -20 below the low threshold or +15 at/above the high threshold. Evolution modifiers are dormant registered +30, dormant regional +25, dormant signature +35, armed industrial +20, armed frontier +20, sovereign-congress regional +15, sovereign-congress signature +30, open-sovereignty high-chaos +55, and open-sovereignty formable +40. World Collapse applies a 1.35 rarity multiplier when the candidate's earliest band is Totalen-only.

These are Clausewitz willingness scores used to build proportional weighted pools, not click probabilities. Because candidate eligibility and the modifier inputs are unresolved in MCP, the trace is score-only and cannot be normalized into exact IW-033/IW-041 selection percentages.

The allocator recomputes weights before every draw, selects through the outer 14-region pool and inner Region-04 pool, and loops while selected count is below target and attempts are below 206. It marks `independence_wave_plan_exact_count_failed` for insufficient pool or misaligned arrays and does not claim contribution readiness unless the exact target and array alignment both hold.

## Findings

- Pool completeness: Region 04 has an exact eight-entry `random_list`; the global allocator has an exact 14-entry outer `random_list`; the mission file has 20 discovered candidates but an incomplete runtime pool; the custom-pool adapter has no discoverable pool.
- AI validity: source wrappers gate each Region-04 weight through `can_plan_independence_wave_package_*`; route-only IW-034/IW-035 are excluded from the automatic pool; no positive weight is proven for an impossible candidate because the actual trigger scopes are unresolved.
- Dominance: no exact candidate or region dominance is proven. The base/modifier table could produce large rank differences under sponsorship, evolution, and novelty flags, but this is score-only until runtime states are supplied.
- Starvation: no proven starvation of IW-033 or IW-041. The blocked scenarios are declared arrays, but MCP cannot prove that the corresponding `can_plan` trigger evaluates false in the live scope. The two founding mission warnings are intentional passive `always = no` entries.
- Rank reversal: the regional and global sweeps performed rank-reversal searches, but all candidate traces remain unresolved, so no rank reversal or stable ordering is proven.
- Repetition: prior-package, prior-region, and prior-host penalties plus new-region/new-host bonuses are source-visible anti-repetition controls. No repeated-draw exploit is proven; a complete sequence run is not authorized because the dynamic package pool, cadence, reservation releases, and terminal state are not fully declared.
- Capacity and exploit risk: the exact-count loop, attempt cap, aligned-array gate, and pool-exhausted failure path are source-visible fail-closed guards. MCP cannot prove a 20-release success or disprove a runtime reservation/host collision under the 21/20 witness.
- AI strategy: KAR/CRI source factors are visible only by source review because the `ai_strategy_factor` adapter returned `PROBABILITY_SURFACE_EMPTY`; strategy dominance or timing cannot be claimed.

## Recommended fixes or follow-up evidence (do not apply here)

1. Add a supported typed MCP fixture or adapter manifest for `can_plan_independence_wave_package_*`, anchor/host ownership, runtime content attestation, evolution flags, opening confidence, and prior-wave arrays, then repeat the same Region-04 scenario IDs and the same 21/20 global scenario IDs.
2. Preserve the complete Region-04 eight-entry pool and the explicit exclusion of route-only IW-034/IW-035; any future admission or removal must rerun the `random_list` inspect, required scenarios, sweep, and compare artifacts.
3. If exact 21/20 capacity claims are required, expose reservation-group uniqueness, capital-preferred host survival, Event-005 conflict state, and rollback/cleanup state to a supported allocator scenario adapter; the current 21 attested packages and 20 compatible groups are not sufficient engine proof.
4. Add a supported read-only `ai_strategy_factor` adapter for the KAR/CRI strategy file or provide a manifest that maps `build_army`, production, construction, and `avoid_starting_wars` factors to named scenarios. Do not infer strategy probabilities from the static values.
5. For future balance patches to decisions, compare the same four package states against a baseline and include the package trigger/effect graph in the compare manifest so capital-loss and network-gate changes are not omitted.

## Skipped analyses, blockers, and uncertainty

- No `probability_simulate` run was performed because the task did not declare uncertain numeric inputs or a seed, and simulation cannot substitute for missing runtime scopes.
- No `probability_sequence` run was performed because the complete package pool, cadence, reservation release transitions, and terminal state were not declared to the adapter.
- No exact selection probability, timing distribution, or score-to-click conversion is claimed.
- No live game launch or runtime log inspection was performed; live consumer validation remains parent/user scope.
- The event structural check used `hoi4.event_inspect` scan mode on `events/006_independence_wave.txt` and returned `EVENT_INSPECTED_PARTIAL` with revision `743b8719ae8db9bf7c09e40315f59c39becf56604654e0511451d072b1c5182f`, graph hash `b479d02621100306fdb9b48476f9700b0904dad943146a4854e48f427f9e4640`, and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1694cc68dbe14ad96dff50d83c48f6bb55150408f7038e477f8b70e9463b963d/5512df2721ff7dc7dd7f046f0f802d35cdb3add7d1690ca1ae55d7beadf8f26a/event-scan-743b8719ae8d.json`; this was a broad structural scan and did not replace the probability pass.

No gameplay, AI, event, decision, trigger, effect, localisation, asset, or runtime file was changed by this audit. The only intended change is this read-only handoff document.
