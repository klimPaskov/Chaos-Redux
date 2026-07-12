# Event 014 Unified CBL Focus Implementation Handoff

## Scope and ownership

This bounded patch implements the complete ordinary, post-reveal unified-country focus graph and its isolated reward-effect layer. It changes only:

- common/national_focus/014_cannibalism_unified_focus.txt
- common/scripted_effects/014_cannibalism_unified_focus_effects.txt
- docs/plans/014_cannibalism_plans/subagent_handoffs/event014_unified_focus_implementation.md

Tree id: cannibalism_unified_focus_tree

The tree selector, the root allow_branch, and the root available block all require the same identity:

- tag = CBL
- has_country_flag = cannibalism_unified_country
- has_global_flag = cannibalism_reveal_complete
- NOT = { has_country_flag = cannibalism_wendigo_hannibal_country }

All other nodes descend from CBL_reveal_the_command. The ordinary unified tree therefore has no pre-reveal player-facing surface and cannot be selected by the Wendigo-Hannibal country.

The parent remains the owner of localisation, sprites and DDS files, idea definitions, decision and mission implementations, shared Event 014 transactions, the ordinary terminal helper, super-event wiring, package documentation, spreadsheet alignment, and final audits.

## Exact focus count and identifiers

The tree contains exactly 108 manually authored focuses. Every identifier below has:

- one unique focus id
- icon GFX_goal_<focus_id>
- title key <focus_id>
- description key <focus_id>_desc
- tooltip key <focus_id>_tt
- reward effect cannibalism_unified_focus_<focus id without CBL_>
- an owned ai_will_do block

### Opening convergence: 8

1. CBL_reveal_the_command
2. CBL_summon_the_warlords
3. CBL_choose_the_first_command_capital
4. CBL_audit_the_submitted_hosts
5. CBL_bind_the_network_territories
6. CBL_settle_the_host_question
7. CBL_open_the_continental_ledger
8. CBL_establish_the_first_continental_command

### Warlord disposition: 15

9. CBL_keep_the_lieutenants
10. CBL_seat_the_regional_governors
11. CBL_preserve_the_origin_commands
12. CBL_arbitrate_the_captains
13. CBL_council_of_retained_hosts
14. CBL_break_the_warlords
15. CBL_seize_the_hidden_hoards
16. CBL_dissolve_the_regional_commands
17. CBL_appoint_the_bone_officers
18. CBL_authority_without_rivals
19. CBL_chain_the_rivals
20. CBL_take_their_heirs
21. CBL_levy_hostage_tribute
22. CBL_rotate_the_hostage_governors
23. CBL_dominion_of_chains

### Supreme hierarchy: 15

24. CBL_one_command
25. CBL_standardize_host_ranks
26. CBL_centralize_the_larder_quota
27. CBL_command_without_distance
28. CBL_the_single_operational_will
29. CBL_many_jaws
30. CBL_charter_the_regional_hosts
31. CBL_divide_the_campaign_theaters
32. CBL_covenant_of_mutual_predation
33. CBL_confederation_under_one_name
34. CBL_ritual_administration
35. CBL_codify_the_feeding_law
36. CBL_ordain_the_punishment_tables
37. CBL_census_of_mouths_and_chains
38. CBL_the_state_of_the_last_table

### Continental Larder: 23

39. CBL_central_accounting
40. CBL_classify_the_consumption_states
41. CBL_build_the_storage_network
42. CBL_boards_of_captured_industry
43. CBL_continental_larder_doctrine
44. CBL_burn_through_the_near_states
45. CBL_feed_the_legion_surge
46. CBL_exhaust_the_frontier
47. CBL_short_horizon_continent
48. CBL_preserve_the_working_herds
49. CBL_rotate_the_feeding_districts
50. CBL_police_the_long_harvest
51. CBL_managed_continental_reserve
52. CBL_prisoner_trains
53. CBL_escort_the_larder_columns
54. CBL_oceanic_hulk_routes
55. CBL_the_larder_that_moves
56. CBL_mark_the_battlefield_yields
57. CBL_recovery_battalions
58. CBL_convert_the_captured_hospitals
59. CBL_harvest_follows_victory
60. CBL_continents_as_supply_regions
61. CBL_abolish_the_old_supply_ceiling

