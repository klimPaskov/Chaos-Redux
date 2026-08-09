# Event 018 DHO Focus Tree Final Current-Source Audit

Audit date: 2026-08-09

Scope: read-only final audit of the current DHO national focus tree for Event 018 (Resources Found). No gameplay, localisation, interface, AI, decision, or other source files were edited. The only file written by this audit is this handoff.

## Source and method

The audited tree is `common/national_focus/018_resources_found_cave_focus_tree.txt`, tree id `018_resources_found_cave_focus_tree`, for DHO with `original_tag = DHO` and `resources_found_cave_country`. The current source contains 67 focus definitions. Related source review covered `common/ai_strategy/018_resources_found_ai_strategy.txt`, `localisation/english/018_resources_found_system_l_english.yml`, `interface/018_resources_found.gfx`, `common/scripted_effects/018_resources_found_cave_effects.txt`, `common/scripted_triggers/018_resources_found_cave_triggers.txt`, `common/decisions/018_resources_found_decisions.txt`, `common/decisions/categories/018_resources_found_categories.txt`, and the Event 018 specification package under `docs/specs/018_resources_found_specs/`.

The required offline Paradox wiki focus, trigger, effect, localisation, scope, decision, event, idea, AI, and national-focus references and the corresponding vanilla documentation were consulted before this source audit. No Hearts of Iron IV executable was launched.

## HOI4 MCP evidence

`hoi4.focus_inspect` was called with `relativePath = common/national_focus/018_resources_found_cave_focus_tree.txt`, `treeId = 018_resources_found_cave_focus_tree`, and `mode = national`. It returned `FOCUS_INSPECTED` in workspace `mod_chaos_redux_ea3b2d67c2c0`, revision `6a99f2c29fb6725b5ff756100ab48692d62654392605fc3ef83fadf79a373182`, with artifact:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6b9316bb7ebd8f8e6af98b5cf5733abc9c313c76a9e7997fb41fc431d5bcf217/7842684e289eaf6c8713ca25f621d5bd925ac8c23376ca15ae55efe351f64efc/focus-inspect.6a99f2c29fb6725b.json`

The inspect result reports 67 focuses, 81 connectors, zero crossings, zero node intersections, zero long connectors, maximum horizontal span 8, maximum vertical span 4, maximum Manhattan span 10, bounds `x = 3..26`, `y = 0..29`, no too-close spacing diagnostics, and layout hash `776a29503fc0a2697f7421e085d3174fbe6fab691b7ac3966e6dd994fe8c3bdd`. The Event 018 tree itself has zero focus-layout diagnostics.

`hoi4.focus_render` was called with the same path/tree/mode and review scale 1.0, horizontal spacing 96, vertical spacing 130, and padding 24. It returned `FOCUS_RENDERED`, layout hash `776a29503fc0a2697f7421e085d3174fbe6fab691b7ac3966e6dd994fe8c3bdd`, at 2400 x 3894 pixels. Returned artifacts were:

- HTML: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/64fdbd02237dfd9e50adc81be31b663a2cf41867d7651d006b061b798c2eb60d/535ee04ced2137e9fda3cf868f3429bd326759fa915dfafbd7e635a8e42080b1/018_resources_found_cave_focus_tree.focus.html`
- SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4da0a205a84e05ed27b9206a4997607c9cefafff9adf4a41c6470181a3559d35/3363049257737a2d9931fd36bbf95c563c4588d905797bc5068b5f475429de78/018_resources_found_cave_focus_tree.focus.svg`
- JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ad5f863b6ee3f3814811e0703e541d25d79244e7f44920343454419bcbcaf249/7fef460c96ee15e8fec4e4319632f218b27b8a93dede390a4526cfc9ed336eb5/018_resources_found_cave_focus_tree.focus.json`
- Source map: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4c225345aa639568ee923a3408805c518df2437f2650042a38a15ca61e8f02b0/e2a26f08e80284b98c1944e7a7860a2b1bf5f79015851cc3d1e4e3d3c441e7f0/018_resources_found_cave_focus_tree.focus.source-map.json`
- Plan: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/62c8279f8e01442c7e1e0238a9afa0b626886c9151273aaa61aedcb8e2fbdd25/dac75133a969065a221f0a23f5c3f48bd5aba7a3793e0ca46436f3489b030b54/018_resources_found_cave_focus_tree.focus.plan.json`

