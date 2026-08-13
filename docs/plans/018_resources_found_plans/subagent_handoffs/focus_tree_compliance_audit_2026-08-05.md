# Event 018 DHO Focus-Tree Compliance Audit

Date: 2026-08-05  
Mode: read-only focus-tree compliance audit with parent-owned narrow source correction  
Scope: `common\national_focus\018_resources_found_cave_focus_tree.txt`, `interface\018_resources_found.gfx`, Event 018 focus localisation, and directly linked focus route contracts.  
Status: **audit complete; no source patch authored by this subagent**

## References and validation surface

This pass followed `AGENTS.md`, `.agents\skills\chaos-redux-focus-trees\SKILL.md`, `.agents\skills\chaos-redux-events\SKILL.md`, `.agents\skills\chaos-redux-decisions-missions\SKILL.md`, `.agents\skills\chaos-redux-event-assets\SKILL.md`, `.agents\skills\chaos-redux-improvement-loop\SKILL.md`, and `.agents\skills\chaos-redux-subagents\SKILL.md`.

The required offline Paradox wiki national-focus, trigger, effect, localisation, scope, modifier, AI, graphical-asset, and character references were consulted alongside the vanilla `triggers_documentation.md`, `effects_documentation.md`, and `script_concept_documentation.md` files.

The current parent worktree includes a vanilla-compatible Stone Phalanx AI correction at `common\national_focus\018_resources_found_cave_focus_tree.txt:591` (`bunker > @cave_ai_fort_level_threshold`) and comments documenting the non-round focus pacing and AI tiers at lines 10-25. Those parent edits were preserved and are not claimed as this subagent's patch.

## Route coverage table

| Route family | Count | Focus identifiers | Audit result |
| --- | ---: | --- | --- |
| Emergence trunk | 4 | `DHO_the_first_breach`, `DHO_secure_the_origin_chamber`, `DHO_organize_the_first_war_broods`, `DHO_read_the_surface_veins` | Complete |
| One Maw hierarchy | 5 | `DHO_one_maw` through `DHO_the_singular_hunger` | Complete; root excludes the other two hierarchy roots |
| Many Chambers hierarchy | 5 | `DHO_many_chambers` through `DHO_the_host_without_a_head` | Complete; candidate gate is deliberate |
| Hoard the Veins hierarchy | 6 | `DHO_hoard_the_veins` through `DHO_vaults_beneath_the_continent` | Complete; rich-anchor route gate is deliberate |
| Shared resource-anchor lane | 7 | `DHO_survey_surface_seams` through `DHO_the_continental_network` | Complete; converges through explicit route and doctrine capstones |
| Doctrine introduction | 2 | `DHO_learn_the_open_sky`, `DHO_read_the_enemy_line` | Complete |
| Stone Phalanx doctrine | 6 | `DHO_stone_phalanx` through `DHO_the_moving_mountain` | Complete; cumulative doctrine spirit and strongpoint objective |
| Burrow War doctrine | 6 | `DHO_burrow_war` through `DHO_the_front_has_a_floor` | Complete; bounded anchor-adjacent transport objectives |
| Scree Tide doctrine | 6 | `DHO_scree_tide` through `DHO_the_hills_begin_to_move` | Complete; cumulative lighter-brood progression |
| Adaptation lane | 6 | `DHO_study_broken_weapons` through `DHO_choose_the_final_adaptation` | Complete; dense/open mutual exclusion and cumulative stages |
| Continental and world-end lane | 12 | `DHO_mark_the_richest_route` through `DHO_the_world_opens_below` | Complete; exact continent and delayed world-end gates |
| **Total** | **65** | All Event 018 DHO focus IDs | Complete |

The parser found 65 unique IDs, 65 unique coordinates, no missing prerequisite targets, no mutual-exclusion asymmetry, and no prerequisite cycle. `DHO_link_the_chambers` uses separate prerequisite blocks correctly: the shared industry lane is required, one of the three hierarchy capstones is required, and one of the three doctrine capstones is required.

## Missing or simplified content

- No requested hierarchy, doctrine, resource, adaptation, continental, or world-end route is missing from the live tree.
- No full route family or large branch redesign is required by this audit.
- The only narrow reward simplification is `DHO_organize_the_first_war_broods` at `common\national_focus\018_resources_found_cave_focus_tree.txt:116-125`. Its helper `resources_found_cave_recruit_commanders` at `common\scripted_effects\018_resources_found_cave_effects.txt:1021` is intentionally empty because `DHO_thessik`, `DHO_orrukesh`, and `DHO_khalvek` are recruited by `history\countries\DHO - Oth-Kesh Host.txt:22-24` before the focus tree can be selected. The tooltip says “Recruits” while the focus does not perform a runtime recruitment; this is a low-priority wording/ownership mismatch, not a missing commander at runtime.
- The 15 `available` gates have no bypass blocks because they represent actual campaign accomplishments: a secondary-capital candidate, battle observations, urban campaign, broken ring, industrial belt, capital capture, exact continent progress, valid footholds, chaos threshold, and delayed world-end verification. No stranded route was proven in the current event/effect contracts.

## Icon coverage table