### Army: 14

62. CBL_integrate_the_warbands
63. CBL_map_the_origin_templates
64. CBL_standardize_captured_calibers
65. CBL_raise_the_cannibal_legions
66. CBL_legion_reinforcement_tables
67. CBL_legions_of_the_continents
68. CBL_bone_guard_command
69. CBL_shield_the_supreme_body
70. CBL_breach_the_enemy_capitals
71. CBL_enemy_collapse_doctrine
72. CBL_harvest_the_rout
73. CBL_break_the_retreating_fronts
74. CBL_coordinate_the_three_armies
75. CBL_the_army_that_does_not_end

### Navy: 8

76. CBL_captured_shipyards
77. CBL_raider_flotillas
78. CBL_prison_hulks
79. CBL_convoy_hunt_tables
80. CBL_amphibious_feeding_columns
81. CBL_silent_anchorages
82. CBL_island_command_network
83. CBL_every_ocean_a_corridor

### Air: 7

84. CBL_repair_the_captured_airframes
85. CBL_terror_reconnaissance
86. CBL_interdiction_markers
87. CBL_airborne_cell_insertion
88. CBL_battlefield_recovery_signals
89. CBL_fear_bombing_tables
90. CBL_skies_over_the_larder

### Intelligence and cells: 8

91. CBL_global_courier_network
92. CBL_prison_and_port_cells
93. CBL_corrupt_the_enemy_officers
94. CBL_perfect_the_false_surrender
95. CBL_sleep_beneath_retreat
96. CBL_synchronize_the_uprisings
97. CBL_reactivate_the_cured_networks
98. CBL_the_war_begins_inside

### Continental expansion: 4

99. CBL_read_the_continental_weakness
100. CBL_terror_ultimata
101. CBL_cell_backed_border_incidents
102. CBL_host_theaters_without_borders

### World-hostility counterwar: 4

103. CBL_measure_world_hostility
104. CBL_break_the_relief_corridors
105. CBL_sever_the_coalition_command
106. CBL_consume_the_counterwar

### Ordinary world end: 2

107. CBL_final_global_mobilization
108. CBL_dismantle_the_ordinary_world

## Route coverage and graph contract

| Surface | Structure | Count | Contract |
| --- | --- | ---: | --- |
| Opening convergence | one reveal-gated convergence trunk | 8 | establishes command, territory, ledger, and global mechanic flags |
| Warlord disposition | Keep Lieutenants, Break Warlords, Chain Rivals | 15 | three symmetric mutually exclusive routes, five nodes each |
| Supreme hierarchy | One Command, Many Jaws, Ritual Administration | 15 | three symmetric mutually exclusive routes, five nodes each |
| Continental Larder | five-node trunk, four four-node methods, two-node convergence | 23 | Rapid, Managed, Mobile, and Battlefield methods are mutually exclusive |
| Army | integration, legions, Bone Guard, collapse doctrine, terminal army | 14 | recruitment remains decision-owned and costed |
| Navy | captured shipyards through global corridors | 8 | captured-hull, convoy, fuel, and escort costs remain decision-owned |
| Air | captured airframes through air-network capstone | 7 | captured-aircraft and transport costs remain decision-owned |
| Intelligence | couriers through internal-front capstone | 8 | target caps, exposure, and counterintelligence remain decision-owned |
| Expansion | scoring, ultimata, incidents, global theaters | 4 | war and postwar integration remain parent-owned |
| Counterwar | hostility measurement through coalition conversion | 4 | consumes the world response rather than bypassing it |
| Ordinary terminal | mobilization and final world-end request | 2 | strict readiness and Chaos gates are repeated |

