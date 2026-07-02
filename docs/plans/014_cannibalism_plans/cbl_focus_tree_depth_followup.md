# Event 014 CBL Focus Tree Depth Follow-Up

Status: implemented in the Event 014 CBL depth pass.

This plan recorded broad route-depth gaps found during the CBL focus tree audit. The gaps have been folded into `common/national_focus/014_cannibalism_focus_tree.txt`, `common/decisions/014_cannibalism_decisions.txt`, `common/scripted_effects/014_cannibalism_effects.txt`, `common/scripted_triggers/014_cannibalism_triggers.txt`, `common/ai_strategy/014_cannibalism.txt`, localisation, assets, and the Event 014 documentation.

## Current Tree Shape

The implemented `cannibalism_commune_focus_tree` has 36 focuses:

- Opening and consolidation: `cbl_first_table`, `cbl_seal_the_origin_state`, `cbl_night_larder_columns`, `cbl_black_kitchens`
- Command hierarchy: `cbl_council_of_knives`, `cbl_warlord_kitchen`, `cbl_hannibal_discipline`
- Supply economy: `cbl_captured_depot_inventory`, `cbl_field_kitchen_conversions`, `cbl_prisoner_ledger_administration`, `cbl_commune_ration_codes`
- Military branch: `cbl_hunger_column_organization`, `cbl_scavenger_party_mobility`, `cbl_butcher_pack_shock_doctrine`, `cbl_prison_processions`, `cbl_hannibal_cadres`
- Origin expansion: `cbl_silent_anchorages`, `cbl_convoy_ambush_plans`, `cbl_coastal_port_lists`, `cbl_prison_road_route`, `cbl_rail_corridor_hunts`, `cbl_mainland_hunting_corridors`
- Route discipline: `cbl_no_public_feasts`, `cbl_hunting_ground_doctrine`, `cbl_restrained_consumption_registers`, `cbl_runaway_consumption_accounts`, `cbl_empty_larder_war_discipline` after major enemy capitulation
- Network and formable route: `cbl_couriers_between_tables`, `cbl_cannibal_pact_compact`, `cbl_refuse_the_wider_pact`, `cbl_listen_for_hannibal`, `cbl_last_table_preparations`, `cbl_map_the_final_larder`, `cbl_proclaim_the_last_table`, `cbl_controlled_region_projects`, `cbl_world_as_larder_gate`. The solitary route records rival-table proof through the validated map mission before the `Table for One` achievement flag is set.

The focus tree now uses route-specific ideas, division-template spawns, origin gates, AI strategy support, CBL decisions/missions, map validation, claims/wargoals, and post-formation regional projects.

## Expansion Needed

### Command Hierarchy Fork

Implemented command choices after the opening trunk:

- Council of knives: obedience, lower splinter risk, slower expansion, council identity payoff.
- Warlord kitchen: shock units, raid pressure, higher splinter or coup risk.
- Hannibal discipline: hidden or route-locked until the Hannibal or accepted-unifier hook is valid.

These alter later military, supply, and pact choices through route flags, AI weights, ideas, and decision unlocks.

### Origin-Specific Expansion

Replaced the single `cbl_port_harvests` expansion node with origin-aware branches:

- Island origin: island chain raids, silent anchorages, convoy ambushes, landing missions.
- Coastal origin: port seizure, shoreline raids, hospital/prison port targeting.
- Inland origin: prison roads, rail corridors, supply hubs, depot routes.

The branches use state modifiers, claims, war goals, transport/equipment rewards, and Last Table project hooks. They do not grant broad free cores.

### Cannibal Pact Versus Solitary Rampage

Deepened the current `cbl_refuse_the_wider_pact` and Hannibal listener split:

- Pact route: non-aggression or coordination with other cannibal actors, shared couriers, stronger Hannibal takeover risk.
- Solitary route: independent war planning, stronger individual aggression, weaker network discipline.

Decision and AI support are implemented through pact courier missions, solitary border raids, and route-specific AI strategy entries.

### Last Table Formation Route

Turned `cbl_proclaim_the_last_table` into a formation lane rather than only a cosmetic payoff:

- preparation focus group
- visible map requirement decision
- claims or state groups
- integration or consumption projects after formation
- diplomatic reactions and world-threat refresh
- AI safety checks

`cbl_proclaim_the_last_table` now requires the map mission validation flag, and `cbl_controlled_region_projects` unlocks post-formation regional projects.

### Military Branch Depth

Added more than reinforcement rewards:

- hunger column organization
- scavenger party mobility
- butcher pack shock doctrine
- prison procession coercion
- commander or officer unlocks
- night assault or island landing methods

The tree now uses templates, timed missions, decisions, a commander recruit, and route-specific idea upgrades.

### AI Route Planning

Added route-specific focus and strategic AI rather than only baseline `ai_will_do` values:

- prioritize origin survival first
- prefer coastal expansion only with coastal control
- prefer pact when weak or Hannibal exists
- prefer solitary route when strong and isolated
- avoid world-end gate unless the world-end trigger is actually valid

AI support lives in `common/ai_strategy/014_cannibalism.txt` and route-aware `ai_will_do` blocks.

## Acceptance Criteria

- Route coverage table shows opening, command hierarchy, supply economy, military, expansion, pact/solitary, Hannibal, Last Table, and world-end routes as implemented.
- Each major route has at least one mechanical unlock beyond modifiers.
- Expansion creates map or diplomatic consequences.
- Last Table formation is validated through a decision and map-control gate.
- AI has route-aware focus behavior.
- Localisation, icons, idea lifecycles, and docs are updated with every new focus.
