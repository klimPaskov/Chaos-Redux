# Event 033 Acid Rain GUI Handoff

## Status

The bounded Event 033 source UI is implemented in the three parent-approved source files and is ready for parent integration review.

The source-level layout, stable identifiers, read-only scripted-GUI contract, and final-asset registrations are complete.

Engine-backed visual completion remains unresolved because the final Event 033 DDS files are not present and the post-anchor GUI render and rewrite routes timed out at the MCP 180-second limit.

No in-game completion claim is made.

## Event ownership and entry point

Event 033 is the Acid Rain event owned by `chaosx.nr33.1`, confirmed at `events/033_acid_rain.txt:23`.

The accepted Event 033 Part 6 specification assigns the bounded world footprint and preparedness surface to this event, and the decision GUI prompt assigns its presentation surface to the Acid Rain decision category while keeping decisions as the action surface.

The existing category entry at `common/decisions/categories/033_acid_rain_categories.txt:27` is `scripted_gui = acid_rain_decisions_scripted_gui` under `chaosx_acid_rain_decision_category`.

That stable scripted-GUI identifier is preserved, and its `window_name` now resolves to the dedicated `acid_rain_world_window` instead of the old prototype container.

No category, event, shared window, event log, event details framework, decision, gameplay effect, or localisation file was edited.

## Changed paths

- `interface/033_acid_rain.gui`
- `interface/033_acid_rain.gfx`
- `common/scripted_guis/033_acid_rain_scripted_guis.txt`
- `docs/plans/033_acid_rain_plans/subagent_handoffs/033_acid_rain_event_ui_handoff.md`

## Exact identifiers

The dedicated GUI root is `acid_rain_world_window`.

The stable scripted-GUI id is `acid_rain_decisions_scripted_gui` with `context_type = decision_category` and `window_name = "acid_rain_world_window"`.

The bounded GUI element names are `acid_rain_world_title`, `acid_rain_world_phase`, `acid_rain_world_global_ledger`, `acid_rain_world_close`, `acid_rain_map_panel`, `acid_rain_front_stack`, `acid_rain_front_card_1`, `acid_rain_front_card_2`, `acid_rain_front_card_3`, `acid_rain_global_card`, `acid_rain_empty_card`, `acid_rain_coverage_panel`, `acid_rain_coverage_frame`, `acid_rain_region_row_1` through `acid_rain_region_row_7`, `acid_rain_region_completed_1` through `acid_rain_region_completed_7`, `acid_rain_national_strip`, `acid_rain_preparedness_badge`, `acid_rain_preparedness_value`, `acid_rain_preparedness_component_pip_1` through `acid_rain_preparedness_component_pip_4`, `acid_rain_world_refresh`, and `acid_rain_world_read_only_hint`.

The map layer element names are `acid_rain_map_base`, `acid_rain_map_region_overlay_1` through `acid_rain_map_region_overlay_7`, `acid_rain_map_visited_veil`, `acid_rain_map_ordinary_veil`, `acid_rain_map_warning_veil`, and `acid_rain_map_global_veil`.

The map marker element names are `acid_rain_map_front_1_marker`, `acid_rain_map_front_1_warning_marker`, `acid_rain_map_front_1_severe_marker`, and the corresponding `_front_2_` and `_front_3_` names.

The card marker element names are `acid_rain_front_card_1_marker`, `acid_rain_front_card_1_warning_marker`, `acid_rain_front_card_1_severe_marker`, and the corresponding `_card_2_` and `_card_3_` names.

The global list element names are `acid_rain_global_superstorm_1`, `acid_rain_global_superstorm_2`, and `acid_rain_global_superstorm_3`.

The coverage fill elements are `acid_rain_coverage_fill_1` through `acid_rain_coverage_fill_10`.

The exact Event 033 sprite registrations are `GFX_acid_rain_map_base`, `GFX_acid_rain_region_overlay_1` through `GFX_acid_rain_region_overlay_7`, `GFX_acid_rain_visited_veil`, `GFX_acid_rain_warning_veil`, `GFX_acid_rain_ordinary_veil`, `GFX_acid_rain_global_veil`, `GFX_acid_rain_front_marker`, `GFX_acid_rain_warning_marker`, `GFX_acid_rain_severe_marker`, `GFX_acid_rain_card_background`, `GFX_acid_rain_coverage_frame`, `GFX_acid_rain_coverage_fill`, `GFX_acid_rain_preparedness_badge`, and `GFX_acid_rain_component_pip`.