The final mobilization focus has four explicit AND prerequisites:

- CBL_abolish_the_old_supply_ceiling
- CBL_the_army_that_does_not_end
- CBL_host_theaters_without_borders
- CBL_consume_the_counterwar

Those capstones set the four permanent terminal gates. The refresh helper assigns 25 progress for each gate, produces a 0-100 cannibalism_terminal_progress value, and sets both cannibalism_terminal_route_ready and architecture-compatible cannibalism_terminal_route_complete only after all four gates exist on the valid ordinary CBL country.

## Localisation contract

The parent must add 324 focus-localisation keys to localisation/english/014_cannibalism_l_english.yml:

- 108 title keys exactly matching the focus ids above
- 108 description keys exactly <focus_id>_desc
- 108 reward tooltip keys exactly <focus_id>_tt

The file must remain UTF-8 with BOM and keys must not use :0. The title text should preserve the displayed terminology Command, Host, Larder, Frenzy, Bone Guard, Network, and the Last Table. Descriptions must be written as if the system has always existed, with no update-history or implementation wording.

Every tooltip must describe only its current visible result:

- route selections name the mutually exclusive political or Larder commitment
- idea stages name the idea added or upgraded
- decision, mission, or project unlocks name the actual player action family
- map rewards name the bounded building level granted
- risk flags name the matching resistance, exhaustion, exposure, escort, or hostility tradeoff
- recruitment and harvest tooltips state that actions require Larder, equipment, eligible population, state control, caps, and Deaths-accounted transactions
- terminal tooltips state that readiness is rechecked at completion and that the ordinary terminal requires Chaos strictly above the configured threshold

No localisation may claim a free population, Larder, manpower, equipment, ship, aircraft, division, or template reward.

## Focus icon and idea-art contract

For every focus id above, register both:

- sprite: GFX_goal_<focus_id>
- shine sprite: GFX_goal_<focus_id>_shine

Use texture path gfx/interface/goals/014_cannibalism/goal_<focus_id>.dds and register the sprites in interface/014_cannibalism.gfx. Each of the 108 DDS files must be unique final art, not a recolour-only duplicate.

Branch art direction:

| Branch | Stable visual family |
| --- | --- |
| Opening | black command tables, red map threads, first public seal |
| Keep Lieutenants | retained insignia, regional chairs, bound banners |
| Break Warlords | broken crowns, seized hoards, bone officers |
| Chain Rivals | iron chains, hostage seals, tribute ledgers |
| One Command | single standard, centralized quota, distant command lines |
| Many Jaws | several jaws around one map, host charters, divided theaters |
| Ritual State | feeding law tablets, punishment tables, ritual census |
| Rapid Larder | flame, stripped districts, short-horizon maps |
| Managed Larder | fenced districts, rotation ledgers, guarded reserves |
| Mobile Larder | prisoner trains, escort columns, ocean hulks |
| Battlefield Larder | casualty markers, recovery teams, captured hospitals |
| Army | integrated warbands, standardized calibers, legions, Bone Guard |
| Navy | captured yards, raider hulls, prison hulks, silent anchorages |
| Air | repaired airframes, target markers, airborne couriers, fear bombing |
| Cells | courier threads, prison and port nodes, false surrender papers |
| Expansion | continental weakness maps, ultimata, border-cell incidents |
| Counterwar | broken relief corridors and severed coalition command |
| Terminal | four-gate mobilization seal and the ordinary world dismantled |

The 20 parent-owned idea icons below use picture = <idea id>, sprite GFX_idea_<idea id>, and texture gfx/interface/ideas/014_cannibalism/idea_<idea id>.dds.

## Exact idea lifecycle

CBL_establish_the_first_continental_command retires cannibalism_unified_command_burden. The tree then keeps at most one disposition idea, one hierarchy idea, and one Larder-method idea, for a maximum of three simultaneous focus-owned spirits.

