# Event 013 family decision objective patch handoff

## Changed files

- `common/decisions/013_natural_disasters_decisions.txt`
- `common/script_constants/013_natural_disasters_constants.txt`
- `common/scripted_effects/013_natural_disasters_effects.txt`
- `localisation/english/013_natural_disasters_l_english.yml`

`common/decisions/categories/013_natural_disasters_categories.txt` was inspected and left unchanged.

## Changed decision and mission ids

- `nd_flood_clear_the_river_rail_belt_mission`
- `nd_cyclone_reopen_the_main_harbor_mission`
- `nd_severe_storm_restore_the_storm_cut_roads_mission`
- `nd_hail_protect_the_harvest_line_mission`
- `nd_wind_reopen_the_wind_cut_supply_line_mission`
- `nd_corridor_keep_the_corridor_connected_mission`
- `nd_seismic_clear_the_rubble_belt_mission`
- `nd_rupture_hold_the_rupture_line_mission`
- `nd_tsunami_shelter_the_coastal_belt_mission`
- `nd_volcano_secure_the_ashfall_zone_mission`
- `nd_massive_eruption_hold_the_eruption_ring_mission`
- `nd_firefront_contain_the_firefront_mission`
- `nd_drought_stabilize_the_water_table_mission`
- `nd_heat_keep_the_grid_alive_mission`
- `nd_winter_hold_the_fuel_line_mission`
- `nd_dust_hold_the_dust_belt_mission`
- `nd_landslide_clear_the_buried_pass_mission`
- `nd_slope_secure_the_slope_line_mission`
- `nd_skyfall_stabilize_the_skyfall_field_mission`
- `nd_meteor_storm_survive_the_meteor_barrage_mission`
- `nd_famine_displacement_shelter_refugee_columns_mission`

## Changed helper and tuning ids

- `natural_disasters_objective_type`
- `natural_disasters_pay_rail_bridge_cost`
- `natural_disasters_pay_corridor_forecast_cost`
- `natural_disasters_pay_port_convoy_cost`
- `natural_disasters_pay_airfield_cost`
- `natural_disasters_pay_firebreak_cost`
- `natural_disasters_pay_water_food_cost`
- `natural_disasters_pay_pass_rescue_cost`
- `natural_disasters_pay_crater_cordon_cost`
- `natural_disasters_pay_fuel_line_cost`
- `natural_disasters_pay_harvest_airfield_cost`
- `natural_disasters_apply_family_objective_success`
- `natural_disasters_apply_family_objective_failure`
- `natural_disasters_cleanup_family_objective_packet`

## Localisation keys added

- `nd_cost_rail_bridge_text`
- `nd_cost_corridor_forecast_text`
- `nd_cost_port_convoy_text`
- `nd_cost_airfield_text`
- `nd_cost_firebreak_text`
- `nd_cost_water_food_text`
- `nd_cost_pass_rescue_text`
- `nd_cost_crater_cordon_text`
- `nd_cost_fuel_line_text`
- `nd_cost_harvest_airfield_text`

Each key has matching `_blocked` and `_tooltip` entries.

## Before behavior

Most selectable aftermath missions used the same relief cost, paid the same relief helper, and routed through a shared recovery success or failure path. Mission names referenced ports, rail, ash, firebreaks, fuel, crater fields, and passes, but those predicates did not materially change the cost, success handling, failure handling, or cleanup.

## After behavior

All 21 selectable missions now set `natural_disasters_objective_type_id` on success and failure. Family packets use distinct non-political costs and effects:

- Flood and wind missions spend trains, support equipment, fuel, and command power to restore rail or supply belts.
- Cyclone uses convoy, fuel, support equipment, and navy XP to reopen ports.
- Severe storm, dust, and volcanic ash objectives use air XP and support equipment for airfield or ash clearance.
- Hail uses infantry equipment, support equipment, and air XP for harvest and airfield protection.
- Corridor storm uses trains, support equipment, fuel, and air XP for forecast and rail continuity.
- Earthquake and rupture missions use bridge and rail objective handling, with aftershock and rupture cleanup.
- Tsunami and heat use shelter objectives.
- Massive eruption and drought use water and food route objectives.
- Wildfire uses a firebreak objective with motorized equipment, fuel, manpower, and command power.
- Winter uses a fuel-line objective with trains, support equipment, fuel, and war support.
- Landslide and slope collapse use pass rescue objectives.
- Skyfall and meteor storm use crater cordon objectives.
- Famine displacement uses water and food objective routing.

The shared success helper now clears or advances family predicates such as floodwater, aftershock watch, ashfall, firefront aftermath, water and food pressure, fuel line pressure, pass rescue, and crater aftermath. The failure helper records failed objective state, opens displacement pressure where relevant, and forces follow-up family pressure based on the failed objective or family.

## Validation

- Counted 21 selectable missions and 42 objective-type assignments, meaning each mission has an objective type on both success and failure.
- Confirmed no selectable mission is missing `natural_disasters_objective_type_id`.
- Checked brace balance on the touched decision, effect, and constants scripts.
- Checked the touched scripts for unsupported `<=` and `>=` operators.
- Confirmed the Event 013 English localisation file still has UTF-8 BOM.

## Remaining risks and incomplete items

- This patch clears the decision and mission depth issue from the prior audit. It does not claim full Event 013 completion.
- Broader addendum items remain outside this patch: target scoring, warning variance, Evolution II and III chain controllers, scripted GUI animation surface, achievement predicate rewiring, and news routing.
- Existing worktree changes outside the owned files were present and were not reverted or modified by this patch.