The only scripted-GUI effect is `acid_rain_world_refresh_click`, which calls `acid_rain_gui_refresh_read_only = yes`.

The refresh trigger is `acid_rain_world_refresh_click_enabled`, and the close trigger is `acid_rain_world_close_click_enabled`.

The scripted-GUI presentation visibility families are `global.acid_rain_gui_window_visible`, `global.acid_rain_gui_region_1_visible` through `global.acid_rain_gui_region_7_visible`, `global.acid_rain_gui_region_1_completed` through `global.acid_rain_gui_region_7_completed`, `global.acid_rain_gui_visited_layer_active`, `global.acid_rain_gui_ordinary_layer_active`, `global.acid_rain_gui_warning_layer_active`, `global.acid_rain_gui_global_layer_active`, `global.acid_rain_gui_front_1_visible` through `global.acid_rain_gui_front_3_visible`, `global.acid_rain_gui_front_1_warning` through `global.acid_rain_gui_front_3_warning`, `global.acid_rain_gui_front_1_severe` through `global.acid_rain_gui_front_3_severe`, `global.acid_rain_gui_superstorm_1_visible` through `global.acid_rain_gui_superstorm_3_visible`, `global.acid_rain_gui_coverage_percent`, and `global.acid_rain_gui_refresh_enabled`.

The scripted-GUI property frame variables are `acid_rain_gui_component_1_tier`, `acid_rain_gui_component_2_tier`, `acid_rain_gui_component_3_tier`, and `acid_rain_gui_component_4_tier`.

The GUI reads the global presentation values `global.acid_rain_gui_phase`, `global.acid_rain_gui_current_air_contamination_bp`, `global.acid_rain_gui_lifetime_air_added_bp`, `global.acid_rain_gui_air_allowance_remaining_bp`, `global.acid_rain_gui_global_deaths`, `global.acid_rain_gui_coverage_percent`, `global.acid_rain_gui_coverage_touched`, `global.acid_rain_gui_coverage_eligible`, `global.acid_rain_gui_region_1_touched` through `global.acid_rain_gui_region_7_touched`, `global.acid_rain_gui_region_1_eligible` through `global.acid_rain_gui_region_7_eligible`, `global.acid_rain_gui_front_1_id` through `global.acid_rain_gui_front_3_id`, `global.acid_rain_gui_front_1_region` through `global.acid_rain_gui_front_3_region`, `global.acid_rain_gui_front_1_intensity` through `global.acid_rain_gui_front_3_intensity`, `global.acid_rain_gui_front_1_active_states` through `global.acid_rain_gui_front_3_active_states`, `global.acid_rain_gui_front_1_movement_days` through `global.acid_rain_gui_front_3_movement_days`, `global.acid_rain_gui_front_1_next_region` through `global.acid_rain_gui_front_3_next_region`, `global.acid_rain_gui_front_1_severe_state_count` through `global.acid_rain_gui_front_3_severe_state_count`, `global.acid_rain_gui_global_days_since_transition`, `global.acid_rain_gui_global_minimum_remaining_days`, `global.acid_rain_gui_global_next_dissipation_days`, `global.acid_rain_gui_global_superstorm_count`, `global.acid_rain_gui_global_strongest_band`, `global.acid_rain_gui_superstorm_1_name` through `global.acid_rain_gui_superstorm_3_name`, and `global.acid_rain_gui_superstorm_1_band` through `global.acid_rain_gui_superstorm_3_band`.

The national strip reads the country-scoped presentation values `acid_rain_gui_preparedness`, `acid_rain_gui_current_warning_state_count`, `acid_rain_gui_exposed_state_count`, `acid_rain_gui_severe_warning_state_count`, `acid_rain_gui_aftermath_state_count`, `acid_rain_gui_event_deaths`, `acid_rain_gui_deaths_prevented`, and `acid_rain_gui_current_contamination_bp`.

The expected parent-owned tooltip keys are `acid_rain_gui_contamination_tt`, `acid_rain_gui_front_timer_tt`, `acid_rain_gui_severe_cell_tt`, `acid_rain_gui_global_card_tt`, `acid_rain_gui_coverage_tt`, `acid_rain_gui_region_1_tt` through `acid_rain_gui_region_7_tt`, `acid_rain_gui_preparedness_tt`, and `acid_rain_gui_refresh_tt`.

