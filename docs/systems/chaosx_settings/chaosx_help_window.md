# Chaos Redux Help Window

## Purpose

The Help window gives players an in-game reference for Chaos Redux systems with live values from the current campaign.

It is opened from the Settings title row with the help button or through `Ctrl+Shift+H`.

## Behavior

The window is movable and centered when opened. It uses tab buttons to switch the same body panel between:

1. Overview
2. Events
3. Chaos
4. Warfare
5. Controls

The body text is provided by `GetChaosxHelpBody` in `common/scripted_localisation/chaosx_scripted_localisation_settings.txt`. The open and tab effects refresh live values through `update_chaosx_help_live_values`.

Live values include current chaos value and tier, current event timer, dynamic timer range, current timer modifier, fired event counts, fired evolution counts, unfired event counts, cluster counts, and compact death totals.

Help tab buttons use separate idle and active buttons. The active button remains visible with `GFX_chaosx_sort_button_100x29_2` while its tab flag is set.

The Overview tab explains the shared Chaos Meter, weighted event pool, per-player timers, the effective dynamic timer range, manual controls, event logs, and multiplayer behavior. The Events tab explains repeatable, fire once, major, evolution, cluster, and world-end behavior without naming individual events.

The Warfare tab is intentionally split into broad sections for Chaos Warfare, Chemical Warfare, Biological Warfare, and contamination mitigation. It should explain mechanics as systems, not individual unlocks or one-off event content.

## Controls

- Settings help button: `chaosx_help_button`
- Help shortcut: `Ctrl+Shift+H`
- Disable Event System shortcut: `Ctrl+Shift+D`
- Event Timer shortcut: `Ctrl+Shift+T`
- Close button: `ESCAPE`

The always-visible shortcut container is disabled while the Settings window is open so it does not double-toggle against the visible Settings help button.

The Disable Event System shortcut is bound to visible disable buttons in the Trigger Events and Timer System views. The global hidden shortcut is disabled while those visible buttons are active, so the shortcut does not fire twice.

## Files

- `interface/chaosx.gui`
- `interface/chaosx.gfx`
- `common/scripted_guis/chaosx_scripted_gui_settings.txt`
- `common/scripted_effects/chaosx_settings_effects.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_settings.txt`
- `localisation/english/chaosx_gui_l_english.yml`

## Icons And Assets

- Button sprite: `GFX_chaosx_button_help`
- DDS path: `gfx/interface/chaosx_button_help.dds`
- GFX definition: `interface/chaosx.gfx`
- In-game button: `chaosx_help_button` in `interface/chaosx.gui`

The Help window itself uses existing tiled window and tab button sprites.

## Future Plans

- Add more per-country live values when a selected-country context is available.
- Keep the window focused on broad systems and put individual event details in event popups or log detail windows.
