# Event 014 Local Warlord Focus Implementation Handoff

> **Historical implementation handoff.** The tree-count and asset details in
> this early handoff describe an intermediate draft. Current route counts and
> package status are defined by the consolidated Event 014 focus audit.

## Scope and files

This bounded patch implements the shared local warlord focus tree and its reward effects. It changes only:

- `common/national_focus/014_cannibalism_warlord_focus.txt`
- `common/scripted_effects/014_cannibalism_warlord_focus_effects.txt`
- `docs/plans/014_cannibalism_plans/subagent_handoffs/event014_warlord_focus_implementation.md`

Tree id: `cannibalism_warlord_focus_tree`

Selectable country contract:

- `is_cannibalism_warlord_country = yes`, which requires the Event 014 created-warlord flag and an exact CBA-CBH tag
- `cannibalism_warlord_slot_in_use`
- `cannibalism_warlord_decisions_open`
- no `cannibalism_warlord_slot_release_pending`

The existing country setup also loads this exact tree with `keep_completed = no` only after successful Event 014 warlord creation.

## Exact focus count and identifiers

The tree has exactly 72 focuses. Every focus uses one unique icon id in the exact form `GFX_goal_cannibalism_warlord_<suffix>`, one matching tooltip key `<focus_id>_tt`, one matching reward effect `cannibalism_warlord_focus_<suffix>`, and one `ai_will_do` block.

1. `cannibalism_warlord_survive_the_first_encirclement`
2. `cannibalism_warlord_hold_the_origin_ground`
3. `cannibalism_warlord_repair_the_broken_routes`
4. `cannibalism_warlord_secure_the_first_larder`
5. `cannibalism_warlord_name_the_first_lieutenants`
6. `cannibalism_warlord_the_host_endures`
7. `cannibalism_warlord_seize_the_knives`
8. `cannibalism_warlord_break_the_captains`
9. `cannibalism_warlord_bind_the_guard_to_one_mouth`
10. `cannibalism_warlord_personal_dominion`
11. `cannibalism_warlord_divide_the_first_table`
12. `cannibalism_warlord_recognize_the_captains`
13. `cannibalism_warlord_assign_feeding_districts`
14. `cannibalism_warlord_council_of_hosts`
15. `cannibalism_warlord_free_the_captains`
16. `cannibalism_warlord_mark_the_hunting_grounds`
17. `cannibalism_warlord_share_the_captured_roads`
18. `cannibalism_warlord_no_single_mouth`
19. `cannibalism_warlord_inventory_the_captured_stores`
20. `cannibalism_warlord_secure_the_prisoner_ledger`
21. `cannibalism_warlord_restore_the_taken_workshops`
22. `cannibalism_warlord_organize_battlefield_recovery`
23. `cannibalism_warlord_establish_larder_accounting`
24. `cannibalism_warlord_rapid_consumption`
25. `cannibalism_warlord_short_horizon_larder`
26. `cannibalism_warlord_managed_herds`
27. `cannibalism_warlord_long_larder`
28. `cannibalism_warlord_mobile_larder`
29. `cannibalism_warlord_moving_larder`
30. `cannibalism_warlord_discipline_the_warbands`
31. `cannibalism_warlord_captains_as_officers`
32. `cannibalism_warlord_form_the_feast_cohorts`
33. `cannibalism_warlord_train_the_origin_specialists`
34. `cannibalism_warlord_raise_the_bone_guard`
35. `cannibalism_warlord_battlefield_harvest`
36. `cannibalism_warlord_protect_the_command_body`
37. `cannibalism_warlord_disciplined_feeding_army`
38. `cannibalism_warlord_war_doctrine_of_the_host`
39. `cannibalism_warlord_island_repair_the_ports`
40. `cannibalism_warlord_island_ambush_the_convoys`
41. `cannibalism_warlord_island_train_landing_cadres`
42. `cannibalism_warlord_island_archipelago_hunt`
43. `cannibalism_warlord_siege_fortify_feeding_districts`
44. `cannibalism_warlord_siege_open_the_tunnels`
45. `cannibalism_warlord_siege_take_the_workshops`
46. `cannibalism_warlord_siege_city_that_eats`
47. `cannibalism_warlord_march_seize_wheels_and_mounts`
48. `cannibalism_warlord_march_raid_the_depots`
49. `cannibalism_warlord_march_sabotage_the_rails`
50. `cannibalism_warlord_march_moving_front`
51. `cannibalism_warlord_prison_unite_cells_and_guards`
52. `cannibalism_warlord_prison_infiltrate_the_transfers`
53. `cannibalism_warlord_prison_arm_the_penal_columns`
54. `cannibalism_warlord_prison_lockhouse_network`
55. `cannibalism_warlord_raid_the_neighboring_states`
56. `cannibalism_warlord_mark_the_supply_hubs`
57. `cannibalism_warlord_seize_prisons_and_depots`
58. `cannibalism_warlord_open_the_predatory_corridors`
59. `cannibalism_warlord_shelter_foreign_cells`
60. `cannibalism_warlord_train_network_cadres`
61. `cannibalism_warlord_corrupt_the_enemy_officers`
62. `cannibalism_warlord_synchronized_sabotage`
63. `cannibalism_warlord_read_the_common_signs`
64. `cannibalism_warlord_accept_the_common_symbols`
65. `cannibalism_warlord_open_the_courier_routes`
66. `cannibalism_warlord_regional_common_table`
67. `cannibalism_warlord_copy_the_shared_doctrine`
68. `cannibalism_warlord_divert_the_courier_routes`
69. `cannibalism_warlord_regional_stolen_routes`
70. `cannibalism_warlord_execute_the_couriers`
71. `cannibalism_warlord_fortify_independent_ground`
72. `cannibalism_warlord_independent_regional_host`

