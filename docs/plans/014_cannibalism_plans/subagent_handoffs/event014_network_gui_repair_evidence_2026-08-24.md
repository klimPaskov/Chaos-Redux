# Event 014 Cannibalism network GUI hitbox verification

Review date: 2026-08-24.

## Result

The reported selector syntax defect is stale in the current source.

Both Event 014 network entry selectors already use the verified HOI4 `buttonType` vector form `size = { x = ... y = ... }`.

Changing these buttons to `size = { width = ... height = ... }` would contradict the installed vanilla precedent and recreate the malformed `width` and `height` token failure described by the earlier audit.

No GUI source rewrite was applied.

The required multi-state and multi-resolution MCP evidence remains incomplete because the renderer timed out or returned only one bounded 1920x1080 artifact.

This handoff does not claim visual or engine completion.

## Event ownership and scope proof

Event ID and slug: `014_cannibalism`.

The dedicated window is `cannibalism_network_window` in `interface/014_cannibalism_frontline_hunger.gui`.

The owning binding is `cannibalism_network_scripted_gui` in `common/scripted_guis/014_cannibalism_scripted_gui.txt`.

That binding uses `context_type = player_context`, `parent_window_token = top_bar`, and `window_name = "cannibalism_network_window"`.

The Event 014 early header opens the window through `cannibalism_network_open`, which calls `cannibalism_gui_open_network_view`.

The two reviewed controls are `cannibalism_network_country_entry_select` and `cannibalism_network_state_entry_select`.

Their scripted effects are `cannibalism_network_country_entry_select_click` and `cannibalism_network_state_entry_select_click`.

Their click-enabled triggers are the matching `_click_enabled` identifiers, both currently `always = yes` while their dynamic-list rows exist.

The shared event log, Event Details, settings, super-events, registries, decisions, gameplay effects, assets, and the other four Event 014 windows were not modified.

## Exact linked identifiers

| Surface | Identifiers |
| --- | --- |
| GUI layout | `cannibalism_network_window`, `cannibalism_network_country_entry`, `cannibalism_network_state_entry`, `cannibalism_network_country_dynamic_list`, `cannibalism_network_state_dynamic_list` |
| Selector controls | `cannibalism_network_country_entry_select`, `cannibalism_network_state_entry_select` |
| Scripted GUI | `cannibalism_network_scripted_gui` |
| Entry point | `cannibalism_network_open`, `cannibalism_gui_open_network_view`, player context, top bar parent |
| Selection effects | `cannibalism_gui_select_country_entry`, `cannibalism_gui_select_state_entry` |
| GFX registration | `interface/014_cannibalism.gfx` |
| Row and panel sprites | `GFX_cannibalism_network_window_background`, `GFX_cannibalism_network_country_card`, `GFX_cannibalism_network_state_card`, `GFX_cannibalism_network_target_frame`, `GFX_tiled_window_transparent` |
| Supporting sprites | `GFX_cannibalism_network_threads_animated`, `GFX_cannibalism_network_threads_static`, `GFX_cannibalism_island_alert_animated`, `GFX_cannibalism_island_alert_static`, `GFX_cannibalism_selected_target_overlay_animated`, `GFX_cannibalism_selected_target_overlay_static`, `GFX_cannibalism_network_alignment_meter`, `GFX_flag_small2` |
| Localisation family | `cannibalism.gui.network.*`, `cannibalism.gui.tab.*`, `cannibalism.gui.sort`, `cannibalism.gui.refresh`, `cannibalism.gui.close` |
| Asset files | `gfx/interface/014_cannibalism/network_window_background.dds`, `network_country_card.dds`, `network_state_card.dds`, `network_target_frame.dds`, plus the registered Event 014 animated static and sheet DDS files |

## References inspected

Required repository guidance and skills were read from `AGENTS.md`, `.agents/skills/chaos-redux-decisions-missions/SKILL.md`, and `.agents/skills/chaos-redux-events/SKILL.md`.

The offline `Interface modding` and `Scripted GUI modding` wiki pages were consulted together with the required core offline wiki pages.

Installed vanilla documentation was consulted at `common/scripted_guis/_documentation.md` and `documentation/script_concept_documentation.md`.

The exact applicable vanilla precedent is `interface/countryarmyview.gui`, where `filter_button` uses `size = {x=80 y=29}` with `quadTextureSprite = "GFX_tiled_window_transparent"`.

