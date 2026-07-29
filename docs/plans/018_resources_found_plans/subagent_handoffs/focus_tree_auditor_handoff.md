# Event 018 DHO Focus-Tree Audit and Patch Handoff

Date: 2026-07-11  
Mode: patch-capable focus-tree audit; no commit  
Scope: the final live 65-focus Oth-Kesh package and its directly consumed ideas, effects, decisions, AI, units, localisation, and country documentation  
Status: **gameplay/static focus audit repaired and all 65 focus sprites verified; completion remains open because the separate live idea/state GFX registration pass is still owned by the active icon-asset subagent**

## References followed

This pass used `hoi4-focus-trees` and read the complete Event 018 spec package, focus architecture, active implementation-depth addendum, acceptance/AI/tuning matrices, and cave-country documentation. It also consulted the required offline wiki pages, including National Focus, Idea, and AI modding, the official vanilla script/effect/trigger/AI documentation, and vanilla staged-idea precedents using `swap_ideas`.

## Files changed

- `common/national_focus/018_resources_found_cave_focus_tree.txt`
  - retained all 65 focuses and the accepted graph;
  - routed doctrine and adaptation rewards through cumulative swap helpers;
  - removed write-only focus markers and the no-op template refresh calls;
  - gave Mineral Tithe, Vaults Beneath the Continent, tunnel links, and the Continental Network concrete persistent consumers.
- `common/ideas/018_resources_found_cave_ideas.txt`
  - made every advanced doctrine idea cumulative through named constants;
  - added four route-specific cumulative adaptation ideas;
  - removed the two generic standalone Surface/Sky idea stages that caused stacking.
- `common/scripted_effects/018_resources_found_cave_effects.txt`
  - made hierarchy selection enforce one hierarchy idea and flag;
  - made doctrine/adaptation progression use guarded `swap_ideas` and cleanup;
  - made final adaptation idempotent;
  - consumed tunnel endpoint, converted-industry, coastal-anchor, fortification, vault, and Continental Network state;
  - preserved all three target variables and their independent cleanup paths.
- `common/scripted_effects/018_resources_found_decision_effects.txt`
  - removed the write-only `resources_found_cave_tunnel_link_deepened` marker; the completed project now relies on the linked endpoints' real spawn-location consumer.
- `common/script_constants/018_resources_found_cave_constants.txt`
  - added `resources_found_cave_runtime.anchor_vault_extra_fort_level`.
- `common/units/018_resources_found_cave_broods.txt`
  - set `@CAVE_SCREE_SPEED = -0.45`, so every cave sub-unit speed modifier is negative and even the fastest completed Scree/Open/World Below package remains below the ordinary foot baseline.
- `localisation/english/018_resources_found_system_l_english.yml`
  - added the four new idea keys and exact cumulative doctrine/adaptation descriptions;
  - aligned route, spawn, vault, link, and final-adaptation tooltips with live effects.
- `localisation/english/018_resources_found_decisions_l_english.yml`
  - aligned the tunnel-link project text with bounded endpoint selection and automatic-spawn priority.
- `docs/events/018_resources_found/cave_country.md`
  - documented the one-spirit progression, route-spirit cap, vault lifecycle, linked spawn endpoints, and corrected speed table.

## New and materially changed identifiers

New cumulative adaptation ideas, reusing the existing Surface Senses and Sky-Hardened picture tokens:

- `cave_dense_surface_senses_adaptation`
- `cave_open_surface_senses_adaptation`
- `cave_dense_sky_hardened_adaptation`
- `cave_open_sky_hardened_adaptation`

New helpers/state lifecycle:

- `resources_found_cave_choose_dense_plate_adaptation`
- `resources_found_cave_choose_open_joint_adaptation`
- `resources_found_cave_upgrade_surface_senses_adaptation`
- `resources_found_cave_upgrade_sky_hardened_adaptation`
- `resources_found_cave_deepen_anchor_vaults`
- `cave_deep_anchor_vaults_unlocked`
- `resources_found_cave_anchor_fortifications_built`
- `resources_found_cave_anchor_vaulted`

The following existing helpers were materially changed:

