# Chaos Redux Miscellaneous Settings Menu

## Overview
This change adds a new `Miscellaneous` category to the Chaos Redux settings menu and moves a few utility behaviors into a clearer flow.

The update covers:
- A new `Miscellaneous` menu entry below `Advanced Settings`.
- Super-event playback channel selection between music and sound.
- Super-event audio volume selection with a stepped slider covering the explicit multiplier tiers.
- Direct keyboard entry for event IDs after clicking the event ID box.
- A reset confirmation popup for `Reset All Settings`.
- Random-event button behavior changed from immediate fire to random ID selection.
- Timer update flow fixed so staged values do not apply until the manual update action is used.
- Tag Management sync helpers for currently selected countries and state controllers.

## Miscellaneous menu flow
1. Clicking `Miscellaneous` opens a dedicated content panel in the settings window.
2. `Playback Channel` cycles between:
- `Music`
- `Sound`
3. `Super Event Audio Volume` cycles between:
- `0x`
- `0.5x`
- `1.0x`
- `1.5x`
- `2.0x`
- `2.5x`
- `3.0x`
4. Default values are:
- Audio mode: `Sound`
- Audio volume: `1.5x`

These defaults are applied in both `initialize_miscellaneous_settings` and `reset_miscellaneous_to_defaults`.

## Super-event audio behavior
Super-event playback is now routed through `play_current_super_event_audio` in:
- `common/scripted_effects/chaosx_settings_effects.txt`

Behavior:
- `Music` mode plays the current super-event track through the music channel.
- `Sound` mode plays that same current super-event track through the sound-effects channel.
- `0x` mutes super-event playback entirely.
- `1.5x` preserves the previous loudness as the default volume tier.
- `Sound` is now the default playback channel for new saves and for `Reset All Settings`.

Current song routing:
- The script now builds `chaosx_super_event_<id>_<volume_suffix>` dynamically through `meta_effect`.
- Sound-channel playback builds `chaosx_super_event_<id>_sound_<volume_suffix>` the same way.
- Current live super-event IDs `1`, `2`, and `3` reuse the zombie outbreak track definitions.
- Current live super-event ID `4` reuses the default track definitions.
- Current live super-event ID `5` uses the zombie-threat-defeated track definitions.
- Current live super-event ID `6` uses the wendigo track definitions.

The variant song IDs are defined in:
- `music/chaosx_super_event_music.asset`

Each registered per-ID variant reuses the same underlying track file from:
- `music/chaosx_super_event_music.asset`

The Miscellaneous panel no longer shows explanatory note text under the controls.
The volume control no longer uses a boxed value field. It now uses a vanilla game-rules style slider look with:
- a slider track
- a snap-position knob
- clickable fixed stops for each supported multiplier
- left/right arrow buttons that still cycle between those same stops
- explicit visibility triggers on the track and snap points so the slider does not remain visible outside the `Miscellaneous` tab

Because scripted GUI does not expose a custom drag-value callback for this menu, the knob snaps to one of the seven fixed positions when the track is clicked rather than supporting free drag input.

## Event ID manual entry
The Trigger Events `Event ID` box now supports direct keyboard entry.

Flow:
1. Click the event ID box.
2. Type numeric keys `0-9`.
3. Press `Enter` to apply the typed ID.
4. Press `Del` to clear the current typed buffer.

Implementation note:
- HOI4 scripted GUI does not expose a documented custom edit-box value callback for this panel.
- The feature is therefore implemented as a focused manual-entry buffer driven by keyboard shortcuts on hidden scripted-GUI buttons, while keeping the visible box as the entry target.

## Reset confirmation popup
`Reset All Settings` now opens a confirmation popup instead of resetting immediately.

Popup behavior:
1. Clicking `Reset All Settings` opens `chaosx_reset_settings_popup`.
2. The popup uses the vanilla `generic_popup_win` background with standard vanilla close and action buttons.
3. `Reset` calls `confirm_reset_all_settings`.
4. `Cancel` and the close button both dismiss the popup without applying changes.

The confirmed reset still applies immediately after acceptance.

## Random-event button behavior
The random-event button no longer fires an event on click.

New flow:
1. Clicking the button selects a random valid event ID.
2. The selected ID is written into `settings_selected_event_id`.
3. The player can then trigger that selected event normally.

Selection rules:
- Normal mode uses the same weighted selection logic as the live event system.
- Force Trigger mode switches the random button to an unweighted random pick inside the current category filter.

Shared selector helpers live in:
- `common/scripted_effects/chaosx_random_event_selection_effects.txt`

