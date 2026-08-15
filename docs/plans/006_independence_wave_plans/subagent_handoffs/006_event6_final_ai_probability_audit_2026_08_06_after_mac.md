# Event 006 final AI and probability audit after IW-026 Macedonia

Date: 2026-08-06

Mode: read-only probability audit; no gameplay, AI, event, decision, focus, localisation, or runtime files were changed.

## Scope and revision

The audited source target is commit `56e72be08a00cd3b84c1170734624717855288cd` (`Implement IW-026 Macedonia package adapter`). The local worktree advanced after the audit, but the HOI4 MCP source snapshot used here is `sourceRevision=73416e4cb8b3533fd51442cce1a6da08044932e01a694e17bb1a372c4996d3b6` in workspace `mod_chaos_redux_ea3b2d67c2c0`.

Required source and structural references were read before the audit: `AGENTS.md`, the Chaos Redux events, subagents, improvement-loop, and HOI4 MTTH skills, the required offline Paradox wiki pages, and the relevant vanilla documentation files.

## Read-only verdict

Verdict: **HOLD/PARTIAL**.

The MCP probability route proves source discovery and several complete `random_list` pools, but the named scenario evaluations were run with empty state records and incomplete external context. They therefore provide bounded score evidence and eligibility diagnostics only. They do not establish click probabilities, live AI choice rates, timing distributions, dominance, starvation, rank reversal, repetition, or exploit safety.

## Audited weighted surfaces

### Package allocator random lists

`common/scripted_effects/006_independence_wave_package_allocator_effects.txt` inspected as `random_list`: 14/14 candidates, unresolved 0, `poolComplete=true`, source hash `bc6f7ff8598df33b610442e6ada24c28d7d82167fe135474deb18094b3b6cf83`.

Region allocator files were all inspected as `random_list` and returned `PROBABILITY_SOURCE_INSPECTED`, `poolComplete=true`, unresolved 0: Region 01 (9/9), Region 02 (9/9), Region 03 (8/8), Region 04 (8/8), Region 05 (12/12), Region 06 (12/12), Region 07 (5/5), Region 08 (3/3), Region 09 (7/7), Region 10 (7/7), Region 11 (5/5), Region 12 (13/13), Region 13 (19/19), and Region 14 (9/9). The formable registry random list was also complete at 2/2. The Region 03 selector includes IW-026 Macedonia and excludes IW-025 Vojvodina in the current source snapshot.

Representative inspect artifacts:

