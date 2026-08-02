# State Map Modes

This adds five scripted state map modes for crisis visibility without duplicating gameplay logic.

## What was added

1. `contaminated_states_map_mode`
2. `deaths_state_map_mode`
3. `air_winter_state_map_mode`
4. `air_winter_exposure_map_mode`
5. `air_winter_survival_map_mode`

The contamination view reads the live state contamination systems:

- `chem_state_contamination`
- `anthrax_contaminated_state`
- `plague_contaminated_state`
- `tularemia_contaminated_state`
- `smallpox_contaminated_state`
- `nuclear_fallout_state`
- Event 20 Black Plague state phase and monitoring memory

The deaths view reads cumulative state-level civilian deaths from `chaos_state_civilian_deaths_total`, which is now written directly by the shared chaos-meter death registration pipeline whenever a civilian death source also reduces state population.

## Contamination map mode

The contamination map mode uses a full-state bottom layer and a status-border top layer. Ordinary hazards retain their shared colors:

- Chemical: amber
- Disease: green
- Nuclear: cyan-blue

Event 20 follows a stricter presentation contract:

- Threatened states use an amber-brown surveillance fill.
- Incubating, Infected, Severe Crisis, Collapsed, Contained, Recovery, and Rat-Controlled states use a pure black base when they are visible to the mapmode player.
- Cured states and states retained only for post-cure monitoring use pale green-grey.
- Incubating and Infected states have neutral phase borders. Severe Crisis and Collapsed states use heavier orange and red borders. Contained uses blue. Recovery and Cured use green.
- Currently weaponized infection with public attribution uses a purple border without changing the black base. A historical release flag cannot keep the border purple after provenance changes.
- Rat-Controlled states use the heaviest ochre-red border without changing the black base.

The Rat-Controlled border has highest priority, followed by currently weaponized infection with public attribution and then the ordinary phase accent. Owners and controllers can inspect the exact phase, disease load, mortality pressure, spread pressure, containment, treatment coverage, relapse risk, Rat Infestation, and known provenance. Other countries see a state only after public recognition and receive qualitative containment and Rat Infestation bands plus public provenance. Secret foreign Incubating states do not color the map or expose a tooltip.

If an established Event 20 state also carries chemical, ordinary disease, or nuclear contamination, the Event 20 black base takes priority. The tooltip still lists every tracked hazard. States without established Event 20 infection continue to blend ordinary hazard colors additively. Mixed ordinary hazards pulse so overlap remains obvious.

The map mode updates daily, which keeps it in sync with timed contamination expiry without needing separate refresh hooks in every chemical, biological, and nuclear effect path.
Event 20 also marks weekly state and provenance changes dirty and consumes that flag through one refresh after the complete pulse. Batch setup paths rebuild once after all state changes rather than refreshing separately for every state. The response and deployment tranche must call the same explicit refresh helper after each complete standalone transaction.

The canonical predicates are `black_plague_state_is_established` for the seven black-base phases and `black_plague_state_is_tracked` for Threatened, every established phase, Cured, and temporary post-cure monitoring. `black_plague_state_is_visible_to_mapmode_player` and `black_plague_state_details_are_visible_to_mapmode_player` enforce public and private disclosure separately. Shared disease detection and border-proximity AI use the established predicate without reusing the legacy plague modifier. Event 20 response decisions consume the same predicate through selected-state helpers. The older copy-coded hospital and quarantine rows remain outside the accepted Event 20 response package. The shared crisis-board disease selector remains required for decision presentation. The latest Event 20 acceptance rule keeps every authorized established Black Plague state black in the shared contamination mapmode regardless of the selected disease tab.

The scripted mapmode engine exposes two flat color layers, one optional border, and pulsation. It does not expose state-clipped textures, patterns, broken edges, particles, or the active-mapmode state to scripted effects. Black fog clipped inside infected state borders is therefore not safely implementable through this engine surface. A state-centroid particle would spill across borders and remain visible outside the mapmode, so it is not used as an unapproved substitute.

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

## Air Winter views

The Air Winter package exposes its three accepted display layers as adjacent engine-native scripted mapmode buttons.

- `air_winter_state_map_mode` colors phases 0 through 6 and uses border weight to distinguish worsening conditions from sustained recovery.
- `air_winter_exposure_map_mode` uses the state's 0 through 100 exposure value as a continuous cold-blue to red burden gradient. The tooltip separates local fallout intensity, global air contamination, shelter protection, and adaptation.
- `air_winter_survival_map_mode` uses the state's derived 0 through 100 survival value as a continuous red to green gradient. It exposes food, shelter, reclamation, recovery, adaptation, exposure, and regional conditions.

The three buttons avoid an undocumented GUI-to-mapmode switch. They retain the normal scripted-mapmode render path, daily refresh, state tooltips, and ordinary map selection behavior. Their values come from the Air Winter monthly state update rather than a second visual-only calculation.

## Files

- Map mode definitions: `common/map_modes/chaosx_state_map_modes.txt`
- Map mode constants: `common/script_constants/state_map_modes_constants.txt`
- Shared contamination map mode triggers: `common/scripted_triggers/cbw_triggers.txt`
- Black Plague phase and viewer-authorization triggers: `common/scripted_triggers/020_black_plague_triggers.txt`
- Tooltip scripted localisation: `common/scripted_localisation/chaosx_scripted_localisation_map_modes.txt`
- Shared-strip and scripted-map-mode sprite definitions: `interface/mapmodes_interface.gfx`
- English localisation: `localisation/english/chaosx_map_modes_l_english.yml`

## Map mode icons

The shared vanilla-style strips contain `19` frames at `20x18` pixels per frame:

- `gfx/interface/mapmode/mapmode_buttons_deselected_small.dds`
- `gfx/interface/mapmode/mapmode_buttons_selected_small.dds`

Chaos Redux uses vanilla's otherwise blank frame `18` for civilian deaths and appends frame `19` for contamination. The strip definitions therefore remain at `noOfFrames = 19`.

Scripted map modes do not resolve those shared-strip positions directly. They require the exact per-mode sprite names defined in `interface/mapmodes_interface.gfx`:

- `GFX_mapmode_buttons_deselected_small_deaths_state_map_mode`
- `GFX_mapmode_buttons_selected_small_deaths_state_map_mode`
- `GFX_mapmode_buttons_deselected_small_contaminated_states_map_mode`
- `GFX_mapmode_buttons_selected_small_contaminated_states_map_mode`
- `GFX_mapmode_buttons_deselected_small_air_winter_state_map_mode`
- `GFX_mapmode_buttons_selected_small_air_winter_state_map_mode`
- `GFX_mapmode_buttons_deselected_small_air_winter_exposure_map_mode`
- `GFX_mapmode_buttons_selected_small_air_winter_exposure_map_mode`
- `GFX_mapmode_buttons_deselected_small_air_winter_survival_map_mode`
- `GFX_mapmode_buttons_selected_small_air_winter_survival_map_mode`

Their dedicated `20x18` DDS files live under `gfx/interface/mapmode/custom/`. Source and processed PNG copies are recorded under `docs/assets/shared_gfx_cleanup/`.

Current strip-source assignment:

- Frame `18`: `deaths_state_map_mode`
- Frame `19`: `contaminated_states_map_mode`