## Layout hierarchy and geometry

The root is a non-moveable, clipped 900x600 `containerWindowType` with `orientation = center`, `origo = upper_left`, and `position = { x = -450 y = -300 }`.

This places the upper-left board corner at `{ x = 510, y = 240 }` on 1920x1080, `{ x = 350, y = 150 }` on 1600x900, and `{ x = 233, y = 84 }` on 1366x768.

The root uses the existing `GFX_tiled_window` background, and all child coordinates are local to the board.

The hierarchy is:

- Root header at local y 10 through 57 with title, phase, four compact global ledger entries, and a vanilla close button.
- `acid_rain_map_panel` at local `{ x = 24, y = 74 }` with size 560x300, map base, seven region overlays, four veils, a compact legend, and three fixed visual marker anchors.
- `acid_rain_front_stack` at local `{ x = 604, y = 74 }` with size 272x300, three 272x86 front cards at local y 25, 119, and 213, plus mutually exclusive global and empty-card presentations.
- `acid_rain_coverage_panel` at local `{ x = 24, y = 390 }` with size 560x110, a ten-segment coverage meter, and seven fixed region rows.
- `acid_rain_national_strip` at local `{ x = 24, y = 508 }` with size 852x44, Preparedness badge and value, four component pips, and compact warning, exposure, severe, aftermath, deaths, prevented, and local-contamination status.
- Footer at local y 560 through 594 with the read-only `acid_rain_world_refresh` button and the action-surface hint.

The map source composition is assumed to be 1672x941 and is rendered at scale 0.335 to approximately 560x315 inside a clipped 560x300 panel.

The three fixed map anchors are local `{ x = 148, y = 130 }`, `{ x = 276, y = 157 }`, and `{ x = 408, y = 112 }` for front slots 1, 2, and 3.

## Background and asset coverage map

| GUI use | Sprite | Expected final path |
| --- | --- | --- |
| Map base | `GFX_acid_rain_map_base` | `gfx/interface/033_acid_rain/gui/acid_rain_map_base.dds` |
| Region masks 1 through 7 | `GFX_acid_rain_region_overlay_1` through `GFX_acid_rain_region_overlay_7` | `gfx/interface/033_acid_rain/gui/acid_rain_region_overlay_1.dds` through `acid_rain_region_overlay_7.dds` |
| Visited map veil | `GFX_acid_rain_visited_veil` | `gfx/interface/033_acid_rain/gui/acid_rain_visited_veil.dds` |
| Ordinary map veil | `GFX_acid_rain_ordinary_veil` | `gfx/interface/033_acid_rain/gui/acid_rain_ordinary_veil.dds` |
| Warning map veil | `GFX_acid_rain_warning_veil` | `gfx/interface/033_acid_rain/gui/acid_rain_warning_veil.dds` |
| Global map veil | `GFX_acid_rain_global_veil` | `gfx/interface/033_acid_rain/gui/acid_rain_global_veil.dds` |
| Ordinary front marker | `GFX_acid_rain_front_marker` | `gfx/interface/033_acid_rain/gui/acid_rain_front_marker.dds` |
| Warning front marker | `GFX_acid_rain_warning_marker` | `gfx/interface/033_acid_rain/gui/acid_rain_warning_marker.dds` |
| Severe front marker | `GFX_acid_rain_severe_marker` | `gfx/interface/033_acid_rain/gui/acid_rain_severe_marker.dds` |
| Front card background | `GFX_acid_rain_card_background` | `gfx/interface/033_acid_rain/gui/acid_rain_card_background.dds` |
| Coverage frame | `GFX_acid_rain_coverage_frame` | `gfx/interface/033_acid_rain/gui/acid_rain_coverage_frame.dds` |
| Coverage segment fill | `GFX_acid_rain_coverage_fill` | `gfx/interface/033_acid_rain/gui/acid_rain_coverage_fill.dds` |
| Preparedness badge | `GFX_acid_rain_preparedness_badge` | `gfx/interface/033_acid_rain/gui/acid_rain_preparedness_badge.dds` |
| Preparedness component pip | `GFX_acid_rain_component_pip` | `gfx/interface/033_acid_rain/gui/acid_rain_component_pip.dds` |