## Timer settings fix
The timer range bug came from the live timer calculation reading staged GUI values instead of the applied timer values.

The fix:
- `calculate_next_timer_value` now reads `timer_min_days` and `timer_max_days`.
- `update_timer_from_settings` is the only step that copies staged GUI values from:
  - `settings_timer_min_days`
  - `settings_timer_max_days`
  into the live timer range.

Result:
- Simply changing the staged min/max selectors does not affect the live timer.
- Only the currently applied range is used until the user manually updates it.

## Tag Management selected country sync
Tag Management now includes selected-country and selected-state/controller sync helpers through scripted GUI contexts:
- `selected_country_context`
- `selected_state_context`

Implemented behavior:
- Clicking the Tag Management tag value box toggles map sync mode.
- While map sync mode is active, the selected-country preview is drawn on top of the existing Tag Management controls at the same positions, so the panel layout does not switch to a different sub-window.
- The selected-country preview uses `selected_country_context` attached to a plain GUI anchor at the settings-window position and only overlays the tag/name plus invisible click-catchers over the existing Enable/Disable buttons.
- A selected state can sync its current controller into Tag Management.
- If the current country filter hides that tag, the sync falls back to:
  - Country filter `All`
  - Continent filter `All`
  and then reselects the matching country.

Important note:
- The offline wiki snapshot and vanilla scripted GUI documentation expose click-driven scripted GUI effects, but do not document a safe automatic `selection changed` effect callback.
- Because of that engine-facing limitation, this implementation uses selected-country and selected-state scripted GUI contexts layered onto the existing settings panel rather than a fully automatic player-context callback.

## Tooltip and localisation updates
This change also includes:
- Tooltip added for the Timer System `Disable Event System` checkbox.
- `All continents` display changed to simply `All`.
- Random-event button label updated to reflect ID selection rather than immediate firing.

## Files touched
- `common/script_constants/settings_constants.txt`
- `common/scripted_effects/chaosx_logic_effects.txt`
- `common/scripted_effects/chaosx_settings_effects.txt`
- `common/scripted_effects/chaosx_random_event_selection_effects.txt`
- `common/scripted_effects/chaosx_super_event_audio_effects.txt`
- `common/scripted_effects/chaosx_effects.txt`
- `common/scripted_guis/chaosx_scripted_gui_settings.txt`
- `common/on_actions/chaosx_on_actions_system.txt`
- `common/on_actions/chaosx_on_actions.txt`
- `events/chaosx_events.txt`
- `interface/chaosx.gui`
- `music/chaosx_super_event_music.asset`
- `sound/chaosx_sound.asset`
- `common/scripted_localisation/chaosx_scripted_localisation_settings.txt`
- `localisation/english/chaosx_gui_l_english.yml`

## Icons and asset wiring
No new custom art is required for this change.

Existing assets used:
- Popup background sprite:
  - `GFX_generic_popup_win`
  - file: `gfx/interface/generic_popup_win.dds`
- Popup close button:
  - `GFX_closebutton`
- Popup action button:
  - `GFX_button_148x34`
- Tag sync buttons:
  - `GFX_chaosx_button_123x34`
- Volume slider visuals:
  - `GFX_custom_setting_slider_bg`
  - `yearslider_background`
  - `GFX_scroll_drager`
  - `yearslider_leftbutton`
  - `yearslider_rightbutton`

Audio assets used:
- Music definition file:
  - `music/chaosx_super_event_music.asset`
- Sound definition file:
  - `sound/chaosx_sound.asset`
- Music-channel sources:
  - `music/default.ogg`
  - `music/zombies.ogg`
  - `music/zombies_defeat.ogg`
  - `music/wendigo.ogg`
- Sound-channel sources:
  - `sound/chaosx_super_event_default.wav`
  - `sound/chaosx_super_event_zombies.wav`
  - `sound/chaosx_super_event_zombies_defeat.wav`
  - `sound/chaosx_super_event_wendigo.wav`

If custom art is later desired for the Miscellaneous menu or sync controls:
- Put textures in `gfx/interface/`
- Register sprites in the existing Chaos Redux GFX file used for settings assets
- Keep names stable under a `chaosx_settings_*` or `chaosx_tag_management_*` pattern

## Future plans
- Replace the selected-country/state sync buttons with a true automatic map-selection hook if Paradox exposes a documented callback for selection changes in scripted GUI.
- Register per-ID definitions for any newly-added super events as soon as they start using `super_event_visible`, so the dynamic audio builder can resolve them immediately.
- Add a live preview button for super-event audio mode and loudness testing inside the Miscellaneous panel.
