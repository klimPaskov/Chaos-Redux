# Event 018 Oth-Kesh Focus-Tree Visual Audit Handoff

Date: 2026-07-25  
Mode: patch-capable visual and icon-wiring audit; no commit  
Scope: `common/national_focus/018_resources_found_cave_focus_tree.txt`, Event 018 focus presentation, `interface/018_resources_found.gfx`, and the Event 018 focus localisation surface  
Status: **visual layout is clean and all 65 focus icons now have matching shine registrations**

## References followed

This pass used `chaos-redux-focus-trees`, `chaos-redux-events`, `chaos-redux-decisions-missions`, `chaos-redux-event-assets`, and `chaos-redux-subagents`. It read `AGENTS.md`, the required offline Paradox wiki pages, the vanilla script and localisation documentation, vanilla `interface/goals.gfx` and `interface/goals_shine.gfx`, and the established Chaos Redux one-line shine registrations in Events 006 and 007. `chaos-redux-improvement-loop` was not used because the tree is not shallow and this pass did not redesign a route family.

## Changed files

- `interface/018_resources_found.gfx`
  - added 65 `GFX_focus_DHO_*_shine` sprite registrations;
  - each shine uses the corresponding 94x86 Event 018 focus DDS and `effectFile = "gfx/FX/buttonstate.lua"`;
  - the regular 65 focus registrations and all 65 new shine registrations are unique.
- `docs/plans/018_resources_found_plans/subagent_handoffs/focus_tree_visual_audit_2026-07-25.md`
  - records this audit, patch evidence, and remaining visual risks.

No focus-tree source or localisation source was changed because the graph and all player-facing focus keys were complete and internally aligned.

## Changed focus identifiers

The 65 changed presentation identifiers are the shine companions for every focus in `018_resources_found_cave_focus_tree`: `DHO_the_first_breach`, `DHO_secure_the_origin_chamber`, `DHO_organize_the_first_war_broods`, `DHO_read_the_surface_veins`, `DHO_one_maw`, `DHO_central_resonance`, `DHO_directed_war_broods`, `DHO_origin_above_all`, `DHO_the_singular_hunger`, `DHO_many_chambers`, `DHO_local_brood_memory`, `DHO_distributed_command`, `DHO_a_second_deep_capital`, `DHO_the_host_without_a_head`, `DHO_hoard_the_veins`, `DHO_mineral_tithe`, `DHO_guard_the_feeding_chambers`, `DHO_refuse_barren_ground`, `DHO_preserve_every_plate`, `DHO_vaults_beneath_the_continent`, `DHO_survey_surface_seams`, `DHO_activate_resource_anchors`, `DHO_build_brood_queues`, `DHO_fortify_the_feeding_state`, `DHO_consume_captured_industry`, `DHO_link_the_chambers`, `DHO_the_continental_network`, `DHO_learn_the_open_sky`, `DHO_read_the_enemy_line`, `DHO_stone_phalanx`, `DHO_interlocking_carapaces`, `DHO_deliberate_front_advance`, `DHO_resist_the_great_guns`, `DHO_crush_the_fortified_line`, `DHO_the_moving_mountain`, `DHO_burrow_war`, `DHO_listen_beneath_the_roads`, `DHO_hidden_approach_chambers`, `DHO_undermine_the_rail_junction`, `DHO_urban_cellar_networks`, `DHO_the_front_has_a_floor`, `DHO_scree_tide`, `DHO_split_the_great_broods`, `DHO_lighter_plates`, `DHO_follow_the_retreat`, `DHO_swarm_the_crossings`, `DHO_the_hills_begin_to_move`, `DHO_study_broken_weapons`, `DHO_grow_denser_plates`, `DHO_open_the_joints`, `DHO_surface_senses`, `DHO_harden_against_the_sky`, `DHO_choose_the_final_adaptation`, `DHO_mark_the_richest_route`, `DHO_break_the_first_ring`, `DHO_consume_an_industrial_belt`, `DHO_take_the_continental_capitals`, `DHO_seal_the_coast`, `DHO_break_continental_coalitions`, `DHO_consume_the_last_resistance`, `DHO_continent_consumed`, `DHO_deepen_the_continental_heart`, `DHO_listen_beneath_distant_shores`, `DHO_choose_the_first_rupture`, and `DHO_the_world_opens_below`.