The component pip is registered as a five-frame static strip for tiers 0 through 4.

The existing vanilla `GFX_tiled_window`, `GFX_tiled_window_transparent`, `GFX_closebutton`, `GFX_button_123x34`, and `GFX_checkbox_small` registrations are reused without modification.

## Value, action, text, and cost audit

The active national mechanic value is Preparedness.

Coverage is the single strategic support meter, and the global ledger, front cards, region rows, and national strip provide compact required status and history context rather than additional spendable mechanics or action controls.

The source displays no more than the accepted bounded set of required read-only status summaries and contains no extra meter, tab, target selector, or action tray.

The only visible controls are `acid_rain_world_refresh` and `acid_rain_world_close`.

Refresh calls only the parent-owned read-model helper, and close uses the standard close-button treatment and `ESCAPE` shortcut.

There are zero gameplay-changing controls and zero displayed spendable cost types.

No texticons are required because this surface displays no spendable resource cost.

The map, three front cards, global card, coverage rows, and national strip use short labels, fixed max widths, and bounded line heights so the layout does not depend on paragraph-sized explanatory text.

The GUI currently uses concise literal labels inside the bounded source because the user scope explicitly forbids localisation edits.

## State matrix

| State | Presentation behavior |
| --- | --- |
| Normal | Ordinary veil, current region masks, active front cards, coverage meter, and Preparedness strip read from the projected model. |
| Hover | Vanilla button hover treatment and the parent-owned tooltip keys apply to refresh, close, coverage, front timer, severe cell, global card, region rows, and Preparedness. Decorative map and card elements are click-through. |
| Selected | No map, card, target, or region selection state exists because the surface is read-only. |
| Locked | No active fronts shows the bounded empty card; no gameplay controls are exposed. |
| Disabled | Refresh is enabled only when `global.acid_rain_gui_refresh_enabled` is positive; close remains enabled. |
| Warning | Warning veil, warning front markers, and warning card marker states are mutually exclusive with ordinary and severe marker states. |
| Active | One, two, or three stable front cards are shown in front-id order, with matching map marker state. |
| Completed | Region rows expose a neutral checkbox frame when the corresponding projected completion value is positive. |
| Empty list | The empty card states that no active front is present and waits for the next transition. |
| Full list | The global card exposes a bounded three-row superstorm list when the global layer replaces ordinary fronts. |
| Minimum value | Empty or minimum presentation values leave the meter unfilled and preserve the row and card bounds. |
| Maximum value | Ten coverage segments and the four pip frames can represent the maximum projected tiers without changing geometry. |
| Long text | Front, region, and global text boxes keep fixed widths and heights; parent localisation must remain concise within those bounds. |
| Missing localisation | Expected Event 033 tooltip keys are documented but not added because localisation is outside this worker scope. |

## MCP evidence

The workspace id used for all GUI MCP calls was `mod_chaos_redux_ea3b2d67c2c0`.

### Pre-change inspect

`hoi4.gui_inspect` was run before source edits for selector `windowName = "acid_rain_world_window"` and scenario `{ "id": "event033_acid_rain_baseline" }`.

Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/da50bcbf2f088f05b29db837f0eb5560c3b8c1f4a2ffeec6fb6caa6d888fc7c9/5f83aaaf42188a9be4c06087c7dfc1bd54ca35d0a34b6c178d00f960ad16e3df/gui-inspect.4f659e72dc422253.json`.

The route returned `GUI_INSPECTED`, `complete = true`, `skippedSourceCount = 0`, and `inspectedElementCount = 0`.

The exact GUI-specific finding was `GUI window acid_rain_world_window was not found`, with fidelity counts `{ modelled: 0, approximated: 1, missing: 1 }`.

The route also returned the configuration diagnostic `MCP_INLINE_COLLECTIONS_TRUNCATED` as a blocker and `MCP_INLINE_FILES_TRUNCATED` as an informational diagnostic.

### Pre-change render

`hoi4.gui_render` was run for selector `windowName = "acid_rain_world_window"`, scenario `{ "id": "event033_acid_rain_baseline" }`, resolutions 1920x1080, 1600x900, and 1366x768, and the requested state matrix.

Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7ad50386501e5fae7fb9b5530d437a5667840699197e900d7b06072be7c8bf6c/49a1b38ca265e0ad3552f71d95f891f5dd9f3b1570a89ebf5345e0d902113bd3/acid_rain_world_window-full.svg`.