A wider installed-vanilla scan found 126 parsed `buttonType` size declarations using `x` and `y` and no active button precedent using `width` and `height`.

Vanilla `interface/mapicons.gui` also proves that GUI constants are valid inside a button vector through `size = { x=@intel_map_mode_map_icon_box_width y=64 }`.

The earlier Event 014 audit was read from `docs/plans/014_cannibalism_plans/subagent_handoffs/event014_decision_gui_audit_2026-08-24.md`.

## Source verification and behavior

Each dynamic-list slot is 374 by 64 pixels through `@CANNIBALISM_NETWORK_ENTRY_WIDTH` and `@CANNIBALISM_NETWORK_ENTRY_HEIGHT`.

Each entry container is 374 by 64 pixels.

Each transparent selector begins at local position 0,0 and uses the same 374 by 64 `x`,`y` size vector.

The country flag and both row text elements use `alwaysTransparent = yes`, so they do not intentionally intercept the row selector.

The current source therefore maps each visible country or state card to a full-card selector region without changing gameplay or visual design.

The prior audit cited a captured prelaunch log with malformed `width` and `height` tokens near these rows.

Those tokens do not occur in the current button definitions and should not be reintroduced.

Before and after behavior is unchanged because the valid source form was already present before this pass.

## Layout hierarchy

```text
cannibalism_network_window (860x620)
|-- background, title, summary, close
|-- five network tabs, sort, refresh
|-- network thread and island alert presentation
|-- country header
|   `-- country list panel (394x222, clipped)
|       `-- country dynamic list
|           `-- country entry (374x64)
|               |-- full-row transparent selector (374x64)
|               |-- flag
|               `-- text
|-- state header
|   `-- state list panel (394x222, clipped)
|       `-- state dynamic list
|           `-- state entry (374x64)
|               |-- full-row transparent selector (374x64)
|               `-- text
`-- selected-target card, overlay, flag, and text
```

## Background coverage map

| Background region | Intended content | GUI elements | Interaction or state | Status |
| --- | --- | --- | --- | --- |
| Header band | Title, summary, close | title and summary text, close button | normal, hover, disabled where scripted | Existing design preserved |
| Tab band | Network filters and refresh controls | five tabs, sort, refresh | normal, hover, selected, disabled | Existing design preserved |
| Central network field | Animated network and alert presentation | threads and island alert sprites | normal and warning presentation | Existing design preserved |
| Left list well | Country targets | country header, clipped list, country cards | empty, populated, crowded, hover, selected | Selector source bounds match the row |
| Right list well | State targets | state header, clipped list, state cards | empty, populated, crowded, hover, selected | Selector source bounds match the row |
| Lower target frame | Current target summary | target frame, overlay, flag, text | empty and selected | Existing design preserved |

## Value, action, text, and cost budgets

The network window exposes no spendable mechanic value and no gameplay-changing action.

Its selected-target summary is informational, so the visible mechanic-value count is zero and the supporting selection summary count is one.

The two dynamic selector types choose a country or state target and spend no resource.

The window also contains five filter tabs, sort, refresh, and close controls.

Those are navigation and view controls rather than primary gameplay actions, but the count should remain visible to any later full-window design audit.

No cost strings or texticons belong to the two selector controls.

The selector tooltip uses the existing `cannibalism.gui.network.entry.select.tt` localisation key.

No localisation was changed in this bounded pass.

## MCP evidence

### Pre-review inspection

The first `hoi4.gui_inspect` attempt used unsupported scenario keys and returned input validation error `-32602` because `scenario.scriptedGui` expected a record and `sourceFiles`, `identifiers`, `entryPoint`, and `scopeLimit` were unrecognized.

The corrected call used `windowName = cannibalism_network_window` and scenario `event014_network_hitbox_pre_2026_08_24`.

It completed with code `GUI_INSPECTED` in workspace `mod_chaos_redux_ea3b2d67c2c0`.

Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e2cf69dd308c3d8f82edf75c3c7e40113774113f8ace97ce21aa492f5715f7d5/123a3ab6485197b608d3600052f17cb59916a63ceb87b4e434a01ba8450c8074/gui-inspect.418adc0dfb6f7e8d.json`.

The inspection resolved 27 elements for the named network window.

Its global source graph was not a clean acceptance result because diagnostics were truncated at the fixed 2000-entry ceiling.

