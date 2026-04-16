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

If a state carries more than one hazard category at once, the map mode blends those colors additively and switches to a brighter pulsing fill so overlap is obvious at a glance.

The map mode updates daily, which keeps it in sync with timed contamination expiry without needing separate refresh hooks in every chemical, biological, and nuclear effect path.
The scripted top layer now renders the whole state fill instead of only a border layer, and it only renders for states that actually match the contamination triggers. This avoids the earlier target-selection issues and keeps the contamination view restricted to genuinely contaminated states.

## Civilian deaths map mode

The deaths map mode is a heat map based on cumulative recorded civilian deaths per state.

The data flow is:

1. A death source sets the normal chaos-meter state death inputs.
2. `chaos_meter_register_state_civilian_deaths_percent` calculates the death amount.
3. `chaos_meter_register_deaths` applies the state population loss.
4. The same effect now also adds the loss to `chaos_state_civilian_deaths_total`.
5. If that state total exceeds the global peak, `global.chaos_state_civilian_deaths_map_max` is updated.
6. The map mode colors each state relative to the current global peak so the hottest state is always clearly visible.
7. The deaths view now uses a continuous red heat gradient instead of coarse discrete steps, so each state's fill gets redder and more opaque as its cumulative civilian death total rises.
8. The scripted top layer renders full state fill only for states with tracked civilian-death history, which keeps the deaths view separate from contamination and makes the heat map much more legible.

This keeps the feature dynamic and easy to extend. Any future civilian-death source that already uses the shared chaos-meter registration path will automatically appear on the map without extra map-view-specific logic. Combat-caused civilian deaths use the same registration path, so the heat map highlights whichever frontier states actually receive those civilian-combat death entries.

## Files

- Map mode definitions: `common/map_modes/chaosx_state_map_modes.txt`
- Map mode constants: `common/script_constants/state_map_modes_constants.txt`
- Reusable map mode triggers: `common/scripted_triggers/chaosx_dynamic_triggers.txt`
- Tooltip scripted localisation: `common/scripted_localisation/chaosx_scripted_localisation_map_modes.txt`
- Shared strip sprite definitions: `interface/mapmodes_interface.gfx`
- English localisation: `localisation/english/chaosx_map_modes_l_english.yml`

## Icons needed

The button icons come from the shared vanilla-style strip:

- `gfx/interface/mapmode/mapmode_buttons_deselected_small.dds`
- `gfx/interface/mapmode/mapmode_buttons_selected_small.dds`

Chaos Redux extends those strips to `20` frames in:

- `interface/mapmodes_interface.gfx`

Vanilla already occupies the first `18` small-strip frames, including hidden deployment and nudger slots, so the two scripted Chaos Redux map modes must use appended frames after the vanilla strip.

Current slot assignment:

- Strip sprite `19`: `deaths_state_map_mode`
- Strip sprite `20`: `contaminated_states_map_mode`

## Future extensions

- Add a strategic-region contamination map mode if air contamination and fallout should also be shown at theater scale.
- Split the deaths heat map into civilian-only and total-deaths variants if military losses later get reliable state attribution.
- Add optional decision integration that opens these map modes directly for cleanup, quarantine, or relief actions.