`hoi4.focus_raster` was first submitted with `columns = 24`. National mode rejected that input with `MCP error -32602: Input validation error ... columns too big (max 12) and columns is not valid in national mode`. This was an input validation error, not a timeout or transport failure. The corrected national-mode call (same path/tree/mode and spacing/padding as render, without `columns`) returned `FOCUS_RASTERIZED` with these artifacts:

- PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/aa0bff58715421ff53d7187327b1373098fa90177dabb9599d5e3037c9181181/ed35f1e9968c7cbdff5b455def2107c278dcc789e524cb8367b5a9cd4b409d70/018_resources_found_cave_focus_tree.focus.png`
- HTML: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/119484bbb278027f3b152ce37dc025576a1b4838120b33a4368b0d5330a02839/6af897b8d543e5750e237c801dd34573b1a2e51555fb7aa6fca9a46c5fb34585/018_resources_found_cave_focus_tree.focus.html`
- SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f8d016de9dfa8f879e99d23b8849c60ed5aea2f49f3327974990ea92035a8dc5/3772c0b609ce0c4d8ec9a46da6a28077c22645366f57eb1ef09915b9f4d4b7b2/018_resources_found_cave_focus_tree.focus.svg`
- JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ad5f863b6ee3f3814811e0703e541d25d79244e7f44920343454419bcbcaf249/75e3baf21d49b2e2b9d0fa690582a796405e439cf9aafac6d8321d3bb28422df/018_resources_found_cave_focus_tree.focus.json`
- Source map: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4c225345aa639568ee923a3408805c518df2437f2650042a38a15ca61e8f02b0/6795ef9cc3c28635546bea3d97197d1d2f89e593845cad3fa150ecab27860f64/018_resources_found_cave_focus_tree.focus.source-map.json`
- Plan: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/62c8279f8e01442c7e1e0238a9afa0b626886c9151273aaa61aedcb8e2fbdd25/8bf381b4375210082c5ad1f3ac4ea2efd5f45ca7afd2c8f19f46ddb5169cb6df/018_resources_found_cave_focus_tree.focus.plan.json`

The inspect, render, and raster responses each carried the same 14 global diagnostics from `game:common/continuous_focus/generic.txt`: 13 `FOCUS_ICON_REFERENCE_MISSING` diagnostics for unrelated vanilla continuous focuses and one `FOCUS_LOCALISATION_REFERENCE_MISSING` for `continuous_restrict_freedom_desc`. These are outside Event 018. No Event 018 DHO focus diagnostic, layout error, icon error, or localisation error was reported. The MCP responses also reported inline-file truncation (74 scanned/64 returned for inspect and 73 scanned/64 returned for render/raster); the complete current source was reviewed locally.

## Route coverage

