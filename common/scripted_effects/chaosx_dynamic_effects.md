# chaosx_dynamic_effects

This file documents reusable dynamic scripted effects from `common/scripted_effects/chaosx_dynamic_effects.txt`. The point of these effects is to keep complex variable/meta logic centralized so events can call one reusable block instead of duplicating large script chunks.

## Reuse guidance

Before adding new dynamic logic, check this file and reuse an existing effect if it already matches the behavior. If no effect matches, create a new one in `chaosx_dynamic_effects.txt` and document it here in the same change with: purpose, scope, inputs, defaults, outputs, side effects, and example usage.

## Table of contents

- [modify_value_based_on_chaos_tier](#modify_value_based_on_chaos_tier)
- [damage_buildings_in_random_states](#damage_buildings_in_random_states)
- [modify_state_population_by_percent](#modify_state_population_by_percent)
- [get_random_sea_region](#get_random_sea_region)

## modify_value_based_on_chaos_tier

This effect converts a base value into a chaos-tier-scaled value. It reads the global flag `chaos_tier`, starts from `base_value`, then adds `add_value * tier_bucket` into the result. The produced output is the temp variable `modified_value`. Tier buckets are handled as `0`, `1`, `2`, `3`, and `4` for any tier above 3.

Use this when you want one place to control chaos scaling and keep call sites short. The usual call flow is to set `base_value`, set `add_value`, call the effect, and then consume `var:modified_value` in another effect like `add_popularity`.

Inputs: `base_value` (required), `add_value` (required).  
Output: `modified_value` (temp variable).  

Important: this effect reads `add_value` by name. If a caller sets a different variable name (for example `base_add`), that value is not used by this effect.

Example:

```txt
set_temp_variable = { base_value = 0.10 }
set_temp_variable = { add_value = 0.02 }
modify_value_based_on_chaos_tier = yes
# result in var:modified_value
```

## damage_buildings_in_random_states

This is the heavy reusable block for random sabotage-style damage. It runs in country scope, calculates how many controlled states should be targeted, picks random owned/controlled states that have at least one eligible building type, applies optional population delta for each selected state, and then performs random building-damage rolls. Because building type must be static in `damage_building`, this effect uses `meta_effect` so damage amount can stay dynamic through `[DMG]`.

Use this whenever you need "damage random buildings across random states" behavior. It exists to avoid rewriting a long random-list/meta-effect pipeline in each event.

Inputs you can set before calling:

- `buildings_to_damage_per_state`: how many damage rolls per selected state.
- `percent_of_states_to_target`: fraction of controlled states to process.
- `damage_modifier`: damage amount per roll.
- `state_population_percent`: decimal population delta per selected state (for example `-0.001` is -0.1%).

Default/fallback behavior when values are not provided or are effectively zero:

- `percent_of_states_to_target = 0.1`
- `damage_modifier = 0.25`
- `buildings_to_damage_per_state = 3`
- `state_population_percent` falls back to `-0.001` effective behavior (internal per-thousand fallback is `-1`)

Main result is state building damage plus manpower delta from the state population calculation. The effect also uses temporary helper variables such as `num_controlled_states`, `num_states_to_target`, and `pop_loss`.

Eligible building types currently covered: `infrastructure`, `arms_factory`, `industrial_complex`, `air_base`, `supply_node`, `rail_way`, `naval_base`, `bunker`, `coastal_bunker`, `dockyard`, `anti_air_building`, `synthetic_refinery`, `fuel_silo`, `radar_station`, `rocket_site`, `nuclear_reactor`, `nuclear_reactor_heavy_water`, `commercial_nuclear_reactor`.

Example:

```txt
set_temp_variable = { state_population_percent = -0.001 }
set_temp_variable = { buildings_to_damage_per_state = 3 }
set_temp_variable = { damage_modifier = 0.25 }
set_temp_variable = { percent_of_states_to_target = 0.1 }
damage_buildings_in_random_states = yes
```

## modify_state_population_by_percent

This is a focused state-scope utility for population-to-manpower delta. It converts `state_population_percent` into per-thousand scale, applies fallback behavior when value is too low, computes `pop_loss` from `state_population_k`, then applies it with `add_manpower`. It also logs the computed value for debugging.

Use this when you already have a state scope and only need the population math, without the building-damage pipeline from `damage_buildings_in_random_states`.

Input: `state_population_percent` (optional; decimal fraction like `-0.001`).  
Fallback behavior: defaults to `-0.001` effective result when unset/too low.  
Output/result: manpower change on the current state scope and a debug log line.

Example:

```txt
random_owned_controlled_state = {
 set_temp_variable = { state_population_percent = -0.001 }
 modify_state_population_by_percent = yes
}
```

## get_random_sea_region

This effect picks one sea-region ID from a curated `random_list` and writes it to `global.rand_sea_region`. It is used as a helper before a second step that needs to inject a dynamic region token via `meta_effect`.

Use this when you want a reusable random sea region selector that can feed dynamic effects such as mine placement or region-based operations.

Input: none.  
Output: `global.rand_sea_region`.

Some IDs are intentionally repeated in the list, which gives those regions more weight than single-entry regions.

Example:

```txt
hidden_effect = { get_random_sea_region = yes }
meta_effect = {
 text = {
  add_mines = { region = [SEA_REGION] amount = 1000 }
 }
 SEA_REGION = "[?global.rand_sea_region|.0]"
}
```