- Outer package allocator: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/08f50bac1050db701611403e27a03701966f02f8925fedefcc05329410b2c5c8/f1cd3d8b89abae49c00cf359846f8bdc0bcc0576525a192440acb7c40102fd61/probability-inspect-bc6f7ff8598d.json`.
- Region 03: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a9666c7277e29d0b7679d2e023983df6fc9d9e900024adfd850cef2d36df35da/b0d81feab2e6138ca1f9b11a21bb330bca6f743ab87fd7e43c5aaedb45863aba/probability-inspect-ff114c943bad.json`.
- Region 04: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fd39d431716377e4302f4eff380382cab28c823747abb750c5ab47e603f956cd/e5701a4d4bd8f874962e490e4c62ba77017cc06b5424f2c20c17dc199d0bb1db/probability-inspect-e8f1792fa6b1.json`.

Named allocator evaluations used complete candidate declarations but empty state records, so all are bounded and partial:

- Outer set `E6_ALLOCATOR_REQUIRED_SCENARIOS_CURRENT_MAC_2026_08_06` (`R03_MAC_OPEN`, `R04_ALL_OPEN`, `R04_KAR_BLOCKED`, `R04_CRI_BLOCKED`, `CAPACITY_20_WITNESS`): analysis `probability-d5a09cc4bf4283756461eefa`, scenario hash `30697835b662c8c36f3a9c5e49c2649b2a50304b67c96528fe6dfeee44f4baea`, 5 scenarios, 70 candidate rows, 14 unresolved, 0 diagnostics. JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/76055df486097950aef7840353f0245bcc153df7135d60d8a259b7b961de1d73/8d319c99264de451bc89126e3d5eeccd8ba1fdd197735f804ee3761b6f9bc0fe/probability-d5a09cc4bf4283756461eefa.json`. Ranking render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/21169ca21d9404c158e6197ec38fd73eab0eb8b57a4ce55688cc4f1e14f6d382/b8f2337c4daa87e34ecc9c064fc6f8bafaa12a98f0040e4e00afd56703efa14e/probability-probability-d5a09cc4bf4283756461eefa-ranking.svg`.
- Region 03 set `E6_R03_ALLOCATOR_SCENARIOS_CURRENT_MAC_2026_08_06` (`MAC_OPEN`, `MAC_LIVING_FORMER_HOST`, `MAC_HOST_WAR`, `MAC_LOW_CAPACITY`): analysis `probability-1058ddcf50884afda456b1ee`, scenario hash `9d5b76e6aab45fdaf629fef5a333d715216c7b1bd7d43cb066b93816ea543e3d`, 4 scenarios, 32 rows, 8 unresolved, 0 diagnostics. Unresolved render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e1d40f65380ad92e4f6c3d9b34b9af29cffe6f7e013ece98661e15f60b6d9ead/e1063142603681b65ec045bcbc13904a96e216b1964e655ee7d778e8da9c0565/probability-probability-1058ddcf50884afda456b1ee-unresolved.svg`.
- Region 04 set `E6_R04_ALLOCATOR_SCENARIOS_CURRENT_MAC_2026_08_06` (`R04_ALL_OPEN`, `R04_KAR_BLOCKED`, `R04_CRI_BLOCKED`, `R04_BOTH_OPEN_LOW_CAPACITY`, `CAPACITY_20_WITNESS`): analysis `probability-1da57bc3ccc5291ae92003d2`, scenario hash `375054f69e2266d840a16bd26d715a296c998d218e486d5f7de2e3a02888eb34`, 5 scenarios, 40 rows, 8 unresolved, 0 diagnostics. Ranking render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2b3e79e146e8c1ada7e5ca3a14f74f651637261be71e2419258e01740ea3f34f/4ec6451be9a0b10de22df99c2671e6159aaf91fbb0cc8cc48e8298d14b9bf495/probability-probability-1da57bc3ccc5291ae92003d2-ranking.svg`.

### IW-026 Macedonia decisions, missions, and strategy

Source `common/decisions/006_independence_wave_macedonia_decisions.txt` inspected with the decision adapter at 1 candidate, 10 required inputs, unresolved 0, `poolComplete=false`, source hash `9d4afb0135117104c8e7624dc132730cf50e390737cc74b8a6bedf13861c59cf`. The same source through the mission adapter returned 11 candidates, 13 required inputs, unresolved 0, `poolComplete=false`.

Named decision set `E6_MAC_DECISION_SCENARIOS_CURRENT_2026_08_06` (`MAC_FOUNDING_CALM`, `MAC_HOST_CRISIS`, `MAC_ROUTE_LOCKED`, `MAC_NO_VALID_TARGET`) returned analysis `probability-50e16d24fb12038cf17559db`, scenario hash `d2934fde0ea5a59080569095a43c4690e163585f39040974fe6403037b4bf567`, 4 scenarios, 4 candidate rows, 17 unresolved, and diagnostic `PROBABILITY_OUTCOME_NEVER_ELIGIBLE` for `independence_wave_mac_codify_vardar_settlement`. JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/24f99491037fa03e70ba1725d778d3c3f03aa177f4c0035fd89eaaa7d2d8d370/5aee8f1bdc1b3c8c74a58fbf05903e19c2afa4c3d6ed40c45ddebbc8969bd5fa/probability-50e16d24fb12038cf17559db.json`.

Named mission set `E6_MAC_MISSION_SCENARIOS_CURRENT_2026_08_06` used the same four empty-state scenarios and returned analysis `probability-910da7cbe88f2d4a9f74d4c1`, scenario hash `c19631893d53244337d16a8fe1645284f549f73edeb4105661265a913f7c158a`, 4 scenarios, 44 rows, 64 unresolved, and diagnostics marking `independence_wave_mac_hold_vardar_council_together` and `independence_wave_mac_open_danube_network` never eligible. JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/204a3f6dd195a55d412ef17ec67c1020e9248061664d70b4331e8dce21bd971f/3d85c91378d178ca137e78db9a2eeeb7bf4a2e11bc76e9db5f852093485d9cda/probability-910da7cbe88f2d4a9f74d4c1.json`. Ranking render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/041c02f9f7c1d108c44d2588cd03a3903462fac9b58e39fade749286bf8a9a9d/635213b92ebc1e4547202b5f33dcf61b2a086b907a0deacae67044c63f99d949/probability-probability-910da7cbe88f2d4a9f74d4c1-ranking.svg`.

`common/ai_strategy/006_independence_wave_macedonia.txt`, `common/ai_strategy/006_independence_wave_generic.txt`, and `common/ai_strategy/006_independence_wave_karelia_crimea.txt` each returned the exact MCP blocker `PROBABILITY_SURFACE_EMPTY` for `ai_strategy_factor`; no strategy ranking evidence is available.

### Shared decisions, missions, focus, event options, MTTH, and scenario navigation

