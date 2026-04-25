# Chaos Redux Event Logs Window

## Purpose
The Event Logs window tracks fired automatic events in a dedicated popup and exposes debugging/inspection controls without cluttering the main settings panels.

## System flow
1. `toggle_events_log_popup` opens/closes the window and defaults to `History`.
2. The popup has four tabs:
   - `Status`
   - `History`
   - `Evolutions`
   - `Event Clusters` (placeholder, empty by design for now)
3. Opening `History` calls `rebuild_events_log_history_view`.
4. Opening `Evolutions` calls `rebuild_events_log_evolution_view`.
5. Status tab shows current counters and controls plus a right-side live-values panel (`current major weight`, `recovery rate`, `cap reduction`, `weight per minor`, `default weight`, `timer modifier`).

## History tab behavior
- Filter options: `All`, `Major`, `Minor Repeatable`, `Minor Fire Once`.
- Sort options: `By Index`, `By Event ID`, `By Actor`.
- Order options: `Ascending`, `Descending`.
- Actor sorting now uses deterministic actor-id passes.
- Rows without actors are always appended after actor rows in actor sort.
- Clicking a history row now opens the same shared event-details popup used by the `Events` tab.
- That shared detail popup uses the clicked history row as context when available, so `Fired on`, `Log #`, and `Actor` reflect the selected log entry instead of a generic placeholder.
- If an event has a mapped actor and it has already fired, the shared detail popup shows that actor as a clickable flag next to the title instead of a separate `Actor:` row.

## Events tab behavior
- Each event row shows the current live selection weight from `global.event_weights`, presented as `0` when the event is disabled or is an already-fired unique event.
- Event rows show `ID`, `Type`, `Weight`, `Fired`, and enabled state on the top line; the event name is kept alone on the second line.
- Sort options: `By Event ID`, `By Fired`, `By Weight`.
- The `Events` tab rebuilds when a new event is logged while the tab is open, keeping live weights and fired counts current.

## Evolutions tab behavior
- Logs evolution entries (currently zombie evolution stages, with room for additional types).
- Zombie evolution logs are written only for the main zombie country (`tag = ZZZ`), not for dynamic outbreak tags.
- Filter options: `All`, `Major`, `Minor` (driven by stored event type for each evolution entry).
- Sort options: `By Index`, `By Tier`, `By Stage`, `By Actor`.
- Order options: `Ascending`, `Descending`.
- Actor flags render only when evolution entry has an actor.
- Each row shows `Tier` and `Stage`.
- Logged evolution rows are inspection rows only: they open the evolution-details popup, but they do not show enable/disable checkboxes.
- The main `Evolutions` tab rows now open the same evolution-details popup reliably even on actor-scoped rows, because the click is resolved back on the player scope before the detail state is written.

## Actor flags
- History actor flags are shown only when `global.events_log_view_has_actor_entries^events_log_history_index > 0`.
- Evolution actor flags are shown only when `global.events_log_evolution_view_has_actor_entries^events_log_evolution_index > 0`.
- Non-actor rows are sanitized to actor `0` and has-actor `0`.

## Data structures
Events-tab metadata arrays:
- `global.events_log_events_view_fired_entries`
- `global.events_log_events_view_enabled_entries`
- `global.events_log_events_view_unique_entries`
- `global.events_log_events_view_weight_entries`

Source history arrays:
- `global.events_log_history_sequence_entries`
- `global.events_log_history_date_entries`
- `global.events_log_history_event_id_entries`
- `global.events_log_history_event_type_entries`
- `global.events_log_history_actor_entries`
- `global.events_log_history_has_actor_entries`

Derived view arrays:
- `global.events_log_view_sequence_entries`
- `global.events_log_view_date_entries`
- `global.events_log_view_event_id_entries`
- `global.events_log_view_event_type_entries`
- `global.events_log_view_actor_entries`
- `global.events_log_view_has_actor_entries`

Source evolution arrays:
- `global.events_log_evolution_sequence_entries`
- `global.events_log_evolution_date_entries`
- `global.events_log_evolution_type_entries`
- `global.events_log_evolution_event_type_entries`
- `global.events_log_evolution_tier_entries`
- `global.events_log_evolution_stage_entries`
- `global.events_log_evolution_actor_entries`
- `global.events_log_evolution_has_actor_entries`

Derived evolution view arrays:
- `global.events_log_evolution_view_sequence_entries`
- `global.events_log_evolution_view_date_entries`
- `global.events_log_evolution_view_type_entries`
- `global.events_log_evolution_view_event_type_entries`
- `global.events_log_evolution_view_tier_entries`
- `global.events_log_evolution_view_stage_entries`
- `global.events_log_evolution_view_actor_entries`
- `global.events_log_evolution_view_has_actor_entries`

## Scripted localisation
- `GetEventsLogHistoryTypeView`
- `GetEventsLogEventTypeView`
- `GetEventsLogHistoryEventName`
- `GetEventsLogFilterType`
- `GetEventsLogSortMode`
- `GetEventsLogSortOrder`
- `GetEventsLogEvolutionFilterType`
- `GetEventsLogEvolutionSortMode`
- `GetEventsLogEvolutionSortOrder`
- `GetEventsLogEvolutionTypeView`
- `GetEventsLogEvolutionTierView`
- `GetEventsLogEvolutionStageView`

These are defined in:
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`

## Interactions with existing systems
- Event record insertion remains in `record_events_log_history_entry` from `chaosx_logic_effects.txt`.
- Opening/tab switching/state values are handled by `chaosx_settings_effects.txt` and `chaosx_scripted_gui_events_log.txt`.
- Event-name localisation reuses existing `chaosx.event_name.*` keys.
- Shared event-details metadata now also derives from:
  - `global.events_log_history_*` for fired/log/actor context,
  - `global.events_log_evolution_*` for the latest reached evolution stage.

## Future extensions
- Populate `Event Clusters` tab when cluster systems are implemented.
- Add per-country actor filter.
- Add cluster/evolution cross-links and stage progression summaries.

## UI/GFX asset wiring
Current assets used:
- `interface/chaosx_events_log_popup.gui`
- Flag sprite: `GFX_flag_small2`
- Flag frame: `GFX_diplo_countrylist_flag_frame`
- Tab/button sprites: `GFX_sort_button_100x29`, `GFX_chaosx_sort_button_100x29_2`
- Arrow sprites: `GFX_chaosx_arrow_left`, `GFX_chaosx_arrow_right`

If new icon art is needed, keep art in:
- `gfx/interface/`

Register new sprites in:
- `interface/chaosx_events_log_popup.gfx` (or existing ChaosX GFX file used for event-log sprites)

Use stable names with the `chaosx_events_log_*` prefix for new event-log-specific sprites.
