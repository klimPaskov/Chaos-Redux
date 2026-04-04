# Chaos Meter Deaths And Events Log UI

## Overview

This note documents the deaths-tab and events-log UI adjustments made for the current Chaos Redux interface pass.

The deaths tab now:

- Rebuilds total population from the live `state_population_k` dynamic variable so the displayed world population stays in a safe thousands-based aggregate and avoids world-total overflow.
- Builds the country list from logged death recipients instead of scanning every country blindly.
- Supports three sort modes: recent update, total filtered deaths, and country order.
- Stores deaths log timestamps as `global.date`, which keeps the date formatter working in localisation.
- Opens a larger per-country details overlay with its own filter, sort mode, and sort order controls.

The events log popup now:

- Closes the separate event-details popup whenever tabs are switched.
- Restricts that popup to the Events tab only.
- Keeps the History tab focused on its click-open history details overlay for fired events.
- Uses a dedicated top-level History details window instead of relying on a permanently nested panel.
- Anchors the History details window to the events-log popup shell and centers it over that window instead of the screen.
- Gives History rows a full-width click target while keeping the actor diplomacy button layered on top.
- Styles the History details window like the borderless event-details panel instead of the bordered evolution panel.
- Colors positive fired counts in the Events tab red instead of green so already-fired events read as spent/used rather than available.

## Step By Step

1. Opening the deaths tab rebuilds the current world population from a thousands-based state aggregate and then rebuilds the grouped deaths rows.
2. Logged death entries with a valid target country are collected into a unique-country working list.
3. Each country row aggregates total, civilian, military, and latest matching entry data from the deaths country cache, and the view now drains any pending cache backfill before it repopulates the visible rows.
4. Automatic open-tab refreshes from newly registered deaths now update only the affected country row in place instead of rebuilding the full visible list, so the deaths entries stay visible while the game is running.
5. Country-scoped military hovers now use the vanilla `CASUALTY` tooltip, so the wars-view opponent casualty breakdown is reused directly on the deaths rows.
6. Death values below 1,000 now use whole-number integer formatting in the UI instead of showing a trailing decimal.
7. The grouped rows are sorted by the selected mode and order, then pushed into the view arrays used by the scripted GUI.
8. Clicking a deaths row or a history/evolution row now writes selection state back to the player scope even when the list entry itself is using `change_scope = yes`.
9. The deaths details overlay rebuilds its own filtered and sorted entry list for the selected country without depending on the main deaths-tab sort controls.
10. Opening the events log popup starts on History, but the standalone event-details popup stays closed until an Events-tab row is clicked.
11. Switching away from a tab clears stale details windows so only the relevant panel remains visible.

## Interaction With Existing Systems

- Death totals still come from the existing deaths registration pipeline in `common/scripted_effects/chaos_meter_effects.txt`.
- History-tab event details still use `events_log_rebuild_history_details_view`.
- Events-tab metadata still uses `events_log_rebuild_open_event_details_view`.
- No new on_actions, decisions, or gameplay modifiers were added.

## Icons

No new sprites are required for this pass.

Existing wired assets already used by these views:

- `GFX_chaosx_arrow_left`
- `GFX_chaosx_arrow_right`
- `GFX_closebutton_small`
- `GFX_mini_tooltip`
- `GFX_diplo_countrylist_flag_frame`
- `GFX_flag_small2`
- `GFX_chaosx_button_123x34_vanilla`
- `GFX_sort_button_100x29`
- `GFX_chaosx_sort_button_100x29_2`

## Future Plans

- If the deaths details panel needs richer attribution later, add explicit per-country cached totals for faster rebuilds.
- If actor ordering needs to be more human-readable, replace the current deterministic country-order sort with a dedicated alphabetical country-index cache.