## Route coverage

| Required route | Implemented focuses | Count | Status |
| --- | --- | ---: | --- |
| Survival trunk | first encirclement through `the_host_endures` | 6 | Complete |
| Personal Tyranny | `seize_the_knives` through `personal_dominion` | 4 | Complete |
| Feast Council | `divide_the_first_table` through `council_of_hosts` | 4 | Complete |
| Pack Confederacy | `free_the_captains` through `no_single_mouth` | 4 | Complete |
| Larder economy | inventory, ledger, workshop, battlefield recovery, accounting | 5 | Complete |
| Rapid Consumption | `rapid_consumption`, `short_horizon_larder` | 2 | Complete |
| Managed Herds | `managed_herds`, `long_larder` | 2 | Complete |
| Mobile Larder | `mobile_larder`, `moving_larder` | 2 | Complete |
| Military | discipline, officers, Feast Cohorts, specialists, Bone Guard, harvest, command protection, army stage, doctrine | 9 | Complete |
| Island overlay | port, convoy, landing, archipelago endgame | 4 | Complete and origin-gated |
| Siege overlay | districts, tunnels, workshops, city endgame | 4 | Complete and origin-gated |
| March overlay | mobility, depots, rail sabotage, moving-front endgame | 4 | Complete and origin-gated |
| Prison overlay | guards, transfers, penal columns, lockhouse endgame | 4 | Complete and origin-gated |
| Expansion | neighboring raids, hubs, prisons and depots, corridors | 4 | Complete |
| Terror and infiltration | foreign cells, cadres, officer corruption, synchronized sabotage | 4 | Complete |
| Evolution II entry | `read_the_common_signs` | 1 | Complete and Evolution II-gated |
| Alignment | common symbols, courier routes, regional common table | 3 | Complete |
| Manipulation | shared doctrine, diverted couriers, regional stolen routes | 3 | Complete |
| Defiance | courier execution, independent fortification, independent regional Host | 3 | Complete |

Hierarchy, Larder, and network route roots are mutually exclusive. Military doctrine requires one completed hierarchy capstone and one completed Larder capstone. Terror requires both the regional corridor and final local war doctrine. Network routes require the completed terror branch and active Evolution II.

## Exact stable decision-contract flags

The following parent-supplied flags are set in semantically matching completion rewards:

- `cannibalism_warlord_basic_recruitment_open`
- `cannibalism_warlord_feast_cohort_open`
- `cannibalism_warlord_bone_guard_open`
- `cannibalism_warlord_origin_specialist_open`
- `cannibalism_warlord_emergency_reinforcement_open`
- `cannibalism_warlord_state_consumption_open`
- `cannibalism_warlord_state_intensification_open`
- `cannibalism_warlord_mobile_larder_open`
- `cannibalism_warlord_raid_decisions_open`
- `cannibalism_warlord_foreign_cell_open`
- `cannibalism_warlord_network_cadre_open`
- `cannibalism_warlord_synchronized_attack_open`
- `cannibalism_warlord_island_actions_open`
- `cannibalism_warlord_siege_actions_open`
- `cannibalism_warlord_march_actions_open`
- `cannibalism_warlord_prison_actions_open`
- `cannibalism_hierarchy_personal_tyranny`
- `cannibalism_hierarchy_feast_council`
- `cannibalism_hierarchy_pack_confederacy`
- `cannibalism_larder_rapid_consumption`
- `cannibalism_larder_managed_herds`
- `cannibalism_larder_mobile`
- `cannibalism_network_route_alignment`
- `cannibalism_network_route_manipulation`
- `cannibalism_network_route_defiance`

