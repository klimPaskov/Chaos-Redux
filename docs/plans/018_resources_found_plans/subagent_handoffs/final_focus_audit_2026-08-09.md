# Event 018 DHO cave focus-tree final audit

Audit date: 2026-08-09. Scope: the DHO cave national-focus tree and its direct focus icons, focus localisation, cave ideas, and cave decision/category integration. This is a read-only audit of the source present after `5a59f61a7` (`Refine Event 018 cave focus layout`); the focus source is unchanged by later concurrent commits. No gameplay files were edited by this audit.

## Result

The Event 018 tree is a conditional pass. The engine-shaped focus graph, layout, focus icon inventory, localisation coverage, reward hooks, and direct decision integration are internally coherent. Two architecture labels (`Count Every Vein` and `Chamber Autonomy`) are not present as separate focus IDs, although the implemented branches contain partial/accepted-equivalent central-capacity and distributed-anchor effects. The specification does not contain a source-of-truth disposition explaining that merge, so strict one-to-one route coverage remains unresolved. Route-aware probability evidence is recorded in the AI section below; if that evidence cannot be supplied, the AI portion is source-pass but MCP-incomplete.

## Required references consulted

- `AGENTS.md` and the complete `docs/specs/018_resources_found_specs/` package, including `focus_graphs/cave_host_focus_architecture.md`, `specs/018_resources_found_spec_part_6_focus_tree_and_brood_warfare.md`, `matrices/acceptance_criteria.md`, `matrices/ai_strategy_matrix.md`, `matrices/decision_mission_matrix.md`, and `prompts/resources_found_asset_prompt.md`.
- `.agents/skills/hoi4-focus-trees/SKILL.md`, `.agents/skills/hoi4-decisions-missions/SKILL.md`, `.agents/skills/chaos-redux-events/SKILL.md`, `.agents/skills/chaos-redux-event-assets/SKILL.md`, `.agents/skills/chaos-redux-improvement-loop/SKILL.md`, and `.agents/skills/chaos-redux-subagents/SKILL.md`.
- Offline Paradox wiki pages in `paradox_wiki/`: Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, National focus modding, and AI focuses.
- Vanilla documentation: `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\effects_documentation.md`, `triggers_documentation.md`, `script_concept_documentation.md`, and the related modifiers/localisation documentation. Vanilla precedents inspected were `common\national_focus\afghanistan.txt` (focus structure, `available`, `ai_will_do`, `search_filters`), `common\national_focus\abdacom_shared_branch.txt` (separate prerequisite blocks as AND), and `common\national_focus\germany.txt` (mutual exclusion).

## HOI4 MCP evidence

`hoi4.focus_inspect` was run against `common/national_focus/018_resources_found_cave_focus_tree.txt`, tree `018_resources_found_cave_focus_tree`, mode `national`, with `laneSpacing=2` and `nodeSpacing=2`.

- Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1ba625c8a9cde2add6119ee80f10b02e5ea3082390e56688794773014e89d79a/ea9aaf8dc31c06a7af84d8106e742dba4bf312f6ecf36716d6400ebd225c75cb/focus-inspect.e6d33821cb8ceba0.json`
- Focus count: 65; resolved title count: 65; 79 connectors; layout hash `9898f96a63e4c4f1207e27499800154ea2db4f2bed143a1df5ebedc9a84f10ca`.
- Bounds are x=3..26 and y=0..29. `crossingCount=0`, `nodeIntersectionCount=0`, `longConnectorCount=0`, maximum horizontal span 8, maximum Manhattan distance 10, and minimum same-row spacing 2. The Event 018 tree diagnostic count is 0.

`hoi4.focus_render` was run with the same source/tree/mode and `reviewScale=1`.

- Render HTML: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4014c348523b90cbd14c566bf9a8885b03078eeac0694e4dec8385a15dfd8bad/0650dd7dc2b80113f3f6aef1188173a5bb3d2aadaa7405f694b19ac05191673b/018_resources_found_cave_focus_tree.focus.html`
- Render SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4950a442494a1b61a0b28c713bb22139b0010d15ca32b1ce4cf6b0cfebc410d4/260c356d3ea09acd092fb2f80bdd4dc46e195a745ac8b65d1c23ca63de184eee/018_resources_found_cave_focus_tree.focus.svg`
- Render JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/93bc591f40d9cb9c29f0a27f0056ebbd02c62be7eb707c020eb2ce6f513ae4aa/054dab58cdf96721801fe69fd244c91d1d9aa21f017644549718d12916ca9516/018_resources_found_cave_focus_tree.focus.json`