| Family | Route root adds | Capstone replaces it with |
| --- | --- | --- |
| Disposition: keep | cannibalism_retained_lieutenants | cannibalism_council_of_retained_hosts |
| Disposition: break | cannibalism_warlords_broken | cannibalism_authority_without_rivals |
| Disposition: chain | cannibalism_rivals_in_chains | cannibalism_dominion_of_chains |
| Hierarchy: central | cannibalism_one_command | cannibalism_single_operational_will |
| Hierarchy: confederate | cannibalism_many_jaws | cannibalism_confederation_under_one_name |
| Hierarchy: ritual | cannibalism_ritual_administration | cannibalism_state_of_the_last_table |
| Larder: rapid | cannibalism_rapid_continental_larder | cannibalism_short_horizon_continent |
| Larder: managed | cannibalism_managed_continental_larder | cannibalism_managed_continental_reserve |
| Larder: mobile | cannibalism_mobile_continental_larder | cannibalism_larder_that_moves |
| Larder: battlefield | cannibalism_battlefield_continental_larder | cannibalism_harvest_follows_victory |

All 20 ideas must be defined under the country idea category in common/ideas/014_cannibalism_ideas.txt with:

- allowed = { is_cannibalism_unified_country = yes }
- allowed_civil_war = { always = yes }
- title key exactly matching the idea id
- description key exactly <idea id>_desc
- tuning sourced from the Event 014 script-constant file, not inline values

Balance direction is contractual even though the constants remain parent-owned: Keep Lieutenants trades direct control for regional command depth; Break Warlords gains direct authority but creates revolt and character losses; Chain Rivals gains tribute and flexible governors but carries hostage-management risk; One Command gains planning and reinforcement at distance-control cost; Many Jaws preserves origin breadth but slows central action; Ritual Administration improves long-horizon control while raising organized resistance; Rapid Larder accelerates early military throughput and exhaustion; Managed Larder extends the campaign but costs administration; Mobile Larder improves operational reach but consumes transport, convoy, and fuel capacity; Battlefield Larder scales from real battle receipts and remains capped.

## Variables and exact route enums

The effect layer owns these country variables:

- cannibalism_unified_warlord_disposition: 0 undecided, 1 keep, 2 break, 3 chain
- cannibalism_unified_hierarchy: 0 undecided, 1 one command, 2 many jaws, 3 ritual
- cannibalism_unified_larder_method: 0 undecided, 1 rapid, 2 managed, 3 mobile, 4 battlefield
- cannibalism_unified_authority: initialized from constant:cannibalism_unification.starting_authority and clamped 0-100
- cannibalism_world_hostility: initialized from constant:cannibalism_unification.starting_world_hostility and clamped 0-100
- cannibalism_terminal_progress: rebuilt from the four 25-point terminal gates and clamped 0-100

The Rapid branch may add the existing Event 014 Frenzy gain. The shared clamp helper reuses constant:cannibalism_consumption.frenzy_min and frenzy_max.

The exact permanent route flags are:

- cannibalism_unified_disposition_keep
- cannibalism_unified_disposition_break
- cannibalism_unified_disposition_chain
- cannibalism_unified_hierarchy_one_command
- cannibalism_unified_hierarchy_many_jaws
- cannibalism_unified_hierarchy_ritual
- cannibalism_unified_larder_method_rapid
- cannibalism_unified_larder_method_managed
- cannibalism_unified_larder_method_mobile
- cannibalism_unified_larder_method_battlefield

## Decision and mission contract

The reward effects expose 212 unique country flags. Every flag is set once, so common/scripted_effects/014_cannibalism_unified_focus_effects.txt is the authoritative focus-to-flag mapping and must not be renamed downstream.

The parent decision layer should use these exact category ids and gates:

