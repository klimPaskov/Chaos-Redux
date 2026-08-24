# Event Details World-End Scenario Catalog

## Overview

The Event Details window includes a **World End Scenarios** section below the evolution preview. It is a registered catalog of terminal branches owned by the selected numbered event. Each terminal branch occupies one row, so events with more than one ending keep separate details and separate enable state. The shared registry also stores unnumbered terminal systems with owner event `none`. Those entries retain stable toggle and active-state identities without appearing under an unrelated numbered event.

This document and the live registry are the integration source of truth. They supersede partial implementation handoffs that described only Event 14 entries as public-details ready.

Clicking a row opens a movable scenario-details window. World-end rows use the same 41-pixel spacing as evolution rows. The detail body is inset inside its clipped scroll area, and the full-size 28 by 23 checkbox sprite has a separate label bay so neither surface clips or overlaps. The row and detail view show the scenario title, owner event, current enabled or active state, and player-facing prose describing the premise and terminal campaign state. Registered hidden identities are named like every other entry, but implementation variables, effect lists, and hidden trigger conditions remain absent.

## Registered entries

| Owner event | Scenario | Linked super-event presentation |
|---|---|---|
| Event 2, Zombie Outbreak | Zombie Apocalypse | Zombie Apocalypse |
| Event 3, The Holy Realm | The Final Silence | The Final Silence |
| Event 2, Zombie Outbreak | Wendigo Ascendancy (registered hidden identity) | Wendigo Ascendancy |
| Event 7, Fury | The World in Fury | The World in Fury |
| Event 10, Death | Last Shores | The Census of Zol |
| Event 14, Cannibalism | The World Is the Larder | The World Is the Larder |
| Event 14, Cannibalism | No Thaw Will Come | No Thaw Will Come |
| Event 18, Resources Found | The World Opens Below | The Deep War Crosses the Seas |
| Event 16, Brilliant Scientist | Laboratory World | Laboratory World |
| Event 16, Brilliant Scientist | The Strategic Singularity | The Strategic Singularity |
| Event 20, Black Plague | The Kingdom of Teeth | The Kingdom of Teeth |
| Event 12, Africa Is One | The World Is One | The World |

## Consequence boundary

Fallout is not a registry entry. It has no Event Details row, evolution entry, ordinary event-log entry, owner event, or linked super-event presentation. The Miscellaneous settings panel controls its request gate, and the dedicated `fallout_world_end` system owns its blackout transition. The stable save-facing Fallout token remains an internal request and settings identity only.

Registered hidden terminal identities are appended to the Event Details view with their hidden visibility metadata intact. Registration therefore supplies the same row, checkbox, title, details text, and independent enable state as other catalog entries without changing the source event's natural runtime gates or revealing unrelated systems.

Event 14's two world-end rows are not reveal-gated in Event Details. Their active and available status still follows the live world-end flags, global world-end lock, and per-scenario enable state.

## Registry and rebuild flow

`initialize_world_end_scenario_registry` rebuilds aligned global definition arrays during event-system initialization. The registry stores numeric fields for:

- stable scenario ID;
- owner event ID;
- owner-local sort order;
- public or hidden visibility;
- public-details readiness, which records whether the row package is complete but does not hide a registered identity;
- default-enabled state;
- terminal-flag dispatch ID;
- related super-event display ID;
- title and details text dispatch IDs;
- availability-helper ID.

`events_log_rebuild_event_detail_world_end_scenarios` filters the registry only to the selected owner event, then inserts every matching registered record into aligned view arrays by its owner-local sort value. Visibility and details-readiness remain registry metadata; static flags and localisation keys are resolved through explicit scenario-ID dispatch because Clausewitz arrays store numeric values rather than script tokens or localisation-key strings.

The selected details state is stored on the player country. Scripted GUI row indices remain temporary unscoped values, and no event target is used by the GUI.

## Enable and disable behavior

The persistent `global.disabled_world_end_scenarios` array records independently disabled scenario IDs. Reopening or rebuilding Event Details does not clear it.

The checkbox changes only the selected terminal branch:

- it does not disable the owner event;
- it does not change sibling terminal branches;
- it does not change evolution toggles;
- it does not clear a world end that has already begun.

Natural terminal paths retain their existing scenario-specific helpers and world-state, Chaos, route, and super-event conditions. The Event Details checkbox continues to store independent scenario state without changing sibling branches or manually launched Triggerable Scenario contracts.

## Files and interaction surfaces

- Registry, row rebuild, selection, active-state dispatch, and toggle effects: `common/scripted_effects/chaosx_events_log_effects.txt`
- Stable registry tuning: `common/script_constants/world_end_scenario_registry_constants.txt`
- Automatic-selection gates: `common/scripted_triggers/chaosx_world_end_scenario_triggers.txt`
- Fallout request, toggle, transition, and blackout dispatch: `common/scripted_effects/fallout_world_end_effects.txt`
- Fallout event namespace and transition events: `events/fallout_world_end_events.txt`
- Scripted GUI row, toggle, click, and detail-window handlers: `common/scripted_guis/chaosx_scripted_gui_events_log.txt`
- Event Details and scenario-details layouts: `interface/chaosx_events_log_popup.gui`
- Dynamic titles, owners, statuses, and details: `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`
- Player-facing English text: `localisation/english/chaosx_gui_l_english.yml`
- Public catalog wording: `docs/spreadsheets/chaos_redux_events_catalog.xlsx`. Each workbook entry retains the complete scenario description. A title may separate multiple branches in one event row, but it never replaces the description body.

## Icons and UI assets

No new art is required.

- Row background: existing `GFX_chaosx_chaos_meter_entry`
- Enabled checkbox: existing `GFX_chaosx_checkbox_checked`
- Disabled checkbox: existing `GFX_chaosx_checkbox_unchecked`
- Window background and close button: existing tiled window and close-button sprites
- Layout registration: `interface/chaosx_events_log_popup.gui`
- Sprite definitions: existing Chaos Redux interface GFX files; no additional `.gfx` registration is needed

## Future plans

- Add authored availability helpers only where a public status can be explained without revealing secret prerequisites.
- Add optional super-event artwork thumbnails if the Event Details window gains a shared, spoiler-safe image contract.
- Keep consequence transitions outside this catalog. Add a separate presentation surface only if a future terminal system receives an approved player-facing catalog contract.