The shared decision source `common/decisions/006_independence_wave_decisions.txt` inspected at 10 candidates/61 required inputs/unresolved 0. The shared mission source inspected at 54/38/0. The current shared decision evaluation `probability-ab9f6f8cec9101f801f38ced` used four named states and returned 4 scenarios, 40 rows, 1990 unresolved, and 8 diagnostics. The shared mission evaluation `probability-5c481fe0bf70d3500330b0e9` returned 4 scenarios, 216 rows, 486 unresolved, and 20 diagnostics. The crisis mission evaluation `probability-ae22241da437afca779b68c5` returned 4 scenarios, 4 rows, 7 unresolved, and 0 diagnostics. All used empty state records and are score-only/bounded.

Generic focus evaluation `E6_FOCUS_SCENARIOS_CURRENT_MAC_2026_08_06` returned analysis `probability-c0b48da4f891d6ab5c2cc666`, scenario hash `cd923df6ccb5c4df2344a109e8a51c64d5c160469f1e31a491fe8bd267a67c35`, 4 scenarios, 736 rows, 1033 unresolved, and an incomplete candidate pool of 184 candidates. Package focus AI adapters and the generic strategy adapter do not provide a complete probability surface.

Event `ai_chance` inspections and evaluations for `events/006_independence_wave.txt`, `events/006_independence_wave_evolution_incidents.txt`, `events/006_independence_wave_form01_02_04.txt`, `events/006_independence_wave_form05.txt`, `events/006_independence_wave_iw043_iw058.txt`, `events/006_independence_wave_iw093_iw098.txt`, `events/006_independence_wave_mediterranean.txt`, `events/006_independence_wave_rhineland_bavaria.txt`, and `events/006_independence_wave_wallonia_frisia.txt` all remained partial with incomplete pools and empty state records. Representative analyses were root `probability-b1341db7e86f8447c22c5434` (4 scenarios/72 rows/23 unresolved), evolution `probability-774a9f1a4ecd36f126814267` (4/40/1), form01/02/04 `probability-8a6c039b53b99bb3fd1e031d` (4/60/22), form05 `probability-e6999b95b1dde63a4fdce591` (4/40/37), and IW043/IW058 `probability-ac629d6245a32753bfc68a8f` (4/272/781).

The `event_mean_time_to_happen` adapter returned the exact blocker `PROBABILITY_SURFACE_EMPTY` for both `common/mtth/006_independence_wave_evolution_mtth.txt` and `common/scripted_effects/006_independence_wave_evolution_effects.txt`. The custom MTTH variable is therefore unresolved by MCP and no timing distribution is claimed.

`common/scripted_effects/006_independence_wave_scenario_effects.txt` returned `PROBABILITY_SURFACE_EMPTY` for direct-random and random-list inspection. The scenario decisions are deterministic navigation over the fixed package registry and do not expose a probability-proportional selection surface.

## Candidate-pool and external-factor discipline

Allocator `random_list` inspections had complete source candidate pools, but named evaluations still lacked runtime state and external modifiers. Decision, mission, focus, and event evaluations had incomplete candidate pools or unresolved required inputs. Every scenario submitted an explicit name and hash, but state was `{}`; no live country, route, prerequisite, target-validity, cooldown, capacity, crisis, or strategy-factor context was asserted. Results are therefore classified as bounded, score-only, or unresolved, never exact selection probabilities.

## Compare, sweep, simulation, and sequence status

`hoi4.probability_compare` was exercised on the Macedonia decision surface. Same-path current-versus-current produced `comparisonChanges=0`, which is only a capability receipt. The route rejects a `revision` field, rejects cached `analysisId`/artifact/source-hash references, and a path suffix such as `@56e72be08^` returns `PROBABILITY_SOURCE_NOT_FOUND`. A valid before/after comparison against the parent commit is therefore blocked, especially because IW-026 files do not exist in the parent revision.

No sweep was run because thresholds and external factors were not declared. No simulation was run because no uncertain input distribution or seed was declared. No sequence was run because no complete custom weighted pool, cadence, cooldown/recovery, cap, removal/reset, timer, or terminal-state contract was declared. Custom-pool inspection returned zero candidates and `poolComplete=false`; source review found no `custom_weighted_pool` construct in Event 006 files.

## Findings and owner recommendations

- Keep the release/balance gate at HOLD/PARTIAL until the same named scenarios are rerun with populated state and external factors.
- Treat the Macedonia never-eligible decision and mission diagnostics as owner follow-up targets, not as proof of a specific fix.
- Do not infer dominance, starvation, timing drift, rank reversal, repetition, or exploit risk from the current empty-state outputs.
- Re-run `probability_compare` after obtaining a revision-capable source route or an explicitly approved snapshot pair; the current adapter cannot prove the IW-026 before/after delta.

No gameplay changes were applied by this audit.