- `resources_found_cave_choose_one_maw`
- `resources_found_cave_choose_many_chambers`
- `resources_found_cave_choose_hoard_the_veins`
- `resources_found_cave_choose_stone_phalanx`
- `resources_found_cave_choose_burrow_war`
- `resources_found_cave_choose_scree_tide`
- `resources_found_cave_unlock_interlocking_carapaces`
- `resources_found_cave_unlock_great_gun_resistance`
- `resources_found_cave_unlock_urban_cellar_networks`
- `resources_found_cave_unlock_split_broods`
- `resources_found_cave_unlock_lighter_plates`
- `resources_found_cave_apply_final_adaptation`
- `resources_found_cave_refresh_anchor_benefits`
- `resources_found_cave_select_spawn_state`
- `resources_found_cave_analyze_enemy_piercing`

Removed write-only/no-op identifiers include `resources_found_cave_refresh_template_access`, `resources_found_cave_locked_templates_loaded`, `cave_interlocking_carapaces`, `cave_resisted_great_guns`, `cave_split_great_broods`, `cave_lighter_plates`, `resources_found_final_template_stone`, `resources_found_final_template_scree`, `cave_origin_fortified`, `cave_tunnel_link_operational`, and the unused direct focus-completion markers. Direct focus flags that remain all have a decision, effect, AI, spawn, or achievement consumer.

## Full route coverage proof

| Surface | Count | Live focuses |
| --- | ---: | --- |
| Emergence trunk | 4 | `DHO_the_first_breach`, `DHO_secure_the_origin_chamber`, `DHO_organize_the_first_war_broods`, `DHO_read_the_surface_veins` |
| One Maw hierarchy | 5 | `DHO_one_maw`, `DHO_central_resonance`, `DHO_directed_war_broods`, `DHO_origin_above_all`, `DHO_the_singular_hunger` |
| Many Chambers hierarchy | 5 | `DHO_many_chambers`, `DHO_local_brood_memory`, `DHO_distributed_command`, `DHO_a_second_deep_capital`, `DHO_the_host_without_a_head` |
| Hoard the Veins hierarchy | 6 | `DHO_hoard_the_veins`, `DHO_mineral_tithe`, `DHO_guard_the_feeding_chambers`, `DHO_refuse_barren_ground`, `DHO_preserve_every_plate`, `DHO_vaults_beneath_the_continent` |
| Shared resource-anchor lane | 7 | `DHO_survey_surface_seams`, `DHO_activate_resource_anchors`, `DHO_build_brood_queues`, `DHO_fortify_the_feeding_state`, `DHO_consume_captured_industry`, `DHO_link_the_chambers`, `DHO_the_continental_network` |
| Doctrine introduction | 2 | `DHO_learn_the_open_sky`, `DHO_read_the_enemy_line` |
| Stone Phalanx doctrine | 6 | `DHO_stone_phalanx`, `DHO_interlocking_carapaces`, `DHO_deliberate_front_advance`, `DHO_resist_the_great_guns`, `DHO_crush_the_fortified_line`, `DHO_the_moving_mountain` |
| Burrow War doctrine | 6 | `DHO_burrow_war`, `DHO_listen_beneath_the_roads`, `DHO_hidden_approach_chambers`, `DHO_undermine_the_rail_junction`, `DHO_urban_cellar_networks`, `DHO_the_front_has_a_floor` |
| Scree Tide doctrine | 6 | `DHO_scree_tide`, `DHO_split_the_great_broods`, `DHO_lighter_plates`, `DHO_follow_the_retreat`, `DHO_swarm_the_crossings`, `DHO_the_hills_begin_to_move` |
| Adaptation lane | 6 | `DHO_study_broken_weapons`, `DHO_grow_denser_plates`, `DHO_open_the_joints`, `DHO_surface_senses`, `DHO_harden_against_the_sky`, `DHO_choose_the_final_adaptation` |
| Continental/world-end lane | 12 | `DHO_mark_the_richest_route` through `DHO_the_world_opens_below` |

The complete count is `4 + 5 + 5 + 6 + 7 + 2 + 6 + 6 + 6 + 6 + 12 = 65`.

