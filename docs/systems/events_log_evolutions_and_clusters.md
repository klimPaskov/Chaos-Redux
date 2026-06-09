# Events Log Evolutions, Events List, and Detail Windows

## Purpose
This UI exposes `History`, `Evolutions`, `Events`, and `Clusters` tabs for fired entries, progression milestones, defined event chains, and the event cluster catalogue.
It also adds clickable detail windows for:
- history entries (shared event detail window),
- evolution entries (evolution detail window),
- events-list entries (shared event detail window),
- cluster catalogue entries and fired cluster history entries (cluster detail window with clickable member events).

The zombie outbreak event has authored gameplay text in the event-details window, and its related evolution milestones can be opened directly from both the history-details overlay and the events-tab detail window.

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
7. Clicking `Clusters` rebuilds `global.events_log_cluster_view_*` from registered cluster definitions.
8. Logged evolution rows are pure history rows. They stay clickable, but their enable/disable checkbox is gone because the evolution already happened.
9. Event-preview evolution rows inside the shared event-details popup still keep their checkbox, because that list is used to control future progression.
10. Clicking any event row from either `History` or `Events` opens the same large movable detail window, centered on screen when opened.
11. Clicking a cluster catalogue row opens current cluster details in the same large movable layout. Fired cluster rows appear in `History` and open the historical cluster details.
12. Cluster rows and cluster details include an enable/disable checkbox. The cluster details window also has a manual trigger button.
13. That shared event detail window shows runtime context when it exists:
   - fired-on date,
   - log number,
   - actor flag beside the title once the event has actually fired,
   - latest reached evolution stage.
14. Event `2` (`Zombie Outbreak`) renders gameplay-useful description text in that detail window.
15. Event `4` (`Random War`) renders War Contagion detail text and stage previews.
16. If the selected event has logged or preview evolutions, the event detail window shows a clickable evolution list under the description text.
17. Clicking a related evolution entry, or an entry from the `Evolutions` tab, opens the evolution detail popup with:
	   - evolution title and summary,
	   - logged actor country link,
	   - a portrait only when that evolution family has an authored portrait mapping for the selected stage,
	   - stage-specific modifier breakdown for the zombie horde.

Evolution rows use the specific stage title for that milestone, such as `Triangular Incident` or `Four Fronts`, and keep generic type labels only as fallback text.

## Events tab sorting and filtering
Events tab supports:
- Filter: `All`, `Enabled`, `Disabled`
- Sort mode: `By Event ID`, `By Fired`, `By Weight`, `By Type`
- Sort order: `Ascending`, `Descending`

Sorting uses deterministic tie-breaking by event id.

## Clusters tab sorting and filtering
Clusters tab supports:
- Filter: `All`, `Available`, `Unavailable`
- Sort mode: `By Cluster ID`, `By Type`, `By Roll`, `By Fired`
- Sort order: `Ascending`, `Descending`

The Clusters tab lists clusters that can be inspected or controlled from the event log. Fired cluster entries belong in `History`.

Cluster member rows are sorted by danger, with lower danger first. Roll chance displays `N/A` while the cluster is locked by chaos tier.

## Shortcuts
- `Ctrl+Shift+E` toggles the Event Logs window.
- `Ctrl+E` opens the Event Logs window directly on the Events tab.
- `Ctrl+Shift+T` shows the Event Timer window.

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
- `events_log_selected_evolution_has_portrait`
- `events_log_selected_evolution_date`
- `events_log_selected_cluster_sequence`
- `events_log_selected_cluster_id`
- `events_log_selected_cluster_type`
- `events_log_selected_cluster_tier`
- `events_log_selected_cluster_unlock_tier`
- `events_log_selected_cluster_roll_chance`
- `events_log_selected_cluster_available`
- `events_log_selected_cluster_enabled`
- `events_log_selected_cluster_actor`
- `events_log_selected_cluster_has_actor`
- `events_log_selected_cluster_member_count`
- `events_log_selected_cluster_fired_count`
- `events_log_selected_cluster_skipped_count`
- `global.events_log_view_cluster_id_entries`
- `global.events_log_view_cluster_sequence_entries`
- `global.events_log_view_cluster_type_entries`
- `global.events_log_cluster_view_enabled_entries`

Generic evolution-disable contract:
- UI toggles set `events_log_evolution_event_id`, `events_log_evolution_type`, and `events_log_evolution_stage`.
- Gameplay scripts can reuse the same three variables and then check `is_current_evolution_enabled = yes`.
- Disabled stages are stored as dynamic global flags, so new evolution chains do not need new constants or bespoke toggle infrastructure.

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
- `GFX_portrait_communist_rebels`
- `GFX_portrait_THR_refuge_bodhisattva`
- `GFX_portrait_THR_bodhisattva_pramudita`
- `GFX_portrait_THR_arhat_administration`
- `GFX_portrait_THR_buddha_mandate`
- `GFX_portrait_THR_divine_sovereignty`
- `GFX_portrait_THR_final_silence`

New art required:
- None for the current event/evolution detail implementation. Evolution details use the portrait layout only when `has_events_log_selected_evolution_authored_portrait` resolves true for the selected evolution type and stage; stages without an authored mapping keep the wide text body.

If new art is required later:
- Put textures in `gfx/interface/`.
- Register them in `interface/chaosx.gfx`.
