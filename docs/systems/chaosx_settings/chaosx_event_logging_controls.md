# ChaosX Event Logging Controls

## Overview
The Chaos Redux settings UI opens the Event Logs popup, and the popup exposes the event-fire logging toggle.
Event-fire logs include runtime statistics.

The system has two parts:
- The Event Logs button in settings (top-right, next to close), which opens the Event Logs popup.
- Automatic event-fire logs from `chaosx_logic_effects`, toggled with the Auto Event Logs checkbox on the popup status tab (default OFF).

## How It Works
1. The small log button (`chaosx_events_log_button`) in `chaosx_settings_window` runs `chaosx_events_log_button_click` in `common/scripted_guis/chaosx_scripted_gui_settings.txt`, which calls `toggle_events_log_popup` and `update_unfired_events_counts`.
2. The Auto Event Logs checkbox (`events_log_auto_checkbox`) on the status tab of the Event Logs popup runs `events_log_auto_checkbox_click` in `common/scripted_guis/chaosx_scripted_gui_events_log.txt`, which calls `toggle_logic_log_lines`.
3. `toggle_logic_log_lines` in `common/scripted_effects/chaosx_settings_effects.txt` toggles `settings_logic_log_lines_enabled` and writes one log line stating the new state.
The checkbox sprite follows the flag through the `GetLogicLogLinesCheckboxSprite` scripted localisation.
4. `on_major_event_fired`, `on_repeatable_event_fired`, and `on_fire_once_event_fired` call `log_event_fired_summary`.
5. `log_event_fired_summary` writes:
- Fired event ID
- Fired event name
- Fired event type
- Unique events left
- Minor events since last major
- Total fired count
- Remaining per category (major/fire-once/repeatable)
6. The daily full debug dump in `common/on_actions/chaosx_on_actions_system.txt` calls `log_event_system_debug` after that day's event processing and is gated by `settings_logic_log_lines_enabled`.
No button forces a one-off `log_event_system_debug` call, and `log_event_fired_summary` also accepts the `temp_force_logic_log` temporary variable as an alternative to the flag.

## State and Defaults
- Global flag: `settings_logic_log_lines_enabled`
- Default: disabled (`initialize_global_settings_system` clears it)

## Implementation Files
- `interface/chaosx.gui`
- `interface/chaosx.gfx`
- `interface/chaosx_events_log_popup.gui`
- `common/scripted_guis/chaosx_scripted_gui_settings.txt`
- `common/scripted_guis/chaosx_scripted_gui_events_log.txt`
- `common/scripted_effects/chaosx_settings_effects.txt`
- `common/scripted_effects/chaosx_logic_effects.txt`
- `common/on_actions/chaosx_on_actions_system.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_settings.txt`
- `localisation/english/chaosx_gui_l_english.yml`

## Icon and Sprite Wiring
- Source copied from vanilla:
  - `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/interface/equipmentdesigner/edit_notes_button.dds`
- Mod texture path:
  - `gfx/interface/chaosx_events_log_button.dds`
- GFX definition file:
  - `interface/chaosx.gfx`
- Sprite name used in code:
  - `GFX_chaosx_events_log_button`
- GUI element using it:
  - `chaosx_events_log_button` in `interface/chaosx.gui`

## Future Improvements
- Add a manual one-off snapshot control that calls `log_event_system_debug`, with category filters (major-only, fire-once-only, repeatable-only).
- Add per-country auto-log scope toggle in addition to the current global toggle.
- Add a compact in-UI text panel for key counts (unique left, minor-since-major) without reading logs.
