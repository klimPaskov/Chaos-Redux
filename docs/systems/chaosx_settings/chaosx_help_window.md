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

Live values include current chaos value and tier, current event timer, dynamic timer range, current timer modifier, fired event counts, fired evolution counts, unfired event counts, cluster counts, compact death totals, and global air contamination.

Help tab buttons use separate idle and active buttons. The active button remains visible with `GFX_chaosx_sort_button_100x29_2` while its tab flag is set.

The Overview tab explains the shared Chaos Meter, weighted event pool, per-player timers, the effective dynamic timer range, manual controls, event logs, and multiplayer behavior. The Events tab explains repeatable, fire once, major, evolution, cluster, and world-end behavior without naming individual events.

The Chaos tab explains the Chaos Meter and Deaths System together with the global Air Cleanliness ledger, the separate state-level Famine mechanic, the cohort-based Migration mechanic, and the Camp Repression network. It keeps their ownership boundaries explicit: famine may request migration, migration may submit trapped-population food demand, and both famine and camps report verified mortality through the shared Deaths System without duplicating population loss.

The Air Cleanliness summary covers contamination sources, chaos conversion, the 25%, 50%, 75%, and 100% thresholds, Air Winter, the Air Cleanliness Treaty, and the Fallout request boundary. The famine and migration summaries name their three canonical player-facing values, decisions and missions, reports, and dedicated mapmodes. The camp summary points players to the Repression Ledger, country-specific routes, discovery, Condemnation, reform, and dismantlement.

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