The route returned `GUI_RENDERED` in offline representation mode, but the full SVG was a 649-byte missing-window placeholder with the exact message `GUI window acid_rain_world_window was not found`.

### Mandatory rewrite attempts before and after source implementation

The required pre-edit source-mode rewrite attempt returned `MCP error -32602: Input validation error: Invalid arguments for tool hoi4.gui_rewrite: source is required in source mode` because the route requires a source payload.

The required pre-edit patches-mode rewrite attempt returned `MCP error -32602: Input validation error: Too small: expected array to have >=1 items at patches; patches and expectedSourceHash are required in patches mode` because an empty patch set is rejected.

After the local source implementation, a source-mode rewrite was attempted with the complete `interface/033_acid_rain.gui` source, selector `windowName = "acid_rain_world_window"`, and scenario `{ "id": "event033_acid_rain_postchange_rewrite" }`.

That route returned `tool call error: tool call failed for hoi4_agent_tools/hoi4.gui_rewrite` followed by `Caused by: timed out awaiting tools/call after 180s`.

No MCP rewrite artifact was returned and no MCP rewrite was applied to the workspace.

### Post-source render evidence before the final anchor correction

`hoi4.gui_render` succeeded after the initial source implementation for scenario `{ "id": "event033_acid_rain_postchange" }`, comparison `{ "id": "event033_acid_rain_baseline" }`, all three required resolutions, and all 14 requested states.

The route returned `GUI_RENDERED` with `artifactCount = 27`, `stateCount = 14`, `resolutionCount = 3`, `offlineRepresentation = true`, and comparison `{ changedPixels: 3759, changedRatio: 0.0018127893518518519 }`.

Representative artifacts are the full view `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c4fdb9725b40e163cbfabca17a8a19f57f1b8004c1c6f32aa19dc19ee529d7e9/b3964576d3da85aa47b84ccc9f2fbb127221e6ae1459a3f96b9e1ae271c08792/acid_rain_world_window-full.svg`, cropped view `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3b7bf7135143e21d8d54e30d904e931e69431a66c774a52f4bff72b6a07f3902/4a6fca2600f8ea2692132ec87fefea7623281466dd3fd1df418dd2d897909a3f/acid_rain_world_window-cropped.svg`, annotated view `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ef4727c5eaff7a15f9015733f7c7bccc3aa2643a2412507f9c8f3ba619a40729/4d8f1a58e5d8743b76c8b3ab2cbbdf44ab38fded449adab8d08cae449879e8e6/acid_rain_world_window-annotated.svg`, click-region view `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/24bf13cd29c4039f3051f1f4d1b779c5a072cddaf5544696abac5b43304496f2/a1ca9df312cef2a33c96a684c9c0e713509d6a19059dcc6389be0c23435e29e7/acid_rain_world_window-click-regions.svg`, hierarchy view `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6d5f29a0f3f48ae6a7fe63f7920b1d187416818be21fa59c29b66410b01eef7f/cb9efb0a61d806cb6f7c619e425d69c06d0fde262e97db72511fff6010318220/acid_rain_world_window-hierarchy.svg`, layout JSON `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6c345f035993683259c853fc4dbaa20947312c21e5afe6ad545f88991c1f780d/f50c8210dd486b71ecf1a7eccdc114edd5669e48d01f0ddf422aba129e03dd39/acid_rain_world_window-layout.json`, resolution-scale view `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5938b0740ae81e42cd17e78bda0356a4330e36f29f4379196d75b938fcfeab9f/062980833ebb5ae69130237fadd0c8d41c41e2d0e1d02eaeaca1f125b804d971/acid_rain_world_window-resolution-scale.svg`, comparison view `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ae861ef936c315cf7890345d52a5aa821485eaf2a28bde9e6c73d9361e86d6ae/c1fe493ec06fb21af80402373a1afa099ab10454e3a650f3ec9c09d5d2a0b275/acid_rain_world_window-comparison.png`, comparison JSON `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bb5abd8c371ec047f01df0d84268ed2f8a7e3132462341bd20c4b844674a97a0/472d56866b3106cae256a4781f75204955dfa7f8519e8d9e6faa535876804172/acid_rain_world_window-comparison.json`, fidelity JSON `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9ba1b85fcffd1d4c3bfd1e178b98fef0d8ee3b9d9a15e50e62b9aa18a482122b/a401776f5601eb7895c4df74f8df8dc80d5bfb817b94dd8e44ef594ffc545f2c/acid_rain_world_window-fidelity.json`, source graph JSON `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/62d7f01a75c699a9f148a92b3956a2b1cd71a45c37c7d014a93482b34f3eb434/b8a0a04faf6ac75212cab3842654e00d580a5a874693dd5c2ab2d50393c72cbd/acid_rain_world_window-source-graph.json`, and validation JSON `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a920cebe27bd4ab8fcd49e70876cad71803959eca218a0c873066702f6b3dd06/02e75e60fa1c75e60c4605b2b5411f9fc763fc259ee305614abe14bf12c6a77c/acid_rain_world_window-validation.json`.