## Additional focus-owned flags

The following exact flags are also exposed. They are all cleared by `cannibalism_warlord_focus_reset_contracts` and should be copied into the parent-owned reusable-slot cleanup:

- `cannibalism_warlord_alignment_endgame_open`
- `cannibalism_warlord_anti_absorption_open`
- `cannibalism_warlord_anti_decapitation_open`
- `cannibalism_warlord_battlefield_harvest_open`
- `cannibalism_warlord_bone_guard_cap_upgraded`
- `cannibalism_warlord_capital_repairs_open`
- `cannibalism_warlord_commune_absorption_open`
- `cannibalism_warlord_confederacy_doctrine_open`
- `cannibalism_warlord_convergence_leverage_open`
- `cannibalism_warlord_council_doctrine_open`
- `cannibalism_warlord_council_votes_open`
- `cannibalism_warlord_courier_routes_open`
- `cannibalism_warlord_defiance_endgame_open`
- `cannibalism_warlord_depot_raids_open`
- `cannibalism_warlord_distributed_recruitment_open`
- `cannibalism_warlord_diverted_couriers_open`
- `cannibalism_warlord_feeding_districts_open`
- `cannibalism_warlord_hidden_anchorages_open`
- `cannibalism_warlord_hierarchy_routes_open`
- `cannibalism_warlord_independent_fortification_open`
- `cannibalism_warlord_island_endgame_open`
- `cannibalism_warlord_landing_operations_open`
- `cannibalism_warlord_larder_accounting_open`
- `cannibalism_warlord_larder_inventory_open`
- `cannibalism_warlord_leader_protection_open`
- `cannibalism_warlord_lieutenant_assignments_open`
- `cannibalism_warlord_managed_herd_actions_open`
- `cannibalism_warlord_manipulation_endgame_open`
- `cannibalism_warlord_march_endgame_open`
- `cannibalism_warlord_mobile_larder_escort_open`
- `cannibalism_warlord_network_cadre_cap_upgraded`
- `cannibalism_warlord_network_manipulation_open`
- `cannibalism_warlord_network_routes_open`
- `cannibalism_warlord_officer_corruption_open`
- `cannibalism_warlord_officer_training_open`
- `cannibalism_warlord_origin_defense_open`
- `cannibalism_warlord_origin_specialist_cap_upgraded`
- `cannibalism_warlord_penal_column_actions_open`
- `cannibalism_warlord_personal_guard_doctrine_open`
- `cannibalism_warlord_predatory_corridors_open`
- `cannibalism_warlord_prison_depot_raids_open`
- `cannibalism_warlord_prison_endgame_open`
- `cannibalism_warlord_prisoner_ledger_open`
- `cannibalism_warlord_provincial_servants_open`
- `cannibalism_warlord_purge_decisions_open`
- `cannibalism_warlord_rail_sabotage_open`
- `cannibalism_warlord_rapid_consumption_open`
- `cannibalism_warlord_relief_ambush_open`
- `cannibalism_warlord_relocation_open`
- `cannibalism_warlord_shared_roads_open`
- `cannibalism_warlord_siege_endgame_open`
- `cannibalism_warlord_state_exhaustion_risk`
- `cannibalism_warlord_submission_preparation_open`
- `cannibalism_warlord_supply_targeting_open`
- `cannibalism_warlord_survival_order_open`
- `cannibalism_warlord_transfer_infiltration_open`
- `cannibalism_warlord_tunnel_operations_open`
- `cannibalism_warlord_tyrant_doctrine_open`
- `cannibalism_warlord_workshop_conversion_open`

## Variables

Focus-owned route and tuning variables that should be reset for every reusable slot incarnation:

- `cannibalism_hierarchy`
- `cannibalism_larder_route`
- `cannibalism_network_route`
- `cannibalism_warlord_consumption_yield_factor`
- `cannibalism_warlord_mobile_larder_yield_factor`

Existing Event 014 meters adjusted by focus rewards and then clamped through the existing Event 014 meter ranges:

- `cannibalism_frenzy`
- `cannibalism_network_alignment`

No focus sets, adds, subtracts, or awards `cannibalism_larder`.

## Idea lifecycle

The tree performs one-for-one swaps. It does not remove `cannibalism_closed_muster_rolls` and defensively restores it if absent.