| Asset surface | Expected | Present | Result |
| --- | ---: | ---: | --- |
| Focus `icon =` references in `018_resources_found_cave_focus_tree.txt` | 65 | 65 | Complete |
| Regular `GFX_focus_DHO_*` registrations in `interface\018_resources_found.gfx:88-152` | 65 | 65 | Complete |
| Shine `GFX_focus_DHO_*_shine` registrations in `interface\018_resources_found.gfx:153-217` | 65 | 65 | Complete |
| Focus DDS files under `gfx\interface\goals\018_resources_found\` | 65 | 65 | Complete |
| DDS dimensions and headers | 94x86 | 65/65 | Complete |
| Duplicate focus texture hashes | 0 | 0 | Complete |

All regular and shine sprite names resolve to the intended focus IDs and every registered texture path exists.

## Localisation and reward mismatch list

- All 65 title keys, all 65 `_desc` keys, and all 65 `_tt` keys resolve in `localisation\english\018_resources_found_system_l_english.yml:276-470`.
- All 65 focus blocks contain `completion_reward`, `ai_will_do`, and `search_filters` blocks.
- The title/description/tooltips match the live route mechanics for hierarchy, anchor, doctrine, adaptation, continental, and terminal focuses.
- `DHO_organize_the_first_war_broods_tt` is the one low-priority mismatch because it describes a recruitment action owned by country history rather than by the completion effect; see the simplification note above.
- The longest tooltips are `DHO_surface_senses_tt`, `DHO_lighter_plates_tt`, and `DHO_urban_cellar_networks_tt`. The rendered review showed no clipping; narrow live UI wrapping remains an unproven presentation risk.

## AI behavior audit

The route roots use route-aware state modifiers rather than flat weights.

| AI route | Focus evidence | Result |
| --- | --- | --- |
| One Maw | `DHO_one_maw` lines 163-168 | Favored for compact hosts and weighted to zero after origin loss |
| Many Chambers | `DHO_many_chambers` lines 249-254 | Favored for broad hosts and threatened origins |
| Hoard the Veins | `DHO_hoard_the_veins` lines 337-342 | Favored by three rich anchors and weighted to zero without a rich reachable state |
| Stone Phalanx | `DHO_stone_phalanx` lines 583-592 | Favored against major enemies and enemy states with `bunker > 2`; the bunker predicate now follows vanilla state-trigger syntax |
| Burrow War | `DHO_burrow_war` lines 684-692 | Favored when the country controls mountain or urban terrain and after piercing is observed |
| Scree Tide | `DHO_scree_tide` lines 783-790 | Favored against non-major enemies and weighted to zero after high piercing is observed |
| Adaptation | `DHO_grow_denser_plates`, `DHO_open_the_joints`, `DHO_harden_against_the_sky` lines 892-953 | Dense/open route preference follows observed piercing; sky hardening requires observed air attack |
| Continental/world end | `DHO_mark_the_richest_route` through `DHO_the_world_opens_below` lines 970-1177 | Progression weights rise through exact campaign gates and terminal verification |

No route-specific AI gap was confirmed. The non-round AI tiers 42, 43, 44, 46, 47, 48, 52, 62, 68, and 78 remain because they preserve ordering among adjacent route/milestone priorities. The parent added a rationale comment at the tuning header rather than flattening distinct priorities into duplicate round values.

## High-priority fixes first

1. **Resolved by parent:** replace the invalid `fort_level` predicate with the vanilla state building trigger `bunker > @cave_ai_fort_level_threshold` at `common\national_focus\018_resources_found_cave_focus_tree.txt:591`.
2. **Resolved by parent:** document the 35/49/70/84/98-day focus-cost bands and the fine-grained AI priority tiers at `common\national_focus\018_resources_found_cave_focus_tree.txt:10-25`, satisfying the focus skill's documented-reason exception without changing route pacing.
3. **No patch required:** retain the current route graph, icon registrations, localisation, and cumulative idea lifecycle.

## Meaningful validation

- A static parser confirmed 65 IDs, 65 coordinates, 65 reward blocks, 65 AI blocks, 65 search filters, 65 regular focus icons, 65 shine icons, and complete title/description/tooltip coverage.
- The graph parser confirmed no missing prerequisite or mutual-exclusion IDs, no asymmetric mutual exclusions, no duplicate coordinates, and no prerequisite cycle.
- The icon audit confirmed 65 existing 94x86 DDS files, no missing paths, no malformed DDS headers, and no duplicate texture hashes.
- The direct focus-effect scan resolved all 47 distinct scripted effects called from focus rewards to live definitions.
- `hoi4.focus_inspect` after the parent correction reported 65 Event 018 focuses and `diagnosticCount = 0`. Its Event 018 layout metrics are bounds x2-26/y0-29, 79 connectors, zero crossings, zero node intersections, zero long connectors, maximum horizontal span 8, and minimum same-row spacing 2.
- `hoi4.focus_render` after the parent correction produced the review artifacts at `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/159ebc59ed04255da2ee88b47edf4ab8ef64359abc980f61896fca0a2241cfe8/be37845947a97b73c350f002bc0bdd998ef3817020525c9622f83cec6c4fec17/018_resources_found_cave_focus_tree.focus.svg` and its paired JSON/source-map artifacts.
- `hoi4.focus_raster` after the parent correction produced the PNG review artifact at `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/786e753c039d3b50e0f0cfd6182a1ed73f625ab670937bf3b5fc29b3fb5a8cb0/3d76b1457015cfbc068a80bc6aa7fd1825874216d3296cf9c70bb8ad05932f2b/018_resources_found_cave_focus_tree.focus.png`.

## Skipped validation and remaining risks

- The global MCP validation remains false because the workspace includes 14 unrelated vanilla generic continuous-focus icon/localisation diagnostics. The Event 018 tree itself has zero MCP diagnostics.
- No Hearts of Iron IV executable was launched, in accordance with repository instructions; live campaign selection, AI behavior, and narrow tooltip wrapping remain user-owned runtime checks.
- The commander-tooltip wording mismatch remains low priority because the commanders are already history-recruited and no runtime leader is missing.

No improvement plan was written because the tree is not shallow, duplicated, or missing a route family. No source gameplay patch was authored by this subagent.
