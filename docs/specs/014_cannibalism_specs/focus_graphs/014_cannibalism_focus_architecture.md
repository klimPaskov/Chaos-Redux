# Event 014 Cannibal country focus architecture sketch

This is a design sketch, not an exact in-game coordinate plan.

```text
Opening survival trunk
  secure origin state
  count garrison and prisoners
  choose supply method
  choose command hierarchy

Command hierarchy
  council of knives
    obedience and slower expansion
    animated council seal
  warlord kitchen
    shock units and raid pressure
    higher splinter risk
  Hannibal discipline
    hidden until Hannibal exists
    global courier and elite cadres

Supply and economy
  captured depot inventory
  field kitchen conversions
  convoy ambush plans
  prisoner ledger administration
  hunting-ground extraction
  restrained consumption
  runaway consumption

Military
  hunger columns
  scavenger parties
  butcher packs
  prison processions
  island landing methods
  Hannibal cadres when valid

Expansion
  island chain raids
  port seizure
  prison road route
  mainland hunting corridors
  cannibal pact
  solitary rampage

World threat
  public reveal
  global courier routes
  Last Table formation
  Hannibal takeover if valid
  world-end preparation
```

Implementation should choose exact focus count, coordinates, prerequisites, bypasses, and mutual exclusions while preserving this route logic. Route coverage must be reported before completion.

## Implemented Route Map

The implemented CBL tree uses 36 focuses in `common/national_focus/014_cannibalism_focus_tree.txt`.

- Opening survival trunk: `cbl_first_table`, `cbl_seal_the_origin_state`, `cbl_night_larder_columns`, `cbl_black_kitchens`
- Command hierarchy: `cbl_council_of_knives`, `cbl_warlord_kitchen`, `cbl_hannibal_discipline`
- Supply and economy: `cbl_captured_depot_inventory`, `cbl_field_kitchen_conversions`, `cbl_prisoner_ledger_administration`, `cbl_commune_ration_codes`
- Military: `cbl_hunger_column_organization`, `cbl_scavenger_party_mobility`, `cbl_butcher_pack_shock_doctrine`, `cbl_prison_processions`, `cbl_hannibal_cadres`
- Origin expansion: `cbl_silent_anchorages`, `cbl_convoy_ambush_plans`, `cbl_coastal_port_lists`, `cbl_prison_road_route`, `cbl_rail_corridor_hunts`, `cbl_mainland_hunting_corridors`
- Discipline fork: `cbl_no_public_feasts`, `cbl_hunting_ground_doctrine`, `cbl_restrained_consumption_registers`, `cbl_runaway_consumption_accounts`, `cbl_empty_larder_war_discipline`
- Network and formable routes: `cbl_couriers_between_tables`, `cbl_cannibal_pact_compact`, `cbl_refuse_the_wider_pact`, `cbl_listen_for_hannibal`, `cbl_last_table_preparations`, `cbl_map_the_final_larder`, `cbl_proclaim_the_last_table`, `cbl_controlled_region_projects`
- Terminal gate: `cbl_world_as_larder_gate`

The Empty Larder achievement path requires restrained consumption and `cbl_empty_larder_war_discipline` after a major enemy capitulates. The Last Table route is validated through the `cannibalism_cbl_map_the_last_table` decision and `cannibalism_cbl_last_table_map_mission` before `cbl_proclaim_the_last_table` can form `CBL_LAST_TABLE`. For the solitary achievement path, the successful map mission also records rival-table proof when the world has produced multiple commune declarations.