| Starting idea removed | Route idea added |
| --- | --- |
| `cannibalism_broken_chain_of_command` | `cannibalism_personal_dominion` |
| `cannibalism_broken_chain_of_command` | `cannibalism_council_of_hosts` |
| `cannibalism_broken_chain_of_command` | `cannibalism_no_single_mouth` |
| `cannibalism_first_larder` | `cannibalism_short_horizon_larder` |
| `cannibalism_first_larder` | `cannibalism_long_larder` |
| `cannibalism_first_larder` | `cannibalism_moving_larder` |
| `cannibalism_starving_warband` | `cannibalism_disciplined_feeding_army` |
| `cannibalism_island_host_origin` | `cannibalism_archipelago_hunt` |
| `cannibalism_siege_commune_origin` | `cannibalism_city_that_eats` |
| `cannibalism_march_host_origin` | `cannibalism_moving_front` |
| `cannibalism_prison_host_origin` | `cannibalism_lockhouse_network` |
| `cannibalism_hunted_by_all` | `cannibalism_common_table` |
| `cannibalism_hunted_by_all` | `cannibalism_stolen_routes` |
| `cannibalism_hunted_by_all` | `cannibalism_independent_supremacy` |

`cannibalism_warlord_focus_reset_contracts` removes every route-stage idea before a reused tag begins the first focus. Parent cleanup should perform the same removal before the tree or decisions become visible.

## Scripted effect contract

There are 78 top-level scripted effects in the new effects file:

- 72 reward effects, exactly `cannibalism_warlord_focus_<focus_suffix>` for the 72 focus suffixes listed above
- `cannibalism_warlord_focus_reset_contracts`
- `cannibalism_warlord_focus_refresh_meters`
- `cannibalism_warlord_focus_add_capital_infrastructure`
- `cannibalism_warlord_focus_add_capital_defenses`
- `cannibalism_warlord_focus_add_capital_workshop`
- `cannibalism_warlord_focus_add_capital_port_capacity`

The map helpers construct only in the capital. The Island helper adds port and dockyard capacity. Workshop focuses add one military workshop and one shared slot. Defense focuses add one land-fort level. Route repair focuses add one infrastructure level.

## AI behavior

Every focus has campaign-aware AI. Major choice weights read:

- `cannibalism_warlord_origin` through the four origin flags
- `cannibalism_warlord_personality`
- `num_of_controlled_states`
- `cannibalism_larder`
- `cannibalism_frenzy`
- `cannibalism_network_alignment`
- current war state
- controlled coastal states with a naval base for naval and Mobile Larder choices

Invalid origin and Evolution II branches receive the existing zero factor. Personal Tyranny favors suspicious and hoarding leaders. Feast Council favors Prison Hosts, Feast Captains, and multi-state countries. Pack Confederacy favors March Hosts, Defiant Mouths, and high Frenzy. The three network routes favor Network Disciple, leverage-seeking, and defiant profiles respectively.

## Validation evidence

- Parsed 72 focus blocks, 72 unique focus ids, 72 unique icon ids, 72 completion rewards, 72 tooltip keys, 72 unique reward-effect calls, and 72 AI blocks.
- Verified all 72 reward effects resolve to defined scripted effects.
- Verified one graph root, no missing prerequisites, no prerequisite cycle, and every prerequisite parent placed above its child.
- Verified no duplicate coordinates and symmetrical mutual exclusions for all hierarchy, Larder, and network route roots.
- Verified all 25 parent-supplied decision and route flags are set.
- Verified all 14 supplied route ideas are reached through one-for-one swaps.
- Verified the tree selector combines the Event 014 CBA-CBH identity trigger with active-slot flags.
- Verified the origin branch roots use matching `allow_branch` and `available` gates.
- Verified the network branch uses active Evolution II for both visibility and availability.
- Verified no Hannibal, reveal, Evolution III, unit creation, manpower grant, equipment grant, direct Larder award, or normal-recruitment enablement exists in either gameplay file.

## Remaining integration risks and parent follow-up

1. Localisation and GFX are intentionally outside this patch. The parent must add all 72 title, description, and tooltip keys, plus all 72 exact focus sprite ids and shine entries.
2. Reusable-slot cleanup outside this patch must clear the exact focus-owned flags, variables, and route ideas listed above before decisions open. The first focus select effect performs a defensive reset, but that is later than country setup.
3. The existing country package starts with Closed Muster Rolls, five burden ideas, and one origin idea. This tree preserves the package count through one-for-one swaps. Meeting the focus-tree skill ceiling of three simultaneous package spirits requires consolidation in the ideas and country setup files, which were outside the allowed edit surface.
4. The added unlock flags require the parent decision implementation to consume them with costs, population accounting, Larder spending, equipment checks, caps, cooldowns, and cleanup. The focus tree grants no unit or population reward itself.
5. `allow_branch` is evaluated when the tree loads. Current warlord creation already requires active Evolution II, so the network branch loads correctly. Any future design that creates warlords before Evolution II must reload or dirty the layout when Evolution II activates.

No focus route or requested focus mechanic was simplified in this bounded implementation.