## Route coverage table

| Route family | Count | Coverage |
| --- | ---: | --- |
| Emergence trunk | 4 | `DHO_the_first_breach` through `DHO_read_the_surface_veins` |
| Hierarchy routes | 16 | One Maw 5, Many Chambers 5, Hoard the Veins 6 |
| Shared resource-anchor lane | 7 | `DHO_survey_surface_seams` through `DHO_the_continental_network` |
| Doctrine introduction | 2 | `DHO_learn_the_open_sky`, `DHO_read_the_enemy_line` |
| Surface-war doctrines | 18 | Stone Phalanx 6, Burrow War 6, Scree Tide 6 |
| Enemy-linked adaptation | 6 | `DHO_study_broken_weapons` through `DHO_choose_the_final_adaptation` |
| Continental and world-end lane | 12 | `DHO_mark_the_richest_route` through `DHO_the_world_opens_below` |
| **Total** | **65** | All focus blocks present in the inspected tree |

The three hierarchy roots are pairwise mutually exclusive. The three doctrine roots are pairwise mutually exclusive. MCP layout inspection found no duplicate coordinates, no crossing connectors, no node intersections, and no long connectors.

## Visual and layout findings

| Check | Result | Evidence |
| --- | --- | --- |
| Focus count | 65 | `hoi4.focus_inspect` tree `018_resources_found_cave_focus_tree` |
| Coordinate bounds | x 2-26, y 0-29 | MCP layout metrics |
| Connectors | 79, with 0 crossings and 0 node intersections | MCP layout metrics |
| Connector span | 0 long connectors, max horizontal span 8, max vertical span 4 | MCP layout metrics |
| Same-row spacing | 36 checked pairs, minimum spacing 2, 0 too-close pairs | MCP layout metrics |
| Render at review scale 1.0 | 2608x2460 | `hoi4.focus_render`, layout hash `fda25197f0592ec2c653232ae5e0ca2c5b73169ad0439120cff20650d480da57` |
| Raster at review scale 0.75 | 1956x1845 | `hoi4.focus_raster`, same layout hash |
| Event 018 layout diagnostics | 0 | MCP inspect, render, and raster filtered to Event 018 |

The trunk starts at the configured initial position `x = 12`, `y = 0`. The hierarchy, anchor, doctrine, adaptation, continental, and world-end families occupy distinct lanes and remain readable at the reduced review scale. There is no confirmed clipping or connector occlusion in the generated artifacts.

## Icon coverage table

| Asset surface | Expected | Present | Result |
| --- | ---: | ---: | --- |
| Focus `icon =` references | 65 | 65 | Complete |
| Regular `GFX_focus_DHO_*` registrations | 65 | 65 | Complete |
| Shine `GFX_focus_DHO_*_shine` registrations | 65 | 65 | Added in this pass |
| Event 018 focus DDS files | 65 | 65 | Complete |
| DDS dimensions | 94x86 each | 65/65 | Matches focus-icon target |
| Duplicate DDS hashes | 0 | 0 | Each focus icon is distinct |

The previous defect was the missing shine companion block. Vanilla National Focus wiring and the established Event 006, Event 007, and Germany custom focus patterns all pair a regular focus sprite with a `_shine` sprite. The new block uses the mod's existing compact `buttonstate.lua` convention rather than introducing a new animation asset family.

## Localisation and reward mismatch list