| Lane or route | Current focus ids | Count | Result |
|---|---|---:|---|
| Emergence/origin | `DHO_the_first_breach`, `DHO_secure_the_origin_chamber`, `DHO_organize_the_first_war_broods`, `DHO_read_the_surface_veins` | 4 | PASS |
| One Maw hierarchy | `DHO_one_maw`, `DHO_central_resonance`, `DHO_directed_war_broods`, `DHO_count_every_vein`, `DHO_origin_above_all`, `DHO_the_singular_hunger` | 6 | PASS |
| Many Chambers hierarchy | `DHO_many_chambers`, `DHO_local_brood_memory`, `DHO_distributed_command`, `DHO_chamber_autonomy`, `DHO_a_second_deep_capital`, `DHO_the_host_without_a_head` | 6 | PASS |
| Hoard the Veins hierarchy | `DHO_hoard_the_veins`, `DHO_mineral_tithe`, `DHO_guard_the_feeding_chambers`, `DHO_refuse_barren_ground`, `DHO_preserve_every_plate`, `DHO_vaults_beneath_the_continent` | 6 | PASS |
| Shared resource economy/anchors | `DHO_survey_surface_seams`, `DHO_activate_resource_anchors`, `DHO_build_brood_queues`, `DHO_fortify_the_feeding_state`, `DHO_consume_captured_industry`, `DHO_link_the_chambers`, `DHO_the_continental_network` | 7 | PASS |
| Shared surface opening | `DHO_learn_the_open_sky`, `DHO_read_the_enemy_line` | 2 | PASS |
| Stone Phalanx doctrine | `DHO_stone_phalanx`, `DHO_interlocking_carapaces`, `DHO_deliberate_front_advance`, `DHO_resist_the_great_guns`, `DHO_crush_the_fortified_line`, `DHO_the_moving_mountain` | 6 | PASS |
| Burrow War doctrine | `DHO_burrow_war`, `DHO_listen_beneath_the_roads`, `DHO_hidden_approach_chambers`, `DHO_undermine_the_rail_junction`, `DHO_urban_cellar_networks`, `DHO_the_front_has_a_floor` | 6 | PASS |
| Scree Tide doctrine | `DHO_scree_tide`, `DHO_split_the_great_broods`, `DHO_lighter_plates`, `DHO_follow_the_retreat`, `DHO_swarm_the_crossings`, `DHO_the_hills_begin_to_move` | 6 | PASS |
| Adaptation | `DHO_study_broken_weapons`, `DHO_grow_denser_plates`, `DHO_open_the_joints`, `DHO_surface_senses`, `DHO_harden_against_the_sky`, `DHO_choose_the_final_adaptation` | 6 | CONDITIONAL |
| Continental expansion | `DHO_mark_the_richest_route`, `DHO_break_the_first_ring`, `DHO_consume_an_industrial_belt`, `DHO_take_the_continental_capitals`, `DHO_seal_the_coast`, `DHO_break_continental_coalitions`, `DHO_consume_the_last_resistance`, `DHO_continent_consumed` | 8 | PASS |
| World-end | `DHO_deepen_the_continental_heart`, `DHO_listen_beneath_distant_shores`, `DHO_choose_the_first_rupture`, `DHO_the_world_opens_below` | 4 | CONDITIONAL |

The total is 67 focuses, matching the MCP tree count. The three hierarchy roots (`DHO_one_maw`, `DHO_many_chambers`, `DHO_hoard_the_veins`) are mutually exclusive and share the emergence prerequisite. The three doctrine roots (`DHO_stone_phalanx`, `DHO_burrow_war`, `DHO_scree_tide`) are mutually exclusive and share `DHO_read_the_enemy_line`. The same-block prerequisite lists in `DHO_link_the_chambers` and `DHO_surface_senses` are OR groups under national-focus syntax; this appears intentional (any selected hierarchy/doctrine capstone and either compatible adaptation branch), but should remain explicitly documented because changing a block to separate prerequisites would make mutually exclusive routes impossible.

## Required standalone mechanic verification

| Focus | Source/reward evidence | Distinct mechanic verdict |
|---|---|---|
| `DHO_count_every_vein` (`common/national_focus/018_resources_found_cave_focus_tree.txt:202-216`) | Calls `resources_found_cave_enable_capacity_accounting`, which sets `cave_count_every_vein` and recalculates anchor capacity (`common/scripted_effects/018_resources_found_cave_effects.txt:1139-1144`). When the flag is set, spawn cooldown is reduced by `count_every_vein_spawn_reduction_days = 5` and clamped to `minimum_spawn_interval_days = 15` (`...cave_effects.txt:975-984`; constants `...cave_constants.txt:41-45`). Localisation documents floor(total resources/10) with a cap of 10 divisions per non-origin state. | PASS: standalone accounting/capacity and spawn-reliability effect; not merely a duplicate of Chamber Autonomy. |
| `DHO_chamber_autonomy` (`common/national_focus/018_resources_found_cave_focus_tree.txt:306-322`) | Calls `resources_found_cave_enable_chamber_autonomy`, setting `cave_chamber_autonomy`, extending local-memory grace and refreshing AI targets (`...cave_effects.txt:1146-1150`). Non-origin anchor activation is reduced by `chamber_autonomy_activation_reduction_days = 10` from the 30-day baseline (`...cave_effects.txt:516-527`; constants `...cave_constants.txt:44-45`), and spawn selection prefers active frontier chambers (`...cave_effects.txt:875-922`). | PASS: standalone regional queue/frontier/autonomy effect, separate from Count Every Vein. |

