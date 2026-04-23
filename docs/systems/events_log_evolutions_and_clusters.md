# Events Log Evolutions, Events List, and Detail Windows

## Purpose
This update keeps `History` and `Evolutions`, and replaces the old placeholder `Event Clusters` tab with a real `Events` tab that lists all currently defined events.
It also adds clickable detail windows for:
- history entries (shared event detail window),
- evolution entries (evolution detail window),
- events-list entries (shared event detail window).

The zombie outbreak event now has authored gameplay text in the event-details window, and its related evolution milestones can be opened directly from both the history-details overlay and the events-tab detail window.

## Step-by-step behavior
1. Opening the popup (`toggle_events_log_popup`) initializes all three tab-state groups:
   - history controls,
   - evolution controls,
   - events-list controls (`settings_events_log_events_*`).
2. Clicking `History` rebuilds `global.events_log_view_*` from fired history.
3. Clicking `Evolutions` rebuilds `global.events_log_evolution_view_*`.
4. Clicking `Events` rebuilds a catalogue view using `global.all_events` plus runtime metadata:
   - fired count per event (from history log arrays),
   - enabled/disabled state (from `global.disabled_events`),
   - unique flag (major/fire-once vs repeatable).
   - live selection weight for each row (zeroed for disabled events and already-fired unique events).
5. The square toggle button in each `Events` row instantly enables/disables the event and rebuilds the list.
6. When a new event is recorded while the `Events` tab is open, the catalogue view rebuilds so live weight values stay current.
7. Logged evolution rows are now pure history rows. They stay clickable, but their enable/disable checkbox is gone because the evolution already happened.
8. Event-preview evolution rows inside the shared event-details popup still keep their checkbox, because that list is used to control future progression.
9. Clicking any event row from either `History` or `Events` opens the same large detail window.
10. That shared event detail window now shows runtime context when it exists:
   - fired-on date,
   - log number,
   - actor flag beside the title once the event has actually fired,
   - latest reached evolution stage.
11. Event `2` (`Zombie Outbreak`) now renders gameplay-useful description text in that detail window instead of the old placeholder copy.
12. If the selected event has logged or preview evolutions, the event detail window shows a clickable evolution list under the description text.
13. Clicking a related evolution entry, or an entry from the `Evolutions` tab, opens the evolution detail popup with:
   - evolution title and summary,
   - logged actor country link,
   - evolved zombie portrait,
   - stage-specific modifier breakdown for the zombie horde.

## Events tab sorting and filtering
Events tab supports:
- Filter: `All`, `Enabled`, `Disabled`
- Sort mode: `By Event ID`, `By Unique`, `By Fired`
- Sort order: `Ascending`, `Descending`

Sorting uses deterministic tie-breaking by event id.

## Data integration
Events-list metadata arrays:
- `global.events_log_events_view_fired_entries`
- `global.events_log_events_view_enabled_entries`
- `global.events_log_events_view_unique_entries`
- `global.events_log_events_view_weight_entries`

The row id/type payload reuses:
- `global.events_log_view_event_id_entries`
- `global.events_log_view_event_type_entries`

Detail-window selection variables:
- `events_log_selected_event_id`
- `events_log_selected_event_type`
- `events_log_selected_evolution_type`
- `events_log_selected_evolution_tier`
- `events_log_selected_evolution_stage`
- `events_log_selected_evolution_event_id`
- `events_log_selected_evolution_event_type`
- `events_log_selected_evolution_actor`
- `events_log_selected_evolution_has_actor`
- `events_log_selected_evolution_date`

Generic evolution-disable contract:
- UI toggles set `events_log_evolution_event_id`, `events_log_evolution_type`, and `events_log_evolution_stage`.
- Gameplay scripts can reuse the same three variables and then check `is_current_evolution_enabled = yes`.
- Disabled stages are stored as dynamic global flags, so new evolution chains do not need new constants or bespoke toggle infrastructure.

## Future plans
1. Extend authored event-detail text to other major event chains besides zombies.
2. Add non-zombie evolution detail content once those evolution families are implemented.
3. If the layout gets crowded later, split the evolution popup into a portrait column and a richer modifier panel with icons.

## UI assets and wiring
GUI files touched:
- `interface/chaosx_events_log_popup.gui`
- `common/scripted_guis/chaosx_scripted_gui_events_log.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`
- `localisation/english/chaosx_gui_l_english.yml`

Sprites currently used:
- `GFX_sort_button_100x29`
- `GFX_chaosx_sort_button_100x29_2`
- `GFX_chaosx_arrow_left`
- `GFX_chaosx_arrow_right`
- `GFX_chaosx_chaos_meter_entry`
- `GFX_chaosx_checkbox_checked`
- `GFX_chaosx_checkbox_unchecked`
- `GFX_flag_small2`
- `GFX_diplo_countrylist_flag_frame`
- `GFX_tiled_window_2b_border`
- `GFX_portrait_ZZZ_leader_2`
- `GFX_portrait_ZZZ_leader_3`
- `GFX_portrait_ZZZ_leader_4`
- `GFX_portrait_unknown`

New art required:
- None for the current zombie event/evolution detail implementation. The portrait frame reuses `GFX_tiled_window_2b_border`, and the zombie portraits reuse the already-registered sprites in `interface/chaosx_characters.gfx`.

If new art is required later:
- Put textures in `gfx/interface/`.
- Register them in `interface/chaosx.gfx`.