The three hierarchy roots are pairwise mutually exclusive. The three doctrine roots are pairwise mutually exclusive. `DHO_link_the_chambers` requires the shared anchor lane plus one hierarchy capstone and one doctrine capstone, using separate AND prerequisite blocks with OR choices inside the route blocks. All prerequisite targets exist, the graph is acyclic, and there are no duplicate coordinates.

## Doctrine and adaptation progression proof

| Route | Base spirit | Intermediate cumulative spirit | Final cumulative spirit |
| --- | --- | --- | --- |
| Stone | `cave_stone_phalanx_doctrine` | `cave_interlocking_carapaces_adaptation` | `cave_great_gun_resistance` |
| Burrow | `cave_burrow_war_doctrine` | — | `cave_urban_cellar_networks_adaptation` |
| Scree | `cave_scree_tide_doctrine` | `cave_split_broods_adaptation` | `cave_lighter_plates_adaptation` |
| Dense adaptation | `cave_dense_plate_adaptation` | `cave_dense_surface_senses_adaptation` | `cave_dense_sky_hardened_adaptation` |
| Open adaptation | `cave_open_joint_adaptation` | `cave_open_surface_senses_adaptation` | `cave_open_sky_hardened_adaptation` |

The advanced idea definitions contain the exact sum of the preceding stages plus the next tradeoff. Their tooltips and descriptions report the same cumulative values. Every transition is guarded, uses `swap_ideas` when the previous stage exists, removes stale earlier stages, and refuses to downgrade a final stage when called again. `resources_found_cave_apply_final_adaptation` calls only the final-stage upgrader and an idempotent Stone/Scree spawn preference; it does not shorten the spawn interval or re-add base/Surface stages.

## Spirit-count proof for every completed route combination

Every completed route has exactly one hierarchy spirit, one doctrine spirit, and one adaptation spirit. The matrix below gives the total focus-created route-spirit count for all 18 hierarchy/doctrine/adaptation combinations.

| Hierarchy | Stone + Dense | Stone + Open | Burrow + Dense | Burrow + Open | Scree + Dense | Scree + Open |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| One Maw | 3 | 3 | 3 | 3 | 3 | 3 |
| Many Chambers | 3 | 3 | 3 | 3 | 3 | 3 |
| Hoard the Veins | 3 | 3 | 3 | 3 | 3 | 3 |

At intermediate points the count is never higher: hierarchy selection removes the other two hierarchy ideas; each doctrine helper removes its previous route stage; each adaptation helper removes its prior and opposite-route stages. Starting biological/economic spirits and the terminal `cave_world_below_network` identity are separate from these three route-spirit families.

## Focus, localisation, icon, AI, and reward audit

Static extraction results:

- 65 focus blocks, 65 unique IDs, 65 unique coordinates;
- 65 `completion_reward` blocks and 65 `ai_will_do` blocks;
- 65 icon references;
- 65 complete title/description/tooltip localisation triplets;
- 15 conditional `available` blocks and no `bypass` blocks;
- no missing prerequisite IDs, no asymmetric mutual exclusions, and no graph cycle;
- every scripted effect called directly by a focus resolves to a live definition;
- every direct focus country flag left in the tree has a real external consumer.

No bypass was added because the conditional focuses are deliberate campaign accomplishments rather than already-satisfied substitutes: a second active capital candidate, observed piercing, an urban campaign, actual air-power observation, broken neighbor ring, captured industrial belt/capital, exact continent progress, valid footholds, Chaos strictly above 1000, and final verification.

AI consumption remains route-specific:

- `resources_found_rich_target_state` owns `resources_found_cave_marked_objective`, consumed by resource-corridor, One Maw, and Scree strategies;
- `resources_found_strongpoint_target_state` owns `resources_found_cave_strongpoint_objective`, consumed by the Stone strongpoint strategy;
- `resources_found_transport_target_state` owns `resources_found_cave_transport_objective`, consumed by the Burrow transport strategy;
- continental capital objectives retain their own state flag and DHO `front_unit_request` strategy;
- hierarchy and doctrine flags still select their corresponding defense/offense plans and automatic brood types;
- tunnel endpoints are now consumed by spawn-state selection once `cave_continental_network` is active.