## Icons, localisation, and rewards

| Surface | Evidence | Result |
|---|---|---|
| Focus icons | All 67 focus blocks reference an icon; references are unique. `interface/018_resources_found.gfx` defines 67 focus sprites and 67 matching shine sprites under `gfx/interface/goals/018_resources_found/`. All referenced DDS paths exist. | PASS; no missing or repeated Event 018 focus icon found. |
| Focus title/description localisation | `localisation/english/018_resources_found_system_l_english.yml` contains title and `_desc` keys for all 67 focus ids. | PASS; no missing title/description key found. |
| Focus tooltips | All 67 focus blocks contain a custom `*_tt` tooltip and matching localisation. | PASS; player-facing mechanics are not falling back to generic hover text. |
| Completion rewards | 66 focuses call an Event 018 cave scripted helper; `DHO_guard_the_feeding_chambers` is the deliberate exception, setting `cave_feeding_chamber_guards_unlocked` and documenting the Feeding Guard template unlock in its tooltip. | PASS with one documented flag-driven exception; no generic reward-only branch found. |

The source and localisation contain several authored non-round tuning values (for example 8, 12, 13, 18, 22, 23, 25, 33, and 45 in focus tooltips/effects). These are not an icon or localisation defect, but the focus-tree guidance calls for round authored tuning values unless documented. The current package does not provide a per-value justification in the focus file, so this remains a balance/documentation follow-up rather than a structural failure.

## Prerequisites, availability, bypasses, and mechanic links

The emergence chain is linear. Hierarchy and doctrine exclusion logic is present and consistent with the three-route architecture. Resource, continental, and world-end lanes are connected to their prior lanes and use Event 018 flags/helpers for campaign progress. The file contains no explicit `bypass` blocks. External-state gates therefore depend on `available` conditions and helper-set flags.

The principal route-stranding risk is `DHO_harden_against_the_sky`, gated by `resources_found_cave_has_suffered_air_attack`, followed by `DHO_choose_the_final_adaptation`, which requires it. No focus-local bypass or alternate completion gate is present. Similar enemy-experience gates exist for `DHO_resist_the_great_guns`/`DHO_grow_denser_plates` (piercing enemy) and `DHO_urban_cellar_networks` (urban campaign). These may be intentional scenario gates, but the tree has no fallback if the required experience never occurs.

The continental sequence uses explicit campaign-state availability flags (`resources_found_cave_first_neighbor_ring_broken`, industrial-belt objective, continental-capital capture, near-continent control, origin-continent control). World-end entry is guarded by `resources_found_cave_world_end_route_available`, a cross-continent candidate, the chaos gate, and final `resources_found_cave_world_end_verified` completion. The source-level `DHO_choose_the_first_rupture` availability checks the chaos threshold; helper-side verification is required for the remaining conditions.

Major decision/mechanic links are visible through the focus helper calls and flags consumed by `common/decisions/018_resources_found_decisions.txt` and `common/decisions/categories/018_resources_found_categories.txt`, including anchor activation, brood queues, feeding-chamber guards, industry conversion, chamber links, continental objectives, and world-end verification. No missing focus-local hook was found in the current tree; final runtime consumer validation remains outside this read-only focus audit.

## AI behavior and unresolved probability evidence

Every one of the 67 focuses has an `ai_will_do` block. `common/ai_strategy/018_resources_found_ai_strategy.txt` contains route-aware hierarchy strategies (One Maw concentration, Many Chambers defense, Hoard anchor defense), doctrine strategies (Stone strongpoint assault, Burrow transport assault, Scree weighted assault), capacity/origin recovery, resource-corridor and continental objectives, world-end fronts, and DHO counter-strategies. No branch was found with an absent focus-level AI block or an obviously generic route-only strategy.

