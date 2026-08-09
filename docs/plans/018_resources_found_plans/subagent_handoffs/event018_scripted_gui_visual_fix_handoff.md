# Event 018 scripted GUI visual-fix handoff

## Ownership and scope

This handoff covers only the dedicated scripted GUI introduced by Event 018 Resources Found.

- Event: `018_resources_found`.
- Decision category: `resources_found_field_management_category` in `common/decisions/categories/018_resources_found_categories.txt`.
- Category entry point: `scripted_gui = resources_found_field_scripted_gui`.
- Scripted GUI: `resources_found_field_scripted_gui` in `common/scripted_guis/018_resources_found_scripted_gui.txt`.
- Window: `resources_found_field_window`.
- Background: `GFX_018_resource_field_panel`, `gfx/interface/018_resources_found/resource_field_panel.dds`.

The category entry and scripted GUI are event-owned, player-only, and are not part of the shared event log, event-details window, settings UI, or super-event framework.

## Files changed by the parent implementation

- `interface/018_resources_found.gui`.
- `interface/018_resources_found.gfx`.
- `common/scripted_effects/018_resources_found_ui_effects.txt`.
- `localisation/english/018_resources_found_system_l_english.yml`.

`common/scripted_guis/018_resources_found_scripted_gui.txt` was audited but its gameplay and visibility semantics were left unchanged.

The display-only helper `resources_found_gui_update_display_position` copies the zero-based `resources_found_gui_selected_index`, adds one for display, and clears the display variable when the list is empty. It does not alter field selection or gameplay outcomes.

## Baseline defects

The baseline used five scaled controls with source positions outside the 470x304 root. Labels were not centered in their painted wells, click boxes did not match the visible controls, rows and dynamic text collided, the right-side seal was covered by status text, and all five controls were squeezed onto art with four actual wells.

Baseline cropped reference supplied by the parent: `C:/Users/klimp/AppData/Local/hoi4-agent-tools/workspaces/mod_chaos_redux_ea3b2d67c2c0/artifacts/f6/f69f5dce32ff81683ebaa1ff8cb3b06ebaf39fa1137c6c4b0018fa021a5ae9d4/resources_found_field_window-cropped.png`.

## Layout and background coverage

The final root remains 470x304 with clipping enabled.

- Header title is centered in `x=24..272`, `y=7..27` using `hoi_18mbs`, keeping the full native glyph box inside the engraved top rail.
- Active and closed headers use the same centered `x=24..272`, `y=28..66` two-line band, with short `Field`/`Sealed` prefixes and the active one-based position in the active state.
- Both active and closed content containers are `x=16..454`, `y=72..252`, `438x180`, clipped independently.
- Left content stays in `x=24..272`. The compact summary is at local `y=2`, the four metric lines occupy local `y=22..88`, conditional Disturbance and Breach rows occupy local `y=92..110` and `y=112..130`, and the dedicated status band occupies local `y=132..180`.
- The 128x128 state art starts at root `x=306`, `y=72` and ends at `x=434`, `y=200`, leaving the status band clear of the seal aperture.
- Navigation arrows occupy the first painted well at `x=31` and `x=89`, `y=265`, using 16x16 sprites. The active position/count is shown in the compact header so no fifth bottom well is invented.
- The three remaining painted wells use unscaled 100x29 two-frame controls at `x=128`, `x=239`, and `x=350`, `y=258`, for Show State, Animation, and History (`goto`, `animation`, and `history` identifiers respectively).
- No `scale` property remains in the owned GUI. All labels use native button text with `format = center` and frame 2 for the action controls.

## State matrix and visibility semantics