Those artifacts exposed a real layout defect in the first version: the root rectangle was `{ x: 510, y: 240, width: 900, height: 600 }`, while the child positions were interpreted from the screen center, placing the map at approximately `{ x: 984, y: 614 }` and the footer below the canvas.

The render was treated as a source defect, not dismissed as an offline-render discrepancy.

### Post-anchor and post-close-fix inspect evidence

The root was corrected to an explicit centered screen anchor with a top-left local origin by adding `position = { x = -450 y = -300 }`, `orientation = center`, and `origo = upper_left` to the root.

Post-anchor inspect for `windowName = "acid_rain_world_window"` and scenario `{ "id": "event033_acid_rain_postanchor" }` returned `GUI_INSPECTED` with `complete = true`, `inspectedElementCount = 112`, and fidelity counts `{ modelled: 999, approximated: 96, ignored: 29, missing: 1, unsupported: 62, unresolved: 0 }`.

Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5425b4b1472b72d9646122a3e76c3ca1303206f6753bd7c924f321d71752da55/73d8b23ed41c3ed283e183b306101c9be8b5670884342210c0c5cf88ac96f8b6/gui-inspect.0e469d84fd1c5a1a.json`.

After the close-trigger correction, the final post-close-fix inspect for scenario `{ "id": "event033_acid_rain_postclosefix" }` returned `GUI_INSPECTED` with `complete = true`, `inspectedElementCount = 112`, and fidelity counts `{ modelled: 999, approximated: 96, ignored: 29, missing: 1, unsupported: 62, unresolved: 0 }`.

Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7521f4fc5f7b6f72d6e7cb025d13619d028236cab4c392e933ab6bd530563ed2/308b321526a437e3cf5b42d91219c6c4cf9e8da91c3c474d4edced85eab5eb22/gui-inspect.848622df0ce6fce2.json`.

The final inspect source graph parsed successfully, and its `gui-source-graph` validation check passed.

The overall validation remained false because all Event 033 final DDS paths are absent from the workspace, producing `GUI_MISSING_TEXTURE` and `GUI_TEXTURE_UNSUPPORTED` diagnostics, plus the linked-resource truncation diagnostic `MCP_INLINE_COLLECTIONS_TRUNCATED`.

### Post-anchor render blocker

The required post-anchor full render was attempted with selector `windowName = "acid_rain_world_window"`, scenario `{ "id": "event033_acid_rain_postanchor" }`, the three required resolutions, all requested states, and comparison `{ "id": "event033_acid_rain_baseline" }`.

It returned `tool call error: tool call failed for hoi4_agent_tools/hoi4.gui_render` followed by `Caused by: timed out awaiting tools/call after 180s`.

A reduced post-anchor normal-state render was then attempted with selector `windowName = "acid_rain_world_window"`, scenario `{ "id": "event033_acid_rain_postanchor_normal" }`, and the same three resolutions.

It returned the same exact `hoi4.gui_render` 180-second timeout.

A final post-close-fix normal-state render was attempted with selector `windowName = "acid_rain_world_window"`, scenario `{ "id": "event033_acid_rain_postclosefix_render" }`, the same three resolutions, and comparison `{ "id": "event033_acid_rain_baseline" }`.