| Category id | Visibility gate |
| --- | --- |
| cannibalism_unified_command_category | cannibalism_unified_command_category_open |
| cannibalism_unified_warlord_settlement_category | cannibalism_unified_warlord_settlement_category_open |
| cannibalism_unified_larder_category | cannibalism_unified_larder_category_open |
| cannibalism_unified_military_category | cannibalism_unified_warband_integration_open |
| cannibalism_unified_cells_category | cannibalism_unified_cell_category_open |
| cannibalism_unified_campaign_category | cannibalism_unified_campaign_category_open |
| cannibalism_unified_counterwar_category | cannibalism_unified_counterwar_category_open |
| cannibalism_unified_world_end_category | cannibalism_unified_final_global_mobilization_active |

The exact focus-owned category flags are:

- cannibalism_unified_command_category_open
- cannibalism_unified_warlord_settlement_category_open
- cannibalism_unified_larder_category_open
- cannibalism_unified_cell_category_open
- cannibalism_unified_campaign_category_open
- cannibalism_unified_counterwar_category_open

The exact terminal and safety flags consumed by the parent are:

- cannibalism_unified_terminal_larder_gate
- cannibalism_unified_terminal_army_gate
- cannibalism_unified_terminal_expansion_gate
- cannibalism_unified_terminal_counterwar_gate
- cannibalism_terminal_route_ready
- cannibalism_terminal_route_complete
- cannibalism_unified_final_global_mobilization_active
- cannibalism_unified_terminal_consumption_preparation_open
- cannibalism_unified_world_end_focus_complete
- cannibalism_unified_legion_deaths_accounting_required
- cannibalism_unified_battlefield_harvest_caps_required
- cannibalism_unified_rout_harvest_caps_required
- cannibalism_unified_convoy_harvest_caps_required
- cannibalism_unified_legion_cap_active
- cannibalism_unified_legion_cap_upgraded
- cannibalism_unified_bone_guard_cap_active
- cannibalism_unified_bone_guard_cap_upgraded
- cannibalism_unified_uprising_target_cap_active
- cannibalism_unified_rapid_recruitment_cost_scaling_open
- cannibalism_unified_raider_construction_costs_required
- cannibalism_unified_airframe_stockpile_costs_required
- cannibalism_unified_transport_aircraft_costs_required

At minimum, the decision implementation must cover the Part 6 unified action families with exact cannibalism_unified_ prefixed ids: absorb warlord, appoint governor, purge rival, centralize Larder, create cannibal legion, launch continental hunt, seed major enemy army, designate feeding capital, destroy coalition hub, and begin terminal mobilization. More specific projects and missions are gated by the matching _decisions_open, _missions_open, _projects_open, target-pool, risk, cap, cost-required, and package-pending flags in the reward-effect file.

Every recruitment, reinforcement, hull conversion, airframe repair, cell insertion, harvest, captured-hospital conversion, state-consumption, postwar-integration, and terminal-consumption action must:

1. call a reusable scripted trigger for its full cost and map requirements
2. show custom cost and blocked-cost localisation
3. pay Larder, equipment, population, transport, convoy, fuel, command, or target costs before results
4. route all civilian population loss through the canonical Event 014 consumption transaction
5. preserve Deaths-enabled and Deaths-disabled population parity
6. apply caps and cooldowns from script constants
7. expose matching AI logic using the same requirements and costs
8. clean active missions, targets, and transient flags on defeat, invalid scope, global cleanup, or terminal transition

No decision may interpret a focus unlock as a prepaid unit, population, Larder, equipment, ship, aircraft, core, or annexation reward. Continental expansion must select live targets dynamically, create ordinary war or operation state, and perform postwar integration through the parent Event 014 lifecycle. It must not grant mass cores or annex countries directly from the focus reward.

## Reward-effect contract

The effect file has 121 top-level definitions:

- 108 one-to-one focus reward effects
- 13 shared helpers for initialization, clamping, idea-family cleanup, bounded construction, and terminal-progress refresh

Construction is deliberately bounded:

