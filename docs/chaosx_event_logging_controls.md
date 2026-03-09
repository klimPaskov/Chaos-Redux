# ChaosX Event Logging Controls

## Overview
This change adds explicit event-fire logging controls to the Chaos Redux settings UI and extends event-fire logs with runtime statistics.

The system now has two logging entry points:
- Manual snapshot log button in settings (top-right, next to close).
- Automatic event-fire logs from `chaosx_logic_effects` (toggleable with a checkbox, default OFF).

## How It Works
1. A new small log button (`chaosx_log_button`) in `chaosx_settings_window` triggers `write_event_log_snapshot`.
2. `write_event_log_snapshot` forces one call of `log_event_system_debug` regardless of the auto-log toggle.
3. A new checkbox (`logic_log_lines_checkbox`) in Trigger Events toggles `settings_logic_log_lines_enabled`.
4. `on_major_event_fired`, `on_repeatable_event_fired`, and `on_fire_once_event_fired` now call `log_event_fired_summary`.
5. `log_event_fired_summary` writes:
- Fired event ID
- Fired event name
- Fired event type
- Unique events left
- Minor events since last major
- Total fired count
- Remaining per category (major/fire-once/repeatable)
6. Daily full debug dump in `common/on_actions/chaosx_on_actions_system.txt` is now gated by `settings_logic_log_lines_enabled`.

## State and Defaults
- Global flag: `settings_logic_log_lines_enabled`
- Default: disabled (`initialize_global_settings_system` clears it)

## Files Updated
- `interface/chaosx.gui`
- `interface/chaosx.gfx`
- `common/scripted_guis/chaosx_scripted_gui_settings.txt`
- `common/scripted_effects/chaosx_settings_effects.txt`
- `common/scripted_effects/chaosx_logic_effects.txt`
- `common/on_actions/chaosx_on_actions_system.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_settings.txt`
- `localisation/english/chaosx_gui_l_english.yml`

## Icon and Sprite Wiring
- Source copied from vanilla:
  - `/home/klim/projects/Hearts of Iron IV/gfx/interface/equipmentdesigner/edit_notes_button.dds`
- Mod texture path:
  - `gfx/interface/chaosx_events_log_button.dds`
- GFX definition file:
  - `interface/chaosx.gfx`
- Sprite name used in code:
  - `GFX_chaosx_edit_notes_button`
- GUI element using it:
  - `chaosx_log_button` in `interface/chaosx.gui`

## Future Improvements
- Add category-filtered snapshot logging from the same button (major-only, fire-once-only, repeatable-only).
- Add per-country auto-log scope toggle in addition to the current global toggle.
- Add a compact in-UI text panel for key counts (unique left, minor-since-major) without reading logs.