It returned the same exact `tool call error: tool call failed for hoi4_agent_tools/hoi4.gui_render` and `Caused by: timed out awaiting tools/call after 180s`.

The successful pre-anchor render artifacts therefore provide state, hierarchy, click-region, resolution, and comparison coverage for the source implementation, while the final anchor correction has inspect evidence but no post-correction raster or SVG artifact because the route timed out.

## Precedents and required references inspected

The required repository instructions in `AGENTS.md` were read before editing.

The complete `chaos-redux-decisions-missions`, `chaos-redux-events`, `chaos-redux-event-assets`, and `chaos-redux-frame-animation` skills were read.

All files in `docs/specs/033_acid_rain_specs/` were read, including Part 6 and the decision GUI prompt.

The offline Paradox wiki pages for Interface Modding, Scripted GUI Modding, Graphical Asset Modding, Data Structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event Modding, Decision Modding, Idea Modding, and AI Modding were consulted.

The installed vanilla documentation for script concepts, effects, triggers, modifiers, dynamic variables, localisation formatters, localisation objects, and script math was consulted.

The bounded Chaos Redux Event 025 Expedition Board, Event 018 Resources Found field window, and Event 020 Black Plague Response category window were inspected as exact event-owned GUI precedents.

## Asset and animation assumptions

No DDS, PNG, frame sheet, or other asset file was edited or created by this worker.

The repository contains Event 033 source PNGs under `docs/assets/033_acid_rain/source_png/`, including the map base, seven region overlays, three marker sources, and the visited, warning, ordinary, global, and severe veil sources.

The inspected source compositions are approximately 1672x941 for the map layers and 1254x1254 for marker sources.

The GFX file assumes the final converted DDS package will be installed under `gfx/interface/033_acid_rain/gui/` using the exact paths in the asset coverage table.

No reviewed final frame-sheet output exists in the current workspace, so no `frameAnimatedSpriteType` entry was invented.

The GUI uses static ordinary, warning, and severe marker sprites as the safe fallback, and the handoff remains open for the frame-animation worker if the accepted plan still requires pulsing severe cells or animated warning markers.

## Parent-owned integration and validation

The parent runtime owner must implement or expose `acid_rain_gui_refresh_read_only` and populate the presentation variables listed above.

The read-only helper must project stored Acid Rain state into the presentation variables without scanning targets, selecting targets, advancing timers, repairing state, changing coverage, changing contamination, changing deaths, changing costs, or mutating global gameplay state.

The parent localisation owner must add and validate the tooltip keys listed above and should replace the bounded literal labels with concise localisation if that is required by the final integration policy.

The parent decision owner retains the decision category, decision costs, decision effects, entry visibility, AI behavior, action routing, and all gameplay outcomes.

The parent event-details owner retains any Event 033 Event Details entry and any route that opens this bounded window from Event Details.

The parent asset owner must deliver and install the final DDS files, verify alpha and dimensions, and decide whether an approved real frame-sheet package should replace the static fallback.

The parent must perform live in-game consumer validation; this worker did not launch Hearts of Iron IV.

## Simplifications, omissions, and blockers

- The final Event 033 DDS assets are not present, so MCP source validation reports missing and unsupported textures for the exact registered paths.
- The accepted animated severe or warning treatment is represented by static state-specific marker fallbacks because no reviewed frame-sheet output was available.
- Localisation was intentionally not changed by the explicit user scope, so tooltip keys are parent-owned dependencies and the GUI retains concise literal labels.
- The close control is visually registered and has a standard shortcut and click-enabled trigger, but no scripted close effect was added because the scripted GUI was explicitly restricted to the read-only refresh helper and presentation reads.
- The decision category and Event Details entry points were not edited because they are outside the three owned source files; the existing category attachment is documented above for parent integration.
- The post-anchor and post-close-fix GUI renders were blocked by the exact MCP 180-second timeout recorded above, so the final centered layout has no post-correction visual artifact.
- The required MCP rewrite route was attempted and blocked by the exact source-mode argument error, empty-patch argument error, and final 180-second timeout recorded above; no rewrite was silently substituted.
- MCP inline collection truncation remained present in inspect output, while the linked inspect artifact retained the bulk evidence.

The only source files changed within the implementation scope are the two Event 033 interface files and the Event 033 scripted-GUI file listed at the top of this handoff.