The omitted diagnostics included one `GUI_CLICK_BOUNDS_MISMATCH`, but the truncated response did not retain a path or element that could attribute that finding to either Event 014 selector.

### Pre-review rendering

The matrix call requested normal, hover, selected, disabled, warning, empty-list, full-list, and long-text at 1366x768, 1600x900, 1920x1080, and 2560x1440.

It returned code `GUI_RENDERED` with one 1920x1080 full-window SVG and `MCP_RESPONSE_TRUNCATED`.

Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/40cfb5508bb2c3917099dda1c792b23e57108c299e4e0861d0e778b0ad8a2970/23982d86c9e9432c931bc6911bf22ed7698a6a1228c1dfb0c11cedaa0ff2ea5d/cannibalism_network_window-full.svg`.

The returned SVG records offline approximations for font glyphs and animated sprite frames.

It does not provide a complete state or resolution matrix.

A parallel four-resolution retry produced no output after more than four minutes and was terminated.

An isolated normal-state retry for 1366x768 timed out awaiting `tools/call` after 180 seconds.

### Post-review inspection

The post-review call used scenario `event014_network_post_source_verification_2026_08_24` and recorded that no source rewrite was applied.

It completed with code `GUI_INSPECTED` and again resolved 27 elements.

Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4de35a53d4ea6267adad3dc3c3445bbc4caaa856c60ea67f50eb8ec644b5bc55/76a7f6fce185a0136a2ef9f788e9589a08b909a767ece279ec6ee6343623b06b/gui-inspect.e1c124f2a3f144e2.json`.

The post-review graph has the same global truncation limitation and cannot isolate the one omitted click-bounds diagnostic.

### Rewrite and comparison disposition

`hoi4.gui_rewrite` was not called because the current selectors already match the verified vanilla form and no MCP diagnostic retained an Event 014 selector-specific rewrite recommendation.

A rewrite from `x`,`y` to `width`,`height` would be an unsafe regression.

No before-and-after comparison exists because no source change was justified.

## State and resolution matrix

| View | 1366x768 | 1600x900 | 1920x1080 | 2560x1440 |
| --- | --- | --- | --- | --- |
| Normal | Timed out after 180 seconds | Requested but no artifact returned | Full-window SVG returned | Requested but no artifact returned |
| Hover | Requested but no distinct artifact returned | Requested but no distinct artifact returned | Requested but no distinct artifact returned | Requested but no distinct artifact returned |
| Selected | Requested but no distinct artifact returned | Requested but no distinct artifact returned | Requested but no distinct artifact returned | Requested but no distinct artifact returned |
| Disabled | Requested but no distinct artifact returned | Requested but no distinct artifact returned | Requested but no distinct artifact returned | Requested but no distinct artifact returned |
| Warning | Requested but no distinct artifact returned | Requested but no distinct artifact returned | Requested but no distinct artifact returned | Requested but no distinct artifact returned |
| Empty list | Requested but no distinct artifact returned | Requested but no distinct artifact returned | Requested but no distinct artifact returned | Requested but no distinct artifact returned |
| Crowded list | Requested as `full-list`, no distinct artifact returned | Requested as `full-list`, no distinct artifact returned | Requested as `full-list`, no distinct artifact returned | Requested as `full-list`, no distinct artifact returned |
| Long text | Requested but no distinct artifact returned | Requested but no distinct artifact returned | Requested but no distinct artifact returned | Requested but no distinct artifact returned |

Active and completed states do not apply to these view-only target selectors.

## Files changed

Only this handoff was added by this worker.

`interface/014_cannibalism_frontline_hunger.gui` already contained the verified selector form and was not edited by this worker.

That interface file had unrelated concurrent changes to the counter tab, sort, and refresh positions before this pass.

Those concurrent changes were preserved and were not staged or reverted.

## Remaining parent-owned work and blockers

The parent still owns live consumer and in-game validation.

The MCP must produce isolated state, hierarchy, click-region, clipping, overlap, and four-resolution evidence before the Event 014 network window can receive a visual completion claim.

The single omitted `GUI_CLICK_BOUNDS_MISMATCH` in the globally truncated inspect graph must be attributed to an exact element before it can be accepted or repaired.

No missing asset was discovered in the bounded selector source review, but the offline renderer approximated animated frames and fonts.

No gameplay, balance, AI, cost, localisation, or asset change was made.

No simplification or fallback was introduced.

The evidence pass is incomplete only where the MCP failed to return the required state and resolution artifacts.