| State or probe | Visible content | Expected art and rows |
| --- | --- | --- |
| Active baseline | Active header and active container | Seal or unsafe art; four core values; conditional rows hidden until revealed |
| Unsafe/high pressure | Active header and active container | Unsafe art selected by the existing safety trigger; rows remain bounded |
| Evolution II disturbance | Active header and active container | Disturbance row and disturbance art become visible; breach remains gated |
| Evolution III breach | Active header and active container | Breach row and breach art become visible; status remains in the left band |
| Sealing | Active header and active container | Sealing art replaces other state art; existing full-seal trigger is preserved |
| Suspended | Active header and active container | Suspended art; disturbance and breach rows stay hidden by existing suspended semantics |
| Closed/history | Closed header and closed container | Closed art, reversed compact ledger, closed values/status, and history control |
| Hover/disabled | Same state-specific ancestor | Scripted GUI enabled triggers remain authoritative; arrow and native two-frame action sprites provide hover/disabled treatment |

The active and closed containers are separate and their scripted-GUI visibility triggers are mutually exclusive in runtime. The offline inspector can still model both branches in one graph, which is why its global overlap check is not treated as an Event 018 runtime overlap.

## Value and localisation budget

The compact on-panel summary keeps the left column readable. `resources_found.gui.resources.tt` and `resources_found.gui.closed_resources.tt` retain all six dynamic resource amounts, totals, and the explanatory distinction between Event 018 additions and the full state total. Developed Yield, Excavation Depth, Workforce Safety, Foreign Pressure, Disturbance, and Breach remain individually bounded rows with existing tooltips.

Static font/width evidence from the final source review:

- Panel: 470x304.
- `hoi_18mbs` title uses a native 18 px line height inside the 248x20 title bound.
- Long tested closed header (`Sealed: Equatorial Guinea and Sao Tome`): 234/248 px.
- Long tested active header: 224/248 px.
- Nine-digit compact summary: 221/248 px.
- Longest threshold row (`Subsurface Disturbance 100 Anomalous`): 230/248 px.
- Action sheet: 200x29 DDS with two frames, yielding 100x29 controls.
- Arrow sprites: 16x16 each.

## MCP evidence

### Baseline artifacts

Baseline `hoi4.gui_inspect` succeeded for `resources_found_field_window` under scenario `event018_resources_found`.

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d9ddd41b9f668f2300dfa54c173df9b32cf37682586b8188b967ffbf52e75fb5/a2f7b68bcf4599a9ed0dcba7cc9436d44366227d2a758da9327775b1052d5d08/gui-inspect.b93e9b1caad064c3.json`

Baseline `hoi4.gui_render` succeeded with the requested normal, hover, selected, disabled, warning, active, completed, empty-list, full-list, minimum-value, maximum-value, long-text, and missing-localisation probes at 1280x720, 1366x768, 1920x1080, and 2560x1440 at UI scale 1.0. Its full, cropped, annotated, click-region, hierarchy, state-matrix, resolution-scale, source-map, validation, fidelity, and comparison artifact URIs were returned by the MCP call. The primary baseline full artifact was:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7e20c2ceaf232650cd7923402756cb6556d30d8d070ca85f9223e81ad1c29a4d/35252ad6bb8d00fc50392d45784ff4ed39c7b669d438b85479c04e70dfbc6ad7/resources_found_field_window-full.svg`

### Interim post-change artifact

An interim post-change full SVG existed before the final vanilla-pattern GFX, font, bounds, and localisation corrections. It must not be used as final-revision proof:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/be23d336d793f50faa0aa920cf650dc0f6c81101df75b7c43a932c7d7847d9c3/e7f1c5e337e3c142b8a68751c189e29f010c57e0aa17fd6218036be0985d7b31/resources_found_field_window-full.svg`

An interim post-change inspect also completed before the final edits:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9cad4e37b72ae4c58968e69c1dfffc20754b5bfb2477c7323c9f23208a1d8fc4/eacf5192306a6ec6a9e2acfc9c320e2c99a4b8bd405420f10088954adf817f7f/gui-inspect.3fd2616a001f58a7.json`

That inspect reported 34 Event 018 elements and correctly resolved the revised left/right geometry, but its global graph contained unrelated repository diagnostics and it predates the final corrections.

### Final-revision MCP evidence