The known repaired target lifecycles were not collapsed. State-control cleanup clears only the variable/flag belonging to the captured rich, strongpoint, or transport objective. The `.83` counterplay event still sets piercing or hostile-air observations only in the actual response options. The capital observation still comes from capturing a marked capital objective.

Template integration is direct: Evolution IV loads all five locked DHO templates; every spawn string matches the OOB names; all five templates remain `is_locked = yes` and `force_allow_recruiting = no`; doctrine/final-adaptation helpers select Stone, Burrow, or Scree automatic spawns; Feeding Guards require their focus flag. The removed template-refresh helper never changed template state.

All 65 focus DDS files exist at `gfx/interface/goals/018_resources_found/`, match the live focus IDs, and inspect as 94×86 RGBA DDS. The icon subagent's registration block landed before closeout: `interface/018_resources_found.gfx` contains exactly 65 live `GFX_focus_DHO_*` definitions, all 65 focus references resolve, all registered texture files exist, and there are no missing or extra focus tokens. The separate idea/state sprite pass had not landed at closeout: the 20 live Event 018 idea `picture` tokens still had no matching `GFX_idea_*` definitions in that file and remain owned by `chaosx_icon_artist`.

## Balance proof

- Stone final cumulative spirit: +16% attack, +15% planning speed, +14% organization, +32% defense, -23% speed, +8% supply consumption.
- Burrow final cumulative spirit: +13% attack, +25% planning speed, -23% supply consumption, -8% defense, plus the real 120-day transport disruption consumer.
- Scree final cumulative spirit: +45% speed, +10% planning speed, -9% organization, +8% organization recovery, -18% defense, +5% supply consumption.
- Dense final cumulative adaptation: +10% organization, +16% defense, -12% speed, +12% planning speed, +10% maximum planning, +15% reconnaissance, and -20% hostile air-superiority combat effect.
- Open final cumulative adaptation: +18% speed, +10% organization recovery, net 0% defense change after sky-hardening, +12% planning speed, +10% maximum planning, +15% reconnaissance, and -20% hostile air-superiority combat effect.
- Every sub-unit `maximum_speed` modifier is negative: base -45%, Stone -65%, Burrow -30%, Scree -45%, Guard -75%.
- With a 4 km/h foot baseline, the fastest ordinary completed Scree/Open package remains about 2.82 km/h after Slow Blood; even its terminal +15% World Below speed remains about 3.15 km/h. Hoard is slower still.
- Mineral Tithe reduces the spawn interval once by five days; Split Great Broods does the same only on its first actual stage transition. Both respect the existing 15-day floor.
- Standard anchor forts and the extra vault level each have their own state marker, so refreshes and recaptures cannot stack fort levels repeatedly.

## Validation performed

- Parsed all 65 focus blocks and verified unique IDs/coordinates, complete graph references, acyclicity, mutual-exclusion symmetry, reward presence, AI presence, icon references, and localisation triplets.
- Resolved all 47 distinct focus-called Event 018 scripted effects to live definitions.
- Audited the remaining focus-set flags and the focus-helper flag tranche for write-only state; none remains write-only.
- Resolved the advanced idea constants and confirmed the cumulative numeric values listed above.
- Confirmed all five OOB template names, locks, no-recruit settings, and negative sub-unit speed constants.
- Confirmed the touched scripts have balanced scopes and tab indentation, and both touched localisation files retain UTF-8 BOM.

## Simplifications, omissions, and blockers

- No gameplay route, focus, decision unlock, reward, target lifecycle, AI strategy, doctrine stage, adaptation stage, or terminal gate was omitted or replaced with a fallback.
- Focus-icon integration is closed at 65/65. **Remaining asset integration:** the live idea/state `.gfx` block is pending from `chaosx_icon_artist`. Event 018 must not receive a full completion claim until those registrations are rescanned against all 20 live idea `picture` tokens.
- The conditional Stone and Sky gates remain dependent on actual ordinary-country choices in `chaosx.nr18.83`. This preserves the repaired response-driven observation contract, but a campaign in which no participant ever chooses the relevant countermeasure can delay that focus route. No synthetic observation or bypass was added.
- Validation here is static. The parent still owns final integration review and any live-session behavior check it considers necessary; this handoff does not claim engine execution.

No commit was created.