- All 65 focus IDs have title, `_desc`, and `_tt` keys in `localisation/english/018_resources_found_system_l_english.yml`.
- All 65 `custom_effect_tooltip` references in the focus tree resolve to existing `_tt` keys.
- No title or description key is missing, duplicated, or assigned to the wrong focus ID.
- No focus title or description was changed in this visual pass because the existing strings match their rewards and route roles in the inspected source.
- The longest hover strings are the evolution tooltips `DHO_surface_senses_tt` (284 characters), `DHO_lighter_plates_tt` (269 characters), and `DHO_urban_cellar_networks_tt` (265 characters). The generated render shows no confirmed clipping, but live narrow-width wrapping remains a low-priority presentation risk.

## AI behavior gaps

- All 65 focus blocks contain `ai_will_do`.
- Root and route-capstone weights are route-aware in the existing tree. Hierarchy and doctrine roots use route gates and state-aware modifiers, while anchor, adaptation, continental, and terminal focuses use their existing objective and readiness weights.
- No AI change was necessary for this visual scope. A future balance pass may still review tooltip readability and route weight tuning separately from icon wiring.

## Missing or simplified content

- No focus route, focus reward, prerequisite, mutual exclusion, focus filter, title, description, tooltip, or AI block was omitted or replaced in this pass.
- No bypass was added because the conditional focuses are deliberate campaign gates.
- The new shine registrations use the existing one-line `effectFile = "gfx/FX/buttonstate.lua"` pattern. They do not add vanilla's separate `shine_overlay.dds` animation blocks. This is consistent with the established Chaos Redux custom focus assets, but a future art pass could add bespoke animated shine overlays if the project wants a stronger presentation layer.

## Validation performed

- Parsed the tree and confirmed 65 unique focus IDs, 65 icon references, 65 rewards, 65 AI blocks, and complete title, description, and tooltip coverage.
- Compared focus icon references with `interface/018_resources_found.gfx` and `gfx/interface/goals/018_resources_found/`. All 65 regular sprites, all 65 shine sprites, and all 65 DDS paths resolve.
- Read DDS headers for all 65 focus files. Every file reports 94x86 dimensions.
- Confirmed all 65 DDS hashes are unique.
- Re-ran `hoi4.focus_inspect` after the patch. Event 018 retains 0 diagnostics and the same layout hash.
- Re-ran `hoi4.focus_render` at review scale 1.0. The tree remains 2608x2460 with 0 Event 018 diagnostics.
- Re-ran `hoi4.focus_raster` at review scale 0.75. The tree remains 1956x1845 with 0 Event 018 diagnostics.

The MCP workspace validation remains globally false because it reports 14 unrelated vanilla generic continuous-focus icon/localisation diagnostics. None references Event 018.

## Artifact links

- Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b86daa3ca4520ef1bbf1543d3981a17c2b8149efaa4a4dab896868010154c082/82ae7c17a6c6d853249d0ca3d98a2c660e8752dd3e016d670b0e47a16a3bef85/focus-inspect.25c5f64ad4bf54d8.json`
- Review render SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6738a113e7d15bc37d08c99db7e6c7ecc358ca6de9751c3ba869dcae646364d7/2a2da22a0af5a2544ab0ec59a2658f5b00899692a19f4d5fff5d549db6fab69b/018_resources_found_cave_focus_tree.focus.svg`
- Review raster PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1b18783791ae6a5049990b2c97b2c5c5e1eb7d8258e19b5768a2a7d409565380/f03e47e96a325677712534c45567200147b8ed724d27cd9a417c0357f4b56aeb/018_resources_found_cave_focus_tree.focus.png`

## Remaining route and presentation risks

- MCP cannot prove the live game's narrow tooltip wrap behavior. The three long evolution tooltips listed above are the only visual text risk found in static review.
- The new `_shine` sprites use static source DDS textures with the standard button-state effect. No custom shine-overlay animation was added.
- Workspace-level MCP validation remains blocked by unrelated generic continuous-focus diagnostics. This does not block Event 018 focus inspection, rendering, or rasterization.
- No commit was created. The parent agent owns final review and commit selection.