Probability-specific MCP evidence is unresolved. A prior `hoi4.probability_inspect` attempt using adapter `national_focus_ai_will_do` and source fields `{ relativePath: common/national_focus/018_resources_found_cave_focus_tree.txt, treeId: 018_resources_found_cave_focus_tree }` was rejected with `MCP error -32602` because those source keys were unrecognized. No valid probability inspect/compare scenario was run after that rejection, so AI balance and route-selection probabilities are CONDITIONAL rather than fully passed. The AI strategy file also contains many authored weights that are not round multiples of five; they need a probability-auditor pass before a hard balance claim.

## Simplifications, omissions, and blockers

- No Event 018 route family is missing: all seven architecture lanes and three hierarchy plus three doctrine choices are represented in the 67-focus tree.
- No Event 018 layout, icon, title/description localisation, or focus-count simplification was made.
- Explicit bypass blocks are absent; the air-attack-gated adaptation route is the highest-priority possible strand.
- Focus-AI probability evidence is incomplete because the attempted probability MCP input schema was rejected; this is an audit limitation, not proof that the AI is balanced.
- The 14 global continuous-focus diagnostics are unrelated to Event 018 and should not be attributed to this tree.
- No live-game or executable validation was run, per scope and repository instructions.

## Recommended fixes, highest priority first

1. Add a safe alternate availability/bypass or documented guaranteed experience path for `DHO_harden_against_the_sky` and `DHO_choose_the_final_adaptation`, and review the piercing/urban experience gates for the same strand risk.
2. Run the correctly shaped `chaosx_ai_probability_auditor`/HOI4 MCP probability workflow for representative One Maw, Many Chambers, Hoard, Stone, Burrow, and Scree scenarios, then compare route-selection weights before claiming AI balance.
3. Document the intended OR semantics for the same-block prerequisites in `DHO_link_the_chambers` and `DHO_surface_senses` so future edits do not accidentally turn compatible route alternatives into impossible AND requirements.
4. Either document the non-round player-facing tuning values or normalize them during a dedicated balance pass; this is not required to repair the current tree layout.
5. Track the unrelated `game:common/continuous_focus/generic.txt` diagnostics separately from Event 018.

## Verdict

**CONDITIONAL PASS for the current Event 018 DHO focus tree.** The MCP-inspected/rendered/rasterized tree is structurally clean at 67 focuses, has complete route coverage, unique wired icons, complete focus title/description/tooltips, distinct Count Every Vein and Chamber Autonomy mechanics, and route-aware focus/strategy AI. A full PASS is withheld because external experience gates have no explicit bypass fallback, the required probability audit did not obtain valid MCP evidence, authored tuning values are not fully justified, and the MCP session reports unrelated global continuous-focus diagnostics. No Event 018-specific MCP structural diagnostic failed.

## Parent disposition after the audit

The route-stranding finding was accepted and fixed. `DHO_harden_against_the_sky` is now a proactive adaptation after `DHO_surface_senses`; it no longer depends on an ordinary country selecting the air-power option in `chaosx.nr18.83`. The focus keeps its cumulative Sky-Hardened mechanical reward and the shared continental/world-end chain keeps its authored connector geometry.

The intended OR semantics for `DHO_link_the_chambers` and `DHO_surface_senses`, and the ordering purpose of the non-round focus AI tiers, are now explicit in `docs/events/018_resources_found/cave_country.md`.

Fresh post-fix MCP inspection, rendering, and rasterization retained 67 focuses, 81 connectors, layout hash `776a29503fc0a2697f7421e085d3174fbe6fab691b7ac3966e6dd994fe8c3bdd`, zero crossings, zero node intersections, zero long connectors, zero too-close same-row pairs, and zero Event 018 diagnostics. The current evidence is recorded in `docs/plans/018_resources_found_plans/018_current_mcp_validation_2026-08-09.md`.

The remaining conditional item is the separately mandated probability audit. The unrelated 14 vanilla continuous-focus diagnostics remain outside Event 018.