A final `hoi4.gui_inspect` completed after the title, bounds, sprites, tooltips, and four-well control layout were settled. It inspected all 34 Event 018 elements with a complete source graph and no Event 018-local diagnostic returned inline:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/af65f01433f093d8e876c1a6acb462a7c5b98e7194d5243ea7d2b51619e39121/8865916154548f3bbebe8c7d748681c3f4a068e1ee9f2433a2ae3db9694e973b/gui-inspect.07ea06f0b395f66c.json`

The final inspect reported no text overflow, no child outside a clipped parent, no click-bounds mismatch, no invisible or conflicting click region, no missing sprite, texture, font, or localisation, no resolution drift, and no missing button effect or trigger. Its failed headline validation is repository-global: the full GUI source graph retained 2,000 unrelated blocking diagnostics before the Event 018 projection, while the Event 018 render itself returned no local blocker. The offline renderer also cannot infer the country-flag toggle pairing between the five animated sprites and their five named static alternatives, although both sides are explicitly registered and gated in the scripted GUI.

The final active maximum-content render used realistic longest English field/status values, explicit runtime-exclusive visibility, all interactive button states, and the supported 1280x720, 1366x768, 1920x1080, and 2560x1440 resolution probes. It completed with `GUI_RENDERED`; its sole warning was response-wire truncation because the linked SVG exceeded the inline result budget:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5c43cdb1bdae94790dd1a56ecf96fb772a3622ba65a87fe01787a907b6b6e81b/c21ccb6ec66cb82ac34db23852951e08a7fe7bd2b6f9d8298abbacf01ed6c38d/resources_found_field_window-full.svg`

Dedicated final state renders also completed for the condition-specific surfaces:

- Evolution II disturbance: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f22f22b44e3d664502459ddaaa2cbbb2eabe36270522e8073796fb4fd9d0f2b8/2a1b01a40241fe9fdc2a0272cd202715d21ce90cc56e09a4889893c975751859/resources_found_field_window-full.svg`.
- Full sealing: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/01db343073f597dd17e961220e28dadb1784e979f471ba19f63fe3e9d3201953/44817f53396febff755e607573b0d0361bf29731b73c65e40abe91b23bf59032/resources_found_field_window-full.svg`.
- Suspended field: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6f6c49589dee7a4adcad42c0964fab197ca5a2e8d13224a4d1f07e5f8c3797ba/806c89d58e2cf9ff38f21c7c3232966f405181d2fa7db2bdc88a2cc1890cf955/resources_found_field_window-full.svg`.
- Exact-seal history: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/28ce774794195a6506c6687e47d0de3761c183705486f9d2d2a3f5bd6ea142ea/8f7aa55aa1963460becd4b3c5fbbe99d81235363ba0baea54a3af1be8282ae64/resources_found_field_window-full.svg`.

The MCP places an `OFFLINE APPROXIMATION - NOT HOI4` banner over the top rail in rendered evidence. That review watermark is not part of the game GUI and is why the final title is partially obscured in the SVG even though its native 18 px glyph box is wholly within `y=7..27`.

## Rewrite adapter result

The required `hoi4.gui_rewrite` route was attempted against the owned GUI. Source mode was rejected by input validation with `patch fields are accepted only in patches mode`; patches mode first required an expected source hash and then rejected the bounded multi-line replacement with `GUI_UNSAFE_PATCH_RANGE`. A corrected scalar-range attempt did not produce a rewrite artifact before the adapter call timed out/interrupted. The parent applied the reviewed bounded source patch through the normal repository edit path and retained this exact adapter limitation for review.

## Remaining risks and blockers

- The offline inspector's repository-global overlap and unresolved-reference diagnostics include unrelated GUI files and can model both mutually exclusive Event 018 containers together when their child visibility is not mocked explicitly. Every final Event 018 render used explicit active/history and art-state visibility.
- The MCP cannot display native scripted-localisation results without scenario overrides. Final renders therefore used concrete maximum-length English values matching the live keys and thresholds.
- In-game visual and interaction behavior remains outside agent validation; no Hearts of Iron IV runtime was launched.

No gameplay costs, effects, balance, AI, decision outcomes, or shared interfaces were changed by this UI pass.
