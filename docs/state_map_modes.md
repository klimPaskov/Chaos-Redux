# State Map Modes

This adds two scripted state map modes for crisis visibility without duplicating gameplay logic.

## What was added

1. `contaminated_states_map_mode`
2. `deaths_state_map_mode`

The contamination view reads the live state contamination systems:

- `chem_state_contamination`
- `anthrax_contaminated_state`
- `plague_contaminated_state`
- `tularemia_contaminated_state`
- `smallpox_contaminated_state`
- `nuclear_fallout_state`

The deaths view reads cumulative state-level civilian deaths from `chaos_state_civilian_deaths_total`, which is now written directly by the shared chaos-meter death registration pipeline whenever a civilian death source also reduces state population.

## Contamination map mode

The contamination map mode uses distinct hazard colors:

- Chemical: amber
- Disease: green
- Nuclear: cyan-blue

If a state carries more than one hazard category at once, the map mode blends those colors additively and switches to a brighter pulsing border so overlap is obvious at a glance.

The map mode updates daily, which keeps it in sync with timed contamination expiry without needing separate refresh hooks in every chemical, biological, and nuclear effect path.

## Civilian deaths map mode

The deaths map mode is a heat map based on cumulative recorded civilian deaths per state.

The data flow is:

1. A death source sets the normal chaos-meter state death inputs.
2. `chaos_meter_register_state_civilian_deaths_percent` calculates the death amount.
3. `chaos_meter_register_deaths` applies the state population loss.
4. The same effect now also adds the loss to `chaos_state_civilian_deaths_total`.
5. If that state total exceeds the global peak, `global.chaos_state_civilian_deaths_map_max` is updated.
6. The map mode colors each state relative to the current global peak so the hottest state is always clearly visible.

This keeps the feature dynamic and easy to extend. Any future civilian-death source that already uses the shared chaos-meter registration path will automatically appear on the map without extra map-view-specific logic.

## Files

- Map mode definitions: `common/map_modes/chaosx_state_map_modes.txt`
- Map mode constants: `common/script_constants/state_map_modes_constants.txt`
- Reusable map mode triggers: `common/scripted_triggers/chaosx_dynamic_triggers.txt`
- Tooltip scripted localisation: `common/scripted_localisation/chaosx_scripted_localisation_map_modes.txt`
- Icon sprite definitions: `interface/chaosx_map_modes.gfx`
- English localisation: `localisation/english/chaosx_map_modes_l_english.yml`

## Icons needed

The button icons are already wired. Replace these placeholder files later with final art:

- `gfx/interface/mapmode/mapmode_buttons_deselected_small_contaminated_states_map_mode.dds`
- `gfx/interface/mapmode/mapmode_buttons_selected_small_contaminated_states_map_mode.dds`
- `gfx/interface/mapmode/mapmode_buttons_deselected_small_deaths_state_map_mode.dds`
- `gfx/interface/mapmode/mapmode_buttons_selected_small_deaths_state_map_mode.dds`

These are referenced by:

- `interface/chaosx_map_modes.gfx`

Sprite keys used by the engine:

- `GFX_mapmode_buttons_deselected_small_contaminated_states_map_mode`
- `GFX_mapmode_buttons_selected_small_contaminated_states_map_mode`
- `GFX_mapmode_buttons_deselected_small_deaths_state_map_mode`
- `GFX_mapmode_buttons_selected_small_deaths_state_map_mode`

## Future extensions

- Add a strategic-region contamination map mode if air contamination and fallout should also be shown at theater scale.
- Split the deaths heat map into civilian-only and total-deaths variants if military losses later get reliable state attribution.
- Add optional decision integration that opens these map modes directly for cleanup, quarantine, or relief actions.
