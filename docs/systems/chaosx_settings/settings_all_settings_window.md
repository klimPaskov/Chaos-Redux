# All Settings Window

## Overview

`Settings > Advanced Settings > Show All Settings` opens `chaosx_all_settings_window`, one scrollable window that lists every adjustable Chaos Redux setting with its current value and a control to change it.
Every control calls the same scripted effect as its settings page or system window, so bounds, side effects and staged values stay in one place.
Changing a value here changes the same variable or flag the settings pages read.

## Files

| Surface | File |
| --- | --- |
| Window layout | `interface/chaosx_all_settings.gui` |
| Scripted GUI wiring | `common/scripted_guis/chaosx_scripted_gui_all_settings.txt` |
| Open and close effects | `common/scripted_effects/chaosx_all_settings_effects.txt` |
| Positive-polarity checkbox sprites | `common/scripted_localisation/chaosx_scripted_localisation_all_settings.txt` |
| Fallout availability trigger | `fallout_consequence_setting_available` in `common/scripted_triggers/chaosx_world_end_scenario_triggers.txt` |
| Localisation | `localisation/english/chaosx_all_settings_l_english.yml` |
| Open button | `show_all_settings_button` in the Advanced Settings page of `interface/chaosx.gui` |

## Flow

1. `show_all_settings_button` calls `toggle_chaosx_all_settings_window`, which sets or clears the country flag `chaosx_all_settings_open`.
2. The window is visible only while both `chaosx_settings_open` and `chaosx_all_settings_open` are set.
3. The close button calls `close_chaosx_all_settings_window`. Closing or reopening the settings window clears the flag through `close_chaosx_settings` and `open_chaosx_settings`.
4. The window is moveable and centred on screen; its 600x540 frame fits a 1093x614 virtual screen.

## Rows

Every checkbox in this window is checked when its feature is on.
The settings pages keep their own "Disable ..." wording.

| Group | Row | Effect called | Scope |
| --- | --- | --- | --- |
| Automatic Events | Automatic events | `toggle_event_system` | player country |
| Automatic Events | Shortest and longest interval | `decrease_timer_min`, `increase_timer_min`, `decrease_timer_max`, `increase_timer_max`; right click `toggle_timer_increment_mode` | player country, staged |
| Automatic Events | Apply Interval | `update_timer_from_settings` | player country |
| Automatic Events | Show event timer window | `toggle_timer_window` | player country |
| Automatic Events | Force trigger mode | `toggle_force_trigger_mode` | player country |
| Event Weights | Recovery rate, weight cut after firing, baseline major gain | `decrease_advanced_*`, `increase_advanced_*`; right click `toggle_advanced_increment_mode` | global, staged |
| Event Weights | Apply Weights, Reset Weights | `update_advanced_settings_values`, `reset_advanced_settings_to_defaults` | global |
| Chaos and World End | Chaos Meter | `toggle_chaos_meter_disabled` (locked after a world end begins) | global |
| Chaos and World End | World-end scenarios | `toggle_world_end` | global |
| Chaos and World End | Allow Fallout | `fallout_toggle_system_scenario_disabled` (locked by `fallout_consequence_setting_available`) | global |
| World Systems | Air Cleanliness | `toggle_air_cleanliness_system_disabled` (same lock as the Air Cleanliness tab) | global |
| World Systems | Deaths ledger | `toggle_chaos_meter_deaths_system_disabled` | global |
| World Systems | Static winter map | `air_winter_toggle_static_climate_map` | global |
| Country Control | Enable events on tag switch, disable events for previous tag | `toggle_auto_enable_on_switch`, `toggle_disable_previous_tag` | global |
| Super-Event Audio | Super-event volume | `cycle_super_event_audio_volume_prev`, `cycle_super_event_audio_volume_next` | player country |

Staged rows show the pending value in the value box and the value in use beside it.
Manual event firing, cluster firing, tag selection and Chaos level editing are actions rather than settings and stay on their settings pages.

## Fallout control

The Fallout consequence toggle lives in the Air Cleanliness tab of the Chaos Meter window (`air_fallout_toggle_checkbox`) and in this window.
Both call `fallout_toggle_system_scenario_disabled`, which writes both Fallout entries of `global.disabled_world_end_scenarios`, and both read `GetFalloutAllowedCheckboxSprite`.
The control locks once Fallout begins or another world-end scenario is active.

## Icons and assets

No new art is required.
The window reuses `GFX_tiled_window_2b_border`, `GFX_tiled_plain_bg`, `GFX_closebutton_small`, `GFX_chaosx_checkbox_checked`, `GFX_chaosx_checkbox_unchecked`, `GFX_chaosx_add_*`, `GFX_chaosx_subtract_*`, `GFX_chaosx_text_bg_60`, `GFX_chaosx_button_123x34`, `yearslider_leftbutton` and `yearslider_rightbutton`, all registered in `interface/chaosx.gfx` or the installed game.

## Future plans

- Add a per-row "default" marker so changed settings stand out.
- Add the settings export button to this window once export covers every listed row.