`hoi4.focus_raster` was then run successfully with `horizontalSpacing=96`, `verticalSpacing=72`, and `padding=12` (the first attempt was rejected by the tool's minimum spacing validation and was retried without touching source).

- Raster PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0214a61dbdc308f65944f52e7b8a8e95ddfcc8c8744c58d267cf5dee8e59e4d7/0d5618780a061eac08d04998ff6b414d28859bc66b1cb2ace3c3efdabad66e5c/018_resources_found_cave_focus_tree.focus.png`
- Raster SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8809e48135a2254d7641891096cfbd042f6eca4aefe4ad9c6a4e8794f60ecc05/8ececdca835547719f841f7c23b634a2706979b655567b39bb1497e3792af00d/018_resources_found_cave_focus_tree.focus.svg`
- Raster JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/93bc591f40d9cb9c29f0a27f0056ebbd02c62be7eb707c020eb2ce6f513ae4aa/1c93ea1224e0bfc1b830d7a8f800aea1ed237a70bd9ae4f0398c5d3891e695c0/018_resources_found_cave_focus_tree.focus.json`
- Raster dimensions: 2376 by 2188.

The MCP workspace's global validation summary still reports 14 blocking diagnostics for unrelated vanilla continuous-focus entries (missing continuous-focus icons/localisation in DEN, ETH, SWI, and generic entries). None points to the Event 018 file, its IDs, or its assets. This is a workspace-level blocker if a clean global MCP validation is required, not an Event 018 tree failure.

## Route coverage

| Spec lane | Implemented focus IDs | Result and evidence |
| --- | --- | --- |
| Opening/emergence | `DHO_the_first_breach`, `DHO_secure_the_origin_chamber`, `DHO_organize_the_first_war_broods`, `DHO_read_the_surface_veins` | PASS. Four-focus trunk opens the hierarchy, resource, doctrine, and adaptation lanes. `common/national_focus/018_resources_found_cave_focus_tree.txt:78-143`. |
| One Maw | `DHO_one_maw`, `DHO_central_resonance`, `DHO_directed_war_broods`, `DHO_origin_above_all`, `DHO_the_singular_hunger` | CONDITIONAL. Route lock, central resonance, directed broods, origin dependency, and capstone are present at `:150-230`; `DHO_one_maw` is mutually exclusive with the other two roots at `:158`. The named `Count Every Vein` group from `focus_graphs/cave_host_focus_architecture.md:86-107` and spec part 6 `:137-161` is not a separate ID. |
| Many Chambers | `DHO_many_chambers`, `DHO_local_brood_memory`, `DHO_distributed_command`, `DHO_a_second_deep_capital`, `DHO_the_host_without_a_head` | CONDITIONAL. Distributed route, local recovery, multi-front command, secondary capital, and capstone are present at `:236-318`; root mutual exclusion is at `:244`. The named `Chamber Autonomy` group from architecture `:109-130` and spec part 6 `:178-202` is not a separate ID. |
| Hoard the Veins | `DHO_hoard_the_veins`, `DHO_mineral_tithe`, `DHO_guard_the_feeding_chambers`, `DHO_refuse_barren_ground`, `DHO_preserve_every_plate`, `DHO_vaults_beneath_the_continent` | PASS. Six-focus rich-anchor route with root lock and guarded/preserved-hoard effects at `:324-425`. |
| Resource economy | `DHO_survey_surface_seams`, `DHO_activate_resource_anchors`, `DHO_build_brood_queues`, `DHO_fortify_the_feeding_state`, `DHO_consume_captured_industry`, `DHO_link_the_chambers`, `DHO_the_continental_network` | PASS. The convergence focus at `:505-520` correctly uses separate prerequisite blocks: `DHO_consume_captured_industry` AND one hierarchy capstone AND one doctrine capstone. This matches the wiki/vanilla AND-versus-OR semantics. |
| Doctrine entry | `DHO_learn_the_open_sky`, `DHO_read_the_enemy_line` | PASS. Shared entry requires the opening trunk and feeds three mutually exclusive doctrines. |
| Stone Phalanx | `DHO_stone_phalanx`, `DHO_interlocking_carapaces`, `DHO_deliberate_front_advance`, `DHO_resist_the_great_guns`, `DHO_crush_the_fortified_line`, `DHO_the_moving_mountain` | PASS. Route lock and route-aware AI are present at `:576-665`; great-gun resistance is combat-gated and the final focus requires both branch prerequisites. |
| Burrow War | `DHO_burrow_war`, `DHO_listen_beneath_the_roads`, `DHO_hidden_approach_chambers`, `DHO_undermine_the_rail_junction`, `DHO_urban_cellar_networks`, `DHO_the_front_has_a_floor` | PASS. Terrain and observed-piercing gates are present at `:677-766`; urban focus requires both branch focuses. |
| Scree Tide | `DHO_scree_tide`, `DHO_split_the_great_broods`, `DHO_lighter_plates`, `DHO_follow_the_retreat`, `DHO_swarm_the_crossings`, `DHO_the_hills_begin_to_move` | PASS. Route lock, branch convergence, non-major preference, and high-piercing zeroing are present at `:777-869`. |
| Adaptation | `DHO_study_broken_weapons`, `DHO_grow_denser_plates`, `DHO_open_the_joints`, `DHO_surface_senses`, `DHO_harden_against_the_sky`, `DHO_choose_the_final_adaptation` | PASS. Dense/open adaptation is a genuine mutual exclusion; surface senses accepts either branch; sky hardening is battle-gated at `:873-978`. |
| Continental/world-end | `DHO_mark_the_richest_route`, `DHO_break_the_first_ring`, `DHO_consume_an_industrial_belt`, `DHO_take_the_continental_capitals`, `DHO_seal_the_coast`, `DHO_break_continental_coalitions`, `DHO_consume_the_last_resistance`, `DHO_continent_consumed`, `DHO_deepen_the_continental_heart`, `DHO_listen_beneath_distant_shores`, `DHO_choose_the_first_rupture`, `DHO_the_world_opens_below` | PASS. State-control, continent, distant-shore, and world-opening gates are present at `:981-1183`; terminal checks are not bypassable by focus completion alone. |

## Missing and simplified content

1. **Medium, strict architecture deviation:** `Count Every Vein` and `Chamber Autonomy` are specified as separate groups with separate mechanical roles, but no corresponding focus IDs exist. The current tree has 65 focuses and preserves the route depth, while `DHO_central_resonance` (`:170-184`), shared `DHO_activate_resource_anchors`/`DHO_build_brood_queues`, and `DHO_local_brood_memory`/`DHO_distributed_command` (`:256-285`) provide partial central-capacity/distributed-anchor equivalents. The acceptance matrix permits an “accepted equivalent” (`matrices/acceptance_criteria.md:282-297`), but no current spec or handoff explicitly records this merge. Parent disposition is required: document the equivalence in the spec/source-of-truth, or add bounded route focuses in a later implementation plan. This audit does not patch gameplay.
2. **Low, visual simplification:** Several lifecycle idea IDs intentionally reuse route-family pictures: `cave_interlocking_carapaces_adaptation` and `cave_great_gun_resistance` use `cave_stone_phalanx_doctrine`; `cave_urban_cellar_networks_adaptation` uses `cave_burrow_war_doctrine`; `cave_split_broods_adaptation` and `cave_lighter_plates_adaptation` use `cave_scree_tide_doctrine`; dense/open surface-senses and sky-hardened ideas use their adaptation-family pictures (`common/ideas/018_resources_found_cave_ideas.txt:228-254,268-315,341-395`). Every referenced picture and DDS exists, so this is not an asset-wiring failure. It is only a deviation if the asset prompt's separate idea-family art direction is treated as mandatory.

No fake vertical branch, repeated generic combat-only branch, broken root mutual exclusion, OR/AND prerequisite error, missing focus icon, or Event 018 MCP layout collision was found.

## Icon coverage

| Surface | Definitions | Registration/assets | Result |
| --- | ---: | --- | --- |
| Focus goals | 65 normal plus 65 shine IDs | `interface/018_resources_found.gfx:101-230`; 65 DDS under `gfx/interface/goals/018_resources_found/` | PASS. All focus textures are 94 by 86 RGBA with non-empty alpha and map one-to-one to focus IDs. |
| Cave ideas | 27 top-level ideas | `common/ideas/018_resources_found_cave_ideas.txt:117-457`; all `picture` IDs resolve through `interface/018_resources_found.gfx:233-268`; 36 referenced-folder DDS assets are present at 64 by 64 RGBA | PASS for wiring. Reuse noted above is a design simplification only. |
| Cave decisions/category | 22 cave decision IDs, six distinct cave decision icons, and one cave category icon | `common/decisions/018_resources_found_decisions.txt:983-1239`; category `common/decisions/categories/018_resources_found_categories.txt:67-76`; GFX registrations in `interface/018_resources_found.gfx:271+` | PASS. Focus unlock flags are consumed by the decision family. |

## Localisation and reward mismatch list

- **No missing focus localisation:** `localisation/english/018_resources_found_system_l_english.yml:277-472` contains 65 title keys, 65 `_desc` keys, and 65 `_tt` keys; the file has a UTF-8 BOM.
- **No confirmed focus reward mismatch:** all focus reward calls resolve to helpers in `common/scripted_effects/018_resources_found_cave_effects.txt`, and current tooltips match their helper effects. In particular, `DHO_organize_the_first_war_broods` calls `resources_found_cave_recruit_commanders`, which recruits `DHO_thessik`, `DHO_orrukesh`, and `DHO_khalvek` in the effect helper (`:1017-1020`); the history file only starting-recruits `DHO_vhorruk`, so this runtime focus reward is intentional.
- Cave idea titles/descriptions and cave decision/category localisation resolve in their direct Event 018 localisation files. The generic `resources_found_refresh_project_estimates_tt` used by the refresh decision is present at `localisation/english/018_resources_found_decisions_l_english.yml:372`.
- Long tooltips (`DHO_surface_senses_tt`, `DHO_lighter_plates_tt`, and `DHO_urban_cellar_networks_tt`) render in MCP without clipping at review scale 1. Narrow live-window wrapping was not tested because the HOI4 executable is not launched by agents.

## AI behavior gaps and evidence

All 65 focus blocks have `ai_will_do`. The route roots and capstones use contextual gates rather than a uniform ladder: One Maw uses small-host preference and zeroes after `cave_origin_lost` (`:163-167`); Many Chambers favors larger hosts or a threatened origin (`:249-253`); Hoard favors rich-anchor conditions and zeroes without the required state (`:337-342`); Stone uses major-enemy/bunker context (`:588-592`); Burrow uses mountain/urban terrain and observed piercing (`:689-692`); Scree favors non-major wars and zeroes under high piercing (`:789-792`); adaptation uses battle observations (`:909-925`, `:951-955`); and the late route uses expansion/world-end readiness (`:1154-1165`).

The mandatory route-aware `chaosx_ai_probability_auditor` pass is the remaining AI evidence dependency for this handoff. Its scenarios must cover the three hierarchy roots, the three doctrine roots, dense versus open adaptation, and continental/world-end focuses, using the same named baseline/compare scenarios. If the auditor returns MCP probability artifacts, append those URIs and its ordering/zero-gate findings here before calling the AI surface complete. If it cannot reach the probability route, retain the source-level findings above but mark weighted AI validation MCP-blocked.

## High-priority follow-up

1. Resolve or explicitly document the `Count Every Vein` and `Chamber Autonomy` accepted-equivalent decision in the Event 018 spec/source-of-truth. This is the only substantive route-coverage deviation found.
2. Append the probability auditor's route-aware MCP evidence and compare result, or record the exact MCP blocker.
3. If the repository requires a clean global MCP gate, triage the 14 unrelated vanilla continuous-focus diagnostics separately; they do not originate in Event 018.
4. User-owned live validation remains: in-game tooltip wrapping, AI selection in a real campaign, and runtime decision availability after focus completion.

## Validation and limits

- Fresh `hoi4.focus_inspect`, `hoi4.focus_render`, and successful `hoi4.focus_raster` evidence is recorded above.
- Static checks found 65 unique focus IDs, 65 focus title/description/tooltip sets, 130 focus normal/shine GFX registrations, and 65 focus DDS files. Direct idea and decision GFX/picture references were resolved against the repository assets.
- `hoi4.focus_rewrite` was intentionally not used because this was a read-only audit. No gameplay source, localisation, GFX, idea, decision, or history file was changed.
- The HOI4 executable was not launched, so live consumer behavior, campaign AI selection, and narrow-window text wrapping remain unverified by design.

Overall status: **CONDITIONAL PASS — layout/assets/localisation/reward/decision surfaces pass; strict route naming and weighted-AI MCP proof remain disposition items.**