- one infrastructure level in a valid controlled route state
- one land-fort level in the owned and controlled capital
- one civilian or military factory plus one shared slot in the owned and controlled capital
- one air-base level in the owned and controlled capital
- one dockyard plus one shared slot in a controlled coastal state

No reward effect creates units, templates, population, manpower, equipment, Larder, ships, aircraft, cores, puppets, annexations, or direct war goals.

## Strict ordinary world-end contract

Both CBL_final_global_mobilization and CBL_dismantle_the_ordinary_world use:

	cannibalism_can_complete_ordinary_world_end = yes
	check_variable = { global.chaos_meter_value > constant:cannibalism_evolution_threshold.world_end_chaos }

The same two checks are repeated in both reward effects. The configured threshold is 1000, so equality is deliberately insufficient.

The final reward then calls cannibalism_try_start_ordinary_world_end = yes. This helper is defined by the Event 014 architecture but is not currently implemented in the repository and was intentionally not duplicated in this bounded file. Parent implementation is a blocking integration dependency. Its exact country-scope contract is:

1. revalidate the ordinary unified identity and cannibalism_can_complete_ordinary_world_end
2. revalidate global Chaos strictly above constant:cannibalism_evolution_threshold.world_end_chaos
3. guard against any existing shared or route-specific world-end state
4. set world_end_cannibalism_ordinary and the shared world_end state exactly once
5. preserve durable Event 014 history while cleaning active runtime, missions, targets, and threat state
6. fire only Event 014's unique ordinary super event and its mapped audio
7. never call Event 002's Wendigo terminal event or set the Wendigo route flags

## AI behavior

Every focus owns an ai_will_do block. The major branch choices and campaign branches read combinations of:

- inherited warlord origin or specialist state
- cannibalism_network_alignment and global Network Reach
- cannibalism_larder and Frenzy
- cannibalism_world_hostility
- controlled-state count
- war and major-war state
- strict ordinary terminal readiness

Invalid mutually exclusive routes are structurally unavailable rather than merely discouraged. Terminal focuses cannot be selected until both the scripted readiness trigger and explicit Chaos condition are true.

## Validation evidence

- Parsed 108 focus blocks, 108 unique focus ids, 108 icon references, 108 tooltip references, 108 reward-effect calls, and 108 AI blocks.
- Verified all 108 reward calls resolve to one of 121 unique scripted-effect definitions.
- Verified one graph root, no missing prerequisites, no prerequisite cycles, no child placed above its prerequisite, no duplicate coordinates, and symmetric mutual exclusions.
- Verified the exact CBL, unified-country, reveal-complete, and no-Wendigo selector contract at the tree and root.
- Verified both terminal focuses and both reward effects repeat the strict readiness trigger and explicit greater-than-1000 Chaos test.
- Verified all referenced script constants and every file-scoped tuning token resolve.
- Verified all 20 route-idea identifiers are reached by a defined add or swap path and the opening convergence retires the starting unified burden before route spirits accumulate.
- Verified the effect layer contains no unit creation, manpower grant, equipment grant, population grant, direct Larder award, core grant, annexation, or war-goal grant.

The parent must still run chaosx_focus_tree_auditor after localisation, ideas, decisions, GFX, and the terminal helper are integrated. No audit slot was available during this bounded parallel tranche.

## Simplifications, omissions, and blockers

No requested focus, route, branch, selector condition, terminal gate, focus tooltip hook, icon hook, reward hook, or AI block was simplified or omitted inside this bounded focus implementation.

The full Event 014 package is not complete until the parent supplies:

1. all 324 focus localisation keys
2. all 108 focus icons and shine sprites
3. all 20 route ideas, localisation, constants, and idea icons
4. all gated decisions, missions, projects, costs, caps, AI, target selection, and cleanup
5. cannibalism_try_start_ordinary_world_end and the unique ordinary super-event path
6. final Event 014 documentation, spreadsheet and presentation alignment
7. focus-tree, decision/mission, localisation, country-package, and event-completion audits

No fallback or weaker substitute was used.
